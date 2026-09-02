---
title: Distributed training and deep-learning systems — framework internals (tensors, autograd tapes, operators, kernels, graph vs eager), ML compilers (XLA, TVM, torch.compile/Inductor, Triton — fusion, tiling, schedule search), the memory and compute budget of training, data parallelism and all-reduce (ring/tree, NCCL), ZeRO/FSDP sharding, tensor (Megatron) and pipeline (GPipe/1F1B) parallelism, 3D parallelism and sequence/context parallelism, mixed precision and activation checkpointing, collective communication and interconnects, fault tolerance and checkpointing, and utilization (MFU) accounting
type: concept
section: "6.9"
level: 500
tags: [distributed-training, deep-learning-systems, framework-internals, tensors, autograd, operators, kernels, cudnn, cublas, eager-vs-graph, define-by-run, ml-compilers, xla, tvm, torch-compile, inductor, triton, operator-fusion, tiling, schedule-search, memory-budget, activation-memory, optimizer-state, data-parallelism, all-reduce, ring-all-reduce, nccl, gradient-accumulation, zero, fsdp, sharding, tensor-parallelism, megatron, pipeline-parallelism, gpipe, 1f1b, pipeline-bubble, 3d-parallelism, sequence-parallelism, context-parallelism, expert-parallelism, mixed-precision, activation-checkpointing, gradient-checkpointing, collective-communication, nvlink, infiniband, rdma, fault-tolerance, checkpointing, elastic-training, straggglers, mfu, model-flops-utilization, scaling-efficiency, 10-714, needle]
sources: [ml-systems-and-mlops-texts-courses-and-seminal-papers]
summary: A deep-learning framework is a tensor library with an autograd tape that records operators and replays their vector–Jacobian products (define-by-run in PyTorch; static graphs in TensorFlow 1/JAX-jit), dispatching to vendor kernels (cuBLAS, cuDNN) or compiler-generated ones — XLA, TVM, torch.compile/Inductor and Triton fuse elementwise ops into matmul epilogues, tile loops for the memory hierarchy, and search schedules, because most layers are memory-bound and fusion is the main lever; training memory per parameter in mixed precision is ~16 bytes (bf16 weights and gradients, fp32 master weights and two Adam moments) plus activations that scale with batch × sequence × layers (cut by activation checkpointing), so models beyond one GPU need parallelism: data parallelism replicates the model and all-reduces gradients (ring all-reduce moves 2(N−1)/N of the gradient bytes per worker regardless of worker count; NCCL over NVLink/InfiniBand), ZeRO/FSDP shard optimizer state, gradients and parameters across data-parallel ranks so memory falls with the number of GPUs at the cost of extra all-gathers, tensor parallelism (Megatron) splits each layer's matmuls across GPUs with two all-reduces per transformer layer (needs NVLink bandwidth, so it stays within a node), pipeline parallelism assigns layer ranges to stages and streams micro-batches to hide the bubble (GPipe, 1F1B/interleaved schedules), and 3D parallelism combines them with sequence/context parallelism for long inputs and expert parallelism for MoE; fault tolerance at thousands of GPUs is checkpointing, elastic restarts and straggler handling, and the score that matters is model-FLOPs utilization — the fraction of peak hardware FLOPs the training loop achieves (30–50 % is good) — which the 6ND accounting of scaling laws lets you budget.
---
# Distributed training and deep-learning systems

**In one sentence.** A framework turns a forward function into a tape of kernels and
replays it backward; a compiler fuses and tiles those kernels for the memory hierarchy;
and when the model or batch outgrows one GPU you shard the data, the parameters, the
layers, or the sequence across a cluster — each split trading memory for communication —
and measure success as the fraction of peak FLOPs you actually use.

## Framework internals (10-714; Paszke et al. 2019; Abadi et al. 2016)
**Tensor**: shape, dtype, strides, device, storage (views share storage — transposes are
free, contiguity matters for kernels — [[caches-and-memory-hierarchy]]). **Autograd**: each
differentiable op records its inputs and a backward function on a **tape** (dynamic graph);
`backward()` walks the tape in reverse topological order accumulating gradients
([[deep-learning-basics]]); higher-order grads by taping the backward pass. **Operators**
dispatch by device/dtype to kernels — vendor libraries (**cuBLAS** GEMM, **cuDNN**
convolutions/attention, **NCCL** collectives) or hand-written/generated CUDA
([[gpu-programming-cuda]]); the Python overhead of eager dispatch matters for small ops
(CUDA graphs, or compile). Modules (parameter containers), optimizers (state per parameter),
data loaders (parallel workers, prefetch, pinned memory — the input pipeline is a common
bottleneck), mixed-precision autocast. **TensorFlow 1** built static dataflow graphs then
executed them (optimizable, hard to debug); **PyTorch** chose define-by-run (Pythonic control
flow, easy debugging) and later added tracing/compilation (TorchScript → `torch.compile`);
**JAX** makes the trade explicit — pure functions traced by `jit` into XLA. Building one (the
10-714 `needle` framework: NDArray backend with strides, CPU/CUDA kernels, autograd, modules,
optimizers) is the fastest way to understand the cost of every line of model code.

## ML compilers and kernels (Chen et al. 2018 TVM; XLA; Triton; FlashAttention)
Most non-matmul layers are **memory-bound** ([[roofline-model]]): a LayerNorm or a GELU
reads and writes the whole activation for a handful of FLOPs — so **operator fusion**
(elementwise chains folded into the producer's epilogue, reductions fused with their
consumers) is the biggest win, followed by **layout** choices (NHWC/channels-last, tensor-core
friendly tiles), **tiling** for shared memory/registers, and algorithm selection
(Winograd/implicit-GEMM convs). **XLA** (TF/JAX): graph → HLO → fusion + buffer assignment →
LLVM/PTX; **TVM**: Relay graph IR + tensor-expression schedules (loop tiling, vectorization,
unrolling) with **learned cost models** auto-tuning schedules per device (AutoTVM/Ansor);
**torch.compile**: TorchDynamo captures Python bytecode into FX graphs, **Inductor** emits
**Triton** kernels (a Python DSL for tiled GPU programs — the language in which
FlashAttention-2 and most new kernels are written) and C++/OpenMP for CPU; MLIR as the
shared infrastructure; hardware targets — GPUs, TPUs (systolic arrays), custom NPUs
([[hardware-accelerators]]). Kernel-level algorithms: **FlashAttention** (IO-aware tiling, never
materialize T×T), fused Adam, fused cross-entropy ([[transformers-and-attention]]); profiling
with Nsight/torch.profiler ([[profiling-and-performance]]).

## The budget: memory, compute, and utilization (Scaling-laws FLOP rule; Korthikanti et al. 2022)
Per parameter, mixed-precision Adam training holds bf16 weights (2 B) + bf16 gradients
(2 B) + fp32 master weights (4 B) + two fp32 moments (8 B) = **16 bytes/param** (70 B params →
1.1 TB before activations); **activations** scale as batch × sequence × hidden × layers ×
~34 bytes per token per layer (attention scores extra without FlashAttention) — the
dominant term at long sequence — cut by **activation (gradient) checkpointing** (recompute
in backward: ~30 % more compute, memory ∝ √layers), selective recomputation, and FlashAttention;
KV-cache is inference's analogue ([[llm-inference-and-serving]]). Compute: **6·N·D** FLOPs
for training ([[scaling-laws]]); hardware peak (H100 ≈ 990 TFLOP/s dense bf16); **MFU
(model FLOPs utilization)** = achieved model FLOPs / peak — 40–50 % for well-tuned LLM runs,
lower with small batches, poor overlap, or pipeline bubbles; HFU counts recomputation.
Batch size and the **critical batch size** (beyond which more data-parallel replicas stop
helping — [[neural-network-training]]) set how much parallelism is useful.

## Data parallelism, all-reduce, and ZeRO/FSDP (Goyal et al. 2017; Rajbhandari et al. 2020)
**Data parallel (DDP)**: every worker holds the full model, processes a micro-batch,
**all-reduces** gradients (average), and steps identically. **Ring all-reduce** (reduce-
scatter + all-gather over a ring): each of N workers sends/receives 2(N−1)/N × gradient
bytes — bandwidth-optimal and independent of N; tree/hierarchical variants for latency;
**NCCL** over **NVLink/NVSwitch** (intra-node ~900 GB/s) and **InfiniBand/RoCE with RDMA**
(inter-node ~50–100 GB/s per NIC — [[link-layer-and-lans]], [[distributed-systems-basics]]);
overlap communication with the backward pass by bucketing gradients; **gradient
accumulation** for larger effective batches. Memory doesn't shrink with more GPUs — hence
**ZeRO**: stage 1 shards optimizer state, stage 2 gradients, stage 3 parameters across the
data-parallel group (each rank owns 1/N; parameters are **all-gathered** just-in-time per
layer and freed after — reduce-scatter for gradients); memory per GPU ≈ 16 bytes/param ÷ N +
activations, at ~1.5× the communication of DDP. PyTorch **FSDP** is ZeRO-3 with per-module
wrapping; ZeRO-Offload/Infinity push state to CPU/NVMe. Large-batch training needs LR
scaling/warmup and LAMB/LARS at extremes.

## Tensor, pipeline, and 3D parallelism (Shoeybi et al. 2019; Huang et al. 2019; Narayanan et al. 2021)
**Tensor (model) parallelism**: split a layer's weight matrices across GPUs — Megatron splits
the MLP column-wise then row-wise (one all-reduce), attention by heads (one all-reduce):
two all-reduces per transformer layer in forward and two in backward; communication ∝
activations, so it needs NVLink bandwidth and stays **within a node** (TP = 8). **Sequence
parallelism** shards the LayerNorm/dropout activations along the sequence to remove the
remaining replicated memory. **Pipeline parallelism**: assign consecutive layers to
stages; a naive pipeline idles (N−1)/N of the time — the **bubble**; **GPipe** splits the batch
into M micro-batches (bubble fraction (P−1)/(M+P−1)); **1F1B** (PipeDream-Flush) interleaves
forward and backward to bound activation memory to P micro-batches; **interleaved** 1F1B
assigns multiple non-contiguous stages per GPU to shrink the bubble further; asynchronous
variants trade staleness for utilization. **3D parallelism** (Megatron-DeepSpeed, Llama 3,
GPT-4-scale runs): TP inside the node × PP across nodes × DP (with ZeRO-1) across replicas —
e.g. 16k GPUs = TP 8 × PP 16 × DP 128; **context parallelism** (ring attention — shard the
sequence across GPUs and pass KV blocks around the ring) for 128k+ contexts; **expert
parallelism** for MoE (all-to-all routing of tokens to expert GPUs — load balancing
losses); the optimal combination is found by cost models or simulators (Alpa automates
it). JAX/TPU pods express all of this as sharding annotations (GSPMD) over a mesh.

## Fault tolerance and operations at scale (Llama 3 report; Jiang et al. 2024 MegaScale)
At 10⁴ GPUs something fails every few hours (GPU/HBM errors, NIC, straggling nodes,
silent data corruption): **checkpoint** frequently to distributed storage (async, sharded —
minutes of lost work, not hours), **elastic**/automatic restart from checkpoints, health
checks, straggler detection (one slow GPU slows the synchronous step), deterministic data
ordering to resume exactly, loss-spike detection and rollback, and telemetry per rank
([[site-reliability-engineering]], [[warehouse-scale-computing]]). Storage/IO: dataset
streaming from object stores with prefetch ([[distributed-file-and-object-storage]]);
tokenized, shuffled, sharded datasets (WebDataset/Mosaic streaming). Cost: GPU-hours ×
price; scheduling on Kubernetes/Slurm ([[cluster-scheduling-and-observability]]).

## Pitfalls
- Data loader as the bottleneck (GPU idle) — profile before touching the model.
- Small ops in eager mode (launch overhead) — fuse/compile; measuring MFU with the wrong
  FLOP count.
- Tensor parallelism across nodes over InfiniBand (bandwidth-bound); pipeline with too few
  micro-batches (bubble).
- FSDP with tiny modules (all-gather overhead) or without prefetch/overlap.
- Non-deterministic data order making restarts non-reproducible; checkpoints too rare.
- Scaling batch size without LR/warmup changes; forgetting gradient accumulation
  interacts with BatchNorm and per-step schedules.

## Related
- [[deep-learning-basics]], [[neural-network-training]], [[gpu-programming-cuda]],
  [[roofline-model]], [[caches-and-memory-hierarchy]], [[hardware-accelerators]],
  [[profiling-and-performance]], [[transformers-and-attention]], [[scaling-laws]],
  [[llm-inference-and-serving]], [[mlops-and-ml-systems]], [[parallel-programming-models]],
  [[distributed-systems-basics]], [[link-layer-and-lans]], [[warehouse-scale-computing]],
  [[cluster-scheduling-and-observability]], [[distributed-file-and-object-storage]],
  [[site-reliability-engineering]], [[compilers-overview]].

## Sources
CMU 10-714 (course structure); Paszke et al. 2019; Abadi et al. 2016; Chen et al. 2018 (TVM); Tillet et al. 2019 (Triton); Goyal et al. 2017; Rajbhandari et al. 2020 (ZeRO); Shoeybi et al. 2019 (Megatron); Huang et al. 2019 (GPipe); Narayanan et al. 2021 (Megatron-LM 2, interleaved 1F1B); Korthikanti et al. 2022 (sequence parallelism/selective recompute); Zheng et al. 2022 (Alpa); Liu et al. 2023 (ring attention); Llama 3 report 2024; Jiang et al. 2024 (MegaScale); Dao et al. 2022.

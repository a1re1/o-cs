---
title: GPU programming with CUDA — SIMT execution, threads/blocks/grids, warps and divergence, the memory hierarchy and tiling, coalescing, occupancy, and the core parallel patterns
type: concept
section: "4.7"
level: 400
tags: [gpu, cuda, simt, kernels, threads, blocks, grids, warps, warp-divergence, streaming-multiprocessor, shared-memory, global-memory, registers, constant-memory, tiling, coalescing, occupancy, memory-bandwidth, latency-hiding, atomics, privatization, reduction, scan, histogram, convolution, stencil, matrix-multiplication, tensor-cores, streams, unified-memory, opencl, sycl, hip, triton, cudnn, cublas]
sources: [stanford-cs149-and-cmu-15-418, parallel-programming-texts, parallel-computing-seminal-papers]
summary: A GPU runs thousands of threads in SIMT fashion — a kernel launches a grid of blocks of threads, each block runs on one streaming multiprocessor in warps of 32 threads that execute one instruction in lockstep (divergent branches within a warp serialize), and the hardware hides memory latency by switching among many resident warps rather than with big caches — so performance comes from exposing enough parallelism (occupancy: registers and shared memory per block bound resident warps), making memory access coalesced (consecutive threads → consecutive addresses), and moving reused data into the per-block shared memory via tiling (the classic tiled matrix multiply raises arithmetic intensity from memory-bound to compute-bound), while the standard patterns — reduction (tree in shared memory, warp shuffles), scan (Kogge–Stone/Brent–Kung), histogram (privatization then atomics), convolution/stencil (halo tiles, constant memory), sparse matrix–vector (CSR/ELL), BFS frontiers — are the building blocks behind cuBLAS/cuDNN, tensor cores and the deep-learning stack.
---
# GPU programming with CUDA

**In one sentence.** Write the program for one thread, launch a hundred thousand of them,
and then spend all your effort on how they touch memory.

## Execution model (CS149 L7; PMPP ch. 2–4; Nickolls 2008)
Host (CPU) launches a **kernel** `f<<<grid, block>>>(args)`; the **grid** is up to 3-D of
**blocks**, each up to 1024 **threads**; `blockIdx`, `threadIdx`, `blockDim` give each thread
its index. Blocks are scheduled independently onto **streaming multiprocessors** (SMs) — no
ordering or communication guarantees between blocks (scalability across GPU sizes); threads
in a block can synchronize (`__syncthreads()`) and share **shared memory**. Hardware executes a
block as **warps** of 32 threads in **SIMT**: one instruction stream, per-thread predication;
**divergence** (`if (threadIdx.x % 2)`) serializes both paths — keep divergence at warp
granularity. Latency hiding: an SM holds many resident warps and issues from whichever is
ready — the GPU's replacement for out-of-order execution and large caches
([[parallel-architectures-simd-gpu]]). **Occupancy** = resident warps / max; limited by
registers per thread, shared memory per block, threads per block; more occupancy ≠ always
faster (ILP within a thread also hides latency — Volkov).

## Memory hierarchy (PMPP ch. 5–6)
| Space | Scope | Speed | Use |
|---|---|---|---|
| Registers | thread | fastest | scalars; spills to local memory hurt |
| Shared memory | block | ~L1, banked (bank conflicts) | tiles, block-level reductions |
| L1/L2 caches | SM / device | automatic | |
| Global memory (HBM/GDDR) | device | 100s GB/s–TB/s, ~500 cycle latency | main data; **coalescing**: a warp's 32 accesses to consecutive 4-byte words → few 128 B transactions; strided/random access wastes bandwidth |
| Constant memory | device, read-only, broadcast cache | | filter masks, parameters |
| Texture | read-only, spatial cache | | images, interpolation |
Host↔device copies over PCIe/NVLink are slow — minimize, overlap with **streams**; **unified
memory** simplifies at a cost; pinned host memory for async copies. **Tiling**: load a tile of
inputs into shared memory cooperatively, `__syncthreads`, compute from shared memory, repeat
— tiled matrix multiply cuts global traffic by the tile width and turns a memory-bound kernel
compute-bound ([[roofline-model]]); register tiling and tensor cores (`mma`/WMMA, mixed
precision) push further; cuBLAS/CUTLASS encode all of this.

## Patterns (PMPP part II; CS149 L8)
- **Reduction**: tree in shared memory with stride halving (avoid divergence: contiguous active
  threads), warp shuffles (`__shfl_down_sync`), one atomic per block; **scan**: Kogge–Stone
  (step-efficient) vs Brent–Kung (work-efficient) within blocks, then block sums scanned and
  added; **histogram**: privatized copies in shared memory then merge with atomics
  (contention/aggregation); **convolution/stencil**: input tiles with halos, constant-memory
  masks, register tiling for 3-D; **sparse**: CSR (SpMV with a warp per row), ELL/JDS/hybrid
  for regularity; **merge/sort**: co-rank merge, radix sort via scan; **graph**: frontier-based
  BFS, load balancing across degree skew; **dynamic parallelism**, cooperative groups.
- Deep learning: convolution as im2col + GEMM or Winograd/FFT, fused kernels, attention
  (FlashAttention: tiling + recomputation for memory bandwidth), quantization; frameworks
  (cuDNN, PyTorch) and compilers (Triton, TVM, XLA) generate these kernels
  ([[neural-network-training]]).

## Ecosystem
CUDA (NVIDIA), HIP/ROCm (AMD), OpenCL/SYCL (portable), Metal, WebGPU; Python via CuPy/Numba/
Triton; profiling with Nsight Compute/Systems (achieved occupancy, memory throughput, warp
stall reasons); multi-GPU with NCCL all-reduce ([[parallel-programming-models]]).

## Pitfalls
- Uncoalesced access (array-of-structs), bank conflicts, warp divergence in inner loops.
- Too little work per launch; host–device copies inside loops; synchronous `cudaMemcpy`.
- Global atomics as the reduction strategy; race conditions on shared memory without
  `__syncthreads` (and calling it inside divergent branches — deadlock).
- Assuming more threads is always better; register pressure → spills.

## Related
- [[parallel-architectures-simd-gpu]], [[parallel-programming-models]], [[roofline-model]],
  [[caches-and-memory-hierarchy]], [[neural-network-training]], [[fft]].

## Sources
PMPP 4th ed. ch. 2–15; CS149 L7–8, 10; Nickolls et al. 2008; Volkov "Better performance at lower occupancy"; NVIDIA CUDA C++ Programming Guide.

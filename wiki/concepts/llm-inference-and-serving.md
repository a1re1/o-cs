---
title: LLM inference, serving, and efficient deep learning — the prefill/decode split and why decode is memory-bound, KV-cache sizing and PagedAttention, continuous batching, multi-/grouped-query attention, quantization (INT8/INT4/FP8; GPTQ, AWQ, SmoothQuant; QAT vs PTQ), pruning and sparsity, knowledge distillation, speculative decoding, prefix caching and prompt compression, tensor-parallel serving, latency/throughput/cost metrics, edge and TinyML (MCUNet, neural architecture search), and compilers/runtimes (TensorRT-LLM, vLLM, llama.cpp, ONNX)
type: concept
section: "6.9"
level: 500
tags: [llm-inference, model-serving, inference-optimization, prefill, decode, memory-bound, arithmetic-intensity, kv-cache, kv-cache-size, pagedattention, vllm, continuous-batching, iteration-level-scheduling, batching, multi-query-attention, grouped-query-attention, gqa, quantization, int8, int4, fp8, ptq, qat, gptq, awq, smoothquant, llm-int8, outliers, pruning, structured-pruning, unstructured-sparsity, 2-4-sparsity, knowledge-distillation, speculative-decoding, draft-model, medusa, prefix-caching, prompt-caching, tensor-parallel-serving, latency, time-to-first-token, tokens-per-second, throughput, cost-per-token, sla, tensorrt-llm, sglang, llama-cpp, onnx-runtime, edge-inference, tinyml, mcunet, neural-architecture-search, once-for-all, efficient-deep-learning, song-han, compression]
sources: [ml-systems-and-mlops-texts-courses-and-seminal-papers]
summary: Serving an LLM has two phases with opposite bottlenecks — prefill processes the prompt in one compute-bound pass, decode generates one token per step and is memory-bound because every step re-reads all weights and the growing KV cache for a few FLOPs per byte (arithmetic intensity ≈ batch size), so throughput comes from batching many requests per step and cost is dominated by memory bandwidth and KV-cache capacity: the cache is 2 × layers × heads × head_dim × bytes per token (tens of GB at long context), grouped-query attention shrinks it by sharing KV heads, PagedAttention (vLLM) allocates it in non-contiguous blocks like virtual memory to end fragmentation and enable prefix sharing, and continuous (iteration-level) batching admits and retires requests every step instead of padding to the longest; quantization cuts weight bytes — INT8 with outlier handling (LLM.int8, SmoothQuant), 4-bit weight-only post-training methods (GPTQ's second-order rounding, AWQ's activation-aware scaling) that lose little accuracy, FP8 on Hopper, quantization-aware training when PTQ fails, and KV-cache quantization; pruning (unstructured, 2:4 semi-structured for tensor cores, structured/layer dropping) and knowledge distillation (train a small student on the teacher's outputs) shrink models; speculative decoding uses a small draft model to propose tokens the large model verifies in parallel with an exact accept/reject rule for 2–3× lower latency; prefix/prompt caching reuses KV for shared system prompts; serving stacks (vLLM, SGLang, TensorRT-LLM, llama.cpp) combine these with tensor parallelism across GPUs; the metrics are time-to-first-token, inter-token latency, tokens/s per GPU, and dollars per million tokens against an SLA; and the same efficiency toolkit (Han's TinyML: pruning, quantization, NAS/once-for-all, distillation, MCUNet) puts models on phones and microcontrollers.
---
# LLM inference, serving, and efficient deep learning

**In one sentence.** Decoding is a memory-bandwidth problem — every token re-reads the
weights and the KV cache — so inference engineering is about batching more tokens per
byte read (continuous batching, paged KV), reading fewer bytes (quantization, GQA,
pruning, distillation), and generating more than one token per read (speculative decoding).

## Prefill vs decode and the roofline (Pope et al. 2022; Han 6.5940)
**Prefill**: the prompt's T tokens go through the model in one batched forward pass — large
matmuls, **compute-bound** (like training); produces the KV cache and the first token; cost
∝ T·2N FLOPs — sets **time-to-first-token**. **Decode**: one token per step, each step a
forward pass over a single token per sequence — matrix–*vector* products that read all
weights (2N bytes in bf16) plus the entire KV cache for ~2N FLOPs: **arithmetic intensity
≈ batch size** tokens/step, far below the GPU's ridge point (~300 FLOP/byte on H100) unless
hundreds of sequences are batched ([[roofline-model]]). So per-token latency at small
batch = (weights + KV bytes)/memory bandwidth (70 B bf16 on one 3.3 TB/s H100 ≈ 40 ms/token,
independent of FLOPs), and **throughput** grows almost linearly with batch until compute or
KV memory saturates. Metrics: **TTFT**, **inter-token latency / tokens per second per user**,
**throughput** (tokens/s per GPU), goodput under an SLA, **cost per million tokens**;
input and output tokens are priced differently for this reason.

## KV cache, attention variants, PagedAttention, batching (Kwon et al. 2023; Shazeer 2019; Ainslie et al. 2023)
**KV-cache size per token** = 2 (K and V) × layers × n_kv_heads × head_dim × bytes; Llama-2-70B
(80 layers, 8 KV heads via GQA, 128 dim, bf16) ≈ 320 KB/token → 128k context ≈ 40 GB per
sequence; without GQA (64 heads) 8× more. **Multi-query attention** (one KV head shared by
all query heads) and **grouped-query attention** (groups of query heads share a KV head)
reduce cache and bandwidth with little quality loss — standard in Llama 2/3, Mistral;
sliding-window attention bounds it; KV quantization (8-bit) and eviction/compression
(H2O, token merging) go further ([[transformers-and-attention]]). Naive serving reserves
max-length contiguous KV per request → internal/external **fragmentation** wastes 60–80 %
of memory; **PagedAttention** (vLLM) stores KV in fixed-size **blocks** with a block table per
sequence — allocation on demand, near-zero waste, **copy-on-write** sharing of prefixes across
beams/parallel samples/shared system prompts ([[virtual-memory]] applied to attention).
**Continuous (iteration-level) batching** (Orca): schedule at every decode step — new
requests join as soon as any slot frees, finished ones leave, prefill of newcomers is
chunked and interleaved with others' decode (chunked prefill) to avoid stalls; result:
2–4× throughput over static batching at the same latency. **Prefix/prompt caching**
(SGLang RadixAttention, provider "prompt caching"): reuse the KV of a shared prefix across
requests — long system prompts, few-shot examples, agent loops; **disaggregated serving**:
separate prefill and decode GPU pools sized independently.

## Quantization (Dettmers et al. 2022; Frantar et al. 2022; Lin et al. 2023; Han lectures)
Represent weights (and optionally activations, KV) in fewer bits: **INT8** (per-channel/
per-group scales; activations have **outlier** channels in LLMs > 6 B that break naive
quantization — **LLM.int8()** keeps outliers in fp16, **SmoothQuant** migrates activation
scale into weights offline for W8A8), **FP8** (E4M3/E5M2 with per-tensor scaling — Hopper
native, used for training too), **4-bit weight-only** (W4A16 — decode is weight-bandwidth-
bound, so 4-bit weights ≈ 3–4× faster and 4× smaller with fp16 compute): **GPTQ** (layer-
wise, rounds weights one column at a time using the inverse Hessian of the layer input to
compensate — OBS lineage), **AWQ** (protect the ~1 % salient weights identified by
activation magnitude via per-channel scaling; no backprop), NF4/QLoRA's data type for
fine-tuning, GGUF k-quants in llama.cpp; 2–3-bit and vector quantization (AQLM, QuIP#) at
some quality cost. **PTQ** (calibrate on a few hundred samples, minutes) vs **QAT** (train with
fake quantization; needed for aggressive activation quantization and small models);
evaluate on perplexity *and* downstream tasks — perplexity hides task regressions.
Hardware: INT8/FP8 tensor cores, INT4 kernels (Marlin, ExLlama), dequant-on-the-fly.

## Pruning, sparsity, distillation, architecture search (Han et al. 2015; Hinton et al. 2015; Cai et al. 2020)
**Pruning**: magnitude-based **unstructured** sparsity (90 %+ on CNNs; needs sparse kernels to
realize speedups — mostly memory savings), **2:4 semi-structured** (2 of every 4 weights
zero — NVIDIA sparse tensor cores give ~2×), **structured** (channels/heads/layers — real
speedups on dense hardware; Wanda/SparseGPT for LLMs); iterative prune–retrain; the
**lottery ticket** hypothesis ([[statistical-learning-theory]]). **Knowledge distillation**:
train a small student to match the teacher's soft outputs (temperature-scaled logits)
and/or hidden states — DistilBERT, TinyLlama-style, and the way frontier reasoning
behaviour reaches 7 B models ([[llm-post-training-sft-rlhf-dpo]]); sequence-level
distillation for generation. **Neural architecture search**: search spaces (cells,
widths, depths), strategies (RL, evolutionary, differentiable — DARTS), and
**once-for-all** networks (train one supernet, extract sub-networks per device without
retraining; hardware-aware latency predictors — ProxylessNAS, MCUNet's TinyNAS +
TinyEngine for 256 KB microcontrollers — [[microcontrollers-and-embedded-programming]]);
efficient architectures (MobileNet/EfficientNet — [[convolutional-neural-networks]];
MoE for LLMs). **TinyML** stack: quantized INT8 models, operator libraries (CMSIS-NN,
TFLite Micro), memory scheduling; on-device training with sparse updates.

## Speculative decoding and other latency tricks (Leviathan et al. 2023; Chen et al. 2023)
Decode wastes bandwidth at batch 1; **speculative decoding**: a small **draft** model (or
extra prediction heads — Medusa; or n-gram/lookahead) proposes k tokens autoregressively,
the target model scores all k+1 positions in *one* forward pass, tokens are accepted by a
**rejection-sampling** rule that reproduces the target distribution exactly, and the first
rejected position is resampled — 2–3× fewer target passes when the draft agrees often
(code, boilerplate), no quality change; EAGLE/self-speculation variants; tree-structured
drafts. Others: early exit, layer skipping, prompt compression (LLMLingua), constrained
decoding via token masks (grammar-guided JSON — [[large-language-models]]), and batching
identical prefixes. Long-context serving: ring/context-parallel attention across GPUs for
prefill, KV offload to CPU/NVMe with prefetch.

## Serving stacks and deployment ([[mlops-and-ml-systems]])
**vLLM** (PagedAttention, continuous batching, TP/PP, quantized kernels, OpenAI-compatible
API), **SGLang** (RadixAttention prefix caching, structured outputs, faster scheduling),
**TensorRT-LLM** (NVIDIA compiled kernels, in-flight batching, FP8), **llama.cpp** (CPU/Metal/
CUDA, GGUF quantized weights — laptops and phones), **ONNX Runtime / OpenVINO / CoreML /
TFLite** for non-LLM models and edge; **Triton Inference Server** / KServe / Ray Serve for
multi-model fleets ([[cloud-and-serverless]] autoscaling on tokens/s, not requests/s).
**Tensor-parallel serving** across 2–8 GPUs for models that don't fit or for lower
latency (bandwidth aggregation); pipeline parallel for throughput; **MoE serving** needs all
experts resident (memory) with expert parallelism. Capacity planning: peak concurrent
sequences × KV per sequence ≤ HBM − weights; batch size ↔ latency curves per model; caching
and routing small requests to small models ([[large-language-models]] model cascades);
observability: per-request token counts, queue time, TTFT/ITL percentiles
([[tail-latency-at-scale]]).

## Pitfalls
- Benchmarking decode with FLOPs; expecting a bigger GPU (more FLOPs, same bandwidth) to
  speed up batch-1 decode.
- Static batching with padding; reserving max-context KV per request.
- Quantizing activations naively past 6 B parameters (outliers); judging quantization by
  perplexity alone.
- Speculative decoding with a draft that disagrees (slower than plain decode); Medusa
  heads without enough acceptance.
- Unstructured pruning and expecting wall-clock gains on dense hardware.
- Serving without prefix caching for agentic workloads that resend the same 10k-token
  system prompt.

## Related
- [[large-language-models]], [[transformers-and-attention]], [[roofline-model]],
  [[gpu-programming-cuda]], [[distributed-training-and-ml-systems]], [[virtual-memory]],
  [[mlops-and-ml-systems]], [[llm-post-training-sft-rlhf-dpo]] (QLoRA, distillation),
  [[convolutional-neural-networks]], [[microcontrollers-and-embedded-programming]],
  [[cloud-and-serverless]], [[tail-latency-at-scale]], [[statistical-learning-theory]],
  [[floating-point]] (FP8/INT formats), [[hardware-accelerators]].

## Sources
Kwon et al. 2023 (vLLM); Yu et al. 2022 (Orca); Pope et al. 2022 (efficiently scaling transformer inference); Shazeer 2019 (MQA); Ainslie et al. 2023 (GQA); Dettmers et al. 2022 (LLM.int8); Xiao et al. 2023 (SmoothQuant); Frantar et al. 2022 (GPTQ); Lin et al. 2023 (AWQ); Leviathan et al. 2023 and Chen et al. 2023 (speculative decoding); Cai et al. 2024 (Medusa); Zheng et al. 2023 (SGLang); Han et al. 2015 (deep compression); Hinton et al. 2015; Cai et al. 2020 (once-for-all); Lin et al. 2020 (MCUNet); MIT 6.5940 lecture list.

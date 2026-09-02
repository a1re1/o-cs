---
title: Efficient Transformers and Long Context
type: concept
section: "6.4"
level: 400
tags: [efficient-transformers, attention, kv-cache, flash-attention, long-context, sparse-attention]
sources: [nlp-and-llm-courses-texts-and-seminal-papers]
summary: Making transformers handle long sequences — the quadratic-attention bottleneck and its fixes: FlashAttention, KV caching, sparse/linear attention, and context-extension tricks like RoPE scaling.
---

# Efficient Transformers and Long Context
**In one sentence.** Standard self-attention costs time and memory quadratic in sequence
length, so long-context transformers rely on IO-aware kernels (FlashAttention), caching
(KV cache), and sparse/linear attention or position-scaling to scale to long inputs.

## Why it matters
Context length limits what an LLM can read at once — a whole codebase, a long document,
a long conversation. The quadratic cost of attention is the central obstacle, and the
techniques to beat it are what make today's long-context models and efficient serving
possible. Builds on [[transformers-and-attention]].

## How it works
**The bottleneck.** Self-attention compares every token with every other: `O(n²)` in
both compute and memory for sequence length `n`. At long `n` the `n×n` attention matrix
dominates cost and memory.

**Making exact attention cheaper (no approximation):**
- **FlashAttention** — an **IO-aware** kernel that computes attention in tiles that fit in
  fast on-chip SRAM, never materializing the full `n×n` matrix in slow HBM. Same result,
  far less memory traffic — the reason it is a big speedup. Ties to
  [[caches-and-memory-hierarchy]] (the win is memory movement, not FLOPs).
- **KV cache** — at inference, cache the key/value vectors of past tokens so each new
  token attends to them without recomputation, turning generation from `O(n²)` per step
  into `O(n)`. The cache's size becomes the memory bottleneck for long context (addressed
  by multi-query / grouped-query attention and paged KV caches — see
  [[llm-inference-and-serving]]).

**Approximate / sub-quadratic attention:**
- **Sparse attention** (Longformer, BigBird) — each token attends only to a local window
  plus a few global tokens: `O(n·w)`.
- **Linear attention / state-space models** (Performer, Mamba) — reformulate attention to
  `O(n)` via kernel feature maps or a recurrent state; strong for very long sequences,
  sometimes at a quality cost.

**Extending context length:**
- **Positional-encoding scaling** — **RoPE** (rotary embeddings) can be interpolated or
  scaled (NTK/YaRN) to extend a model to longer contexts than it was trained on, often
  with light fine-tuning.
- **Retrieval augmentation** sidesteps context limits by fetching only relevant passages
  (see [[dense-retrieval-and-embeddings]]) instead of stuffing everything into the prompt.

## Complexity & trade-offs
- FlashAttention and KV caching keep attention **exact** while cutting memory/latency —
  pure wins, now standard.
- Sparse/linear attention trade some modeling quality for sub-quadratic scaling; worth it
  only when `n` is large enough that quadratic is infeasible.
- Long context costs memory (KV cache grows with length) and can dilute attention
  ("lost in the middle"); retrieval is often cheaper than a giant context.

## Pitfalls & gotchas
- **KV-cache memory blowup** — long contexts and large batches exhaust GPU memory;
  grouped-query attention and paged caches mitigate it.
- **Naive context extension** past training length degrades quality without RoPE
  scaling/fine-tuning.
- **"Lost in the middle"** — models attend less to the middle of very long contexts;
  placement of key information matters.
- **Quality of linear/sparse attention** varies by task; validate, don't assume parity.

## Worked example
Serving a chat model: the first forward pass over a 4,000-token prompt builds the KV
cache; each generated token then attends to the cache in `O(n)` instead of reprocessing
the prompt, and FlashAttention keeps even the prefill from materializing a 4000×4000
attention matrix — together making interactive generation feasible on one GPU.

## Related
- [[transformers-and-attention]] — the base architecture.
- [[large-language-models]] — where long context matters most.
- [[llm-inference-and-serving]] — KV-cache management and serving.
- [[dense-retrieval-and-embeddings]] — retrieval as an alternative to long context.
- [[caches-and-memory-hierarchy]] — why FlashAttention's IO-awareness wins.

## Sources
Distilled from [[nlp-and-llm-courses-texts-and-seminal-papers]] (FlashAttention; Longformer/BigBird;
RoPE/YaRN; Mamba).

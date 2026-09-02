---
title: Transformers and attention — scaled dot-product attention (queries, keys, values), multi-head attention, positional encodings (sinusoidal, learned, RoPE), the encoder/decoder block (attention + MLP with residuals and LayerNorm), causal masking, complexity and KV caches, the encoder-only/decoder-only/encoder–decoder families (BERT, GPT, T5), Vision Transformers, and why the architecture scaled
type: concept
section: "6.3"
level: 400
tags: [transformer, attention, self-attention, scaled-dot-product-attention, queries-keys-values, qkv, softmax, multi-head-attention, positional-encoding, sinusoidal, learned-positions, rope, rotary, alibi, encoder, decoder, encoder-decoder, causal-mask, masked-attention, cross-attention, feed-forward, mlp-block, residual, layernorm, pre-ln, kv-cache, quadratic-complexity, sequence-length, flash-attention, bert, gpt, t5, vision-transformer, vit, patches, cls-token, mixture-of-experts, moe, attention-is-all-you-need, vaswani, inductive-bias, scaling]
sources: [deep-learning-texts-courses-and-seminal-papers]
summary: A transformer layer lets every position gather information from every other by attention — each token emits a query, key and value (linear projections of its embedding), attention weights are softmax(QKᵀ/√d_k) (scaled so dot products don't saturate the softmax), and the output is the weighted sum of values, a content-addressed lookup that is permutation-equivariant, so position must be injected by positional encodings (sinusoidal, learned, or rotary/RoPE which encodes relative position in the dot product); multiple heads attend to different subspaces in parallel and are concatenated, followed by a position-wise MLP (most of the parameters), each sub-layer wrapped in a residual connection and LayerNorm (pre-LN for stability); decoders add a causal mask so position t sees only positions ≤ t (autoregressive generation with a KV cache making each new token O(T)), and encoder–decoders add cross-attention from decoder queries to encoder keys/values; the compute is O(T²d) per layer in sequence length (the reason for FlashAttention's IO-aware kernels and long-context variants) and O(Td²) in the MLP; the families are encoder-only (BERT: bidirectional masked-LM pretraining for understanding), decoder-only (GPT: next-token prediction, now the default for everything), and encoder–decoder (T5, translation); Vision Transformers treat 16×16 image patches as tokens and beat CNNs with enough data; and the architecture won because it is parallel over sequence length, has constant path length between positions, and its performance keeps improving predictably with data and compute.
---
# Transformers and attention

**In one sentence.** Attention is a differentiable dictionary lookup — every token asks a
question (query), every token advertises what it holds (key) and what it will hand over
(value), and the softmax over similarities routes information — and a transformer is a
stack of attention + MLP blocks with residuals and LayerNorm, which trains in parallel and
scales.

## Scaled dot-product attention (Vaswani et al. 2017; CS231n lecture 8; D2L ch. 11)
Input X ∈ ℝ^{T×d}; Q = XW_Q, K = XW_K, V = XW_V (d_k = d_v = d/h per head).
**Attention(Q, K, V) = softmax(QKᵀ/√d_k) V**: row i is a convex combination of value vectors
weighted by the similarity of query i to each key. The **√d_k** scaling keeps dot-product
variance ≈ 1 so the softmax isn't saturated at init (gradients would vanish). Intuition:
soft, content-based, differentiable retrieval ([[hash-tables]] made continuous); the
attention matrix is T × T — **O(T²d) time and O(T²) memory per head**, the cost that limits
context length. Attention is **permutation-equivariant** (a set operation): word order must
be injected. Variants: additive (Bahdanau) attention — same idea, MLP score; **cross-
attention** (queries from one sequence, keys/values from another — decoder ↔ encoder,
text ↔ image in diffusion models); **causal (masked)** attention sets scores for j > i to −∞
so the output at i depends only on positions ≤ i — autoregressive models, and the trick
that lets one forward pass train on all T next-token predictions at once.

## Multi-head attention, positions, and the block
**Multi-head**: h heads with separate projections attend in parallel (different heads learn
syntax, coreference, copying — induction heads), outputs concatenated and projected by W_O;
same FLOPs as one wide head, richer. **Positional encoding**: added to token embeddings —
**sinusoidal** PE(pos, 2i) = sin(pos/10000^{2i/d}) (relative offsets are linear functions;
extrapolates in principle), **learned** absolute positions (BERT, GPT-2; fixed max length),
**relative** biases (T5, ALiBi), and **RoPE** (rotary: rotate q and k by position-dependent
angles so qᵀk depends on the relative offset — Llama and most modern LLMs; extended by
position interpolation/YaRN for longer contexts). **The block**: x ← x + MHA(LN(x)); x ← x +
MLP(LN(x)), with MLP = W₂ φ(W₁ x) expanding d → 4d → d (GELU/SwiGLU; ~2/3 of parameters,
and where factual "memories" seem to live). **Pre-LN** (normalize before the sub-layer) is
stabler than the original post-LN; RMSNorm is the cheaper norm. Residuals give the
"residual stream" reading: each layer reads from and writes to a shared d-dimensional
channel ([[interpretability-and-explainability]]). Parameter count per layer ≈ 12d²
(4d² attention + 8d² MLP); FLOPs per token ≈ 2 × params + attention's 2Td per layer
([[scaling-laws]] for the 6ND rule).

## Encoders, decoders, and the families (D2L ch. 11; Prince ch. 12)
- **Encoder–decoder** (original, translation; **T5**, BART): encoder self-attention
  (bidirectional), decoder causal self-attention + cross-attention; trained on
  sequence-to-sequence objectives.
- **Encoder-only** (**BERT** 2018): bidirectional; pretrained with masked-language modelling
  (predict 15 % masked tokens) + next-sentence prediction; fine-tune with a task head on a
  [CLS] token — classification, NER, QA (extractive), retrieval embeddings
  ([[nlp-fundamentals]], [[dense-retrieval-and-embeddings]]).
- **Decoder-only** (**GPT** 2018 → GPT-3 2020 → everything): next-token prediction on raw
  text; generation by sampling with a **KV cache** (store past keys/values so each new token
  costs O(T) attention instead of recomputing O(T²); cache memory = 2 × layers × T × d × bytes
  — the inference bottleneck and the reason for multi-query/grouped-query attention);
  prompting and in-context learning emerge at scale — [[large-language-models]].
**Vision Transformer** (Dosovitskiy et al. 2020): split the image into 16×16 patches,
linearly embed, add positions and a [CLS] token, run a plain encoder — fewer inductive
biases than CNNs ([[convolutional-neural-networks]]), so it needs more data (JFT-300M, or
self-supervised DINO/MAE pretraining) and then wins; Swin adds locality/hierarchy; the same
recipe extends to audio, video, proteins, and multimodal models (CLIP: contrastive image–
text — [[self-supervised-and-contrastive-learning]]). **Mixture-of-experts** MLPs (Switch,
Mixtral): route each token to k of E expert MLPs — parameters grow, per-token FLOPs don't.

## Efficiency and long context
Attention's T² is memory-bound on GPUs: **FlashAttention** (Dao et al. 2022) tiles Q, K, V
through SRAM and never materializes the T × T matrix (exact, 2–4× faster, linear memory —
[[roofline-model]], [[gpu-programming-cuda]]). Approximate/linear attention, sliding windows,
sparse patterns, and state-space models trade exactness for length; context lengths went
from 512 (BERT) to 128k–1M+ tokens ([[efficient-transformers-and-long-context]]). Training:
Adam with warmup, pre-LN, gradient clipping, bf16, weight decay 0.1, dropout 0–0.1
([[neural-network-training]]); at scale, tensor/pipeline/data parallelism
([[distributed-training-and-ml-systems]]).

## Why it won (Vaswani et al. §4)
Per-layer cost O(T²d) vs RNN O(Td²) — cheaper when T < d (typical); **sequential operations
O(1)** vs O(T) — full parallelism over the sequence on accelerators; **maximum path length
O(1)** between any two positions vs O(T) — no vanishing over distance
([[recurrent-neural-networks-and-lstms]]). Combined with pretraining on unlabeled text and
predictable improvement with scale ([[scaling-laws]]), one architecture now serves language,
vision, speech, code, and biology; inductive bias is supplied by data rather than
architecture — the "bitter lesson" ([[intelligent-agents-and-ai-history]]).

## Pitfalls
- Forgetting the √d_k scaling or the causal mask (future leakage looks like a great LM).
- Attention over padding tokens without masking; softmax in fp16 without the max-subtract.
- Post-LN without warmup (divergence); learned absolute positions beyond training length.
- Treating attention weights as explanations (they are not faithful in general).
- Ignoring the KV cache in serving cost estimates; batch-1 generation is memory-bound.

## Related
- [[recurrent-neural-networks-and-lstms]], [[deep-learning-basics]],
  [[neural-network-training]], [[large-language-models]], [[nlp-fundamentals]],
  [[convolutional-neural-networks]], [[scaling-laws]],
  [[efficient-transformers-and-long-context]], [[dense-retrieval-and-embeddings]],
  [[self-supervised-and-contrastive-learning]], [[interpretability-and-explainability]],
  [[gpu-programming-cuda]], [[roofline-model]], [[distributed-training-and-ml-systems]],
  [[hash-tables]].

## Sources
Vaswani et al. 2017; Bahdanau et al. 2014; Devlin et al. 2018 (BERT); Radford et al. 2018–19 (GPT); Raffel et al. 2020 (T5); Dosovitskiy et al. 2020 (ViT); Su et al. 2021 (RoPE); Dao et al. 2022 (FlashAttention); CS231n lecture 8 (schedule read); D2L ch. 11; Prince ch. 12; Karpathy, "Let's build GPT" 2023.

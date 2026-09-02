---
title: Source coding and data compression (Huffman, arithmetic coding, Lempel–Ziv)
type: concept
section: "1.7"
level: 400
tags: [source-coding, compression, huffman-coding, prefix-codes, kraft-inequality, arithmetic-coding, lempel-ziv, lz77, typical-set, aep, universal-codes, entropy-coding]
sources: [mackay-itila, shannon-1948]
summary: The source coding theorem says N i.i.d. symbols compress to ≈ NH bits and no fewer; prefix codes obey the Kraft inequality and Huffman is optimal among them (within 1 bit of H per symbol); arithmetic coding reaches H with any adaptive probability model; Lempel–Ziv is universal without a model — and every modern compressor is a model plus an entropy coder.
---
# Source coding and compression

**In one sentence.** Compression = assign short codewords to probable messages; the entropy H is the
floor on the average length, and the engineering is in modelling the probabilities.

## The theorem (MacKay ch. 4)
**Asymptotic equipartition / typical set**: for N i.i.d. symbols, with high probability the sequence lies
in a set of ≈ 2^{NH} "typical" sequences, each with probability ≈ 2^{−NH}. So N symbols can be described
with N(H + ε) bits with vanishing error, and cannot be described with N(H − ε) bits even allowing
error probability close to 1 — "H bits per symbol, no more and no less". Lossless compression of a
uniformly random file is impossible on average ([[pigeonhole-principle]]).

## Symbol codes (MacKay ch. 5)
- **Prefix (instantaneous) codes** are uniquely decodable; **Kraft–McMillan**: a uniquely decodable code
  with lengths lᵢ exists iff Σ 2^{−lᵢ} ≤ 1. Optimal lengths lᵢ = log₂(1/pᵢ) ⇒ expected length = H.
- **Huffman**: merge the two least-probable symbols repeatedly; optimal among symbol codes; expected
  length L < H + 1. The +1 hurts when one symbol dominates (p = 0.99 still costs ≥ 1 bit/symbol).
  Canonical Huffman for compact tables; used in DEFLATE (gzip/PNG), JPEG.

## Stream codes (MacKay ch. 6)
- **Arithmetic coding**: encode the whole message as a subinterval of [0,1) whose width is the message's
  probability; length ≈ log₂(1/P(message)) + 2 bits, i.e. within 2 bits of optimal *for the whole
  message*. Crucially it takes probabilities from *any* model, adaptive ones included (PPM, context
  mixing, neural LMs) — modelling and coding are decoupled. Range coding / ANS (asymmetric numeral
  systems, used in zstd, JPEG XL) are fast implementations.
- **Lempel–Ziv** (LZ77/LZ78/LZW): replace repeats with (offset, length) references; no probability model,
  asymptotically optimal for any stationary ergodic source (universal), and the core of gzip, zstd,
  brotli, LZ4 (which then entropy-code the tokens with Huffman/ANS).
- Codes for integers (unary, Elias γ/δ, Golomb/Rice) for when the alphabet is unbounded — inverted-index
  gap compression ([[inverted-index]]).

## Practical picture
compressor = **model** (predict next symbol distribution: order-k contexts, dictionary matches, or a
neural net) + **entropy coder** (Huffman/arithmetic/ANS). Better model ⇒ better ratio; the Hutter prize
and "compression = intelligence" argument formalize this ([[entropy-and-information]],
[[kolmogorov-complexity]]). Lossy compression (JPEG, MP3, video) adds rate–distortion: minimize bits
subject to allowed distortion, exploiting perceptual irrelevance.

## Pitfalls
- Huffman on a skewed binary source wastes up to ~100%; block symbols or use arithmetic coding.
- Compressing already-compressed or encrypted data does nothing (it looks uniformly random).
- Compression ratio claims without the model/dictionary size are misleading; small inputs can grow.

## Related
- [[entropy-and-information]], [[channel-capacity-and-error-correction]], [[inverted-index]],
  [[kolmogorov-complexity]].

## Sources
MacKay ch. 4–7; Shannon 1948 Part I (noiseless coding theorem).

---
title: Vectors, inner products, norms, and cosine similarity
type: concept
section: "1.2"
level: 200
tags: [vectors, inner-product, dot-product, norms, euclidean-norm, cosine-similarity, distance, rms, flops, sparse-vectors, embeddings]
sources: [boyd-vmls, strang-18-06, 3b1b-essence-of-linear-algebra]
summary: The vector operations behind embeddings and numeric code — inner product, Euclidean and other norms, distance, angle and cosine similarity, standard deviation as a norm, Cauchy–Schwarz and triangle inequalities — with flop counts and the reasons cosine similarity is used for embeddings.
---
# Vectors, inner products, norms

**In one sentence.** The inner product xᵀy = Σ xᵢyᵢ measures alignment, its induced norm
‖x‖ = √(xᵀx) measures size, and almost every similarity or loss in ML is one of these two.

## Definitions and identities
- **Norm**: ‖x‖₂ = √Σxᵢ²; ‖x‖₁ = Σ|xᵢ|; ‖x‖∞ = max|xᵢ|. Properties: homogeneity, triangle inequality
  ‖x + y‖ ≤ ‖x‖ + ‖y‖, definiteness. RMS(x) = ‖x‖/√n is the size "per entry".
- **Distance**: ‖x − y‖; nearest-neighbour search is minimizing this ([[ann-search]] for the scalable version).
- **Cauchy–Schwarz**: |xᵀy| ≤ ‖x‖‖y‖, with equality iff parallel. Hence the **angle**
  θ = arccos(xᵀy / ‖x‖‖y‖) is well defined; cos θ is **cosine similarity**. Orthogonal ⇔ xᵀy = 0.
- **Standard deviation** of a vector is the norm of its de-meaned version over √n; correlation
  coefficient = cosine similarity of the de-meaned vectors — so Pearson correlation is an angle.
- **Sparse vectors**: store (index, value) pairs; inner product of sparse vectors costs
  O(min(nnz(x), nnz(y))) with merge or hashing.

## Complexity (flops, VMLS 1.5)
Inner product 2n; vector add n; ‖x‖ 2n; matrix–vector (m×n) 2mn; matrix–matrix (m×n by n×p) 2mnp.
A 1 GFLOP/s machine does a length-10⁶ inner product in ~2 ms; modern hardware is 10⁹–10¹³ FLOP/s and
memory bandwidth, not arithmetic, usually dominates ([[roofline-model]]).

## Why cosine similarity for embeddings
Embedding models (bge, word2vec, …) place related texts along similar directions; magnitudes carry
frequency/length artifacts. Normalizing to unit length makes cosine = dot product, so a dense index can
rank by a single matrix–vector product; oasis does exactly this after L2-normalizing bge-small vectors
([[dense-retrieval]]).

## Pitfalls
- Comparing norms across different dimensions or scalings (feature scaling matters for k-means/kNN).
- Cosine similarity of zero vectors is undefined; of very high-dimensional random vectors is ≈ 0 with
  small variance (concentration), so tiny differences can be meaningful.
- Floating-point summation order changes results slightly; use pairwise/Kahan summation when accumulating
  many terms ([[floating-point]]).

## Related
- [[matrices-and-linear-maps]] — matrix–vector product as many inner products.
- [[orthogonality-and-projections]] — projection = inner product with a unit vector.
- [[k-means-clustering]] — distances drive assignment.

## Sources
VMLS ch. 1, 3; Strang lecture 1; 3Blue1Brown "dot products and duality".

---
title: Similarity search — k-d trees, curse of dimensionality, MinHash, Johnson–Lindenstrauss, and locality-sensitive hashing
type: concept
section: "3.3"
level: 400
tags: [similarity-search, nearest-neighbor, k-d-trees, curse-of-dimensionality, minhash, jaccard, johnson-lindenstrauss, random-projection, dimension-reduction, locality-sensitive-hashing, lsh, simhash, cosine-similarity, approximate-nearest-neighbor, hnsw, vector-search]
sources: [cs168-modern-algorithmic-toolbox, karp-cook-and-classic-papers]
summary: Exact nearest-neighbour search works in low dimensions (k-d trees, ≲ 20 dims) but collapses in high dimensions because distances concentrate; the remedies are distance-preserving compression — MinHash turns Jaccard similarity into collision probability of a random permutation's minimum, Johnson–Lindenstrauss says a random projection to O(log n / ε²) dimensions preserves all pairwise Euclidean distances within 1 ± ε — and locality-sensitive hashing (Indyk–Motwani), which amplifies "similar items collide" hash families into sublinear approximate nearest-neighbour search; graph indexes (HNSW) dominate modern vector databases.
---
# Similarity search and locality-sensitive hashing

**In one sentence.** In high dimensions you cannot afford exact nearest neighbours, so hash so
that similar items collide and dissimilar ones don't — and let random projections shrink the
space first.

## Metrics and the low-dimensional case (CS168 week 2)
Jaccard |A∩B|/|A∪B| for sets (documents as shingles), Euclidean/ℓp, cosine for embeddings,
Hamming for bit vectors, edit distance for strings. **k-d trees** (split on alternating
coordinates at the median; backtrack with a ball test) give ~log n queries up to ~20 dimensions.
Beyond that the **curse of dimensionality**: volume concentrates near the surface, pairwise
distances concentrate around their mean (nearest ≈ farthest), and the kissing number grows
exponentially, so tree pruning stops working and brute force O(nd) is the baseline
([[vectors-and-inner-products]]).

## Distance-preserving compression
- **MinHash** (Broder): for a random permutation π, Pr[min π(A) = min π(B)] = Jaccard(A, B).
  Keep k minima as a signature; estimate similarity by the fraction of equal coordinates (variance
  J(1−J)/k). Near-duplicate detection in web search; b-bit minwise hashing.
- **Johnson–Lindenstrauss**: a random Gaussian (or ±1) matrix A ∈ ℝ^{d'×d} with d' = O(log n / ε²)
  satisfies (1−ε)‖x−y‖ ≤ ‖Ax−Ay‖/√d' ≤ (1+ε)‖x−y‖ for all n points w.h.p. — independent of the
  original dimension d. Proof: each squared projected length is a χ² concentration
  ([[concentration-inequalities]]); union bound over pairs. Used for fast regression sketches,
  streaming ℓ₂, and as a preprocessing step. Contrast PCA, which preserves *variance*, not all
  distances ([[svd-and-pca]]).
- **SimHash** (random hyperplanes): Pr[sign(r·x) = sign(r·y)] = 1 − θ(x,y)/π — cosine
  similarity as Hamming distance of short fingerprints.

## Locality-sensitive hashing (Indyk–Motwani 1998)
A family H is (r, cr, p₁, p₂)-sensitive if close points (dist ≤ r) collide with probability ≥ p₁
and far points (≥ cr) with ≤ p₂ < p₁. **Amplification**: AND k functions per table (lowers both
probabilities, p^k) and OR over L tables (raises them, 1 − (1 − p^k)^L); choose k, L so that
close pairs collide in some table w.h.p. and far pairs rarely do. Query time n^ρ with ρ = ln
p₁ / ln p₂ < 1 (ρ ≈ 1/c for Hamming/Jaccard/p-stable Euclidean). Families: bit sampling
(Hamming), MinHash (Jaccard), random hyperplanes (cosine), p-stable projections with quantization
(ℓ₂). Data-dependent LSH and learned hashes improve ρ.

## Modern practice
Vector databases use **HNSW** (hierarchical navigable small-world graphs: greedy search on a
layered proximity graph, ~log n hops), IVF (k-means coarse quantization + inverted lists — see
[[k-means-clustering]]), and **product quantization** for compression; FAISS, ScaNN, Annoy,
DiskANN. Trade recall for speed; measure recall@k on held-out queries. Hybrid search fuses dense
ANN with lexical BM25 by reciprocal rank fusion — the design of [[search-engines-and-ranking]].

## Pitfalls
- Using k-d trees or exact search in 100+ dimensions; normalizing vectors when the metric
  assumes it (cosine vs dot product).
- Too few MinHash/JL dimensions for the required ε (variance ~ 1/k).
- LSH parameter tuning: k too large (nothing collides), L too large (memory).

## Related
- [[hash-tables]], [[streaming-and-sketching]], [[svd-and-pca]], [[concentration-inequalities]],
  [[vectors-and-inner-products]], [[k-means-clustering]], [[search-engines-and-ranking]].

## Sources
CS168 weeks 2; Indyk & Motwani 1998; Broder 1997; Johnson & Lindenstrauss 1984; Malkov & Yashunin 2018 (HNSW).

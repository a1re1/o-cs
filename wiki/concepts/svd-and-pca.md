---
title: Singular value decomposition (SVD), low-rank approximation, PCA, pseudoinverse
type: concept
section: "1.2"
level: 300
tags: [svd, singular-values, low-rank-approximation, eckart-young, pca, principal-components, pseudoinverse, condition-number, dimensionality-reduction, matrix-rank]
sources: [strang-18-06, boyd-vmls]
summary: Every matrix factors as A = UΣVᵀ (orthonormal U, V; nonnegative σ₁ ≥ σ₂ ≥ …), giving rank, condition number, the best rank-k approximation (Eckart–Young), the pseudoinverse for least squares, and PCA when applied to centered data — the workhorse of dimensionality reduction and embeddings.
---
# SVD, low-rank approximation, PCA

**In one sentence.** A = UΣVᵀ says any linear map is a rotation, then axis scaling, then another
rotation; the singular values σᵢ are the "right" sizes of A, and truncating them gives the best
low-rank approximation.

## Definition and computation
- A (m×n) = U (m×m orthogonal) Σ (m×n diagonal, σ₁ ≥ … ≥ σ_r > 0) Vᵀ (n×n orthogonal). Columns of V are
  eigenvectors of AᵀA (eigenvalues σᵢ²); columns of U are eigenvectors of AAᵀ; Avᵢ = σᵢuᵢ.
- Rank r = number of nonzero σ; numerically, count σᵢ > tol·σ₁. Thin SVD keeps r columns.
- Cost O(min(mn², m²n)); randomized SVD for huge matrices; Lanczos for a few top components.
- ‖A‖₂ = σ₁; ‖A‖_F² = Σσᵢ²; **condition number** κ = σ₁/σ_r (∞ if singular) — expect to lose log₁₀κ
  digits solving with A ([[gaussian-elimination-lu]]).

## Low-rank approximation (Eckart–Young)
A_k = Σ_{i≤k} σᵢuᵢvᵢᵀ minimizes ‖A − B‖ (2-norm and Frobenius) over all rank-k B; error = σ_{k+1}
(2-norm). Uses: compression, denoising, latent semantic analysis (term-document matrices), recommender
matrix factorization, and initializing embeddings ([[dense-retrieval]]). Storage kr(m+n) instead of mn.

## PCA
Center the data matrix X (n samples × d features). Covariance C = XᵀX/(n−1) = VΣ²Vᵀ/(n−1). Principal
components = columns of V; variance explained by component i ∝ σᵢ². Project onto the top k for
dimensionality reduction/visualization; choose k by cumulative explained variance. Standardize features
first when units differ. PCA is unsupervised and linear; see t-SNE/UMAP for nonlinear embeddings (§6.2).

## Pseudoinverse
A⁺ = VΣ⁺Uᵀ (invert nonzero σ). x̂ = A⁺b gives the least-squares solution of minimum norm for *any* A,
rank-deficient included; truncating small σ (or ridge) regularizes ([[least-squares]]).

## Pitfalls
- Sign/ordering ambiguity of singular vectors; compare subspaces, not vectors.
- Forgetting to center before PCA (the first component then points at the mean).
- Eckart–Young is optimal for unweighted norms; missing entries (recommenders) need alternating least
  squares or SGD instead.
- σ values scale with the data; use relative tolerances.

## Related
- [[eigenvalues-and-eigenvectors]] (SVD = spectral theorem for AᵀA), [[orthogonality-and-projections]],
  [[least-squares]], [[four-fundamental-subspaces]].

## Sources
Strang lectures 29 and 31, "The big picture of the SVD"; VMLS ch. 12 (pseudoinverse), appendix.

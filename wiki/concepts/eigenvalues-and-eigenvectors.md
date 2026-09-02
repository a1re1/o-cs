---
title: Eigenvalues, eigenvectors, diagonalization, and symmetric matrices
type: concept
section: "1.2"
level: 200
tags: [eigenvalues, eigenvectors, diagonalization, characteristic-polynomial, spectral-theorem, symmetric-matrices, positive-definite, markov-matrices, power-iteration, pagerank, matrix-powers, similar-matrices]
sources: [strang-18-06, hefferon-linear-algebra, 3b1b-essence-of-linear-algebra]
summary: Directions a matrix only stretches (Ax = λx); when n independent ones exist A = XΛX⁻¹ and powers/exponentials become trivial; symmetric matrices have real eigenvalues and orthogonal eigenvectors (A = QΛQᵀ), positive definiteness means all λ > 0, and Markov/PageRank matrices converge to their λ = 1 eigenvector under power iteration.
---
# Eigenvalues and eigenvectors

**In one sentence.** Ax = λx picks out the invariant directions of a linear map; in that basis the map
is diagonal, which is why eigen-decompositions solve recurrences, dynamics, Markov chains and PCA.

## Basics
- det(A − λI) = 0 (characteristic polynomial, degree n) gives eigenvalues; nullspace of A − λI gives
  eigenvectors. Σλ = trace, Πλ = det. Triangular ⇒ eigenvalues on the diagonal. Real matrices can have
  complex eigenvalues (rotations).
- **Diagonalization**: if A has n independent eigenvectors (columns of X), A = XΛX⁻¹ and
  A^k = XΛ^kX⁻¹. Distinct eigenvalues ⇒ diagonalizable; repeated eigenvalues may not be (Jordan form).
- Fibonacci / linear recurrences: u_{k+1} = Au_k ⇒ u_k = Σ cᵢλᵢ^k xᵢ, growth rate = |λ_max|
  ([[recurrences]]). Difference/differential equations likewise (e^{At} = Xe^{Λt}X⁻¹).
- Similar matrices B = P⁻¹AP have the same eigenvalues (same map, different basis).

## Symmetric and positive definite (Strang lectures 25–27)
- **Spectral theorem**: real symmetric A = QΛQᵀ with real λ and orthonormal eigenvectors. Every
  covariance matrix, graph Laplacian, and AᵀA is symmetric — so this is the common case.
- **Positive definite** (xᵀAx > 0 ∀x ≠ 0) ⇔ all λ > 0 ⇔ all pivots > 0 ⇔ all leading principal
  minors > 0 ⇔ A = RᵀR with R invertible. Semidefinite allows 0. Hessians of convex functions are PSD
  ([[derivatives-and-gradients]], §1.6).
- The quadratic form xᵀAx has level sets that are ellipsoids with axes along eigenvectors, lengths
  1/√λ — the geometry behind conditioning of gradient descent.

## Markov matrices and power iteration
Column-stochastic P (entries ≥ 0, columns sum to 1): λ = 1 is an eigenvalue, all |λ| ≤ 1; if the chain
is irreducible and aperiodic, P^k u₀ → the stationary distribution (eigenvector for λ = 1), at rate
|λ₂|^k. **PageRank** = stationary distribution of the random-surfer chain with teleportation
([[pagerank]]). **Power iteration** x ← Ax/‖Ax‖ finds the dominant eigenvector; Lanczos/Arnoldi for
more; QR algorithm for all (O(n³)).

## Pitfalls
- Eigenvectors of non-symmetric matrices need not be orthogonal; don't assume Q.
- Computing eigenvalues via the characteristic polynomial is numerically terrible beyond n ≈ 4.
- "Positive definite" is only defined for symmetric (or Hermitian) matrices in most contexts.
- A nilpotent matrix ([[0,1],[0,0]]) has all eigenvalues 0 but is not the zero matrix — eigenvalues alone
  don't determine the map unless diagonalizable.

## Related
- [[svd-and-pca]] — the eigen-decomposition of AᵀA, works for any A.
- [[matrices-and-linear-maps]], [[gaussian-elimination-lu]] (pivots), [[recurrences]].

## Sources
Strang lectures 21–28; Hefferon ch. 5; 3Blue1Brown ep. 14.

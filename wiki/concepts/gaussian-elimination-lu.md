---
title: Gaussian elimination, LU factorization, and determinants
type: concept
section: "1.2"
level: 200
tags: [gaussian-elimination, lu-factorization, pivoting, row-echelon-form, determinants, solving-linear-systems, back-substitution, numerical-stability, flops]
sources: [strang-18-06, hefferon-linear-algebra, boyd-vmls]
summary: How Ax=b is actually solved — elimination to upper-triangular form, recorded as A = LU (with a permutation for pivoting), back-substitution, ~2n³/3 flops — plus what the pivots tell you (rank, determinant, positive definiteness) and why determinants are for theory, not computation.
---
# Gaussian elimination, LU, determinants

**In one sentence.** Elimination subtracts multiples of rows to reach an upper-triangular U; the
multipliers form a lower-triangular L with A = LU (PA = LU with row swaps), and then solving is two
triangular solves.

## The algorithm
```
for k in 0..n-1:                   # column k
    pivot = row with largest |a[i][k]|, i >= k   (partial pivoting); swap into row k
    for i in k+1..n-1:
        m = a[i][k] / a[k][k]      # multiplier -> L[i][k]
        a[i][k..] -= m * a[k][k..]
# then Ly = Pb (forward), Ux = y (back-substitution)
```
Cost: ≈ 2n³/3 flops for the factorization, 2n² per solve. Factor once, solve for many right-hand
sides. Banded/sparse matrices cost far less (tridiagonal: O(n)).

## What elimination reveals
- **Pivots**: number of nonzero pivots = rank; a zero pivot with no swap available ⇒ singular.
- **Reduced row echelon form** (Gauss–Jordan) is unique and exposes pivot columns (a basis of the column
  space) and free columns (which give the nullspace) — [[four-fundamental-subspaces]].
- **Determinant** = ± product of pivots. Properties: det(AB) = det A det B, det Aᵀ = det A, swapping rows
  flips sign, det = 0 ⇔ singular; |det| = volume scaling factor (3Blue1Brown). Cofactor expansion is
  O(n!) and Cramer's rule is a theoretical curiosity — compute det via LU in O(n³).
- **Positive definite** symmetric A ⇔ all pivots > 0 ⇔ all eigenvalues > 0 ⇔ Cholesky A = LLᵀ exists
  (half the cost of LU, no pivoting needed) — [[eigenvalues-and-eigenvectors]].

## Numerical stability
- Partial pivoting is essential: eliminating with a tiny pivot amplifies round-off (growth factor).
  With pivoting, LU is backward stable in practice.
- Condition number κ(A) = ‖A‖‖A⁻¹‖ = σ_max/σ_min bounds relative error amplification: expect to lose
  log₁₀ κ digits. Ill-conditioned systems need QR/SVD or regularization ([[svd-and-pca]], [[floating-point]]).
- Never test `det(A) == 0` in floating point; use rank via SVD or a pivot tolerance.

## Related
- [[matrices-and-linear-maps]], [[four-fundamental-subspaces]].
- [[least-squares]] — for rectangular systems.
- [[orthogonality-and-projections]] — QR as the stable alternative.

## Sources
Strang lectures 2–4, 18–20; Hefferon ch. 1, 4; VMLS ch. 11.

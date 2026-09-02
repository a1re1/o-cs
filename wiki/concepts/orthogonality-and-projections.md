---
title: Orthogonality, projections, Gram–Schmidt, and QR
type: concept
section: "1.2"
level: 200
tags: [orthogonality, projection, projection-matrix, gram-schmidt, qr-factorization, orthonormal-basis, householder, orthogonal-matrices]
sources: [strang-18-06, boyd-vmls, 3b1b-essence-of-linear-algebra]
summary: Projecting b onto a subspace gives the closest point; with an orthonormal basis the projection is a sum of inner products, Gram–Schmidt manufactures such a basis (and doubles as an independence test), and A = QR is the numerically sound way to solve least squares.
---
# Orthogonality, projections, Gram–Schmidt, QR

**In one sentence.** The closest point to b in a subspace is its orthogonal projection, and orthonormal
bases make projections (and therefore least squares) a sequence of inner products.

## Projection
- Onto a line through a: p = (aᵀb / aᵀa) a; error e = b − p ⊥ a.
- Onto C(A) (independent columns): p = A(AᵀA)⁻¹Aᵀ b; the projection matrix P = A(AᵀA)⁻¹Aᵀ satisfies
  P² = P = Pᵀ. If A = Q has orthonormal columns, P = QQᵀ and p = Σ (qᵢᵀb) qᵢ.
- The orthogonal complement: Rᵐ = C(A) ⊕ N(Aᵀ); b = p + e uniquely ([[four-fundamental-subspaces]]).

## Gram–Schmidt (VMLS Algorithm 5.1)
For a₁…a_k: q̃ᵢ = aᵢ − Σ_{j<i} (qⱼᵀaᵢ)qⱼ; if q̃ᵢ = 0 the aᵢ are dependent (stop — this is the
independence test); else qᵢ = q̃ᵢ/‖q̃ᵢ‖. Cost ≈ 2nk². Output: A = QR with Q orthonormal columns
and R upper triangular (Rᵢⱼ = qᵢᵀaⱼ, Rᵢᵢ = ‖q̃ᵢ‖).

## QR in practice
- **Modified Gram–Schmidt** (orthogonalize against the running q's, not the original a's) or
  **Householder reflections** are used by libraries: classical GS loses orthogonality in floating
  point when columns are nearly dependent.
- Solve Ax = b (square) via QR: x = R⁻¹Qᵀb, 2n³ flops, more stable than LU without pivoting.
- Least squares: x̂ = R⁻¹Qᵀb — avoids forming AᵀA ([[least-squares]]).
- Orthogonal matrices preserve norms (‖Qx‖ = ‖x‖) so they never amplify round-off error — the reason
  numerical linear algebra is built from them (QR, SVD, Householder, Givens).

## Pitfalls
- Projection onto a *subspace* needs independent columns for (AᵀA)⁻¹; otherwise use QR/SVD.
- P is idempotent but not invertible (unless P = I).
- Orthogonal ≠ orthonormal; normalize before using P = QQᵀ.

## Related
- [[least-squares]], [[four-fundamental-subspaces]], [[gaussian-elimination-lu]], [[svd-and-pca]].
- [[vectors-and-inner-products]].

## Sources
Strang lectures 14–17; VMLS 5.3–5.4, 10.4, 11.x; 3Blue1Brown ep. 9.

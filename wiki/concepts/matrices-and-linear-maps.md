---
title: Matrices as linear maps (column picture, multiplication, inverses, transformations)
type: concept
section: "1.2"
level: 200
tags: [matrices, linear-maps, matrix-multiplication, column-picture, inverse, transpose, change-of-basis, geometric-transformations, incidence-matrix, convolution]
sources: [strang-18-06, boyd-vmls, hefferon-linear-algebra, 3b1b-essence-of-linear-algebra]
summary: A matrix is a linear map written in a basis — its columns are where the basis vectors land — so Ax is a combination of columns, AB is composition, the inverse undoes the map, and rotations, projections, selectors, graph incidence matrices and convolutions are all just matrices.
---
# Matrices as linear maps

**In one sentence.** Ax = x₁a₁ + … + xₙaₙ (a combination of the columns), so questions about
solving, invertibility, and rank are questions about the columns.

## Two pictures of Ax = b (Strang lecture 1)
- **Row picture**: each equation is a hyperplane; solve by intersecting.
- **Column picture**: find the combination of columns equal to b. Ax = b is solvable iff b is in the
  column space ([[four-fundamental-subspaces]]). This is the picture to think in.

## Multiplication as composition
(AB)x = A(Bx): apply B, then A. Four ways to compute AB — dot products of rows with columns, columns of
B mapped by A, rows of A mapped by B, sum of outer products (column k of A times row k of B). Cost
2mnp flops for m×n by n×p; not commutative; associative. Block multiplication works as if blocks were
scalars — the basis of cache-blocked and parallel matmul ([[cache-oblivious-algorithms]]).

## Inverse and transpose
- A⁻¹ exists iff A is square with independent columns (det ≠ 0, full rank, Ax = 0 only for x = 0).
  (AB)⁻¹ = B⁻¹A⁻¹. Compute by Gauss–Jordan on [A | I] in 2n³ flops — but *solve* systems with LU/QR
  instead of forming A⁻¹ ([[gaussian-elimination-lu]]).
- Transpose: (AB)ᵀ = BᵀAᵀ; (Ax)ᵀy = xᵀ(Aᵀy). Symmetric A = Aᵀ. Orthogonal Q: QᵀQ = I, preserves lengths
  and angles; Q⁻¹ = Qᵀ (cheap).
- **Change of basis**: if P's columns are the new basis, the same map has matrix P⁻¹AP — similar
  matrices share eigenvalues ([[eigenvalues-and-eigenvectors]]).

## Matrices you meet constantly (VMLS ch. 7)
| Matrix | Meaning |
|---|---|
| Rotation [[cos θ, −sin θ],[sin θ, cos θ]] | rotate by θ; orthogonal |
| Diagonal D | scale each coordinate; Dx cost n |
| Permutation / selector | reorder or pick entries; PᵀP = I |
| Projection P = P² = Pᵀ | drop the component orthogonal to a subspace |
| Incidence matrix of a graph (nodes × edges, ±1) | Kirchhoff's laws; Aᵀ A is the graph Laplacian |
| Toeplitz / circulant | convolution y = h * x; FFT diagonalizes circulant matrices |
| Low-rank uvᵀ | rank-one update; matmul with it is O(n) not O(n²) |

## Pitfalls
- Never invert a matrix to solve one system; never form AᵀA when a QR is available (squares the
  condition number, [[svd-and-pca]]).
- Rows vs columns: a linear map is determined by what it does to basis vectors — the *columns*.
- Element-wise product (Hadamard) is not matrix multiplication; NumPy `*` vs `@`.

## Related
- [[gaussian-elimination-lu]], [[four-fundamental-subspaces]], [[orthogonality-and-projections]].
- [[eigenvalues-and-eigenvectors]] — the invariant directions of a map.

## Sources
Strang lectures 1–3, 30–31; VMLS ch. 6–7, 10–11; Hefferon ch. 3; 3Blue1Brown eps. 3–4.

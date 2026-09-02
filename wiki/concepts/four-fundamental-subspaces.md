---
title: Four fundamental subspaces, rank, and rank–nullity
type: concept
section: "1.2"
level: 200
tags: [subspaces, column-space, nullspace, row-space, left-nullspace, rank, rank-nullity, basis, dimension, linear-independence, span]
sources: [strang-18-06, hefferon-linear-algebra]
summary: Column space C(A) and nullspace N(A) (with their transposes) organise everything about Ax=b — solvability, uniqueness, dimension counting — via rank r: dim C(A) = dim C(Aᵀ) = r, dim N(A) = n − r, dim N(Aᵀ) = m − r, with row space ⊥ nullspace.
---
# Four fundamental subspaces

**In one sentence.** For an m×n matrix of rank r, the column space (dim r) and left nullspace
(dim m−r) partition Rᵐ orthogonally, and the row space (dim r) and nullspace (dim n−r) partition Rⁿ.

## Definitions
- Span, linear independence (Σcᵢvᵢ = 0 only trivially), basis (independent + spanning), dimension
  (size of any basis — well defined). Test independence with elimination or Gram–Schmidt.
- **Column space** C(A) ⊆ Rᵐ: all Ax. Ax = b solvable ⇔ b ∈ C(A).
- **Nullspace** N(A) ⊆ Rⁿ: all x with Ax = 0. Solutions of Ax = b are x_particular + N(A) — unique
  iff N(A) = {0} iff columns independent.
- **Row space** C(Aᵀ) ⊆ Rⁿ and **left nullspace** N(Aᵀ) ⊆ Rᵐ.
- **Rank–nullity**: r + dim N(A) = n. Row rank = column rank (a real theorem, via elimination).
- **Orthogonality**: N(A) ⊥ C(Aᵀ) (each row is orthogonal to every nullspace vector) and
  N(Aᵀ) ⊥ C(A). Strang's "big picture": A maps the row space bijectively onto the column space and kills
  the nullspace.

## Computing them
Reduce to RREF R. Pivot columns of *A* (not R) form a basis of C(A); the nonzero rows of R form a basis
of C(Aᵀ); the special solutions (one free variable = 1, others 0) form a basis of N(A). Numerically use
the SVD: rank = number of singular values above tolerance ([[svd-and-pca]]).

## Why a programmer cares
- Underdetermined systems (n > m) have a whole affine space of solutions; pick the minimum-norm one
  (pseudoinverse) or add constraints.
- Overdetermined (m > n) usually have no solution ⇒ [[least-squares]] projects b onto C(A).
- Rank deficiency = redundant features/constraints/sensors; the nullspace tells you *which* combinations
  are unidentifiable.
- Graph incidence matrix A (m edges × n nodes): N(A) = constant vectors per connected component, so
  rank = n − #components; dim N(Aᵀ) = m − n + #components = number of independent cycles (Euler's formula
  in disguise, [[graph-theory-basics]]).

## Pitfalls
- Dimension ≠ number of vectors listed; check independence.
- The column space is not preserved by row operations (row space is); read C(A)'s basis from the
  original columns.

## Related
- [[gaussian-elimination-lu]], [[matrices-and-linear-maps]], [[orthogonality-and-projections]], [[least-squares]].

## Sources
Strang lectures 5–10, 12; Hefferon ch. 2–3.

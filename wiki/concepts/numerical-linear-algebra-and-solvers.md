---
title: Numerical Linear Algebra and Solvers
type: concept
section: "11.2"
level: 400
tags: [numerical-linear-algebra, conditioning, stability, lu-decomposition, iterative-solvers, ode-pde, sparse]
sources: [scientific-computing-texts-and-courses]
summary: Solving linear systems, least squares, and differential equations numerically — conditioning vs stability, direct (LU/QR) vs iterative (CG/GMRES) solvers, sparsity, and discretizing ODEs/PDEs.
---

# Numerical Linear Algebra and Solvers
**In one sentence.** The algorithms that solve `Ax = b`, least squares, eigenproblems,
and discretized differential equations on finite-precision hardware, and the theory —
conditioning and stability — that says when the answers can be trusted.

## Why it matters
Almost every simulation, optimization, graphics transform, and ML training step reduces
to numerical linear algebra. Getting it wrong doesn't crash — it silently returns a
plausible but wrong answer, because [[floating-point]] is not exact arithmetic.
Understanding conditioning and stability is the difference between a result and a
guess.

## How it works
**Conditioning vs stability (the two central ideas):**
- **Conditioning** is a property of the *problem*: the **condition number** `κ(A)`
  measures how much the solution can change for a small change in the input. An
  ill-conditioned system (`κ` huge) amplifies rounding error no matter the algorithm.
- **Stability** is a property of the *algorithm*: a backward-stable method returns the
  exact answer to a slightly perturbed problem. You need a stable algorithm *and* a
  well-conditioned problem to trust the result.

**Direct solvers (factorizations):**
- **LU decomposition** with partial pivoting solves `Ax=b` in O(n³); pivoting is what
  makes Gaussian elimination stable.
- **QR** (Gram-Schmidt/Householder) solves least squares `min ‖Ax−b‖` stably; **never**
  form the normal equations `AᵀA` naively — it squares the condition number.
- **Cholesky** for symmetric positive-definite systems (half the cost of LU).
- **SVD** is the most robust (and reveals rank/conditioning); see [[svd-and-pca]].

**Iterative solvers.** For large **sparse** systems (from PDEs), direct O(n³) is
infeasible. Iterative methods do only matrix-vector products (O(nnz) each):
- **Conjugate gradient (CG)** for symmetric positive-definite systems.
- **GMRES** for general nonsymmetric systems.
- **Preconditioning** transforms the system to improve conditioning and convergence —
  often the deciding factor in practice.

**Discretizing ODEs/PDEs.** Differential equations become linear/nonlinear systems:
- **ODEs** — step forward in time (Euler, Runge-Kutta); **stiff** problems need implicit
  methods for stability, echoing [[physics-simulation-and-collision-detection]].
- **PDEs** — finite differences (grid stencils) or finite elements (mesh basis
  functions) turn a PDE into a large sparse linear system solved iteratively. The
  **CFL condition** bounds the stable time step for explicit schemes.

## Complexity & trade-offs
- Direct solvers: O(n³) dense, exact-ish, robust, but memory-heavy; excellent for
  moderate dense systems and when you need many right-hand sides (reuse the factorization).
- Iterative solvers: O(nnz) per iteration, exploit sparsity, scale to millions of
  unknowns, but convergence depends on conditioning/preconditioning and they give only
  approximate solutions.

## Pitfalls & gotchas
- **Normal equations for least squares** square the condition number — use QR/SVD.
- **Ignoring conditioning** — a huge `κ(A)` means the answer is garbage regardless of
  algorithm; check it.
- **Explicit ODE/PDE steps on stiff problems** blow up unless the step obeys the
  stability limit; use implicit methods.
- **Inverting a matrix to solve `Ax=b`** — computing `A⁻¹` is slower and less stable than
  factoring and back-substituting.

## Worked example
A heat-equation PDE on a 1000×1000 grid gives a million-unknown sparse linear system
each time step. A dense LU (O(10¹⁸)) is impossible; instead, use conjugate gradient
with a multigrid preconditioner exploiting the sparse stencil structure, solving each
step in near-linear time — the standard scientific-computing workhorse.

## Related
- [[floating-point]] — why conditioning and stability matter.
- [[svd-and-pca]] — the most robust factorization.
- [[matrices-and-linear-maps]] — the underlying math.
- [[automatic-differentiation]] — gradients for optimization/PDE-constrained problems.
- [[parallel-architectures-simd-gpu]] — sparse solvers on HPC hardware.

## Sources
Distilled from [[scientific-computing-texts-and-courses]] (Heath; Trefethen & Bau
*Numerical Linear Algebra*; Numerical Recipes; Barba CFD Python).

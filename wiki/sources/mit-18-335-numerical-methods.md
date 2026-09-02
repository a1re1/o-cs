---
title: MIT 18.335 Introduction to Numerical Methods and Numerical Linear Algebra (Trefethen & Bau)
type: source
section: "1.6"
level: 400
tags: [numerical-methods, numerical-linear-algebra, floating-point, conditioning, stability, qr, svd, iterative-methods, krylov, eigenvalue-algorithms]
sources: []
authors: [Steven G. Johnson, Lloyd N. Trefethen, David Bau]
year: 2023
institution: MIT
url: https://github.com/mitmath/18335
license: CC-BY-NC-SA
format: html
summary: The graduate numerical linear algebra course (notes, pset, Julia notebooks on GitHub) following Trefethen & Bau — floating point and error analysis, conditioning vs stability, backward stability, QR/Householder, SVD, least squares, eigenvalue algorithms (QR iteration, Lanczos/Arnoldi), iterative solvers (conjugate gradient, GMRES), and the "why did my computation lose all its digits" toolkit.
---
# MIT 18.335 / Numerical Linear Algebra (Trefethen & Bau)

## What it is
Level 400. Topics: IEEE floating point, rounding, catastrophic cancellation; conditioning of problems
and stability of algorithms (backward error: the computed answer is the exact answer to a nearby
problem); Householder QR, Gram–Schmidt instability; SVD, low-rank approximation; least squares by QR/SVD;
eigenvalue algorithms (power iteration, QR algorithm with shifts, Rayleigh quotient, Lanczos/Arnoldi);
Krylov iterative methods (CG, GMRES) for sparse systems; preconditioning; a few weeks on FFTs, ODE
integrators, or automatic differentiation depending on the year. Course materials are on GitHub.

## Key ideas → pages
- Accuracy ≈ (condition number of the problem) × (backward error of the algorithm); a stable algorithm
  on an ill-conditioned problem still gives garbage — [[floating-point]], [[gaussian-elimination-lu]].
- Orthogonal transformations are the stable building blocks — [[orthogonality-and-projections]].
- Iterative Krylov methods make huge sparse systems tractable; CG converges in O(√κ log(1/ε))
  iterations — [[gradient-descent]] (conjugate gradient as the exact-arithmetic ideal).

## What it adds
The reasons behind the "never form AᵀA / never invert" rules stated in §1.2, with error bounds.

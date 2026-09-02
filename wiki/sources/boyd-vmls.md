---
title: Introduction to Applied Linear Algebra — Vectors, Matrices, and Least Squares (Boyd & Vandenberghe)
type: source
section: "1.2"
level: 200
tags: [linear-algebra, least-squares, regression, clustering, k-means, norms, flops, data-fitting, validation]
sources: []
authors: [Stephen Boyd, Lieven Vandenberghe]
year: 2018
institution: Stanford
url: https://web.stanford.edu/~boyd/vmls/
license: proprietary-open-access
format: pdf
summary: The free "VMLS" text — vectors, norms/distance, k-means, linear independence and Gram–Schmidt, matrices, linear equations, then least squares and its applications (data fitting, validation, classification, constrained and nonlinear least squares) — with flop counts for every algorithm and no eigenvalues at all.
---
# Introduction to Applied Linear Algebra (Boyd & Vandenberghe, 2018)

## What it is
Free PDF (Cambridge UP allows it), used for Stanford EE103/ENGR108. Three parts: **I Vectors**
(vectors, linear functions, norm & distance, clustering/k-means, linear independence & Gram–Schmidt),
**II Matrices** (matrices, examples: geometric transforms/selectors/incidence/convolution, linear
equations, linear dynamical systems, matrix multiplication, inverses), **III Least squares** (least
squares, data fitting, classification, multi-objective, constrained, nonlinear least squares, constrained
nonlinear). Deliberately omits eigenvalues, determinants and abstract vector spaces.

## Key ideas → pages
- Inner products, norms, RMS, cosine/angle, and **flop counts** (inner product 2n, matrix–vector
  2mn, Gram–Schmidt 2nk², solving Ax=b via QR 2n³) — [[vectors-and-inner-products]].
- k-means as alternating minimization of a clustering objective (assign, then recompute centroids) —
  [[k-means-clustering]].
- Gram–Schmidt as *the* independence test and the engine of QR — [[orthogonality-and-projections]].
- Least squares: minimize ‖Ax − b‖²; solution via normal equations AᵀAx̂ = Aᵀb or, numerically, QR;
  "x̂ need not satisfy Ax = b" — [[least-squares]].
- Data fitting: features, regression model y ≈ xᵀβ + v, polynomial fitting, out-of-sample
  **validation** (80/20 split) and cross-validation as the intuitive test of generalization;
  regularization (multi-objective least squares, ridge) — [[least-squares]].
- Floating point: 64-bit doubles, ~10 significant digits in practice, round-off means identities do not
  hold exactly — [[floating-point]].

## Notable claims & quotes
- "A least squares approximate solution x̂ of Ax = b need not satisfy the equations Ax = b."
- "The goal of model fitting is typically not to just achieve a good fit on the given data set, but
  rather to achieve a good fit on new data" — the whole ML validation story in one sentence.

## What it adds
Concrete algorithms with costs; a route from linear algebra straight to regression and classification
that §6.2 builds on. Pair with [[strang-18-06]] for eigenvalues and the SVD.

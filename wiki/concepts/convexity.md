---
title: Convex sets, convex functions, and convex optimization
type: concept
section: "1.6"
level: 400
tags: [convexity, convex-sets, convex-functions, jensen-inequality, global-optimum, disciplined-convex-programming, epigraph, subgradient, strong-convexity, lp, qp, socp, sdp]
sources: [boyd-convex-optimization]
summary: A problem is convex when the objective and feasible set are convex; then every local minimum is global, first-order conditions suffice, duality is tight, and polynomial-time interior-point methods exist — so the practical skill is recognizing or transforming problems into convex form (LP, QP, SOCP, SDP).
---
# Convexity

**In one sentence.** f is convex if f(θx + (1−θ)y) ≤ θf(x) + (1−θ)f(y) — chords lie above the
graph — and minimizing a convex function over a convex set has no spurious local minima.

## Recognizing convexity
- **Sets**: line segments stay inside. Examples: halfspaces, polyhedra, norm balls, PSD cone.
  Preserved by intersection, affine maps, perspective.
- **Functions**: first-order test f(y) ≥ f(x) + ∇f(x)ᵀ(y − x) (the tangent plane is a global
  underestimator); second-order test ∇²f ⪰ 0 ([[eigenvalues-and-eigenvectors]]). Examples: affine, eˣ,
  −log x, ‖x‖, x²/y (y > 0), log-sum-exp, max of convex functions, quadratic-over-linear, negative
  entropy. Concave: log, √x, geometric mean, min of affine.
- **Preserved by**: nonnegative weighted sums, pointwise max/sup, composition with affine maps,
  f(x) = h(g(x)) with h convex nondecreasing and g convex (the rules CVXPY checks — disciplined convex
  programming).
- **Jensen**: f(E[X]) ≤ E[f(X)] for convex f — the source of many inequalities
  ([[random-variables-expectation]], [[entropy-and-information]]).
- Strong convexity (∇²f ⪰ mI) gives unique minimizers and linear convergence rates
  ([[gradient-descent]]).

## Why convex problems are easy
- Local optimum ⇒ global optimum; the optimal set is convex.
- x* is optimal iff ∇f(x*)ᵀ(y − x*) ≥ 0 for all feasible y (unconstrained: ∇f = 0).
- Strong duality under Slater's condition; KKT conditions are necessary and sufficient
  ([[linear-programming-and-duality]]).
- Interior-point methods solve to high accuracy in tens of iterations, each a Newton step; problem
  size, not problem "hardness", determines cost.

## The standard classes (each contains the previous)
LP (linear objective/constraints) ⊂ QP (quadratic objective) ⊂ QCQP ⊂ SOCP (norm-cone constraints,
covers robust LP, Huber fitting) ⊂ SDP (matrix inequalities; relaxations of combinatorial problems
like max-cut). Geometric programs become convex after a log transform.

## Non-convex in practice
Deep learning losses, k-means, matrix factorization with missing data are non-convex; gradient methods
still work well empirically, but no global guarantee. Convex relaxations (lasso for sparsity, nuclear
norm for rank, SDP for max-cut) give tractable approximations with certificates.

## Pitfalls
- x ≥ 0 with integer constraints breaks convexity (integer programming is NP-hard).
- Equality constraints must be affine; h(x) = 0 with h convex but not affine is non-convex.
- Convexity of the *problem* depends on formulation: minimizing ‖Ax − b‖ subject to x ∈ {rank ≤ k}
  is non-convex, but the nuclear-norm version is convex.

## Related
- [[linear-programming-and-duality]], [[gradient-descent]], [[least-squares]], [[derivatives-and-gradients]].

## Sources
Boyd & Vandenberghe ch. 2–4.

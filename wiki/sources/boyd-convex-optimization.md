---
title: Convex Optimization (Boyd & Vandenberghe) and Stanford EE364A
type: source
section: "1.6"
level: 400
tags: [convex-optimization, convex-sets, convex-functions, duality, kkt, linear-programming, interior-point, gradient-descent, newton-method]
sources: []
authors: [Stephen Boyd, Lieven Vandenberghe]
year: 2004
institution: Stanford
url: https://web.stanford.edu/~boyd/cvxbook/
license: proprietary-open-access
format: pdf
summary: The standard graduate text (free PDF) and its course EE364A — convex sets and functions, recognizing and transforming convex problems (LP, QP, SOCP, SDP, geometric programs), Lagrangian duality and KKT conditions, applications (approximation, statistical estimation, geometric problems), and unconstrained/equality-constrained/interior-point algorithms with convergence proofs.
---
# Convex Optimization (Boyd & Vandenberghe, 2004)

## What it is
Part I Theory: convex sets (affine/convex hulls, cones, separating hyperplanes, dual cones); convex
functions (first/second-order conditions, operations preserving convexity, conjugates, quasiconvexity,
log-concavity); convex optimization problems (standard form, LP, QP/QCQP, SOCP, SDP, geometric programming,
vector optimization); duality (Lagrangian, weak/strong duality, Slater, KKT, sensitivity). Part II
Applications: approximation and fitting (norm approximation, regularization, robust), statistical
estimation (MLE as convex problem, experiment design), geometric problems. Part III Algorithms:
unconstrained minimization (descent methods, gradient, steepest descent, Newton, self-concordance),
equality-constrained, interior-point (barrier, primal-dual). Appendices on linear algebra and numerics.
EE364A lectures/slides/homework and the CVX/CVXPY modeling tools are open.

## Key ideas → pages
- Convexity is the dividing line: local = global optimum, duality gap zero (with Slater), efficient
  interior-point solvers — [[convexity]].
- "Recognize or transform your problem into a convex one" (the book's thesis) — the disciplined convex
  programming rules behind CVXPY — [[convexity]], [[linear-programming-and-duality]].
- Gradient descent with backtracking line search converges linearly on strongly convex f: error shrinks by
  (1 − m/M) per step, where m, M bound the Hessian; the ratio M/m is the condition number —
  [[gradient-descent]].
- Newton's method: affine invariant, quadratic convergence near the optimum, self-concordance gives
  complexity bounds — [[gradient-descent]].
- Lagrangian L(x, λ, ν) = f₀ + Σλᵢfᵢ + Σνᵢhᵢ; dual function g(λ, ν) = inf_x L ≤ p*; KKT conditions
  (stationarity, primal/dual feasibility, complementary slackness) — [[linear-programming-and-duality]].

## Notable claims
- "With only a bit of exaggeration, we can say that, if you formulate a practical problem as a convex
  optimization problem, then you have solved the original problem."
- The gradient method's iteration count depends on log((f(x⁰) − p*)/ε)/log(1/(1 − m/M)) — crude, but it
  shows why conditioning dominates.

## What it adds
The theory that makes [[least-squares]] and [[maximum-likelihood-estimation]] special cases, and the
vocabulary (KKT, duality, conditioning) used throughout ML optimization (§6.2–6.3).

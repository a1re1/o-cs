---
title: Linear programming, Lagrangian duality, and KKT conditions
type: concept
section: "1.6"
level: 400
tags: [linear-programming, simplex, duality, weak-duality, strong-duality, lagrangian, kkt-conditions, complementary-slackness, slater-condition, interior-point, lp-relaxation, dual-certificate]
sources: [boyd-convex-optimization]
summary: LPs (maximize cᵀx subject to Ax ≤ b, x ≥ 0) are solved by simplex or interior-point methods; every constrained problem has a Lagrangian dual whose value lower-bounds the primal (weak duality), equals it for convex problems under Slater (strong duality), and whose optimal multipliers are sensitivities; the KKT conditions turn "is this optimal?" into equations and the dual solution into a certificate.
---
# Linear programming and duality

**In one sentence.** Every minimization has a dual maximization whose value never exceeds it; when the
gap closes, the dual solution certifies optimality and prices the constraints.

## Linear programs
Standard form min cᵀx s.t. Ax = b, x ≥ 0 (any LP converts to it with slack variables). Feasible set is a
polyhedron; an optimum (if it exists) occurs at a vertex. **Simplex** walks vertices (exponential worst
case, fast in practice); **interior-point** methods are polynomial (Karmarkar 1984) and dominate for
large sparse LPs; **ellipsoid** (Khachiyan 1979) proved LP ∈ P. Integer LP is NP-hard; LP relaxations plus
rounding give approximation algorithms ([[approximation-algorithms]]). Max-flow/min-cut, bipartite
matching, shortest paths are LPs with totally unimodular constraint matrices (integral vertices) —
[[network-flow]].

## Lagrangian duality (Boyd ch. 5)
Primal: min f₀(x) s.t. fᵢ(x) ≤ 0, hⱼ(x) = 0. Lagrangian L(x, λ, ν) = f₀(x) + Σλᵢfᵢ(x) + Σνⱼhⱼ(x),
λ ≥ 0. Dual function g(λ, ν) = inf_x L — always concave (inf of affine functions), and
**weak duality** g(λ, ν) ≤ p* for every λ ≥ 0. Dual problem: max g. **Strong duality** d* = p* holds
for convex problems satisfying **Slater's condition** (a strictly feasible point) and for all feasible
LPs. Examples: LP dual (max bᵀy s.t. Aᵀy ≤ c), the dual of least-norm is a quadratic, the dual of
lasso/SVM problems reveals kernels ([[support-vector-machines]]).

## KKT conditions
At (x*, λ*, ν*) with strong duality:
1. primal feasibility fᵢ(x*) ≤ 0, hⱼ(x*) = 0;
2. dual feasibility λ* ≥ 0;
3. **complementary slackness** λᵢ*fᵢ(x*) = 0 (a constraint is either tight or its multiplier is 0);
4. stationarity ∇f₀ + Σλᵢ*∇fᵢ + Σνⱼ*∇hⱼ = 0.
Necessary and sufficient for convex problems; for non-convex problems necessary under constraint
qualifications. Multipliers are **shadow prices**: ∂p*/∂bᵢ = −λᵢ* (sensitivity of the optimum to
loosening constraint i).

## Uses
- Certify optimality (a dual feasible point with matching value) — solvers report the duality gap.
- Decomposition: dual variables coordinate subproblems (dual decomposition, ADMM) in distributed
  optimization and network utility maximization ([[congestion-control]] interprets TCP this way).
- Derive algorithms: SVM dual, ridge closed forms, water-filling for channel capacity
  ([[channel-capacity-and-error-correction]]).
- Lower bounds in combinatorial optimization (LP duality proves max-flow = min-cut, König's theorem).

## Pitfalls
- Strong duality can fail for non-convex problems (positive duality gap) and even for convex ones
  without Slater.
- Sign conventions for λ vary between texts; check whether constraints are ≤ 0 or ≥ 0.
- Unbounded primal ⇒ infeasible dual and vice versa.

## Related
- [[convexity]], [[gradient-descent]], [[network-flow]], [[approximation-algorithms]].

## Sources
Boyd & Vandenberghe ch. 4.3 (LP), 5 (duality, KKT), 11 (interior-point).

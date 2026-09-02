---
title: Derivatives, chain rule, gradients, Jacobians, Hessians, and Taylor approximation
type: concept
section: "1.3"
level: 200
tags: [derivatives, chain-rule, gradient, jacobian, hessian, taylor-series, linearization, partial-derivatives, critical-points, lagrange-multipliers, backpropagation, numerical-differentiation]
sources: [strang-calculus, boyd-vmls]
summary: The derivative is the best linear approximation; the chain rule composes local linear maps (which is all backpropagation does); gradients point uphill and vanish at optima; the Hessian's definiteness classifies critical points; Taylor's first and second order expansions justify gradient descent and Newton's method.
---
# Derivatives, gradients, Taylor approximation

**In one sentence.** f(x + h) ≈ f(x) + f′(x)h: the derivative is the slope of the local linear
model, and everything in optimization and deep learning is built by composing such models.

## Single variable
- f′(x) = lim (f(x+h) − f(x))/h. Rules: product, quotient, **chain rule** (f∘g)′ = f′(g(x))·g′(x).
- Standard derivatives: xⁿ → nxⁿ⁻¹; eˣ → eˣ; ln x → 1/x; sin → cos; σ(x) = 1/(1+e⁻ˣ) → σ(1−σ);
  tanh → 1 − tanh²; softplus → σ; ReLU → step (0 at 0 by convention).
- **Taylor**: f(x+h) = f(x) + f′(x)h + ½f″(x)h² + O(h³). First order ⇒ gradient descent step
  x − αf′(x) decreases f for small α; second order ⇒ Newton step x − f′/f″.
- Critical points f′ = 0: min if f″ > 0, max if f″ < 0, inconclusive if f″ = 0.

## Several variables
- **Gradient** ∇f ∈ Rⁿ (partials); directional derivative = ∇fᵀd; ∇f points in the direction of
  steepest ascent and is orthogonal to level sets. Linearization: f(x+h) ≈ f(x) + ∇f(x)ᵀh (VMLS 2.2).
- **Jacobian** J ∈ R^{m×n} of F: Rⁿ → Rᵐ; chain rule: J_{F∘G} = J_F(G(x)) · J_G(x) — matrix
  multiplication of local linear maps. Reverse-mode autodiff evaluates vᵀJ products from the output
  backwards (cost ≈ one forward pass per output), forward-mode evaluates Jv (one pass per input);
  backpropagation is reverse mode on a scalar loss ([[backpropagation]], [[automatic-differentiation]]).
- **Hessian** H (symmetric matrix of second partials). Second-order Taylor: f(x+h) ≈ f + ∇fᵀh + ½hᵀHh.
  At a critical point: H positive definite ⇒ local min, negative definite ⇒ max, indefinite ⇒ saddle
  ([[eigenvalues-and-eigenvectors]]). Condition number of H governs gradient-descent speed ([[gradient-descent]]).
- Useful gradients: ∇(aᵀx) = a; ∇(xᵀAx) = (A + Aᵀ)x; ∇‖Ax − b‖² = 2Aᵀ(Ax − b) (hence the normal
  equations, [[least-squares]]).
- **Lagrange multipliers**: at a constrained optimum of f subject to g = 0, ∇f = λ∇g (gradients
  parallel); generalizes to KKT conditions (§1.6).

## Numerical differentiation
Finite differences (f(x+h) − f(x−h))/2h with h ≈ 10⁻⁵ (double precision) — use only to *check* an
analytic/autodiff gradient (gradient checking), never in production ([[floating-point]]).

## Pitfalls
- Chain-rule bookkeeping errors with shapes: write Jacobian dimensions explicitly (m×n)(n×p).
- Nondifferentiable points (ReLU at 0, |x|) — subgradients; max/abs are fine in practice.
- Vanishing/exploding products of many Jacobians in deep networks — the reason for careful
  initialization and normalization (§6.3).

## Related
- [[integrals-and-sums]], [[least-squares]], [[gradient-descent]], [[convexity]] (§1.6).

## Sources
Strang Calculus ch. 2–4, 10, 13; VMLS 2.2 (Taylor approximation); 18.02 gradients/Lagrange lectures.

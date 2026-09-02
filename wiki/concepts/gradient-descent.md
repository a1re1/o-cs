---
title: Gradient descent, Newton's method, and first-order optimization
type: concept
section: "1.6"
level: 400
tags: [gradient-descent, line-search, backtracking, convergence-rate, condition-number, newton-method, conjugate-gradient, sgd, momentum, adam, learning-rate, strong-convexity, lipschitz-gradient]
sources: [boyd-convex-optimization, mit-18-335-numerical-methods]
summary: Step against the gradient with a step size from a line search or a fixed schedule; on strongly convex functions the error shrinks geometrically by (1 − m/M) per step so conditioning M/m sets the iteration count; Newton's method fixes conditioning at O(n³) per step; conjugate gradient and momentum sit between; SGD trades exact gradients for cheap noisy ones and dominates machine learning.
---
# Gradient descent and friends

**In one sentence.** x ← x − t∇f(x) decreases f for small enough t because the Taylor expansion
f(x − t∇f) ≈ f − t‖∇f‖² ([[derivatives-and-gradients]]); everything else is about choosing t and the
direction so convergence is fast despite bad conditioning.

## The algorithm (Boyd Algorithm 9.3)
```
repeat:
    d = -grad f(x)
    choose t by exact or backtracking line search   # backtracking: t=1; while f(x+t d) > f(x) + a t grad·d: t *= b  (a≈0.3, b≈0.8)
    x = x + t d
until ||grad f(x)|| <= eta
```
Fixed step t ≤ 1/M also works when ∇f is M-Lipschitz (∇²f ⪯ MI).

## Convergence (strongly convex, mI ⪯ ∇²f ⪯ MI)
f(x⁽ᵏ⁾) − p* ≤ (1 − m/M)ᵏ (f(x⁽⁰⁾) − p*): **linear convergence**, iterations ≈ (M/m) log(1/ε).
κ = M/m is the condition number of the Hessian ([[eigenvalues-and-eigenvectors]]); level sets are
ellipsoids with axis ratio √κ and steepest descent zig-zags across the narrow direction. Without strong
convexity (merely convex, Lipschitz gradient): O(1/k) sublinear; Nesterov acceleration gives O(1/k²)
and √κ dependence — optimal for first-order methods.

## Fixes for conditioning
- **Preconditioning / feature scaling**: change variables so the Hessian is closer to I (standardize
  inputs; diagonal preconditioners; Adam's per-coordinate scaling is an adaptive one).
- **Newton's method**: d = −∇²f⁻¹∇f; affine invariant (κ irrelevant), quadratic convergence near the
  optimum (digits double each step), but O(n³) per step and needs damping (line search) far away.
  Quasi-Newton (BFGS, L-BFGS) approximates the Hessian from gradient differences — the default for
  smooth medium-scale problems.
- **Conjugate gradient**: for quadratics (linear systems Ax = b, A ⪰ 0) converges in n steps exactly and
  in O(√κ log 1/ε) steps to tolerance; the model for momentum methods; Krylov cousins GMRES/MINRES
  for non-symmetric ([[mit-18-335-numerical-methods]]).
- **Momentum / heavy ball / Nesterov**: keep a velocity; achieves the √κ rate.

## Stochastic gradient descent
Replace ∇f = (1/n)Σ∇fᵢ by a minibatch estimate: cost per step independent of n. Converges to a noise
ball of radius ∝ learning rate; decay the rate (1/√k or schedules) or average iterates. Adam/RMSProp/
AdaGrad add per-coordinate adaptive scaling; weight decay = L2 regularization. In deep learning the
noise is also a regularizer and the landscape is non-convex, so the theory here gives intuition, not
guarantees ([[neural-network-training]]).

## Practical checklist
1. Scale features / parameters. 2. Verify gradients numerically once. 3. Start with a backtracking or
small fixed step; watch f decrease monotonically (if not, step too large). 4. Stop on ‖∇f‖ or relative
change. 5. If slow and n is moderate, switch to L-BFGS/Newton; if n is huge, minibatch SGD.
6. Non-smooth terms (L1, hinge): subgradients or proximal gradient (ISTA/FISTA).

## Pitfalls
- Learning rate too large diverges; too small crawls — plot the loss.
- Exact line search is rarely worth it; backtracking is.
- Newton on non-convex f can climb to a saddle/max; use trust regions or add damping.
- Gradient descent finds stationary points; on non-convex problems that can be saddles (though random
  perturbations escape them).

## Related
- [[convexity]], [[derivatives-and-gradients]], [[least-squares]], [[linear-programming-and-duality]],
  [[floating-point]].

## Sources
Boyd & Vandenberghe 9.2–9.5 (descent methods, gradient, steepest descent, Newton), 10–11; 18.335 notes on CG/Krylov.

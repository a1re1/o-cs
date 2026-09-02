---
title: Nonlinear Optimization
type: concept
section: "6.2"
level: 400
tags: [optimization, gradient-descent, convexity, newton-method, constrained-optimization, lagrange-multipliers]
sources: [deep-learning-texts-courses-and-seminal-papers]
summary: Minimizing smooth nonlinear objectives — gradient descent and its variants, second-order (Newton/quasi-Newton) methods, convex vs nonconvex landscapes, and constrained optimization via Lagrange multipliers and KKT.
---

# Nonlinear Optimization
**In one sentence.** Nonlinear optimization finds inputs that minimize (or maximize) a
smooth nonlinear objective, using derivative information to iteratively descend toward a
(local) optimum, possibly subject to constraints.

## Why it matters
Nearly all of machine learning is optimization: training a model *is* minimizing a loss.
The same machinery solves control, portfolio, and engineering-design problems.
Understanding convexity, conditioning, and constraints explains why training works, why
it sometimes doesn't, and which method to reach for.

## How it works
**Unconstrained: descend using gradients.**
- **Gradient descent** — step opposite the gradient, `x ← x − η∇f(x)`; see
  [[gradient-descent]]. Convergence and step size depend on conditioning.
- **Momentum / Nesterov** — accumulate a velocity to accelerate through ravines and damp
  oscillation.
- **Adaptive methods (Adam, RMSProp)** — per-coordinate learning rates; the workhorses of
  deep learning.
- **Second-order (Newton's method)** — use the Hessian: `x ← x − H⁻¹∇f`, quadratic
  convergence near the optimum but O(n³) per step. **Quasi-Newton (BFGS/L-BFGS)**
  approximate the Hessian from gradients — excellent for smooth medium-scale problems.

**Convex vs nonconvex.**
- A **convex** objective has one global minimum and any local minimum is global —
  optimization is reliable (see [[convexity]]). Least squares, logistic regression, SVMs.
- **Nonconvex** objectives (neural nets) have many local minima and saddle points; SGD
  nonetheless finds good solutions in practice because most minima are comparably good and
  saddles are escapable with noise.

**Constrained optimization.** Minimize `f(x)` subject to constraints `g(x) ≤ 0`,
`h(x) = 0`:
- **Lagrange multipliers** handle equality constraints by forming the Lagrangian and
  setting its gradient to zero.
- The **KKT conditions** generalize this to inequalities (stationarity, primal/dual
  feasibility, complementary slackness) — the optimality conditions behind SVMs and
  much of [[linear-programming-and-duality]]'s nonlinear cousin, convex programming.

## Complexity & trade-offs
- First-order methods cost O(n) per step and scale to billions of parameters (deep
  learning) but converge slowly on ill-conditioned problems.
- Second-order methods converge in far fewer steps but each step is expensive
  (Hessian/inverse); L-BFGS is the practical middle ground for smooth problems that fit.
- Step size (learning rate) is the key knob: too large diverges, too small crawls.

## Pitfalls & gotchas
- **Ill-conditioning** — elongated valleys make plain gradient descent zig-zag; use
  momentum, adaptive methods, or preconditioning.
- **Wrong learning rate** is the most common training failure; tune or schedule it.
- **Assuming a local min is global** on nonconvex problems — it isn't guaranteed.
- **Ignoring constraints' feasibility** — projecting or penalizing incorrectly gives
  invalid solutions.

## Worked example
Training logistic regression minimizes a convex cross-entropy loss: gradient descent (or
L-BFGS) converges to the unique global optimum regardless of initialization. Swap in a
neural network and the loss becomes nonconvex — Adam still finds a good local minimum, but
the run now depends on initialization, learning rate, and batch noise.

## Related
- [[gradient-descent]] — the first-order core.
- [[convexity]] — when optimization is guaranteed to succeed.
- [[neural-network-training]] — nonconvex optimization in practice.
- [[linear-programming-and-duality]] — the linear/convex constrained case.
- [[numerical-linear-algebra-and-solvers]] — the linear algebra inside Newton steps.

## Sources
Distilled from [[deep-learning-texts-courses-and-seminal-papers]] (Boyd & Vandenberghe *Convex
Optimization*; Nocedal & Wright *Numerical Optimization*; CS229).

---
title: Automatic Differentiation
type: concept
section: "11.2"
level: 400
tags: [automatic-differentiation, autodiff, backpropagation, forward-mode, reverse-mode, dual-numbers, jacobian]
sources: [scientific-computing-texts-and-courses]
summary: Computing exact derivatives of programs by the chain rule — forward mode (dual numbers) vs reverse mode (backpropagation), their cost trade-offs, and why reverse mode powers deep learning.
---

# Automatic Differentiation
**In one sentence.** Automatic differentiation (AD) computes exact derivatives of a
function expressed as a program by mechanically applying the chain rule to its
elementary operations — not symbolic manipulation, and not finite-difference
approximation.

## Why it matters
AD is the engine under deep-learning training (backpropagation is reverse-mode AD),
gradient-based optimization, sensitivity analysis, and differentiable physics/graphics.
It gives derivatives to machine precision at a small constant factor over evaluating the
function — dramatically better than the two flawed alternatives below.

## How it works
**Why not the alternatives:**
- **Numerical (finite differences)** `(f(x+h) − f(x))/h` — simple but inaccurate
  (truncation vs [[floating-point]] roundoff trade-off) and costs one evaluation per
  input dimension.
- **Symbolic differentiation** — produces exact formulas but suffers *expression swell*
  and can't handle control flow/loops in a program.

AD sidesteps both: it treats the program as a composition of elementary ops (`+`, `×`,
`sin`, `exp`) with known local derivatives and composes them by the chain rule.

**Forward mode.** Carry a derivative alongside each value — a **dual number**
`a + b·ε` with `ε²=0`, where `b` tracks the derivative. One forward pass computes the
function and its derivative *with respect to one input*. Cost ∝ number of **inputs**, so
efficient when inputs ≪ outputs.

**Reverse mode (backpropagation).** Do a forward pass recording the computation graph,
then a backward pass propagating derivatives of the output back to every input via the
chain rule (accumulating **adjoints**). One backward pass gives the gradient with
respect to *all* inputs at once. Cost ∝ number of **outputs**, so ideal for scalar-loss
functions of millions of parameters — exactly deep learning.

**Rule of thumb:** for `f: ℝⁿ → ℝᵐ`, forward mode costs ~n passes, reverse mode ~m
passes. Neural nets have `m=1` (scalar loss) and huge `n`, so reverse mode wins
overwhelmingly — that is why it dominates ML.

## Complexity & trade-offs
- Reverse mode gives the full gradient in O(1) function-evaluations of time but must
  **store the computation graph / intermediate activations** — O(operations) memory.
  This memory cost is why training large models is memory-bound; **gradient
  checkpointing** trades recompute for memory.
- Forward mode is memory-cheap and simple but costs one pass per input — good for few
  inputs or Jacobian-vector products.

## Pitfalls & gotchas
- **Non-differentiable points** (`abs`, `relu` at 0, `max`) — AD returns *a* subgradient
  by convention; usually fine but be aware.
- **In-place mutation / non-recorded ops** break the graph in reverse mode; frameworks
  forbid or specially handle them.
- **Confusing AD with numerical differentiation** — AD is exact (to floating point),
  not an `h`-approximation.
- **Control flow** — AD differentiates the path *taken*; a branch on the input is a
  discontinuity AD won't smooth.

## Worked example
For `f(x, y) = x·y + sin(x)`, reverse mode forward-computes `v1=x·y`, `v2=sin(x)`,
`f=v1+v2`; then backpropagates adjoints: `∂f/∂v1=1`, `∂f/∂v2=1`, giving `∂f/∂x = y +
cos(x)` and `∂f/∂y = x` in one backward pass — both partials from a single sweep, the
same mechanism that computes gradients for a billion-parameter network.

## Related
- [[deep-learning-basics]] — backpropagation is reverse-mode AD.
- [[derivatives-and-gradients]] — the calculus AD automates.
- [[numerical-linear-algebra-and-solvers]] — gradients drive optimization/solvers.
- [[floating-point]] — why finite differences are inferior to AD.

## Sources
Distilled from [[scientific-computing-texts-and-courses]] (Griewank & Walther
*Evaluating Derivatives*; MIT 18.S191; Baydin et al. AD survey).

---
title: Calculus (Strang) and MIT 18.01/18.02
type: source
section: "1.3"
level: 100
tags: [calculus, derivatives, integrals, multivariable, gradients, taylor-series, chain-rule]
sources: []
authors: [Gilbert Strang]
year: 1991
institution: MIT
url: https://ocw.mit.edu/courses/res-18-001-calculus-fall-2023/
license: CC-BY-NC-SA
format: pdf
summary: Strang's free calculus text (with the "Highlights of Calculus" videos) plus OCW 18.01 single-variable and 18.02 multivariable; the CS-relevant core is derivatives/chain rule, Taylor approximation, integrals as sums, and gradients/Jacobians/Hessians for optimization.
---
# Calculus (Strang) with MIT 18.01 / 18.02

## What it is
Free PDF textbook (17 chapters) and video series. Chapters relevant to CS: 2–4 derivatives and the
chain rule; 5 integrals; 8 applications of the integral; 10 infinite series (Taylor); 11 vectors and
matrices; 13 partial derivatives (gradients, tangent planes, second derivatives/Hessian, constrained
optimization with Lagrange multipliers); 14 multiple integrals. 18.01/18.02 on OCW follow the same arc
with problem sets and exams.

## Key ideas → pages
- Derivative as best linear approximation; chain rule as multiplication of local slopes — the rule
  backpropagation applies mechanically — [[derivatives-and-gradients]].
- Taylor expansion f(x+h) ≈ f(x) + f′(x)h + ½f″(x)h²; first-order for gradient descent, second-order for
  Newton's method — [[derivatives-and-gradients]].
- Integrals as limits of Riemann sums; the integral test for bounding sums — [[integrals-and-sums]],
  used in [[asymptotic-notation]].
- Gradient, Jacobian, Hessian; critical points; Lagrange multipliers for equality constraints —
  [[derivatives-and-gradients]].

## What it adds
Enough single- and multivariable calculus to read optimization (§1.6), probability densities (§1.4)
and machine learning (§6); the rest of calculus (trigonometric integrals, series convergence tests)
is rarely needed and left to the source.

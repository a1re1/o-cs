---
title: Scientific Computing & Computational Physics — Texts and Courses
type: source
section: "11.2"
level: 400
tags: [scientific-computing, numerical-methods, ode-pde, sparse-linear-algebra, automatic-differentiation]
authors: Heath; Press et al.; Barba
year: 2018
institution: MIT, Berkeley, Harvard
url: https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/
license: mixed
format: texts+courses
sources: []
summary: The scientific-computing canon — Heath's Scientific Computing, Numerical Recipes, MIT 18.335 and Berkeley CS267, and Barba's CFD Python — covering numerical linear algebra, ODE/PDE solvers, Monte Carlo, and automatic differentiation.
---

# Scientific Computing & Computational Physics — Texts and Courses

## What it is
The discipline of solving continuous mathematical models (differential equations,
linear systems, optimization) approximately on computers, with attention to accuracy,
stability, and performance. It is the computational engine of physics, engineering, and
increasingly machine learning.

## Key ideas
- **Numerical linear algebra** — solving `Ax=b`, eigenproblems, least squares, with
  attention to conditioning and stability. See [[numerical-linear-algebra-and-solvers]].
- **ODE/PDE solvers** — discretizing differential equations (finite difference/element),
  stability. See [[numerical-linear-algebra-and-solvers]].
- **Automatic differentiation** — computing exact derivatives of programs. See
  [[automatic-differentiation]].
- **Monte Carlo** — randomized numerical integration and simulation. See
  [[monte-carlo-methods]].

## Chapter / lecture map
- **Heath, *Scientific Computing*** — the balanced survey: linear systems,
  interpolation, ODEs, PDEs, optimization, FFT.
- **Press et al., *Numerical Recipes*** — algorithms with code and caveats.
- **MIT 18.335 (numerical methods), Berkeley CS267 (parallel scientific computing)** —
  the graduate courses; CS267 emphasizes HPC.
- **Barba, *CFD Python* ("12 steps to Navier-Stokes", free)** — hands-on PDE solving.
- **MIT 18.S191 *Introduction to Computational Thinking* (Julia, free)** — modern,
  differentiable scientific computing.

## Notable claims & quotes
- The central lesson: **floating-point is not the reals** — conditioning (sensitivity of
  the problem) and stability (behavior of the algorithm) determine whether an answer is
  trustworthy. See [[floating-point]].
- Sparse structure is everything at scale: exploiting zeros turns intractable dense
  O(n³) solves into feasible sparse ones.

## What it adds
The rigorous numerical foundation under graphics, ML, simulation, and engineering. It
connects to [[floating-point]] (rounding and stability), [[matrices-and-linear-maps]]
(the math), [[monte-carlo-methods]], [[parallel-architectures-simd-gpu]] (HPC), and
[[automatic-differentiation]] (the bridge to deep learning's backprop).

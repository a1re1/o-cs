---
title: Random variables, expectation, variance, and conditional expectation
type: concept
section: "1.4"
level: 200
tags: [random-variables, pmf, pdf, cdf, expectation, linearity-of-expectation, indicator-variables, variance, covariance, lotus, conditional-expectation, law-of-total-expectation, adams-law, eves-law]
sources: [blitzstein-stat110, cs109-probability-for-computer-scientists, mcs-lehman-leighton-meyer]
summary: A random variable is a function on the sample space; PMF/PDF/CDF describe it; expectation is linear regardless of independence (the indicator trick), variance is E[X²] − (E[X])², and conditional expectation with the laws of total expectation and total variance turn messy analyses into first-step recursions.
---
# Random variables and expectation

**In one sentence.** E[X + Y] = E[X] + E[Y] always, so write the quantity you care about as a sum of
simple (often indicator) variables and add their expectations — the single most powerful trick in
probabilistic analysis.

## Describing a random variable
- **PMF** p(x) = P(X = x) (discrete); **PDF** f with P(a ≤ X ≤ b) = ∫ₐᵇ f (continuous); **CDF**
  F(x) = P(X ≤ x) works for both and is the right object for comparing distributions and computing
  percentiles ([[think-stats-downey]]).
- **Expectation** E[X] = Σ x p(x) or ∫ x f(x) dx; **LOTUS**: E[g(X)] = Σ g(x)p(x) — no need for the
  distribution of g(X).
- **Variance** Var(X) = E[(X − μ)²] = E[X²] − μ²; SD = √Var; Var(aX + b) = a²Var(X).
  **Covariance** Cov(X,Y) = E[XY] − E[X]E[Y]; correlation ρ = Cov/(σ_Xσ_Y) ∈ [−1, 1]; independent ⇒
  uncorrelated, not conversely.
- Var(X + Y) = Var X + Var Y + 2Cov(X,Y); for pairwise independent (or uncorrelated) variables variances
  add. Hence the sample mean of n i.i.d. copies has variance σ²/n — the √n law.

## The indicator trick (fundamental bridge)
For an event A, I_A ∈ {0,1} and E[I_A] = P(A). Any count "number of things that happen" is Σ I_i, so
E[count] = Σ P(A_i) even when the A_i are wildly dependent.
- Hat-check: n people get random hats; E[#own hat] = n · 1/n = 1.
- Birthday: E[#colliding pairs] = C(n,2)/d.
- Expected number of records/fixed points/comparisons in quicksort ([[probabilistic-analysis-of-algorithms]]).
- Second moments: Var of a sum of indicators needs Cov(I_i, I_j) = P(A_i ∩ A_j) − P(A_i)P(A_j).

## Conditional expectation
E[X | Y = y] is a number; E[X | Y] is a random variable (function of Y).
- **Law of total expectation (Adam's law)**: E[X] = E[E[X | Y]] = Σ_y E[X | Y=y] P(Y=y). CS109's
  distributed-file-system example: E[fetch time] = Σ_location E[time | location]·P(location).
- **Law of total variance (Eve's law)**: Var(X) = E[Var(X|Y)] + Var(E[X|Y]) — "within" plus "between".
- **First-step analysis**: condition on the first trial/step to get an equation for an expectation —
  expected number of coin flips until HH, expected time to absorb in a Markov chain, expected running
  time of a randomized algorithm ([[markov-chains]]).
- Wald's identity: E[Σ_{i=1}^{N} X_i] = E[N]E[X] when N is a stopping time independent of the X's.

## Pitfalls
- E[1/X] ≠ 1/E[X], E[X²] ≠ (E[X])² (Jensen: for convex g, E[g(X)] ≥ g(E[X])).
- E[XY] = E[X]E[Y] requires independence (or uncorrelatedness); linearity does not.
- Infinite expectations exist (St. Petersburg, Cauchy has no mean); heavy tails break "average" reasoning.
- Conditioning on a zero-probability event needs densities, not the ratio formula.

## Related
- [[four-step-method]], [[common-distributions]], [[concentration-inequalities]],
  [[central-limit-theorem-and-lln]], [[probabilistic-analysis-of-algorithms]].

## Sources
Blitzstein ch. 3–4, 7, 9; CS109 reader Part 2 and "Algorithmic Analysis"; MCS ch. 18.

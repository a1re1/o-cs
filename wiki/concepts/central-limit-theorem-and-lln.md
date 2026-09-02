---
title: Law of large numbers and the central limit theorem
type: concept
section: "1.4"
level: 200
tags: [law-of-large-numbers, central-limit-theorem, normal-approximation, sample-mean, standard-error, convergence, delta-method, heavy-tails, monte-carlo-error]
sources: [cs109-probability-for-computer-scientists, blitzstein-stat110, wasserman-all-of-statistics]
summary: Averages of i.i.d. variables converge to the mean (LLN) and their fluctuations are normal with standard deviation σ/√n (CLT) — the basis of standard errors, confidence intervals, Monte Carlo error bars, and the 1/√n cost of precision — with the conditions under which they fail.
---
# Law of large numbers and central limit theorem

**In one sentence.** For i.i.d. X₁…X_n with mean μ and variance σ², the sample mean X̄ → μ, and
√n (X̄ − μ)/σ → N(0,1); equivalently Σ Xᵢ ≈ N(nμ, nσ²) and X̄ ≈ N(μ, σ²/n).

## Statements
- **Weak LLN**: P(|X̄ − μ| > ε) → 0 (proof: Chebyshev with Var(X̄) = σ²/n — [[concentration-inequalities]]).
  Strong LLN: X̄ → μ almost surely. Needs only a finite mean.
- **CLT** (CS109's two forms): sum version Σ Xᵢ ~ N(nμ, nσ²); mean version X̄ ~ N(μ, σ²/n).
  Needs finite variance; "n ≥ 30" is folklore — skewed or heavy-tailed X need far more, symmetric
  bounded X far less. Lindeberg/Lyapunov versions relax "identically distributed".
- **Standard error** of the mean = σ/√n (estimate σ by the sample SD) — to halve the error, quadruple n.
- **Delta method**: g(X̄) ≈ N(g(μ), g′(μ)²σ²/n) — error bars for functions of averages (ratios, logs).
- Convergence modes: in probability (LLN) vs in distribution (CLT) vs almost surely; Slutsky lets you
  plug consistent estimates into CLT statements.

## Where it shows up
- Confidence intervals X̄ ± 1.96 σ̂/√n ([[hypothesis-testing-and-confidence-intervals]]).
- Monte Carlo integration/estimation: error O(1/√N) regardless of dimension ([[monte-carlo-methods]],
  [[integrals-and-sums]]).
- Binomial ≈ normal for polling, A/B tests, load estimates ([[common-distributions]]).
- Why measurement noise and "sum of many small effects" are Gaussian — and why Gaussian assumptions
  fail for latency tails, file sizes, and finance (heavy tails: Pareto, lognormal).
- Sampling and bootstrapping rely on the sample being representative; the CLT says nothing about bias.

## Pitfalls
- Infinite variance (Cauchy, Pareto α < 2): averages do not stabilize; the CLT does not apply.
- Dependence (time series, autocorrelated logs): effective sample size ≪ n; use block bootstrap or
  account for correlation.
- The CLT is about the *center*; tail probabilities need Chernoff/exact calculations.
- "Grades are not normal" (CS109): bounded, skewed, multimodal data — check before assuming.

## Related
- [[random-variables-expectation]], [[concentration-inequalities]], [[common-distributions]],
  [[hypothesis-testing-and-confidence-intervals]].

## Sources
CS109 reader "Central Limit Theorem", "Sampling"; Blitzstein ch. 10; Wasserman ch. 5.

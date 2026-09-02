---
title: Log probabilities and the log-sum-exp trick
type: concept
section: "1.4"
level: 200
tags: [log-probabilities, log-likelihood, underflow, logsumexp, numerical-stability, softmax, floating-point, naive-bayes]
sources: [cs109-probability-for-computer-scientists]
summary: Work with log P instead of P — products become sums, tiny probabilities stop underflowing to zero, and argmax is unchanged — plus the log-sum-exp trick for normalizing (softmax, marginalizing) without overflow.
---
# Log probabilities

**In one sentence.** log P ∈ (−∞, 0]; multiply probabilities by adding logs, compare by comparing
logs, and only exponentiate at the very end (if at all).

## Why
- A document of 1,000 words each with P ≈ 10⁻³ has probability 10⁻³⁰⁰⁰ — below the smallest double
  (≈ 10⁻³⁰⁸) ⇒ underflow to 0 ([[floating-point]]). Its log is −6908, a perfectly ordinary number.
- Sums are cheaper and more accurate than products; gradients of log-likelihoods are simpler
  ([[maximum-likelihood-estimation]]).
- Since log is monotone, argmax_y P(y | x) = argmax_y log P(y) + Σ log P(x_i | y) (naive Bayes,
  [[bayes-theorem-and-inference]]).

## Log-sum-exp
To compute log Σ_i e^{a_i} (normalizing a softmax, marginalizing in log space) with a_i ≈ −10⁴:
log Σ e^{a_i} = m + log Σ e^{a_i − m}, with m = max a_i. The largest term becomes e⁰ = 1, nothing
overflows, and underflowing terms were negligible anyway. Every ML library's `logsumexp`,
`log_softmax` and cross-entropy loss do this; compute log-softmax directly rather than log(softmax).

## Related tricks
- Log-space addition of two probabilities: log(p + q) = log p + log1p(e^{log q − log p}) for p ≥ q.
- Use `log1p`, `expm1` for values near 0/1; `math.fsum`/Kahan for long sums.
- Entropy and cross-entropy are expectations of log-probabilities ([[entropy-and-information]]).

## Related
- [[floating-point]], [[maximum-likelihood-estimation]], [[bayes-theorem-and-inference]].

## Sources
CS109 reader "Log Probabilities"; standard numerical-ML practice.

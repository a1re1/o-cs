---
title: Hypothesis testing, p-values, confidence intervals, bootstrap, and A/B tests
type: concept
section: "1.4"
level: 300
tags: [hypothesis-testing, p-values, confidence-intervals, bootstrap, permutation-test, a-b-testing, type-i-error, power, multiple-comparisons, p-hacking, effect-size, standard-error]
sources: [cs109-probability-for-computer-scientists, wasserman-all-of-statistics, think-stats-downey]
summary: How to decide whether an observed effect is real — null hypotheses and p-values, Type I/II errors and power, confidence intervals from the CLT, the bootstrap and permutation tests that need no formulas, A/B testing mechanics, and the ways these are abused (p-hacking, peeking, multiple comparisons).
---
# Hypothesis testing and confidence intervals

**In one sentence.** A p-value is the probability, *if the null hypothesis were true*, of seeing an
effect at least as extreme as the one observed — it is not the probability the null is true.

## The frequentist toolkit
- Null H₀ vs alternative H₁; test statistic T; p = P(T ≥ t_obs | H₀). Reject at level α (0.05 by
  convention). **Type I** error = false positive (rate α); **Type II** = miss; **power** = 1 − β,
  raised by larger n or larger true effect. Plan n from the desired power *before* running.
- **Confidence interval**: estimate ± z_{α/2}·SE (SE = σ̂/√n by the CLT — [[central-limit-theorem-and-lln]]).
  Interpretation: 95% of such intervals, over repeated experiments, contain the truth. Report the CI
  and the effect size, not just p.
- Common tests: z/t-test for means, two-proportion z-test (A/B conversion), χ² for counts, Wald and
  likelihood-ratio tests for MLE parameters ([[maximum-likelihood-estimation]]).

## Simulation-based methods (CS109, Think Stats)
- **Bootstrap** (Efron 1979): the sample is the best estimate of the population. Resample n points
  *with replacement* B ≈ 1000 times, recompute the statistic (mean, median, correlation, model
  coefficient…), read off its distribution → SE, percentile CI, p-values. Works for statistics with no
  formula; fails for extremes (max), tiny n, or dependent data (use block bootstrap).
- **Permutation test**: under H₀ "no difference", labels are exchangeable; shuffle labels many times,
  recompute the difference, p = fraction ≥ observed. Exact and assumption-free for two-sample comparisons.

## A/B testing mechanics
Randomize assignment; fix the metric and n in advance; compute the two-proportion test or a bootstrap
CI on the difference; **don't peek** and stop when significant (inflates α — use sequential tests or
Bayesian bandits/Thompson sampling instead); beware novelty effects and interference between units.

## Multiple comparisons and p-hacking
Testing m hypotheses at α gives ~mα false positives; Bonferroni (α/m) or Benjamini–Hochberg (FDR).
P-hacking = trying analyses until p < 0.05 (CS109 has a simulation showing "significant" results from
pure noise); pre-register, hold out, replicate.

## Bayesian alternative
Credible intervals and posterior probabilities of hypotheses answer the question people actually ask
("how likely is the effect real?") at the price of a prior ([[bayes-theorem-and-inference]]).

## Pitfalls
- "Not significant" ≠ "no effect" (low power).
- Statistically significant ≠ practically significant; with large n everything is significant.
- Confidence intervals of two groups overlapping does not imply no significant difference.

## Related
- [[central-limit-theorem-and-lln]], [[maximum-likelihood-estimation]], [[bayes-theorem-and-inference]].

## Sources
CS109 "Sampling", "Bootstrapping", "P-Hacking"; Wasserman ch. 8, 10; Think Stats ch. 7–9.

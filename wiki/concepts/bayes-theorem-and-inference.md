---
title: Bayes' theorem, base rates, and Bayesian inference
type: concept
section: "1.4"
level: 200
tags: [bayes-theorem, conditional-probability, base-rate-fallacy, prior, posterior, likelihood, naive-bayes, map, bayesian-inference, conjugate-priors, credible-intervals]
sources: [cs109-probability-for-computer-scientists, blitzstein-stat110, wasserman-all-of-statistics, think-stats-downey]
summary: Posterior ∝ likelihood × prior; why base rates dominate rare-event tests; naive Bayes as Bayes plus a conditional-independence assumption; MAP estimation as regularized MLE; conjugate priors that make updating arithmetic; and the frequentist/Bayesian split on what a probability means.
---
# Bayes' theorem and Bayesian inference

**In one sentence.** P(H | E) = P(E | H) P(H) / P(E): update a prior belief P(H) by how much better
H explains the evidence than the alternatives do.

## The theorem and its traps
- P(E) = Σ_i P(E | H_i) P(H_i) (law of total probability) is the normalizer; often you only need the
  ratio, so compute unnormalized posteriors and divide by their sum (grid approximation, Think Bayes).
- **Base-rate fallacy**: test with 99% sensitivity and 99% specificity for a 1-in-10,000 condition:
  P(sick | positive) ≈ 0.0099·1/(0.0099 + 0.01·0.9999) ≈ 1%. Draw the tree ([[four-step-method]]).
- Prosecutor's fallacy: P(evidence | innocent) ≠ P(innocent | evidence).
- Odds form: posterior odds = prior odds × likelihood ratio (Bayes factor) — the cleanest way to chain
  evidence; in log space evidence just adds ([[log-probabilities]]).

## Naive Bayes
Classify y from features x₁…x_d assuming P(x | y) = Π P(x_i | y). Train by counting (with Laplace
smoothing = Beta/Dirichlet prior), predict argmax_y log P(y) + Σ log P(x_i | y). Absurd independence
assumption, yet strong for text (Federalist papers authorship, spam); calibrates poorly (§6.2).

## Estimation with priors
- **MAP**: θ̂ = argmax P(θ | data) = argmax [log P(data | θ) + log P(θ)]. A Gaussian prior on weights
  is L2 regularization; Laplace prior is L1 — so "ridge = MAP with Gaussian prior"
  ([[maximum-likelihood-estimation]], [[least-squares]]).
- **Conjugate priors**: Beta for Bernoulli/binomial, Dirichlet for categorical, Gamma for Poisson,
  Normal for Normal mean — posterior stays in the family, so updating is counting
  ([[common-distributions]]). Thompson sampling = sample θ from each arm's posterior, pull the best.
- Full posterior vs point estimate: credible intervals (posterior probability) vs confidence intervals
  (frequency over repeated samples) answer different questions
  ([[hypothesis-testing-and-confidence-intervals]]).
- When the posterior is intractable: MCMC ([[markov-chains]]) or variational inference (§6.7).

## Bayesian networks (CS109 Part 3)
A DAG of variables with P(x₁..x_n) = Π P(x_i | parents). Inference by enumeration is exponential;
rejection sampling / likelihood weighting / Gibbs sampling approximate it; exact algorithms in §6.7.

## Pitfalls
- Flat priors are not "no assumptions" (they depend on parameterization).
- Naive Bayes probabilities are overconfident — don't read them as calibrated.
- Conditioning on the evidence you selected because it was surprising (selection effects, p-hacking).

## Related
- [[four-step-method]], [[maximum-likelihood-estimation]], [[log-probabilities]], [[common-distributions]].

## Sources
CS109 reader Part 1 (Bayes, log probabilities), Part 3, Part 5 (MAP, naive Bayes); Blitzstein ch. 2; Wasserman ch. 11; Think Bayes ch. 1–4.

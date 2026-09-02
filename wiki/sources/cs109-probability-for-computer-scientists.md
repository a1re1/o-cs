---
title: Stanford CS109 Probability for Computer Scientists (Piech course reader)
type: source
section: "1.4"
level: 200
tags: [probability, random-variables, bayes, mle, bootstrapping, central-limit-theorem, log-probabilities, algorithmic-analysis, naive-bayes, logistic-regression]
sources: []
authors: [Chris Piech, Mehran Sahami, Lisa Yan, Jerry Cain, Chris Gregg]
year: 2023
institution: Stanford
url: https://chrispiech.github.io/probabilityForComputerScientists/en/
license: unknown
format: html
summary: Stanford's probability course for CS majors and its free online reader in five parts — core probability, random variables, probabilistic models, uncertainty theory (CLT, sampling, bootstrapping, algorithmic analysis, information theory), and machine learning (MLE, MAP, naive Bayes, logistic regression) — with applications like Enigma, Federalist papers, Thompson sampling, p-hacking and differential privacy.
---
# Stanford CS109 Probability for Computer Scientists

## What it is
Level 200; prerequisite CS106B and basic calculus. The reader (Chris Piech, v0.92, 2023) is the
curriculum: **Part 1 Core probability** (counting, axioms, equally likely outcomes, conditional
probability, independence, law of total probability, Bayes, log probabilities, many coin flips);
**Part 2 Random variables** (PMFs, expectation, variance, Bernoulli/binomial/Poisson/geometric/
negative binomial/categorical, continuous: uniform/exponential/normal, binomial approximation);
**Part 3 Probabilistic models** (joint, marginalization, multinomial, inference, Bayesian networks,
correlation, general inference by sampling); **Part 4 Uncertainty theory** (beta distribution, adding
random variables, CLT, sampling, bootstrapping, algorithmic analysis, information theory, distances
between distributions); **Part 5 Machine learning** (parameter estimation, MLE, MAP, naive Bayes,
logistic regression, diffusion). The 2026 lecture list adds sampling & bootstrapping, deep learning,
diffusion and RL as capstones.

## Key ideas → pages
- Bayes' theorem with explicit base rates; **log probabilities** to avoid underflow and turn products
  into sums — [[bayes-theorem-and-inference]], [[log-probabilities]].
- Expectation of a sum = sum of expectations *regardless of independence*; law of total expectation as
  a tool to analyze code (distributed file system example: E[T] = Σ E[T | L=l]P(L=l)) —
  [[random-variables-expectation]], [[probabilistic-analysis-of-algorithms]].
- CLT in two forms (sum ~ N(nμ, nσ²), mean ~ N(μ, σ²/n)) — [[central-limit-theorem-and-lln]].
- **Bootstrapping** (Efron 1979): estimate F by the empirical distribution, resample with replacement,
  recompute the statistic many times to get its sampling distribution and p-values —
  [[hypothesis-testing-and-confidence-intervals]].
- MLE picks θ maximizing the likelihood of i.i.d. data; MAP adds a prior (= regularization) —
  [[maximum-likelihood-estimation]].
- Applications worth remembering: Enigma (Bayesian codebreaking), Federalist papers (naive Bayes
  authorship), Thompson sampling (beta posteriors for bandits), p-hacking, differential privacy
  (randomized response), curse of dimensionality.

## What it adds
The most *computational* of the probability sources: every concept comes with Python and with a
"use this to analyze a program" example. Pair with [[blitzstein-stat110]] for depth and proofs.

---
title: All of Statistics (Wasserman)
type: source
section: "1.4"
level: 300
tags: [statistics, estimation, confidence-intervals, hypothesis-testing, bootstrap, bayesian-inference, nonparametric, regression, statistical-learning]
sources: []
authors: [Larry Wasserman]
year: 2004
institution: Carnegie Mellon
url: https://www.stat.cmu.edu/~larry/all-of-statistics/
license: unknown
format: pdf
summary: The "concise course in statistical inference" for CS/ML people — probability review, then convergence, models and inference (empirical CDF, bootstrap, parametric inference/MLE, hypothesis testing, Bayesian inference, decision theory), regression, classification, nonparametric methods; chapters are short and the theorems are the ones ML papers cite.
---
# All of Statistics (Wasserman, 2004)

## What it is
Level 300 (assumes calculus and linear algebra). Part I Probability (random variables, expectation,
inequalities, convergence: in probability/distribution, LLN, CLT, delta method). Part II Statistical
inference: models and estimation (bias, consistency, MSE, sampling distributions), the empirical
distribution and plug-in estimators, **the bootstrap**, parametric inference (MLE properties:
consistency, asymptotic normality, Fisher information, Cramér–Rao), hypothesis testing and p-values
(Wald, likelihood ratio, multiple testing), Bayesian inference, statistical decision theory.
Part III Statistical models and methods: linear/logistic regression, multivariate models, graphs,
log-linear models, nonparametric curve estimation, smoothing, classification, simulation (MCMC).

## Key ideas → pages
- Estimator quality: bias, variance, MSE = bias² + variance; consistency; sampling distribution and
  standard error — [[maximum-likelihood-estimation]], [[hypothesis-testing-and-confidence-intervals]].
- MLE is asymptotically normal with variance 1/(nI(θ)) (Fisher information); Cramér–Rao lower bound;
  the delta method for functions of estimators — [[maximum-likelihood-estimation]].
- p-values, Type I/II errors, power, Bonferroni/FDR for multiple comparisons —
  [[hypothesis-testing-and-confidence-intervals]].
- Bayesian vs frequentist: priors, posteriors, credible vs confidence intervals; MAP —
  [[bayes-theorem-and-inference]].
- Convergence modes and the CLT/delta method — [[central-limit-theorem-and-lln]].

## What it adds
The theorems (Fisher information, Cramér–Rao, asymptotic normality of the MLE, delta method) that
[[cs109-probability-for-computer-scientists]] states informally.

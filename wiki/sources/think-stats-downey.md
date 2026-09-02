---
title: Think Stats and Think Bayes (Downey)
type: source
section: "1.4"
level: 200
tags: [statistics, exploratory-analysis, cdf, hypothesis-testing, bayesian-inference, python, simulation]
sources: []
authors: [Allen B. Downey]
year: 2014
institution: Olin College / Green Tea Press
url: https://greenteapress.com/wp/think-stats-2e/
license: CC-BY-NC
format: html
summary: Two free, code-first books — Think Stats (exploratory data analysis, distributions as CDFs, modeling, estimation, hypothesis testing by simulation/permutation, regression, time series) and Think Bayes (Bayesian inference computed with discrete PMFs) — for programmers who learn statistics by writing Python.
---
# Think Stats / Think Bayes (Downey)

## What it is
Think Stats (2e): exploratory analysis of the NSFG survey ("do first babies arrive late?"),
distributions (histograms, PMFs, CDFs, percentiles), modeling distributions (exponential, normal,
lognormal, Pareto), relationships (scatter, correlation), estimation (bias, MSE, bootstrapping),
**hypothesis testing by simulation** (permutation tests, power), regression, time series, survival
analysis. Think Bayes: Bayes's theorem with discrete PMF objects, estimation, decision analysis, MCMC.

## Key ideas → pages
- Prefer **CDFs** to histograms/PMFs for comparing distributions (class-size paradox: the mean class
  size seen by students exceeds the mean over classes — length-biased sampling) — [[common-distributions]].
- Hypothesis testing as "simulate the null model and see how often the observed effect appears";
  permutation tests need no formulas; report effect size, not only p — [[hypothesis-testing-and-confidence-intervals]].
- Bayesian updates as arithmetic on a PMF (grid approximation) — [[bayes-theorem-and-inference]].

## What it adds
The simulation-first attitude: when unsure of a distribution, resample or simulate. Complements the
analytic treatment in [[blitzstein-stat110]] and [[wasserman-all-of-statistics]].

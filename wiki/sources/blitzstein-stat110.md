---
title: Harvard Stat 110 and Introduction to Probability (Blitzstein & Hwang)
type: source
section: "1.4"
level: 200
tags: [probability, conditional-probability, random-variables, expectation, distributions, markov-chains, mcmc, poisson-process, inequalities, limit-theorems]
sources: []
authors: [Joe Blitzstein, Jessica Hwang]
year: 2019
institution: Harvard
url: https://projects.iq.harvard.edu/stat110
license: proprietary-open-access
format: pdf
summary: Blitzstein's Harvard course (34 open lectures) and free-PDF textbook (2nd ed.) — the canonical rigorous-but-intuitive probability text: conditioning as "the soul of statistics", story proofs, named distributions and their relationships, LOTUS, conditional expectation, inequalities and limit theorems, Markov chains, MCMC, Poisson processes.
---
# Harvard Stat 110 / Introduction to Probability (Blitzstein & Hwang)

## What it is
Level 200–300. Chapters: 1 Probability and counting; 2 Conditional probability; 3 Random variables and
distributions; 4 Expectation; 5 Continuous random variables; 6 Moments; 7 Joint distributions;
8 Transformations; 9 Conditional expectation; 10 Inequalities and limit theorems; 11 Markov chains;
12 Markov chain Monte Carlo; 13 Poisson processes. Free PDF from the authors; lectures, strategic
practice problems and solutions on the course site.

## Key ideas → pages
- "Conditioning is the soul of statistics": Bayes' rule, law of total probability, first-step analysis
  (condition on the first step to solve recursions) — [[bayes-theorem-and-inference]].
- **Story proofs** and the **fundamental bridge** E[I_A] = P(A): prove identities and compute
  expectations by writing a random variable as a sum of indicators — [[random-variables-expectation]],
  [[probabilistic-analysis-of-algorithms]].
- The distribution family tree: Bernoulli → Binomial → Poisson (rare events limit); Geometric/Negative
  binomial; Uniform → universality of the uniform (inverse-CDF sampling); Exponential (memoryless) →
  Gamma; Normal; Beta as the conjugate prior for Bernoulli/Binomial ("Beta-Binomial conjugacy") —
  [[common-distributions]].
- LOTUS (E[g(X)] = Σ g(x)P(X=x)), variance = E[X²] − (E[X])², covariance and correlation, Adam's law
  E[E[Y|X]] = E[Y] and Eve's law Var(Y) = E[Var(Y|X)] + Var(E[Y|X]) — [[random-variables-expectation]].
- Markov, Chebyshev, Chernoff, Jensen, Cauchy–Schwarz; LLN and CLT — [[concentration-inequalities]],
  [[central-limit-theorem-and-lln]].
- Markov chains: transition matrices, stationary distributions, reversibility, and MCMC
  (Metropolis–Hastings, Gibbs) as *designing* a chain whose stationary distribution is the target —
  [[markov-chains]].

## Notable claims & quotes
- "Conditioning is the soul of statistics."
- On the Monty Hall and prosecutor's fallacy family of problems: write down what is conditioned on.

## What it adds
Depth and proofs behind [[cs109-probability-for-computer-scientists]]; the Markov chain / MCMC chapters
are the bridge to §6.7 and to PageRank ([[pagerank]]).

---
title: Common probability distributions and when they arise
type: concept
section: "1.4"
level: 200
tags: [distributions, bernoulli, binomial, geometric, poisson, negative-binomial, uniform, exponential, normal, gaussian, beta, gamma, memoryless, conjugate-prior, inverse-cdf-sampling]
sources: [blitzstein-stat110, cs109-probability-for-computer-scientists, think-stats-downey]
summary: The named distributions as stories — Bernoulli/binomial (fixed trials), geometric/negative binomial (waiting for successes), Poisson (rare events, binomial limit), uniform, exponential (memoryless waiting), normal (sums), beta (a probability's distribution), gamma — with means, variances, relationships, and how to sample from them.
---
# Common distributions

**In one sentence.** Recognize the *story* (how the randomness is generated) and the distribution
follows; each row below is a story plus the two numbers you need.

| Distribution | Story | Mean | Variance |
|---|---|---|---|
| Bernoulli(p) | one trial, success w.p. p | p | p(1−p) |
| Binomial(n,p) | # successes in n independent trials | np | np(1−p) |
| Geometric(p) | # trials until first success (support 1,2,…) | 1/p | (1−p)/p² |
| Negative binomial(r,p) | # trials until r-th success | r/p | r(1−p)/p² |
| Poisson(λ) | # events in an interval with rate λ; limit of Bin(n, λ/n) | λ | λ |
| Uniform(a,b) | equally likely on an interval | (a+b)/2 | (b−a)²/12 |
| Exponential(λ) | waiting time between Poisson events; memoryless | 1/λ | 1/λ² |
| Gamma(k,λ) | sum of k exponentials | k/λ | k/λ² |
| Normal(μ,σ²) | sum/average of many small independent effects (CLT) | μ | σ² |
| Beta(a,b) | distribution of a probability after a−1 successes, b−1 failures | a/(a+b) | ab/((a+b)²(a+b+1)) |
| Categorical/Multinomial | k-sided die | np_i | np_i(1−p_i) |

## Relationships that save work
- Bin(n,p) ≈ Poisson(np) when n large, p small (rare events; bugs per line, requests per ms).
- Bin(n,p) ≈ N(np, np(1−p)) when np(1−p) ≳ 10 (continuity correction ±0.5).
- Sum of independent Poissons is Poisson; sum of independent normals is normal; sum of n i.i.d.
  Geometric is Negative binomial; sum of k Exponential(λ) is Gamma(k, λ).
- **Memorylessness**: P(X > s+t | X > s) = P(X > t) characterizes geometric (discrete) and exponential
  (continuous) — the mathematical basis of "the past doesn't matter" in Markov models and of why
  retry-after-timeout policies need care.
- **Beta–Binomial conjugacy**: prior Beta(a,b), observe k successes in n ⇒ posterior Beta(a+k, b+n−k).
  Laplace smoothing (add-one) is Beta(1,1); Thompson sampling draws from these posteriors.
- Poisson process: counts in disjoint intervals independent Poisson; inter-arrivals Exponential; given
  N events in [0,T], their times are i.i.d. Uniform.

## Sampling (universality of the uniform)
If U ~ Uniform(0,1) then F⁻¹(U) ~ F. Exponential: −ln(U)/λ. Normal: Box–Muller or `numpy.random.normal`.
Discrete: cumulative table + binary search, or the alias method for O(1) draws. Rejection sampling when
F⁻¹ is unavailable; MCMC when even the normalizer is unknown ([[markov-chains]]).

## Heavy tails (Think Stats)
Lognormal, Pareto/power laws (file sizes, city sizes, word frequencies, degree distributions) have means
dominated by rare huge values; sample means converge slowly or not at all; use medians/quantiles and
log-log plots ([[central-limit-theorem-and-lln]]).

## Pitfalls
- Geometric support convention (trials vs failures) shifts the mean by 1.
- Exponential's parameter is a rate; NumPy's `exponential(scale)` takes 1/λ.
- Normal approximations fail in the tails — use Chernoff bounds or exact binomials for p < 10⁻³ events
  ([[concentration-inequalities]]).

## Related
- [[random-variables-expectation]], [[bayes-theorem-and-inference]] (Beta priors), [[markov-chains]].

## Sources
Blitzstein ch. 3, 5, 8, 13; CS109 Part 2; Think Stats ch. 5.

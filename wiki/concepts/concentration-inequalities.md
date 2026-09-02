---
title: Concentration inequalities (Markov, Chebyshev, Chernoff, union bound)
type: concept
section: "1.4"
level: 300
tags: [concentration-inequalities, markov-inequality, chebyshev, chernoff-bound, tail-bounds, union-bound, variance, randomized-algorithms, load-balancing]
sources: [mcs-lehman-leighton-meyer]
summary: The three tail bounds every randomized-algorithm analysis uses — Markov (mean only), Chebyshev (variance), Chernoff (sum of independent 0/1 variables, exponentially small tails) — plus the union bound, with the rule of thumb for which one is tight enough.
---
# Concentration inequalities

**In one sentence.** Knowing only the mean bounds the tail loosely (Markov); adding variance makes it
quadratic (Chebyshev); independence makes it exponential (Chernoff).

## The bounds
| Bound | Hypothesis | Statement |
|---|---|---|
| **Markov** | R ≥ 0 | Pr[R ≥ x] ≤ E[R]/x, i.e. Pr[R ≥ c·E[R]] ≤ 1/c |
| **Chebyshev** | finite variance | Pr[\|R − E[R]\| ≥ x] ≤ Var[R]/x² |
| **Chernoff** | T = Σ of independent variables in [0,1], E[T] = μ | Pr[T ≥ (1+δ)μ] ≤ e^{−δ²μ/3} for 0<δ≤1; Pr[T ≤ (1−δ)μ] ≤ e^{−δ²μ/2}; for any c > 1, Pr[T ≥ cμ] ≤ e^{−(c ln c − c + 1)μ} |
| **Union bound** | any events | Pr[∪A_i] ≤ Σ Pr[A_i] |

Markov's proof is one line: E[R] ≥ x·Pr[R ≥ x] because R ≥ 0. Chebyshev is Markov applied to
(R − μ)². Chernoff is Markov applied to e^{tT} with t optimized (the "moment generating function"
trick); independence is what lets E[e^{tT}] factor.

## Intuition from MCS
Average IQ is 100 ⇒ at most 1/3 of people have IQ ≥ 300 (Markov). For the Chinese-appetizer problem
(n people, rotating tray, R = # who get their own dish) E[R] = 1 and Markov's bound Pr[R ≥ n] ≤ 1/n is
*exactly right*; for the hat-check problem (random permutation) the same bound is hopelessly loose
(truth is 1/n!). Markov is tight only when the distribution is two-point.

## How to choose
- Only the mean is known, or R is heavy-tailed: Markov (weak, but honest).
- Variance known (e.g. a sum of pairwise independent variables — Var adds): Chebyshev. Also gives the
  weak law of large numbers: sample mean of n i.i.d. copies has Var/n.
- Sum of many independent bounded variables (balls in bins, hashing, sampling, randomized rounding):
  Chernoff — tails fall exponentially in μ. E.g. n balls into n bins: max load is O(log n / log log n)
  w.h.p.; for μ = Θ(log n), deviation by a constant factor has probability n^{−Ω(1)}, so a union bound
  over n bins still works.
- Many "bad events" each rare: union bound, then make each rare enough (Chernoff) to absorb the sum.

## Pitfalls
- Chernoff needs *independence* (or negative association / martingale versions such as
  Azuma–Hoeffding); do not apply it to correlated indicators.
- Markov needs non-negativity; Chebyshev needs the variance to exist (fails for Cauchy).
- "With high probability" should name the probability (1 − 1/n^c) and the c.

## Related
- [[four-step-method]] — computing exact probabilities when possible.
- [[random-variables-expectation]] — linearity of expectation and variance (§1.4).
- [[hash-tables]], [[randomized-algorithms]] — main consumers.

## Sources
MCS ch. 19 (Deviation from the Mean: Markov, Chebyshev, Chernoff, sampling); ch. 20 (random walks) for hitting times.

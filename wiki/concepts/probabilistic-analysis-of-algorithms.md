---
title: Probabilistic analysis of algorithms (expected running time, hashing, quicksort, coupon collector)
type: concept
section: "1.4"
level: 300
tags: [probabilistic-analysis, expected-running-time, indicator-variables, linearity-of-expectation, hashing, birthday-problem, quicksort, coupon-collector, balls-in-bins, randomized-algorithms, average-case, with-high-probability]
sources: [cs109-probability-for-computer-scientists, mcs-lehman-leighton-meyer, blitzstein-stat110]
summary: The standard moves for analyzing randomized or average-case algorithms — indicator variables plus linearity of expectation, the law of total expectation on the first step, harmonic sums, balls-in-bins/birthday calculations, coupon collector, and Chernoff bounds for "with high probability" — illustrated on hashing, quicksort, and load balancing.
---
# Probabilistic analysis of algorithms

**In one sentence.** Define X = Σ (indicator of each elementary event), compute E[X] by linearity
without caring about dependence, then, if you need a guarantee rather than an average, add a tail bound.

## The moves
1. **Indicators + linearity** ([[random-variables-expectation]]).
2. **Condition on the first step** (law of total expectation) to get a recurrence ([[recurrences]]).
3. **Symmetry**: random permutations make "i-th element is a record / pivot separates i and j" easy.
4. **Harmonic sums** appear whenever "probability 1/k at step k" — H_n = ln n + O(1) ([[integrals-and-sums]]).
5. **Tail bound** for w.h.p. claims: Markov if only the mean is known, Chebyshev with variance, Chernoff
   + union bound for sums of independent indicators ([[concentration-inequalities]]).
6. **Bad event analysis**: bound P(any bad event) ≤ Σ P(bad_i) (union bound), then push each below 1/n^c.

## Worked results
- **Hashing** n keys into m slots uniformly: expected chain length n/m (load factor α); expected probes
  for a successful search ≈ 1 + α/2. Birthday: collisions become likely at n ≈ √(2m ln 2) ≈ 1.18√m
  ([[hash-tables]], [[four-step-method]]).
- **Balls in bins** (n into n): expected max load Θ(log n / log log n); with "power of two choices"
  (put the ball in the emptier of two random bins) it drops to Θ(log log n) — a real load-balancing trick.
- **Quicksort** with a random pivot: elements i and j (rank distance d) are compared iff one of them is
  the first pivot chosen among the d+1 elements between them, probability 2/(d+1); summing gives
  E[comparisons] = 2n ln n + O(n) ≈ 1.39 n log₂ n ([[sorting]]).
- **Coupon collector**: to see all n types, E[draws] = n H_n ≈ n ln n; used for "how many random probes
  until every bucket is hit", random testing coverage, and epidemics on graphs.
- **Randomized selection / treaps / skip lists**: expected O(n) / O(log n) via the same indicator sums.
- **Geometric waiting**: expected tries until success with probability p is 1/p — retries, Bloom filter
  false-positive budgets, Miller–Rabin rounds ([[common-distributions]]).

## Average case vs randomized
Average-case analysis assumes a distribution over inputs (fragile); a randomized algorithm puts the
randomness inside and its expected bound holds for *every* input — which is why random pivots and
random hash functions are preferred to "assume the input is random" ([[randomized-algorithms]]).

## Pitfalls
- Expected O(n log n) does not preclude a bad run; state w.h.p. bounds when tail behaviour matters.
- Adversarial inputs can break "average-case" but not "randomized" bounds — unless the adversary sees
  the random bits (hash-flooding attacks on predictable hash functions; use seeded/SipHash).
- Dependence between indicators is irrelevant for E but crucial for Var and Chernoff.

## Related
- [[random-variables-expectation]], [[concentration-inequalities]], [[hash-tables]], [[sorting]],
  [[randomized-algorithms]].

## Sources
CS109 "Algorithmic Analysis", "Random Shuffles", "Approximate Counting"; MCS ch. 18–19; Blitzstein ch. 4 (indicator method).

---
title: Randomized algorithms — Las Vegas vs Monte Carlo, random pivots, hashing, min cut, and analysis tools
type: concept
section: "3.2"
level: 300
tags: [randomized-algorithms, las-vegas, monte-carlo, quicksort-analysis, quickselect, randomized-selection, karger-min-cut, universal-hashing, bloom-filters, skip-lists, treaps, primality-testing, miller-rabin, fingerprinting, rabin-karp, chernoff-bounds, linearity-of-expectation, derandomization]
sources: [clrs, kleinberg-tardos-skiena, roughgarden-algorithms-illuminated, erickson-algorithms]
summary: Randomization turns worst-case inputs into average-case ones (random pivots make quicksort O(n log n) expected on every input), gives simple structures with expected guarantees (skip lists, treaps, universal hashing, Bloom filters), and enables algorithms with a small error probability that repetition drives to zero (Miller–Rabin primality, Karger's min cut, Rabin–Karp fingerprints, polynomial identity testing); Las Vegas algorithms are always correct with random running time, Monte Carlo are fast with bounded error, and the analysis uses indicator variables, linearity of expectation, and Chernoff/union bounds.
---
# Randomized algorithms

**In one sentence.** Flip coins inside the algorithm so that no input is bad for it — the
adversary chose the input before you chose your randomness.

## Two flavours
- **Las Vegas**: always correct, running time is a random variable (randomized quicksort,
  QuickSelect, hashing with chaining, skip lists). Report expected time; Markov's inequality
  bounds tail probabilities; restart if unlucky.
- **Monte Carlo**: bounded time, may err with probability ≤ ε; repeat k times to get ε^k
  (one-sided error) — Miller–Rabin, Karger, Freivalds' matrix product check, Rabin–Karp.
  Convert Monte Carlo → Las Vegas when answers are verifiable.

## Canonical analyses (CLRS ch. 5, K&T ch. 13, Roughgarden part 1)
- **Quicksort**: elements i and j are compared iff the first pivot chosen from [i..j] is one of
  them: probability 2/(j − i + 1); summing gives expected 2n ln n compares — indicator variables
  + **linearity of expectation** ([[random-variables-expectation]]), no independence needed.
- **QuickSelect**: expected O(n) since a "good" pivot (middle half) shrinks the array to ¾ with
  probability ½ → geometric number of phases.
- **Hashing**: universal family ⇒ expected chain length α; birthday bound √M for collisions;
  balls-in-bins max load Θ(log n / log log n), power of two choices Θ(log log n) — [[hash-tables]].
- **Karger's min cut**: contract random edges until two vertices remain; a specific min cut
  survives with probability ≥ 2/n²; repeat n² ln n times for high probability (Karger–Stein
  O(n² log³ n)) — [[network-flow]] gives the deterministic route.
- **Miller–Rabin**: a composite passes a random witness test with probability ≤ ¼; 40 rounds
  suffice for cryptography ([[number-theory-basics]]); AKS is deterministic but slow.
- **Fingerprinting**: compare hashes mod a random prime (Rabin–Karp substring search — [[string-algorithms]];
  Freivalds' check of AB = C in O(n²); Schwartz–Zippel polynomial identity testing).
- **Concentration**: Chernoff bounds make "expected" into "with high probability" — load
  balancing, packet routing, sampling estimates ([[concentration-inequalities]]).
- **Randomized data structures**: skip lists, treaps ([[balanced-search-trees]]), Bloom filters
  (false-positive rate (1 − e^{−kn/m})^k), count–min sketch, HyperLogLog ([[streaming-and-sketching]]).

## Why it works / when to use
Symmetry-breaking (distributed consensus, contention resolution), avoiding adversarial worst
cases (pivots, hash seeds), sampling instead of enumerating (estimation, approximate counting),
amplification. Derandomization (method of conditional expectations, pairwise independence)
sometimes recovers deterministic versions. Pseudorandom generators suffice in practice; use
cryptographic randomness only when an adversary can predict seeds ([[cryptography-basics]]).

## Pitfalls
- Analyzing average-case over inputs and calling it randomized (that's [[probabilistic-analysis-of-algorithms]]).
- Independence assumptions where only pairwise independence holds (or none).
- Fixed seeds in production hash tables (hash-flooding DoS).
- Forgetting to bound the error after composition (union bound over many Monte Carlo calls).

## Related
- [[probabilistic-analysis-of-algorithms]], [[random-variables-expectation]], [[concentration-inequalities]],
  [[hash-tables]], [[sorting]], [[balanced-search-trees]], [[number-theory-basics]], [[string-algorithms]].

## Sources
CLRS ch. 5, 7, 11, 31; K&T ch. 13; Roughgarden part 1–2; Erickson ch. 1.

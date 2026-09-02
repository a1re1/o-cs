---
title: Streaming algorithms and sketches — Bloom filters, count-min, heavy hitters, reservoir sampling, HyperLogLog
type: concept
section: "3.3"
level: 400
tags: [streaming, sketching, bloom-filter, count-min-sketch, heavy-hitters, misra-gries, reservoir-sampling, hyperloglog, distinct-counting, frequency-estimation, approximate-membership, one-pass, sublinear-space, lossy-compression]
sources: [cs168-modern-algorithmic-toolbox, karp-cook-and-classic-papers, roughgarden-algorithms-illuminated]
summary: When data arrives faster than it can be stored, keep a small randomized summary that answers a specific question approximately — a Bloom filter (k hashes into m bits; no false negatives, false-positive rate ≈ (1 − e^{−kn/m})^k) for membership, count-min sketch (d rows × w counters, take the minimum; over-estimates by ≤ εN with probability 1 − δ using w = e/ε, d = ln 1/δ) and Misra–Gries for heavy hitters, reservoir sampling for a uniform sample of a stream, HyperLogLog for distinct counts in ~1.5 KB with 2% error — all "property-preserving lossy compression" built from hashing and concentration bounds.
---
# Streaming and sketching

**In one sentence.** Decide the question first, then compress the data in a way that preserves
exactly the answer to that question (CS168's "property-preserving lossy compression").

## Membership: Bloom filter (Bloom 1970)
m-bit array, k independent hash functions; insert sets k bits; query says "maybe" if all k bits
are set. No false negatives; false-positive rate ≈ (1 − e^{−kn/m})^k, minimized at k = (m/n) ln 2
giving ≈ 0.6185^{m/n} (10 bits/element, k = 7 → ~1%). No deletions (counting Bloom filters,
cuckoo filters fix this); union = OR. Uses: avoid disk lookups for absent keys (LSM trees —
[[storage-engines-and-indexes]]), Chrome's malicious-URL list, cache admission, distributed
joins.

## Frequencies and heavy hitters
- **Majority / Misra–Gries** (deterministic): keep k − 1 counters; decrement all when full; any
  element with frequency > N/k survives; a second pass verifies. Space O(k).
- **Count-min sketch** (Cormode–Muthukrishnan): d hash rows × w counters; increment d cells per
  item; estimate = min over rows. Never under-estimates; over-estimate ≤ εN with probability
  ≥ 1 − δ for w = ⌈e/ε⌉, d = ⌈ln(1/δ)⌉ (Markov + independence across rows). Supports point
  queries, heavy hitters (with a heap), range queries (dyadic), inner products; mergeable.
- Count sketch (±1 signs, median): unbiased, error in ℓ₂ norm; better for skewed data.

## Sampling
- **Reservoir sampling**: keep the first k; replace a random slot with item i with probability
  k/i — a uniform k-sample of an unknown-length stream in one pass. Weighted (Efraimidis–Spirakis)
  and distributed variants.
- Importance sampling and Good–Turing (mass of unseen items) for estimation from samples;
  Markov/Chebyshev/Chernoff give the sample sizes ([[concentration-inequalities]]).

## Distinct elements: HyperLogLog (Flajolet et al.)
Hash each item; the maximum number of leading zeros ρ across items estimates log₂ of the
cardinality; average across m registers with the harmonic mean; error ≈ 1.04/√m (m = 2¹⁴ →
0.8% in 12 KB). Mergeable (max per register) — Redis `PFCOUNT`, analytics "unique users". Earlier:
Flajolet–Martin, LogLog; MinHash-based estimators.

## Other sketches
AMS/F₂ (second moment via ±1 hashes), ℓ₀ sampling, quantile sketches (GK, KLL, t-digest),
sliding-window counts (exponential histograms), graph sketches (connectivity via ℓ₀ samples),
matrix sketching (frequent directions). Linear sketches are mergeable and thus map-reduce/
distributed friendly ([[mapreduce-and-dataflow]]).

## Pitfalls
- Bloom filter sized for the wrong n (FP rate explodes as it fills); needing deletes.
- Count-min on heavy-tailed data: small items inflated by big ones (use count sketch or
  conservative update).
- Correlated hash functions violating the analysis; use independent seeds/tabulation
  ([[hash-tables]]).
- Forgetting that "approximate" means guarantees are probabilistic — set ε, δ deliberately.

## Related
- [[hash-tables]], [[randomized-algorithms]], [[concentration-inequalities]], [[similarity-search-and-lsh]],
  [[storage-engines-and-indexes]], [[mapreduce-and-dataflow]], [[log-probabilities]].

## Sources
CS168 week 1, 7; Bloom 1970; Cormode & Muthukrishnan 2005; Flajolet et al. 2007; Roughgarden part 2 (Bloom filters).

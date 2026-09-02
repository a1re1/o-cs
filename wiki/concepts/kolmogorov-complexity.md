---
title: Kolmogorov complexity and minimum description length
type: concept
section: "1.7"
level: 400
tags: [kolmogorov-complexity, algorithmic-information, incompressibility, minimum-description-length, occams-razor, randomness, uncomputable, chaitin]
sources: [mackay-itila]
summary: K(x) = length of the shortest program printing x — the algorithmic counterpart of entropy: most strings are incompressible, K is uncomputable but bounded above by any compressor, and the minimum description length principle turns Occam's razor into a model-selection rule (data cost + model cost).
---
# Kolmogorov complexity and MDL

**In one sentence.** A string is random iff no program much shorter than the string itself produces
it; the length of the shortest such program is its Kolmogorov complexity K(x).

## Facts
- Invariance: K depends on the reference universal machine only up to an additive constant.
- K(x) ≤ |x| + c; by counting, at most 2^{n−k} strings of length n have K < n − k, so most strings are
  incompressible (the [[pigeonhole-principle]] again). Incompressibility arguments give lower bounds
  (e.g. one-tape Turing machines need Ω(n²) for palindromes).
- **Uncomputable**: if K were computable, "the smallest number whose K ≥ n" would be describable in
  O(log n) bits (Berry paradox); relates to the [[computability-and-halting-problem]]. Upper bounds are
  easy (run gzip); lower bounds are impossible to certify in general.
- Expected K of samples from a computable distribution ≈ its entropy: K is entropy for individual
  objects ([[entropy-and-information]]).
- Chaitin's Ω (halting probability) is algorithmically random.

## Minimum description length (MDL)
Pick the model M minimizing L(M) + L(data | M): bits to describe the model plus bits to encode the
data with it. Equivalent to MAP with the prior 2^{−L(M)} and to the Bayesian evidence framework
(MacKay ch. 28). Penalizes complexity automatically — the principled form of Occam's razor behind
BIC and behind "a model that compresses well predicts well" ([[maximum-likelihood-estimation]],
[[source-coding-and-compression]]). Normalized compression distance (NCD) uses real compressors to
cluster sequences/files without features.

## Related
- [[entropy-and-information]], [[source-coding-and-compression]], [[computability-and-halting-problem]].

## Sources
MacKay ch. 28 (Occam's razor, evidence); Li & Vitányi for the theory (not ingested).

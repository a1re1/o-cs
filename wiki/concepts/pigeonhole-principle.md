---
title: Pigeonhole principle
type: concept
section: "1.1"
level: 200
tags: [pigeonhole, combinatorics, existence-proofs, hashing, collisions]
sources: [mcs-lehman-leighton-meyer]
summary: If more than k·|B| pigeons fly into |B| holes some hole holds at least k+1; the three-part recipe (name the pigeons, the holes, the function) and its CS consequences — hash collisions, lossless compression limits, and subset-sum coincidences.
---
# Pigeonhole principle

**In one sentence.** If |A| > |B| then no function A → B is injective, so two elements of A share an
image; generalized: |A| > k|B| forces k+1 elements to share.

## Recipe (MCS 14.8)
Solving a pigeonhole problem means identifying exactly three things:
1. the set A of **pigeons**,
2. the set B of **holes**,
3. the **function** f: A → B assigning each pigeon to a hole.
Then |A| > |B| does the rest. The creativity is in choosing f.

## Examples
- Socks in the dark with 3 colours: 4 socks guarantee a pair.
- Boston: 500,000 non-bald people, ≤ 200,000 possible hair counts ⇒ at least three people with
  identical hair counts (generalized principle, k = 2).
- Subset sums: among ninety 25-digit numbers there are 2^90 subsets but sums are < 90·10^25 < 10^27, so
  two different subsets have the same sum — a pure existence proof; finding them is hard (this is
  subset-sum, NP-hard).
- **Hashing**: any hash from strings of length > k bits to k bits has collisions; a table with m slots
  and > m keys must chain or probe ([[hash-tables]]).
- **Compression**: no lossless scheme shrinks *every* file, because 2^n inputs cannot inject into < 2^n outputs.
- Among any n+1 integers from {1..2n}, one divides another (holes = odd parts).

## Pitfalls
- The principle proves *existence*, not *how to find* — algorithms need something else.
- Miscounting the holes (e.g. forgetting the zero case) invalidates the bound.

## Related
- [[counting-rules]], [[sets-relations-functions]] (injection rule).
- [[hash-tables]] — collisions are unavoidable, so handle them.

## Sources
MCS 14.8 (Pigeonhole Principle, generalized principle, subsets with same sum).

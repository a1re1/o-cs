---
title: Counting rules (sum, product, bijection, division, binomial, inclusion–exclusion)
type: concept
section: "1.1"
level: 200
tags: [combinatorics, counting, permutations, combinations, binomial-coefficients, inclusion-exclusion, stars-and-bars, bijection, generalized-product-rule]
sources: [mcs-lehman-leighton-meyer, levin-dmoi, berkeley-cs70]
summary: The handful of rules that count almost everything — sum, product, generalized product, bijection, division (k-to-1), subsets C(n,k), sequences with repetition (multinomials, stars and bars), inclusion–exclusion — with the recipes for recognising which one a problem needs.
---
# Counting rules

**In one sentence.** Reduce the set you care about to one you can count, by a bijection, a product of
choices, or a k-to-1 map, and correct for double counting with inclusion–exclusion.

## The rules
| Rule | Statement | Typical use |
|---|---|---|
| Sum | disjoint A, B: \|A ∪ B\| = \|A\| + \|B\| | case split |
| Product | \|A × B\| = \|A\|·\|B\| | independent choices; n-bit strings = 2^n |
| Generalized product | sequence of k choices with n₁, n₂(after 1st), … options ⇒ n₁n₂…n_k | permutations n!/(n−k)!; passwords with constraints |
| Bijection | \|A\| = \|B\| if a bijection exists | count subsets of an n-set as n-bit strings (2^n) |
| Division (k-to-1) | f: A → B k-to-1 ⇒ \|A\| = k\|B\| | circular arrangements n!/n; subsets C(n,k) = n!/(k!(n−k)!) |
| Bookkeeper / multinomial | arrangements of a word with letter multiplicities | n!/(n₁!…n_k!) |
| Stars and bars | # of solutions to x₁+…+x_k = n in N | C(n+k−1, k−1): donuts of k flavours, multisets |
| Inclusion–exclusion | \|A ∪ B ∪ C\| = Σ\|A_i\| − Σ\|A_i ∩ A_j\| + \|A ∩ B ∩ C\| | "at least one" constraints, derangements |
| Binomial theorem | (x+y)^n = Σ C(n,k) x^k y^{n−k} | identities like Σ C(n,k) = 2^n |

## Recognising the rule
1. Are items ordered? (sequence → product rule; set → divide by k!.)
2. Repetition allowed? (yes → n^k or stars and bars; no → falling factorial or C(n,k).)
3. "At least one of…"? → inclusion–exclusion or complement counting (total − none).
4. Symmetry that maps several arrangements to one object? → division rule.
5. Stuck? Look for a bijection to a set you already know (e.g. lattice paths ↔ bit strings).

## Combinatorial proofs
Prove an identity by counting one set two ways. Pascal's rule C(n,k) = C(n−1,k−1) + C(n−1,k): subsets
of n containing element n vs not. Vandermonde: C(m+n,k) = Σ_j C(m,j)C(n,k−j). Such proofs also give
recurrences for dynamic programming (§3.2).

## Pitfalls
- Overcounting by treating identical items as distinct (fix with the division rule), or undercounting by
  treating distinct as identical.
- Division rule needs the map to be *exactly* k-to-1 for every target.
- "At least" problems: choosing the "guaranteed" item first then filling the rest overcounts; use
  complement or inclusion–exclusion.

## Related
- [[pigeonhole-principle]] — the contrapositive of the injection rule.
- [[sets-relations-functions]] — the mapping rules.
- [[recurrences]] — generating functions as a counting engine.
- [[four-step-method]] — counting uniform sample spaces gives probabilities.

## Sources
MCS ch. 14; Levin ch. 1; CS70 counting notes.

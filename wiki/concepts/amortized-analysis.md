---
title: Amortized analysis — aggregate, accounting, and potential methods
type: concept
section: "2.4"
level: 300
tags: [amortized-analysis, aggregate-method, accounting-method, bankers-method, potential-method, physicists-method, dynamic-array, binary-counter, two-stack-queue, splay-trees, union-find, persistence]
sources: [okasaki-purely-functional-data-structures, cs3110-ocaml, clrs]
summary: Amortized cost bounds the total cost of any sequence of n operations by n times a per-operation figure even though individual operations may be expensive; prove it by aggregate counting, by the accounting/banker's method (prepay credits on cheap operations), or by the potential/physicist's method (Φ ≥ 0, amortized = actual + ΔΦ); dynamic arrays, binary counters, two-stack queues, splay trees and union–find are the standard examples, and persistence breaks the credit argument unless laziness memoizes the expensive work.
---
# Amortized analysis

**In one sentence.** "Rare expensive operations are paid for by many cheap ones" — a worst-case bound
on *sequences*, not an average over inputs ([[probabilistic-analysis-of-algorithms]] is the latter).

## Three methods (CLRS ch. 17)
1. **Aggregate**: bound the total T(n) of any n operations directly; amortized = T(n)/n.
   Binary counter: n increments flip ≤ 2n bits total ⇒ O(1) amortized.
2. **Accounting (banker's)**: charge each operation an amortized cost; the surplus is stored as
   credits on parts of the structure and spent later. Invariant: credit never negative.
   Dynamic array: charge 3 per push (1 to write, 2 saved for copying itself and one old element
   when the array doubles) ⇒ O(1) amortized push despite O(n) resizes.
3. **Potential (physicist's)**: define Φ(D) ≥ 0 with Φ(D₀) = 0; amortized cᵢ' = cᵢ + Φ(Dᵢ) − Φ(Dᵢ₋₁);
   Σcᵢ' ≥ Σcᵢ. Two-stack queue: Φ = size of the input stack; push costs 2, pop is O(1) amortized.
   Splay trees: Φ = Σ log(size of subtree) gives O(log n) amortized. Union–find with path
   compression + union by rank: O(α(n)) amortized.

## Persistence changes the rules (Okasaki ch. 3)
Credits assume each version is operated on once. With persistent structures an old version can be
reused ("multiple futures") and the expensive step repeated. Remedy: perform expensive work lazily
and **memoize** it so it happens once for all futures; account with **debits** attached to
suspensions, discharged before the suspension is forced (banker's method for lazy structures) or a
potential over unevaluated suspensions (physicist's) — [[persistent-data-structures]].
Scheduling converts amortized to worst-case bounds where latency matters (real-time systems, GC).

## Pitfalls
- Amortized ≠ worst-case per operation: one pop may take O(n); unacceptable for real-time paths.
- Forgetting that removal can undo credits (shrinking a dynamic array at half full causes O(n)
  thrash; shrink at quarter full).
- Mixing amortized bounds with persistence or with concurrency (the same version used by many
  threads).

## Related
- [[persistent-data-structures]], [[hash-tables]] (resize), [[balanced-search-trees]] (splay),
  [[union-find]], [[asymptotic-notation]], [[probabilistic-analysis-of-algorithms]].

## Sources
CLRS ch. 17; CS3110 9.2; Okasaki ch. 3–4.

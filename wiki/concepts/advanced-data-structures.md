---
title: Advanced data structures — persistence, integer structures (van Emde Boas), cache-oblivious, succinct, and dynamic trees
type: concept
section: "3.3"
level: 500
tags: [advanced-data-structures, persistence, partial-persistence, full-persistence, retroactivity, van-emde-boas, y-fast-tries, fusion-trees, predecessor-problem, cache-oblivious, memory-hierarchy, succinct-data-structures, rank-select, link-cut-trees, euler-tour-trees, splay-trees, dynamic-optimality, fibonacci-heaps, fractional-cascading, range-trees]
sources: [cs168-modern-algorithmic-toolbox, karp-cook-and-classic-papers, okasaki-purely-functional-data-structures]
summary: Demaine's 6.851 organizes the frontier by model — temporal (make any pointer-machine structure partially persistent with O(1) amortized overhead via fat nodes and node copying; full persistence; retroactivity), integer (van Emde Boas O(log log u) predecessor; y-fast tries in O(n) space; fusion trees O(log_w n); the tradeoff lower bound), memory hierarchy (external-memory B-trees and cache-oblivious structures that are optimal for every cache level without knowing its size), succinct (rank/select in n + o(n) bits, succinct trees), dynamic trees (link-cut, Euler tour trees for dynamic connectivity), geometric (range trees, fractional cascading), and dynamic optimality (splay trees, tango trees).
---
# Advanced data structures

**In one sentence.** Each family answers "what if the model changes?" — time travels
(persistence), keys are machine words (integer structures), memory is hierarchical
(cache-oblivious), space is tight (succinct), or the tree itself changes (dynamic trees).

## Temporal (6.851 L1–L2)
- **Partial persistence** (query any version, update only the latest): Driscoll–Sarnak–Sleator–
  Tarjan — fat nodes with version stamps, or *node copying* with O(1) extra modification slots
  per node; any bounded-in-degree pointer-machine structure gets O(1) amortized overhead per
  operation and O(1) space per change. **Full persistence** (update any version; versions form a
  tree) with an order-maintenance structure for version numbering. **Confluent** (merge
  versions) is largely open. Functional persistence via path copying ([[persistent-data-structures]]).
- **Retroactivity**: change the *past operation sequence* and see the effect now (partial:
  queries at present; full: queries anywhere); priority queues retroactively in O(log n).

## Integer structures (predecessor problem)
Keys from a universe {0..u−1}, word size w ≥ log u. **van Emde Boas**: recursive √u split with
summary → O(log log u) time, O(u) space; **y-fast tries** (x-fast trie of √-samples + balanced
BSTs) → O(log log u) expected, O(n) space; **fusion trees** (Fredman–Willard): B = w^{1/5}
keys per node compared in parallel by sketching → O(log_w n); combining gives
O(min(log_w n, log log u)) and Pătraşcu–Thorup show this is optimal. Practical descendants:
radix trees, Judy arrays, ART, `std::bitset` tricks ([[tries]], [[integer-representation-and-bits]]).

## Memory hierarchy
External-memory model (block size B, memory M): B-trees O(log_B n), sorting O((n/B) log_{M/B}
(n/B)). **Cache-oblivious** (Frigo–Leiserson–Prokop–Ramachandran): no B or M in the code —
recursive layouts (van Emde Boas tree layout, funnelsort, cache-oblivious B-trees via packed-
memory arrays) are optimal at *every* level of the hierarchy simultaneously
([[caches-and-memory-hierarchy]], [[divide-and-conquer]]).

## Succinct structures
Store n-item structures in the information-theoretic minimum + o(n) bits while supporting
operations: **rank/select** on bitvectors in O(1) with o(n) extra (Jacobson; Clark); balanced-
parentheses/LOUDS trees in 2n + o(n) bits with navigation; wavelet trees for rank/select over
large alphabets; compressed suffix arrays and FM-index ([[string-algorithms]]).

## Dynamic trees and graphs
**Link-cut trees** (Sleator–Tarjan): link, cut, path aggregates in O(log n) amortized using splay
trees on preferred paths; **Euler tour trees** for subtree aggregates and dynamic forest
connectivity; Holm–de Lichtenberg–Thorup dynamic connectivity in O(log² n) amortized; top trees.
[[union-find]] is the incremental special case.

## Dynamic optimality and heaps
**Splay trees** are O(log n) amortized and satisfy static optimality, working-set and dynamic-
finger bounds; the **dynamic optimality conjecture** (splay is O(1)-competitive with any BST
algorithm) is open; tango trees achieve O(log log n)-competitive. **Fibonacci heaps**
(Fredman–Tarjan) — lazy consolidation, cascading cuts, potential = trees + 2·marked → O(1)
amortized decrease-key; pairing heaps in practice ([[heaps-and-priority-queues]],
[[amortized-analysis]]).

## Geometric
Range trees (O(log^{d−1} n) with fractional cascading), k-d trees, segment/interval trees,
priority search trees, kinetic data structures — [[advanced-data-structures]].

## Related
- [[persistent-data-structures]], [[balanced-search-trees]], [[amortized-analysis]], [[tries]],
  [[caches-and-memory-hierarchy]], [[string-algorithms]], [[union-find]], [[heaps-and-priority-queues]].

## Sources
MIT 6.851 lectures 1–20 (Demaine); Fredman & Tarjan 1987; Okasaki.

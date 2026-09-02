---
title: Range queries — prefix sums, sparse tables, Fenwick (binary indexed) trees, segment trees with lazy propagation
type: concept
section: "3.4"
level: 300
tags: [range-queries, prefix-sums, sparse-table, rmq, fenwick-tree, binary-indexed-tree, segment-tree, lazy-propagation, point-update, range-update, persistent-segment-tree, 2d-queries, monoid, sqrt-decomposition]
sources: [competitive-programmers-handbook, clrs]
summary: Answer "aggregate over [l, r]" fast — prefix sums give O(1) static sums, sparse tables O(1) static idempotent queries (min/gcd) after O(n log n), Fenwick trees O(log n) point update + prefix query with 20 lines of code (index arithmetic on the lowest set bit), and segment trees O(log n) for any associative operation with point or, via lazy propagation, range updates; extensions include order statistics, persistence, 2D, and merge-sort trees, and sqrt decomposition is the fallback when the operation isn't a monoid.
---
# Range queries

**In one sentence.** Precompute aggregates over a hierarchy of intervals so any [l, r] decomposes
into O(log n) stored pieces.

## Static arrays (CPH ch. 9.1)
- **Prefix sums**: P[i] = Σ a[0..i); sum(l, r) = P[r] − P[l]. 2D: inclusion–exclusion on corners.
  Difference arrays for offline range *updates* (add on [l, r] = +v at l, −v at r+1, then prefix).
- **Sparse table** for idempotent ops (min, max, gcd, OR): st[k][i] = op over [i, i + 2ᵏ); query
  = op(st[k][l], st[k][r − 2ᵏ + 1]) with k = ⌊log(r − l + 1)⌋ — O(1) after O(n log n).

## Fenwick / binary indexed tree (CPH 9.2)
`tree[i]` stores the sum of the last `lowbit(i) = i & −i` elements ending at i (1-indexed).
```
prefix(i): s = 0; while i > 0: s += tree[i]; i -= i & -i
update(i, d): while i <= n: tree[i] += d; i += i & -i
```
O(log n) both; O(n) memory; build in O(n). Range sum = prefix(r) − prefix(l−1). Tricks: range
update + point query (BIT over the difference array), range update + range query (two BITs),
k-th smallest by binary lifting on the tree, 2D BIT. Works for any invertible group operation
(sum, xor), not min.

## Segment tree (CPH 9.3, 28)
Complete binary tree over positions; node covers an interval and stores op of its children; leaves
are elements. Point update: walk root→leaf, recompute O(log n) nodes. Query [l, r]: recurse,
returning fully covered nodes — O(log n) nodes touched. Works for any **monoid** (sum, min, max,
gcd, matrix product, "best subarray" tuples, hash of a segment). Iterative bottom-up version uses
array `t[2n]`, leaves at n..2n−1.
**Lazy propagation** for range updates: each node keeps a pending update to apply to its whole
interval; push down to children only when descending — O(log n) per range add/assign with range
sum/min. Combine "add" and "assign" carefully (assign overrides add).
Extensions: **persistent** segment tree (path copying, O(log n) new nodes per update — versions
for "k-th smallest in [l, r]" — [[persistent-data-structures]]); dynamic/implicit nodes for huge
coordinate ranges; 2D segment trees; merge-sort tree (count < x in range); segment tree beats;
Li Chao tree for lines; segment tree on Euler tour for subtree queries ([[graph-search]]).

## Sqrt decomposition and Mo's algorithm (CPH 27)
Split into blocks of √n: update O(1)/O(√n), query O(√n). Mo's algorithm answers offline range
queries in O((n + q)√n) by ordering queries by (block of l, r) and moving two pointers. Use when
the operation has no clean monoid (distinct counts, mode).

## Choosing
| Need | Structure |
|---|---|
| static sum | prefix sums |
| static min/gcd | sparse table |
| point update + prefix/range sum | Fenwick |
| point update + any monoid | segment tree |
| range update + range query | lazy segment tree (or two BITs for sums) |
| versions / k-th in range | persistent segment tree |
| weird offline queries | Mo's / sqrt decomposition |

## Pitfalls
- 0- vs 1-indexing in Fenwick (`i & -i` fails at 0); overflow in sums (use 64-bit).
- Segment tree size: allocate 4n (recursive) or 2·2^⌈log n⌉; forgetting to push lazy tags on
  query; non-commutative ops need left/right order preserved.
- Using a BIT for min (not invertible) — needs a segment tree.

## Related
- [[balanced-search-trees]] (order statistics alternatives), [[persistent-data-structures]],
  [[amortized-analysis]], [[divide-and-conquer]], [[competitive-programming-techniques]],
  [[advanced-data-structures]].

## Sources
CPH ch. 9, 27, 28; CLRS ch. 17 (augmenting).

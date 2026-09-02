---
title: Heaps and priority queues — binary heap, heapsort, and variants
type: concept
section: "3.1"
level: 200
tags: [heaps, priority-queues, binary-heap, heapify, sift-up, sift-down, swim, sink, heapsort, min-heap, max-heap, decrease-key, indexed-priority-queue, d-ary-heap, fibonacci-heap, top-k, dijkstra]
sources: [sedgewick-algorithms-4e, open-data-structures-morin, berkeley-cs61b, clrs]
summary: A priority queue supports insert and delete-min (or max); a binary heap implements it as a complete binary tree stored in an array (children of i at 2i+1, 2i+2) with the heap-order invariant — insert sifts up, delete-min swaps the last leaf to the root and sifts down, both O(log n); build-heap is O(n) bottom-up; heapsort is in-place O(n log n); indexed heaps add decrease-key for Dijkstra/Prim, and d-ary, pairing and Fibonacci heaps trade constants for better amortized bounds.
---
# Heaps and priority queues

**In one sentence.** Keep only a *partial* order — every parent ≤ its children — and the minimum is
always at the root, with O(log n) repairs after each change.

## Binary heap (Sedgewick 2.4)
- Complete binary tree in an array: root at 0, children of i at `2i+1, 2i+2`, parent at
  `(i−1)/2` (1-indexed: `2i, 2i+1, i/2`). No pointers; contiguous memory
  ([[caches-and-memory-hierarchy]]).
- **Heap order**: parent ≤ children (min-heap). Not sorted; siblings unordered.
- `insert`: append, **swim/sift-up** while smaller than parent — O(log n).
- `delete-min`: take root, move last element to root, **sink/sift-down** swapping with the smaller
  child — O(log n). `peek` O(1).
- **Build-heap**: sink every internal node from `n/2` down to 0 — O(n) total (Σ nodes×height is
  geometric), better than n inserts (O(n log n)).
- **Heapsort**: build max-heap, repeatedly swap root with last and sink on a shrinking prefix —
  in-place, O(n log n) worst case, not stable, poor cache behaviour vs quicksort ([[sorting]]).

## Variants
| Need | Structure |
|---|---|
| decrease-key (Dijkstra, Prim) | **indexed priority queue** (heap + position map) — [[shortest-paths]] |
| fewer cache misses | d-ary heap (d = 4–8) |
| merge two heaps | leftist / skew / pairing / binomial heaps ([[persistent-data-structures]] for functional ones) |
| O(1) amortized decrease-key | Fibonacci heap (theory; pairing heaps win in practice) |
| both min and max | min-max heap or two heaps |
| median / top-k of a stream | two heaps / one bounded heap of size k |
| timers, schedulers | heap keyed by deadline; timing wheels for coarse buckets |

## Uses
Event simulation, Dijkstra/Prim/A*, Huffman coding, k-way merge (external sort, log-structured
storage), top-k queries, load balancers, OS schedulers, `heapq`/`PriorityQueue`/`BinaryHeap`.

## Pitfalls
- Off-by-one in index arithmetic (0- vs 1-based); forgetting to compare with the *smaller* child.
- Updating a key in place without re-sifting (need an indexed PQ or lazy deletion with stale
  entries skipped).
- Assuming heap iteration order is sorted.

## Related
- [[sorting]], [[shortest-paths]], [[binary-search-trees]], [[amortized-analysis]], [[source-coding-and-compression]]
  (Huffman), [[arrays-and-linked-lists]].

## Sources
Sedgewick 2.4; ODS ch. 10; CS61B week 8; CLRS ch. 6.

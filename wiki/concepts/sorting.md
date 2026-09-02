---
title: Sorting — comparison sorts, the n log n lower bound, and linear-time sorts
type: concept
section: "3.2"
level: 200
tags: [sorting, mergesort, quicksort, heapsort, insertion-sort, timsort, introsort, stability, in-place, comparison-lower-bound, decision-tree, counting-sort, radix-sort, bucket-sort, selection, quickselect, external-sort]
sources: [clrs, sedgewick-algorithms-4e, roughgarden-algorithms-illuminated, berkeley-cs61b, erickson-algorithms]
summary: Comparison sorting needs Ω(n log n) comparisons (a decision tree with n! leaves has depth ≥ log₂ n!), matched by mergesort (stable, O(n) extra space), heapsort (in place, poor locality) and quicksort (in place, fastest in practice with random pivots and 3-way partitioning, O(n²) worst case); insertion sort wins for tiny or nearly sorted inputs; counting, radix and bucket sort beat the bound by not comparing (O(n + k), O(d(n + k))); library sorts are hybrids (Timsort, introsort, pdqsort), and selection (k-th smallest) is O(n) expected via QuickSelect.
---
# Sorting

**In one sentence.** Know four algorithms and one lower bound: mergesort, quicksort, heapsort and
insertion sort cover every situation, and Ω(n log n) tells you when to stop looking.

## The comparison sorts
| Algorithm | Time (best / avg / worst) | Space | Stable | Notes |
|---|---|---|---|---|
| Insertion sort | n / n² / n² | O(1) | yes | fastest for n ≲ 16 or nearly sorted (O(n + inversions)); the base case of hybrids |
| Selection sort | n² | O(1) | no | minimal writes |
| Shellsort | ~n^{4/3} | O(1) | no | gap sequences; embedded systems |
| **Mergesort** | n log n always | O(n) (O(1) tricky) | **yes** | [[divide-and-conquer]]; bottom-up variant; the external/parallel sort; linked lists |
| **Quicksort** | n log n / n log n / n² | O(log n) stack | no | partition around a pivot; random pivot ⇒ expected 2n ln n compares ([[randomized-algorithms]]); 3-way (Dijkstra/Bentley–McIlroy) for many duplicates; cutoff to insertion sort |
| **Heapsort** | n log n always | O(1) | no | in place, guaranteed, but cache-unfriendly ([[heaps-and-priority-queues]]) |
| Timsort (Python, Java objects) | n / n log n | O(n) | yes | merges natural runs; adaptive |
| Introsort / pdqsort (C++, Rust unstable) | n log n | O(log n) | no | quicksort + heapsort fallback + insertion sort |

## The lower bound (CLRS 8.1)
Any comparison sort is a decision tree with ≥ n! leaves, so its height (worst-case comparisons)
is ≥ log₂(n!) = Θ(n log n) (Stirling, [[asymptotic-notation]]). Average case has the same bound
(information-theoretic: log₂ n! bits are needed to specify a permutation — [[entropy-and-information]]).

## Beating the bound by not comparing
- **Counting sort**: keys in [0, k): count, prefix-sum, place — O(n + k), stable.
- **Radix sort**: LSD (stable passes from least significant digit; O(d(n + k)) for d digits) or
  MSD (recursive bucketing, like a trie — [[tries]]); strings, fixed-width integers; Sedgewick's
  3-way string quicksort.
- **Bucket sort**: uniformly distributed keys into n buckets, insertion-sort each — expected O(n).
These are the workhorses for integers, GPU sorts, and suffix-array construction.

## Selection and partial sorting
k-th smallest: **QuickSelect** expected O(n) (recurse on one side); median-of-medians worst-case
O(n) ([[divide-and-conquer]]); top-k with a size-k heap O(n log k); `nth_element`/`partial_sort`.

## Choosing
Default to the library sort. Need stability (sort by multiple keys sequentially) → mergesort/
Timsort. Memory-constrained → heapsort or in-place quicksort. Small integer keys → counting/radix.
Data on disk → external mergesort (k-way merge with a heap). Nearly sorted → insertion/Timsort.
Linked lists → mergesort. Parallel → mergesort/sample sort.

## Pitfalls
- Quicksort with first-element pivot on sorted input (O(n²), deep recursion) — shuffle or choose
  median-of-three/random.
- Comparators that aren't strict weak orders (NaN, inconsistent ties) → undefined behaviour in
  `std::sort`, exceptions in Java.
- Assuming sort stability where the library doesn't promise it.

## Related
- [[divide-and-conquer]], [[randomized-algorithms]], [[heaps-and-priority-queues]], [[asymptotic-notation]],
  [[entropy-and-information]], [[tries]], [[caches-and-memory-hierarchy]].

## Sources
CLRS ch. 2, 6–9; Sedgewick ch. 2, 5.1; Roughgarden part 1; CS61B weeks 12–13.

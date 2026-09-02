---
title: Cache-oblivious algorithms — the ideal-cache model, recursive divide-and-conquer that is optimal at every level of the hierarchy, and the van Emde Boas layout
type: concept
section: "4.7"
level: 500
tags: [cache-oblivious, cache-aware, ideal-cache-model, external-memory-model, io-model, cache-complexity, block-size, tall-cache, recursive-matrix-multiply, matrix-transpose, funnelsort, van-emde-boas-layout, cache-oblivious-b-tree, stencil-trapezoids, frigo-leiserson-prokop-ramachandran, blocking, tiling, memory-hierarchy]
sources: [stanford-cs149-and-cmu-15-418, parallel-computing-seminal-papers]
summary: In the external-memory (I/O) model a cache of size M with lines of B words sits in front of slow memory and cost is the number of line transfers; cache-aware algorithms tune B and M explicitly (blocked matrix multiply, B-trees), whereas cache-oblivious algorithms (Frigo, Leiserson, Prokop & Ramachandran 1999) know neither yet achieve asymptotically optimal transfers at every level simultaneously by recursing until subproblems fit in whatever cache exists — recursive matrix multiply and transpose (Θ(n³/(B√M)) and Θ(n²/B) misses), funnelsort (Θ((n/B) log_{M/B}(n/B)), matching the external-memory lower bound), the van Emde Boas layout that stores a search tree recursively by height halves so any search touches O(log_B n) lines, and cache-oblivious stencils via space–time trapezoids — a design principle (recursive locality) that also explains why Z-order/Morton layouts and divide-and-conquer are cache friendly.
---
# Cache-oblivious algorithms

**In one sentence.** Divide and conquer until the problem fits in the cache — any cache — and
you get an algorithm that is optimal for the L1, L2, L3, DRAM and disk levels without ever
being told their sizes.

## Models (6.172 L14–15)
**External-memory / I/O model** (Aggarwal & Vitter 1988): main memory of size M, transfers in
blocks of B, count block transfers. Lower bounds: scanning n/B, sorting Θ((n/B) log_{M/B}(n/B)),
searching Θ(log_B n) — B-trees ([[storage-engines-and-indexes]]) and blocked/tiled algorithms
are **cache-aware** solutions tuned to B and M. The **ideal-cache model**: fully associative,
optimal replacement, tall cache (M ≥ B²) — LRU with a 2× larger cache is within a constant
factor (Sleator–Tarjan competitiveness, [[amortized-analysis]]), so results transfer to real
caches. **Cache-oblivious**: the algorithm has no parameters B or M; analysis assumes an ideal
cache with any B, M — and since that holds for every level, the algorithm is simultaneously
optimal across the whole hierarchy ([[caches-and-memory-hierarchy]]).

## Canonical algorithms (Frigo et al. 1999)
- **Matrix multiply**: split the largest dimension in half recursively; once a subproblem's
  three submatrices fit in M (side ~√M) they load in O(M/B) transfers ⇒ Θ(n³/(B√M)) total,
  matching blocked multiply — with no block size chosen. Same for **transpose**/FFT (Θ(n²/B)),
  and the cache-oblivious FFT via the four-step method ([[fft]]).
- **Funnelsort**: recursively sort n^{1/3} subarrays and merge with a **k-funnel** (a recursive
  merger that buffers output between levels) ⇒ optimal Θ((n/B) log_{M/B}(n/B)); lazy funnelsort
  is practical-ish; in practice, recursive merge sort with a cache-aware base case is close
  ([[sorting]]).
- **Search — van Emde Boas layout**: store a complete binary tree by cutting at half height:
  the top subtree of √n nodes, then each bottom subtree, each laid out recursively; any
  root-to-leaf path crosses O(log_B n) blocks for every B at once. Cache-oblivious B-trees /
  packed-memory arrays support dynamic insertion (Bender, Demaine, Farach-Colton); used in
  static dictionaries and some databases. Morton/Z-order layouts give the same property for
  matrices.
- **Stencils and dynamic programming**: recursive space–time **trapezoid** decomposition
  (Frigo & Strumpen) achieves Θ(nt/(B·M^{1/d})) misses for d-dimensional stencils; cache-
  oblivious LCS/edit distance and Floyd–Warshall via recursive blocking ([[dynamic-programming]]).
- Scanning, prefix sums, and any linear-work recursion are trivially cache-oblivious.

## In practice
Recursion overhead — coarsen the base case (which is a small cache-aware tuning); real caches
have limited associativity and prefetchers favouring sequential access; TLBs add another
level (huge pages). Cache-oblivious code is a robust default when the target hierarchy is
unknown (libraries, portable kernels); cache-aware blocking wins the last 10–30 % when the
target is known (BLAS). Parallel cache-oblivious algorithms combine with work stealing
([[work-stealing-and-fork-join]]) — the same recursion gives locality and parallelism.

## Pitfalls
- Recursing to n = 1; measuring on tiny inputs where everything fits in L2.
- Assuming the tall-cache assumption holds for very large lines/pages.
- Ignoring the difference between cache misses and bandwidth (roofline still applies —
  [[roofline-model]]).

## Related
- [[caches-and-memory-hierarchy]], [[divide-and-conquer]], [[sorting]], [[fft]],
  [[storage-engines-and-indexes]], [[roofline-model]], [[work-stealing-and-fork-join]],
  [[dynamic-programming]].

## Sources
Frigo, Leiserson, Prokop & Ramachandran 1999; Demaine "Cache-Oblivious Algorithms and Data Structures" (survey 2002); Aggarwal & Vitter 1988; 6.172 L14–15; Bender, Demaine & Farach-Colton 2000.

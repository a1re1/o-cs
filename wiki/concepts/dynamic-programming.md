---
title: Dynamic programming — smart recursion, memoization, and the subproblem DAG
type: concept
section: "3.2"
level: 300
tags: [dynamic-programming, memoization, recurrence, optimal-substructure, overlapping-subproblems, subproblem-dag, edit-distance, knapsack, longest-common-subsequence, longest-increasing-subsequence, bellman-ford, floyd-warshall, tabulation, reconstruction, pseudo-polynomial]
sources: [erickson-algorithms, dpv-algorithms, clrs, kleinberg-tardos-skiena]
summary: Dynamic programming is recursion without repetition — write a precise English specification of a subproblem, a correct recurrence that expresses it in terms of smaller instances of the same problem, then memoize or fill a table in an order that respects the dependency DAG; running time = number of subproblems × work per subproblem, and the recurrence, not the table, is the hard part. Classic instances: Fibonacci, LIS, edit distance/alignment, LCS, knapsack, matrix chain, optimal BSTs, shortest paths (Bellman–Ford, Floyd–Warshall), DP on trees and DAGs.
---
# Dynamic programming

**In one sentence.** "Dynamic programming is not about filling in tables. It's about smart
recursion" (Erickson) — find a recurrence over a small family of subproblems, then evaluate each
once.

## Erickson's two-stage recipe
1. **Formulate recursively.** (a) *Specification*: describe in coherent English *what* the
   subproblem computes (e.g. "LIS(i) = length of the longest increasing subsequence of A[i..n]
   that starts at A[i]"). Without this you cannot even check correctness. (b) *Solution*: a
   recurrence in terms of smaller instances of exactly that problem, with base cases.
2. **Build bottom-up.** (a) identify all distinct subproblems reachable from the initial call;
   (b) choose a memo structure (usually an array indexed by the parameters); (c) identify
   dependencies — draw the arrows; (d) pick an evaluation order — a linear extension of the
   dependency partial order ([[dags-and-partial-orders]]); (e) time = Σ over subproblems of the
   work per subproblem assuming recursive calls are O(1) lookups, space = number of subproblems;
   (f) write the nested loops. Memoized recursion (top-down) computes the same thing in DFS
   order and skips unreachable subproblems; DPV: "DP = a DAG of subproblems solved in
   topological order."

## When it applies
**Optimal substructure** (an optimal solution contains optimal solutions to subproblems — usually
provable by cut-and-paste) plus **overlapping subproblems** (the naive recursion recomputes the
same instances — Fibonacci's recursion tree has 2ⁿ nodes but n distinct arguments). If subproblems
don't overlap, it's [[divide-and-conquer]]; if a local choice is provably safe, it's
[[greedy-algorithms]] ("greed is stupid" until an exchange argument says otherwise).

## The canon (subproblem → recurrence)
| Problem | Subproblem | Recurrence | Cost |
|---|---|---|---|
| Fibonacci | F(n) | F(n−1) + F(n−2) | O(n) |
| Longest increasing subsequence | LIS(i) ending at i | 1 + max{LIS(j): j<i, A[j]<A[i]} | O(n²) (O(n log n) with patience sorting) |
| Edit distance / alignment | E(i, j) for prefixes | min(E(i−1,j)+1, E(i,j−1)+1, E(i−1,j−1)+[a≠b]) | O(mn); O(min) space with two rows; Hirschberg for the path |
| LCS | L(i, j) | L(i−1,j−1)+1 if match else max(L(i−1,j), L(i,j−1)) | O(mn) |
| 0/1 knapsack | K(i, w) | max(K(i−1,w), vᵢ + K(i−1, w−wᵢ)) | O(nW) — **pseudo-polynomial** (W in binary is log W bits) |
| Matrix chain / optimal BST | C(i, j) over intervals | min over split k | O(n³) (Knuth's optimization O(n²)) |
| Bellman–Ford | d_k(v) with ≤ k edges | min over in-edges | O(VE) — [[shortest-paths]] |
| Floyd–Warshall | d_k(u, v) using intermediates ≤ k | min(d_{k−1}(u,v), d_{k−1}(u,k)+d_{k−1}(k,v)) | O(V³) |
| Independent set on trees / tree DP | best(v, taken?) | combine children | O(n) |
| TSP (Held–Karp) | C(S, j) | min over last vertex | O(2ⁿ n²) — exponential but ≪ n! |
| Segmented least squares, weighted interval scheduling, RNA folding, text segmentation, coin change, rod cutting | … | … | K&T / Erickson |
**Reconstruction**: store the argmin/argmax choice per subproblem (or recompute by walking back).

## Pitfalls
- A recurrence that is wrong because the subproblem is under-specified ("best so far" without
  saying *ending where* / *using which prefix*). Fix the English first.
- Wrong evaluation order (using a cell before it is computed); off-by-one on base cases.
- Confusing exponential subproblem families (subsets) with polynomial ones (prefixes, intervals,
  suffixes×prefixes) — choose parameters that shrink.
- Memory blow-up: keep only the rows you need; pseudo-polynomial ≠ polynomial.

## Related
- [[recurrences]], [[divide-and-conquer]], [[greedy-algorithms]], [[graph-search]] (memoization =
  DFS), [[shortest-paths]], [[dags-and-partial-orders]], [[induction]] (the correctness proof),
  [[np-completeness-and-reductions]] (knapsack is NP-hard yet has a DP).

## Sources
Erickson ch. 3; DPV ch. 6; CLRS ch. 14; K&T ch. 6; Roughgarden part 3.

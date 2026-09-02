---
title: Competitive programming techniques — complexity budgeting, complete search, meet in the middle, two pointers, binary search on the answer, bitmask DP
type: concept
section: "3.4"
level: 300
tags: [competitive-programming, complexity-budget, complete-search, backtracking, pruning, meet-in-the-middle, two-pointers, sliding-window, monotonic-stack, monotonic-deque, binary-search-on-answer, bitmask-dp, subset-enumeration, sos-dp, prefix-sums, coordinate-compression, offline-queries, binary-lifting, lca, implementation]
sources: [competitive-programmers-handbook, erickson-algorithms]
summary: Contest problem-solving is pattern matching under a time budget — read n to pick the target complexity (n ≤ 20 → 2ⁿ, ≤ 5000 → n², ≤ 10⁶ → n log n), then reach for the matching tool: complete search with pruning or meet in the middle (2^{n/2}), two pointers and monotonic stacks/deques for amortized-linear scans, binary search on the answer when feasibility is monotone, prefix sums and coordinate compression, bitmask DP over subsets (Hamiltonian path 2ⁿn², SOS DP 2ⁿn), binary lifting for LCA and k-th ancestor, and offline processing of queries.
---
# Competitive programming techniques

**In one sentence.** The input size tells you the algorithm: match n to the complexity table,
then apply the standard trick for that budget.

## The budget (CPH 2.3, ~10⁸ simple ops/second)
| n ≤ | target | typical tool |
|---|---|---|
| 10 | n! | permutations, brute force |
| 20 | 2ⁿ | subsets / bitmask DP; meet in the middle to 40 |
| 500 | n³ | Floyd–Warshall, interval DP |
| 5 000 | n² | pairs, LIS n², simple DP |
| 10⁶ | n log n | sorting, BIT/segment tree, Dijkstra, binary search |
| 10⁸ | n | two pointers, prefix sums, sieve |
| bigger | log n / O(1) | math, binary search on answer, closed forms |

## Complete search (CPH ch. 5)
Enumerate subsets by bitmask (`for m in 0..2ⁿ`), permutations by `next_permutation`,
backtracking with pruning (n-queens: symmetry, early infeasibility; order choices by most
constrained). **Meet in the middle**: split into halves, enumerate 2^{n/2} sums each, combine
with sorting/hashing (subset sum with n = 40 → 2·2²⁰). Branch-and-bound with a bound function.

## Amortized linear scans (CPH ch. 8)
- **Two pointers** on sorted or monotone data: subarray with sum x, 2-SUM, merging; each pointer
  only moves forward → O(n) ([[amortized-analysis]]).
- **Sliding window** min/max with a **monotonic deque**; **nearest smaller element** with a
  monotonic stack (largest rectangle in histogram, stock span).
- Prefix sums, difference arrays, prefix xor/gcd/count tricks; **coordinate compression** to map
  large values to ranks before BIT/segment trees ([[range-queries-segment-trees-fenwick]]).

## Binary search on the answer (CPH 3.3)
If "is answer ≤ x feasible?" is monotone and checkable in O(f), the optimum costs O(f log range):
minimize the maximum load, k-th smallest pair distance, largest minimum gap, aggressive cows,
"minimum time to finish" problems. Also ternary search for unimodal functions, parallel binary
search for many queries.

## Bitmask DP (CPH ch. 10)
dp[mask][i] = best way to visit set `mask` ending at i (Hamiltonian path/TSP, O(2ⁿ n²));
dp[mask] over assignments (matching n ≤ 20); **SOS / subset-sum DP** computes Σ over all
submasks in O(2ⁿ n); enumerate submasks with `for s = m; s; s = (s−1) & m`. Bit tricks:
`__builtin_popcount`, `x & −x`, Gray codes ([[integer-representation-and-bits]],
[[dynamic-programming]]).

## Trees and graphs (CPH ch. 14, 18)
Diameter by two BFS/DFS; **binary lifting** `up[k][v]` = 2ᵏ-th ancestor → LCA and k-th ancestor
in O(log n); Euler tour + segment tree for subtree/path queries; rerooting DP; small-to-large
merging (O(n log n) total); centroid decomposition; heavy-light decomposition for path updates.
DP on DAGs (path counts, longest path) after topological sort ([[graph-search]]).

## Offline and reordering tricks
Sort queries and process with a sweep (offline LCA via union-find, Mo's algorithm, CDQ divide and
conquer); process events in time order; reverse the operations (deletions → insertions with
union-find).

## Implementation hygiene
`long long` by default; watch 1e18 overflow in products; fast I/O; avoid `pow` on integers;
modular arithmetic helpers ([[number-theory-algorithms]]); test on n = 1, all-equal, sorted,
reverse-sorted, max n with a stress test against brute force ([[unit-testing]], [[debugging]]).

## Related
- [[dynamic-programming]], [[range-queries-segment-trees-fenwick]], [[graph-search]],
  [[integer-representation-and-bits]], [[number-theory-algorithms]], [[computational-geometry]],
  [[amortized-analysis]], [[sorting]].

## Sources
CPH ch. 2–5, 8, 10, 14, 18, 27; USACO Guide (Silver/Gold); Erickson ch. 2 (backtracking).

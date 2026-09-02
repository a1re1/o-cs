---
title: Greedy algorithms and exchange arguments
type: concept
section: "3.2"
level: 300
tags: [greedy, exchange-argument, greedy-stays-ahead, interval-scheduling, minimizing-lateness, huffman, matroids, cut-property, set-cover, approximation, fractional-knapsack, activity-selection]
sources: [erickson-algorithms, kleinberg-tardos-skiena, clrs, dpv-algorithms]
summary: A greedy algorithm builds a solution by a sequence of locally best choices without revisiting them; it is correct only for problems with the greedy-choice property, proved by an exchange argument (take any optimal solution, find the first place it differs from greedy, swap in the greedy choice without loss, induct) or "greedy stays ahead"; canonical successes are interval scheduling by earliest finish, minimizing lateness by earliest deadline, Huffman coding, MST cut property, Dijkstra, fractional knapsack — and canonical failures are 0/1 knapsack, coin change with odd denominations, and most scheduling variants.
---
# Greedy algorithms

**In one sentence.** Commit to the locally best choice and never look back — "it almost never
works" (Erickson), so a greedy algorithm without an exchange-argument proof is a heuristic.

## The proof pattern (Erickson ch. 4, K&T ch. 4)
**Exchange argument**: assume some optimal solution O differs from greedy G; find the *first*
difference; show you can replace O's choice with G's without making O worse (it might not get
better either); by induction some optimal solution contains all of G's choices, hence equals G
(sometimes with an extra step to show G isn't strictly improvable). **Greedy stays ahead**: show
by induction that after each step greedy's partial solution is at least as good as any
alternative's (interval scheduling: greedy's k-th finish time ≤ any solution's k-th). Both are
[[induction]] in disguise. **Matroids** (CLRS 15.4): when the feasible sets form a matroid
(hereditary + exchange property), greedy by weight is optimal — the structural reason MST works.

## The canon
| Problem | Greedy rule | Proof |
|---|---|---|
| Interval scheduling (max # compatible) | earliest finish time first | stays ahead |
| Minimizing maximum lateness | earliest deadline first (no idle time, no inversions) | exchange adjacent inversions |
| Interval partitioning (min rooms) | by start time, reuse any free room | depth lower bound |
| Fractional knapsack | best value/weight first | exchange |
| Huffman codes | merge the two least frequent symbols | exchange on the deepest leaves ([[source-coding-and-compression]]) |
| MST (Kruskal/Prim/Borůvka) | cheapest safe edge (cut property) | exchange across a cut ([[minimum-spanning-trees]]) |
| Dijkstra | closest unvisited vertex | invariant on finalized distances (non-negative weights) ([[shortest-paths]]) |
| Storing files on tape | shortest (or smallest length/frequency) first | exchange adjacent pair |
| Stable matching (Gale–Shapley) | propose in preference order | invariant, not exchange ([[stable-matching]]) |
| Set cover, vertex cover (2-approx), TSP heuristics | pick the set covering most | approximation ratios (ln n) — [[np-completeness-and-reductions]] |

## Where greedy fails (and what to do)
0/1 knapsack (take the best ratio → wrong; use [[dynamic-programming]]); coin change with
denominations {1, 3, 4} for 6; shortest paths with negative edges (Dijkstra); longest path;
scheduling with weights (weighted interval scheduling needs DP); graph coloring; clustering
beyond single-linkage. Test a candidate greedy rule against tiny adversarial instances before
trying to prove it.

## Pitfalls
- "It worked on the examples" is not a proof; the exchange step must handle every optimal
  solution.
- Sorting by the wrong key (earliest *start* instead of earliest *finish*).
- Greedy that is optimal only under a hidden assumption (non-negative weights, unit sizes).

## Related
- [[dynamic-programming]], [[minimum-spanning-trees]], [[shortest-paths]], [[source-coding-and-compression]],
  [[stable-matching]], [[induction]], [[np-completeness-and-reductions]].

## Sources
Erickson ch. 4; K&T ch. 4; CLRS ch. 15; DPV ch. 5; Roughgarden part 3.

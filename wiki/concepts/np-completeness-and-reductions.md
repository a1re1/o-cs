---
title: NP-completeness and polynomial-time reductions — and what to do when your problem is NP-hard
type: concept
section: "3.2"
level: 400
tags: [np-completeness, np-hard, p-vs-np, polynomial-time-reductions, karp-reductions, cook-levin, sat, 3sat, independent-set, vertex-cover, clique, hamiltonian-cycle, tsp, subset-sum, graph-coloring, approximation-algorithms, branch-and-bound, local-search, sat-solvers, fixed-parameter]
sources: [erickson-algorithms, dpv-algorithms, kleinberg-tardos-skiena, roughgarden-algorithms-illuminated, clrs]
summary: P is what we can solve in polynomial time, NP is what we can verify; a problem is NP-hard if every NP problem reduces to it in polynomial time and NP-complete if it is also in NP; Cook–Levin makes SAT the first, and a web of reductions (3SAT → independent set → vertex cover/clique; 3SAT → Hamiltonian cycle → TSP; 3SAT → subset sum; 3-coloring) transfers hardness — so proving hardness means reducing a known-hard problem *to* yours; then cope with special cases, approximation (vertex cover 2, set cover ln n, knapsack PTAS), exact exponential search (DP over subsets, branch-and-bound), local search, or SAT/MIP solvers.
---
# NP-completeness and reductions

**In one sentence.** If you can reduce 3SAT to your problem in polynomial time, stop looking for a
fast exact algorithm and start choosing which guarantee to give up.

## Definitions
- **Decision problems**; **P**: solvable in polynomial time. **NP**: a yes-instance has a
  certificate checkable in polynomial time (equivalently, non-deterministic polynomial time).
  co-NP: no-instances have certificates. P ⊆ NP ∩ co-NP; P ≠ NP is the open question.
- **Polynomial-time (Karp) reduction** X ≤ₚ Y: a poly-time map f with x ∈ X ⇔ f(x) ∈ Y. Then Y
  fast ⇒ X fast, so **Y is at least as hard as X**. Direction matters: to show *your* problem is
  hard, reduce a known NP-hard problem *to* it.
- **NP-hard**: every NP problem reduces to it. **NP-complete**: NP-hard and in NP.
  **Cook–Levin**: SAT is NP-complete (a poly-time verifier can be encoded as a circuit/formula).
- Same dichotomy as [[computability-and-halting-problem]] one level down: reductions there give
  undecidability, here intractability.

## The reduction web (Erickson ch. 12, DPV ch. 8)
SAT → **3SAT** (clause splitting) → **Independent Set** (a triangle per clause, edges between
literal and its negation; k = #clauses) ↔ **Vertex Cover** (complement) ↔ **Clique** (complement
graph). 3SAT → **3-Coloring** (gadgets) → … 3SAT → **Hamiltonian Cycle/Path** (Rudrata) → **TSP**
(complete graph, weights 1/2, decision at n). 3SAT → **3D Matching** → **Zero-One Equations** →
**Subset Sum** → **Partition** → **Knapsack** (number problems: hardness needs big numbers —
pseudo-polynomial DP exists, "weakly NP-hard"; strongly NP-hard problems like 3-Partition stay hard
with unary numbers). Also: Set Cover, Hitting Set, Graph Coloring (k ≥ 3), Max Cut, Integer
Programming, Longest Path, Bin Packing, Scheduling with precedence, Steiner Tree, Minesweeper,
Sudoku, Tetris. Erickson's recipe: pick the closest known problem (same "flavour": packing,
covering, sequencing, partitioning, numerical), build gadgets, prove both directions of the iff,
check the reduction is polynomial.

## Coping (DPV ch. 9, Roughgarden part 4, K&T ch. 10–12)
1. **Special cases**: trees and bounded treewidth (DP), planar graphs, interval graphs, 2-SAT
   (SCC — [[graph-search]]), small parameters (**FPT**: vertex cover in O(2ᵏ n)).
2. **Approximation** with guarantees: vertex cover 2 (maximal matching), set cover ln n (greedy),
   metric TSP 2 (MST doubling) / 1.5 (Christofides), knapsack FPTAS (scale values), load
   balancing 3/2, LP rounding; inapproximability results bound what's possible.
3. **Exact but exponential**: DP over subsets (TSP Held–Karp 2ⁿn²), backtracking with pruning,
   branch-and-bound with LP relaxations, meet-in-the-middle (2^{n/2}), inclusion–exclusion.
4. **Heuristics**: local search (2-opt, simulated annealing), genetic algorithms — no guarantee,
   often excellent.
5. **Solvers**: SAT (CDCL), SMT, MIP (branch-and-cut), CP — the practical answer for many
   industrial instances; encoding is the skill ([[propositional-logic]], [[linear-programming-and-duality]]).

## Pitfalls
- Reducing in the wrong direction (showing your problem reduces to SAT proves nothing).
- "NP-hard" ≠ "hopeless": instances in practice are often easy; measure.
- Confusing NP (verifiable) with "exponential time"; P vs NP is about *worst case*.
- Forgetting the encoding: numbers in binary make Knapsack hard, unary makes it easy.

## Related
- [[computability-and-halting-problem]], [[dynamic-programming]], [[greedy-algorithms]], [[network-flow]],
  [[linear-programming-and-duality]], [[propositional-logic]], [[complexity-classes]].

## Sources
Erickson ch. 12; DPV ch. 8–9; K&T ch. 8, 10–12; Roughgarden part 4; CLRS ch. 34–35.

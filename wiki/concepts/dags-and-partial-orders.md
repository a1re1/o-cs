---
title: DAGs, partial orders, and scheduling
type: concept
section: "1.1"
level: 200
tags: [dag, directed-graphs, partial-orders, topological-sort, scheduling, chains, antichains, dilworth, critical-path, transitive-closure, well-founded]
sources: [mcs-lehman-leighton-meyer]
summary: Directed graphs and walk relations; DAGs as the shape of every dependency structure; the equivalence between DAGs and strict partial orders; topological orders; minimum parallel schedule time equals the longest chain; and the chain/antichain bound behind Dilworth's theorem.
---
# DAGs, partial orders, and scheduling

**In one sentence.** A directed acyclic graph is exactly a strict partial order (its positive walk
relation), and scheduling tasks with dependencies is a question about chains and antichains in that order.

## Directed graphs
- Edge u → v; in-degree / out-degree; walk relation G⁺ (reachable by ≥ 1 step) and G* (≥ 0 steps) —
  the transitive and reflexive-transitive closures.
- A directed graph has a positive-length closed walk iff it has a cycle (shortcut repeats).
- **DAG** = no cycles. Every finite DAG has a vertex with in-degree 0 (a *minimal* element) — start
  from any vertex and walk backwards; acyclicity forces the walk to end.

## DAGs ⇔ strict partial orders
The relation "u → v by a positive-length walk" in a DAG is irreflexive and transitive, i.e. a
**strict partial order**; conversely the graph of a strict partial order is a DAG. Weak partial orders
add reflexivity (⊆ on sets, | on integers, ≤ on numbers). A **total (linear) order** compares every pair.
Every partial order on a finite set extends to a total order — that extension is a **topological sort**
(repeatedly remove a minimal element; Kahn's algorithm O(V+E), or DFS post-order reversed).

## Scheduling (MCS 9.5)
Tasks with prerequisites form a DAG. A **chain** is a totally ordered subset (a dependency path); an
**antichain** is a set of pairwise incomparable tasks (can run in parallel).
- With unlimited processors, minimum time to finish = length of the longest chain (critical path), and
  the schedule is "run each task at depth = length of the longest chain ending at it".
- **Chain/antichain lemma**: if the longest chain has t elements, the n elements split into t antichains
  (by depth), so some antichain has ≥ n/t elements. Dilworth's theorem is the dual: minimum number of
  chains covering the set = size of the largest antichain.
- With p processors the bound becomes ≥ max(longest chain, n/p) — see Brent's theorem in §4.7 for the
  work/span view.

## Well-founded orders and termination
A strict partial order with no infinite descending chain is **well-founded**; termination proofs pick
a measure into a well-founded order that decreases each step ([[invariant-principle]]). Lexicographic
order on tuples of naturals is well-founded, which handles nested loops.

## Pitfalls
- Topological order is not unique; algorithms that assume one canonical order (e.g. build systems,
  dependency resolution) must break ties deterministically for reproducibility.
- Cycle detection needs DFS colouring (white/grey/black) or Kahn's leftover check; "no vertex of
  in-degree 0" ⇒ cycle.
- Partial order ≠ preorder: antisymmetry fails when two distinct items each precede the other (version
  constraints often produce this).

## Related
- [[graph-theory-basics]], [[sets-relations-functions]] (relations and their properties).
- [[invariant-principle]] — well-founded measures for termination.
- [[graph-search]] — DFS-based topological sort (§3.1).

## Sources
MCS ch. 9 (directed graphs & partial orders: walk relations, DAGs & scheduling, chains/antichains).

---
title: Minimum spanning trees — cut and cycle properties, Kruskal, Prim, Borůvka
type: concept
section: "3.2"
level: 300
tags: [minimum-spanning-trees, mst, cut-property, cycle-property, kruskal, prim, boruvka, jarnik, union-find, priority-queue, clustering, single-linkage, steiner-tree]
sources: [erickson-algorithms, dpv-algorithms, clrs, kleinberg-tardos-skiena, sedgewick-algorithms-4e]
summary: The cut property (the lightest edge crossing any cut is in some MST) and the cycle property (the heaviest edge on any cycle is in no MST) justify every MST algorithm — Kruskal (edges by weight, union-find to skip cycles, O(E log E)), Prim/Jarník (grow one tree from a vertex with a priority queue, O(E log V)), Borůvka (every component adds its cheapest edge in parallel rounds, O(E log V)) — with unique MST under distinct weights; MSTs give single-linkage clustering and 2-approximate TSP tours.
---
# Minimum spanning trees

**In one sentence.** Connect all vertices at minimum total weight; any rule that only ever adds a
"safe" edge — the lightest one across some cut that the current forest doesn't cross — is correct.

## The two properties (DPV 5.1, K&T 4.5)
- **Cut property**: for any partition (S, V∖S) and any lightest edge e crossing it, some MST
  contains e. Proof by exchange: an MST without e plus e has a cycle crossing the cut twice;
  drop the other crossing edge (≥ weight) ([[greedy-algorithms]]).
- **Cycle property**: the strictly heaviest edge on any cycle is in no MST.
- With distinct weights the MST is **unique**; with ties, any consistent tie-break works. A
  spanning tree has exactly V−1 edges; the MST minimizes the *sum*, and also the maximum edge
  (bottleneck) — but not shortest paths between vertices ([[shortest-paths]]).

## Algorithms (all output the same tree under distinct weights)
| Algorithm | Idea | Data structure | Time |
|---|---|---|---|
| **Kruskal** | scan edges in increasing weight; add if endpoints are in different components | sort + [[union-find]] | O(E log E) = O(E log V) |
| **Prim / Jarník** | grow one tree; repeatedly add the lightest edge leaving it | priority queue of vertices keyed by lightest connecting edge (lazy or indexed) | O(E log V) heap; O(V²) dense |
| **Borůvka** | every component picks its lightest outgoing edge; merge; repeat (components at least halve) | union-find | O(E log V); parallel-friendly; basis of expected-linear Karger–Klein–Tarjan |
| Reverse-delete | remove heaviest edge whose removal keeps connectivity | cycle property | slower, conceptual |
Erickson's "generic MST": maintain an acyclic subgraph F; add safe edges (lightest with exactly
one endpoint in a component) until F is a tree.

## Uses
Network design (cabling, pipelines) and approximate Steiner trees; **single-linkage clustering** =
remove the k−1 heaviest MST edges (K&T 4.7); TSP 2-approximation (MST double-tour shortcutting)
and Christofides' 1.5 ([[np-completeness-and-reductions]]); image segmentation; maze generation;
bottleneck paths; taxonomy/phylogeny trees.

## Pitfalls
- Directed graphs: MST ≠ minimum arborescence (Chu–Liu/Edmonds).
- Assuming the MST path between u and v is shortest (it minimizes the bottleneck, not length).
- Kruskal without union-find (O(VE)); Prim's lazy heap with stale entries not skipped.

## Related
- [[greedy-algorithms]], [[union-find]], [[heaps-and-priority-queues]], [[graph-search]],
  [[shortest-paths]], [[k-means-clustering]] (hierarchical alternatives), [[np-completeness-and-reductions]].

## Sources
Erickson ch. 7; DPV 5.1; CLRS ch. 21; K&T 4.5–4.7; Sedgewick 4.3.

---
title: Network flow — max-flow/min-cut, augmenting paths, and reductions to flow
type: concept
section: "3.2"
level: 400
tags: [network-flow, max-flow, min-cut, ford-fulkerson, augmenting-paths, residual-graph, edmonds-karp, dinic, push-relabel, bipartite-matching, disjoint-paths, min-cost-flow, image-segmentation, project-selection, baseball-elimination, lp-duality]
sources: [erickson-algorithms, kleinberg-tardos-skiena, clrs, dpv-algorithms]
summary: In a network with capacities, the maximum s–t flow equals the minimum s–t cut (Ford–Fulkerson: augment along residual paths until none exists; the reachable set in the final residual graph is a min cut); Edmonds–Karp (shortest augmenting paths, O(VE²)), Dinic (blocking flows, O(V²E)), push–relabel and modern solvers make it practical, and the power is in reductions — bipartite matching, edge/vertex-disjoint paths, assignment, survey design, image segmentation, project selection, baseball elimination, circulation with demands and lower bounds, min-cost flow.
---
# Network flow

**In one sentence.** Max flow = min cut, computed by repeatedly pushing flow along paths in the
residual graph — and an astonishing number of problems are secretly this one.

## Definitions
Flow network: directed graph, capacities c(e) ≥ 0, source s, sink t. A flow f satisfies capacity
(0 ≤ f(e) ≤ c(e)) and conservation (in = out at every vertex except s, t); value |f| = net out of s.
An s–t **cut** (S, T) has capacity Σ c(e) over edges S→T. Weak duality: any flow ≤ any cut.

## Ford–Fulkerson and the max-flow min-cut theorem
**Residual graph** G_f: forward edges with c − f, backward edges with f (undo). While an s→t path
exists in G_f, augment by its bottleneck. When none exists, let S = vertices reachable from s in
G_f: every S→T edge is saturated and every T→S edge empty, so |f| = cap(S, T) — hence **max flow
= min cut**, and the algorithm's terminal residual graph *exhibits* the min cut. Integer capacities
⇒ integral max flow (integrality theorem — the reason matching reductions work). Plain FF can take
|f*| iterations (or fail to terminate on irrationals); **Edmonds–Karp** (BFS shortest augmenting
path) needs O(VE) augmentations → O(VE²); **Dinic** (level graph + blocking flows) O(V²E), O(E√V)
on unit networks; **push–relabel** O(V²E) or O(V³); Orlin O(VE). Practical solvers: Boykov–
Kolmogorov (vision), HIPR.

## Reductions (K&T ch. 7, Erickson ch. 11)
| Problem | Construction |
|---|---|
| Maximum bipartite matching | s→L, R→t, L→R unit capacities; max flow = matching size; Hall's theorem from min cut; Hopcroft–Karp O(E√V) |
| Edge-disjoint paths | unit capacities; Menger's theorem = max flow min cut |
| Vertex-disjoint paths / vertex capacities | split each vertex into in→out with capacity 1 |
| Assignment / scheduling with capacities | multi-source, multi-sink via super source/sink |
| Circulation with demands and lower bounds | subtract lower bounds, add demand edges, check saturation |
| Project selection (profit vs prerequisites) | min cut separates chosen projects from skipped; max profit = total positive − min cut |
| Image segmentation (foreground/background) | pixel nodes, likelihood edges to s/t, separation penalties between neighbours; min cut |
| Baseball elimination | game nodes → team nodes, capacity bounds; a team is eliminated iff max flow < total remaining games |
| Min-cost flow / min-cost matching | successive shortest augmenting paths with costs; Hungarian algorithm |
Flow is a special LP: max-flow/min-cut is LP duality ([[linear-programming-and-duality]]).

## Pitfalls
- Forgetting backward residual edges (no way to undo a bad early path → wrong answer).
- DFS augmenting paths with large capacities (exponential steps); use BFS/Dinic.
- Directed vs undirected edges (undirected = two opposite arcs); vertex capacities need splitting.
- Modeling errors dominate: verify the cut interpretation on a 3-node example.

## Related
- [[linear-programming-and-duality]], [[graph-search]], [[greedy-algorithms]], [[np-completeness-and-reductions]]
  (what happens when the reduction *isn't* to flow), [[stable-matching]] (a different matching).

## Sources
Erickson ch. 10–11; K&T ch. 7; CLRS ch. 24; DPV 7.2–7.3.

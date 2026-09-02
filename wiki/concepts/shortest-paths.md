---
title: Shortest paths — relaxation, Dijkstra, Bellman–Ford, DAGs, A*, and all-pairs
type: concept
section: "3.2"
level: 300
tags: [shortest-paths, relaxation, dijkstra, bellman-ford, negative-edges, negative-cycles, dag-shortest-paths, a-star, heuristics, floyd-warshall, johnson, all-pairs, priority-queue, triangle-inequality]
sources: [erickson-algorithms, dpv-algorithms, clrs, roughgarden-algorithms-illuminated, sedgewick-algorithms-4e]
summary: Every single-source algorithm relaxes edges — if dist[u] + w(u,v) < dist[v], improve dist[v] and set pred[v] — and they differ only in the order: Dijkstra (non-negative weights, closest tentative vertex first, O((V+E) log V) with a heap), Bellman–Ford (any weights, V−1 rounds over all edges, detects negative cycles, O(VE)), DAG shortest paths in topological order (O(V+E), works with negative edges and gives longest paths), A* (Dijkstra with an admissible heuristic), and all-pairs via Floyd–Warshall (O(V³)) or Johnson (reweight then V Dijkstras).
---
# Shortest paths

**In one sentence.** Tentative distances plus **relaxation** is the whole story; each algorithm is
a schedule for which edges to relax when, and the schedule is dictated by what you can assume
about the weights.

## Relaxation and Ford's generic algorithm (Erickson ch. 8)
`dist[s] = 0, dist[v] = ∞; while some edge u→v is tense (dist[u] + w(u,v) < dist[v]): relax it`.
Invariant: dist[v] is the length of *some* walk s⇝v; when no edge is tense, dist[v] is the true
shortest distance (if no negative cycle is reachable) and `pred` forms a shortest-path tree.
Sub-path optimality (prefixes of shortest paths are shortest) is the optimal substructure that
makes this a [[dynamic-programming]].

## The algorithms
| Algorithm | Assumes | Order of relaxation | Time |
|---|---|---|---|
| BFS | unit weights | queue | O(V + E) ([[graph-search]]) |
| **DAG shortest paths** | acyclic | topological order, each vertex once | O(V + E); handles negative edges; negate for longest path / critical path |
| **Dijkstra** | w ≥ 0 | vertex with smallest dist first (priority queue), each vertex finalized once | O((V + E) log V) binary heap; O(E + V log V) Fibonacci; O(V²) dense array version |
| **Bellman–Ford** | any weights, no negative cycle reachable | V−1 passes over all edges (pass i fixes paths with ≤ i edges); a V-th improvement ⇒ negative cycle | O(VE); SPFA queue variant in practice |
| A* | w ≥ 0 + heuristic h(v) ≤ true distance (admissible; consistent for reuse) | smallest dist + h first | Dijkstra's bound, far fewer expansions ([[search-algorithms-ai]]) |
| **Floyd–Warshall** (all pairs) | no negative cycles | dᵏ(u,v) = min(dᵏ⁻¹(u,v), dᵏ⁻¹(u,k) + dᵏ⁻¹(k,v)) | O(V³), O(V²) space; detects negative cycles on the diagonal |
| **Johnson** (all pairs, sparse) | any weights | Bellman–Ford from a new source to get potentials h; reweight w' = w + h(u) − h(v) ≥ 0; V × Dijkstra | O(VE + V² log V) |
Why Dijkstra fails with negative edges: it finalizes a vertex assuming no later path can be
shorter, which a negative edge violates (adding a constant to all edges does *not* fix it — it
penalizes long paths). Bidirectional Dijkstra, contraction hierarchies and ALT landmarks make
continent-scale road routing sub-millisecond.

## Implementation notes
Dijkstra with a lazy binary heap: push (dist, v) on every improvement, skip stale pops — simpler
than decrease-key ([[heaps-and-priority-queues]]). Store `pred` for path reconstruction. Use
integers or be careful with float ties. For unit/small integer weights, Dial's buckets.

## Pitfalls
- Running Dijkstra with negative weights (silent wrong answers).
- Not checking for negative cycles in Bellman–Ford; assuming "shortest path" is defined when one
  exists (it isn't with a reachable negative cycle).
- O(V²) Floyd–Warshall memory on large graphs; forgetting that all-pairs on sparse graphs is
  cheaper via Johnson.

## Related
- [[graph-search]], [[dynamic-programming]], [[greedy-algorithms]], [[heaps-and-priority-queues]],
  [[minimum-spanning-trees]] (Prim looks like Dijkstra but optimizes a different quantity),
  [[linear-programming-and-duality]] (shortest paths as an LP; potentials are duals), [[search-algorithms-ai]].

## Sources
Erickson ch. 8–9; DPV ch. 4; CLRS ch. 22–23; Roughgarden part 2; Sedgewick 4.4.

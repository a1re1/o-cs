---
title: Graph search — BFS, DFS, topological sort, strongly connected components
type: concept
section: "3.2"
level: 300
tags: [graph-search, bfs, dfs, topological-sort, strongly-connected-components, kosaraju, tarjan, cycle-detection, previsit-postvisit, edge-classification, whatever-first-search, reachability, bipartite]
sources: [erickson-algorithms, dpv-algorithms, clrs, roughgarden-algorithms-illuminated, sedgewick-algorithms-4e]
summary: "Whatever-first search" with a bag visits everything reachable in O(V + E); a stack gives DFS with pre/post timestamps that classify edges (tree, back, forward, cross), detect cycles (a back edge), linearize DAGs (reverse post-order = topological sort) and find strongly connected components (Kosaraju: DFS on the reverse graph, then DFS in decreasing post order; Tarjan: one pass with low-links); a queue gives BFS with distance layers and unweighted shortest paths; and memoized recursion is DFS on the subproblem graph.
---
# Graph search

**In one sentence.** Put the start in a bag; repeatedly take a vertex out, mark it, and put its
unmarked neighbours in — the bag's discipline (stack, queue, priority queue) decides what you learn.

## Whatever-first search (Erickson ch. 5)
```
WFS(s): put s in bag; while bag not empty: v ← take; if v unmarked: mark v; for each edge v→w: put w
```
Each vertex is marked once and each edge examined once: O(V + E) with adjacency lists
([[graph-representations]]). Parent pointers give a spanning tree of the reachable set. Stack →
DFS; queue → BFS; priority queue by distance → Dijkstra ([[shortest-paths]]); priority by edge
weight → Prim ([[minimum-spanning-trees]]). Repeat from every unmarked vertex to get components.

## DFS and its timestamps (DPV ch. 3, CLRS 20.3)
Recursive DFS records `pre[v]` on entry and `post[v]` on exit. Intervals are nested or disjoint
(never crossing). Edge u→v classification: **tree/forward** (pre[u] < pre[v] < post[v] < post[u]),
**back** (v is an ancestor still open: pre[v] < pre[u] < post[u] < post[v]) — a back edge exists
iff the graph has a **cycle**, **cross** (post[v] < pre[u]). In undirected graphs only tree and back
edges occur.
- **Topological sort**: a DAG's vertices in *decreasing post order* are linearized (every edge
  u→v has post[u] > post[v]) — [[dags-and-partial-orders]]; equivalently Kahn's algorithm (repeatedly
  remove in-degree-0 vertices — detects cycles if vertices remain).
- **Strongly connected components**: the sink SCC contains the vertex with the *lowest* post
  number; the vertex with the *highest* post number in the reverse graph lies in a source SCC.
  **Kosaraju**: DFS on Gᴿ, then DFS on G in decreasing Gᴿ-post order; each tree is an SCC.
  **Tarjan**: single DFS with `low[v]` = smallest pre reachable via tree edges and one back
  edge; pop the stack when low[v] = pre[v]. Both O(V + E); the component graph is a DAG (2-SAT
  in linear time via SCCs on the implication graph).
- Applications: reachability, articulation points and bridges (low-link), bipartiteness by
  2-colouring (an odd cycle iff a same-colour edge), maze solving, garbage collection marking
  ([[garbage-collection]]), dependency resolution ([[build-systems-and-make]]).

## BFS
Layers L₀ = {s}, L₁ = neighbours, …: `dist[v]` is the number of edges on a shortest path (unit
weights); `edgeTo` reconstructs the path. Mark on *enqueue*. Bidirectional BFS for point-to-point;
0-1 BFS with a deque for weights in {0, 1}; iterative deepening DFS to get BFS's optimality with
DFS's memory ([[search-algorithms-ai]]).

## Memoization is DFS
The dependency graph of a recurrence is a DAG of subproblems; memoized recursion is DFS on it and
the table-filling order is its topological order — [[dynamic-programming]].

## Pitfalls
- Recursive DFS on a million-vertex path overflows the stack; use an explicit stack (and emulate
  post-order carefully — push a "finish" marker).
- Marking on dequeue in BFS (wrong distances, duplicates in the queue).
- Forgetting to restart search from every vertex (components) or to reverse post order (topo).

## Related
- [[graph-representations]], [[dags-and-partial-orders]], [[shortest-paths]], [[minimum-spanning-trees]],
  [[dynamic-programming]], [[graph-theory-basics]], [[search-algorithms-ai]].

## Sources
Erickson ch. 5–6; DPV ch. 3–4; CLRS ch. 20; Roughgarden part 2; Sedgewick 4.1–4.2.

---
title: Graph representations — adjacency lists, adjacency matrices, edge lists, and traversal basics
type: concept
section: "3.1"
level: 200
tags: [graphs, adjacency-list, adjacency-matrix, edge-list, csr, sparse-graphs, dense-graphs, directed, undirected, weighted, dfs, bfs, connected-components, degree]
sources: [sedgewick-algorithms-4e, open-data-structures-morin, berkeley-cs61b]
summary: Choose the representation by density and operations — adjacency lists (V + E space, O(deg) neighbor iteration; the default), adjacency matrices (V² space, O(1) edge test, good for dense graphs and algebraic methods), edge lists (for Kruskal and streaming), and compressed sparse row for performance; DFS (stack/recursion) and BFS (queue) visit every vertex and edge once, O(V + E), and are the base for components, reachability, and shortest paths in unweighted graphs.
---
# Graph representations and traversal basics

**In one sentence.** A graph is vertices plus edges ([[graph-theory-basics]]); how you store the
edges decides which operations are cheap, and DFS/BFS are the two ways to walk it.

## Representations (V vertices, E edges)
| | Space | edge (u,v)? | iterate neighbors of u | add edge | Best for |
|---|---|---|---|---|---|
| **Adjacency list** (`Vec<Vec<usize>>`, `Map<V, Set<V>>`) | O(V + E) | O(deg u) (O(1) with sets) | O(deg u) | O(1) | sparse graphs — nearly everything |
| Adjacency matrix (V×V bools/weights) | O(V²) | O(1) | O(V) | O(1) | dense graphs, Floyd–Warshall, spectral methods ([[eigenvalues-and-eigenvectors]]) |
| Edge list (`[(u, v, w)]`) | O(E) | O(E) | O(E) | O(1) | Kruskal, Bellman–Ford, storage/streaming |
| CSR (offsets + packed neighbors) | O(V + E) | O(deg) | O(deg), contiguous | rebuild | static high-performance graphs ([[caches-and-memory-hierarchy]]) |
Undirected: store each edge twice (or once with u < v); directed: out-lists (and in-lists if needed);
weighted: store (v, w) pairs; multigraphs/self-loops need care. Implicit graphs (states of a puzzle,
grid cells) generate neighbors on the fly — don't materialize them.

## Traversals — O(V + E) with a visited set
- **DFS**: recursion or explicit stack; pre/post-order timestamps; gives connected components,
  cycle detection, topological order (reverse post-order on DAGs — [[dags-and-partial-orders]]),
  strongly connected components (Kosaraju/Tarjan), articulation points/bridges, and a spanning
  tree. Recursion depth can hit V — use an explicit stack for big graphs.
- **BFS**: queue; visits by distance layers; shortest paths in unweighted graphs (`distTo`,
  `edgeTo` arrays give the path); bipartiteness check (2-coloring). See [[graph-search]] for the
  algorithms built on these.
- Track `marked[]`, `edgeTo[]` (parent pointers → path reconstruction), and `distTo[]`.

## Choosing
Sparse (E ≈ V, social/road/web graphs) → lists. Dense (E ≈ V²) or need constant-time edge tests →
matrix. Many edge insertions and deletions → hash-set adjacency. Read-mostly at scale → CSR.

## Pitfalls
- Forgetting the visited set (infinite loops on cycles); marking on dequeue instead of enqueue in
  BFS (duplicates, wrong distances).
- Directed vs undirected mismatch (adding both directions or only one).
- Iterating a mutable adjacency set while inserting.

## Related
- [[graph-theory-basics]], [[graph-search]], [[dags-and-partial-orders]], [[union-find]],
  [[shortest-paths]], [[minimum-spanning-trees]], [[matrices-and-linear-maps]].

## Sources
Sedgewick 4.1–4.2; ODS ch. 12; CS61B weeks 9–10.

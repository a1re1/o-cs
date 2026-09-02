---
title: Graph theory basics (degrees, paths, bipartite matching, coloring, trees, planarity)
type: concept
section: "1.1"
level: 200
tags: [graph-theory, degrees, handshake-lemma, paths, connectivity, bipartite, matching, halls-theorem, coloring, trees, spanning-trees, planar-graphs, euler-formula, isomorphism]
sources: [mcs-lehman-leighton-meyer, levin-dmoi]
summary: The definitions and small theorems every algorithm course assumes — handshake lemma, walks vs paths, connectivity and cut edges, bipartite graphs and Hall's matching condition, chromatic number bounds, trees (n−1 edges, unique paths), spanning trees, and Euler's planar formula.
---
# Graph theory basics

**In one sentence.** A simple graph is a set of vertices and a set of 2-element edges; nearly every
structural fact below is a counting argument over edges or an induction over vertices.

## Degrees and walks
- **Handshake lemma**: Σ deg(v) = 2|E|; hence the number of odd-degree vertices is even.
- **Walk** (vertices may repeat) vs **path** (no repeats) vs **cycle**. Any walk from u to v contains a
  path from u to v (shortcut the loops). Shortest walks are paths.
- **Connected components** partition V; a graph with n vertices and fewer than n−1 edges is disconnected;
  an edge whose removal disconnects is a **cut edge** (bridge), and an edge is a bridge iff it is on no cycle.
- Adjacency matrix A: (A^k)_{uv} counts length-k walks; adjacency lists are the practical representation.
- **Isomorphism**: relabeling; invariants (degree sequence, cycle counts) can prove non-isomorphism, but
  no known polynomial algorithm decides isomorphism in general (quasi-polynomial, Babai 2015).

## Bipartite graphs and matching
- Bipartite ⇔ 2-colorable ⇔ no odd cycle (BFS layers give the coloring or find the odd cycle).
- A **matching** is a set of disjoint edges; **Hall's theorem**: a bipartite graph with sides L, R has a
  matching saturating L iff every S ⊆ L has |N(S)| ≥ |S| ("no bottleneck"). Corollary: every
  d-regular bipartite graph has a perfect matching. Algorithms: augmenting paths, Hopcroft–Karp
  O(E√V), or max-flow (§3.2). Preference-based matching is [[stable-matching]].

## Coloring
- Chromatic number χ(G): bipartite = 2, odd cycle = 3, K_n = n. Greedy coloring uses ≤ Δ + 1 colors
  (Δ = max degree); Brooks: ≤ Δ unless complete or odd cycle. Deciding 3-colorability is NP-complete.
  Applications: register allocation (§4.3), exam/scheduling conflicts, frequency assignment.

## Trees
Equivalent definitions: connected & acyclic; connected with n−1 edges; acyclic with n−1 edges; unique
path between every pair; connected but every edge is a cut edge. Every tree with ≥ 2 vertices has ≥ 2
leaves (used in inductions: remove a leaf). Every connected graph has a **spanning tree**; minimum
spanning trees (Kruskal/Prim) are §3.2.

## Planarity
Euler's formula for a connected planar embedding: V − E + F = 2. Consequences: a planar graph has
E ≤ 3V − 6 (and ≤ 2V − 4 if triangle-free), so K₅ and K₃,₃ are not planar; every planar graph has a
vertex of degree ≤ 5 and is 6-colorable by induction (5 with more work; 4 by computer).
Kuratowski: planar ⇔ no subdivision of K₅ or K₃,₃.

## Pitfalls
- "Path" is used loosely in many texts to mean walk; check whether repeats are allowed before applying a lemma.
- Hall's condition must be checked for *all* subsets, not just singletons.
- Handshake lemma counts edge *ends*; self-loops count twice.

## Related
- [[dags-and-partial-orders]] — directed graphs, reachability, topological order.
- [[stable-matching]] — Gale–Shapley.
- [[induction]] — most tree/planarity proofs remove a leaf or an edge.
- [[graph-search]] — BFS/DFS make these definitions algorithmic (§3.1).

## Sources
MCS ch. 11 (simple graphs), 12 (planar graphs); Levin ch. 4.

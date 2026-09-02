---
title: Algorithms Illuminated (Roughgarden) with Stanford CS161 and CMU 15-451
type: source
section: "3.2"
level: 300
tags: [roughgarden, algorithms, divide-and-conquer, master-method, quicksort, randomized, graph-search, dijkstra, heaps, hash-tables, bloom-filters, greedy, dynamic-programming, np-hard, local-search]
sources: []
authors: [Tim Roughgarden]
year: 2017
institution: Stanford / Columbia
url: https://www.algorithmsilluminated.org/
license: proprietary (videos free)
format: book
summary: Four short volumes with free lecture videos — 1 The Basics (asymptotics, divide and conquer, master method, quicksort, linear-time selection), 2 Graph Algorithms and Data Structures (BFS/DFS, topological sort, SCC, Dijkstra, heaps, search trees, hash tables, Bloom filters), 3 Greedy Algorithms and Dynamic Programming (scheduling, Huffman, MST, knapsack, sequence alignment, optimal BSTs, Bellman–Ford, Floyd–Warshall), 4 Algorithms for NP-Hard Problems (what NP-hardness means, compromising on correctness or speed, mixed-integer programming and SAT solvers, local search, P vs NP) — CS161 and 15-451 cover the same arc with problem sets.
---
# Algorithms Illuminated (Roughgarden)

## What it is
Part 1: "can we do better?" as the algorithm designer's mantra; Karatsuba; mergesort; asymptotics;
divide and conquer (inversions, Strassen, closest pair); the master method (proof via recursion
tree: three cases by comparing a with b^d); quicksort (randomized pivots, expected n log n by
counting comparisons with indicator variables); linear-time selection (RSelect, DSelect median of
medians); sorting lower bound. Part 2: graph search (BFS layers, connected components, DFS,
topological ordering, Kosaraju's SCC); Dijkstra and why it fails with negative edges; heaps
(with Dijkstra in m log n); search trees; hash tables (birthday paradox, chaining vs probing,
pathological data sets and universal hashing); Bloom filters. Part 3: greedy (scheduling with
exchange arguments, Huffman, MST — Prim, Kruskal, union-find; clustering); DP principles
(weighted independent set on paths, knapsack, sequence alignment, optimal BSTs, Bellman–Ford,
Floyd–Warshall). Part 4: NP-hard problems — the three strategies (special cases, fast heuristics,
exact but exponential), MST-based TSP heuristics, DP for TSP (Held–Karp), local search, MIP/SAT
solvers as workhorses, the meaning of P ≠ NP.
**CS161** (Stanford): same arc with hashing, RSA-free; **15-451** (CMU): adds amortized analysis,
splay trees, linear programming, streaming, online algorithms, and the "hidden" advanced topics.

## What it adds
The most watchable lectures for [[divide-and-conquer]], [[sorting]], [[graph-search]],
[[randomized-algorithms]] (probabilistic analysis of quicksort), and a practical view of
[[np-completeness-and-reductions]].

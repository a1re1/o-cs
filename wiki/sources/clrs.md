---
title: Introduction to Algorithms (Cormen, Leiserson, Rivest, Stein — CLRS, 4th ed.) with MIT 6.046J
type: source
section: "3.2"
level: 300
tags: [clrs, algorithms, sorting, order-statistics, hashing, red-black-trees, dynamic-programming, greedy, amortized-analysis, graphs, mst, shortest-paths, max-flow, string-matching, np-completeness, approximation, randomized, number-theoretic, fft, linear-programming]
sources: []
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
institution: MIT
url: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
license: proprietary
format: book
summary: The encyclopedic reference — foundations (growth of functions, divide-and-conquer with the master theorem, probabilistic analysis), sorting and order statistics (heapsort, quicksort, linear-time sorts, selection), data structures (hash tables, BSTs, red-black trees, augmenting), advanced design (dynamic programming, greedy, amortized analysis), advanced structures (B-trees, Fibonacci heaps, van Emde Boas, disjoint sets), graphs (BFS/DFS, MST, single-source and all-pairs shortest paths, max flow, matchings), selected topics (parallel, online, matrix ops, LP, polynomials/FFT, number theory, string matching, computational geometry, NP-completeness, approximation) — the text behind MIT 6.006/6.046.
---
# Introduction to Algorithms (CLRS)

## What it is
Part I foundations (1–5): insertion sort and loop invariants, asymptotic notation, divide-and-
conquer (substitution, recursion trees, **master theorem**), probabilistic analysis and randomized
algorithms (hiring problem, indicator variables). II sorting (6–9): heapsort, quicksort (randomized;
expected O(n lg n)), lower bound Ω(n lg n) for comparison sorts, counting/radix/bucket sort,
selection in expected and worst-case linear time. III data structures (10–13): stacks/queues/lists,
hash tables (chaining, open addressing, universal and perfect hashing), BSTs, red-black trees.
IV design and analysis (14–16): dynamic programming (rod cutting, matrix-chain, LCS, optimal BST;
optimal substructure + overlapping subproblems), greedy (activity selection, Huffman, matroids),
amortized analysis (aggregate, accounting, potential; dynamic tables). V advanced structures
(17–19): augmenting (order statistics, interval trees), B-trees, disjoint sets. VI graphs (20–25):
representations, BFS/DFS/topological sort/SCC, MST (Kruskal, Prim), single-source shortest paths
(Bellman–Ford, DAG, Dijkstra, difference constraints), all-pairs (Floyd–Warshall, Johnson), max flow
(Ford–Fulkerson, Edmonds–Karp, push-relabel), matchings. VII selected (26–35): parallel algorithms,
online algorithms, matrix operations, linear programming, polynomials and FFT, number-theoretic
algorithms (RSA), string matching (Rabin–Karp, automata, KMP, suffix arrays), machine learning
basics, NP-completeness, approximation algorithms. **6.046J** (design and analysis): divide and
conquer, DP, greedy, amortization, randomization, network flow, linear programming, complexity,
distributed/parallel, cryptography — problem sets public on OCW.

## What it adds
Proof-level depth for every §3.1–3.2 page; the standard vocabulary (loop invariants, master
theorem cases, optimal substructure) that other sources assume.

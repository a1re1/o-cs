---
title: Algorithms (Jeff Erickson, 2019)
type: source
section: "3.2"
level: 300
tags: [algorithms, recursion, reductions, backtracking, dynamic-programming, greedy, graphs, dfs, shortest-paths, mst, max-flow, np-hardness, exchange-argument, recursion-fairy]
sources: []
authors: [Jeff Erickson]
year: 2019
institution: University of Illinois
url: https://jeffe.cs.illinois.edu/teaching/algorithms/
license: CC-BY
format: pdf
summary: A free, opinionated algorithms text built on one idea — reduction, and recursion as reduction to smaller instances of the same problem ("the Recursion Fairy is the induction hypothesis") — with chapters on recursion, backtracking, dynamic programming ("smart recursion, not filling tables": specify the subproblem in English, write the recurrence, then memoize bottom-up), greedy ("greed is stupid" until proved by an exchange argument), basic graph algorithms, DFS, MST, shortest paths, all-pairs, max-flow/min-cut, flow applications, and NP-hardness — plus extensive exercises and appendices on solving recurrences.
---
# Algorithms (Erickson)

## What it is
Ch. 0 introduction (what is an algorithm; Huntington–Hill and peasant multiplication as running
examples); 1 recursion — **reductions** (solve X with a black box for Y; correctness never depends
on how Y works), simplify and delegate (the Recursion Fairy), Tower of Hanoi, mergesort, quicksort,
the pattern, recursion trees, linear-time selection, fast multiplication (Karatsuba), exponentiation;
2 backtracking (n-queens, game trees, subset sum, text segmentation, longest increasing
subsequence, optimal binary search trees — "the recursive structure is the whole game"); 3
**dynamic programming** — Fibonacci, memoization, the pattern (two stages: formulate recursively
with a specification and a solution; then identify subproblems, choose a memo structure, identify
dependencies, pick an evaluation order — a linear extension of the dependency partial order —
analyze, write it down), "greed is stupid", LIS, edit distance, subset sum, optimal BSTs, DP on
trees; 4 **greedy** — storing files on tape, scheduling classes, the general pattern (inductive
exchange argument: assume a different optimum, find the first difference, exchange without loss),
Huffman codes, stable matching; 5 basic graph algorithms (representations, whatever-first search,
reductions to graph problems); 6 depth-first search (preorder/postorder, DAGs, topological sort,
memoization = DFS, strong components); 7 minimum spanning trees (Borůvka, Jarník/Prim, Kruskal);
8 shortest paths (relaxation, Ford's generic algorithm, Dijkstra, Bellman–Ford, DAGs); 9 all-pairs
(Johnson, Floyd–Warshall); 10 maximum flows and minimum cuts (Ford–Fulkerson, augmenting paths,
Edmonds–Karp, Dinic); 11 flow applications (bipartite matching, disjoint paths, assignment,
baseball elimination, project selection); 12 NP-hardness (P vs NP, reductions, 3SAT, vertex cover,
clique, independent set, Hamiltonian cycle, subset sum, choosing the right reduction, a hardness
"recipe").

## Notable claims
- "Dynamic programming is not about filling in tables. It's about smart recursion!"
- Greedy algorithms "almost never work"; when they do, the proof is always an exchange argument.
- Memoization is DFS on the dependency graph; topological order is what the table loop computes.

## What it adds
The reference for [[dynamic-programming]], [[greedy-algorithms]], [[divide-and-conquer]],
[[graph-search]], [[np-completeness-and-reductions]]; CLRS ([[clrs]]) for breadth and proofs,
[[dpv-algorithms]] for brevity.

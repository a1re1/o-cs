---
title: Algorithms, 4th ed. (Sedgewick & Wayne) / Princeton COS 226 / Coursera Algorithms I & II
type: source
section: "3.1"
level: 200
tags: [algorithms, data-structures, union-find, sorting, priority-queues, symbol-tables, bst, red-black-trees, hash-tables, graphs, mst, shortest-paths, strings, tries, java]
sources: []
authors: [Robert Sedgewick, Kevin Wayne]
year: 2011
institution: Princeton
url: https://algs4.cs.princeton.edu/
license: proprietary-open-site
format: html
summary: The booksite carries the full text summaries, Java code, data, and lecture slides — fundamentals (analysis, union-find case study), sorting (elementary, mergesort, quicksort, priority queues/heapsort), searching (symbol tables, BSTs, 2-3 trees and left-leaning red-black BSTs, hash tables), graphs (undirected/directed, MST, shortest paths), strings (sorts, tries, substring search, regex, compression), and context — with a consistent "API, implementation, cost model, proposition" method.
---
# Algorithms, 4th edition (Sedgewick & Wayne)

## What it is
Ch. 1 fundamentals — programming model, data abstraction, bags/queues/stacks (resizing arrays and
linked lists), analysis of algorithms (tilde notation, doubling test), **case study: union-find**
(quick-find, quick-union, weighted quick-union, path compression; cost model = array accesses;
depth ≤ lg n for weighted). Ch. 2 sorting — insertion/selection/shellsort, mergesort (top-down,
bottom-up, n lg n optimal for compares), quicksort (3-way partitioning for duplicates), priority
queues (binary heap, heapsort). Ch. 3 searching — symbol-table API, sequential/binary search, BSTs
(Hibbard deletion), **balanced search trees** (2-3 trees; red-black BSTs as an encoding of 2-3
trees with left-leaning red links; rotations, color flips; height ≤ 2 lg n), **hash tables** (hash
functions: modular hashing, string hashing with R=31, `hashCode` consistent with `equals`;
uniform hashing assumption; separate chaining; linear probing; resizing), applications (sets,
dictionary clients, indexing, sparse vectors). Ch. 4 graphs — undirected graphs (adjacency lists,
DFS, BFS, connected components), digraphs (topological sort, strong components), MST (Prim, Kruskal
with union-find), shortest paths (Dijkstra, edge-weighted DAGs, Bellman-Ford). Ch. 5 strings —
LSD/MSD radix sorts, tries and TSTs, substring search (KMP, Boyer-Moore, Rabin-Karp), regular
expressions (NFA simulation), data compression (Huffman, LZW). Ch. 6 context (B-trees, suffix
arrays, max-flow, reductions, intractability).

## Key ideas → pages
- Union-find and its cost model — [[union-find]].
- Resizing arrays and linked lists as the two ways to implement collections — [[arrays-and-linked-lists]].
- Binary heaps — [[heaps-and-priority-queues]]; BSTs — [[binary-search-trees]]; 2-3/LLRB —
  [[balanced-search-trees]]; hashing — [[hash-tables]]; tries — [[tries]].
- Graph representation and traversal — [[graph-representations]].

## What it adds
The most readable code-first treatment; [[clrs]] gives the proofs, [[open-data-structures-morin]]
the free text.

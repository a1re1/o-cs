---
title: Competitive Programmer's Handbook (Laaksonen) with Competitive Programming 4 (Halim) and the USACO Guide
type: source
section: "3.4"
level: 300
tags: [competitive-programming, cph, cses, codeforces, atcoder, usaco, implementation, complete-search, bit-manipulation, segment-trees, fenwick, range-queries, sqrt-decomposition, number-theory, combinatorics, geometry, sweep-line, game-theory, string-hashing]
sources: []
authors: [Antti Laaksonen, Steven Halim, Felix Halim, Suhendry Effendy]
year: 2018
institution: University of Helsinki / NUS
url: https://cses.fi/book/book.pdf
license: free-pdf
format: pdf
summary: The free CPH is the compact contest curriculum — Part I basic techniques (C++ idioms, time complexity, sorting and binary search, STL data structures, complete search and meet-in-the-middle, greedy, DP, amortized two-pointer/sliding-window tricks, range queries with prefix sums/BIT/segment trees, bit manipulation), Part II graph algorithms (traversal, shortest paths, tree algorithms, spanning trees, directed graphs, strong connectivity, tree queries, paths and circuits, flows and cuts), Part III advanced topics (number theory, combinatorics, matrices, probability, game theory, string algorithms, square root algorithms, segment trees revisited, geometry, sweep line) — with the CSES problem set; CP4 and the USACO Guide add breadth and graded practice.
---
# Competitive Programmer's Handbook

## What it is
**I Basic techniques**: 1 introduction (fast I/O, `long long`, shortening code, math cheat-sheet);
2 time complexity (rules; which complexity fits which n: n ≤ 10 → n!, ≤ 20 → 2ⁿ, ≤ 500 → n³, ≤ 5000
→ n², ≤ 10⁶ → n log n, larger → n or log n; maximum subarray sum three ways); 3 sorting and
binary search (also "binary search on the answer"); 4 STL structures (vector, set/multiset,
map, priority_queue, policy-based trees; "comparison to sorting"); 5 complete search (subsets by
bitmask, permutations, backtracking with pruning — queens; **meet in the middle**); 6 greedy; 7
DP (coin change, LIS, grid paths, knapsack, edit distance, tilings); 8 amortized (two pointers,
nearest smaller elements with a stack, sliding window minimum with a deque); 9 range queries
(prefix sums, sparse table for static min, **binary indexed tree**, **segment tree** with lazy
updates); 10 bit manipulation (representing sets as bitmasks, `__builtin_popcount`, subset
enumeration, bitmask DP — Hamiltonian paths, counting subsets/SOS DP). **II Graph algorithms**: 11
basics, 12 traversal, 13 shortest paths, 14 tree algorithms (diameter, all longest paths, binary
lifting), 15 spanning trees, 16 directed graphs (topological sort, DP on DAGs, successor graphs,
cycle detection), 17 strong connectivity (Kosaraju, 2-SAT), 18 tree queries (LCA, Euler tour,
offline), 19 paths and circuits (Eulerian, Hamiltonian, De Bruijn, knight's tour), 20 flows and
cuts (Ford–Fulkerson, disjoint paths, maximum matchings, Hall, König, path covers). **III
Advanced**: 21 number theory (sieve, Euclid, modular exponentiation/inverse, CRT, Diophantine),
22 combinatorics (binomials, Catalan, inclusion–exclusion, Burnside, Cayley), 23 matrices (fast
linear recurrences, path counting), 24 probability, 25 game theory (nim, Sprague–Grundy), 26
string algorithms (trie, polynomial hashing, Z-algorithm), 27 square root algorithms (block
decomposition, Mo's algorithm, batch processing), 28 segment trees revisited (lazy, dynamic,
persistent, 2D), 29 geometry (complex numbers, cross product, point location, area, distances),
30 sweep line (intersections, closest pair, convex hull).

## What it adds
A checklist of the *implementation* toolkit that textbooks skip: [[range-queries-segment-trees-fenwick]],
[[competitive-programming-techniques]], [[number-theory-algorithms]], [[computational-geometry]];
the complexity-vs-n table is the single most useful contest heuristic.

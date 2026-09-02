---
title: Algorithm Design (Kleinberg & Tardos) and The Algorithm Design Manual (Skiena)
type: source
section: "3.2"
level: 300
tags: [algorithm-design, stable-matching, greedy, divide-and-conquer, dynamic-programming, network-flow, np-completeness, pspace, approximation, local-search, randomized, war-stories, catalog]
sources: []
authors: [Jon Kleinberg, Éva Tardos, Steven Skiena]
year: 2006
institution: Cornell / Stony Brook
url: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/
license: proprietary (slides free)
format: book
summary: Kleinberg & Tardos teach algorithm design as modeling — stable matching first, then greedy (interval scheduling, shortest paths, MST, clustering, Huffman), divide-and-conquer (counting inversions, closest pair, integer multiplication, FFT), dynamic programming (weighted interval scheduling, segmented least squares, knapsack, sequence alignment, Bellman–Ford), network flow and its many applications, NP-completeness, PSPACE, extending tractability, approximation, local search, randomized algorithms — with beautiful problem sets; Skiena's Manual adds war stories, a "how to design an algorithm" checklist, and a catalog of 75 problems with pointers to implementations.
---
# Algorithm Design (K&T) / The Algorithm Design Manual (Skiena)

## What it is
K&T: 1 stable matching (Gale–Shapley as an algorithmic template), 2 basics of analysis, 3 graphs,
4 **greedy** (interval scheduling by earliest finish; minimizing lateness by exchange argument;
Dijkstra; MST with cut/cycle properties; clustering as MST; Huffman), 5 divide and conquer
(mergesort recurrences, inversions, closest pair, integer multiplication, convolution/FFT), 6
**dynamic programming** (weighted interval scheduling — memoization vs iteration; segmented least
squares; subset sums and knapsack (pseudo-polynomial); RNA secondary structure; sequence alignment
in linear space (Hirschberg); Bellman–Ford; negative cycles), 7 **network flow** (max-flow min-cut,
choosing good augmenting paths, bipartite matching, disjoint paths, survey design, airline
scheduling, image segmentation, project selection, baseball elimination), 8 NP and computational
intractability (polynomial-time reductions, independent set/vertex cover/set cover, SAT,
sequencing problems, partitioning, graph coloring, numerical problems, co-NP), 9 PSPACE, 10
extending the limits of tractability (small vertex covers, trees, tree decompositions), 11
approximation algorithms (load balancing, center selection, set cover pricing, LP rounding,
knapsack PTAS), 12 local search (Hopfield nets, max cut, Nash equilibria), 13 randomized
algorithms (contention resolution, global min cut, expectation, randomized divide and conquer,
hashing, load balancing, packet routing, Chernoff bounds).
Skiena: Part I techniques (analysis, data structures, sorting/searching, graph traversal, weighted
graphs, combinatorial search, DP, NP-completeness, dealing with hard problems, how to design
algorithms) with **war stories**; Part II the hitchhiker's guide/catalog (data structures,
numerical, combinatorial, graph (polynomial and hard), computational geometry, set/string
problems) — each with "what are the input/output, how hard, what should I do".

## What it adds
The modeling perspective (turn a real problem into interval scheduling, flow, or alignment) for
[[greedy-algorithms]], [[dynamic-programming]], [[network-flow]], [[np-completeness-and-reductions]];
Skiena's catalog is the lookup table for "is this problem known?".

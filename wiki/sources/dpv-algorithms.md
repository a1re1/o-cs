---
title: Algorithms (Dasgupta, Papadimitriou, Vazirani) and Berkeley CS170
type: source
section: "3.2"
level: 300
tags: [dpv, algorithms, arithmetic, divide-and-conquer, fft, graphs, paths, greedy, dynamic-programming, linear-programming, np-completeness, coping-with-np, quantum]
sources: []
authors: [Sanjoy Dasgupta, Christos Papadimitriou, Umesh Vazirani]
year: 2006
institution: UC San Diego / UC Berkeley
url: https://cseweb.ucsd.edu/~dasgupta/book/
license: free-draft
format: pdf
summary: A short, elegant algorithms text (free draft) that starts from arithmetic (big-number multiplication, modular arithmetic, primality, RSA), then divide-and-conquer (multiplication, master theorem, mergesort, medians, matrix multiplication, FFT as polynomial multiplication), decompositions of graphs (DFS, DAGs, SCC), paths (BFS, Dijkstra, Bellman–Ford, DAG shortest paths), greedy (MST, Huffman, Horn formulas, set cover), dynamic programming (LIS, edit distance, knapsack, chain matrix multiplication, shortest paths, independent sets in trees), linear programming and reductions (duality, flows, matching, simplex), NP-complete problems and reductions, coping with NP-completeness (backtracking, branch-and-bound, approximation, local search), and quantum algorithms — the CS170 text.
---
# Algorithms (DPV) / CS170

## What it is
Prologue (Fibonacci, big-O); 1 algorithms with numbers (addition/multiplication/division,
modular arithmetic, primality testing (Fermat), cryptography (RSA), universal hashing); 2
divide-and-conquer (multiplication (Gauss trick), recurrence relations/master theorem, mergesort,
medians (randomized selection), matrix multiplication (Strassen), **the FFT** — polynomial
multiplication via evaluation at roots of unity, interpolation, the recursive algorithm,
butterfly network); 3 decompositions of graphs (DFS in undirected graphs, connectivity, previsit/
postvisit, DAGs and linearization, strongly connected components — the "sink SCC has the
lowest post number" trick); 4 paths in graphs (BFS, edge lengths, Dijkstra with priority queues,
negative edges (Bellman–Ford), shortest paths in DAGs); 5 greedy (MST: cut property, Kruskal with
union-find, Prim; Huffman; Horn formulas; set cover with ln n approximation); 6 dynamic programming
(shortest paths in DAGs revisited — "DP = DAG of subproblems", LIS, edit distance, knapsack with
and without repetition, chain matrix multiplication, all-pairs (Floyd–Warshall), TSP in 2ⁿ,
independent sets in trees); 7 linear programming and reductions (introduction, flows in networks
(max-flow min-cut via LP duality), bipartite matching, duality, zero-sum games, simplex, circuit
evaluation as the "hardest" P problem); 8 NP-complete problems (search problems, NP-complete
problems, the reductions — SAT→3SAT→independent set→vertex cover/clique, 3SAT→3D matching→ZOE→
subset sum, Rudrata/Hamiltonian, TSP); 9 coping with NP-completeness (intelligent exhaustive
search: backtracking and branch-and-bound; approximation algorithms: vertex cover, clustering, TSP,
knapsack; local search); 10 quantum algorithms (qubits, Fourier transform, factoring).

## Notable claims
- "Dynamic programming is solving a DAG of subproblems in topological order" — the cleanest
  unification of DP with graph search.
- FFT is divide-and-conquer on polynomial evaluation at the n-th roots of unity.

## What it adds
The short path through [[divide-and-conquer]], [[dynamic-programming]], [[graph-search]],
[[np-completeness-and-reductions]], [[fft]]; pairs with [[erickson-algorithms]] (deeper) and
[[clrs]] (broader).

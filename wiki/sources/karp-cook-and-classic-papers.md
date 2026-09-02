---
title: Classic algorithms papers — Cook (1971), Karp (1972), Dijkstra (1959), Edmonds & Karp (1972), Fredman & Tarjan (1987), Bloom (1970), Karger (1993), Indyk & Motwani (1998)
type: source
section: "3.3"
level: 500
tags: [cook-levin, karp-21-problems, dijkstra-1959, edmonds-karp, fibonacci-heaps, bloom-filter-1970, karger-min-cut, locality-sensitive-hashing, history, seminal-papers]
sources: []
authors: [Stephen Cook, Richard Karp, Edsger Dijkstra, Jack Edmonds, Michael Fredman, Robert Tarjan, Burton Bloom, David Karger, Piotr Indyk, Rajeev Motwani]
year: 1971
institution: various
url: https://dl.acm.org/doi/10.1145/800157.805047
license: various
format: pdf
summary: Eight papers that fixed the field's vocabulary — Cook's theorem that SAT is NP-complete via polynomial-time reductions; Karp's 21 NP-complete problems establishing the reduction web and the P vs NP framing; Dijkstra's two-page note giving the shortest-path and MST algorithms; Edmonds–Karp's shortest-augmenting-path bound making Ford–Fulkerson polynomial; Fredman–Tarjan's Fibonacci heaps with O(1) amortized decrease-key; Bloom's space/time trade-off filter allowing errors; Karger's contraction algorithm for min cut; Indyk–Motwani's locality-sensitive hashing for approximate nearest neighbours in high dimensions.
---
# Classic algorithms papers

| Paper | What it established | Page |
|---|---|---|
| Cook, "The Complexity of Theorem-Proving Procedures" (STOC 1971) | Any NP problem reduces to SAT (Cook–Levin); polynomial-time reducibility as the notion of "at least as hard" | [[np-completeness-and-reductions]] |
| Karp, "Reducibility Among Combinatorial Problems" (1972) | 21 problems (clique, vertex cover, set cover, Hamiltonian cycle, 3-colouring, partition, knapsack, …) shown NP-complete by a tree of reductions from SAT; the term "polynomial complete" | [[np-completeness-and-reductions]] |
| Dijkstra, "A Note on Two Problems in Connexion with Graphs" (1959) | Shortest path tree by growing from the source (no heap yet) and Jarník/Prim MST | [[shortest-paths]], [[minimum-spanning-trees]] |
| Edmonds & Karp, "Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems" (1972) | Augmenting along shortest paths gives O(VE²); capacity scaling; the first strongly polynomial max-flow analyses | [[network-flow]] |
| Fredman & Tarjan, "Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms" (1987) | O(1) amortized insert/decrease-key, O(log n) delete-min via lazy consolidation and potential function; Dijkstra in O(E + V log V), Prim likewise | [[heaps-and-priority-queues]], [[amortized-analysis]] |
| Bloom, "Space/Time Trade-offs in Hash Coding with Allowable Errors" (1970) | A bit array with k hash functions answers membership with no false negatives and tunable false positives — trading correctness for space | [[streaming-and-sketching]] |
| Karger, "Global Min-cuts in RNC, and Other Ramifications of a Simple Min-Cut Algorithm" (1993) | Random edge contraction preserves a fixed min cut with probability ≥ 2/n²; repetition gives a simple, parallelizable min-cut algorithm | [[randomized-algorithms]] |
| Indyk & Motwani, "Approximate Nearest Neighbors: Towards Removing the Curse of Dimensionality" (1998) | Locality-sensitive hash families make (1+ε)-approximate nearest neighbour sublinear in high dimensions | [[similarity-search-and-lsh]] |

## Why read the originals
Each is short and states the *question* more clearly than textbooks do: Cook and Karp frame
reductions as the tool; Dijkstra's note shows how little machinery the idea needs; Bloom's
paper is the birth of "allowable errors" as a design dimension; Indyk–Motwani names the curse of
dimensionality as the enemy.

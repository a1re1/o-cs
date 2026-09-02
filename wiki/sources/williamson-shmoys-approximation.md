---
title: The Design of Approximation Algorithms (Williamson & Shmoys) and Approximation Algorithms (Vazirani)
type: source
section: "3.3"
level: 500
tags: [approximation-algorithms, set-cover, lp-rounding, primal-dual, randomized-rounding, local-search, ptas, bin-packing, tsp, facility-location, semidefinite-programming, max-cut, inapproximability, pcp]
sources: []
authors: [David P. Williamson, David B. Shmoys, Vijay V. Vazirani]
year: 2011
institution: Cornell / Georgia Tech
url: https://www.designofapproxalgs.com/
license: free-pdf
format: pdf
summary: Williamson & Shmoys (free PDF) organize approximation algorithms by technique, each introduced on set cover in chapter 1 — deterministic LP rounding, dual rounding, primal-dual, greedy (ln n), randomized rounding — then greedy and local search (k-center, TSP, parallel machines), rounding data and DP (knapsack FPTAS, bin packing), deterministic and randomized LP rounding (facility location, MAX SAT, MAX CUT, Chernoff), SDP rounding (Goemans–Williamson 0.878 MAX CUT), primal-dual, cuts and metrics, and inapproximability via PCP; Vazirani's book is the combinatorial-first classic.
---
# The Design of Approximation Algorithms

## What it is
§1.1 "Fast. Cheap. Reliable. Choose two": if P ≠ NP you cannot have (1) optimal solutions (2) in
polynomial time (3) for every instance; relax special cases (1), exact exponential search (2 —
integer programming, A*, CP), or optimality (3 — heuristics; this book relaxes it *as little as
possible*). **Definition 1.1**: an α-approximation algorithm is a polynomial-time algorithm that
on every instance returns a solution within factor α of optimal (α > 1 minimization, α < 1
maximization). Why: we need solutions; idealized models; a mathematical rigorous basis for
heuristics; a metric of difficulty (some problems admit PTAS, others only O(log n), others
nothing unless P = NP). §1.2–1.7 **set cover** as the tour of techniques: LP relaxation (fractional
set cover), deterministic rounding (pick sets with xⱼ ≥ 1/f → f-approximation), rounding the
dual, the primal-dual method, the greedy algorithm (Hₙ ≈ ln n), randomized rounding (O(log n)
w.h.p.). Ch. 2 greedy and local search (k-center 2-approx and tightness, list scheduling 2 and
LPT 4/3, TSP: double-tree 2 and Christofides 3/2, minimum-degree spanning trees by local search,
edge colouring). Ch. 3 rounding data and DP (knapsack FPTAS by scaling values, PTAS for parallel
machines, bin packing APTAS). Ch. 4 deterministic LP rounding (completion-time scheduling,
ellipsoid method, prize-collecting Steiner tree, facility location 4-approx, bin packing via
Karmarkar–Karp). Ch. 5 randomized rounding (MAX SAT ½ → ¾ by "better of two", MAX CUT ½,
derandomization by conditional expectations, Chernoff bounds, multicommodity flow, dense
3-colouring). Ch. 6 SDP rounding (Goemans–Williamson MAX CUT 0.878, colouring). Ch. 7 primal-dual
(Steiner forest, feedback vertex set). Ch. 8 cuts and metrics (multiway cut, multicut, tree
metrics, sparsest cut O(√log n)). Ch. 9–15 further techniques; ch. 16 inapproximability (PCP
theorem, unique games), ch. 17 open problems.

## What it adds
The technique-indexed reference for [[approximation-algorithms]]; LP duality from
[[linear-programming-and-duality]] is the engine; contrasts with the hardness side of
[[np-completeness-and-reductions]].

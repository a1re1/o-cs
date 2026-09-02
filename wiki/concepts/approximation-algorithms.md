---
title: Approximation algorithms — guarantees, LP rounding, primal-dual, PTAS, and inapproximability
type: concept
section: "3.3"
level: 500
tags: [approximation-algorithms, approximation-ratio, set-cover, vertex-cover, lp-relaxation, lp-rounding, randomized-rounding, primal-dual, greedy-approximation, local-search, ptas, fptas, knapsack, bin-packing, tsp, christofides, max-cut, goemans-williamson, sdp, facility-location, inapproximability, pcp]
sources: [williamson-shmoys-approximation, np-completeness-and-reductions, kleinberg-tardos-skiena, dpv-algorithms]
summary: An α-approximation is a polynomial-time algorithm whose solution is always within factor α of optimal; the toolkit — greedy with a charging argument (set cover ln n, k-center 2), local search, rounding data plus DP (knapsack FPTAS, bin packing APTAS), LP relaxation with deterministic rounding (vertex cover 2, facility location), dual/primal-dual methods, randomized rounding (MAX SAT 3/4, set cover O(log n) w.h.p.), SDP rounding (MAX CUT 0.878) — is illustrated end-to-end on set cover, and PCP-based hardness shows which ratios are best possible unless P = NP.
---
# Approximation algorithms

**In one sentence.** "Fast. Cheap. Reliable. Choose two" — approximation keeps polynomial time and
all instances and relaxes optimality *by a provable factor* (Williamson–Shmoys Definition 1.1).

## Set cover as the tour (W&S ch. 1)
Given sets S₁..Sₘ ⊆ U with weights, cover U at minimum cost. Let f = max element frequency.
LP relaxation: min Σ wⱼxⱼ s.t. Σ_{j∋e} xⱼ ≥ 1, x ≥ 0 — OPT_LP ≤ OPT.
1. **Deterministic rounding**: take every set with xⱼ ≥ 1/f → feasible, cost ≤ f·OPT_LP
   (vertex cover is f = 2 → the classic 2-approximation).
2. **Rounding the dual**: take sets whose dual constraint is tight → also f-approximation, no LP
   solve needed if you construct a dual…
3. **Primal-dual**: raise dual variables of uncovered elements until a set goes tight; add it —
   combinatorial, fast, f-approx. Same engine as Steiner forest, feedback vertex set.
4. **Greedy**: repeatedly take the set with the best cost per newly covered element → Hₙ ≈ ln n
   approximation, tight (Feige: (1−ε) ln n is NP-hard).
5. **Randomized rounding**: include set j with probability xⱼ, repeat ~ln n rounds → O(log n)
   w.h.p. via Chernoff/union bound ([[concentration-inequalities]]).
The recurring proof shape: bound ALG against a lower bound on OPT (LP value, dual feasible
solution, or a combinatorial bound), never against OPT itself ([[linear-programming-and-duality]]).

## Technique catalogue
| Technique | Example results |
|---|---|
| Greedy / charging | k-center 2 (tight), list scheduling 2, LPT 4/3, set cover ln n, max coverage (1 − 1/e) |
| Local search | facility location, min-degree spanning tree (Δ* + 1), k-median (3 + ε) |
| Rounding data + DP | knapsack FPTAS (scale values by ε·v_max/n), makespan PTAS, bin packing APTAS |
| LP rounding | vertex cover 2, completion-time scheduling, facility location 4 → 1.488, bin packing (Karmarkar–Karp) |
| Randomized rounding | MAX SAT ¾ (better of two), MAX CUT ½, multicommodity flow, dense 3-colouring |
| SDP rounding | Goemans–Williamson MAX CUT 0.878 (random hyperplane), colouring |
| Primal-dual | Steiner forest 2, feedback vertex set |
| Metric embeddings / cuts | multiway cut 3/2, multicut O(log k), sparsest cut O(√log n) |
| Structural | metric TSP: MST doubling 2, Christofides 3/2 (matching on odd-degree vertices), Karlin–Klein–Oveis Gharan 3/2 − ε |
Classes: **PTAS** (1+ε for any fixed ε, time poly in n but maybe exponential in 1/ε); **FPTAS**
(poly in n and 1/ε — knapsack, subset sum); APX (constant factor); log-approximable; and
problems with no constant factor unless P = NP.

## Inapproximability (W&S ch. 16)
The PCP theorem (NP = PCP(log n, 1)) gives gap-producing reductions: MAX 3SAT cannot be
approximated better than 7/8, vertex cover better than 1.36 (2 − ε under UGC), set cover better
than ln n, clique within n^{1−ε}, general TSP at all. Gap reductions are the approximation
analogue of [[np-completeness-and-reductions]].

## Pitfalls
- Comparing to OPT you can't compute: always find a computable lower (or upper) bound.
- "Approximation ratio" of a heuristic without a proof is just an observation.
- Integrality gap of the LP caps what LP rounding can achieve; move to SDP or stronger
  relaxations (Sherali–Adams, Lasserre).
- Practical note: MIP solvers often find optimal solutions where the worst-case theory is bleak.

## Related
- [[np-completeness-and-reductions]], [[linear-programming-and-duality]], [[greedy-algorithms]],
  [[dynamic-programming]], [[randomized-algorithms]], [[concentration-inequalities]], [[convexity]].

## Sources
Williamson & Shmoys ch. 1–8, 16; Vazirani; K&T ch. 11; DPV ch. 9.

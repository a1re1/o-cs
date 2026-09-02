---
title: Constraint satisfaction problems (CSPs) — variables, domains, constraints; backtracking search with MRV/LCV ordering, forward checking and arc consistency (AC-3), constraint propagation, tree-structured and cutset decomposition, and min-conflicts local search
type: concept
section: "6.1"
level: 300
tags: [csp, constraint-satisfaction, variables, domains, constraints, backtracking, forward-checking, arc-consistency, ac-3, constraint-propagation, mrv, minimum-remaining-values, degree-heuristic, lcv, least-constraining-value, tree-structured-csp, cutset-conditioning, tree-decomposition, min-conflicts, map-coloring, n-queens, sudoku, scheduling, binary-constraints, global-constraints, alldiff]
sources: [ai-intro-courses-texts-and-seminal-papers]
summary: A CSP factors a state into variables with domains and constraints (map colouring, n-queens, Sudoku, scheduling, cryptarithmetic) so that general-purpose inference can prune the search: backtracking search assigns one variable at a time and checks constraints, made dramatically faster by ordering (MRV — pick the most constrained variable, fail first; degree heuristic to break ties; LCV — try the least constraining value, succeed first) and by inference (forward checking removes inconsistent values from neighbours; arc consistency via AC-3 propagates further, O(n²d³), detecting failure early; maintaining arc consistency after each assignment); structure helps too — independent components, tree-structured CSPs solvable in O(nd²) by directional arc consistency, cutset conditioning (instantiate a small cycle cutset, solve trees) and tree decomposition (treewidth) — while min-conflicts local search (pick a conflicted variable, assign the value that violates fewest constraints) solves million-queen instances in ~50 steps; the same ideas underlie SAT/SMT solvers and constraint programming.
---
# Constraint satisfaction problems

**In one sentence.** Represent the state as variables with domains and constraints, and let
generic inference (propagate consequences, pick the most constrained variable first) do the
work that domain-specific heuristics do in plain search.

## Formulation (AIMA ch. 6; CS188 L4–5)
Variables X₁…Xₙ, domains Dᵢ (finite, discrete; or continuous — linear constraints → LP —
[[linear-programming-and-duality]]), constraints (unary, binary, higher-order/global such as
Alldiff, Atmost). A **solution** is a complete consistent assignment. Examples: map colouring
(WA ≠ NT …), n-queens, Sudoku (27 Alldiff constraints), cryptarithmetic (auxiliary variables
for carries), scheduling (precedence + resource constraints; disjunctive constraints), circuit
layout, timetabling. Represented as a **constraint graph** (nodes = variables, edges =
constraints); higher-order constraints via dual graph or hidden-variable transformation.
A CSP is NP-complete in general (3-colouring — [[np-completeness-and-reductions]]) but
structure and propagation make most practical instances tractable.

## Backtracking search + ordering + inference
Plain DFS over assignments has a b^n frontier; **commutativity** (order of assignment doesn't
matter) means expanding only one variable per level: n!·dⁿ → dⁿ leaves. **Backtracking**:
choose an unassigned variable, try values consistent with the assignment, recurse, undo.
- **Variable ordering — MRV** (minimum remaining values, "most constrained variable", fail
  first): pick the variable with the fewest legal values — detects dead ends early; **degree
  heuristic** (most constraints on unassigned variables) as tie-breaker / first pick.
- **Value ordering — LCV** (least constraining value, succeed first): try the value that rules
  out the fewest values in neighbours (only matters when you need one solution).
- **Forward checking**: after assigning X, delete inconsistent values from each unassigned
  neighbour's domain; backtrack when any domain empties. Doesn't catch failures between two
  unassigned neighbours.
- **Arc consistency**: X→Y is consistent iff every x ∈ D_X has some y ∈ D_Y satisfying the
  constraint. **AC-3**: queue of arcs; revise(X, Y) removes unsupported x; if D_X changed,
  re-queue all arcs Z→X; O(n²d³) (each arc processed ≤ d times, revise O(d²)); an empty
  domain = failure. Run as preprocessing and as **MAC** (maintaining arc consistency) after
  each assignment. Stronger: path consistency, k-consistency (exponential in k); global
  constraints have specialized propagators (Alldiff via bipartite matching — [[network-flow]];
  bounds propagation for resource constraints). Arc consistency alone solves easy Sudokus;
  hard ones need search.
- **Intelligent backtracking**: conflict-directed backjumping (back to the most recent
  variable in the conflict set), **no-good learning** — the same idea as CDCL clause learning
  ([[sat-and-smt-solvers]]).

## Exploiting structure
- **Independent subproblems** (connected components): solve separately — n/c subproblems of
  size c cost O((n/c)d^c) instead of dⁿ.
- **Tree-structured CSPs**: topological order from a root, make it directionally arc
  consistent backwards (parent→child), then assign forwards without backtracking — O(nd²).
- **Cutset conditioning**: choose a cycle cutset S (removing it leaves a tree), enumerate its
  d^|S| assignments, solve the residual tree each time — exponential only in the cutset size.
- **Tree decomposition**: cluster variables into a tree of mega-variables (treewidth w) —
  O(n d^{w+1}); the same idea as junction trees for Bayes nets ([[bayesian-networks-and-hmms]])
  and tree DP on graphs ([[dynamic-programming]]).

## Local search: min-conflicts (Minton et al. 1992)
Start from a complete (random or greedy) assignment; repeatedly pick a conflicted variable
and set it to the value minimizing the number of violated constraints; random walk/tabu to
escape plateaus. Solves n-queens for n = 10⁶ in ~50 steps (the landscape is easy except near
the critical ratio of constraints to variables — phase transitions, as in random 3-SAT).
Used for scheduling (Hubble telescope), with the [[search-algorithms-ai]] local-search toolkit.

## Pitfalls
- Encoding a CSP without auxiliary variables, producing huge higher-order constraints.
- Choosing MRV but not doing any propagation (MRV needs the pruned domains to be informative).
- Confusing arc consistency with a solution (consistent networks can still be unsolvable —
  e.g. a 3-cycle with 2 colours; only tree-structured networks are guaranteed).
- Using systematic search when a solution merely needs to exist (min-conflicts) or local
  search when you must prove unsatisfiability (systematic only).

## Related
- [[search-algorithms-ai]] (backtracking as DFS; local search), [[sat-and-smt-solvers]]
  (CSPs with Boolean domains; propagation ≈ unit propagation, no-goods ≈ learned clauses),
  [[np-completeness-and-reductions]], [[dynamic-programming]], [[network-flow]],
  [[linear-programming-and-duality]], [[bayesian-networks-and-hmms]] (tree decomposition).

## Sources
AIMA 4e ch. 6; CS188 lectures 4–5 and notes 2.1–2.7; Poole & Mackworth ch. 4; Mackworth 1977 (AC-3); Minton et al. 1992 (min-conflicts); Dechter, *Constraint Processing* 2003.

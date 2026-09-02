---
title: Search in AI — state spaces, uninformed search (BFS, DFS, uniform-cost, iterative deepening), informed search with heuristics (greedy best-first, A*, admissibility, consistency, IDA*), designing heuristics by relaxation, and local search (hill climbing, simulated annealing, beam, genetic)
type: concept
section: "6.1"
level: 300
tags: [search, state-space, problem-formulation, uninformed-search, bfs, dfs, uniform-cost-search, iterative-deepening, informed-search, heuristics, greedy-best-first, a-star, admissible, consistent, monotone, ida-star, weighted-a-star, relaxation, pattern-databases, local-search, hill-climbing, simulated-annealing, beam-search, genetic-algorithms, tree-search, graph-search, frontier, explored-set, branching-factor, pacman]
sources: [ai-intro-courses-texts-and-seminal-papers]
summary: Classical AI problem solving formulates a task as a state space (initial state, actions, transition model, goal test, step cost) and searches a tree of paths with a frontier: BFS (complete, optimal for unit costs, O(b^d) space), DFS (O(bm) space but incomplete/non-optimal), uniform-cost search (Dijkstra on the fly, optimal for positive costs), iterative deepening (DFS space with BFS optimality — the default uninformed method); informed search adds a heuristic h(n) estimating cost-to-go — greedy best-first uses h alone (fast, not optimal), A* orders by f = g + h and is optimal when h is admissible (never overestimates) for tree search and consistent (h(n) ≤ c(n,n') + h(n')) for graph search, and expands the fewest nodes of any optimal algorithm given h — with good heuristics derived from relaxed problems (drop constraints: Manhattan distance, misplaced tiles, pattern databases; the max of admissible heuristics is admissible); memory-bounded variants (IDA*, SMA*) and weighted A* trade optimality for speed; and when only the goal state matters, local search (hill climbing, simulated annealing, beam search, genetic algorithms) walks a single state through a landscape, cheap in memory but prone to local optima and plateaus.
---
# Search in AI

**In one sentence.** Turn a problem into states and actions, then explore paths from the
start with a priority order — cost so far (uniform-cost), estimated cost to go (greedy), or
their sum (A*, optimal with an admissible heuristic) — and derive heuristics by solving a
relaxed version of the same problem.

## Problem formulation (AIMA ch. 3; CS188 L2)
A **search problem**: states, initial state, actions(s), result(s, a), goal test, step
cost. A **state** should include only what matters for the decision (the world state is
larger — Pacman's search state is (position) for path finding, (position, dots eaten) for
eat-all-dots; the state-space size is the product of the relevant factors). **Search tree**
(paths from the root; can be infinite with cycles) vs **state graph**; the **frontier**
(open list) holds partial plans; **graph search** adds an explored set so each state is
expanded once. Measures: **completeness**, **optimality**, time/space in branching factor
b, solution depth d, maximum depth m.

## Uninformed search
| Algorithm | Frontier | Complete | Optimal | Time | Space |
|---|---|---|---|---|---|
| BFS | FIFO queue | yes | unit costs | O(b^d) | O(b^d) |
| DFS | LIFO stack | no (loops/infinite) | no | O(b^m) | O(bm) |
| Depth-limited / iterative deepening (IDS) | DFS with limit ℓ = 0,1,2… | yes | unit costs | O(b^d) (repeated work is a constant factor since the last level dominates) | O(bd) |
| Uniform-cost (UCS) | priority queue on g(n) | yes (positive costs) | yes | O(b^{C*/ε}) | same |
| Bidirectional | two frontiers | yes | with care | O(b^{d/2}) | O(b^{d/2}) |
UCS is [[shortest-paths]] (Dijkstra) run lazily from one source; BFS/DFS are [[graph-search]].
IDS is the default uninformed method when the search space is large and depth unknown.

## Informed search: heuristics and A* (Hart–Nilsson–Raphael 1968; Pearl 1984)
A **heuristic** h(n) estimates the cheapest cost from n to a goal; h(goal) = 0. **Greedy
best-first** expands lowest h: fast in practice, incomplete in trees, not optimal (it can
walk down a corridor). **A\*** expands lowest **f(n) = g(n) + h(n)**: with **admissible** h
(h(n) ≤ h*(n), never overestimates) A* tree search is optimal — proof: a suboptimal goal G₂
has f(G₂) = g(G₂) > C*, while some node n on the optimal path has f(n) ≤ C*, so n is expanded
first. With **consistent** (monotone) h — h(n) ≤ c(n, a, n') + h(n'), the triangle inequality
— f is non-decreasing along paths, so A* **graph search** is optimal and expands nodes in
f-order, and each state is expanded at most once. Consistency implies admissibility; most
natural heuristics are consistent. A* is **optimally efficient**: no optimal algorithm using
the same h expands fewer nodes (up to ties) — but the number expanded is exponential unless
the heuristic error is logarithmic; **memory** is the practical limit (frontier size).
**Designing heuristics — relaxation**: drop constraints so the problem is easy, and use the
relaxed optimal cost: 8-puzzle misplaced tiles (any tile jumps) and Manhattan distance
(tiles slide through others); Pacman: Manhattan or maze distance; the cost of an optimal
solution to a relaxed problem is automatically admissible and consistent. **Dominance**: if
h₂ ≥ h₁ everywhere (both admissible), h₂ expands no more nodes; **max** of admissible
heuristics is admissible; **pattern databases** precompute exact costs of subproblems
(disjoint PDBs add). The trade-off curve runs from h = 0 (UCS, many nodes) to h = h*
(follows the optimal path); inadmissible heuristics can be faster and slightly suboptimal —
**weighted A\*** (f = g + w·h, w > 1 gives a w-approximation), and [[shortest-paths]]-style
landmarks/ALT for road networks. Memory-bounded: **IDA\*** (iterative deepening on f-bound —
linear space, used for puzzles), RBFS, SMA*. A* in practice: robot/game path planning on
grids and navigation meshes ([[graph-search]]), planning (with domain-independent heuristics
from delete relaxation — [[intelligent-agents-and-ai-history]]), and [[shortest-paths]] on
maps.

## Local search (AIMA ch. 4)
When the path is irrelevant (n-queens, scheduling, layout, continuous optimization): keep a
current state and move to neighbours. **Hill climbing** (greedy ascent) gets stuck in local
maxima, ridges, plateaus — fixes: sideways moves, random restarts (complete with probability
→ 1), stochastic/first-choice. **Simulated annealing**: accept worse moves with probability
e^{ΔE/T}, temperature T decreasing on a schedule — converges to the global optimum if cooled
slowly enough (a Metropolis chain — [[markov-chains]], [[monte-carlo-methods]]). **Local beam
search**: k states, keep the best k successors (information sharing, not k restarts);
stochastic beam. **Genetic algorithms**: population, fitness-proportional selection,
crossover, mutation — a stochastic beam search with recombination; rarely better than
well-tuned SA/local search, but robust. Continuous spaces: gradient ascent, Newton's method
([[gradient-descent]]); online search and unknown environments (LRTA*).

## Pitfalls
- A state that carries irrelevant information (exploding the space) or drops relevant
  information (making the goal test wrong).
- Using an inadmissible heuristic with A* and expecting optimality; using a merely
  admissible (inconsistent) heuristic with graph search and a closed set (can lose optimality
  — re-open nodes, or ensure consistency).
- Greedy best-first as "A* without g" — it's neither complete in general nor optimal.
- Forgetting that A*'s cost is memory: the frontier is exponential; use IDA* for puzzles.
- Hill climbing without restarts on a landscape with plateaus.

## Related
- [[graph-search]] (BFS/DFS mechanics), [[shortest-paths]] (Dijkstra, A* on maps),
  [[constraint-satisfaction-problems]] (backtracking search with inference),
  [[adversarial-search-and-game-trees]] (search against an opponent),
  [[markov-decision-processes]] (search under uncertainty), [[dynamic-programming]],
  [[monte-carlo-methods]], [[gradient-descent]].

## Sources
AIMA 4e ch. 3–4; CS188 lectures 2–3 and notes 1.2–1.5; Poole & Mackworth ch. 3; Hart, Nilsson & Raphael 1968; Pearl, *Heuristics* 1984.

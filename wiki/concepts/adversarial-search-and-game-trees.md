---
title: Adversarial search and game trees — minimax, alpha–beta pruning and move ordering, depth-limited search with evaluation functions, expectimax for chance and stochastic opponents, utilities and expected-utility maximization, Monte Carlo tree search, and the history from Shannon/Samuel to Deep Blue and AlphaZero
type: concept
section: "6.1"
level: 300
tags: [adversarial-search, games, game-tree, minimax, alpha-beta, alpha-beta-pruning, move-ordering, evaluation-function, depth-limited, horizon-effect, quiescence, expectimax, chance-nodes, stochastic-games, utilities, expected-utility, rationality, multi-agent, zero-sum, mcts, monte-carlo-tree-search, uct, deep-blue, alphago, alphazero, chess, go, backgammon, pacman-ghosts, iterative-deepening, transposition-table]
sources: [ai-intro-courses-texts-and-seminal-papers]
summary: In a two-player zero-sum game the value of a position is computed by minimax — MAX picks the child with the highest value, MIN the lowest — over a game tree that is far too big to enumerate (chess ~35^80), so practical players use alpha–beta pruning (never evaluates a branch that cannot change the decision; with perfect move ordering it searches b^{d/2}, doubling the reachable depth), depth-limited search with an evaluation function (weighted features approximating the true minimax value, learned or hand-tuned) plus iterative deepening, transposition tables and quiescence search to blunt the horizon effect; when outcomes are uncertain — dice, or an opponent who is not optimal — expectimax averages over chance nodes weighted by probability, which requires utilities on a proper scale (only positive affine transformations preserve expectimax decisions, unlike minimax) and connects games to expected-utility rationality and MDPs; Monte Carlo tree search (UCT: bandit-style selection, random rollouts, backup) replaced evaluation functions for Go and, combined with learned policy/value networks, produced AlphaGo and AlphaZero.
---
# Adversarial search and game trees

**In one sentence.** Against an optimal opponent, value a position by assuming they minimize
what you maximize (minimax), prune branches that cannot change the answer (alpha–beta), cut
off with an evaluation function, and average instead of minimizing where chance or a
non-optimal opponent replaces the adversary (expectimax).

## Games as search (AIMA ch. 5; CS188 L6–7)
Deterministic, turn-taking, two-player, **zero-sum**, perfect-information games (chess,
checkers, Go, tic-tac-toe): states, players, actions, result, terminal test, **utility**
(terminal payoff). The game tree alternates MAX and MIN levels; a **strategy** must specify a
move for every possible opponent reply. **Minimax value**: V(terminal) = utility; V(MAX node)
= max over children; V(MIN node) = min over children — computed by DFS, O(b^m) time, O(bm)
space; optimal against an optimal opponent (and does at least as well against any other).
Multiplayer: vectors of utilities; non-zero-sum games and alliances ([[game-theory]]).

## Alpha–beta pruning
Carry α (best value MAX can guarantee on the path so far) and β (best MIN can guarantee);
prune a MIN node when its value ≤ α (MAX already has something better elsewhere) and a MAX
node when its value ≥ β. The root value is unchanged; intermediate values may be bounds
(matters if you use them for move choice — only the root's best move is exact). With
**perfect move ordering** it examines O(b^{d/2}) nodes — searching twice as deep for the same
cost; random ordering gives ~b^{3d/4}. Ordering heuristics: killer moves, history heuristic,
iterative deepening's previous best move, captures first. **Transposition tables** (hash
the position — Zobrist hashing — [[hash-tables]]) cache values of repeated states (a game
graph, not a tree).

## Resource limits: evaluation functions and cutoffs
Real games cannot reach terminals: **depth-limited** search replaces utility with an
**evaluation function** eval(s) estimating the minimax value — typically a weighted linear sum
of features (material, mobility, king safety, pawn structure), hand-tuned or learned
(Samuel's checkers 1959 learned weights by self-play — the first ML program; modern NNUE
networks in Stockfish; [[reinforcement-learning-basics]] via TD). Only the *ordering* of
evaluations matters for minimax. Pitfalls handled by engineering: the **horizon effect**
(pushing an unavoidable loss beyond the depth limit) — **quiescence search** (extend until the
position is quiet: no pending captures); singular extensions; forward pruning (null-move,
late-move reductions) trades safety for depth. **Iterative deepening** gives anytime behaviour
under a clock. Deep Blue (1997): ~200 M positions/s, alpha–beta with extensions, 8,000-feature
eval, opening/endgame databases; checkers solved (Schaeffer 2007, a draw) with proof-number
search and endgame tables ([[dynamic-programming]] over retrograde analysis).

## Expectimax, utilities, and uncertainty
When outcomes involve **chance** (backgammon dice) or the opponent is a known stochastic
policy (random Pacman ghosts), use **chance nodes** whose value is the **expected** value of
children: V = Σ P(c)·V(c). Against a random adversary expectimax outperforms minimax
(minimax is too pessimistic — it forgoes gains); against an optimal adversary expectimax can
be exploited. Chance makes exact **utility scale** matter: minimax is invariant under any
monotone transformation of utilities, expectimax only under positive affine ones
(U' = aU + b) — so utilities must be genuine (von Neumann–Morgenstern axioms: orderability,
transitivity, continuity, substitutability, monotonicity, decomposability → an agent with
consistent preferences maximizes expected utility; risk aversion via concave utility of money;
[[probability-and-statistics-for-cs]]). Pruning is limited (need bounds on eval — *-minimax);
depth is shallower (the tree branches on dice too); **mixed** trees (max/min/chance) model
games like backgammon (TD-Gammon 1992 learned its eval by self-play). Expectimax with a
single agent acting repeatedly *is* an [[markov-decision-processes]] computation: value
iteration is expectimax on a graph with discounting and reuse. Multi-agent utilities, cooperation,
and mechanism design → [[game-theory]].

## Monte Carlo tree search (Coulom 2006; Kocsis–Szepesvári UCT 2006)
For games with huge branching and no good evaluation function (Go: b ≈ 250): grow a tree
asymmetrically — **select** with the UCB rule (exploit high win-rate, explore rarely-visited:
argmax wᵢ/nᵢ + c√(ln N/nᵢ) — [[multi-armed-bandits]] at every node), **expand** a leaf,
**simulate** a random (or policy-guided) rollout to the end, **backpropagate** the result;
anytime, no heuristic needed, converges to minimax. **AlphaGo** (2016) replaced rollouts with
a value network and guided selection with a policy network trained by supervised + RL;
**AlphaZero** (2017) learned both from self-play only, generalizing to chess and shogi and
beating alpha–beta engines with ~1000× fewer evaluations — search + learned evaluation is the
enduring lesson ([[deep-reinforcement-learning]]).

## Pitfalls
- Using minimax against a known-random opponent (leaves value on the table); expectimax
  against an adaptive one.
- Applying an evaluation function at non-quiet positions (horizon effect).
- Trusting non-root alpha–beta values as exact.
- Treating utilities as ordinal in expectimax.

## Related
- [[search-algorithms-ai]], [[markov-decision-processes]], [[game-theory]],
  [[multi-armed-bandits]], [[reinforcement-learning-basics]], [[deep-reinforcement-learning]],
  [[hash-tables]], [[dynamic-programming]], [[probability-and-statistics-for-cs]].

## Sources
AIMA 4e ch. 5 and 16; CS188 lectures 6–7 and notes 3.1–3.3; Poole & Mackworth ch. 14; Shannon 1950 ("Programming a Computer for Playing Chess"); Knuth & Moore 1975 (alpha–beta analysis); Campbell et al. 2002 (Deep Blue); Silver et al. 2016/2017 (AlphaGo/AlphaZero).

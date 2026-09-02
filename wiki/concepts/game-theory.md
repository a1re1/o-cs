---
title: Game Theory
type: concept
section: "11.5"
level: 500
tags: [game-theory, nash-equilibrium, dominant-strategy, prisoners-dilemma, price-of-anarchy, ppad, zero-sum]
sources: [algorithmic-game-theory-texts-and-papers]
summary: The mathematics of strategic interaction — payoff matrices, dominant strategies, Nash equilibrium (and its PPAD-complete computation), zero-sum games and minimax, and the price of anarchy.
---

# Game Theory
**In one sentence.** Game theory models situations where each participant's best action
depends on what others do, and predicts outcomes via solution concepts like dominant
strategies and Nash equilibrium.

## Why it matters
Any system with self-interested participants — auctions, markets, ad platforms, network
routing, blockchains, even ML training dynamics — is a game. Game theory predicts how
such systems behave, and its algorithmic branch asks whether the predicted outcomes can
even be computed. It is the foundation for [[mechanism-design-and-auctions]].

## How it works
**A game** = players, each with a set of **strategies**, and **payoffs** for every
combination of choices. The **normal form** is a payoff matrix.

**Solution concepts (increasing generality):**
- **Dominant strategy** — best regardless of others' choices. If everyone has one, the
  outcome is obvious (and stable).
- **Nash equilibrium** — a strategy profile where **no player can improve by
  unilaterally deviating**. It is the central concept: a self-enforcing outcome. **Nash
  (1950)** proved every finite game has at least one, possibly in **mixed strategies**
  (randomized).

**The Prisoner's Dilemma** — the canonical example: two players each better off
defecting no matter what the other does (defection is dominant), so both defect and get
a worse outcome than mutual cooperation. It shows individual rationality can produce
collective loss — the engine behind tragedy-of-the-commons, arms races, and free-riding.

**Zero-sum games and minimax.** When one player's gain is another's loss, the
**minimax theorem** (von Neumann) says there is a well-defined optimal (possibly mixed)
strategy and game value; this is the theory under adversarial search (see
[[adversarial-search-and-game-trees]]) and generative adversarial training.

**Repeated & sequential games.** Repetition can sustain cooperation (tit-for-tat, folk
theorems). **Extensive form** (game trees) models sequential moves; **subgame-perfect
equilibrium** refines Nash by backward induction.

**The computational question (algorithmic game theory):**
- Computing a Nash equilibrium is **PPAD-complete** (Daskalakis et al. 2009) — believed
  intractable in the worst case, so equilibrium can exist yet be unreachable by rational
  agents or algorithms.
- Zero-sum equilibria, by contrast, are computable in polynomial time via linear
  programming (see [[linear-programming-and-duality]]).

**Price of anarchy.** The ratio of the social cost at the *worst* Nash equilibrium to
the *optimal* centrally-coordinated cost — how much selfishness hurts. For many routing
and load-balancing games it is a small constant (e.g. 4/3 for selfish routing),
justifying decentralized designs.

## Complexity & trade-offs
- Nash equilibrium is the most general predictor but may be non-unique and hard to
  compute (PPAD); dominant-strategy outcomes are rare but computationally and
  behaviorally clean — a reason mechanism design *engineers* dominant strategies.
- Modeling as zero-sum buys polynomial-time solvability and minimax guarantees, but most
  real interactions are general-sum.

## Pitfalls & gotchas
- **Assuming a unique equilibrium** — many games have several; which one occurs is a
  coordination question game theory alone may not resolve.
- **Equilibrium ≠ good outcome** — the Prisoner's Dilemma's equilibrium is
  Pareto-inferior; equilibrium predicts, it doesn't optimize.
- **Rationality assumptions** — real agents are boundedly rational; behavioral deviations
  matter.
- **Existence ≠ computability** — Nash proved existence, but finding it is PPAD-complete.

## Worked example
Two firms choose High or Low price. Each does better undercutting, so (Low, Low) is the
unique Nash equilibrium via dominant strategies — both earn less than under (High, High),
the Prisoner's Dilemma of price competition. Only a binding mechanism (or repetition
with punishment) escapes it.

## Related
- [[mechanism-design-and-auctions]] — designing games with good equilibria.
- [[adversarial-search-and-game-trees]] — minimax in zero-sum games.
- [[np-completeness-and-reductions]] — PPAD and equilibrium hardness.
- [[linear-programming-and-duality]] — zero-sum equilibria via LP duality.
- [[blockchain-and-cryptocurrencies]] — incentive design as a game.

## Sources
Distilled from [[algorithmic-game-theory-texts-and-papers]] (Roughgarden *Twenty
Lectures*; Nash 1950; Koutsoupias-Papadimitriou 1999; Daskalakis et al. 2009).

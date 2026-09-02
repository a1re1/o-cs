---
title: Algorithmic Game Theory & Economics of Computing — Texts and Papers
type: source
section: "11.5"
level: 500
tags: [game-theory, mechanism-design, auctions, price-of-anarchy, matching-markets]
authors: Roughgarden; Nisan, Roughgarden, Tardos, Vazirani
year: 2016
institution: Stanford
url: https://timroughgarden.org/f13/f13.html
license: mixed
format: texts+courses+papers
sources: []
summary: The algorithmic game theory canon — Roughgarden's Twenty Lectures and CS364A, the Nisan et al. AGT book, and the seminal work from Nash and Vickrey to the price of anarchy, PPAD-completeness of Nash, and sponsored-search auctions.
---

# Algorithmic Game Theory & Economics of Computing — Texts and Papers

## What it is
The intersection of computer science and economics: analyzing systems with **strategic**
participants who act in self-interest, designing rules (mechanisms) that produce good
outcomes despite that, and studying the computational complexity of equilibria. It is
the theory behind auctions, markets, matching, and networked resource allocation.

## Key ideas
- **Games and equilibria** — Nash equilibrium, dominant strategies, and their
  computation. See [[game-theory]].
- **Mechanism design** — "inverse game theory": design rules so truthful behavior is
  optimal (VCG auctions). See [[mechanism-design-and-auctions]].
- **Price of anarchy** — how much selfish behavior degrades a system vs the optimum.
  See [[game-theory]].
- **Matching markets** — stable matching and market-clearing algorithms. See
  [[mechanism-design-and-auctions]].

## Chapter / lecture map
- **Roughgarden, *Twenty Lectures on Algorithmic Game Theory* / Stanford CS364A (free)**
  — the accessible spine: auctions, mechanism design, price of anarchy, equilibria.
- **Nisan, Roughgarden, Tardos & Vazirani, *Algorithmic Game Theory* (free)** — the
  comprehensive reference.
- **Coursera Game Theory (Stanford/UBC)** — foundations for a broad audience.

## Notable claims & quotes
- **Every finite game has a mixed-strategy Nash equilibrium** (Nash 1950) — but finding
  one is **PPAD-complete** (Daskalakis, Goldberg & Papadimitriou 2009), so equilibrium
  may be economically real yet computationally intractable.
- **The price of anarchy** quantifies the cost of decentralization; for many routing and
  scheduling games it is a small constant, reassuring for networked systems.

## Seminal papers
- **Nash (1950)** — existence of equilibrium.
- **Vickrey (1961)** — the second-price (truthful) auction.
- **Myerson (1981)** — optimal (revenue-maximizing) auction design.
- **Koutsoupias & Papadimitriou (1999)** — the price of anarchy.
- **Daskalakis, Goldberg & Papadimitriou (2009)** — PPAD-completeness of Nash.
- **Edelman, Ostrovsky & Schwarz (2007)** — generalized second-price (GSP) sponsored
  -search auctions (how Google/Bing sell ads).

## What it adds
Brings incentives and strategic behavior into system design — essential for auctions,
ad markets, blockchains ([[blockchain-and-cryptocurrencies]] incentive design), and
network protocols. Connects to [[np-completeness-and-reductions]] (PPAD),
[[markov-decision-processes]] and [[reinforcement-learning-basics]] (multi-agent), and
[[network-science]] (games on networks).

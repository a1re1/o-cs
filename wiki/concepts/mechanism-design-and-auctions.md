---
title: Mechanism Design and Auctions
type: concept
section: "11.5"
level: 500
tags: [mechanism-design, auctions, vcg, second-price, truthfulness, matching-markets, gsp]
sources: [algorithmic-game-theory-texts-and-papers]
summary: Inverse game theory — designing rules so that self-interested agents' best strategy is to behave as the designer wants; the second-price and VCG auctions, truthfulness, sponsored-search GSP, and stable matching.
---

# Mechanism Design and Auctions
**In one sentence.** Mechanism design is "inverse game theory": instead of predicting
behavior in a fixed game, it *designs the game's rules* so that rational, self-interested
participants are led to a desired outcome — most famously, telling the truth.

## Why it matters
Mechanism design runs the modern economy of computing: ad auctions (the revenue engine
of the web), spectrum auctions, matching markets (residents to hospitals, students to
schools), and blockchain fee markets. Getting the rules right means the system elicits
honest information and allocates efficiently; getting them wrong invites manipulation.

## How it works
**The goal.** Design a mechanism (allocation rule + payment rule) with good properties:
- **Incentive compatibility / truthfulness** — each agent's best strategy is to report
  its true value (a **dominant-strategy** truthful mechanism removes the need to guess
  others' behavior — see [[game-theory]]).
- **Individual rationality** — participating never hurts.
- **Efficiency** — the item goes to whoever values it most; or **optimality** —
  maximize the designer's revenue.

**The second-price (Vickrey) auction (1961).** Highest bidder wins but pays the
**second**-highest bid. Bidding your true value is a **dominant strategy**: overbidding
risks paying more than the item is worth, underbidding risks losing a profitable win,
and your bid never affects your price (only whether you win). Truthfulness for free.

**VCG (Vickrey-Clarke-Groves).** Generalizes the second-price idea to complex allocations
(multiple items, combinations): choose the welfare-maximizing allocation, and charge each
winner the **externality** it imposes — the harm its presence does to everyone else. VCG
is truthful and efficient in great generality, but has practical flaws (low/erratic
revenue, computational hardness of the underlying allocation, vulnerability to collusion).

**Sponsored search — GSP (Edelman, Ostrovsky & Schwarz 2007).** Search ads are sold by
the **generalized second-price** auction: rank bidders (× quality), each pays roughly the
next bidder's bid. Notably, **GSP is *not* truthful** (unlike VCG), yet it is what
Google/Bing actually use — a real gap between elegant theory (VCG) and deployed practice.

**Matching markets (stable matching).** No money, two sides with preferences (doctors and
hospitals). The **Gale-Shapley deferred-acceptance** algorithm produces a **stable**
matching (no pair prefers each other to their assignment) and is **strategy-proof for the
proposing side**. It powers residency matching and school choice.

**Revelation principle.** Any outcome achievable by *some* mechanism is achievable by a
*truthful* one — so, in theory, restricting attention to truthful mechanisms loses
nothing, which is why truthfulness is the central design target.

## Complexity & trade-offs
- VCG is truthful and efficient but computing the welfare-maximizing allocation can be
  NP-hard (combinatorial auctions), and its revenue can be poor — practical mechanisms
  (GSP, simple reserve-price auctions) trade truthfulness for revenue, robustness, and
  computability.
- Revenue-optimal (Myerson) vs efficiency-optimal (VCG) are different goals needing
  different mechanisms; reserve prices trade some efficiency for revenue.

## Pitfalls & gotchas
- **Assuming deployed = truthful** — GSP is the counterexample; real ad auctions require
  strategic bidding.
- **VCG revenue and collusion problems** make it rare in practice despite its theory.
- **Ignoring the allocation's computational cost** — a truthful mechanism whose
  allocation is NP-hard isn't runnable at scale.
- **Manipulation on the non-proposing side** of Gale-Shapley — stability is strategy
  -proof only for proposers.

## Worked example
Selling one item to bidders valuing it at $10, $7, $4. A first-price auction invites
shading bids below value; the **second-price** auction awards it to the $10 bidder at the
$7 price, and all three do best bidding their true values — the auctioneer gets truthful
information and an efficient allocation without anyone needing to model rivals.

## Related
- [[game-theory]] — the strategic analysis mechanism design inverts.
- [[blockchain-and-cryptocurrencies]] — fee markets and incentive design.
- [[linear-programming-and-duality]] — optimization behind allocations/matching.
- [[network-science]] — two-sided platforms and matching markets.

## Sources
Distilled from [[algorithmic-game-theory-texts-and-papers]] (Roughgarden; Vickrey 1961;
VCG; Edelman et al. 2007; Gale-Shapley).

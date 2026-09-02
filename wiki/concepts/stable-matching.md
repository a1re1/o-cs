---
title: Stable matching (Gale–Shapley)
type: concept
section: "1.1"
level: 200
tags: [stable-matching, gale-shapley, matching, invariants, algorithms, market-design, deferred-acceptance]
sources: [mcs-lehman-leighton-meyer, berkeley-cs70]
summary: The deferred-acceptance "mating ritual" — proposers work down their lists, receivers hold their best offer — always terminates in a stable matching, is proposer-optimal and receiver-pessimal, and is a model proof-by-invariant that also runs hospital residency matches.
---
# Stable matching (Gale–Shapley)

**In one sentence.** Given n proposers and n receivers each ranking the other side, the
proposer-proposing deferred-acceptance algorithm ends in O(n²) proposals with a matching that has no
*rogue couple* (two people who prefer each other to their assigned partners).

## The algorithm (MCS "mating ritual")
Each day: every unmatched proposer proposes to the top receiver still on their list; each receiver
keeps the best proposer so far (tentatively) and rejects the rest; rejected proposers cross that receiver
off. Stop when no proposer is rejected; the tentative pairs become permanent.

## Proof by invariants (a template worth copying)
1. **Termination**: each day at least one name is crossed off some list until the last day; n² names
   total ⇒ ≤ n² + 1 days. (Decreasing measure — [[invariant-principle]].)
2. **Invariant P**: if receiver R has rejected proposer P, then R currently holds someone she prefers
   to P. Preserved because a receiver only ever trades up.
3. **Everyone is matched**: if some proposer were unmatched at the end his list is empty, so every
   receiver rejected him and by P holds someone — n receivers matched to n proposers, contradiction.
4. **Stability**: suppose P and R prefer each other to their partners. P proposed to R before his partner,
   so R rejected him and by P holds someone better than P at the end — contradiction.
5. **Optimality**: the proposing side gets its best possible stable partner; the receiving side its
   worst (proposer-optimal, receiver-pessimal). So who proposes matters — a design decision.

## Where it is used
National Resident Matching Program (hospitals ↔ residents, since 1952; Roth & Shapley Nobel 2012),
school choice, dating apps' pairing, and as the canonical example that a greedy-looking procedure can be
proved correct with two invariants. "Buddy" matching (one-sided, non-bipartite) can have *no* stable
matching (Irving's algorithm decides).

## Pitfalls
- Ties and incomplete lists complicate the guarantees; with ties, "stable" needs a definition (weak/strong).
- Truthfulness: the proposing side has no incentive to lie; receivers may.

## Related
- [[graph-theory-basics]] — bipartite matching without preferences (Hall's theorem).
- [[invariant-principle]], [[induction]].

## Sources
MCS 11.6 (The Stable Marriage Problem); CS70 stable matching note.

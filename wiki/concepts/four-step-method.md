---
title: Four-step method for probability problems (sample spaces, tree diagrams)
type: concept
section: "1.1"
level: 200
tags: [probability-discrete, sample-space, events, tree-diagrams, conditional-probability, monty-hall, independence, bayes]
sources: [mcs-lehman-leighton-meyer]
summary: MCS's discipline for "what is the probability that…" questions — find the sample space, define the event, assign outcome probabilities (tree diagram), sum — which makes Monty Hall, birthday, and conditional-probability puzzles mechanical instead of confusing.
---
# Four-step method for probability

**In one sentence.** Model first, compute second: (1) enumerate outcomes, (2) identify the event,
(3) assign probabilities to outcomes, (4) add them up.

## The steps (MCS 16.2)
1. **Find the sample space** — the set of all outcomes of the randomized experiment. Draw a
   **tree diagram**: one level per random choice; leaves are outcomes.
2. **Define the events of interest** as subsets of the sample space (mark the leaves).
3. **Determine outcome probabilities**: label each branch with a probability (conditional on the path
   so far), the leaf probability is the product along the path. Branch labels at each node sum to 1.
4. **Compute event probabilities** by summing leaf probabilities in the event.

Monty Hall: levels = car location (1/3 each), player's pick (1/3), host's reveal (forced or 1/2).
Twelve leaves; "switching wins" has probability 2/3. The confusion vanishes once the host's rule is a
branch label.

## Conditional probability and independence
- Pr[A | B] = Pr[A ∩ B] / Pr[B]; the tree diagram *is* the product rule Pr[A ∩ B] = Pr[B]·Pr[A | B].
- Law of total probability: Pr[A] = Σ_i Pr[A | B_i] Pr[B_i] over a partition. Bayes: Pr[B | A] =
  Pr[A | B]Pr[B] / Pr[A] — reverse the tree.
- Independence: Pr[A ∩ B] = Pr[A]Pr[B]; mutual independence of many events is stronger than pairwise.
- **Medical test / base-rate fallacy**: a 99%-accurate test for a 1-in-10,000 disease gives a positive
  that is wrong ~99% of the time; the tree makes the arithmetic explicit.

## Birthday principle
With n people and d days, Pr[no collision] ≈ e^{−n²/2d}; collisions become likely at n ≈ √(2d ln 2) ≈
1.18√d. This is why 64-bit hashes collide around 2^32 items and why birthday attacks halve a hash's
security ([[hash-tables]], §5.3).

## Pitfalls
- Choosing a non-uniform sample space and then counting outcomes as if uniform (the classic
  "two children, one is a boy" errors).
- Forgetting that branch probabilities are *conditional* on the path.
- Independence is an assumption about the model, not something you can read off the tree.

## Related
- [[counting-rules]] — uniform sample spaces reduce to counting.
- [[concentration-inequalities]] — from probabilities to bounds on random variables.
- [[random-variables-expectation]] — the next layer (§1.4).

## Sources
MCS ch. 16 (Events and Probability Spaces), 17 (Conditional Probability), 18.

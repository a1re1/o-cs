---
title: Bayesian networks and hidden Markov models (intro level) — conditional independence and d-separation, factored joint distributions, exact inference by enumeration and variable elimination, approximate inference by sampling (prior, rejection, likelihood weighting, Gibbs), temporal models (HMMs: filtering, forward algorithm, Viterbi, smoothing), particle filters, decision networks and value of perfect information, and naive Bayes
type: concept
section: "6.1"
level: 300
tags: [bayes-nets, bayesian-networks, probabilistic-reasoning, conditional-independence, d-separation, active-triples, cpt, chain-rule, factored-joint, inference-by-enumeration, variable-elimination, factors, elimination-order, treewidth, sampling, prior-sampling, rejection-sampling, likelihood-weighting, gibbs-sampling, mcmc, hmm, hidden-markov-model, filtering, forward-algorithm, viterbi, smoothing, forward-backward, particle-filter, dynamic-bayes-net, kalman, decision-networks, influence-diagram, vpi, value-of-information, naive-bayes, pearl]
sources: [ai-intro-courses-texts-and-seminal-papers]
summary: A Bayesian network (Pearl 1988) is a DAG over random variables with a conditional probability table per node given its parents, encoding the joint as Π P(Xᵢ | parents(Xᵢ)) — exponentially smaller than the full table when the graph is sparse — and its conditional independences are read off by d-separation (chains and forks block when the middle node is observed, colliders/v-structures block unless the collider or a descendant is observed — "explaining away"); exact inference answers P(query | evidence) by enumeration (exponential) or variable elimination (multiply factors, sum out hidden variables in a good order; cost exponential in the treewidth, polynomial for polytrees, NP-hard in general); approximate inference samples — prior sampling, rejection sampling (wastes samples with unlikely evidence), likelihood weighting (fix evidence, weight samples), and Gibbs sampling (an MCMC chain resampling one variable given its Markov blanket); time adds a Markov chain over hidden states with an emission per step — the HMM — where filtering (forward algorithm: predict with the transition model, update with the emission, normalize) tracks belief in O(S²) per step, Viterbi finds the most likely state sequence by max-product DP, forward–backward smooths with future evidence, and particle filters approximate filtering with weighted samples (Monte Carlo localization; resampling to fight degeneracy); decision networks add action and utility nodes so the value of perfect information prices evidence before buying it, and naive Bayes is the simplest network used as a classifier.
---
# Bayesian networks and hidden Markov models

**In one sentence.** Write the joint distribution as a product of local conditionals over a
DAG so that independence is structural, inference is variable elimination or sampling, and
tracking over time is the same machinery on a chain: predict, then update with evidence.

## Representation (AIMA ch. 13; CS188 L12–13)
Variables and the joint P(X₁…Xₙ) (2ⁿ entries — [[probability-and-statistics-for-cs]],
[[bayes-theorem-and-inference]]). A **Bayes net**: a DAG plus, for each node, P(Xᵢ |
Parents(Xᵢ)) (a **CPT**); the joint is P(x₁…xₙ) = Π P(xᵢ | parents(xᵢ)) — valid when each
variable is conditionally independent of its non-descendants given its parents (the
construction: order the variables, choose minimal parent sets; a causal order gives compact,
robust networks). Size: n·2^k for k parents vs 2ⁿ. Classics: burglary–earthquake–alarm–
John/Mary; sprinkler/rain/wet grass; medical diagnosis nets (QMR-DT with noisy-OR CPTs).
**Independence from structure — d-separation**: X ⊥ Y | Z iff every undirected path is
blocked by an inactive triple: causal chain A→B→C and common cause A←B→C are blocked when B
is observed; common effect A→B←C (**v-structure**, collider) is blocked unless B or a
descendant is observed — observing the effect makes causes dependent (**explaining away**).
The **Markov blanket** (parents, children, children's parents) makes a node independent of
everything else. Structure supports **causality** claims only with extra assumptions
(Pearl's do-calculus; Poole & Mackworth ch. 11).

## Exact inference (AIMA ch. 13.3; CS188 L14)
Query P(Q | e): **enumeration** sums the joint over hidden variables — O(2ⁿ) with repeated
work. **Variable elimination**: represent CPTs as **factors**; for each hidden variable in an
elimination order, **join** (pointwise multiply) all factors mentioning it and **sum it out**;
finally normalize. Cost is exponential in the size of the largest factor created = 
**treewidth** of the induced graph under the order (finding the best order is NP-hard;
heuristics: min-degree, min-fill); polynomial on **polytrees** (singly connected); NP-hard in
general (even #P-hard for exact probabilities — 3-SAT reduces to inference). Junction-tree /
clique-tree algorithms answer all marginals at once; the same message-passing is belief
propagation (exact on trees, approximate — "loopy" — on graphs; [[constraint-satisfaction-problems]]
tree decomposition, [[dynamic-programming]]). Deeper: [[probabilistic-graphical-models]].

## Approximate inference by sampling (CS188 L15)
- **Prior sampling**: sample topologically from CPTs; estimate any probability by counting —
  consistent as N → ∞.
- **Rejection sampling**: discard samples inconsistent with evidence — wasteful when evidence
  is unlikely (most samples rejected).
- **Likelihood weighting**: fix evidence variables, sample the rest, weight each sample by
  Π P(eᵢ | parents(eᵢ)); evidence influences only descendants' sampling — poor when evidence
  is downstream of many hidden variables.
- **Gibbs sampling**: start from a consistent assignment; repeatedly resample one hidden
  variable conditioned on all others (only its Markov blanket matters — cheap); the stationary
  distribution of this **Markov chain** is P(X | e) ([[markov-chains]], [[monte-carlo-methods]]);
  burn-in, mixing; the entry to **MCMC** (Metropolis–Hastings) — [[probabilistic-graphical-models]].

## Temporal models: HMMs and particle filters (AIMA ch. 14; CS188 L16–17)
Add time: hidden state Xₜ with a stationary **transition model** P(Xₜ | Xₜ₋₁) (first-order
Markov — [[markov-chains]]) and **sensor model** P(Eₜ | Xₜ) — an **HMM** when X is a single
discrete variable; a **dynamic Bayes net** in general. Tasks:
- **Filtering** P(Xₜ | e₁:ₜ) — the **forward algorithm**: predict B'(Xₜ) = Σ P(Xₜ | xₜ₋₁) B(xₜ₋₁)
  (belief spreads toward the stationary distribution), then update B(Xₜ) ∝ P(eₜ | Xₜ) B'(Xₜ);
  O(S²) per step, constant memory — robot localization, speech, tracking.
- **Prediction** (forward without evidence), **smoothing** P(Xₖ | e₁:ₜ) with the
  **forward–backward** algorithm, **most likely explanation** by **Viterbi** (replace sum by
  max — [[dynamic-programming]]; speech decoding, POS tagging — [[nlp-fundamentals]]).
- **Particle filtering** when S is too large (continuous or joint states): represent the
  belief by N samples; **elapse time** by sampling each particle's transition; **observe** by
  weighting with P(e | x); **resample** N particles proportional to weight (avoids weight
  degeneracy; loses diversity — Monte Carlo localization for robots, SLAM's Rao-Blackwellized
  filters). Continuous Gaussian linear models → the **Kalman filter** (exact, closed form;
  [[state-estimation-and-kalman-filters]]).

## Decisions and value of information (AIMA ch. 16; CS188 L18)
**Decision network** (influence diagram): chance nodes + action (rectangle) + utility
(diamond) nodes; choose the action maximizing expected utility given evidence, via Bayes-net
inference for P(outcome | evidence, action). **Value of perfect information** VPI(E' | e) =
E_{e'}[MEU(e, e')] − MEU(e) ≥ 0 (nonnegative, not additive, order-independent) — decide whether
to buy a test before acting; the basis of information-gathering agents and active learning.
**Naive Bayes** (one class node, conditionally independent features): P(Y | f) ∝ P(Y) Π P(fᵢ
| Y) — inference is trivial; parameters by counting with Laplace smoothing; tune smoothing on
held-out data — the intro to [[machine-learning-basics]] classification (spam, digits).

## Pitfalls
- Reading independence off edges instead of d-separation (forgetting explaining away).
- Assuming a Bayes net must be causal, or that arrows imply causation.
- Rejection sampling with rare evidence; likelihood weighting with evidence far downstream.
- Poor elimination order (treewidth blow-up) — or exact inference where sampling suffices.
- Particle filters without resampling (degeneracy) or with too few particles (loss of the
  true hypothesis — particle deprivation).

## Related
- [[bayes-theorem-and-inference]], [[probability-and-statistics-for-cs]], [[markov-chains]],
  [[monte-carlo-methods]], [[dynamic-programming]], [[probabilistic-graphical-models]] (Koller
  & Friedman depth), [[state-estimation-and-kalman-filters]], [[machine-learning-basics]],
  [[nlp-fundamentals]], [[constraint-satisfaction-problems]], [[markov-decision-processes]].

## Sources
AIMA 4e ch. 12–14, 16; CS188 lectures 12–18 and notes 6–9; Poole & Mackworth ch. 9–11; Pearl 1988; Rabiner 1989 (HMM tutorial); Doucet et al. 2001 (particle filters).

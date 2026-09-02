---
title: Multi-armed bandits — the exploration–exploitation problem, regret, explore-then-commit and ε-greedy, optimism (UCB1 and its O(√(KT log T)) regret), Thompson sampling (Bayesian posterior sampling), lower bounds (Lai–Robbins), adversarial bandits (Exp3), contextual and linear bandits (LinUCB), best-arm identification, and applications from A/B testing and recommendation to MCTS and hyperparameter search
type: concept
section: "6.6"
level: 400
tags: [bandits, multi-armed-bandit, exploration-exploitation, regret, pseudo-regret, explore-then-commit, epsilon-greedy, optimism-in-the-face-of-uncertainty, ucb, ucb1, kl-ucb, confidence-bounds, hoeffding, thompson-sampling, posterior-sampling, beta-bernoulli, bayesian-bandits, lai-robbins, lower-bound, gap-dependent, minimax, adversarial-bandits, exp3, contextual-bandits, linear-bandits, linucb, off-policy-evaluation, inverse-propensity, best-arm-identification, successive-elimination, a-b-testing, recommendation, ad-auctions, mcts-uct, hyperparameter-optimization, successive-halving, hyperband, lattimore-szepesvari]
sources: [reinforcement-learning-texts-courses-and-seminal-papers]
summary: A bandit is reinforcement learning with one state: K arms with unknown reward distributions, T rounds, and the goal of minimizing regret — the gap between the reward of always pulling the best arm and what the algorithm earned — which forces the exploration–exploitation trade-off in its purest form; naive strategies (explore-then-commit, ε-greedy) incur regret linear or T^{2/3}, while optimism in the face of uncertainty — UCB1 pulls the arm maximizing empirical mean + √(2 ln t / nᵢ), a Hoeffding upper confidence bound — achieves O(Σᵢ log T / Δᵢ) gap-dependent and O(√(KT log T)) worst-case regret, essentially matching the Lai–Robbins lower bound (Ω(log T) is unavoidable), and Thompson sampling — sample a plausible mean for each arm from its Bayesian posterior (Beta for Bernoulli rewards) and pull the sampled best — matches it with better constants and trivial implementation; adversarial bandits (Exp3, exponential weights with importance-weighted estimates) drop the stochastic assumption at a √K cost, contextual bandits choose arms given features (LinUCB's ridge-regression confidence ellipsoids; the model of news recommendation, ad placement, and personalization, evaluated offline by inverse-propensity scoring), and best-arm identification switches the goal from cumulative reward to confident selection (successive elimination, racing); the same optimism/posterior-sampling ideas run MCTS's UCT selection rule, RL exploration bonuses, adaptive A/B tests, and hyperparameter search (successive halving, Hyperband).
---
# Multi-armed bandits

**In one sentence.** With no state to worry about, the only question is how to trade
information for reward, and the answer — be optimistic about what you haven't tried, or
sample from your beliefs — costs only logarithmic regret and reappears in every
exploration problem from MCTS to A/B testing.

## The problem and regret (Sutton & Barto ch. 2; Lattimore & Szepesvári ch. 4)
K arms; pulling arm i yields a reward from an unknown distribution with mean μᵢ; μ* = max μᵢ,
gaps Δᵢ = μ* − μᵢ. Over T rounds the learner's (pseudo-)**regret** is R_T = T μ* − E[Σ rewards]
= Σᵢ Δᵢ E[nᵢ(T)] — the price of not knowing the best arm. Sublinear regret (R_T/T → 0) means
the learner eventually plays optimally. **Explore-then-commit**: pull each arm m times,
commit to the empirical best — regret O(T^{2/3}) with the best m (and requires knowing T);
**ε-greedy**: linear regret for fixed ε, O(log T)-ish with ε_t ∝ 1/t if tuned to the gaps;
**optimistic initialization** (start all estimates high) explores once then stops; the
**gradient bandit** (softmax preferences updated by reward − baseline) is REINFORCE with one
state ([[deep-reinforcement-learning]]). Non-stationary rewards: constant step size /
sliding windows.

## Optimism: UCB (Auer, Cesa-Bianchi & Fischer 2002)
**UCB1**: pull argmaxᵢ [μ̂ᵢ + √(2 ln t / nᵢ)] — the empirical mean plus a Hoeffding confidence
radius ([[concentration-inequalities]]); "optimism in the face of uncertainty": an arm is
pulled either because it is good or because it is uncertain, and each pull shrinks the
uncertainty. Regret ≤ Σ_{i: Δᵢ>0} (8 ln T)/Δᵢ + O(K) — **O(log T)**, gap-dependent; worst case
(Δ ≈ √(K/T)) gives O(√(KT log T)); MOSS/UCB-V/KL-UCB tighten constants (KL-UCB is
asymptotically optimal for Bernoulli). **Lower bound** (Lai & Robbins 1985): any consistent
algorithm has E[nᵢ(T)] ≥ ln T / KL(μᵢ, μ*) asymptotically — logarithmic regret is necessary;
minimax lower bound Ω(√(KT)). Tuning the confidence width trades the two regimes.

## Thompson sampling (Thompson 1933; Chapelle & Li 2011; Agrawal & Goyal 2012)
Maintain a posterior over each arm's mean (Beta(αᵢ, βᵢ) for Bernoulli rewards — update
α += reward, β += 1 − reward; Gaussian for Gaussian rewards — [[bayes-theorem-and-inference]],
[[bayesian-inference]]); each round **sample** θᵢ from each posterior and pull argmax θᵢ.
Probability matching: an arm is pulled with the posterior probability that it is best.
Regret matches the Lai–Robbins bound (Kaufmann et al. 2012), empirically beats UCB, handles
delayed feedback and batching gracefully, extends to any likelihood via MCMC/approximations
([[monte-carlo-methods]]) — the practical default in industry (ad/recommendation systems).
Bayesian bandits with a known horizon: Gittins indices (optimal for discounted infinite-
horizon, expensive); information-directed sampling.

## Adversarial, contextual, and linear bandits (Lattimore & Szepesvári parts III–V)
**Adversarial**: rewards chosen by an adversary; compete with the best fixed arm in
hindsight. **Exp3**: exponential weights over arms (Hedge — [[online-learning-and-regret]])
fed with **importance-weighted** reward estimates r̂ᵢ = rᵢ 1[aₜ = i]/pᵢ (unbiased, only the
pulled arm is observed); regret O(√(KT log K)) — the √K over full-information is the price
of bandit feedback; Exp3-IX/Exp4 (with expert advice). **Contextual bandits**: see context
xₜ (user features), choose arm, observe only that arm's reward — supervised learning with
partial labels; **LinUCB** (Li et al. 2010): assume E[r | x, a] = θₐᵀx, ridge-regress θₐ,
pull argmax θ̂ₐᵀx + α√(xᵀAₐ⁻¹x) (a confidence ellipsoid; regret Õ(d√T)); Thompson sampling
with Gaussian posteriors; neural/tree policies via reductions to cost-sensitive
classification (Vowpal Wabbit); **off-policy evaluation** of a new policy from logged
bandit data by inverse propensity scoring / doubly robust estimators — the counterfactual
evaluation problem of recommendation and ads ([[causal-inference]]). Combinatorial and
dueling bandits (preference feedback — the bandit ancestor of RLHF).

## Best-arm identification and applications
**Pure exploration**: find the best arm with confidence 1 − δ using as few pulls as possible
(fixed confidence: successive elimination / racing, LUCB; fixed budget: successive halving) —
sample complexity Σ log(1/δ)/Δᵢ²; the theory behind **adaptive A/B testing** and early stopping
of experiments ([[hypothesis-testing-and-confidence-intervals]]; peeking at p-values is the
naive version). **Hyperband** (Li et al. 2017): successive halving over training budgets for
hyperparameter search ([[neural-network-training]]). **UCT** in **MCTS**: UCB1 at every tree
node is what made Go tractable ([[adversarial-search-and-game-trees]]). RL exploration
bonuses and posterior-sampling RL (PSRL, bootstrapped DQN) are the multi-state
generalizations ([[deep-reinforcement-learning]]); clinical trials (adaptive allocation),
network routing, ad auctions and recommendation (with delayed/censored rewards) are the
deployed uses.

## Pitfalls
- ε-greedy with a fixed ε forever (linear regret); explore-then-commit with an unknown
  horizon.
- Using UCB confidence widths for rewards outside [0, 1] without scaling.
- Evaluating a contextual-bandit policy on logged data without propensities (selection
  bias).
- Stopping an A/B test when the difference "looks significant" (best-arm identification
  needs the sequential bound).
- Treating non-stationary or adversarial settings with stochastic algorithms.

## Related
- [[reinforcement-learning-basics]], [[deep-reinforcement-learning]],
  [[markov-decision-processes]], [[adversarial-search-and-game-trees]],
  [[concentration-inequalities]], [[bayes-theorem-and-inference]], [[bayesian-inference]],
  [[monte-carlo-methods]], [[online-learning-and-regret]], [[causal-inference]],
  [[hypothesis-testing-and-confidence-intervals]], [[neural-network-training]],
  [[llm-post-training-sft-rlhf-dpo]] (dueling bandits → RLHF).

## Sources
Sutton & Barto ch. 2; Lattimore & Szepesvári 2020 (ToC/structure from memory); Auer, Cesa-Bianchi & Fischer 2002; Lai & Robbins 1985; Thompson 1933; Chapelle & Li 2011; Agrawal & Goyal 2012; Auer et al. 2002b (Exp3); Li et al. 2010 (LinUCB); Li et al. 2017 (Hyperband); Kocsis & Szepesvári 2006 (UCT).

---
title: Reinforcement learning basics (Sutton & Barto) — the agent–environment loop, returns and value functions, dynamic programming vs Monte Carlo vs temporal-difference learning, SARSA and Q-learning (on- vs off-policy), n-step methods and eligibility traces (TD(λ)), exploration, function approximation and the deadly triad, planning with learned models (Dyna), and the unifying dimensions of RL algorithms
type: concept
section: "6.6"
level: 400
tags: [reinforcement-learning, agent-environment, reward-hypothesis, return, discount, episodic, continuing, policy, value-function, state-value, action-value, q-function, bellman, dynamic-programming, policy-evaluation, policy-improvement, generalized-policy-iteration, monte-carlo, first-visit, temporal-difference, td-0, td-error, bootstrapping, sarsa, q-learning, expected-sarsa, on-policy, off-policy, importance-sampling, n-step, eligibility-traces, td-lambda, exploration, epsilon-greedy, optimistic-initialization, function-approximation, semi-gradient, linear-features, tile-coding, deadly-triad, dyna, planning, prioritized-sweeping, model-based, sutton-barto, gridworld, cliff-walking, mountain-car]
sources: [reinforcement-learning-texts-courses-and-seminal-papers]
summary: Sutton & Barto's RL is learning to act from reward through the agent–environment loop, with the reward hypothesis (all goals as maximization of expected cumulative scalar reward) and the MDP as the formal frame; value functions V^π and Q^π satisfy Bellman equations, and every learning method estimates them by some mix of three ideas — dynamic programming (full-width expected backups, needs the model), Monte Carlo (sample complete episodes, average returns; unbiased, high variance, no bootstrapping), and temporal-difference learning (update toward r + γV(s′), bootstrapping from the current estimate; biased, low variance, online, works in continuing tasks; TD(0), and n-step/TD(λ) with eligibility traces interpolating between TD and MC) — organized by generalized policy iteration (evaluate, then improve greedily) with exploration (ε-greedy, optimistic initial values, UCB) to keep visiting states; control algorithms differ in what they bootstrap toward — SARSA (on-policy: the action actually taken; learns the safe path on the cliff) vs Q-learning (off-policy: the max; learns the optimal path but explores dangerously) vs expected SARSA — and off-policy learning of one policy from another's data needs importance sampling; scaling beyond tables uses function approximation (linear features, tile coding, neural nets) with semi-gradient updates, which is where the deadly triad — bootstrapping + off-policy + function approximation — can diverge; and Dyna unifies learning and planning by using a learned model to generate simulated experience for the same updates.
---
# Reinforcement learning basics

**In one sentence.** Estimate how good states and actions are from experience, improve the
policy toward what looks best, keep exploring — and choose, along three dials
(bootstrap or not, sample or expect, on- or off-policy), how much to trust your own
current guesses versus the returns you actually observed.

## The problem (Sutton & Barto ch. 1, 3; Spinning Up part 1)
Agent observes state sₜ (or an observation of it), takes action aₜ ~ π(· | sₜ), receives
reward rₜ₊₁ and next state; the **reward hypothesis**: goals = maximizing expected
cumulative reward. **Return** Gₜ = Σ γᵏ rₜ₊ₖ₊₁ (episodic: finite; continuing: discounted, γ < 1).
The formal frame is the [[markov-decision-processes]] page (states, transitions, Bellman
equations, value/policy iteration when the model is known — **dynamic programming**). Here
the model is unknown or too big: learn from samples. Value functions: V^π(s) = E[Gₜ | sₜ = s],
Q^π(s, a); optimal V*, Q*; π* greedy in Q*. **Generalized policy iteration (GPI)**: any
interleaving of (approximate) evaluation and greedy improvement converges — the template
for every control algorithm. Exploration vs exploitation: ε-greedy, optimistic initial
values, UCB ([[multi-armed-bandits]] is RL with one state).

## Three ways to estimate value (ch. 4–6)
| Method | Update target | Needs model | Bias/variance | Online |
|---|---|---|---|---|
| Dynamic programming | Σ p(s′, r | s, a)[r + γV(s′)] (expected, full width) | yes | exact | no |
| Monte Carlo | actual return Gₜ (episode end) | no | unbiased, high variance | no (episodic) |
| Temporal difference TD(0) | rₜ₊₁ + γV(sₜ₊₁) (sample, bootstraps) | no | biased, low variance | yes |
**TD(0)**: V(sₜ) ← V(sₜ) + α[rₜ₊₁ + γV(sₜ₊₁) − V(sₜ)] — the bracket is the **TD error** δₜ (the
dopamine signal of ch. 15). TD converges to the certainty-equivalence (maximum-likelihood
MDP) solution and is usually faster than MC on Markov tasks; MC is robust to non-Markov
states. **Bootstrapping** = updating a guess from a guess; **sampling** = one transition
instead of the expectation. **n-step** returns Gₜ:ₜ₊ₙ = rₜ₊₁ + … + γⁿ⁻¹rₜ₊ₙ + γⁿV(sₜ₊ₙ) interpolate;
**TD(λ)** averages all n-step returns with weights (1−λ)λⁿ⁻¹ — the **λ-return**; implemented
backward with **eligibility traces** eₜ = γλeₜ₋₁ + ∇V(sₜ) (a decaying memory of visited states;
each TD error updates all recently visited states) — λ = 0 is TD(0), λ = 1 is MC; true online
TD(λ). Choosing λ/n trades bias against variance and speeds credit assignment.

## Control: SARSA, Q-learning, expected SARSA (ch. 6.4–6.6)
Learn Q instead of V (no model needed to act greedily — [[markov-decision-processes]]).
- **SARSA** (on-policy): Q(s, a) ← Q + α[r + γ Q(s′, a′) − Q(s, a)] with a′ the action the
  ε-greedy policy actually takes next; converges to the optimal ε-greedy policy (if ε → 0,
  to Q*). On **cliff walking** it learns the safe path away from the cliff (it accounts for
  its own exploration).
- **Q-learning** (off-policy, Watkins 1989): target r + γ maxₐ′ Q(s′, a′) — learns Q* directly
  regardless of the behaviour policy (given infinite visits and decaying α); takes the
  optimal cliff-edge path and falls off during training. **Maximization bias**: the max over
  noisy estimates is optimistic → **double Q-learning** (two estimators, one selects, the other
  evaluates — Double DQN later).
- **Expected SARSA**: target r + γ Σₐ′ π(a′ | s′) Q(s′, a′) — lower variance, generalizes both.
**Off-policy learning** in general (learn π from data of b): weight returns by the
**importance-sampling ratio** Π π(aₖ | sₖ)/b(aₖ | sₖ) — unbiased but high variance (ordinary vs
weighted IS; per-decision IS); Q-learning avoids it by bootstrapping one step. Monte Carlo
control: exploring starts or ε-soft policies; first-visit vs every-visit.

## Function approximation and the deadly triad (ch. 9–11)
Tables don't scale (Go: 10¹⁷⁰ states); represent V(s; w) or Q(s, a; w) with **linear
features** (tile coding, coarse coding, Fourier basis, RBFs) or neural nets
([[deep-reinforcement-learning]]). **Semi-gradient TD**: w ← w + α[r + γ V(s′; w) − V(s; w)]
∇V(s; w) — "semi" because the target's dependence on w is ignored; converges for linear
on-policy prediction (to within a bounded error of the best fit under the on-policy
distribution), and semi-gradient SARSA works for control (**mountain car** with tile
coding). Generalization couples states: an update to one changes others, so the
**on-policy distribution** matters. The **deadly triad** — **function approximation** +
**bootstrapping** + **off-policy** training — can diverge (Baird's counterexample; the
off-policy distribution and bootstrapped targets can amplify errors); remedies: gradient-TD
methods (GTD, TDC — true gradients of the projected Bellman error), emphatic TD, target
networks and replay in practice (DQN), or avoiding one leg (MC targets, on-policy). LSTD
solves the linear case in closed form. Least-squares and batch methods; the
bias/variance/stability trade-offs behind every deep RL trick.

## Planning and learning: Dyna (ch. 8)
A **model** (learned transition/reward, tabular or approximate) lets the agent generate
**simulated experience**; **Dyna-Q**: after each real step, do the Q-learning update, update
the model, then do n planning updates on sampled (s, a) from the model — the same update
rule for real and simulated data; dramatically more sample-efficient; wrong models are
corrected by real experience (Dyna-Q+ adds exploration bonuses for stale transitions).
**Prioritized sweeping** plans backward from states whose values changed most. Decision-time
planning: rollouts, **MCTS** ([[adversarial-search-and-game-trees]]) — AlphaGo is "planning
with learned value/policy". Trajectory sampling, expected vs sample backups, and the
unifying view: DP, MC, TD, Dyna, MCTS are all backup diagrams of different width and depth.

## Unifying dimensions (ch. 17; Silver lecture 8)
Every method is characterized by: **backup width** (sample ↔ expected), **backup depth**
(one-step TD ↔ full-return MC, with n-step/λ between), **on-/off-policy**, **model-free ↔
model-based**, **tabular ↔ approximate**, **value-based ↔ policy-based ↔ actor-critic**
([[deep-reinforcement-learning]]), **prediction ↔ control**. Reading a new algorithm means
locating it on these axes. Beyond the basics: average-reward and options/hierarchical RL,
partial observability (POMDPs — [[bayesian-networks-and-hmms]]), reward design and shaping
(potential-based shaping preserves optimal policies), and the psychological/neural
correspondences (TD error ≈ dopamine; habits ≈ model-free, goal-directed ≈ model-based).

## Pitfalls
- Confusing on-policy SARSA with off-policy Q-learning targets (a′ taken vs max).
- Constant α in a stationary problem (never converges) vs decaying α in a non-stationary one
  (stops adapting).
- Off-policy + bootstrapping + approximation without stabilization (divergence).
- Monte Carlo in continuing tasks; TD in strongly non-Markov observations.
- Reward shaping that is not potential-based (changes the optimal policy); sparse rewards
  with naive ε-greedy exploration (never finds the goal — see [[deep-reinforcement-learning]]).

## Related
- [[markov-decision-processes]], [[multi-armed-bandits]], [[deep-reinforcement-learning]],
  [[adversarial-search-and-game-trees]], [[dynamic-programming]], [[markov-chains]],
  [[monte-carlo-methods]], [[bayesian-networks-and-hmms]], [[gradient-descent]],
  [[llm-post-training-sft-rlhf-dpo]] (RL applied to language models).

## Sources
Sutton & Barto 2e ch. 1–13, 17 (site read; content from the book); Silver UCL lectures 1–8; Spinning Up part 1 (read); Szepesvári 2010; Sutton 1988; Watkins 1989; Rummery & Niranjan 1994 (SARSA); van Hasselt 2010 (double Q); Baird 1995.

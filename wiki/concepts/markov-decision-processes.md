---
title: Markov decision processes (MDPs) — states, actions, transitions, rewards, discounting; policies and the Bellman equations; value iteration and policy iteration; and the bridge to reinforcement learning (model-free TD, Q-learning, exploration) when the model is unknown
type: concept
section: "6.1"
level: 300
tags: [mdp, markov-decision-process, states, actions, transition-model, rewards, discount-factor, gamma, policy, optimal-policy, utility, value-function, q-values, bellman-equation, bellman-optimality, value-iteration, policy-iteration, policy-evaluation, policy-extraction, convergence, contraction, horizon, stationarity, living-reward, gridworld, reinforcement-learning-basics, model-based, model-free, temporal-difference, q-learning, exploration-exploitation, epsilon-greedy, approximate-q-learning, feature-based, stochastic-planning]
sources: [ai-intro-courses-texts-and-seminal-papers]
summary: An MDP models sequential decision making under uncertainty with states, actions, a transition model P(s'|s,a) (Markov: the next state depends only on the current state and action), rewards R(s,a,s'), and a discount γ ∈ (0,1) that makes infinite-horizon sums finite and expresses preference for sooner reward; a policy π maps states to actions, its value V^π(s) is the expected discounted return, and the optimal values satisfy the Bellman optimality equation V*(s) = max_a Σ_s' P(s'|s,a)[R + γV*(s')] (Q*(s,a) for state-action pairs) — a fixed-point of a γ-contraction, so value iteration (repeated Bellman backups, O(S²A) per sweep, converging geometrically) and policy iteration (evaluate the current policy by solving a linear system or iterating, then greedily improve; converges in few iterations) compute optimal policies exactly — expectimax with reuse and discounting; when P and R are unknown the agent must learn from experience, which is reinforcement learning: model-based (estimate P, R, then plan), or model-free — temporal-difference learning of V^π from samples (moving average of sampled Bellman backups), Q-learning (off-policy: learns Q* while following any exploring policy; converges with decaying learning rate and sufficient exploration), ε-greedy and optimism for exploration, and feature-based approximate Q-learning to generalize across large state spaces.
---
# Markov decision processes

**In one sentence.** When actions have uncertain outcomes, plan for expected discounted
reward: the optimal value function is the unique fixed point of the Bellman backup, and
value/policy iteration find it — and when you don't know the transition model, sampling the
backups from experience is reinforcement learning.

## The model (AIMA ch. 17; CS188 L8–9)
An **MDP** = (S, A, P(s'|s,a), R(s,a,s'), γ, start state, optional terminals). **Markov
property**: the future depends only on the present state and action — the same assumption
as [[markov-chains]] plus a decision at each step. **Gridworld**: a "noisy" move goes the
intended way with probability 0.8 and sideways 0.1 each; a **living reward** (small negative)
shapes urgency. A **policy** π: S → A (stationary policies suffice for infinite-horizon
discounted MDPs); the agent wants the policy maximizing expected **discounted return**
E[Σ γᵗ rₜ]. **Discounting** γ < 1: keeps sums bounded (≤ R_max/(1−γ)), prefers earlier rewards,
and models termination probability; alternatives: finite horizon (non-stationary optimal
policies), average reward, absorbing states. Utilities of sequences must be stationary to
justify additive discounted rewards.

## Values and the Bellman equations
- V^π(s) = E[return | start s, follow π] = Σ_s' P(s'|s,π(s))[R(s,π(s),s') + γ V^π(s')] —
  a linear system (**policy evaluation**), solvable in O(S³) or by iteration.
- **Q-values**: Q*(s,a) = Σ_s' P(s'|s,a)[R + γ V*(s')]; V*(s) = max_a Q*(s,a); π*(s) =
  argmax_a Q*(s,a) (**policy extraction** — given Q*, no model needed; given V*, one
  lookahead with the model).
- **Bellman optimality**: V*(s) = max_a Σ_s' P(s'|s,a)[R(s,a,s') + γ V*(s')] — one equation
  per state, nonlinear because of the max; V* is its unique solution. The Bellman operator is
  a **γ-contraction** in max-norm, hence a unique fixed point and geometric convergence
  ([[recurrences]]-style fixed-point reasoning as in [[abstract-interpretation]]).

## Solving MDPs
- **Value iteration**: V₀ = 0; V_{k+1}(s) = max_a Σ P[R + γ V_k(s')] — V_k is the optimal
  k-step value (expectimax to depth k with memoization — [[adversarial-search-and-game-trees]],
  [[dynamic-programming]]); ‖V_{k+1} − V*‖ ≤ γ‖V_k − V*‖; stop when the change is < ε(1−γ)/γ.
  O(S²A) per iteration; the policy usually converges long before the values do; asynchronous
  / prioritized sweeping updates states in useful order.
- **Policy iteration**: alternate **evaluation** (solve V^π exactly or by a few sweeps —
  "modified PI") and **improvement** π'(s) = argmax_a Σ P[R + γ V^π(s')]; each improvement is
  strictly better unless optimal; converges in few iterations (often < 10), each expensive.
  Both are polynomial in S, A, 1/(1−γ); MDPs are also solvable as an LP (min Σ V(s) s.t.
  V ≥ Bellman backups — [[linear-programming-and-duality]]).
- Large state spaces: factored MDPs, function approximation, Monte Carlo planning (MCTS —
  sparse sampling, UCT), real-time DP. Partially observable → **POMDP** (belief-state MDP,
  continuous; exact solution PSPACE-hard; point-based approximations — [[bayesian-networks-and-hmms]]
  for the belief update).

## When the model is unknown: reinforcement learning basics (CS188 L10–11; AIMA ch. 22)
The agent acts, observes (s, a, r, s') samples, and must learn without P or R. **Model-based
RL**: count transitions to estimate P̂ and R̂, then solve the MDP (sample-efficient, needs
exploration to cover states). **Model-free**:
- **Direct evaluation**: average observed returns per state (unbiased, wastes structure).
- **Temporal-difference (TD) learning** of V^π: V(s) ← (1−α)V(s) + α[r + γ V(s')] — an
  exponential moving average of sampled Bellman backups; bootstraps; converges with decaying
  α. Gives V^π but no policy without a model.
- **Q-learning** (Watkins 1989): Q(s,a) ← (1−α)Q(s,a) + α[r + γ max_a' Q(s',a')] —
  **off-policy**: converges to Q* regardless of the behaviour policy provided every (s,a) is
  visited infinitely often and α decays properly; SARSA is the on-policy variant (learns the
  value of the exploring policy — safer near cliffs).
- **Exploration vs exploitation**: ε-greedy (decay ε), **optimistic initialization** /
  exploration functions f(u, n) = u + k/n (bonus for rarely-tried actions);
  [[multi-armed-bandits]] as the one-state case; **regret** measures the cost of learning.
- **Generalization**: tabular Q is hopeless beyond ~10⁶ states; **approximate Q-learning** with
  linear features Q(s,a) = Σ wᵢ fᵢ(s,a), updated by wᵢ ← wᵢ + α·[target − Q]·fᵢ — online least
  squares ([[gradient-descent]]); deep networks as the feature extractor →
  [[deep-reinforcement-learning]]. **Policy search** optimizes π directly (evaluation via
  rollouts; policy gradient) when the value function is hard but the policy is simple.
  Full treatment: [[reinforcement-learning-basics]] (Sutton & Barto).

## Pitfalls
- γ = 1 with an infinite horizon and no terminals (unbounded values, no unique solution).
- Extracting a policy from values without the model (need Q or P).
- Confusing V^π (a fixed policy) with V* (the optimal); evaluating a policy with a max.
- Q-learning with a fixed α (never converges) or with no exploration (locks in).
- Reward shaping that changes the optimal policy (must be potential-based to be safe).

## Related
- [[markov-chains]], [[dynamic-programming]], [[adversarial-search-and-game-trees]]
  (expectimax), [[reinforcement-learning-basics]], [[deep-reinforcement-learning]],
  [[multi-armed-bandits]], [[bayesian-networks-and-hmms]] (POMDP belief tracking),
  [[linear-programming-and-duality]], [[abstract-interpretation]] (fixed points),
  [[gradient-descent]].

## Sources
AIMA 4e ch. 17 and 22; CS188 lectures 8–11 and notes 4.1–4.6, 5.1–5.5; Poole & Mackworth ch. 12–13; Bellman 1957; Howard 1960 (policy iteration); Watkins 1989; Sutton & Barto ch. 3–6.

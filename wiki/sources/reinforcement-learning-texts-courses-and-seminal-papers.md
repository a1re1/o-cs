---
title: Reinforcement learning texts, courses and seminal papers — Sutton & Barto (free), Szepesvári's Algorithms for RL, Lattimore & Szepesvári's Bandit Algorithms; David Silver's UCL/DeepMind course, Berkeley CS285 (Levine), Stanford CS234, OpenAI Spinning Up, Hugging Face Deep RL; Bellman, Sutton TD, Watkins Q-learning, Williams REINFORCE, DQN, AlphaGo/AlphaZero, TRPO/PPO, DDPG, SAC, UCB, inverse RL, Decision Transformer
type: source
section: "6.6"
level: 500
tags: [sutton-barto, reinforcement-learning-an-introduction, szepesvari, algorithms-for-rl, lattimore, bandit-algorithms, david-silver, ucl-rl, cs285, levine, deep-rl-course, cs234, spinning-up, openai, hugging-face-deep-rl, bellman, sutton-td, watkins, q-learning, williams, reinforce, mnih, dqn, silver, alphago, alphazero, schulman, trpo, ppo, lillicrap, ddpg, haarnoja, sac, auer, ucb, ng-russell, inverse-rl, chen, decision-transformer]
sources: []
authors: [Richard Sutton, Andrew Barto, Csaba Szepesvári, Tor Lattimore, David Silver, Sergey Levine, Emma Brunskill, Joshua Achiam, Richard Bellman, Christopher Watkins, Ronald Williams, Volodymyr Mnih, John Schulman, Timothy Lillicrap, Tuomas Haarnoja, Peter Auer, Andrew Ng, Stuart Russell, Lili Chen]
year: 2018
institution: UCL / DeepMind / Berkeley / Stanford / OpenAI
url: http://incompleteideas.net/book/the-book-2nd.html
license: mixed (Sutton & Barto, Szepesvári, Lattimore & Szepesvári, Spinning Up, HF course free)
format: html
summary: Sutton & Barto's Reinforcement Learning: An Introduction (2e 2018, free) is the canon — Part I tabular methods (multi-armed bandits; finite MDPs; dynamic programming; Monte Carlo; temporal-difference learning; n-step bootstrapping; planning and learning with tabular models), Part II approximate methods (on-policy prediction and control with function approximation, off-policy methods and the deadly triad, eligibility traces, policy gradient), Part III frontiers (psychology, neuroscience, applications — TD-Gammon, Watson, AlphaGo) — organized around the tension between bootstrapping, sampling, and function approximation; Szepesvári's short monograph gives the algorithms with convergence statements, Lattimore & Szepesvári is the bandit reference (regret bounds for UCB, Thompson sampling, adversarial and contextual bandits); Silver's ten UCL lectures follow Sutton & Barto to deep RL, CS285 (Levine) is the deep-RL research course (imitation, policy gradients, actor-critic, value methods, model-based, exploration, offline RL, inverse RL, meta-RL), CS234 the Stanford equivalent; OpenAI Spinning Up teaches the concepts (states/observations, action spaces, deterministic/stochastic policies, trajectories, return, value/Q/advantage functions, Bellman equations) then the kinds of algorithms (model-free vs model-based, policy optimization vs Q-learning) with clean implementations of VPG, TRPO, PPO, DDPG, TD3, SAC; and the seminal papers are Bellman's DP (1957), Sutton's TD(λ) (1988), Watkins' Q-learning (1989), Williams' REINFORCE (1992), DQN on Atari (2015), AlphaGo/AlphaZero (2016/17), TRPO and PPO (2015/17), DDPG (2015), SAC (2018), Auer's UCB regret bounds (2002), Ng & Russell's inverse RL (2000), and the Decision Transformer's RL-as-sequence-modelling (2021).
---
# Reinforcement learning: texts, courses, and seminal papers

## What they are
- **Sutton & Barto** (2e 2018; free): 1 introduction; **I tabular** — 2 multi-armed bandits,
  3 finite MDPs, 4 dynamic programming, 5 Monte Carlo methods, 6 temporal-difference
  learning, 7 n-step bootstrapping, 8 planning and learning with tabular methods (Dyna,
  prioritized sweeping, MCTS); **II approximate** — 9 on-policy prediction with approximation,
  10 on-policy control (semi-gradient Sarsa), 11 off-policy methods with approximation (the
  deadly triad), 12 eligibility traces, 13 policy gradient methods; **III looking deeper** —
  14 psychology, 15 neuroscience (dopamine as TD error), 16 applications and case studies
  (TD-Gammon, Samuel's checkers, Watson's wagering, memory control, human-level video
  game play, AlphaGo), 17 frontiers. The unifying picture: every method is a point in the
  space of {bootstrapping depth (MC ↔ TD), sampling (expected ↔ sample updates), on/off-
  policy, tabular ↔ approximate}.
- **Szepesvári, Algorithms for RL** (2010; free, ~100 pp): MDPs, value prediction (TD, LSTD),
  control (Q-learning, actor-critic, policy gradient), with convergence results.
  **Lattimore & Szepesvári, Bandit Algorithms** (2020; free): stochastic bandits (explore-
  then-commit, UCB, KL-UCB, Thompson sampling), lower bounds, adversarial bandits (Exp3),
  contextual and linear bandits (LinUCB), pure exploration, partial monitoring.
- **Courses**: **Silver, UCL RL** (10 lectures, 2015): intro, MDPs, planning by DP, model-free
  prediction, model-free control, value function approximation, policy gradient,
  integrating learning and planning, exploration and exploitation, case study (games).
  **CS285 Deep RL** (Levine; open lectures/homeworks): imitation learning, policy gradients,
  actor-critic, value-based (DQN), advanced policy gradients (TRPO/PPO), model-based RL
  and planning, model-based policy learning, exploration (count-based, curiosity,
  posterior sampling), offline RL (CQL, IQL), inverse RL, RL and language models, transfer/
  meta-RL, open problems. **CS234** (Brunskill): similar with more emphasis on bandits,
  batch RL, and RLHF. **Spinning Up** (Achiam; OpenAI): Part 1 key concepts (below), Part 2
  a taxonomy of algorithms (model-free vs model-based; policy optimization — VPG/A2C/PPO/
  TRPO — vs Q-learning — DQN/C51/QR-DQN/HER — and the middle ground DDPG/TD3/SAC), Part 3
  policy optimization derivations; PyTorch implementations, "key papers in deep RL" list,
  and advice on becoming a researcher. **Hugging Face Deep RL course**: hands-on with
  Stable-Baselines3, gym environments, PPO/DQN/SAC, Unity/MuJoCo.
- **Seminal**: Bellman 1957 (DP, the equation); Sutton 1988 (TD(λ) — learning to predict by
  the method of temporal differences); Watkins 1989 (Q-learning, proven convergent 1992);
  Williams 1992 (**REINFORCE**: the likelihood-ratio policy gradient); Tesauro 1995
  (TD-Gammon — self-play + neural net, the deep-RL prototype); Mnih et al. 2015 (**DQN**:
  experience replay, target networks, Atari from pixels); Silver et al. 2016/2017
  (**AlphaGo**, **AlphaZero**: MCTS + policy/value nets + self-play); Schulman et al. 2015/2017
  (**TRPO** trust regions, **PPO** clipped surrogate — the default on-policy method and the RLHF
  workhorse); Lillicrap et al. 2015 (**DDPG**: DQN for continuous actions); Fujimoto 2018 (TD3);
  Haarnoja et al. 2018 (**SAC**: maximum-entropy off-policy actor-critic — the continuous-
  control default); Auer, Cesa-Bianchi & Fischer 2002 (**UCB1** and its O(log T) regret);
  Thompson 1933; Ng & Russell 2000 (**inverse RL**: infer the reward from behaviour); Levine
  et al. 2020 (offline RL survey); Chen et al. 2021 (**Decision Transformer**: return-conditioned
  sequence modelling replaces value functions); Ouyang et al. 2022 (RLHF — [[llm-post-training-sft-rlhf-dpo]]).

## Key ideas → pages
[[reinforcement-learning-basics]], [[deep-reinforcement-learning]], [[multi-armed-bandits]],
[[markov-decision-processes]] (§6.1 foundation), [[adversarial-search-and-game-trees]] (MCTS),
[[llm-post-training-sft-rlhf-dpo]] (RLHF/PPO/GRPO).

## What they add
Sutton & Barto for the concepts and the unifying dimensions; Spinning Up for the cleanest
derivation of policy gradients and the algorithm taxonomy; CS285 for everything after 2015
(model-based, offline, exploration); Lattimore & Szepesvári for regret bounds; the papers
show two lines converging — value-based (TD → Q-learning → DQN) and policy-based (REINFORCE
→ TRPO/PPO → SAC) — into actor-critic, and RL leaving games for language models.

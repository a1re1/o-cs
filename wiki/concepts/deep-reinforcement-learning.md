---
title: Deep reinforcement learning — DQN (replay, target networks) and its improvements (double, dueling, prioritized replay, distributional, Rainbow), policy gradients (REINFORCE, baselines, advantage, GAE), actor-critic (A2C/A3C), trust regions (TRPO) and PPO's clipped objective, off-policy continuous control (DDPG, TD3, SAC and maximum entropy), model-based RL (Dyna-style, MuZero, Dreamer), exploration (curiosity, RND), offline RL (CQL, IQL), imitation and inverse RL, Decision Transformers, and the practical reproducibility problems
type: concept
section: "6.6"
level: 500
tags: [deep-reinforcement-learning, deep-rl, dqn, experience-replay, target-network, atari, double-dqn, dueling, prioritized-replay, distributional-rl, c51, rainbow, policy-gradient, reinforce, likelihood-ratio, baseline, advantage, gae, actor-critic, a2c, a3c, trpo, trust-region, natural-gradient, ppo, clipped-surrogate, ddpg, td3, sac, maximum-entropy, entropy-bonus, continuous-control, mujoco, model-based-rl, world-models, muzero, dreamer, mbpo, exploration, curiosity, rnd, count-based, offline-rl, batch-rl, cql, iql, distribution-shift, imitation-learning, behavior-cloning, dagger, inverse-rl, gail, decision-transformer, sim-to-real, reward-hacking, reproducibility, spinning-up, cs285]
sources: [reinforcement-learning-texts-courses-and-seminal-papers]
summary: Deep RL replaces tables with neural networks and pays for it with instability, so its algorithms are the stabilization tricks: DQN made Q-learning from pixels work with experience replay (decorrelate samples, reuse data) and a slowly updated target network (a fixed bootstrapping target), improved by double DQN (maximization bias), dueling heads, prioritized replay, distributional value learning and n-step returns (Rainbow); policy-gradient methods optimize the policy directly with the likelihood-ratio gradient ∇J = E[Σ ∇log π(a|s) Â] (REINFORCE, with a learned value baseline giving the advantage and GAE trading bias for variance), which is unbiased, handles continuous actions and stochastic policies, but is on-policy and high-variance; TRPO constrains each update by a KL trust region (natural gradient) and PPO approximates it with a clipped surrogate objective — simple, robust, the default (and the RLHF optimizer); off-policy actor-critics for continuous control learn a Q-function and a policy that maximizes it (DDPG, TD3's twin critics and delayed updates, SAC's maximum-entropy objective with an entropy bonus and automatic temperature — the sample-efficient default for robotics); model-based methods learn dynamics and plan or imagine (MuZero's learned latent model with MCTS, Dreamer's world models, MBPO's short model rollouts), exploration bonuses (counts, curiosity/prediction error, RND) attack sparse rewards, offline RL learns from fixed datasets by penalizing out-of-distribution actions (CQL, IQL), imitation and inverse RL learn from demonstrations (behaviour cloning, DAgger, GAIL), and Decision Transformers recast control as return-conditioned sequence modelling — with the honest caveats that results vary wildly across seeds, hyperparameters and implementation details, rewards get hacked, and sim-to-real transfer is the hard part.
---
# Deep reinforcement learning

**In one sentence.** Put a neural network where the table was, then add the machinery
that keeps bootstrapped, off-policy, approximate learning from diverging — replay buffers
and target networks on the value side, trust regions and clipping on the policy side, and
entropy, models, and exploration bonuses to find good data at all.

## Value-based: DQN and Rainbow (Mnih et al. 2015; Hessel et al. 2018; CS285 lecture 8)
**DQN**: Q(s, a; θ) as a CNN over 4 stacked frames; loss (r + γ maxₐ′ Q(s′, a′; θ⁻) − Q(s, a; θ))²;
**experience replay** (store transitions, sample minibatches uniformly — breaks correlation,
reuses data, makes it off-policy) and a **target network** θ⁻ copied every C steps (a fixed
regression target — bootstrapping to a moving target is the deadly-triad instability of
[[reinforcement-learning-basics]]); ε-greedy with annealing, reward clipping, Huber loss,
frame skipping; human-level on 29 of 49 Atari games from pixels. Improvements: **Double DQN**
(select with online, evaluate with target — kills maximization bias), **dueling** (V and
advantage streams), **prioritized replay** (sample by |TD error|, importance-weighted),
**n-step** returns, **distributional** RL (C51/QR-DQN predict the return distribution — better
representations), noisy nets for exploration; **Rainbow** combines them. Limits: discrete
actions, sample inefficiency (10⁷–10⁸ frames), overestimation, sensitivity to hyperparameters;
DQN → R2D2/Agent57/MuZero for the Atari frontier. Hindsight experience replay (HER) for
goal-conditioned sparse rewards.

## Policy gradients (Williams 1992; Spinning Up part 3; CS285 lectures 5–6)
Parameterize π_θ(a | s) (softmax over discrete actions, Gaussian for continuous); maximize
J(θ) = E_τ[R(τ)]. **Policy gradient theorem** / likelihood-ratio trick: ∇J = E_τ[Σₜ ∇log π_θ(aₜ | sₜ)
· Gₜ] — no model, no differentiation through the environment; **REINFORCE** samples it.
Variance reduction: **reward-to-go** (only future rewards), a **baseline** b(s) (any state
function keeps the gradient unbiased — use V(s)), giving the **advantage** A = Q − V;
**GAE(λ)** (Schulman 2016): exponentially weighted n-step advantage estimates from a learned
V — the λ of TD(λ) applied to advantages; normalize advantages per batch; entropy bonus for
exploration. **Actor-critic**: the critic V_φ is trained by TD, the actor by the advantage
gradient — **A2C/A3C** (parallel workers instead of replay). Pros: continuous/stochastic
policies, convergence to a local optimum, works with partial observability; cons: on-policy
(each batch used once), high variance, step-size sensitivity (a bad step collapses the
policy and the data it generates).

## Trust regions and PPO (Schulman et al. 2015, 2017)
Large policy steps are catastrophic because the *data distribution* changes with the policy.
**TRPO**: maximize the surrogate E[π_θ/π_old · Â] subject to KL(π_old ‖ π_θ) ≤ δ — a natural-
gradient step (Fisher-metric — [[gradient-descent]]) with conjugate gradient and line search;
monotonic improvement guarantee (Kakade & Langford). **PPO** keeps the idea, drops the
machinery: maximize E[min(ρ Â, clip(ρ, 1−ε, 1+ε) Â)] with ρ = π_θ/π_old, ε = 0.2 — the clip
removes the incentive to move ρ outside the interval; several epochs of minibatch SGD per
batch; plus value loss, entropy bonus, GAE, advantage normalization, and (important, often
undocumented) implementation details (value clipping, orthogonal init, LR annealing —
"the 37 implementation details"). PPO is the default for anything on-policy, from MuJoCo
locomotion to Dota 2, robot hands, and **RLHF** for LLMs (with a KL penalty to the reference
— [[llm-post-training-sft-rlhf-dpo]]; GRPO is PPO without a critic).

## Off-policy actor-critic for continuous control (Lillicrap 2015; Fujimoto 2018; Haarnoja 2018)
**DDPG**: deterministic policy μ_θ(s) trained by ∇ₐQ(s, a)|ₐ₌μ(s) ∇_θ μ (the deterministic
policy gradient), Q by DQN-style replay + target networks, Gaussian/OU noise for
exploration — sample-efficient, brittle. **TD3**: twin critics (take the min — fights
overestimation), delayed policy updates, target policy smoothing. **SAC**: maximum-entropy
RL — maximize E[Σ r + α H(π(· | s))]: stochastic Gaussian policy (reparameterized), soft Q
targets include the entropy term, **automatic temperature** α tuning to a target entropy;
robust, exploratory, the go-to for robotics and simulated control (MuJoCo benchmarks:
HalfCheetah, Humanoid); entropy regularization also explains why RL policies should stay
stochastic during training ([[markov-decision-processes]] with an entropy bonus is the same
KL-regularized objective as in RLHF).

## Model-based RL, exploration, and offline RL (CS285 lectures 11–13, 14–16)
**Model-based**: learn p(s′ | s, a) (ensembles for uncertainty), then plan (MPC with CEM/
random shooting; PETS), or generate short rollouts to train a model-free learner (**MBPO**,
Dyna-style — [[reinforcement-learning-basics]]), or learn a **latent world model** and train
the policy in imagination (**Dreamer** v1–v3; PlaNet); **MuZero** learns a latent model whose
only requirement is predicting reward, value, and policy, and plans with MCTS — Atari, Go,
chess, shogi from scratch ([[adversarial-search-and-game-trees]]). 10–100× more sample-
efficient; model exploitation (the policy finds model errors) is the failure mode.
**Exploration**: ε-greedy fails on sparse rewards (Montezuma's Revenge); bonuses from
pseudo-counts, **curiosity** (prediction error of a forward model — ICM), **RND** (error of
predicting a random network's features — novelty), Go-Explore (archive + return-to-state),
posterior sampling/bootstrapped DQN (Thompson-style — [[multi-armed-bandits]]), information
gain. **Offline (batch) RL**: learn from a fixed dataset with no interaction (healthcare,
logged robot data): naive off-policy methods fail from **distribution shift** (the Q-function
is queried at actions never seen, overestimates, the policy exploits it); **CQL** penalizes
Q on OOD actions, **IQL** avoids querying OOD actions via expectile regression, BCQ/TD3+BC
constrain to the data; off-policy evaluation (importance sampling, FQE). Related: imitation
— **behaviour cloning** (supervised, suffers compounding error), **DAgger** (query the expert
on the learner's states), **inverse RL** (Ng & Russell 2000: recover a reward under which
demonstrations are optimal; max-entropy IRL; **GAIL** — adversarial imitation, the GAN of
RL — [[deep-generative-models]]); **Decision Transformer** (Chen et al. 2021): condition a
causal transformer on (return-to-go, state, action) tokens and ask for a high return — RL as
sequence modelling, no Bellman backups ([[transformers-and-attention]]).

## Practice and caveats (Henderson et al. 2018; Spinning Up "research")
Results depend on seeds (report ≥ 5–10 with CIs), hyperparameters, network sizes, reward
scaling, observation normalization, frame stacking, and code-level details; benchmarks
(Atari, MuJoCo/DM Control, Procgen, Minecraft) saturate or leak; **reward hacking**
(specification gaming: the boat racing in circles) is the norm not the exception
([[ai-safety-and-alignment]]); **sim-to-real** needs domain randomization, system ID, or real
fine-tuning ([[robotics-and-autonomous-systems]]); sample efficiency remains orders of
magnitude below humans; the field's largest recent impact is RLHF/RLVR on language models
([[llm-post-training-sft-rlhf-dpo]]) and games (AlphaStar, OpenAI Five, GT Sophy), plus
chip placement, data-centre cooling, and nuclear-fusion control.

## Pitfalls
- No target network / no replay in DQN; replaying on-policy PPO data more than a few epochs.
- Un-normalized advantages or rewards; a value function that never converges (check
  explained variance).
- PPO clip without the min (clipping alone doesn't bound the objective).
- Deterministic policies evaluated without exploration noise removed; SAC with a fixed α.
- Offline RL with vanilla Q-learning (OOD overestimation); trusting a model beyond its
  data.
- One seed, one environment, one number.

## Related
- [[reinforcement-learning-basics]], [[markov-decision-processes]], [[multi-armed-bandits]],
  [[adversarial-search-and-game-trees]] (MCTS, AlphaZero), [[neural-network-training]],
  [[gradient-descent]] (natural gradient), [[llm-post-training-sft-rlhf-dpo]],
  [[transformers-and-attention]], [[deep-generative-models]] (GAIL),
  [[robotics-and-autonomous-systems]], [[ai-safety-and-alignment]], [[game-theory]]
  (multi-agent RL).

## Sources
Mnih et al. 2015; Hessel et al. 2018 (Rainbow); Williams 1992; Schulman et al. 2015 (TRPO), 2016 (GAE), 2017 (PPO); Lillicrap et al. 2015; Fujimoto et al. 2018; Haarnoja et al. 2018; Schrittwieser et al. 2020 (MuZero); Hafner et al. 2019–23 (Dreamer); Burda et al. 2018 (RND); Kumar et al. 2020 (CQL); Kostrikov et al. 2021 (IQL); Ross et al. 2011 (DAgger); Ho & Ermon 2016 (GAIL); Chen et al. 2021; Henderson et al. 2018; Spinning Up parts 2–3 (ToC read); CS285 lectures 5–16 (site read).

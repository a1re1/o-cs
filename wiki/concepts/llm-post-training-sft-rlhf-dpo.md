---
title: LLM post-training — supervised fine-tuning / instruction tuning, RLHF (reward models from pairwise preferences, PPO with a KL penalty to the reference policy, reward hacking), DPO and its variants, Constitutional AI and RLAIF, parameter-efficient fine-tuning (LoRA, QLoRA, adapters), reasoning models trained with RL on verifiable rewards (GRPO, o1/R1), distillation, and the alignment trade-offs (helpful/harmless/honest, sycophancy, over-refusal)
type: concept
section: "6.4"
level: 500
tags: [post-training, fine-tuning, sft, supervised-fine-tuning, instruction-tuning, flan, alpaca, chat-template, rlhf, reward-model, bradley-terry, preference-data, pairwise-comparison, ppo, kl-penalty, reference-policy, reward-hacking, goodhart, dpo, direct-preference-optimization, ipo, kto, rlaif, constitutional-ai, critique-revision, lora, qlora, peft, adapters, prefix-tuning, catastrophic-forgetting, reasoning-models, rlvr, verifiable-rewards, grpo, o1, deepseek-r1, chain-of-thought-rl, process-reward, outcome-reward, self-play, distillation, model-merging, helpful-harmless-honest, sycophancy, over-refusal, alignment-tax, red-teaming, jailbreaks]
sources: [nlp-and-llm-courses-texts-and-seminal-papers]
summary: A pretrained LLM predicts text; post-training turns it into an assistant in stages — supervised fine-tuning on instruction–response demonstrations (FLAN, Alpaca; a chat template with roles) teaches the format and basic helpfulness, then reinforcement learning from human feedback (Ouyang et al. 2022, InstructGPT) fits a reward model to pairwise human preferences (Bradley–Terry likelihood) and optimizes the policy with PPO against that reward minus a KL penalty to the SFT reference (which prevents reward hacking of an imperfect reward model and keeps the language distribution intact — Goodhart's law is the central hazard), which DPO (Rafailov et al. 2023) collapses into a closed-form classification loss on preference pairs with no reward model or RL loop (the reward is implicit in the log-ratio to the reference), Constitutional AI/RLAIF replace human raters with model critiques guided by written principles, and parameter-efficient methods (LoRA: train low-rank updates ΔW = BA on frozen weights; QLoRA on 4-bit bases) make fine-tuning feasible on one GPU; since 2024 reasoning models (o1, DeepSeek-R1) are trained by RL on verifiable rewards (math answers, unit tests) with GRPO-style group-relative advantages, learning long chains of thought, self-verification and backtracking, then distilled into smaller models — and every stage trades helpfulness against harmlessness and honesty, with sycophancy, over-refusal, and jailbreak robustness as the measured side effects.
---
# LLM post-training: SFT, RLHF, DPO, and reasoning RL

**In one sentence.** Pretraining gives you a model that continues text; SFT shows it the
assistant format, preference optimization (RLHF/DPO) moves it toward answers people prefer
while a KL leash keeps it from gaming the judge, and RL on verifiable rewards teaches it
to think longer — each step a lever on helpful-vs-harmless-vs-honest.

## Supervised fine-tuning / instruction tuning (Wei et al. 2021 FLAN; Taori et al. 2023 Alpaca)
Continue training the base model on (instruction, response) pairs formatted with a **chat
template** (system/user/assistant roles, special tokens), loss on the response tokens only.
Data: human-written demonstrations (InstructGPT's ~13k), academic task collections (FLAN:
1.8k tasks → zero-shot generalization to unseen tasks), self-instruct/synthetic data from
stronger models (Alpaca: 52k from GPT-3.5 — and the licensing/distillation debates), and
curated small sets (LIMA: 1k high-quality examples suffice for format; "superficial
alignment hypothesis"). Teaches style, format, refusal templates, tool-call syntax; does
not reliably teach *preferences* between plausible answers — SFT can only imitate. Risks:
**catastrophic forgetting** of pretraining knowledge (mix in pretraining data, lower LR),
overfitting to raters' style, and learning to hallucinate when demonstrations assert facts
the model doesn't know (so demonstrations should be conditioned on the model's knowledge).

## RLHF (Christiano et al. 2017; Ouyang et al. 2022; Bai et al. 2022)
1. Collect **comparisons**: for a prompt, sample two responses, a rater picks the better.
2. Train a **reward model** r_φ(x, y) (a copy of the LM with a scalar head) with the
   **Bradley–Terry** loss −log σ(r(x, y_w) − r(x, y_l)) ([[linear-models-logistic-regression-and-glms]]).
3. Optimize the policy π_θ with **PPO** ([[deep-reinforcement-learning]]) to maximize
   E[r_φ(x, y)] − β·KL(π_θ(y | x) ‖ π_ref(y | x)), where π_ref is the SFT model: the KL term
   keeps outputs in-distribution for the reward model (which is only accurate near the data
   it was trained on) and prevents mode collapse/degenerate text; value model, GAE,
   clipped objective, per-token KL as reward shaping; four models in memory.
Results (InstructGPT): a 1.3 B RLHF model preferred over 175 B GPT-3; big gains in
instruction following, truthfulness, and harmlessness. Hazards: **reward hacking**
(Goodhart — the policy finds outputs the reward model over-scores: verbosity, lists,
confident tone, flattery → **sycophancy**), rater disagreement and bias, **over-optimization**
(gold reward falls as proxy reward rises — Gao et al. 2022 scaling laws for RM
overoptimization), and the **alignment tax** on capabilities (mitigated by mixing
pretraining gradients). Anthropic's **HH-RLHF** (helpful and harmless) and **Constitutional
AI** (Bai et al. 2022): the model critiques and revises its own outputs against a written
constitution (SL phase), then preference labels come from the model (**RLAIF**) — scalable,
transparent principles, fewer human labels on harmful content.

## DPO and the preference-optimization family (Rafailov et al. 2023)
The KL-regularized RL objective has a closed-form optimum π*(y | x) ∝ π_ref(y | x) exp(r(x, y)/β),
so r(x, y) = β log[π*(y | x)/π_ref(y | x)] + const — the reward is *implicit* in the policy.
Substituting into Bradley–Terry gives the **DPO loss**:
−log σ(β [log π_θ(y_w | x)/π_ref(y_w | x) − log π_θ(y_l | x)/π_ref(y_l | x)]) — a classification
loss on preference pairs, trained like SFT, no reward model, no sampling, no PPO. Simpler
and stabler; used by Zephyr, Llama 3 (with rejection sampling and iterative rounds),
Tülu. Caveats: optimizes offline data (no exploration — on-policy sampling + a judge, or
iterative/online DPO, closes the gap); can over-reduce the probability of *both* responses;
variants IPO (bounded), KTO (unpaired thumbs-up/down), ORPO (no reference), SimPO
(length-normalized, reference-free), and RLOO/GRPO as cheaper on-policy RL. Rejection
sampling fine-tuning (best-of-n by a reward model, then SFT) is the simple strong baseline.

## Parameter-efficient fine-tuning (Hu et al. 2021 LoRA; Dettmers et al. 2023 QLoRA)
Full fine-tuning of a 70 B model needs ~1 TB of optimizer state ([[neural-network-training]]).
**LoRA**: freeze W ∈ ℝ^{d×k}; learn ΔW = BA with B ∈ ℝ^{d×r}, A ∈ ℝ^{r×k}, r = 8–64 — 0.1–1 % of
the parameters, no inference latency once merged, swappable adapters per task/customer;
apply to attention (and MLP) projections; hypothesis: fine-tuning updates have low
intrinsic rank. **QLoRA**: 4-bit NF4 base weights + paged optimizers + LoRA → 65 B fine-tuning
on one 48 GB GPU. Adapters, prefix/prompt tuning, (IA)³ are alternatives; LoRA ≈ full
fine-tuning for style/format tasks, somewhat worse for learning lots of new knowledge
(continued pretraining is for that — [[transfer-learning-and-fine-tuning]]). Model
**merging** (task-vector averaging, TIES/DARE) and **distillation** (train a student on the
teacher's outputs — the route by which frontier behaviours reach small open models).

## Reasoning models: RL on verifiable rewards (2024–25; CS336 assignment 5)
Instead of a learned reward model, use tasks with **checkable answers** — math (final answer
match), code (unit tests), logic — and run RL directly on the base/SFT model with long
chain-of-thought sampling: **GRPO** (DeepSeek): sample G responses per prompt, advantage =
(reward − group mean)/group std, PPO-style clipped update with a KL to the reference, no
value network; **outcome** vs **process** reward models (step-level supervision); the
model learns to allocate more tokens, verify, backtrack ("aha moments" in R1-Zero) —
test-time compute as a trained skill ([[scaling-laws]]). OpenAI **o1** (hidden reasoning),
**DeepSeek-R1** (open recipe: R1-Zero pure RL → cold-start SFT → RL → rejection sampling +
SFT → RL; distilled into Qwen/Llama students matching much larger models). Caveats:
rewards must be hard to hack (test-case overfitting, answer-format exploits), gains
concentrate in verifiable domains, and long reasoning inflates inference cost and can
reduce faithfulness of the visible chain to the actual computation.

## Trade-offs and evaluation ([[ai-safety-and-alignment]])
Helpful vs harmless vs honest (HHH); **over-refusal** (declining benign requests) vs
jailbreaks; sycophancy vs candour; verbosity bias in judges; **red-teaming** and adversarial
training; safety-tuning can be undone by a few fine-tuning steps (fine-tuning attacks) —
open weights complicate this. Measurement: preference win-rates by human/LLM judges (with
length control), refusal/jailbreak benchmarks, honesty/calibration evals, capability
regression suites ([[llm-evaluation-and-benchmarks]]). The engineering reality: post-training
is now most of the differentiation between models of similar pretraining scale.

## Pitfalls
- Training the reward model on out-of-distribution responses and then optimizing hard
  (over-optimization); no KL penalty.
- DPO on stale off-policy pairs and expecting RLHF-level gains; ignoring length bias.
- SFT on demonstrations that contain facts the model can't know (teaches hallucination).
- LoRA for large knowledge injection; merging adapters trained on different bases.
- Verifiable-reward RL with leaky verifiers (models learn the leak).

## Related
- [[large-language-models]], [[scaling-laws]], [[deep-reinforcement-learning]] (PPO),
  [[markov-decision-processes]], [[neural-network-training]],
  [[transfer-learning-and-fine-tuning]], [[llm-evaluation-and-benchmarks]],
  [[ai-safety-and-alignment]], [[linear-models-logistic-regression-and-glms]] (Bradley–Terry),
  [[game-theory]] (preference models), [[interpretability-and-explainability]].

## Sources
Ouyang et al. 2022; Christiano et al. 2017; Bai et al. 2022 (HH-RLHF, Constitutional AI); Rafailov et al. 2023; Hu et al. 2021; Dettmers et al. 2023; Wei et al. 2021 (FLAN); Zhou et al. 2023 (LIMA); Gao et al. 2022; Shao et al. 2024 (GRPO); DeepSeek-AI 2025 (R1); Llama 3 report 2024; CS336 assignment 5 (read); SLP3 2026 alignment chapter (title read).

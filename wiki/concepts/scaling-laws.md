---
title: Scaling laws — power-law loss vs parameters, data and compute (Kaplan 2020), compute-optimal training and the Chinchilla correction (~20 tokens per parameter), the 6ND FLOP rule, sample efficiency of large models, emergent abilities and their measurement, data constraints and overtraining for inference, and test-time compute scaling
type: concept
section: "6.4"
level: 500
tags: [scaling-laws, power-law, kaplan, chinchilla, hoffmann, compute-optimal, tokens-per-parameter, 6nd, flops, training-compute, model-size, dataset-size, sample-efficiency, loss-curves, irreducible-loss, emergent-abilities, emergence, metrics, mirage, overtraining, inference-cost, data-constraints, epochs, repeated-data, mixture-of-experts, scaling-hypothesis, bitter-lesson, test-time-compute, inference-scaling, reasoning-models, mup, hyperparameter-transfer, extrapolation, scaling-experiments]
sources: [nlp-and-llm-courses-texts-and-seminal-papers]
summary: Kaplan et al. (2020) found that language-model cross-entropy loss falls as a smooth power law in each of model parameters N, dataset tokens D and training compute C over seven orders of magnitude — L(N) ∝ N^{−0.076}, L(D) ∝ D^{−0.095}, L(C) ∝ C^{−0.05} — with architecture details mattering little, larger models being more sample-efficient, and a fixed compute budget best spent on big models trained briefly; Hoffmann et al. (2022, Chinchilla) redid the sweep with tuned learning-rate schedules and found the compute-optimal frontier scales N and D equally (≈ 20 tokens per parameter), so a 70 B model on 1.4 T tokens beats a 280 B Gopher on 300 B — which is why later open models (LLaMA, Llama 3, Qwen) are "overtrained" far past Chinchilla-optimal because inference cost, not training cost, dominates deployment; the FLOP accounting is C ≈ 6ND (forward + backward, 2 + 4 FLOPs per parameter per token), which lets you budget runs on a napkin; scaling laws hold for downstream loss but "emergent abilities" that appear suddenly at scale are partly artefacts of discontinuous metrics (exact match) and become smooth under continuous ones; hyperparameters transfer across widths with µP; data is the coming constraint (repeating tokens works for ~4 epochs then decays; synthetic data, curation and MoE stretch it); and since 2024 a second axis — test-time compute, spending more inference tokens on reasoning, search or verification — has its own scaling curves that trade against pretraining scale.
---
# Scaling laws

**In one sentence.** Loss is a power law in parameters, data, and compute — smooth enough to
extrapolate a large run from small ones — and the only real debates are the exponents
(how to split compute between N and D), which capabilities are truly discontinuous, and
how to trade training compute for inference-time compute.

## Kaplan et al. 2020 (abstract read)
"The loss scales as a power-law with model size, dataset size, and the amount of compute
used for training, with some trends spanning more than seven orders of magnitude. Other
architectural details such as network width or depth have minimal effects within a wide
range. … Larger models are significantly more sample-efficient, such that optimally
compute-efficient training involves training very large models on a relatively modest
amount of data and stopping significantly before convergence." Fits (non-embedding
parameters N, tokens D, PF-days C): L(N) = (N_c/N)^{0.076}, L(D) = (D_c/D)^{0.095}, L(C_min) =
(C_c/C)^{0.050}; a joint L(N, D) form predicts **overfitting** when D grows slower than
N^{0.74}; training curves are predictable early; the optimal allocation put most of the
budget into N (D ∝ N^{0.27} — later revised). Consequences accepted immediately: GPT-3 (175 B
on 300 B tokens), the "scaling hypothesis", and the abandonment of architecture search in
favour of scale ([[transformers-and-attention]]).

## Chinchilla: compute-optimal training (Hoffmann et al. 2022)
Three methods (fixed-N loss curves, IsoFLOP profiles, parametric fit L(N, D) = E + A/N^α +
B/D^β) agree: for a fixed compute budget, **N and D should scale equally** — N_opt ∝ C^{0.5},
D_opt ∝ C^{0.5}, roughly **D ≈ 20 N** tokens. Kaplan's fits were skewed by learning-rate
schedules not matched to run length and by counting embedding parameters. Chinchilla (70 B,
1.4 T tokens) outperformed Gopher (280 B, 300 B tokens) at the same compute — most 2020–22
models were **undertrained**. The fitted form gives an **irreducible loss** E (entropy of
text) and separable N and D terms — the finite-model and finite-data penalties add.

## FLOP accounting and inference (CS336 assignment 3; Sardana & Frankle 2023)
Training compute **C ≈ 6·N·D** FLOPs (2 per parameter per token forward — one multiply and
one add — and 4 backward), plus attention's 2·T·d per layer per token (negligible unless T
is huge). Example: 70 B × 15 T tokens ≈ 6.3 × 10²⁴ FLOPs; at 40 % utilization of an H100
(~10¹⁵ FLOP/s bf16) that is ~1.6 × 10¹⁰ GPU-seconds ≈ 5,000 GPUs for ~37 days
([[distributed-training-and-ml-systems]], [[roofline-model]]). Inference costs ~2N FLOPs per
token *forever*, so the deployment-optimal model is **smaller and trained on far more data**
than Chinchilla-optimal — LLaMA-1 (7 B on 1 T), Llama 3 (8 B on 15 T = 1,900 tokens/param),
and small models keep improving past "optimal" because the loss curve in D is still
falling; the trade-off is a curve, not a point. **Mixture-of-experts** decouples parameters
from per-token FLOPs (sparse scaling laws), and **quantization/distillation** shift the
inference side ([[large-language-models]]).

## Emergence, metrics, and downstream transfer (Wei et al. 2022; Schaeffer et al. 2023)
**Emergent abilities**: capabilities (arithmetic, multi-step reasoning, word unscrambling)
that are near zero for small models and jump at some scale — the argument that scaling
buys qualitatively new behaviour, and the reason for capability-forecasting anxiety
([[ai-safety-and-alignment]]). Schaeffer et al.: many "emergences" are artefacts of
**discontinuous metrics** (exact match on a 5-digit answer needs all 5 tokens right — the
per-token probability improves smoothly); under continuous metrics (token edit distance,
log-likelihood) the curves are smooth. Both are right: the loss is smooth, but thresholded
*usefulness* can be sudden. Downstream benchmark performance is predictable from loss only
imperfectly (inverse scaling exists for some tasks); **compute-loss-capability** links are the
subject of [[llm-evaluation-and-benchmarks]]. Scaling holds beyond text (vision, speech,
protein LMs, RL) with different exponents.

## Practice: extrapolating, transferring hyperparameters, and data limits
Fit laws on a sweep of small models (≥ 5 sizes over 2+ orders of magnitude; hold the
recipe fixed; use the correct schedule for each run length — cosine to the end, or WSD);
predict the big run's loss, batch size (critical batch size grows with training —
[[neural-network-training]]), and learning rate; **µP (maximal update parameterization)**
makes the optimal learning rate constant across width so it can be tuned on a small proxy
(Yang et al. 2022) — used for GPT-4 predictions. **Data**: public high-quality text is
~10¹³–10¹⁴ tokens; Muennighoff et al. 2023 — repeating data up to ~4 epochs is nearly free,
beyond that returns decay; curation (dedup, quality filters, mixing) is now the highest-
leverage lever (CS336 assignment 4); synthetic data helps for math/code where verifiable.
The **bitter lesson** (Sutton 2019) reframed: general methods + compute win, and scaling laws
are its quantitative form ([[intelligent-agents-and-ai-history]]).

## Test-time compute (2024–25)
A second axis: let the model spend more tokens *at inference* — chain-of-thought, sampling
many solutions with a verifier or majority vote, tree search, and models trained by RL to
reason at length (OpenAI o1, DeepSeek-R1 — [[llm-post-training-sft-rlhf-dpo]]). Snell et al.
2024: for a fixed FLOP budget, adaptive test-time compute can beat a 14× larger model on
easier problems; the frontier is a trade-off between pretraining scale and inference
scale, with its own (steeper, task-dependent) curves — and inference cost per query
becomes variable, changing the economics of serving ([[llm-inference-and-serving]]).

## Pitfalls
- Extrapolating with a schedule mismatched to run length (Kaplan's error).
- Reading "loss is smooth" as "capabilities are smooth", or the reverse.
- Chinchilla-optimal training for a model that will be served at scale (overtrain
  instead).
- Ignoring data repetition and contamination when counting tokens; comparing runs with
  different tokenizers.
- Treating the exponents as universal constants (they depend on data, architecture,
  tokenizer).

## Related
- [[large-language-models]], [[transformers-and-attention]], [[neural-network-training]],
  [[distributed-training-and-ml-systems]], [[roofline-model]],
  [[llm-post-training-sft-rlhf-dpo]], [[llm-evaluation-and-benchmarks]],
  [[llm-inference-and-serving]], [[ai-safety-and-alignment]],
  [[generalization-bias-variance-and-regularization]] (double descent),
  [[intelligent-agents-and-ai-history]] (bitter lesson).

## Sources
Kaplan et al. 2020 (abstract read); Hoffmann et al. 2022; Wei et al. 2022 (emergence); Schaeffer et al. 2023; Muennighoff et al. 2023; Yang et al. 2022 (µP); Sardana & Frankle 2023; Snell et al. 2024; CS336 assignment 3 (read); CS324 scaling-laws notes.

---
title: Interpretability and explainability — intrinsically interpretable models (linear/GAMs/trees/rules), model-agnostic post-hoc methods (permutation importance, PDP/ICE/ALE, global surrogates, LIME, Shapley values and SHAP, counterfactual explanations, anchors), neural-network attribution (saliency, integrated gradients, Grad-CAM, feature visualization, TCAV), their failure modes (unfaithfulness, instability, adversarial manipulation), probing and representation analysis, mechanistic interpretability (circuits, induction heads, superposition, sparse autoencoders and monosemantic features, activation patching), and the uses — debugging, science, safety, regulation
type: concept
section: "6.11"
level: 500
tags: [interpretability, explainability, xai, interpretable-models, gam, rule-lists, model-agnostic, permutation-importance, partial-dependence, pdp, ice, ale, global-surrogate, lime, local-surrogate, shapley-values, shap, kernel-shap, tree-shap, counterfactual-explanations, anchors, saliency, gradient-attribution, integrated-gradients, grad-cam, feature-visualization, deep-dream, tcav, concept-activation, faithfulness, sanity-checks, attribution-instability, adversarial-explanations, probing, linear-probes, representation-similarity, mechanistic-interpretability, circuits, induction-heads, attention-heads, residual-stream, superposition, polysemanticity, sparse-autoencoders, monosemanticity, dictionary-learning, activation-patching, causal-tracing, logit-lens, features, steering, molnar, olah, anthropic, right-to-explanation]
sources: [ai-safety-fairness-and-interpretability-texts-courses-and-seminal-papers]
summary: Interpretability asks what a model has learned and why it produced an output, for debugging, scientific discovery, trust, safety and legal accountability; the options are to use models that are interpretable by construction (linear models, GAMs, small trees, rule lists — often competitive on tabular data and the honest default when stakes are high), or to explain black boxes post hoc: model-agnostic methods perturb inputs — permutation importance (global; misleading under correlated features), partial-dependence and ICE/ALE plots (marginal effects), global surrogate models, LIME (fit a sparse linear model to the black box around one instance on perturbed samples — intuitive, unstable across seeds and kernel widths), Shapley values (the unique attribution satisfying efficiency, symmetry, dummy and additivity from cooperative game theory, approximated by KernelSHAP and computed exactly for trees by TreeSHAP), counterfactual explanations (the smallest change that flips the decision — the form regulation and users actually want) and anchors (sufficient-condition rules); neural methods use gradients (saliency, integrated gradients along a baseline path, Grad-CAM on convolutional feature maps) or optimization (feature visualization) and concept probes (TCAV), but sanity checks show many saliency maps barely depend on the trained weights, attributions can be manipulated adversarially, and explanations are generally not faithful to the computation; probing classifiers and representation-similarity measures test what information is linearly present in activations; and mechanistic interpretability tries to reverse-engineer the actual algorithm — circuits of neurons/heads (curve detectors, induction heads that implement in-context copying), the residual-stream view of transformers, superposition (models pack more features than dimensions, making neurons polysemantic), sparse autoencoders that decompose activations into interpretable monosemantic features (scaled to production models — the Golden Gate Bridge feature), activation patching/causal tracing to locate where a behaviour is computed, and feature steering — with safety (detecting deception, hidden objectives) as the motivating application and faithfulness/scalability as the open problems.
---
# Interpretability and explainability

**In one sentence.** You can explain a model's outputs (attributions, counterfactuals),
explain its representations (probes, features), or explain its algorithm (circuits) — and
the field's hard-won lesson is that the first is easy to produce and hard to trust, the
last is trustworthy and hard to produce.

## Why, for whom, and the interpretable-by-design option (Molnar ch. 2–5; Rudin 2019)
Goals: **debugging** (is the model using the watermark, the hospital tag, the background?
— Clever Hans), **science** (what did it discover?), **trust and actionability** (what would
change the decision?), **fairness auditing** ([[fairness-in-machine-learning]]), **safety**
([[ai-safety-and-alignment]]), **regulation** (GDPR's "meaningful information about the logic",
adverse-action notices in credit). Taxonomy: intrinsic vs post hoc; global vs local;
model-specific vs agnostic; explanation types (feature summaries, examples, internals,
surrogates). **Interpretable models**: linear/logistic regression (coefficients — but
interactions and correlated features confuse), **GAMs** (f(x) = Σ fⱼ(xⱼ): each feature's
shape function plotted; EBMs/GA²Ms are competitive with boosted trees on tabular data),
small decision trees and **rule lists**/scoring systems (CORELS, RiskSLIM — optimal, sparse),
k-NN prototypes. Rudin's argument: for high-stakes decisions, don't explain a black box —
build an interpretable model; the accuracy gap on tabular data is usually small
([[decision-trees-and-ensembles]], [[linear-models-logistic-regression-and-glms]]).

## Model-agnostic post-hoc methods (Molnar ch. 8–9; Ribeiro 2016; Lundberg & Lee 2017)
- **Permutation feature importance**: loss increase when a feature is shuffled — global,
  cheap; under correlated features it creates unrealistic inputs and splits importance;
  use conditional variants or grouped features.
- **Partial dependence plots** (average prediction as one feature varies), **ICE** (per-
  instance curves — reveal heterogeneity PDP averages away), **ALE** (accumulated local
  effects — correct under correlation; the recommended global effect plot).
- **Global surrogates**: fit an interpretable model to the black box's predictions; check R².
- **LIME**: sample perturbations around x, weight by proximity (kernel), fit a sparse linear
  model on interpretable features (super-pixels, words) — local, any model; **unstable**
  (different seeds/kernel widths give different explanations), sampling is off-manifold,
  and it can be **gamed** (Slack et al. 2020: a classifier that discriminates but looks fair
  to LIME/SHAP by detecting perturbed inputs).
- **Shapley values**: attribute the prediction f(x) − E[f] to features as the average
  marginal contribution over all orderings — unique under efficiency, symmetry, dummy,
  additivity axioms ([[game-theory]]); exponential in features → **KernelSHAP** (weighted
  linear regression on coalitions), **TreeSHAP** (exact, polynomial for tree ensembles),
  DeepSHAP; global summaries (mean |SHAP|, dependence plots); caveats: which baseline/
  "absent feature" distribution (interventional vs observational — correlated features
  again), values are attributions not causal effects, and they can be manipulated too.
- **Counterfactual explanations** (Wachter et al. 2017): the nearest x′ with a different
  prediction ("you'd be approved with $5k less debt") — actionable, contrastive, needs
  plausibility/actionability constraints (DiCE); recourse as the fairness-adjacent
  question ([[causal-inference]] for real counterfactuals vs model counterfactuals).
- **Anchors**: if-then rules that suffice for the prediction with high precision locally.
- **Example-based**: prototypes/criticisms, influential training instances (influence
  functions — [[statistical-learning-theory]] stability), nearest neighbours.

## Neural-network attribution and its sanity checks (Molnar ch. 10; Adebayo et al. 2018)
**Saliency** ∂f/∂x (noisy; SmoothGrad averages over noise), **gradient × input**, **integrated
gradients** (path integral of gradients from a baseline — satisfies completeness; baseline
choice matters), **Grad-CAM** (weight conv feature maps by pooled gradients — coarse
localization), occlusion, LRP/DeepLIFT. **Sanity checks** (Adebayo et al.): several methods
produce nearly identical maps for a trained and a randomly initialized network — they act
as edge detectors, not explanations; attributions can be shifted arbitrarily by
imperceptible perturbations (Ghorbani et al.) and disagree with each other (the
"disagreement problem"). **Feature visualization** (optimize an input to maximize a
neuron/channel with regularization — DeepDream lineage; Olah et al. 2017) shows what
units respond to; **TCAV** tests whether a human concept (stripes) has a directional
influence on a class (zebra) via concept activation vectors. **Attention weights** are not
explanations in general ([[transformers-and-attention]]). Faithfulness metrics (deletion/
insertion curves, ROAR retraining) are how to evaluate any attribution.

## Probing and representations (Belinkov & Glass 2019; Kornblith et al. 2019)
**Linear probes**: train a classifier from a layer's activations to a property (POS,
syntax tree depth, truth of a statement, board state in Othello-GPT) — evidence the
information is linearly present, not that the model uses it (control tasks, minimum-
description-length probing); causal probes intervene on the representation. **Representation
similarity** (CKA, SVCCA) compares layers/models; the **linear representation hypothesis**
(concepts as directions — word2vec's analogies to LLM features — [[nlp-fundamentals]]);
**logit lens**/tuned lens (decode intermediate residual states to vocabulary) to watch a
prediction form layer by layer; emergent world models (Othello, chess, maps of space and
time in LLMs).

## Mechanistic interpretability (Olah et al. 2020; Elhage et al. 2021, 2022; Bricken 2023; Templeton 2024)
Goal: reverse-engineer the algorithm the weights implement. **Circuits** in vision models
(curve detectors → curve families → shape features; universality across models);
**transformer circuits**: the **residual stream** as a shared communication channel that
attention heads and MLPs read from and write to; **induction heads** — a two-head circuit
(previous-token head + copy head) implementing "[A][B] … [A] → [B]" that appears in a phase
change during training and underlies in-context learning; QK/OV decomposition of heads.
**Superposition** (toy models): with more features than dimensions and sparse features,
networks store features as nearly-orthogonal directions, so single neurons are
**polysemantic** — the obstacle to neuron-level interpretation. **Sparse autoencoders /
dictionary learning**: train an overcomplete sparse encoder on activations to recover
**monosemantic features** — thousands in a one-layer model (Bricken et al.), millions in
Claude 3 Sonnet (Templeton et al.: features for the Golden Gate Bridge, code bugs,
sycophancy, deception-related concepts; clamping a feature **steers** behaviour — "Golden
Gate Claude"); feature splitting with dictionary size, and the open questions of
completeness and faithfulness. **Activation patching / causal tracing** (Meng et al. 2022
ROME): replace activations from a corrupted run with clean ones to localize where a fact
or behaviour is computed (factual recall in mid-layer MLPs); **attribution graphs**/
circuit tracing on production models (2025) that show multi-step reasoning, planning in
poems, and unfaithful chain-of-thought; **model editing** as the intervention test.
Uses for safety: detect deception or hidden goals from internals, audit for dangerous
knowledge, monitor features at inference; limits: scale (billions of features), the
interpretation step is still human, and "explanation" of a circuit is not a guarantee of
behaviour outside the studied distribution ([[ai-safety-and-alignment]]).

## Pitfalls
- Trusting a saliency map that fails the randomization sanity check; reading attention
  as explanation.
- SHAP/LIME on correlated features without saying which baseline distribution was used.
- Presenting an unstable local explanation as "the reason".
- Probing accuracy read as "the model uses this"; features from an SAE read as complete.
- Explaining a black box when an interpretable model would do (Rudin).
- Explanations as compliance theatre — no faithfulness evaluation, no user study.

## Related
- [[fairness-in-machine-learning]], [[ai-safety-and-alignment]], [[causal-inference]]
  (counterfactuals, interventions), [[game-theory]] (Shapley), [[decision-trees-and-ensembles]],
  [[linear-models-logistic-regression-and-glms]], [[transformers-and-attention]],
  [[large-language-models]], [[nlp-fundamentals]] (embeddings), [[convolutional-neural-networks]]
  (feature visualization, adversarial examples), [[statistical-learning-theory]]
  (influence/stability), [[unsupervised-learning-em-and-mixture-models]] (dictionary
  learning as sparse coding), [[machine-learning-basics]].

## Sources
Molnar, *Interpretable Machine Learning* (2e; chapter structure from the book); Rudin 2019; Ribeiro, Singh & Guestrin 2016 (LIME), 2018 (anchors); Lundberg & Lee 2017; Lundberg et al. 2020 (TreeSHAP); Wachter et al. 2017; Adebayo et al. 2018; Ghorbani et al. 2019; Slack et al. 2020; Sundararajan et al. 2017 (IG); Selvaraju et al. 2017 (Grad-CAM); Kim et al. 2018 (TCAV); Olah et al. 2017, 2020; Elhage et al. 2021, 2022; Olsson et al. 2022 (induction heads); Bricken et al. 2023; Templeton et al. 2024; Meng et al. 2022; Belinkov & Glass 2019; Kornblith et al. 2019.

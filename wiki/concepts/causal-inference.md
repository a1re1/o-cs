---
title: Causal inference — why correlation isn't causation (confounding, selection, Simpson's paradox), structural causal models and causal DAGs, interventions and the do-operator, the ladder of causation (association, intervention, counterfactuals), identification (backdoor and frontdoor criteria, do-calculus, instrumental variables), potential outcomes and estimation (randomized experiments/A-B tests, matching, propensity scores, inverse probability weighting, doubly robust, difference-in-differences, regression discontinuity), causal discovery, and causal ML (uplift, off-policy evaluation, invariance)
type: concept
section: "6.7"
level: 500
tags: [causal-inference, causality, correlation-vs-causation, confounding, confounder, collider, selection-bias, simpsons-paradox, structural-causal-model, scm, causal-dag, intervention, do-operator, do-calculus, ladder-of-causation, counterfactuals, identification, backdoor-criterion, frontdoor-criterion, adjustment, instrumental-variables, potential-outcomes, rubin, neyman, ate, cate, ignorability, randomized-experiment, rct, a-b-testing, matching, propensity-score, ipw, inverse-probability-weighting, doubly-robust, difference-in-differences, regression-discontinuity, synthetic-control, causal-discovery, pc-algorithm, uplift-modeling, heterogeneous-effects, off-policy-evaluation, invariance, pearl, imbens-rubin, hernan-robins]
sources: [pgm-and-bayesian-texts-courses-and-seminal-papers]
summary: Observational data answers "what is P(Y | X = x)?" but decisions need "what happens to Y if I set X to x?" — P(Y | do(x)) — and the two differ whenever a confounder affects both (ice cream and drowning), a collider is conditioned on (selection bias, Berkson's paradox), or aggregation reverses trends (Simpson's paradox); Pearl's structural causal models write each variable as a function of its parents and noise, drawn as a causal DAG, define interventions as surgery on the graph (delete incoming edges to X, fix its value), and the ladder of causation orders what can be answered — association from data alone, intervention from a causal graph (identification: the backdoor criterion says adjust for a set Z that blocks all confounding paths and contains no descendants of X, P(y | do(x)) = Σ_z P(y | x, z)P(z); the frontdoor criterion identifies through a mediator when the confounder is unobserved; do-calculus is complete for what is identifiable; instrumental variables exploit an exogenous cause of X), and counterfactuals ("would this patient have recovered without the drug") from the full SCM; the potential-outcomes framework (Neyman–Rubin) defines effects as Y(1) − Y(0), unobservable per unit (the fundamental problem), identified under ignorability which randomization guarantees (RCTs/A-B tests remain the gold standard) and observational methods assume — matching, propensity scores, inverse probability weighting, doubly robust/TMLE estimators, and quasi-experiments (difference-in-differences, regression discontinuity, synthetic controls); causal discovery infers graphs from independence tests (PC/FCI) or scores under strong assumptions; and in ML causal thinking appears as uplift/heterogeneous-effect modelling, off-policy evaluation of recommender and bandit policies, invariant prediction for distribution shift, and the reason predictive models fail when deployed as interventions.
---
# Causal inference

**In one sentence.** Prediction asks what you will see; causation asks what you will get if
you act — and the gap between them is exactly the confounding and selection structure a
causal graph makes explicit, so that you can either randomize it away or adjust for it
with a justified formula.

## Why correlation isn't causation (Pearl, *Causality*; Hernán & Robins ch. 1–8)
Three ways X and Y correlate without X causing Y: a **confounder** Z → X, Z → Y (ice cream ↔
drowning via summer; the classic reason observational studies mislead); **selection/
collider bias** — conditioning on a common effect C ← X, C → Y induces dependence (Berkson:
among hospital patients two diseases anticorrelate; among admitted students test scores
and essays anticorrelate; survivorship bias); reverse causation. **Simpson's paradox**: a
trend in every subgroup reverses in the aggregate — the *correct* answer depends on the
causal structure (adjust for a confounder, don't adjust for a mediator), which no
statistic of the data can decide. Hence: the causal question needs causal assumptions
outside the data — a graph or a design.

## Structural causal models and interventions (Pearl 2009; Pearl, Glymour & Jewell 2016)
**SCM**: variables Xᵢ = fᵢ(pa(Xᵢ), Uᵢ) with independent exogenous noises U; the induced
**causal DAG** is a Bayesian network ([[bayesian-networks-and-hmms]], [[probabilistic-graphical-models]])
whose arrows *mean* direct causation (unlike a merely statistical BN). **Intervention
do(X = x)**: replace X's equation by the constant x (cut the incoming edges — "graph
surgery"); the interventional distribution P(Y | do(x)) is computed in the mutilated model
and generally ≠ P(Y | x) (conditioning). The **ladder of causation**: (1) association
P(y | x) — seeing; (2) intervention P(y | do(x)) — doing; (3) **counterfactuals** P(Y_x = y | X =
x′, Y = y′) — imagining what would have happened; higher rungs need more assumptions
(counterfactuals need the functional form, computed by abduction → action → prediction on
the noise). Mediation (direct/indirect effects), causal effect of treatment on the treated,
and probabilities of necessity/sufficiency live on rung 3.

## Identification: from graph to formula
Given the DAG, which interventional quantities are computable from observational data?
- **Backdoor criterion**: a set Z satisfying (i) no node in Z is a descendant of X, (ii) Z
  blocks every path between X and Y that starts with an arrow *into* X → **adjustment
  formula** P(y | do(x)) = Σ_z P(y | x, z) P(z) ("stratify and average"; regression adjustment,
  matching, IPW all estimate it). Adjusting for a collider or a mediator *creates* bias — the
  "table 2 fallacy" and why "control for everything" is wrong.
- **Frontdoor criterion**: unobserved confounder U of X and Y, but X affects Y only through a
  mediator M unconfounded with X and shielded from U: P(y | do(x)) = Σ_m P(m | x) Σ_{x′}
  P(y | m, x′) P(x′) (smoking → tar → cancer).
- **do-calculus**: three graphical rules for manipulating do-expressions; complete —
  an effect is identifiable iff do-calculus derives it (ID algorithm); non-identifiable
  cases need experiments or bounds (partial identification, sensitivity analysis to
  unmeasured confounding).
- **Instrumental variables**: an instrument I affecting Y only through X and independent of
  confounders (random encouragement, distance to a hospital, lotteries) identifies the
  effect for compliers — LATE — via Wald/2SLS; weak instruments and exclusion violations
  are the failure modes.

## Potential outcomes and estimation (Imbens & Rubin 2015; Hernán & Robins 2020)
Each unit has potential outcomes Y(1), Y(0); individual effect Y(1) − Y(0) is never
observed (**fundamental problem of causal inference**); target the **ATE** E[Y(1) − Y(0)],
ATT, or **CATE** τ(x) = E[Y(1) − Y(0) | X = x] (heterogeneous effects). Identification
assumptions: **ignorability/unconfoundedness** (Y(0), Y(1)) ⊥ T | X (= a backdoor set),
**positivity/overlap** 0 < P(T | X) < 1, **SUTVA** (no interference, one version of
treatment — violated by network effects, spillovers in marketplaces).
- **Randomized experiments / A-B tests**: randomization makes T ⊥ (Y(0), Y(1)); difference
  in means is unbiased; variance reduction (CUPED, stratification), sequential testing and
  peeking ([[hypothesis-testing-and-confidence-intervals]], [[multi-armed-bandits]] for
  adaptive designs), interference (switchback, cluster randomization), long-term effects
  via surrogates — the industry practice of causal inference.
- **Observational adjustment**: outcome regression E[Y | T, X]; **matching** (nearest
  neighbour on X or on the **propensity score** e(X) = P(T = 1 | X) — Rosenbaum & Rubin:
  conditioning on e(X) suffices); **inverse probability weighting** (weight by 1/e(X) or
  1/(1 − e(X)) to create a pseudo-population; unstable with extreme propensities);
  **doubly robust** (AIPW/TMLE: consistent if either the outcome or propensity model is
  right; with ML nuisance models and cross-fitting — "double machine learning" — [[machine-learning-basics]]);
  **heterogeneous effects** by causal forests, meta-learners (T/S/X-learners) — **uplift
  modelling** for targeting.
- **Quasi-experiments**: **difference-in-differences** (parallel trends), **regression
  discontinuity** (threshold assignment — local randomization), **synthetic control**
  (weighted donor pool for one treated unit), event studies, interrupted time series.
- Bounds and **sensitivity analysis** (how strong must an unmeasured confounder be to
  explain the effect — E-values, Rosenbaum bounds) when assumptions are doubtful.

## Causal discovery and causal ML
**Discovery** from data: constraint-based (**PC**, FCI with latent confounders — conditional
independence tests → skeleton → orient v-structures; only up to a Markov equivalence
class), score-based (GES), functional-form methods (LiNGAM: non-Gaussian noise; additive
noise models; the asymmetry of cause and effect), continuous optimization (NOTEARS);
requires faithfulness and enough data, and interventional data resolves equivalence
classes ([[probabilistic-graphical-models]] structure learning). **In ML**: predictive
models used as interventions fail (the model learned P(Y | X) under one policy; deploying
it changes the policy — Goodhart/[[llm-post-training-sft-rlhf-dpo]] reward hacking is a
causal failure); **off-policy evaluation** of recommenders and bandit policies via IPW/
doubly robust from logged data ([[multi-armed-bandits]], [[deep-reinforcement-learning]]
offline RL); **invariant risk minimization**/causal features for **distribution shift**
(causal mechanisms are stable across environments; spurious correlations aren't —
[[fairness-in-machine-learning]] for the causal definitions of discrimination);
counterfactual explanations ([[interpretability-and-explainability]]); causal
representation learning and LLMs' causal reasoning as open problems.

## Pitfalls
- Adjusting for everything available (colliders, mediators, post-treatment variables).
- Interpreting regression coefficients as effects without an identification argument.
- Propensity models with extreme scores (no overlap) — trim, or admit non-identifiability.
- A-B tests with interference (two-sided markets), peeking, or metrics that are surrogates
  for the real outcome.
- Causal discovery output read as the causal graph rather than an equivalence class under
  strong assumptions.

## Related
- [[bayesian-networks-and-hmms]], [[probabilistic-graphical-models]],
  [[hypothesis-testing-and-confidence-intervals]], [[multi-armed-bandits]],
  [[machine-learning-basics]], [[deep-reinforcement-learning]], [[fairness-in-machine-learning]],
  [[interpretability-and-explainability]], [[llm-post-training-sft-rlhf-dpo]],
  [[bayesian-inference]], [[probability-and-statistics-for-cs]].

## Sources
Pearl 2009 (*Causality*, 2e); Pearl, Glymour & Jewell 2016 (*Causal Inference in Statistics: A Primer*); Pearl & Mackenzie 2018 (*The Book of Why* — ladder of causation); Imbens & Rubin 2015; Hernán & Robins 2020 (*What If*, free); Rosenbaum & Rubin 1983; Angrist & Pischke 2009; Chernozhukov et al. 2018 (DML); Spirtes, Glymour & Scheines 2000; Poole & Mackworth ch. 11 (§6.1); Kohavi et al. 2020 (*Trustworthy Online Controlled Experiments*).

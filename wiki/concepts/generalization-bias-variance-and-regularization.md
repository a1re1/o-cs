---
title: Generalization, bias–variance, and regularization — the bias–variance decomposition, underfitting vs overfitting, learning curves, double descent, sample-complexity bounds for finite hypothesis classes (Hoeffding + union bound) and the VC preview, uniform convergence, L1/L2 regularization and its Bayesian (MAP) reading, implicit regularization, cross-validation and model selection, Occam and no free lunch
type: concept
section: "6.2"
level: 400
tags: [generalization, bias-variance, bias-variance-decomposition, underfitting, overfitting, model-complexity, learning-curves, double-descent, interpolation, benign-overfitting, sample-complexity, hoeffding, union-bound, uniform-convergence, finite-hypothesis-class, vc-dimension, erm, regularization, l2, ridge, weight-decay, l1, lasso, sparsity, map, bayesian-regularization, implicit-regularization, early-stopping, cross-validation, model-selection, hyperparameters, validation, occams-razor, no-free-lunch, test-error, training-error, generalization-gap]
sources: [ml-courses-texts-and-seminal-papers]
summary: Expected test error of a learned predictor decomposes into irreducible noise + bias² (the error of the best model in the class — too simple a class underfits) + variance (sensitivity of the fitted model to the particular training sample — too rich a class overfits), so error vs complexity is U-shaped and error vs training size (learning curves) separates the two regimes; modern over-parameterized models show double descent — test error rises to a peak at the interpolation threshold (model just able to fit the training data) and then falls again as capacity grows, because among the many interpolating solutions optimizers pick smooth ones (implicit regularization); the theory behind the classical picture is uniform convergence — for a finite class of k hypotheses, Hoeffding plus a union bound give that with probability 1−δ every hypothesis' training error is within √(log(2k/δ)/2m) of its true error, so ERM is within twice that of the best in class and the sample complexity is O((1/ε²) log(k/δ)), i.e. logarithmic in the number of hypotheses ("parameters"); infinite classes are handled by the VC dimension (roughly the number of parameters), which is the subject of learning theory proper; regularization trades bias for variance explicitly — L2/ridge/weight decay shrinks weights (Gaussian prior, MAP), L1/lasso zeroes them (Laplace prior, sparsity), early stopping and dropout act similarly, and gradient descent itself regularizes implicitly (minimum-norm solutions) — with the strength chosen by cross-validation on a held-out set, never on the test set; Occam's razor is a statement about generalization, not model size, and no free lunch says no procedure generalizes on every distribution.
---
# Generalization, bias–variance, and regularization

**In one sentence.** Test error = noise + bias² + variance, so learning is a trade between a
class rich enough to contain the truth and a sample large enough to pin down which member
— regularization buys variance reduction with bias, cross-validation prices the trade, and
over-parameterized models bend the classical U-curve into double descent.

## Bias–variance decomposition (CS229 ch. 8; Abu-Mostafa ch. 2; ESL ch. 7)
For squared loss at a point x, with training set S random: E_S[(h_S(x) − y)²] = **σ²**
(irreducible noise) + **(E_S[h_S(x)] − f(x))²** (bias²: how far the *average* fitted model is
from the truth — the class can't represent f, or the learner can't find it) + **E_S[(h_S(x) −
E_S[h_S(x)])²]** (variance: how much the fit wobbles with the sample). A constant model has
zero variance and huge bias; a degree-20 polynomial through 21 points has zero bias on the
training set and enormous variance. **Underfitting** (high bias: training and test error
both high) vs **overfitting** (high variance: training error low, test error high); the
**generalization gap** is the second symptom. **Learning curves** (train/validation error vs
m): converging high → bias (more data won't help; need a richer model/features); a wide gap
closing slowly → variance (more data, regularization, simpler model). Classification's
analogue is looser (bias and variance interact through the decision boundary) but the
intuition carries. Remedies are dual: for bias — more features, less regularization, deeper
models, boosting; for variance — more data, regularization, feature selection, bagging,
ensembles ([[decision-trees-and-ensembles]]).

## Double descent (Belkin et al. 2019; CS229 ch. 8.2)
Classical theory predicts a U-shaped test error in model complexity. Over-parameterized
models (deep nets, wide random features, even linear regression with d > n) show **double
descent**: test error rises to a peak at the **interpolation threshold** (parameters ≈
samples — the model can just barely fit every training point, and is forced into a wild
interpolant), then *decreases* as parameters grow further, often below the classical
optimum. Explanation: with many interpolating solutions the optimizer (GD from small init)
selects the **minimum-norm** one, which gets smoother as capacity increases — **implicit
regularization**; explicit regularization or early stopping removes the peak. Also
**sample-wise** double descent (more data can hurt near the threshold) and **epoch-wise**.
Consequences: "bigger is better" for neural networks is not a contradiction of theory but
of the classical proxy for complexity (parameter count); the right complexity measures are
norms/margins ([[statistical-learning-theory]], [[scaling-laws]]).

## Why learning works — and how many training examples do I need? Uniform convergence and sample complexity (CS229 ch. 8.3; UML ch. 2–4; Abu-Mostafa ch. 1–2)
Setup: m i.i.d. samples, 0–1 loss, hypothesis class H; ε̂(h) training error, ε(h) true error;
ERM picks ĥ = argmin ε̂. **Hoeffding**: for a fixed h, P(|ε̂(h) − ε(h)| > γ) ≤ 2e^{−2γ²m}
([[concentration-inequalities]]). **Union bound** over a finite H of size k: with probability
≥ 1 − δ, **uniform convergence** |ε̂(h) − ε(h)| ≤ γ for *all* h ∈ H simultaneously, with
γ = √((1/2m) log(2k/δ)). Then ε(ĥ) ≤ ε̂(ĥ) + γ ≤ ε̂(h*) + γ ≤ ε(h*) + 2γ: ERM is within 2γ of
the best hypothesis in the class. **Sample complexity**: m ≥ (1/2γ²) log(2k/δ) = O((1/γ²)
log(k/δ)) suffices — **logarithmic in |H|**, so a class of 2^{64d} float-parameterized models
needs O(d) samples: parameters count, but only linearly. The bound also displays
bias–variance: ε(h*) is bias (falls with a richer H), 2γ is variance (grows with log k).
Infinite H: **VC dimension** (largest set H can shatter; d+1 for linear classifiers in ℝᵈ)
replaces log k: ε(ĥ) ≤ ε(h*) + O(√((VC/m) log(m/VC) + (1/m) log(1/δ))), and learnability ⇔
finite VC (the fundamental theorem — [[statistical-learning-theory]], PAC learning). The
"why learning is possible" argument: the training set is a sample of the same distribution,
so the empirical mean tracks the true mean for each hypothesis, and the class isn't big
enough for the maximum deviation to be large. **No free lunch** (Wolpert): without
restricting H (an inductive bias), no learner generalizes; **Occam**: prefer the simpler
*class* because its bound is tighter — not because simple models are truer.

## Regularization (CS229 ch. 9; ESL ch. 3, 7)
Add a penalty to ERM: J(θ) + λ R(θ).
- **L2 / ridge / weight decay** R = ‖θ‖²: shrinks all weights toward zero (never exactly),
  closed form for linear regression (XᵀX + λI)⁻¹Xᵀy; equals **MAP** with a Gaussian prior
  θ ~ N(0, τ²I) ([[maximum-likelihood-estimation]], [[bayesian-inference]]); SGD with weight
  decay implements it.
- **L1 / lasso** R = ‖θ‖₁: sparse solutions (corners of the L1 ball hit the contours — Tibshirani
  1996); Laplace prior; feature selection; solved by coordinate descent / proximal gradient;
  elastic net mixes both (handles correlated features).
- **Other**: **early stopping** (iterations as the complexity knob — equivalent to L2 for GD on
  quadratics), **dropout**, data augmentation, noise injection, parameter sharing (CNNs),
  bagging — all reduce variance ([[deep-learning-basics]]); **implicit** regularization by the
  optimizer (GD converges to minimum-norm / max-margin solutions for logistic loss).
- Bayesian reading: the full posterior instead of MAP averages over models (predictive
  distribution) — the principled variance control, expensive; [[bayesian-inference]].
λ trades bias for variance; the regularization path (θ̂(λ)) and **cross-validation** choose it.

## Model selection and cross-validation (CS229 ch. 9.3; ISLR ch. 5)
Hold-out: fit on 70 %, select on 30 %, then refit on all. **k-fold CV** (k = 5–10): average
validation error over folds; **leave-one-out** for tiny data (efficient closed form for
linear smoothers). Select hyperparameters (λ, depth, kernel width, architecture) and
features by CV, then estimate the chosen model's error on an untouched **test** set — or use
**nested** CV. Analytic alternatives: AIC/BIC, Mallows' Cp, MDL (penalize training error by
effective parameters — [[kolmogorov-complexity]]); Bayesian model evidence. Feature
selection by forward search or filter scores (mutual information) is itself a model choice
and must be inside the CV loop ([[machine-learning-basics]] on leakage).

## Pitfalls
- Diagnosing overfitting from training error alone; "fixing" bias by adding data.
- Tuning on the test set (the most common way to publish an optimistic number).
- Comparing models by parameter count when norms/margins are what matter (double descent).
- Regularizing the bias term or unscaled features (penalties are scale-dependent —
  standardize first).
- Reading a sparse lasso model as "the true features" when features are correlated.

## Related
- [[machine-learning-basics]], [[statistical-learning-theory]] (VC, Rademacher, PAC),
  [[concentration-inequalities]], [[maximum-likelihood-estimation]], [[bayesian-inference]],
  [[linear-models-logistic-regression-and-glms]], [[decision-trees-and-ensembles]],
  [[deep-learning-basics]], [[scaling-laws]], [[kolmogorov-complexity]],
  [[gradient-descent]].

## Sources
CS229 notes ch. 8–9 (ToC read; content from memory of earlier editions); Abu-Mostafa ch. 1–2, 4–5; UML ch. 2–5, 11, 13; ESL ch. 3, 7; ISLR ch. 5–6; Belkin et al. 2019; Wolpert 1996; Tibshirani 1996.

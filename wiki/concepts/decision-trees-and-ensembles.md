---
title: Decision trees and ensembles — CART (greedy splits by Gini/entropy/variance, pruning), why single trees are high-variance, bagging and random forests (bootstrap + random feature subsets, out-of-bag error, feature importance), boosting (AdaBoost, gradient boosting as functional gradient descent, XGBoost/LightGBM/CatBoost), stacking, and why boosted trees rule tabular data
type: concept
section: "6.2"
level: 400
tags: [decision-trees, cart, id3, c4-5, gini-impurity, entropy, information-gain, variance-reduction, greedy-splitting, pruning, cost-complexity, overfitting, axis-aligned, ensembles, bagging, bootstrap, random-forests, breiman, out-of-bag, feature-importance, permutation-importance, boosting, adaboost, weak-learner, exponential-loss, gradient-boosting, friedman, functional-gradient-descent, shrinkage, learning-rate, subsampling, xgboost, second-order, regularized-objective, histogram-splits, lightgbm, catboost, stacking, blending, bias-variance, tabular-data, interpretability]
sources: [ml-courses-texts-and-seminal-papers]
summary: A decision tree recursively partitions the input space with axis-aligned tests chosen greedily to reduce impurity (Gini or entropy for classification, variance for regression — CART), predicting a constant per leaf; it is fast, handles mixed and unscaled features and missing values, and is interpretable, but a fully grown tree overfits and is unstable (small data changes give a different tree), i.e. low bias, high variance, and pruning helps only partly; ensembles fix this — bagging averages trees grown on bootstrap resamples, and random forests (Breiman 2001) decorrelate them further by restricting each split to a random subset of features, giving a strong, nearly tuning-free learner with free out-of-bag validation and feature-importance estimates; boosting instead builds trees sequentially, each fitting what the previous ensemble got wrong — AdaBoost reweights misclassified points (exponential loss), gradient boosting (Friedman 2001) fits each new small tree to the negative gradient of any differentiable loss (functional gradient descent) with shrinkage and subsampling, and XGBoost/LightGBM/CatBoost add a second-order Taylor expansion, an explicitly regularized objective, histogram-based split finding, sparsity handling and systems engineering — the reason boosted trees win most tabular-data competitions while neural networks win on perception; stacking learns how to combine heterogeneous models.
---
# Decision trees and ensembles

**In one sentence.** Trees are the flexible, unstable base learner; averaging many
decorrelated trees (random forests) removes variance, and adding trees one at a time to
descend the loss (gradient boosting) removes bias — which is why the best tabular models
are forests of small trees.

## Decision trees: CART (ISLR ch. 8; ESL ch. 9)
Recursively choose a feature j and threshold t splitting the region into {xⱼ < t} and
{xⱼ ≥ t}; predict the leaf's majority class or mean. **Split criterion**: minimize weighted
impurity of children — classification: **Gini** Σ pₖ(1 − pₖ) or **entropy** −Σ pₖ log pₖ
(**information gain** — [[entropy-and-information]]; ID3/C4.5 lineage), misclassification
error is too flat to grow trees; regression: sum of squared deviations (**variance
reduction**). Greedy, top-down; O(d·n log n) per level with sorted features; categorical
features by subset splits; **missing values** via surrogate splits or a default direction.
Stop by depth / min samples per leaf / min impurity decrease; better: grow full, then
**cost-complexity pruning** (minimize error + α·|leaves|, α by cross-validation). Properties:
invariant to monotone feature transforms (no scaling), automatic feature selection and
interactions, interpretable paths, **axis-aligned** boundaries (poor for diagonal
relationships — oblique/rotation forests), piecewise-constant predictions (no
extrapolation), and **high variance**: a tree is a set of nested greedy decisions, so
resampling the data changes the top split and everything below. Trees are the classic
low-bias/high-variance learner ([[generalization-bias-variance-and-regularization]]).

## Bagging and random forests (Breiman 1996, 2001)
**Bagging** (bootstrap aggregating): draw B bootstrap samples, grow a full tree on each,
average predictions (or vote). Averaging B i.i.d. predictors divides variance by B; but
bootstrap trees are correlated ρ, so variance → ρσ² + (1−ρ)σ²/B — the correlation is the
floor. **Random forests** lower ρ: at each split consider only m random features (m ≈ √d for
classification, d/3 for regression); trees are grown deep without pruning. Results: strong
out of the box, robust to hyperparameters, parallel, hard to overfit by adding trees (B is
not a regularization knob — more is monotonically better, then flat). **Out-of-bag (OOB)
error**: each tree omits ~37 % of samples; predict those with only the trees that didn't see
them — a free cross-validation. **Feature importance**: mean impurity decrease (biased toward
high-cardinality features) or **permutation importance** (shuffle a feature, measure the OOB
loss increase) — and the caveat that correlated features share importance
([[interpretability-and-explainability]]). Extremely randomized trees randomize thresholds
too. Forests do not extrapolate and can be beaten by boosting when tuned.

## Boosting (Freund & Schapire 1997; Friedman 2001)
Fit an additive model F(x) = Σ γₘ hₘ(x) of **weak learners** (shallow trees — stumps to
depth ~6) **sequentially**, each correcting the current ensemble. **AdaBoost**: maintain
example weights; train hₘ on the weighted data; αₘ = ½ log((1 − errₘ)/errₘ); upweight
misclassified examples by e^{αₘ}; final sign(Σ αₘ hₘ). It is coordinate descent on the
**exponential loss** Σ exp(−yᵢF(xᵢ)) — the statistical view (Friedman, Hastie & Tibshirani
2000) that generalized boosting to any loss; training error drops exponentially, and test
error keeps improving after training error hits zero because the **margin** distribution
keeps improving ([[statistical-learning-theory]]). **Gradient boosting** (GBM): at step m,
compute the negative gradient of the loss at the current predictions (pseudo-residuals rᵢ =
−∂ℓ(yᵢ, F(xᵢ))/∂F), fit a regression tree to r, choose a step (per-leaf line search), update
F ← F + ν·hₘ — **functional gradient descent** ([[gradient-descent]] in the space of functions).
Losses: squared (residual fitting), absolute/Huber (robust), logistic (classification),
multinomial, Poisson, ranking (LambdaMART — [[learning-to-rank]]), quantile. Regularization:
**shrinkage** ν (0.01–0.1; smaller needs more trees), **subsampling** rows (stochastic gradient
boosting) and columns, tree depth/leaves, min child weight, early stopping on validation.
Unlike forests, boosting *can* overfit with too many trees — tune M by early stopping.

## XGBoost, LightGBM, CatBoost (Chen & Guestrin 2016; Ke et al. 2017; Prokhorenkova et al. 2018)
**XGBoost**: second-order Taylor expansion of the loss (gradient gᵢ and Hessian hᵢ per
example) gives a closed-form optimal leaf weight w = −Σg/(Σh + λ) and a split gain
½[G_L²/(H_L+λ) + G_R²/(H_R+λ) − G²/(H+λ)] − γ, with an explicit regularized objective (L2 on
leaf weights, γ per leaf); approximate split finding with weighted quantile sketches;
**sparsity-aware** default directions for missing values; systems: column blocks, cache-aware
prefetching, out-of-core, parallel split evaluation ([[cache-oblivious-algorithms]] in spirit).
**LightGBM**: histogram-binned features, leaf-wise (best-first) growth, gradient-based
one-side sampling, exclusive feature bundling — faster on large n. **CatBoost**: ordered
boosting (fights target leakage in target statistics for categoricals), symmetric trees.
On tabular data these beat deep learning in most benchmarks (Grinsztajn et al. 2022) —
trees handle heterogeneous scales, irrelevant features, and non-smooth targets; neural nets
win when features are homogeneous and huge (images, text, audio — [[deep-learning-basics]]).

## Stacking and other ensembles
**Stacking**: train diverse base models, then a meta-learner on their out-of-fold
predictions (never on in-sample predictions — leakage); blending on a holdout; simple
averaging often captures most of the gain; Netflix Prize and Kaggle lore. **Why ensembles
work**: variance reduction (bagging), bias reduction (boosting), and representational
(the average of models can lie outside the class). Bayesian model averaging is the
principled cousin; dropout and snapshot ensembles are the neural analogues.

## Pitfalls
- Unpruned single trees presented as "the model" (unstable); trusting one tree's splits as
  causal structure.
- Impurity importance on mixed-cardinality features; importance ≠ effect direction.
- Boosting with a high learning rate and no early stopping (overfits); forests with tiny B.
- Extrapolation: trees predict the nearest leaf's constant beyond the training range.
- Stacking on in-sample predictions.

## Related
- [[machine-learning-basics]], [[generalization-bias-variance-and-regularization]],
  [[entropy-and-information]], [[gradient-descent]], [[statistical-learning-theory]],
  [[kernels-and-support-vector-machines]], [[deep-learning-basics]],
  [[interpretability-and-explainability]], [[learning-to-rank]], [[cache-oblivious-algorithms]].

## Sources
Breiman 2001 (random forests; "two cultures"); Breiman et al. 1984 (CART); Freund & Schapire 1997; Friedman 2001; Friedman, Hastie & Tibshirani 2000; Chen & Guestrin 2016; Ke et al. 2017; ISLR ch. 8; ESL ch. 9–10, 15–16; UML ch. 10, 18.

---
title: Machine learning basics — supervised vs unsupervised vs reinforcement learning, the learning problem (hypothesis class, loss, empirical risk minimization), train/validation/test splits and cross-validation, evaluation metrics (accuracy, precision/recall, F1, ROC-AUC, log loss, RMSE), feature engineering and the ML workflow, and Domingos' twelve lessons
type: concept
section: "6.2"
level: 300
tags: [machine-learning, supervised-learning, unsupervised-learning, reinforcement-learning, regression, classification, hypothesis-class, loss-function, empirical-risk-minimization, erm, training-set, validation-set, test-set, cross-validation, k-fold, holdout, overfitting, underfitting, evaluation-metrics, accuracy, precision, recall, f1, roc, auc, confusion-matrix, log-loss, rmse, class-imbalance, calibration, feature-engineering, one-hot, normalization, standardization, feature-selection, data-leakage, pipelines, scikit-learn, baseline, ml-workflow, two-cultures, domingos, no-free-lunch, inductive-bias, curse-of-dimensionality, nearest-neighbours, knn]
sources: [ml-courses-texts-and-seminal-papers]
summary: Machine learning fits a function from data instead of writing it by hand: supervised learning maps inputs to labels (regression for real outputs, classification for discrete) by choosing, from a hypothesis class, the predictor that minimizes average loss on training examples (empirical risk minimization) — the aim being low loss on unseen data, which is why data is split into training, validation (model/hyperparameter selection) and test (final, touched once) sets, why k-fold cross-validation reuses small datasets, and why leakage of test information into training is the commonest silent failure; unsupervised learning finds structure without labels (clustering, dimensionality reduction, density estimation) and reinforcement learning learns from rewards; performance is judged with task-appropriate metrics (RMSE/MAE for regression; accuracy, precision, recall, F1, ROC-AUC, log loss and calibration for classification, chosen with class imbalance and asymmetric costs in mind); features matter as much as models (encoding, scaling, transformations, selection — Domingos: "feature engineering is the key"), a baseline (mean, majority class, k-nearest neighbours, logistic regression) comes before anything complex, no learner beats all others on all problems (no free lunch — inductive bias is unavoidable), and intuition fails in high dimensions (the curse of dimensionality makes nearest neighbours and volumes behave strangely).
---
# Machine learning basics

**In one sentence.** Pick a hypothesis class, a loss, and an optimizer; fit on training data;
choose models on validation data; report on test data touched once — and remember that what
you are optimizing is generalization, which none of those three sets measures directly.

## The learning problem (CS229 ch. 1; Abu-Mostafa ch. 1; UML ch. 1–2)
Data (x⁽ⁱ⁾, y⁽ⁱ⁾) drawn i.i.d. from an unknown distribution D. **Supervised**: learn h: X → Y;
**regression** (y ∈ ℝ: house prices, energy), **classification** (y ∈ {1..k}: spam, digits),
structured outputs (sequences, trees). **Unsupervised**: only x — clustering
([[k-means-clustering]], [[unsupervised-learning-em-and-mixture-models]]), dimensionality
reduction ([[svd-and-pca]]), density estimation, anomaly detection; **self-supervised**
(predict part of x from the rest — the pretraining recipe of [[large-language-models]]);
**reinforcement** (rewards, sequential — [[markov-decision-processes]]). Choose a
**hypothesis class** H (linear functions, trees, neural nets), a **loss** ℓ(h(x), y) (squared,
0–1, logistic/cross-entropy, hinge), and minimize **empirical risk** (1/n) Σ ℓ(h(xᵢ), yᵢ) —
**ERM** — as a proxy for **true risk** E_D[ℓ]. Domingos' decomposition: learning =
**representation** (H) + **evaluation** (loss/objective) + **optimization** (search over H —
[[gradient-descent]], [[convexity]]; closed forms; greedy/tree induction). The probabilistic
view: ERM with log loss is [[maximum-likelihood-estimation]]; regularization is a prior (MAP).

## Generalization is the point
Training error is optimistic: a rich H can memorize (**overfitting**: low training, high
test error) while a poor one cannot fit (**underfitting**). Theory ([[generalization-bias-variance-and-regularization]],
[[statistical-learning-theory]]): test error ≈ training error + complexity penalty that
shrinks with n. Practice:
- **Train / validation / test**: fit on train; pick hyperparameters, features, and models on
  validation; evaluate the final choice **once** on test. Every decision made by looking at
  a set contaminates it (**data snooping**); a test set reused for selection becomes a
  validation set (Kaggle public-leaderboard overfitting).
- **k-fold cross-validation** (k = 5 or 10; leave-one-out for tiny n): rotate the held-out
  fold, average the metric; nested CV when selecting hyperparameters and estimating
  performance; stratify for classification; **time-series** needs forward-chaining splits
  (never shuffle time); **grouped** splits when samples share an entity (patients, users) —
  the leak of the same user into train and test is the classic inflated score.
- **Leakage**: features computed with future or target information (aggregates over the full
  dataset, normalization fit on all data, IDs correlated with labels); fit every
  preprocessing step inside the training fold (**pipelines**).
- **Learning curves** (error vs n) diagnose: high bias (both errors high, converged) → richer
  model/features; high variance (large gap) → more data, regularization, simpler model.

## Evaluation metrics
| Task | Metric | Notes |
|---|---|---|
| regression | RMSE, MAE, R² | RMSE penalizes outliers; MAE robust; compare against predicting the mean |
| classification | accuracy | meaningless under imbalance (99 % negatives → 99 % "accuracy") |
| | confusion matrix; precision = TP/(TP+FP), recall = TP/(TP+FN), F1 | choose by cost of FP vs FN; precision–recall curves for rare positives |
| | ROC curve, AUC | threshold-free ranking quality; AUC = P(score(pos) > score(neg)); insensitive to imbalance (which can mislead — use PR-AUC) |
| | log loss / cross-entropy, Brier score, **calibration** | probability quality; calibrate with Platt scaling / isotonic regression |
| ranking/retrieval | precision@k, recall@k, MRR, nDCG | [[evaluation-of-ir-systems]] — the o-cs eval harness uses these |
| multiclass | macro vs micro averaging, top-k accuracy | macro weights classes equally |
Always report a **baseline** (majority class, mean, last value, k-NN, logistic regression) and
**confidence intervals** (bootstrap, repeated CV — [[hypothesis-testing-and-confidence-intervals]]); a difference smaller
than the CV standard deviation is noise.

## Features and the workflow
Features: numeric scaling (standardize for gradient methods, kernels, k-NN; trees don't
care), **one-hot**/target/embedding encoding for categoricals, log/Box-Cox transforms for
skew, binning, interactions and polynomial features, date/time decomposition, text via
bag-of-words/TF-IDF/embeddings ([[tf-idf-and-vector-space-model]]), missing-value handling
(indicator + imputation), **feature selection** (filter by correlation/mutual information,
wrapper, embedded — Lasso), learned features ([[deep-learning-basics]] replaces most manual
engineering for perception). Workflow: define the metric and baseline → get and inspect data
(distributions, leakage, duplicates) → split → simple model → iterate on features/models with
CV → error analysis (look at the mistakes) → final test → monitor drift in production
([[mlops-and-ml-systems]]). **k-nearest neighbours** as the universal baseline: predict by
majority/mean of the k closest points — no training, all cost at query time
([[similarity-search-and-lsh]]), and the first victim of the **curse of dimensionality**: in
high dimensions all points are nearly equidistant, volumes concentrate in shells, and
learners need exponentially many samples unless the data lies on a low-dimensional manifold
or the model has the right inductive bias.

## Lessons (Domingos 2012; Breiman 2001; Wolpert 1996)
It's generalization that counts; data alone is not enough (inductive bias — **no free lunch**:
averaged over all possible targets every learner is equal, so assumptions are what make
learning possible); overfitting has many faces (bias vs variance); intuition fails in high
dimensions; theoretical guarantees are loose but qualitatively right; feature engineering is
the key; more data beats a cleverer algorithm (and scalable learners beat clever ones);
learn many models — ensembles ([[decision-trees-and-ensembles]]); simplicity does not imply
accuracy (Occam is about generalization, not model size); representable ≠ learnable;
correlation ≠ causation ([[causal-inference]]). Breiman's **two cultures**: the data-modelling
culture (assume a stochastic model, estimate and interpret) vs the algorithmic culture
(predict; judge by held-out accuracy) — the latter won on accuracy, and interpretability
became a separate research problem ([[interpretability-and-explainability]]).

## Related
- [[linear-models-logistic-regression-and-glms]], [[kernels-and-support-vector-machines]],
  [[decision-trees-and-ensembles]], [[generalization-bias-variance-and-regularization]],
  [[unsupervised-learning-em-and-mixture-models]], [[k-means-clustering]], [[svd-and-pca]],
  [[maximum-likelihood-estimation]], [[gradient-descent]], [[statistical-learning-theory]],
  [[deep-learning-basics]], [[evaluation-of-ir-systems]], [[hypothesis-testing-and-confidence-intervals]],
  [[similarity-search-and-lsh]], [[mlops-and-ml-systems]].

## Sources
CS229 notes ch. 1, 8–9 (ToC read; content from memory of earlier editions); Abu-Mostafa ch. 1, 4–5; UML ch. 1–2, 5, 11; ISLR ch. 2, 5; Domingos 2012; Breiman 2001; Wolpert 1996.

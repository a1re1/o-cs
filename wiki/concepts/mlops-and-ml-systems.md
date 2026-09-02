---
title: MLOps and ML systems design — the ML production lifecycle, hidden technical debt (entanglement, data dependencies, feedback loops, pipeline jungles), training data and labelling, feature engineering and feature stores, training/serving skew, offline vs online evaluation (A/B, shadow, canary, interleaving), deployment patterns (batch vs online, edge vs cloud), monitoring and data/concept drift, continual learning and retraining, experiment tracking, reproducibility, testing ML systems, data engineering pipelines (batch/streaming, orchestration, data quality), and responsible-AI operations
type: concept
section: "6.9"
level: 400
tags: [mlops, ml-systems, ml-production, ml-lifecycle, hidden-technical-debt, entanglement, cace, data-dependencies, feedback-loops, pipeline-jungles, configuration-debt, training-data, labeling, weak-supervision, active-learning, class-imbalance, feature-engineering, feature-store, leakage, training-serving-skew, offline-evaluation, online-evaluation, a-b-testing, shadow-deployment, canary, interleaving, deployment, batch-prediction, online-prediction, edge, model-registry, monitoring, observability, data-drift, concept-drift, covariate-shift, label-shift, drift-detection, continual-learning, retraining, experiment-tracking, reproducibility, model-versioning, ci-cd-for-ml, testing-ml, data-validation, data-engineering, etl, elt, batch-vs-streaming, orchestration, airflow, data-quality, data-lineage, lakehouse, huyen, sculley]
sources: [ml-systems-and-mlops-texts-courses-and-seminal-papers]
summary: In production the model is the small box (Sculley et al.): the system around it — data collection, validation, feature computation, serving, monitoring, retraining — is where the cost and the failures live, and ML adds debts ordinary software lacks: entanglement (changing any input feature changes everything — CACE), data dependencies that are unversioned and unstable, hidden feedback loops (the model's outputs shape its future training data), correction cascades, pipeline jungles and configuration debt; the lifecycle Huyen teaches is iterative — scope the problem with a business metric and an ML metric, get training data (sampling, labelling with humans/weak supervision/active learning, class imbalance, augmentation), engineer features (avoid leakage: fit transformations on training folds, respect time; feature stores make one definition serve training and inference to prevent training/serving skew), develop and train with experiment tracking and versioned data/code/config for reproducibility, evaluate offline on sliced and perturbed test sets then online by shadow deployment, canaries, A/B tests or interleaving, deploy as batch predictions or an online service (latency budgets, edge vs cloud, model compression), monitor operational metrics plus data/prediction/label distributions to catch covariate, label and concept drift (statistical tests, feature-level alerts, delayed labels), and retrain on a schedule or trigger (continual learning, champion–challenger, rollbacks); the data-engineering half is the pipeline that makes this possible — batch/streaming ingestion, ETL/ELT into warehouses/lakehouses, orchestration DAGs, data validation and lineage — and the failure modes are almost always data (skew, leakage, drift, silent upstream schema changes), which is why testing ML systems means testing data and pipelines, not just models.
---
# MLOps and ML systems design

**In one sentence.** A model in production is a data pipeline with a learned component
whose behaviour depends on data you don't control — so design for skew, drift, feedback
loops and retraining from the start, version everything, and monitor inputs and outputs
as carefully as latency.

## The lifecycle and the debts (Huyen ch. 1–2; Sculley et al. 2015)
Requirements: reliability (wrong predictions fail silently), scalability (models and
traffic grow), maintainability (many roles touch it), adaptability (data changes). The loop:
**scoping** (a business objective → a proxy ML metric; decoupling multiple objectives into
separate models combined by weights) → **data** → **features** → **model** → **deploy** → **monitor**
→ repeat; most iterations are data changes. **Hidden technical debt** (Sculley): (1)
**entanglement** — no input is really independent (**CACE**: changing anything changes
everything), so features can't be modified in isolation; (2) **correction cascades** —
models trained on other models' outputs; (3) **undeclared consumers** of predictions;
(4) **data dependencies** — unstable upstream signals, underutilized features, no static
analysis of data lineage; (5) **feedback loops** — direct (the model chooses what it sees:
recommenders) and hidden (two systems influencing each other through the world);
(6) anti-patterns — glue code, **pipeline jungles**, dead experimental codepaths;
(7) **configuration debt**; (8) the changing external world — fixed thresholds, monitoring
gaps. The remedy is treating data, features and configs as first-class versioned,
tested artefacts ([[software-engineering-fundamentals]], [[technical-debt-and-maintenance]]).

## Training data (Huyen ch. 4)
Sampling: non-probability (convenience — the default and the bias source) vs random/
stratified/weighted/reservoir (streams — [[randomized-algorithms]]) /importance sampling.
**Labels**: hand labels (expensive, slow, privacy, multi-annotator disagreement — measure
agreement), natural labels (clicks, purchases — with feedback-loop delay), **weak
supervision** (labelling functions combined by a generative model — Snorkel), semi-
supervised, **transfer learning** and **active learning** (label the most uncertain/diverse
points — [[multi-armed-bandits]]-style budget allocation). **Class imbalance**: use the right
metrics (PR-AUC, F-β — [[machine-learning-basics]]), resampling (under/over/SMOTE), cost-
sensitive losses, focal loss, thresholds tuned on validation. Data augmentation (label-
preserving transforms, perturbation for robustness, synthetic data). Data quality > data
quantity past a point; **data cascades** (Sambasivan et al.) as the field's silent failure.

## Features, leakage, skew (Huyen ch. 5)
Handling missing values (MNAR/MAR/MCAR — deletion vs imputation with indicators), scaling
(fit on train only), discretization, encoding (hashing trick for unbounded categories —
[[hash-tables]]), crosses, embeddings. **Leakage**: splitting time-correlated data randomly,
scaling before splitting, filling missing values with test statistics, duplicates across
splits, group leakage, target-derived features (the survey's "hospital" feature) — detect by
measuring each feature's predictive power and ablating. **Training/serving skew**: features
computed by different code (batch SQL vs online Python) or from different data (backfilled
vs streaming) — the **feature store** (Feast, Tecton; offline + online store from one
definition, point-in-time-correct joins for training sets) exists to prevent it; log the
features actually used at serving time and train on those logs. Feature importance and
generalization (feature coverage, distribution) as review criteria.

## Model development, evaluation, deployment (Huyen ch. 6–7)
Start simple (heuristics → logistic regression → boosted trees → deep — [[decision-trees-and-ensembles]]);
evaluate on the same data as the baseline; consider training cost, inference latency,
interpretability and retraining frequency, not only accuracy. **Experiment tracking**
(metrics, hyperparameters, data version, code commit, environment — MLflow/W&B) and
**versioning** of data (DVC, lakeFS) for **reproducibility**; distributed training and
AutoML ([[distributed-training-and-ml-systems]]). **Offline evaluation**: a held-out set that
mirrors production, **slice-based** metrics (subgroups, where models hide failures —
[[fairness-in-machine-learning]]), perturbation/invariance/directional tests (CheckList),
calibration, model-based tests against a baseline and the previous model; **online
evaluation**: **shadow** deployment (serve both, log new), **canary** (small traffic
fraction, roll back on regression), **A/B tests** (randomized — [[causal-inference]],
[[hypothesis-testing-and-confidence-intervals]]), **interleaving** for rankers, bandits for
adaptive routing ([[multi-armed-bandits]]). **Deployment**: **batch prediction** (precompute
on a schedule; simple, stale) vs **online prediction** (request-time, latency budget,
feature freshness — streaming features); cloud vs **edge** (privacy, latency, offline;
needs compression — [[llm-inference-and-serving]]); serving via REST/gRPC with a model
registry, containers, autoscaling ([[cloud-and-serverless]]); model compression and
compilation for the target hardware.

## Monitoring, drift, and continual learning — why did my model's accuracy drop after a few months in production? (Huyen ch. 8–9)
Failures: software (dependencies, hardware, downtime) and ML-specific — **production data
differs from training data** (edge cases, degenerate feedback loops: a recommender that
only shows popular items makes them more popular), and **distribution shifts**: **covariate
shift** P(X) changes (new users/devices), **label shift** P(Y) changes, **concept drift**
P(Y | X) changes (the relationship itself — seasonality, adversaries, policy changes);
sudden, gradual, cyclic. **Monitoring**: operational (latency, throughput, errors, CPU/GPU),
**accuracy** when labels arrive (often delayed → proxies), **predictions** (distribution, mode
collapse to one class), **features** (schema validation, ranges, missingness, drift tests —
two-sample KS/MMD on windows, PSI; too many alerts is the practical problem), plus logs,
dashboards, and alerts tied to owners. **Continual learning**: retraining cadence (daily to
per-batch of new data), stateless (from scratch) vs stateful (fine-tune), evaluation before
promotion (**champion–challenger**), fresh vs stale data value curves, feature-reuse,
catastrophic forgetting; **test in production** as the only true test; rollbacks and
versioned models make it safe.

## Data engineering (Reis & Housley; Huyen ch. 3)
Data sources (user input, system logs, internal DBs, third-party), formats (row: CSV/JSON;
column: Parquet/ORC — analytics reads few columns — [[storage-engines-and-indexes]]),
**OLTP vs OLAP** and the warehouse/lake/**lakehouse** convergence ([[distributed-databases-and-nosql]]);
**ETL vs ELT** (transform after loading into the warehouse — dbt); **batch vs streaming**
(Kafka/Flink for real-time features; exactly-once semantics — [[mapreduce-and-dataflow]]);
**orchestration** (DAGs of tasks with retries and backfills — Airflow/Dagster/Prefect;
the pipeline as code); **data quality and validation** (Great Expectations; schema
enforcement; freshness/volume/distribution checks), **lineage** and catalogs, access
control and privacy (PII handling, retention — [[differential-privacy]]); DataOps.
Training pipelines are data pipelines: the same orchestration, the same idempotency and
backfill discipline ([[site-reliability-engineering]] for the on-call side).

## Responsible AI in operations (Huyen ch. 11)
Interpretability requirements by domain ([[interpretability-and-explainability]]), bias
audits per slice ([[fairness-in-machine-learning]]), privacy (data minimization,
differential privacy, federated learning), security (model theft, poisoning, prompt
injection — [[ai-safety-and-alignment]]), model cards and datasheets as documentation,
human-in-the-loop overrides, and incident response for model failures.

## Pitfalls
- Optimizing the offline metric while the business metric moves the other way (proxy
  gaming; no online test).
- Random splits on temporal data; features computed differently online vs offline.
- No monitoring of input distributions (the model "works" on garbage for weeks).
- Retraining on data the model itself selected (feedback loop) without exploration.
- One-off notebooks as the pipeline; unpinned dependencies; untracked data versions.
- Treating a schema change upstream as someone else's problem.

## Related
- [[machine-learning-basics]], [[distributed-training-and-ml-systems]],
  [[llm-inference-and-serving]], [[decision-trees-and-ensembles]], [[causal-inference]],
  [[hypothesis-testing-and-confidence-intervals]], [[multi-armed-bandits]],
  [[fairness-in-machine-learning]], [[interpretability-and-explainability]],
  [[ai-safety-and-alignment]], [[differential-privacy]], [[storage-engines-and-indexes]],
  [[distributed-databases-and-nosql]], [[mapreduce-and-dataflow]], [[cloud-and-serverless]],
  [[site-reliability-engineering]], [[software-engineering-fundamentals]],
  [[technical-debt-and-maintenance]], [[hash-tables]], [[randomized-algorithms]].

## Sources
Huyen, *Designing Machine Learning Systems* 2022 ch. 1–11; CS329S syllabus (read); Sculley et al. 2015; Reis & Housley 2022; Burkov 2020; Full Stack Deep Learning 2022; Made With ML; Sambasivan et al. 2021 (data cascades); Breck et al. 2017 (ML test score); Kohavi et al. 2020.

---
title: Recommender Systems
type: concept
section: "9.5"
level: 400
tags: [recommender-systems, collaborative-filtering, matrix-factorization, cold-start, implicit-feedback]
sources: [computational-social-science-texts-and-seminal-papers]
summary: Predicting what a user will like — content-based vs collaborative filtering, neighborhood methods, matrix factorization (the Netflix Prize), implicit feedback, and cold-start and evaluation.
---

# Recommender Systems
**In one sentence.** A recommender predicts a user's preference for items from past
behavior — either by matching item content to the user's history (content-based) or
by exploiting patterns across many users (collaborative filtering).

## Why it matters
Recommendation drives a large share of consumption on every major platform and is one
of ML's biggest commercial applications. It is also where computational social science
meets ethics: the same engine that surfaces relevant content can create filter
bubbles and amplify misinformation (see
[[computing-ethics-and-professional-responsibility]]).

## How it works
**Content-based filtering.** Represent items by features (genre, text, tags) and
recommend items similar to those a user liked. Handles new items well; limited to the
user's existing profile ("more of the same").

**Collaborative filtering (CF).** Use the user-item interaction matrix, ignoring
content:
- **Neighborhood / memory-based** — *user-user* ("people like you liked…") or
  *item-item* ("people who bought this also bought…", Amazon's method) similarity via
  cosine or Pearson. Simple and explainable; struggles with sparsity and scale.
- **Model-based: matrix factorization.** Factor the sparse `m×n` rating matrix
  `R ≈ U Vᵀ` into `k`-dimensional user and item **latent factors**; predict rating as
  the dot product `uᵢ · vⱼ`. Learn by minimizing squared error on *observed* entries
  plus L2 regularization, via SGD or alternating least squares. The **Netflix Prize
  (2006–09)** made this the dominant technique. It is the recommender face of
  [[svd-and-pca]].

**Implicit feedback.** Most signals are clicks/plays/purchases, not ratings — positive
-only and confounded with exposure. Methods (weighted ALS, Bayesian Personalized
Ranking) treat unobserved items as weak negatives and optimize *ranking* rather than
rating accuracy.

**Modern pipelines** are two-stage: a cheap **candidate generation** step (embeddings
+ approximate nearest neighbors, or [[graph-neural-networks]] on the user-item graph)
retrieves hundreds of items, then a heavier **ranking** model (gradient-boosted trees
or deep nets) scores them with rich features.

**Evaluation.** Offline: ranking metrics — precision@k, recall@k, **NDCG**, MAP — on
held-out interactions (the same metrics as [[evaluation-of-ir-systems]]). Online: A/B
tests on engagement, since offline metrics correlate imperfectly with real value; see
[[usability-evaluation-and-user-research]].

## Complexity & trade-offs
- Neighborhood CF is explainable but O(users²) or O(items²) similarity; item-item
  precomputes well and is stable as users change.
- Matrix factorization scales to large sparse matrices (cost ∝ observed entries × k)
  and generalizes better, at the cost of interpretability.

## Pitfalls & gotchas
- **Cold start** — new users/items have no interactions; fall back to content or
  popularity, or ask onboarding questions.
- **Popularity bias & feedback loops** — recommending popular items generates more
  data for them, entrenching them and shrinking diversity.
- **Exposure bias in implicit data** — you only observe feedback on what was shown;
  naive training conflates "not shown" with "disliked."
- **Optimizing engagement proxies** can amplify sensational content (Goodhart's law).

## Worked example
A movie site with a sparse rating matrix runs matrix factorization with k=50 latent
factors. A user who rated three sci-fi films highly gets a user vector aligned with
the "sci-fi" latent direction; unrated films whose item vectors point the same way
score high and are recommended — even ones sharing no explicit tags, because the
latent factors captured the pattern from other users' co-ratings.

## Related
- [[network-science]] — recommendation as link prediction on a bipartite graph.
- [[graph-neural-networks]] — modern graph-based candidate generation.
- [[svd-and-pca]] — matrix factorization is low-rank approximation.
- [[evaluation-of-ir-systems]] — NDCG/precision@k are shared ranking metrics.
- [[computing-ethics-and-professional-responsibility]] — filter bubbles and amplification.

## Sources
Distilled from [[computational-social-science-texts-and-seminal-papers]] (*Mining of
Massive Datasets*; Netflix Prize / Koren et al.; item-item CF).

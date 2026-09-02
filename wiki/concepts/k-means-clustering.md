---
title: k-means clustering
type: concept
section: "1.2"
level: 200
tags: [k-means, clustering, unsupervised, lloyd-algorithm, alternating-minimization, centroids, k-means-plus-plus, distance]
sources: [boyd-vmls]
summary: Partition vectors into k groups by minimizing the sum of squared distances to group centroids; Lloyd's alternating assign/recompute algorithm always decreases the objective and converges to a local optimum, so run it several times from k-means++ seeds and pick the best.
---
# k-means clustering

**In one sentence.** Choose assignments c₁…c_N ∈ {1..k} and representatives z₁…z_k to minimize
J = (1/N) Σ ‖xᵢ − z_{cᵢ}‖²; alternate the two easy sub-problems until nothing changes.

## Lloyd's algorithm (VMLS 4.3)
1. Given z's, assign each xᵢ to its nearest zⱼ (assignment step, N·k distance evaluations).
2. Given assignments, set each zⱼ to the mean of its group (update step) — the mean minimizes the sum
   of squared distances to a set of points.
Each step cannot increase J, J ≥ 0, finitely many partitions ⇒ converges (usually in tens of
iterations). Cost O(Nkd) per iteration.

## Practicalities
- Result depends on initialization ⇒ run 10+ times, keep the lowest J; **k-means++** seeds pick points
  with probability ∝ squared distance to the nearest seed (O(log k)-competitive in expectation).
- Choosing k: plot J vs k (elbow), silhouette score, or domain knowledge; J always decreases with k.
- Scale features (VMLS: standardize) or the largest-variance feature dominates; k-means assumes roughly
  spherical, equal-size clusters — fails on rings, elongated or very unequal clusters (use GMM/EM,
  spectral clustering, DBSCAN — §6.2).
- Applications in VMLS: topic discovery from word-count vectors, digit clustering, colour quantization
  (image compression), vector quantization for ANN indexes ([[ann-search]]).

## Pitfalls
- Empty clusters after the assignment step: re-seed that centroid.
- Squared Euclidean is the *only* distance for which the mean is the optimal representative; with cosine
  similarity use spherical k-means (normalize, use mean direction); with L1 use k-medians.

## Related
- [[vectors-and-inner-products]] — distances; [[svd-and-pca]] — reduce dimension first;
  [[expectation-maximization]] — the soft version (§6.2).

## Sources
VMLS ch. 4.

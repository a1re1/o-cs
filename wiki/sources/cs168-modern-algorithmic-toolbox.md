---
title: Stanford CS168 The Modern Algorithmic Toolbox (Valiant / Roughgarden) with MIT 6.851 and 6.854
type: source
section: "3.3"
level: 400
tags: [cs168, consistent-hashing, bloom-filters, count-min-sketch, heavy-hitters, similarity-search, minhash, lsh, johnson-lindenstrauss, dimension-reduction, generalization, regularization, pca, svd, spectral-graph-theory, sampling, reservoir-sampling, mcmc, fourier, multiplicative-weights, convex-optimization, linear-programming, compressive-sensing, differential-privacy, advanced-data-structures, persistence]
sources: []
institution: Stanford / MIT
year: 2024
url: https://web.stanford.edu/class/cs168/
license: open-course
format: html
summary: CS168 is a week-per-idea tour of the modern toolkit with mini-projects — consistent hashing; heavy hitters from Bloom filters to count-min sketch; similarity search with k-d trees, MinHash, Johnson–Lindenstrauss and LSH; generalization and regularization; PCA and SVD; spectral graph theory; reservoir/importance sampling and MCMC; Fourier methods; multiplicative weights and convex optimization; linear programming; compressive sensing; differential privacy — while MIT 6.851 (Demaine) covers persistence, van Emde Boas, fusion trees, cache-oblivious and succinct structures, and 6.854 covers advanced algorithms (flows, LP, approximation, online, streaming).
---
# CS168 The Modern Algorithmic Toolbox / 6.851 / 6.854

## What it is
CS168 weeks: 1 modern hashing — consistent hashing (the Akamai paper), property-preserving lossy
compression: majority → heavy hitters, Bloom filters → count-min sketch; 2 data with distances —
Jaccard/Euclidean/Lp, k-d trees for < 20 dims, curse of dimensionality and kissing numbers,
MinHash for Jaccard, Johnson–Lindenstrauss for Euclidean, locality-sensitive hashing; 3
generalization and regularization — how much data is enough, PAC guarantees for linear
classifiers, ERM, L2/L1 (as tractable L0) regularization; 4–5 linear algebra — PCA (max variance
= min squared distance; power iteration; failure modes), SVD and low-rank approximation, matrix
completion, tensor methods (Jennrich); 6 spectral graph theory — Laplacian eigenvectors,
conductance, λ₂ and random-walk mixing, spectral clustering; 7 sampling and estimation —
reservoir sampling, Markov/Chebyshev, importance sampling, Good–Turing, Markov chains and MCMC;
8 the Fourier perspective — convolution and its uses; 9 online learning with multiplicative
weights, convex optimization; 10 linear programming, compressive sensing/sparse recovery,
differential privacy.
**6.851** (Demaine, videos): temporal (partial/full/confluent/functional persistence, retroactivity),
geometric (range trees, fractional cascading, kinetic), dynamic optimality (splay, tango trees),
memory hierarchy (cache-oblivious B-trees, sorting), dictionaries (hashing, cuckoo), integer
structures (van Emde Boas, y-fast tries, fusion trees, predecessor lower bounds), string
structures (suffix trees/arrays, document retrieval), succinct (rank/select, succinct trees),
dynamic graphs (link-cut trees, Euler tour trees). **6.854**: fibonacci heaps, splay trees,
persistent structures, hashing, flows, LP and duality, approximation, online algorithms,
streaming, matchings.

## Key ideas → pages
- [[streaming-and-sketching]] (Bloom, count-min, heavy hitters, reservoir sampling, HyperLogLog).
- [[similarity-search-and-lsh]] (MinHash, JL, LSH, nearest neighbours).
- [[approximation-algorithms]]; [[advanced-data-structures]] (persistence, vEB, cache-oblivious,
  succinct); [[consistent-hashing]]; spectral methods link to [[svd-and-pca]] and
  [[eigenvalues-and-eigenvectors]]; multiplicative weights to [[online-learning-and-regret]].

## What it adds
The bridge from §3 algorithms to §8–9 ML and systems: the same handful of ideas (hashing,
sketching, random projection, spectra, sampling) appear in databases, networks and learning.

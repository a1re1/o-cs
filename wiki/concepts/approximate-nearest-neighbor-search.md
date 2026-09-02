---
title: Approximate Nearest Neighbor Search
type: concept
section: "10.3"
level: 400
tags: [ann-search, hnsw, faiss, product-quantization, vector-search, ivf]
sources: [manning-irb]
summary: Finding near-duplicates in high-dimensional vector space fast — why exact search fails (curse of dimensionality), and how HNSW graphs, IVF, and product quantization trade a little recall for large speedups.
---

# Approximate Nearest Neighbor Search
**In one sentence.** ANN search finds the vectors closest to a query vector in
sub-linear time by accepting a small chance of missing the true nearest neighbor,
making [[dense-retrieval-and-embeddings]] and vector databases practical at scale.

## Why it matters
Dense retrieval, recommendation, deduplication, and RAG all reduce to "find the k
nearest vectors among millions." Exact search is O(N·dim) per query — too slow — and
tree methods (kd-trees) collapse to linear scan in high dimensions (the **curse of
dimensionality**). ANN indexes are what make vector search fast enough to serve.

## How it works
**HNSW — Hierarchical Navigable Small World (Malkov & Yashunin 2016).** Build a
multi-layer proximity graph: upper layers are sparse (long hops), lower layers dense
(fine steps), echoing skip lists. Search greedily descends from an entry point,
walking to ever-closer neighbors — a small-world graph (see [[network-science]]) so a
few hops reach any region. Gives high recall at ~O(log N) hops; the leading in-memory
method. Parameters: `M` (graph degree) and `efSearch` (candidate breadth) trade recall
for speed and memory.

**IVF — Inverted File (cluster-then-search).** Cluster all vectors (k-means) into cells;
at query time probe only the `nprobe` nearest cells. Cuts the search space by the number
of cells; recall depends on `nprobe`.

**Product Quantization (PQ).** Compress vectors by splitting each into sub-vectors and
quantizing each to a small codebook, so a vector becomes a few bytes. Distances are
computed approximately from precomputed lookup tables, shrinking memory 10–100× and
speeding distance computation. IVF-PQ (FAISS) combines both for billion-scale search.

## Complexity & trade-offs
- **HNSW** — fastest and highest recall in RAM, but high memory (stores the graph) and
  slow, non-incremental to build; deletions are awkward.
- **IVF-PQ** — compact enough for billion-scale on disk/RAM, tunable via `nprobe`, but
  lower recall at the same speed and needs training the quantizer.
- All ANN methods expose a **recall–latency–memory** triangle; there is no free lunch,
  only a chosen operating point.

## Pitfalls & gotchas
- **Silent recall loss** — too-low `efSearch`/`nprobe` drops relevant results with no
  error; measure recall against exact search on a sample.
- **Metric mismatch** — the index must use the same metric (cosine vs L2 vs inner
  product) the embeddings were trained for; normalize vectors for cosine.
- **Updates** — HNSW is costly to rebuild; high-churn corpora may prefer IVF or periodic
  reindexing.

## Worked example
Ten million 384-dim passage embeddings. An HNSW index with `M=16` answers a query in
under a millisecond by walking ~a few hundred graph nodes instead of scoring all 10M,
returning the top 20 with ~98% recall — tune `efSearch` up if recall matters more than
latency for a given query load.

## Related
- [[dense-retrieval-and-embeddings]] — ANN is what makes dense retrieval servable.
- [[similarity-search-and-lsh]] — LSH is the hashing-based ANN alternative.
- [[network-science]] — HNSW is a navigable small-world graph.
- [[k-means-clustering]] — IVF uses k-means to build cells.

## Sources
Distilled from [[manning-irb]] (Malkov & Yashunin HNSW 2016; Johnson et al. FAISS 2017).

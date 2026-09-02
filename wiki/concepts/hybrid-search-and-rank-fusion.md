---
title: Hybrid Search and Rank Fusion
type: concept
section: "10.3"
level: 400
tags: [hybrid-search, reciprocal-rank-fusion, rrf, lexical-dense, ensemble-ranking, score-normalization]
sources: [manning-irb]
summary: Combining lexical (BM25) and dense (embedding) retrieval into one ranking — why each catches what the other misses, and how reciprocal rank fusion (RRF) merges result lists without comparing incomparable scores.
---

# Hybrid Search and Rank Fusion
**In one sentence.** Hybrid search runs lexical [[bm25]] and
[[dense-retrieval-and-embeddings]] in parallel and fuses their result lists, because
each method catches relevant documents the other misses; **reciprocal rank fusion (RRF)**
is the simple, robust way to merge them.

## Why it matters
BM25 nails exact terms, rare identifiers, names, and numbers but is blind to synonyms;
dense retrieval captures meaning but smears exact matches and degrades out of domain.
Fusing them consistently beats either alone — the standard modern retrieval design and
exactly what the [[oasis-search-engine]] does.

## How it works
**The fusion problem.** BM25 scores are unbounded sums; cosine similarities live in
[−1, 1]. They are **not comparable**, so you cannot simply add them. Two families of
solution:

**1. Score normalization (weighted sum).** Rescale each system's scores (min-max or
z-score) to a common range, then take a weighted combination
`α·bm25' + (1−α)·dense'`. Effective but fragile: min-max is sensitive to outliers, and
the best `α` varies by query and corpus, needing tuning.

**2. Reciprocal Rank Fusion (RRF, Cormack et al. 2009).** Ignore scores entirely; use
only **ranks**. For a document `d` appearing at rank `r_s(d)` in each system `s`:

```
RRF(d) = Σ_s  1 / (k + r_s(d))         (k ≈ 60 by convention)
```

A document ranked high by *either* system gets a large contribution; being top of both
is best. The constant `k` damps the influence of very top ranks so a single system
can't dominate. RRF needs **no score normalization and no tuning**, is robust across
corpora, and often matches or beats carefully tuned weighted sums — which is why it is
the default fusion method.

**Two-stage pattern.** Hybrid retrieval usually produces candidates that a
cross-encoder then **re-ranks** (see [[dense-retrieval-and-embeddings]]); fusion is the
candidate-merging step, re-ranking is the precision step on top.

## Complexity & trade-offs
- RRF is O(results) to merge and parameter-light (just `k`), at the cost of discarding
  score *magnitude* information a well-tuned weighted sum could use.
- Weighted-sum fusion can exploit score gaps but must be re-tuned per corpus and is
  sensitive to normalization choice and outliers.
- Running both retrievers doubles retrieval cost, but the recall gain is usually worth
  it; the dense side dominates latency/memory (see
  [[approximate-nearest-neighbor-search]]).

## Pitfalls & gotchas
- **Adding raw scores** from BM25 and cosine — meaningless; normalize or use RRF.
- **Over-tuning `α`** on a small query set overfits; RRF sidesteps this.
- **Duplicate/near-duplicate documents** inflate fused scores; dedupe before fusing.
- **Choosing `k`** in RRF: too small over-weights the very top ranks; ~60 is the tested
  default.

## Worked example
Query "raft consensus". BM25 ranks the page with the literal term "Raft" at position 1
but misses a page titled "leader election and log replication" (no "raft" token). The
dense retriever ranks that conceptual page at position 2. RRF gives the literal page
`1/(60+1)` from BM25 plus a lower dense contribution, and the conceptual page a solid
dense contribution — so both surface in the top results, which neither method alone
achieved.

## Related
- [[bm25]] — the lexical input to fusion.
- [[dense-retrieval-and-embeddings]] — the semantic input to fusion.
- [[evaluation-of-ir-systems]] — how the fused ranking is measured.
- [[oasis-search-engine]] — this wiki's engine fuses BM25 and dense with RRF (k=60).

## Sources
Distilled from [[manning-irb]] (Cormack, Clarke & Büttcher RRF 2009).

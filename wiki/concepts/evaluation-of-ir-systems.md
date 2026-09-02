---
title: Evaluation of IR Systems
type: concept
section: "10.3"
level: 400
tags: [evaluation-ir, precision-recall, map, ndcg, mrr, test-collections, relevance-judgments]
sources: [manning-irb]
summary: How search quality is measured — precision/recall, MAP, MRR, and nDCG over test collections with relevance judgments, plus the online/offline distinction and pooling.
---

# Evaluation of IR Systems
**In one sentence.** IR evaluation measures how well a ranking puts relevant documents
near the top, using rank-aware metrics — precision@k, recall@k, MAP, MRR, and nDCG —
computed over a test collection of queries with human relevance judgments.

## Why it matters
"Better search" is meaningless without a metric. These measures let you compare BM25 vs
dense retrieval, tune parameters without overfitting, and prove a change helps rather
than hurts. This project's own [[oasis-search-engine]] is tracked with exactly these
metrics (recall@k, MRR, nDCG@3) on a growing query set.

## How to measure whether a search ranking is good

## How it works
**The test collection (Cranfield paradigm):** a document corpus, a set of queries, and
**relevance judgments** (which documents are relevant to which query). Metrics are
averaged over queries.

**Set metrics (unranked):**
- **Precision** = relevant retrieved / retrieved. **Recall** = relevant retrieved /
  all relevant. They trade off; **F1** is their harmonic mean.
- **Precision@k / Recall@k** — restricted to the top k, matching how users read.

**Rank-aware metrics:**
- **MRR (Mean Reciprocal Rank)** — `1/rank` of the *first* relevant result, averaged.
  Ideal for known-item / navigational search where one right answer exists.
- **MAP (Mean Average Precision)** — average of precision values at each relevant
  document's rank, averaged over queries; rewards putting *all* relevant docs high.
- **nDCG (normalized Discounted Cumulative Gain)** — sums each result's *graded*
  relevance discounted by `1/log2(rank+1)`, normalized by the ideal ordering (IDCG).
  The standard for graded relevance and web search; nDCG@3 weights the very top.

```
DCG@k = Σ_{i=1..k} rel_i / log2(i + 1)      nDCG@k = DCG@k / IDCG@k
```

**Pooling.** Judging every document per query is infeasible at scale, so **pool** the
top results from several systems and judge only those; unjudged documents are treated
as non-relevant (a known bias against novel systems).

**Online vs offline.** Offline metrics use fixed judgments; **online** evaluation runs
A/B tests and interleaving on live traffic with implicit signals (clicks, dwell time) —
see [[usability-evaluation-and-user-research]]. Click data is biased toward higher
ranks (**position bias**), which counterfactual/IPW methods correct.

## Complexity & trade-offs
- **MRR** is cheap and intuitive but ignores everything after the first hit; **nDCG**
  captures the whole ranking and graded relevance but needs graded judgments.
- Offline metrics are reproducible but may not reflect real user value; online metrics
  are truthful but slow, costly, and risk exposing users to worse results.

## Pitfalls & gotchas
- **Tuning on the test set** inflates results; hold out queries or cross-validate.
- **Incomplete judgments** penalize systems that retrieve relevant-but-unjudged
  documents; be wary of comparing to old pooled collections.
- **Averaging hides variance** — report per-query and significance (paired t-test /
  randomization), not just the mean.
- **Position bias** in click logs makes naive click-through rate a misleading metric.

## Worked example
Two rankers on 100 queries. Ranker A puts the answer at rank 1 for 60 queries and rank
5 for the rest; B puts it at rank 2 for all. A's MRR = 0.6·1 + 0.4·0.2 = 0.68; B's MRR
= 0.5. A wins on MRR despite B being more consistent — which is "better" depends on
whether users need the top hit right (favor A) or tolerate scanning a few (B looks
steadier on nDCG@5).

## Related
- [[bm25]] — the ranker most often evaluated with these metrics.
- [[dense-retrieval-and-embeddings]] — compared against BM25 using these metrics.
- [[recommender-systems]] — shares precision@k, NDCG, MAP.
- [[usability-evaluation-and-user-research]] — online A/B evaluation of search.
- [[oasis-search-engine]] — evaluated with recall@k, MRR, nDCG@3 on this corpus.

## Sources
Distilled from [[manning-irb]] (IIR ch. 8; TREC methodology).

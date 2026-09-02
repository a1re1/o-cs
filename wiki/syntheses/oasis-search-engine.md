---
title: The oasis Search Engine (this wiki's own retrieval)
type: synthesis
section: "10.3"
level: 400
tags: [oasis, hybrid-search, bm25, dense-retrieval, rrf, chunking, evaluation-ir]
sources: [manning-irb]
summary: How oasis — the hybrid BM25 + dense CLI search engine that indexes this wiki — is built, mapped onto the IR concepts it implements, and how its retrieval quality is evaluated on this corpus.
---

# The oasis Search Engine (this wiki's own retrieval)
**In one sentence.** `oasis` is the hybrid search engine that indexes this very wiki
so coding agents can pull CS knowledge on demand; it is a concrete instance of the IR
concepts in §10.3, combining lexical BM25 with dense embeddings via reciprocal rank
fusion.

## Why it matters
This page grounds the abstract IR theory in a system the reader can run, and records
the design and evaluation decisions specific to searching *this* corpus. It is also the
target of the project's search-quality experiments (see the experiments report).

## Architecture, mapped to the concepts
- **Chunking.** Pages are split into heading-aware chunks (~256 tokens, ~32 overlap) so
  a hit points at the relevant section, not a whole page. Chunk size is the classic
  passage-retrieval trade-off from [[dense-retrieval-and-embeddings]] — too large
  dilutes the vector, too small loses context.
- **Lexical channel.** An [[inverted-index]] scored with [[bm25]], plus a **heading
  boost** (~2.0) so terms in section headings weigh more — BM25F-style field weighting.
  This is why phrasing a query to match a page's heading reliably lifts it (a repeatedly
  observed effect in this wiki's evals).
- **Dense channel.** A bi-encoder (bge-small via ONNX Runtime) embeds chunks and the
  query; retrieval is nearest-neighbor over the vectors — [[dense-retrieval-and-embeddings]]
  and [[approximate-nearest-neighbor-search]].
- **Fusion.** The two ranked lists are merged with **reciprocal rank fusion**, `k=60` —
  [[hybrid-search-and-rank-fusion]] — so a chunk ranked well by *either* channel
  surfaces, with no score normalization needed.
- **Filtering.** `--ignore <GLOB>` excludes paths and `--per-page N` caps hits per page
  (dedup), features added and measured against this corpus's evals.

## Evaluation on this corpus
Retrieval quality is tracked with the metrics from [[evaluation-of-ir-systems]] —
recall@k, MRR, and nDCG@3 — over a growing `queries.jsonl` of labeled
`{query, relevant, section, kind}` rows spanning keyword, question, paraphrase, source,
compare, howto, concept, and lookup query styles. Each corpus change is checked to not
regress the eval; results are appended to a history file and summarized in the
experiments report. A consistent finding: **paraphrase** queries (semantic, few shared
terms) are the hardest for the lexical channel, which is the motivation for the dense
channel and for heading-term coverage.

## Trade-offs & lessons
- **Lexical vs dense complementarity** is real here: exact-term and source-title
  queries favor BM25; conceptual/paraphrase queries favor dense — fusion captures both.
- **Heading terms are high-leverage**: because of the heading boost, using a
  practitioner's exact vocabulary in section headings materially improves recall.
- **Chunking granularity** governs whether the right *section* is returned, not just
  the right page.

## Related
- [[bm25]], [[inverted-index]] — the lexical channel.
- [[dense-retrieval-and-embeddings]], [[approximate-nearest-neighbor-search]] — the dense channel.
- [[hybrid-search-and-rank-fusion]] — the RRF fusion oasis uses.
- [[evaluation-of-ir-systems]] — the metrics tracking oasis's quality.
- [[manning-irb]] — the textbook whose concepts oasis instantiates.

## Sources
The IR concepts are distilled from [[manning-irb]]; the system details describe this
project's `oasis` deployment and its evaluation harness.

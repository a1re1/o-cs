---
title: Dense Retrieval and Embeddings
type: concept
section: "10.3"
level: 400
tags: [dense-retrieval, embeddings, dpr, colbert, semantic-search, bi-encoder, ann-search]
sources: [manning-irb]
summary: Neural semantic search — encode queries and documents into dense vectors with a bi-encoder, retrieve by nearest-neighbor vector similarity, and understand DPR, ColBERT late interaction, and cross-encoder re-ranking.
---

# Dense Retrieval and Embeddings
**In one sentence.** Dense retrieval encodes queries and documents into learned dense
vectors so that semantically similar text lands nearby in vector space, and retrieves
by nearest-neighbor search — matching meaning where lexical [[bm25]] matches only words.

## Why it matters
Lexical search fails on the **vocabulary mismatch** problem: "heart attack" vs
"myocardial infarction" share no terms yet mean the same thing. Dense retrieval closes
that gap and is the retrieval half of **RAG** (retrieval-augmented generation) for LLMs.
The dense half of the [[oasis-search-engine]] uses exactly this. It builds on
[[transformers-and-attention]] and [[approximate-nearest-neighbor-search]].

## How semantic search matches meaning, not just keywords

## How it works
**Bi-encoder (the standard architecture).** A transformer encoder (e.g. BERT, or a
small model like bge-small) maps a query to a vector `q` and each document to a vector
`d`, independently. Relevance = `q · d` (dot product or cosine). Because documents are
encoded **offline**, retrieval at query time is just a nearest-neighbor search over
precomputed vectors.

**Training (DPR, Karpukhin et al. 2020).** Learn the encoders with a **contrastive**
objective: pull a query toward its relevant (positive) passage and push it away from
negatives, especially **hard negatives** (BM25-retrieved wrong passages) and in-batch
negatives. This shapes the space so relevant pairs are close. See
[[self-supervised-and-contrastive-learning]].

**Approximate nearest neighbors (ANN).** Exact nearest-neighbor over millions of
vectors is too slow, so use an index — **HNSW** (a navigable small-world graph, Malkov
& Yashunin 2016) or IVF-PQ (FAISS) — for sub-linear, high-recall search. See
[[approximate-nearest-neighbor-search]].

**Interaction spectrum (accuracy vs cost):**
- **Bi-encoder** — one vector per query/doc; fast (ANN-searchable), least expressive.
- **ColBERT late interaction (Khattab & Zaharia 2020)** — keep a vector *per token*,
  score by summing each query token's max similarity over document tokens
  (MaxSim); more accurate, larger index.
- **Cross-encoder re-ranker (Nogueira & Cho 2019)** — feed the query and document
  *together* through a transformer for one relevance score; most accurate, but O(candidates)
  transformer passes, so only used to re-rank the top ~100 from a cheaper retriever.

The production pattern is **retrieve-then-rerank**: BM25 and/or a bi-encoder fetch
candidates, a cross-encoder re-ranks them.

## Complexity & trade-offs
| Method | Query cost | Index size | Semantic |
|---|---|---|---|
| BM25 (lexical) | posting scan | small | no |
| Bi-encoder + ANN | one encode + ANN | 1 vec/doc | yes |
| ColBERT | ANN + MaxSim | many vecs/doc | more |
| Cross-encoder | k transformer passes | none (rerank) | most |

Dense retrieval needs training data and a GPU to encode; it can **miss exact matches**
(names, codes, rare terms) that BM25 nails — the core reason to combine them via
[[hybrid-search-and-rank-fusion]].

## Pitfalls & gotchas
- **Out-of-domain collapse** — an encoder trained on one domain retrieves poorly on
  another; BM25 is more robust zero-shot.
- **Exact/rare-term blindness** — dense vectors smear rare identifiers; keep a lexical
  channel for codes, names, and numbers.
- **Chunking matters** — documents must be split into passages of a size the encoder
  handles; too large dilutes the vector, too small loses context.
- **ANN recall vs speed** — HNSW parameters (M, efSearch) trade recall for latency; a
  low ef silently drops relevant results.

## Worked example
Query "how do I stop my program from using too much memory". BM25 keys on "memory"
and "program" and may surface off-topic hits. A bi-encoder maps the query near
passages about "reducing heap allocation" and "avoiding memory leaks" that share few
literal words — then a cross-encoder re-ranks the top 50 to put the best fix first.

## Related
- [[bm25]] — the lexical counterpart dense retrieval complements.
- [[hybrid-search-and-rank-fusion]] — combining dense and lexical scores.
- [[approximate-nearest-neighbor-search]] — HNSW/FAISS make dense retrieval fast.
- [[transformers-and-attention]] — the encoders producing embeddings.
- [[self-supervised-and-contrastive-learning]] — how the vector space is trained.
- [[oasis-search-engine]] — this wiki's dense channel uses a bi-encoder.

## Sources
Distilled from [[manning-irb]] (Lin et al. *Pretrained Transformers for Text Ranking*;
DPR 2020; ColBERT 2020; HNSW 2016).

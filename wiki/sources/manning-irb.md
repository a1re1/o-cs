---
title: Introduction to Information Retrieval (Manning, Raghavan & Schütze, 2008)
type: source
section: "10.3"
level: 400
tags: [information-retrieval, bm25, inverted-index, vector-space, dense-retrieval, evaluation-ir]
authors: Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze
year: 2008
institution: Stanford
url: https://nlp.stanford.edu/IR-book/
license: free
format: textbook
sources: []
summary: The standard free IR textbook (Manning, Raghavan & Schütze) plus the IR canon it anchors — the inverted index, tf-idf and the vector space model, BM25, evaluation metrics, and the seminal papers through dense retrieval and HNSW.
---

# Introduction to Information Retrieval (Manning, Raghavan & Schütze, 2008)

## What it is
The definitive free undergraduate/graduate **information retrieval** textbook ("IIR"),
covering how search engines index and rank text. It is the theoretical backbone of
any keyword-plus-semantic search system — including the [[oasis-search-engine]] that
searches this wiki. This page also anchors the broader IR canon (CS276; Croft's
*Search Engines*; the dense-retrieval papers).

## Key ideas
- **The inverted index** — the core data structure mapping terms to posting lists.
  See [[inverted-index]].
- **tf-idf and the vector space model** — the classic term-weighting and
  cosine-similarity scoring. See [[tf-idf-and-vector-space-model]].
- **BM25** — the probabilistic ranking function that dominates lexical search. See [[bm25]].
- **Evaluation** — precision/recall, MAP, nDCG, and test collections. See
  [[evaluation-of-ir-systems]].
- **Dense retrieval & ANN** — embedding-based semantic search and approximate nearest
  neighbors. See [[dense-retrieval-and-embeddings]].
- **Hybrid search & rank fusion** — combining lexical and dense signals. See
  [[hybrid-search-and-rank-fusion]].

## Chapter / lecture map
- Ch 1–2: Boolean retrieval, the inverted index, tokenization, normalization.
- Ch 5: index compression (variable-byte, gamma codes).
- Ch 6: tf-idf and the vector space model.
- Ch 8: evaluation (precision, recall, MAP, nDCG, interpolated precision).
- Ch 9: relevance feedback, query expansion (Rocchio).
- Ch 11: probabilistic IR — the binary independence model and **BM25**.
- Ch 12: language models for IR (query likelihood).
- Ch 13–17: text classification and clustering.
- Ch 19–21: web search, crawling, link analysis (PageRank/HITS).

## Notable claims & quotes
- The inverted index makes retrieval time depend on the number of *matching* documents,
  not the collection size — the reason web-scale search is feasible.
- BM25's saturation of term frequency (a word appearing 20 times is not 20× as
  relevant as once) is the key improvement over raw tf-idf.

## Seminal papers (the IR spine)
- **Salton, vector space model (1975)** — documents as term vectors; cosine similarity.
- **Robertson & Spärck Jones (1976); Robertson et al. BM25 (1994)** — probabilistic
  relevance; the Okapi BM25 function.
- **Spärck Jones (1972)** — inverse document frequency (idf).
- **Brin & Page (1998)** — "Anatomy of a Large-Scale Hypertextual Web Search Engine"
  (Google; PageRank + IR). See [[network-science]].
- **Broder (2002)** — a taxonomy of web search (navigational/informational/transactional).
- **Karpukhin et al., DPR (2020); Khattab & Zaharia, ColBERT (2020)** — dense passage
  retrieval and late interaction.
- **Malkov & Yashunin, HNSW (2016); Johnson et al., FAISS (2017)** — approximate
  nearest-neighbor search.
- **Nogueira & Cho (2019)** — BERT cross-encoder re-ranking; **Burges, LambdaMART** —
  learning to rank.

## What it adds
Turns "search" from a black box into a stack of well-understood components. Directly
informs this project's own [[oasis-search-engine]] (BM25 + dense + reciprocal rank
fusion), and connects to [[nlp-fundamentals]], [[transformers-and-attention]], and
[[recommender-systems]] (shared ranking metrics).

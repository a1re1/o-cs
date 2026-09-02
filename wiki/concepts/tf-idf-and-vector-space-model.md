---
title: tf-idf and the Vector Space Model
type: concept
section: "10.3"
level: 400
tags: [tf-idf, vector-space-model, cosine-similarity, term-weighting, ranking]
sources: [manning-irb]
summary: The classic IR scoring scheme — weight terms by term frequency times inverse document frequency, represent documents and queries as vectors, and rank by cosine similarity.
---

# tf-idf and the Vector Space Model
**In one sentence.** Represent each document and query as a vector over the vocabulary,
weight each term by **tf-idf** (frequent in this document, rare across the collection),
and rank documents by the cosine of the angle to the query vector.

## Why it matters
tf-idf is the foundational term-weighting idea in all of IR and text mining; it is the
baseline every ranker (including [[bm25]]) refines, a standard feature for text
classification, and the intuition behind why rare words are informative. It formalizes
"a word matters if it's frequent here but rare elsewhere."

## How it works
**Term frequency (tf).** How often term `t` occurs in document `d`. Raw counts
over-reward repetition, so it is usually dampened: `1 + log(tf)`.

**Inverse document frequency (idf).** How rare `t` is across the collection of `N`
documents with document frequency `df`:

```
idf(t) = log( N / df(t) )
```

Common words (high df) get low idf; rare, discriminating words get high idf. This is
Spärck Jones's 1972 insight.

**tf-idf weight:** `w(t,d) = tf(t,d) · idf(t)`.

**Vector space model (Salton 1975).** Each document is a vector of tf-idf weights over
the vocabulary axes; the query is such a vector too. Rank by **cosine similarity**:

```
cos(q, d) = (q · d) / (‖q‖ · ‖d‖)
```

Cosine (not raw dot product) normalizes for document length, so a long document isn't
favored merely for containing more words. Storing **length-normalized** weights lets
scoring stream over an [[inverted-index]].

## Complexity & trade-offs
- Scoring is O(query terms × their posting lengths) over the inverted index; the vocab
  dimension is huge but vectors are sparse, so only nonzero terms are touched.
- Purely lexical: it has **no notion of synonymy or polysemy** ("car" vs "automobile"
  score zero similarity). Latent semantic indexing (SVD on the term-document matrix;
  see [[svd-and-pca]]) and later [[dense-retrieval-and-embeddings]] address this.

## Pitfalls & gotchas
- **Raw tf without damping** lets keyword stuffing dominate; log-scale or BM25
  saturation fixes it.
- **Cosine ignores term proximity and order** — "dog bites man" ≈ "man bites dog".
- **Out-of-vocabulary and rare-term idf instability** on small collections; smooth idf.
- tf-idf is a heuristic, not a probabilistic model — [[bm25]] derives similar behavior
  from a relevance model and usually wins.

## Worked example
Collection of 1,000,000 docs. The word "the" appears in ~all of them: idf ≈ log(1e6/1e6)
= 0, so it contributes nothing regardless of frequency. "photosynthesis" appears in 100
docs: idf = log(1e6/100) ≈ 4. A document mentioning "photosynthesis" three times scores
`(1+log3)·4 ≈ 5.9` on that axis, dominating the cosine — exactly the discriminating
term we want to rank on.

## Related
- [[bm25]] — the probabilistic ranker that improves on tf-idf with tf saturation.
- [[inverted-index]] — the structure tf-idf scoring runs over.
- [[svd-and-pca]] — latent semantic indexing addresses tf-idf's synonymy blindness.
- [[dense-retrieval-and-embeddings]] — the neural successor for semantic matching.

## Sources
Distilled from [[manning-irb]] (IIR ch. 6; Salton 1975; Spärck Jones 1972).

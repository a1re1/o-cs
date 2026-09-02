---
title: Inverted Index
type: concept
section: "10.3"
level: 400
tags: [inverted-index, posting-list, tokenization, index-compression, search]
sources: [manning-irb]
summary: The core search data structure mapping each term to its posting list of documents, enabling query time proportional to matches rather than collection size; plus tokenization, skip pointers, and compression.
---

# Inverted Index
**In one sentence.** An inverted index maps each *term* to a **posting list** of the
documents (and positions) containing it, so a query is answered by intersecting or
merging a few short lists instead of scanning every document.

## Why it matters
The inverted index is why full-text search over billions of documents returns in
milliseconds: retrieval cost scales with the number of *matching* documents, not the
collection size. It is the substrate under Lucene, Elasticsearch, and the lexical half
of the [[oasis-search-engine]]. Everything in [[bm25]] and
[[tf-idf-and-vector-space-model]] is scored *over* an inverted index.

## How it works
**Build (indexing):**
1. **Tokenize** each document into terms (split on non-letters, handle punctuation,
   CJK segmentation).
2. **Normalize** — case-fold, optionally stem (Porter) or lemmatize, remove or keep
   stop words, apply Unicode normalization.
3. For each term, append `(docID, term-frequency, positions…)` to its **posting list**,
   kept sorted by docID.

The **dictionary** maps term → (document frequency, pointer to posting list); it is
held in memory (often a hash map or FST/trie), while posting lists live on disk.

**Query:**
- **Boolean AND** — intersect posting lists; walk them in tandem (merge), skipping via
  **skip pointers** to leap over non-matching docIDs. Intersection cost ≈ sum of the
  two list lengths (or less with skips).
- **Ranked retrieval** — for each query term, stream its posting list accumulating a
  score per document (see [[bm25]]); return the top-k via a heap. **WAND / block-max
  WAND** prune documents that cannot enter the top-k, skipping most postings.
- **Phrase / proximity** queries use the stored **positions** (positional index).

**Compression.** Posting lists store **gaps** (differences between consecutive docIDs)
rather than absolute IDs, then encode the small gaps with variable-byte or PForDelta;
this shrinks the index several-fold and, because I/O dominates, often speeds queries.

## Complexity & trade-offs
- Query time ≈ O(total postings scanned), reduced by skip pointers and WAND to far
  below the list lengths for top-k.
- Index size ≈ O(total tokens) before compression; positional indexes are larger.
- Updates are awkward: postings are append-friendly but deletes need tombstones and
  periodic **segment merges** (Lucene's model) rather than in-place edits.

## Pitfalls & gotchas
- **Tokenization mismatch** — the query must be analyzed the same way as documents, or
  "U.S.A." won't match "USA". Index-time and query-time analyzers must agree.
- **Over-aggressive stemming** conflates distinct words ("university"→"univers");
  under-stemming misses matches — a recall/precision trade.
- **Stop-word removal** breaks phrase queries like "to be or not to be".
- **Skew** — very common terms have huge posting lists; block-max WAND and early
  termination are needed to keep tail latency bounded.

## Worked example
Query `information AND retrieval`: fetch the two posting lists (say lengths 9,000 and
4,000), walk them together comparing docIDs, using skip pointers on the longer list to
jump ahead past non-matches, emitting only the ~500 docs in both — never touching the
other millions of documents.

## Related
- [[bm25]] — the ranking function scored over the postings.
- [[tf-idf-and-vector-space-model]] — the classic weighting stored per posting.
- [[dense-retrieval-and-embeddings]] — the semantic complement to lexical indexing.
- [[storage-engines-and-indexes]] — B-trees/LSM vs the inverted index.
- [[oasis-search-engine]] — this wiki's search uses an inverted index for BM25.

## Sources
Distilled from [[manning-irb]] (IIR ch. 1–2, 5).

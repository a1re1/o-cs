---
title: Big Data & Data Mining — Texts and Seminal Papers
type: source
section: "10.2"
level: 400
tags: [big-data, data-mining, mapreduce, spark, sketches, frequent-itemsets]
authors: Leskovec, Rajaraman, Ullman; Blum, Hopcroft, Kannan
year: 2020
institution: Stanford, Cornell
url: http://www.mmds.org/
license: free
format: texts+papers
sources: []
summary: The big-data and mining canon — Mining of Massive Datasets, Foundations of Data Science, Han's Data Mining, and the seminal systems and algorithms (MapReduce, Spark, Apriori, MinHash, HyperLogLog, Count-Min, the Dataflow model).
---

# Big Data & Data Mining — Texts and Seminal Papers

## What it is
The algorithms and systems for extracting patterns from datasets too large for one
machine or one pass: distributed processing, streaming sketches, similarity search,
and pattern mining. It fuses systems ([[mapreduce-and-dataflow]]) with algorithm
design under space/pass constraints ([[streaming-and-sketching]]).

## Key ideas
- **Distributed processing** — MapReduce and Spark/dataflow. See [[mapreduce-and-dataflow]].
- **Streaming sketches** — Bloom, Count-Min, HyperLogLog, reservoir sampling. See
  [[streaming-and-sketching]].
- **Similarity search at scale** — MinHash and LSH. See [[similarity-search-and-lsh]].
- **Frequent itemsets & association rules** — Apriori, FP-growth. See
  [[frequent-itemsets-and-association-rules]].
- **Big-data storage** — columnar formats and lakehouses. See
  [[columnar-storage-and-data-formats]].

## Chapter / lecture map
- **Leskovec, Rajaraman & Ullman, *Mining of Massive Datasets* (free) / Stanford CS246**
  — MapReduce, LSH, frequent itemsets, clustering, PageRank, recommenders, streams.
- **Blum, Hopcroft & Kannan, *Foundations of Data Science* (free)** — the theory:
  high-dimensional geometry, random projection, SVD, spectral methods.
- **Han, Kamber & Pei, *Data Mining: Concepts and Techniques*** — the classic mining text.

## Seminal papers
- **Dean & Ghemawat, MapReduce (2004); Zaharia et al., Spark/RDDs (2012)** — see
  [[mapreduce-and-dataflow]].
- **Agrawal & Srikant, association rules / Apriori (1994)** — see
  [[frequent-itemsets-and-association-rules]].
- **Broder, MinHash (1997)** — see [[similarity-search-and-lsh]].
- **Flajolet et al., HyperLogLog (2007); Cormode & Muthukrishnan, Count-Min (2005)** —
  see [[streaming-and-sketching]].
- **Akidau et al., the Dataflow model (2015); Flink (2015)** — unified batch/stream.

## What it adds
Turns "big data" from a buzzword into concrete cost models: what you can compute in one
pass and small space, what needs a cluster, and what approximations buy you. Connects
to [[recommender-systems]], [[network-science]] (PageRank at scale), and
[[distributed-systems-basics]].

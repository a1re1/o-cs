---
title: Computational Social Science & Social Computing — Texts and Seminal Papers
type: source
section: "9.5"
level: 400
tags: [network-science, graph-ml, social-network-analysis, recommender-systems, social-computing]
authors: Easley, Kleinberg, Leskovec, others
year: 2010
institution: Cornell, Stanford
url: https://www.cs.cornell.edu/home/kleinber/networks-book/
license: free
format: texts+courses+papers
sources: []
summary: The computational social science canon — Easley & Kleinberg's Networks, Crowds, and Markets, Leskovec's Mining of Massive Datasets and CS224W, and the seminal network papers from small-world and scale-free to PageRank, HITS, and graph neural networks.
---

# Computational Social Science & Social Computing — Texts and Seminal Papers

## What it is
The study of social phenomena through the lens of large-scale data and network
structure: how information, influence, and behavior spread through the graphs of
human connection, and how to build systems (recommenders, online communities) that
mediate them. It fuses graph theory, machine learning, economics, and sociology.

## Key ideas
- **Network science** — the structure of real networks (small-world, scale-free,
  communities) and processes on them (diffusion, cascades). See [[network-science]].
- **Link analysis** — ranking nodes by the graph structure: PageRank, HITS. See
  [[network-science]].
- **Graph machine learning** — node embeddings and graph neural networks. See
  [[graph-neural-networks]].
- **Recommender systems** — collaborative filtering and matrix factorization. See
  [[recommender-systems]].

## Chapter / lecture map
- **Easley & Kleinberg, *Networks, Crowds, and Markets* (free)** — the accessible
  spine: graphs, game theory, markets, information cascades, the web.
- **Leskovec, Rajaraman & Ullman, *Mining of Massive Datasets* (free)** —
  algorithms at scale: MinHash/LSH, PageRank, community detection, recommenders.
- **Stanford CS224W (Leskovec), Machine Learning with Graphs (open)** — the graph-ML
  course; node2vec, GNNs.
- **Cornell INFO 2040 (Easley & Kleinberg)** — networks for a broad audience.

## Notable claims & quotes
- **Granovetter (1973), "The strength of weak ties"** — novel information reaches you
  through acquaintances (weak ties bridging communities), not close friends.
- Milgram: any two people are connected by ~six intermediaries ("six degrees").

## Seminal papers
- **Milgram (1967)** — the small-world experiment; six degrees of separation.
- **Granovetter (1973)** — weak ties as bridges between clusters.
- **Watts & Strogatz (1998)** — the small-world network model (high clustering + short
  paths from a few random rewirings).
- **Barabási & Albert (1999)** — scale-free networks and preferential attachment
  ("rich get richer") producing power-law degree distributions.
- **Page, Brin, Motwani & Winograd (1998), PageRank** — ranking web pages by a random
  surfer's stationary distribution.
- **Kleinberg (1999), HITS** — hubs and authorities.
- **Kipf & Welling (2016), Graph Convolutional Networks** — deep learning on graphs.

## What it adds
Connects graph algorithms to real social and web systems, and to
[[markov-chains]] (PageRank is a Markov chain), [[graph-representations-and-traversal]]
(the substrate), [[recommender-systems]], and [[computing-ethics-and-professional-responsibility]]
(filter bubbles, misinformation, and algorithmic amplification).

---
title: Graph Neural Networks
type: concept
section: "9.5"
level: 400
tags: [graph-ml, gnn, gcn, message-passing, node-embeddings, node2vec]
sources: [computational-social-science-texts-and-seminal-papers]
summary: Deep learning on graph-structured data — node embeddings (node2vec), the message-passing framework, graph convolutional networks (GCN), and their uses and limits.
---

# Graph Neural Networks
**In one sentence.** Graph neural networks (GNNs) learn representations of nodes,
edges, and whole graphs by iteratively passing and aggregating messages along edges,
generalizing convolution from grids to arbitrary graph structure.

## Why it matters
Much real data is relational — social networks, molecules, knowledge graphs,
recommendation, traffic. GNNs let deep learning exploit that structure directly
instead of flattening it, and now power molecule property prediction, fraud
detection, recommenders, and web-scale ranking. They build on [[network-science]]
and [[deep-learning-basics]].

## How it works
**Node embeddings (the shallow precursor).** Map each node to a vector so that
graph-neighbors are nearby. **node2vec / DeepWalk** run random walks to generate
"sentences" of nodes and apply word2vec-style skip-gram — a graph analogue of
[[nlp-fundamentals]]. Transductive: no features, must retrain for new
nodes.

**Message passing (the GNN framework).** Each layer updates every node's vector by:
1. **Message** — each neighbor sends a function of its current vector.
2. **Aggregate** — combine incoming messages with a *permutation-invariant* operator
   (sum, mean, max).
3. **Update** — combine the aggregate with the node's own vector (an MLP + nonlinearity).

After `k` layers, a node's representation depends on its `k`-hop neighborhood. This
is the unifying view of nearly all GNNs.

**Graph Convolutional Network (GCN, Kipf & Welling 2016)** — the canonical instance:

```
H^(l+1) = σ( D̃^(−1/2) Ã D̃^(−1/2) H^(l) W^(l) )
```

`Ã = A + I` (add self-loops), `D̃` its degree matrix — a symmetric-normalized
neighborhood average followed by a learned linear map and nonlinearity. It is a
first-order approximation of spectral graph convolution; see
[[spectral-graph-theory-and-clustering]].

**Variants:** **GraphSAGE** (sample neighbors, learn an aggregator — *inductive*, works
on unseen nodes), **GAT** (attention-weighted neighbors, akin to
[[transformers-and-attention]]), and message-passing nets for molecules.

**Tasks:** node classification (semi-supervised), link prediction (recommendation,
knowledge-graph completion), and graph classification (molecule property, via a
readout/pooling over all node vectors).

## Complexity & trade-offs
- One GCN layer costs O(edges · feature_dim); scales to large sparse graphs with
  neighbor sampling (GraphSAGE) and mini-batching.
- **Depth is limited:** stacking many layers causes **over-smoothing** — all node
  vectors converge to indistinguishable values — so GNNs are usually 2–4 layers, and
  cannot see beyond that many hops without special tricks.

## Pitfalls & gotchas
- **Over-smoothing** with depth; **over-squashing** — information from an exponentially
  growing neighborhood is crushed into a fixed vector, hurting long-range tasks.
- **Expressive-power ceiling** — standard message-passing GNNs are no more powerful
  than the **Weisfeiler-Leman** graph-isomorphism test; some structures are provably
  indistinguishable.
- **Transductive vs inductive** — node2vec/vanilla GCN can't embed unseen nodes;
  use GraphSAGE for evolving graphs.

## Worked example
Classifying papers in a citation network with few labels: a 2-layer GCN takes each
paper's bag-of-words features, averages over cited/citing neighbors twice (so each
paper sees its 2-hop citation neighborhood), and predicts the subject. It beats a
label-blind classifier because the graph structure carries signal the text alone
lacks — the semi-supervised setting GCN was introduced for.

## Related
- [[network-science]] — the graph structure GNNs learn from.
- [[deep-learning-basics]] — the neural building blocks.
- [[spectral-graph-theory-and-clustering]] — GCN's spectral origin.
- [[transformers-and-attention]] — GAT and transformers as graph attention.
- [[recommender-systems]] — link prediction on user-item graphs.

## Sources
Distilled from [[computational-social-science-texts-and-seminal-papers]] (Kipf &
Welling 2016; node2vec; GraphSAGE; CS224W).

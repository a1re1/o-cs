---
title: PageRank
type: concept
section: "10.3"
level: 400
tags: [pagerank, link-analysis, random-surfer, stationary-distribution, power-iteration, web-search]
sources: [manning-irb]
summary: Google's link-analysis algorithm — rank a page by the stationary distribution of a random surfer following links with damping, computed by power iteration on the sparse web graph.
---

# PageRank
**In one sentence.** PageRank scores a web page by the long-run probability that a
"random surfer" — who follows outlinks at random and occasionally teleports to a random
page — is visiting it, i.e. the stationary distribution of a Markov chain on the web graph.

## Why it matters
PageRank (Brin & Page 1998) was the query-independent signal that made early Google's
results dramatically better: it measures a page's *importance* from the link structure of
the whole web, resisting simple content spam. The same computation ranks nodes in any
graph — citations, social networks, even function-call graphs. See [[network-science]].

## How it works
**The random surfer.** With probability `d` (the damping factor, ≈0.85) the surfer
follows a uniformly random outlink of the current page; with probability `1−d` it
**teleports** to a uniformly random page. A page's PageRank is its probability in the
resulting walk's steady state. Teleportation makes the chain **ergodic**, so a unique
stationary distribution exists (see [[markov-chains]]).

**The equation.** For page `p` with inlinks from pages `q`:

```
PR(p) = (1 − d)/N  +  d · Σ_{q → p}  PR(q) / outdeg(q)
```

Each page passes its rank, split evenly, along its outlinks; the teleport term
distributes `(1−d)` uniformly.

**Computing it — power iteration.** Start with a uniform vector and repeatedly apply the
update `r ← (1−d)/N · 1 + d · Mᵀr`, where `M` is the row-normalized link matrix. It
converges (the leading eigenvector of the damped transition matrix) in tens of iterations,
each an `O(edges)` sparse matrix-vector product — the web-scale computation that motivated
MapReduce-style processing (see [[mapreduce-and-dataflow]]).

**Dangling nodes** (no outlinks) leak probability; redistribute their rank uniformly
(equivalent to making them teleport).

## Complexity & trade-offs
- Each power-iteration step is `O(edges)`; the sparse web graph makes this feasible at
  billions of nodes, and convergence is fast because of damping.
- PageRank is **query-independent** (computed once, offline) — cheap at query time — but
  must be combined with query-dependent relevance ([[bm25]]) for actual search ranking.

## Pitfalls & gotchas
- **Ignoring dangling nodes** breaks conservation and skews ranks.
- **Damping choice** — `d` too high slows convergence and over-weights link structure;
  ≈0.85 is the tested default.
- **Link spam / farms** — PageRank can be gamed by manufactured link structure
  (TrustRank and later signals were responses); raw PageRank is not spam-proof.
- **PageRank ≠ relevance** — a high-PageRank page can be irrelevant to a query; it is one
  signal among many.

## Worked example
Three pages where A and B both link to C, and C links back to A: power iteration
concentrates rank on C (two inlinks from ranked pages) and then feeds some back to A,
converging to a stable distribution where C > A > B — importance flowing along links,
with teleportation keeping every page's rank above zero.

## Related
- [[network-science]] — PageRank as centrality; HITS as the hubs/authorities alternative.
- [[markov-chains]] — PageRank is a stationary distribution.
- [[bm25]] — query-dependent relevance combined with PageRank in web search.
- [[mapreduce-and-dataflow]] — computing PageRank at web scale.

## Sources
Distilled from [[manning-irb]] (Brin & Page 1998; IIR ch. 21 link analysis).

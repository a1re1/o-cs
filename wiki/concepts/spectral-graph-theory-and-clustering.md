---
title: Spectral Graph Theory and Clustering
type: concept
section: "9.5"
level: 400
tags: [spectral-clustering, graph-laplacian, eigenvectors, community-detection, fiedler-vector]
sources: [computational-social-science-texts-and-seminal-papers]
summary: Using the eigenvalues and eigenvectors of the graph Laplacian to partition graphs — the Fiedler vector, spectral clustering, normalized cuts, and the link to PageRank and mesh processing.
---

# Spectral Graph Theory and Clustering
**In one sentence.** Spectral graph theory reads a graph's structure off the
eigenvalues and eigenvectors of its Laplacian matrix, turning combinatorial problems
like graph partitioning into linear-algebra computations.

## Why it matters
The graph Laplacian is a bridge between discrete structure and continuous math: its
spectrum reveals connectivity, bottlenecks, and communities. It powers spectral
clustering, image segmentation (normalized cuts), mesh processing
([[geometry-processing-and-meshes]]), and connects to PageRank and diffusion in
[[network-science]].

## How it works
**The graph Laplacian.** For an undirected graph with adjacency `A` and degree matrix
`D`, the (unnormalized) Laplacian is `L = D − A`. Key facts:
- `L` is symmetric positive semidefinite; `xᵀ L x = Σ_{(i,j)∈E} (xᵢ − xⱼ)²` — it
  measures how much a labeling varies across edges.
- The **multiplicity of eigenvalue 0 equals the number of connected components**; the
  all-ones vector is always a 0-eigenvector.
- The **second-smallest eigenvalue λ₂** — the **algebraic connectivity** or *Fiedler
  value* — is >0 iff the graph is connected, and larger λ₂ means harder to cut. Its
  eigenvector, the **Fiedler vector**, gives a good 2-way partition by sign.

**Spectral clustering.** To find `k` clusters:
1. Build a similarity graph and its (normalized) Laplacian.
2. Compute the `k` eigenvectors of the smallest eigenvalues.
3. Embed each node as the row of the resulting `n×k` matrix.
4. Run [[k-means-clustering]] on those rows.

It finds non-convex, connectivity-based clusters that k-means on raw coordinates
misses, because the Laplacian embedding untangles the manifold. **Normalized cut**
(Shi-Malik) is the same idea derived as a balanced graph-cut relaxation.

**Connections.** The normalized Laplacian's spectrum is tied to the mixing time of
the random walk on the graph — the same walk behind [[network-science]]'s PageRank —
and to expander graphs (large λ₂ = good expansion). In geometry, the mesh cotangent
Laplacian is this operator on a surface.

## Complexity & trade-offs
- Computing a few extreme eigenvectors of a sparse `n×n` Laplacian costs roughly
  O(n·k) per iteration with Lanczos/power methods — feasible for large sparse graphs,
  but full eigendecomposition (O(n³)) is not.
- Spectral clustering needs `k` chosen in advance and can be sensitive to the
  similarity-graph construction (bandwidth, k-NN vs ε-ball).

## Pitfalls & gotchas
- **Unnormalized vs normalized Laplacian** — for clusters of unequal size/degree, the
  normalized version (`L_sym` or `L_rw`) is usually needed to avoid trivial cuts.
- **The relaxation is not exact** — spectral partitioning solves a continuous
  relaxation of an NP-hard cut, so it is a heuristic, not optimal.
- **Disconnected or nearly-disconnected components** dominate the low spectrum and can
  mask finer community structure.

## Worked example
Two blobs connected by a thin bridge of edges: k-means on node coordinates may split
them wrongly, but the Fiedler vector is nearly constant within each blob and flips
sign across the bridge, so thresholding it at 0 cuts exactly the few bridge edges —
the minimum-ish balanced cut.

## Related
- [[network-science]] — communities, diffusion, and the random walk.
- [[k-means-clustering]] — the final step of spectral clustering.
- [[geometry-processing-and-meshes]] — the mesh Laplacian is a graph Laplacian.
- [[graph-neural-networks]] — GCN is a first-order spectral graph convolution.

## Sources
Distilled from [[computational-social-science-texts-and-seminal-papers]] (Shi & Malik
normalized cuts; von Luxburg spectral-clustering tutorial; *Mining of Massive Datasets*).

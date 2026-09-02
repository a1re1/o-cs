---
title: Union-find (disjoint sets) — quick-find, quick-union, weighting, path compression
type: concept
section: "3.1"
level: 200
tags: [union-find, disjoint-sets, dynamic-connectivity, quick-find, quick-union, weighted-quick-union, union-by-rank, path-compression, inverse-ackermann, kruskal, connected-components, equivalence-relation]
sources: [sedgewick-algorithms-4e, berkeley-cs61b, clrs]
summary: Union-find maintains a partition of n elements under union(p, q) and find(p) — quick-find is O(1) find / O(n) union, quick-union stores parent links in a forest, union by size/rank bounds tree depth by lg n, and path compression flattens paths on every find, giving near-constant O(α(n)) amortized cost; it powers Kruskal's MST, connected components, percolation, and equivalence-class problems.
---
# Union-find (disjoint-set forests)

**In one sentence.** Represent each set as a tree of parent pointers; `find` walks to the root,
`union` links roots; keep trees shallow by linking small under large and by compressing paths.

## The problem (Sedgewick 1.5)
Dynamic connectivity: given pairs "p is connected to q" for an equivalence relation (reflexive,
symmetric, transitive — [[sets-relations-functions]]), answer `connected(p, q)` online. Equivalence
classes = components. Only unions, no splits (fully dynamic connectivity is much harder).

## Implementations on an array `id[0..n)`
| | find | union | idea |
|---|---|---|---|
| Quick-find | O(1) | O(n) | `id[p]` = component name; union relabels all |
| Quick-union | O(depth) | O(depth) | `id[p]` = parent; root has `id[r] = r` |
| Weighted quick-union (by size or rank) | O(lg n) | O(lg n) | link root of smaller tree under larger ⇒ depth ≤ lg n (each link doubles the tree containing you) |
| + path compression | O(α(n)) amortized | same | on `find`, point every visited node at the root (or halve paths: `id[p] = id[id[p]]`) |
α(n) is the inverse Ackermann function, ≤ 4 for any practical n — "effectively constant"
([[amortized-analysis]]; Tarjan's bound; Fredman–Saks show it is tight).

```python
def find(p):                     # with path halving
    while p != parent[p]:
        parent[p] = parent[parent[p]]
        p = parent[p]
    return p
def union(p, q):
    rp, rq = find(p), find(q)
    if rp == rq: return
    if size[rp] < size[rq]: rp, rq = rq, rp
    parent[rq] = rp; size[rp] += size[rq]
```

## Uses
Kruskal's MST (add edges in weight order if endpoints are in different sets — [[minimum-spanning-trees]]);
connected components of a graph built incrementally; percolation simulations; image segmentation;
type inference unification (Hindley–Milner — [[type-systems]]); detecting cycles in undirected
graphs; equivalence of DFA states; least common ancestor offline (Tarjan).

## Pitfalls
- Forgetting to union *roots* (linking non-roots breaks the forest).
- Union by size vs by rank both work; mixing rank with path compression is fine (rank is an
  upper bound on height).
- Not a solution when edges are deleted (need link-cut trees or Holm–de Lichtenberg–Thorup).

## Related
- [[amortized-analysis]], [[graph-representations]], [[minimum-spanning-trees]], [[sets-relations-functions]],
  [[graph-theory-basics]].

## Sources
Sedgewick 1.5; CS61B week 5; CLRS ch. 19 (21 in 3rd ed.).

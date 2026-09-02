---
title: Binary search trees — search, insert, delete, traversal, and why height matters
type: concept
section: "3.1"
level: 200
tags: [binary-search-trees, bst, tree-traversal, inorder, preorder, postorder, hibbard-deletion, tree-height, recursion, symbol-table, ordered-map]
sources: [sedgewick-algorithms-4e, open-data-structures-morin, berkeley-cs61b]
summary: A BST keeps keys smaller than a node in its left subtree and larger in its right, so search, insert, min/max, floor/ceiling, rank and delete each cost O(height); random insertion order gives expected height ~ 2 ln n but sorted input gives a linked list, which is the motivation for balanced trees; in-order traversal yields sorted order, and most tree code is structural recursion on (key, left, right).
---
# Binary search trees

**In one sentence.** Binary search made into a linked structure: every comparison halves the
candidates *if* the tree is balanced.

## Invariant and operations
Node = key, value, left, right (optionally subtree size). **BST property**: all keys in `left` < key
< all keys in `right` (a rep invariant — [[abstract-data-types-and-rep-invariants]]).
- `get(k)`: compare, go left/right, O(h). `put(k, v)`: search, attach a new leaf; recursive version
  returns the (possibly new) subtree root: `node.left = put(node.left, k, v)`.
- `min`/`max`: leftmost/rightmost; `floor(k)`: largest key ≤ k (go left if k < key, else try right
  subtree then fall back to this key); `rank(k)` and `select(i)` with subtree sizes; range search by
  pruning subtrees outside [lo, hi].
- `deleteMin`: replace the leftmost node by its right child. `delete(k)` (Hibbard): 0 or 1 child →
  splice; 2 children → replace with successor (min of right subtree) and `deleteMin` there.
  Hibbard deletion is asymmetric and after many random ops the height drifts to ~√n.
- Traversals ([[fold-and-structural-recursion]]): **in-order** (left, node, right) = sorted order;
  pre-order (node first) serializes structure; post-order (children first) frees/evaluates;
  level-order via a queue (BFS). Iterative in-order uses an explicit stack (Morris traversal uses
  none).

## Height
Height h determines everything. Random insertion order: expected height ≈ 2 ln n ≈ 1.39 lg n
(expected search cost ~1.39 lg n compares) — good in practice. Sorted or nearly sorted input:
h = n — the structure becomes a linked list. Guarantees require [[balanced-search-trees]]. Any
binary tree with n nodes has h ≥ ⌈lg(n+1)⌉ − 1.

## Worked example
Insert 50, 30, 70, 20, 40, 60, 80 → perfectly balanced, h = 2. Insert 1..7 in order → chain, h = 6;
`get(7)` costs 7 compares. In-order of either tree: 1..7 or 20..80 sorted.

## Pitfalls
- Duplicate keys: decide (replace value, count, or go right consistently).
- Comparator/`compareTo` inconsistent with `equals` — keys "disappear".
- Recursion depth n on degenerate trees (stack overflow); mutating keys in place.

## Related
- [[balanced-search-trees]], [[hash-tables]], [[recursion-and-iteration]], [[fold-and-structural-recursion]],
  [[heaps-and-priority-queues]] (a different tree invariant), [[graph-representations]].

## Sources
Sedgewick 3.2; ODS ch. 6; CS61B week 5.

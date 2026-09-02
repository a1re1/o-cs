---
title: Balanced search trees — 2-3 trees, red-black BSTs, AVL, B-trees, treaps, skip lists
type: concept
section: "3.1"
level: 300
tags: [balanced-search-trees, 2-3-trees, red-black-trees, left-leaning-red-black, avl-trees, b-trees, treaps, skiplists, scapegoat-trees, splay-trees, rotations, ordered-map, ordered-set, range-queries]
sources: [sedgewick-algorithms-4e, open-data-structures-morin, berkeley-cs61b, clrs]
summary: Balanced trees keep a binary search tree's height O(log n) under insertions and deletions — 2-3 trees by letting nodes hold two keys and splitting 4-nodes upward; red-black BSTs by encoding 3-nodes as left-leaning red links fixed with rotations and color flips (height ≤ 2 lg n); AVL by height-balance rotations; B-trees by wide nodes for disk/cache; treaps and skip lists by randomization; splay trees by amortized self-adjustment — giving ordered maps with O(log n) search, insert, delete, min/max, predecessor, rank, and range queries.
---
# Balanced search trees

**In one sentence.** A plain BST degenerates to a list on sorted input; balanced variants pay a
constant factor on updates to guarantee logarithmic height, and in return give every ordered
operation a hash table cannot.

## 2-3 trees (Sedgewick 3.3)
Nodes hold one key (2-node, two links) or two keys (3-node, three links); all null links at the
same depth. Insert at the bottom: into a 2-node → becomes a 3-node; into a 3-node → temporary
4-node, split into three 2-nodes and push the middle key up, repeating until a 2-node absorbs it
or the root splits (height grows only at the root — the tree stays perfectly balanced). All
transformations are *local*, O(1) links each; height ≤ lg n. Direct implementation is awkward…

## Red-black BSTs (left-leaning, Sedgewick/Guibas)
…so encode 3-nodes as two 2-nodes joined by a **red** link that leans left; black links form the
2-3 tree. Invariants: no node has two red links; no right-leaning red links; perfect black balance
(every path root→null has the same number of black links). Search is plain BST search. Insert = BST
insert with a red link, then on the way up fix with three local operations: rotate left (right-
leaning red), rotate right (two reds in a row), flip colors (both children red = split a 4-node).
Height ≤ 2 lg n; average ≈ 1.00 lg n; O(1) amortized rotations per insert. Classic (CLRS) red-black
trees allow right-leaning reds; same bounds, more cases. Deletion is the hard part (Hibbard
deletion in plain BSTs is asymmetric and degrades balance; LLRB delete needs top-down 2-3-style
transformations).

## Alternatives
| Structure | Guarantee | Why choose it |
|---|---|---|
| AVL tree | height ≤ 1.44 lg n, stricter balance (height diff ≤ 1) | faster lookups, more rotations on update |
| **B-tree** / B+-tree | height log_B n with B ≈ hundreds | one node = one disk block or cache line; databases, filesystems ([[storage-engines-and-indexes]]) |
| Treap | expected O(log n) via random priorities | tiny code, easy split/merge (persistent variants) |
| Skip list | expected O(log n), probabilistic layered lists | lock-free concurrent variants; simple |
| Scapegoat tree | amortized O(log n) by partial rebuilding | no extra per-node data |
| Splay tree | amortized O(log n), self-adjusting | locality of access; no balance info; [[amortized-analysis]] |
Language libraries: Java `TreeMap` (red-black), C++ `std::map` (red-black), Rust `BTreeMap`
(B-tree, cache-friendly), Python has none built in (`sortedcontainers`).

## What ordered maps buy you
`floor`/`ceiling`, predecessor/successor, `rank(k)` and `select(i)` with subtree sizes, range
count and range iteration, ordered traversal, min/max — all O(log n) — plus deterministic
iteration and worst-case (not expected) bounds. Interval trees, order-statistic trees and k-d
trees are augmentations ([[advanced-data-structures]]).

## Pitfalls
- Using a balanced tree where a hash table suffices (2–5× slower for pure lookups).
- Comparator inconsistent with equality (violates the BST invariant silently).
- Recursion depth is fine (log n), but naive BSTs on sorted input recurse n deep.

## Related
- [[binary-search-trees]], [[hash-tables]], [[amortized-analysis]], [[persistent-data-structures]]
  (path copying works on any of these), [[storage-engines-and-indexes]], [[advanced-data-structures]].

## Sources
Sedgewick 3.3; ODS ch. 7–9, 14; CS61B week 6; CLRS ch. 13, 18.

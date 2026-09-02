---
title: Open Data Structures (Pat Morin) and Problem Solving with Algorithms and Data Structures using Python
type: source
section: "3.1"
level: 200
tags: [data-structures, array-based-lists, linked-lists, skiplists, hash-tables, binary-trees, scapegoat-trees, red-black-trees, heaps, sorting, graphs, tries, b-trees, external-memory, python]
sources: []
authors: [Pat Morin, Brad Miller, David Ranum]
year: 2013
institution: Carleton / Luther College
url: https://opendatastructures.org/
license: CC-BY
format: html
summary: A free, rigorous data-structures text (Java/C++/Python editions) with analysis — array-based lists (ArrayStack, ArrayDeque, DualArrayDeque, RootishArrayStack), linked lists (SLList, DLList, SEList), skiplists, hash tables (chaining, linear probing, multiplicative and tabulation hashing), binary trees and BSTs, random BSTs/treaps, scapegoat trees, red-black trees, heaps (binary, meldable), sorting, graphs, tries/binary tries, B-trees — plus the friendly Python book (pythonds) for beginners.
---
# Open Data Structures (Morin) / pythonds

## What it is
Ch. 1 introduction (interfaces List/USet/SSet; math background; the word-RAM model); 2 array-based
lists (amortized resizing analysis: O(1) amortized add/remove at ends); 3 linked lists; 4
skiplists (randomized, expected O(log n)); 5 hash tables — ChainedHashTable, LinearHashTable
(open addressing with tombstones/`del`), hash codes for integers (multiplicative hashing with odd
multiplier, tabulation hashing), for strings and compound objects; 6 binary trees, BinarySearchTree
(unbalanced: O(height)); 7 random binary search trees (treap; expected depth O(log n)); 8
scapegoat trees (partial rebuilding, amortized O(log n)); 9 red-black trees (2-4 tree
correspondence, left-leaning, O(log n) worst case, O(1) amortized rotations); 10 heaps — BinaryHeap
(implicit array), MeldableHeap (randomized); 11 sorting (merge, quick, heap; counting and radix); 12
graphs (adjacency matrix vs lists; BFS/DFS); 13 data structures for integers (binary trie, x-fast
and y-fast tries); 14 external memory searching (B-trees).
pythonds: basic structures, recursion, searching/sorting, trees, graphs in Python with exercises.

## Key ideas → pages
- Amortized resizing proof — [[arrays-and-linked-lists]], [[amortized-analysis]].
- Linear probing with tombstones, multiplicative/tabulation hashing — [[hash-tables]].
- Treaps, scapegoat, red-black — [[balanced-search-trees]]; implicit binary heap —
  [[heaps-and-priority-queues]]; tries — [[tries]]; adjacency representations —
  [[graph-representations]].

## What it adds
Proofs where [[sedgewick-algorithms-4e]] gives intuition; the interface-first framing (List, USet,
SSet) matches the ADT view of [[abstract-data-types-and-rep-invariants]].

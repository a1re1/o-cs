---
title: Persistent (purely functional) data structures
type: concept
section: "2.4"
level: 400
tags: [persistent-data-structures, immutability, structural-sharing, path-copying, functional-queues, banker-queue, real-time-queue, lazy-evaluation, memoization, hamt, finger-trees, red-black-trees, okasaki, versions, undo]
sources: [okasaki-purely-functional-data-structures, cs3110-ocaml]
summary: A persistent structure keeps every old version alive after an update by sharing unchanged substructure (path copying in trees, cons-list prefixes); the batched two-list queue is amortized O(1) only ephemerally, because persistence allows "multiple futures" that repeat an expensive reversal, and Okasaki's fix is to suspend the reversal lazily and memoize it (banker's queue) or schedule it incrementally (real-time queue); HAMTs and finger trees power immutable collections in practice.
---
# Persistent data structures

**In one sentence.** Never mutate; build a new version that shares most of the old one — so
versions are free, threads can't race, undo is trivial, and the price is a log factor or a clever
amortization argument.

## Structural sharing
- Cons lists: `x :: xs` shares `xs` entirely; persistence is automatic ([[fold-and-structural-recursion]]).
- Balanced trees: **path copying** — an insert copies the O(log n) nodes on the root-to-leaf path
  and shares the rest; red-black trees (Okasaki's 4-case balance), 2-3 trees, AVL. Every functional
  map/set works this way ([[balanced-search-trees]]).
- Wide tries: **HAMT** (hash array mapped trie, 32-way branching, log₃₂ n depth) for Clojure/Scala
  maps and Rust `im`; persistent vectors as 32-ary tries with a tail buffer; **finger trees** for
  deques/sequences with O(1) ends and O(log n) split/concat.
- Arrays are the hard case: persistent arrays via version trees or "rerooting" (CS3110 9.6) give O(1)
  for the newest version and slower access to old ones.

## The queue story (Okasaki ch. 3)
- Batched queue = front list + reversed rear list; `dequeue` reverses the rear when the front
  empties. **Ephemerally** amortized O(1) (each element is reversed once).
- Under **persistence**, a client can keep the old version and call `dequeue` on it repeatedly —
  "multiple futures" — paying the O(n) reversal each time: the credit argument assumes each version
  is used once.
- Fix 1, **banker's queue**: make the front a lazy stream and force the reversal *incrementally*,
  rotating when |rear| > |front|; with memoization the suspended reversal is paid once no matter how
  many futures share it. Debits (not credits) are assigned to suspensions and discharged before they
  are forced ([[amortized-analysis]]).
- Fix 2, **real-time queue**: schedule the suspensions so each operation forces a constant number —
  worst-case O(1), no laziness debt.
- Lazy rebuilding generalizes: rebuild the structure gradually alongside operations (deques).

## When to use
- Undo/redo, versioned state (editors, VCS, snapshot isolation in databases), concurrent readers
  without locks, backtracking search that shares state between branches.
- Cost: allocation-heavy, pointer chasing hurts cache locality ([[caches-and-memory-hierarchy]]);
  mutable arrays win for hot loops. Transient/"mutable inside a scope" APIs bridge the two.

## Related
- [[amortized-analysis]], [[streams-and-lazy-evaluation]], [[algebraic-data-types]],
  [[balanced-search-trees]], [[hash-tables]], [[ownership-and-borrowing]] (immutability by default).

## Sources
Okasaki thesis ch. 1–5; CS3110 ch. 9 (amortized analysis, red-black trees, persistent arrays).

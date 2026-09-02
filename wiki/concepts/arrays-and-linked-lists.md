---
title: Arrays, dynamic arrays, linked lists, stacks, queues, and deques
type: concept
section: "3.1"
level: 100
tags: [arrays, dynamic-arrays, resizing-arrays, linked-lists, singly-linked, doubly-linked, stacks, queues, deques, circular-buffer, ring-buffer, sentinel, iterators, cache-locality]
sources: [sedgewick-algorithms-4e, open-data-structures-morin, berkeley-cs61b]
summary: Arrays give O(1) random access and cache-friendly scans but fixed size; dynamic arrays double on overflow for O(1) amortized append; linked lists give O(1) insert/delete at a known node but O(n) access and poor locality; stacks (LIFO), queues (FIFO) and deques are the interfaces, implementable by either — and in practice the resizing array (or ring buffer) wins for almost everything.
---
# Arrays and linked lists (and the stack/queue/deque interfaces)

**In one sentence.** Two ways to store a sequence: contiguous (arrays — fast to index and scan) or
node-linked (lists — fast to splice); every other structure is built from these.

## Arrays
Fixed-size, contiguous, `a[i]` at `base + i·size` — O(1) access, perfect locality
([[caches-and-memory-hierarchy]]). Insert/delete in the middle is O(n) (shift). Bounds checks
matter ([[memory-safety-and-buffer-overflows]]).

## Dynamic (resizing) arrays — `ArrayList`, `Vec`, Python `list`
Capacity c ≥ size n; append writes `a[n]`; when full, allocate 2c and copy. **Amortized O(1)**: n
appends cost ≤ 3n copies (accounting method — [[amortized-analysis]]); shrink at ¼ full to avoid
thrashing. Growth factor 1.5–2 trades memory for copies. Insert/remove at the front is O(n) — use a
**ring/circular buffer** (`ArrayDeque`, `VecDeque`) with head/tail indices mod capacity for O(1) at
both ends. ODS's RootishArrayStack gets O(√n) wasted space.

## Linked lists
Singly linked (`next`), doubly (`prev`, `next`), with a **sentinel** node to remove null checks.
O(1) insert/delete given a node reference; O(n) to find the k-th; each node is a separate
allocation with pointer overhead and cache misses — usually 5–10× slower than arrays for scans.
Good for: intrusive lists in kernels/allocators (the node lives inside the object — see
[[dynamic-memory-allocation]] free lists), LRU caches (list + hash map), splicing whole lists,
persistent cons lists in FP ([[persistent-data-structures]]). In Rust, linked lists fight the borrow
checker — reach for `Vec`/`VecDeque` ([[ownership-and-borrowing]]).

## Interfaces
| ADT | Ops | Array impl | List impl |
|---|---|---|---|
| Stack (LIFO) | push, pop, peek | resizing array (best) | push/pop at head |
| Queue (FIFO) | enqueue, dequeue | ring buffer | head + tail pointers |
| Deque | both ends | ring buffer | doubly linked |
| Bag | add, iterate | either | either |
Uses: call stacks and expression evaluation (Dijkstra's two-stack algorithm), undo, DFS (stack) vs
BFS (queue) ([[graph-representations]]), buffering producers/consumers.

## Pitfalls
- Off-by-one and empty/one-element edge cases in list code; losing the reference when relinking
  (save `next` first).
- Iterator invalidation: modifying a container while iterating (fail-fast iterators, Rust compile
  error).
- Choosing a linked list for "fast inserts" without a node handle — the O(n) search dominates.

## Related
- [[amortized-analysis]], [[hash-tables]], [[heaps-and-priority-queues]], [[caches-and-memory-hierarchy]],
  [[abstract-data-types-and-rep-invariants]], [[recursion-and-iteration]].

## Sources
Sedgewick 1.3; ODS ch. 2–3; CS61B weeks 2–4.

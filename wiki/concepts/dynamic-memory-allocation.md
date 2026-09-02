---
title: Dynamic memory allocation — malloc design, free lists, fragmentation, and common memory bugs
type: concept
section: "2.3"
level: 300
tags: [malloc, free, realloc, heap-allocator, free-list, implicit-free-list, explicit-free-list, segregated-fits, coalescing, fragmentation, alignment, memory-bugs, use-after-free, memory-leak, arena-allocator, garbage-collection]
sources: [csapp-15-213, stanford-cs107, modern-c-gustedt]
summary: An allocator carves a heap into blocks with headers, finds a free block by first/next/best fit from an implicit, explicit, or segregated free list, splits and coalesces (boundary tags) to fight fragmentation, and must keep alignment and throughput high — plus the complete list of ways C programs misuse it (dangling, double free, leak, off-by-one, wrong size) and when an arena or a GC is the better tool.
---
# Dynamic memory allocation

**In one sentence.** `malloc(n)` must return an aligned block of ≥ n bytes without knowing what will be
freed when; every design is a trade-off between throughput, memory utilization (fragmentation), and
simplicity.

## Allocator anatomy (CSAPP 9.9, malloclab)
- **Block** = header (size + allocated bit, using the low bits freed by alignment) + payload
  (+ padding); free blocks may carry a footer (boundary tag) and pointers.
- **Placement**: first fit (fast, front fragments), next fit, best fit (better utilization, slower).
- **Splitting** a larger free block; **coalescing** with neighbours on free — immediate coalescing
  with boundary tags is O(1) (Knuth); deferred coalescing amortizes.
- **Free-list organization**: implicit (walk all blocks), explicit (doubly linked free blocks;
  LIFO or address-ordered), **segregated fits** (size classes; what glibc/jemalloc/tcmalloc do — fast
  and low fragmentation), buddy systems (power-of-two, easy coalescing, internal fragmentation).
- **Fragmentation**: internal (padding/header overhead) vs external (free memory in unusable
  fragments). Utilization = peak payload / heap size.
- Getting memory: `sbrk` (contiguous) or `mmap` (large allocations, returned to the OS on free).
- Production allocators add per-thread caches (no lock on the fast path), size-class bins, and
  security hardening (safe unlinking, guard bytes).
- K&R's allocator (8.7) is the 60-line reference implementation: a circular free list with first fit.

## The API contract
`malloc` returns uninitialized memory aligned for any type (16 bytes on x86-64) or NULL; `calloc`
zeroes (and checks the multiplication overflow); `realloc` may move the block (use the returned
pointer; on failure the old block is intact — don't write `p = realloc(p, n)`); `free(NULL)` is fine;
freeing a non-malloc pointer or twice is UB ([[undefined-behavior]]).

## Common bugs (CSAPP 9.11)
- Dereferencing bad pointers (`scanf("%d", val)` without `&`).
- Reading uninitialized heap memory (assuming malloc zeroes).
- Off-by-one buffer overrun (`malloc(n * sizeof(int))` then writing `a[n]`); wrong size
  (`sizeof(int)` for a `double*` array; forgetting `+1` for the NUL).
- Dangling references after `realloc`/`free`; double free; freeing the middle of a block.
- Memory leaks (lost pointers, missing frees on error paths — use `goto cleanup` in C, RAII elsewhere).
- Detect with ASan/valgrind, `MALLOC_CHECK_`, allocation counters in tests ([[debugging]]).

## Alternatives
- **Arena / region / bump allocators**: allocate by bumping a pointer, free everything at once —
  ideal for request-scoped or phase-scoped data (compilers, servers); no per-object free.
- **Pools** for fixed-size objects; slab allocators in kernels.
- **Garbage collection** (tracing: mark-sweep, copying, generational; reference counting) trades
  control for safety — [[garbage-collection]]; Rust's ownership gives deterministic freeing without a GC
  ([[ownership-and-borrowing]]).

## Related
- [[memory-layout-stack-heap]], [[pointers-and-memory]], [[undefined-behavior]], [[garbage-collection]],
  [[caches-and-memory-hierarchy]] (allocation patterns drive locality).

## Sources
CSAPP 9.9–9.11; CS107 lecture 16 and the heap allocator assignment; K&R 8.7; Modern C level 2 (storage).

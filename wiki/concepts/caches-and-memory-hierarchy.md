---
title: Caches and the memory hierarchy — locality, cache organization, misses, AMAT, and writing cache-friendly code
type: concept
section: "4.1"
level: 300
tags: [caches, memory-hierarchy, locality, temporal-locality, spatial-locality, direct-mapped, set-associative, cache-lines, tags, lru, write-back, write-through, write-allocate, amat, miss-rate, compulsory-capacity-conflict, multilevel-caches, dram, sram, prefetching, cache-blocking, false-sharing, memory-wall]
sources: [patterson-hennessy-cod, csapp-15-213, architecture-seminal-papers]
summary: Registers, L1/L2/L3 SRAM caches, DRAM and disk form a hierarchy that looks as fast as the top and as big as the bottom only because programs have temporal and spatial locality; a cache is organized in sets of lines (address = tag | index | offset), a direct-mapped/set-associative/fully-associative choice trades hit time for conflict misses, misses are compulsory/capacity/conflict, average memory access time = hit time + miss rate × miss penalty, and the programmer's levers — stride-1 access, blocking/tiling, struct layout, avoiding pointer chasing and false sharing — matter more than most algorithmic constant factors.
---
# Caches and the memory hierarchy

**In one sentence.** Memory is ~100× slower than the core; caches hide that only for programs
whose accesses are predictable, so data layout and access order are first-class performance
decisions.

## The hierarchy (COD ch. 5, CSAPP ch. 6)
| Level | Size | Latency (approx.) | Technology |
|---|---|---|---|
| registers | ~1 KB | 0.3 ns | flip-flops |
| L1 I/D | 32–64 KB each | ~1 ns (4 cycles) | SRAM |
| L2 | 256 KB–2 MB | ~4 ns (12–14 cycles) | SRAM |
| L3 (shared) | 8–64 MB | ~10–20 ns | SRAM |
| DRAM | GBs | ~80–100 ns | DRAM (refresh, row buffers) |
| SSD / disk | TBs | 50 µs / 5 ms | flash / magnetic |
**Locality**: temporal (reuse soon) and spatial (nearby next) — loops, arrays, stacks have it;
linked structures and hash tables less so. Each level caches lines (typically 64 B) of the one
below; the "memory wall" (Wulf & McKee) is the growing gap.

## Cache organization
- Address split: tag | set index | block offset. A **direct-mapped** cache has one line per set
  (fast, conflict-prone); **n-way set-associative** has n lines per set with LRU/pseudo-LRU
  replacement; **fully associative** = one set (TLBs, victim caches).
- The four questions (COD 5.8): where can a block go, how is it found (tag compare + valid bit),
  which is replaced, what happens on a write — **write-through** (+ write buffer) vs
  **write-back** (dirty bit); write-allocate vs no-write-allocate.
- Miss types (the 3 Cs): **compulsory** (first touch; prefetching helps), **capacity** (working
  set > cache; blocking helps), **conflict** (mapping collisions; associativity helps). Plus
  coherence misses on multicores ([[cache-coherence-and-memory-consistency]]).
- **AMAT** = hit time + miss rate × miss penalty; multilevel: L1 small and fast (hit time), L2/L3
  large (miss rate); inclusive vs exclusive hierarchies. Hardware prefetchers detect strides.
- Virtually indexed, physically tagged L1s overlap TLB lookup with cache access ([[virtual-memory]]).

## Performance for programmers (CSAPP 6.5–6.6)
- **Stride-1** access in the innermost loop (row-major: iterate columns innermost in C; the
  `i-j-k` vs `i-k-j` matrix-multiply loop orders differ 5–10×).
- **Blocking/tiling**: process sub-blocks that fit in cache (matrix multiply, stencil, transpose)
  — the cache-lab exercise; cache-oblivious recursion achieves this automatically
  ([[advanced-data-structures]]).
- Struct layout: keep hot fields together (struct of arrays vs array of structs — SoA for SIMD);
  pad/align to line boundaries; shrink data (smaller ints, bitfields).
- Avoid pointer chasing (linked lists, trees with random node placement) — each hop is a
  potential miss; prefer arrays, B-trees, HAMTs with wide nodes ([[balanced-search-trees]],
  [[arrays-and-linked-lists]]).
- **False sharing**: two threads writing different variables in the same line ping-pong it —
  pad per-thread data ([[synchronization-primitives]]).
- Measure: the memory mountain (throughput vs size and stride), `perf stat -e cache-misses`,
  cachegrind ([[profiling-and-performance]]).

## Pitfalls
- Reasoning about big-O only: O(n) over a linked list can lose to O(n log n) over an array.
- Assuming sequential access in the wrong dimension (column-major Fortran/NumPy order='F').
- Cache-timing side channels (Spectre, AES table attacks): caches leak what was accessed
  ([[pipelining-and-hazards]]).

## Related
- [[virtual-memory]], [[pipelining-and-hazards]], [[cache-coherence-and-memory-consistency]],
  [[profiling-and-performance]], [[memory-layout-stack-heap]], [[dynamic-memory-allocation]],
  [[advanced-data-structures]], [[storage-engines-and-indexes]].

## Sources
COD ch. 5; CSAPP ch. 6; CA:AQA ch. 2, appendix B.

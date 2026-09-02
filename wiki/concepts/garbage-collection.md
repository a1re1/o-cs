---
title: Garbage collection — reference counting, mark–sweep, copying, generational, and concurrent collectors
type: concept
section: "4.3"
level: 400
tags: [garbage-collection, gc, reference-counting, cycles, mark-sweep, tricolor-marking, copying-collector, cheney, semispace, generational-gc, nursery, write-barrier, remembered-set, incremental-gc, concurrent-gc, stop-the-world, gc-roots, conservative-gc, finalizers, weak-references, gc-pacing, rust-ownership, arc]
sources: [crafting-interpreters, compiler-seminal-papers, cs6120-and-compiler-courses, dragon-book-and-compiler-texts]
summary: A collector decides which heap objects are unreachable from the roots (stack, registers, globals) and reclaims them — reference counting frees deterministically but leaks cycles and costs on every pointer write; tracing collectors mark from the roots (tricolor abstraction) and either sweep in place (fragmentation) or copy survivors to a new space (Cheney's breadth-first algorithm, compaction for free); generational collectors exploit "most objects die young" with a nursery, promoting survivors and using write barriers and remembered sets to track old-to-young pointers; incremental and concurrent collectors bound pauses with barriers; Bacon et al. show tracing and counting are duals, and every production GC is a hybrid tuned for throughput, latency, or footprint.
---
# Garbage collection

**In one sentence.** Reachability is the definition of liveness the runtime can compute; every
collector is a way to compute it cheaply enough — and the trade-off is always throughput vs
pause time vs memory overhead.

## Roots and reachability
Roots: stack slots and registers of every thread, globals, JIT-held references, handles. An
object is **live** if reachable from a root by following pointers; everything else is garbage
(true liveness is undecidable; reachability over-approximates it). Precise collectors know which
words are pointers (stack maps, type info); **conservative** collectors (Boehm) treat any word
that looks like a pointer as one (no moving).

## Reference counting
Each object holds a count of incoming references; increment/decrement on pointer assignment;
free at zero (recursively). Deterministic, incremental, simple (CPython, Swift ARC, Rust `Rc`/
`Arc`, COM). Costs: a write per pointer update (atomic for `Arc` — cache traffic), space per
object, and **cycles never reach zero** — needs a backup cycle collector (CPython's `gc`,
trial deletion) or weak references. Deferred/coalesced counting reduces overhead.

## Tracing: mark–sweep (Crafting Interpreters ch. 26)
**Mark**: from the roots, traverse and set a mark bit; **tricolor** abstraction — white
(unvisited), gray (visited, children pending, on a worklist), black (done); **sweep**: walk the
heap freeing white objects onto free lists. No moving (fragmentation; allocator with size
classes — [[dynamic-memory-allocation]]), pauses proportional to heap size. Lazy sweeping and
bitmap marking amortize. **GC pacing**: trigger when heap grows by a factor (clox's 2×; Go's
GOGC target).

## Copying (Cheney 1970)
Semispace: allocate by bumping a pointer in *from-space*; at collection copy each reachable object
to *to-space* (leave a forwarding pointer), scanning copied objects breadth-first with two
pointers (scan, free) — no recursion, no mark stack. Cost proportional to live data only;
compaction and fast allocation for free; needs 2× memory and moves objects (update all
references; not for conservative roots). Mark–compact (Lisp 2, sliding) compacts in place.

## Generational (Lieberman–Hewitt, Ungar)
The **weak generational hypothesis**: most objects die young. Allocate in a small **nursery**
collected often by copying (cheap: few survivors); promote survivors to the **old generation**
collected rarely by mark–sweep/compact. Old-to-young pointers must be found without scanning
the old generation: **write barrier** on pointer stores records them in a **card table** or
**remembered set**. Most production GCs: HotSpot (G1, ZGC), .NET, V8 (Orinoco), OCaml, Go is
non-generational (concurrent mark–sweep with a small footprint goal).

## Bounding pauses
**Incremental** collectors interleave small mark steps with the mutator; **concurrent**
collectors run marking on other threads; both need barriers to preserve the tricolor invariant
(no black → white pointer): Dijkstra insertion (shade the new target) or Yuasa deletion (shade
the old target) write barriers, or Baker read barriers; snapshot-at-the-beginning vs
incremental update. Concurrent copying (ZGC, Shenandoah, C4) uses load barriers and colored
pointers for sub-millisecond pauses at multi-TB heaps. Parallel collectors use many threads for
throughput. **Real-time** GCs bound worst-case pause and utilization (Metronome).

## The unified view (Bacon, Cheng & Rajan 2004)
Tracing computes liveness from roots (fixed point from ⊥ up); reference counting computes
deadness from decrements (from ⊤ down); their dual structure means generational, deferred RC,
and concurrent designs are points on one spectrum, and real collectors mix them (e.g., RC for
the old generation, tracing nursery).

## Alternatives and interactions
Region/arena allocation and Rust's ownership give deterministic freeing without a collector
([[ownership-and-borrowing]], [[dynamic-memory-allocation]]); escape analysis stack-allocates
short-lived objects ([[compiler-optimizations]]); finalizers and weak/soft/phantom references
complicate semantics; GC and caches (locality of copied objects is good; barriers cost); GC
logs and tuning (heap size, pause targets) are part of running JVM/Go services
([[profiling-and-performance]]).

## Pitfalls
- Leaks by reachability: caches, listeners, static maps hold objects forever (use weak refs).
- Finalizers for resource cleanup (nondeterministic; use try-with-resources/RAII).
- Assuming RC is "free" in multithreaded code (atomic increments) or cycle-safe.
- Tuning a generational GC with a workload of long-lived objects (promotion storms).

## Related
- [[dynamic-memory-allocation]], [[ownership-and-borrowing]], [[bytecode-vms-and-jit]],
  [[compiler-optimizations]], [[graph-search]] (marking is graph traversal), [[virtual-memory]],
  [[synchronization-primitives]].

## Sources
Crafting Interpreters ch. 26; Cheney 1970; Bacon, Cheng & Rajan 2004; Dragon Book 7.4–7.8; CS6120 lesson 11; Jones, Hosking & Moss *The Garbage Collection Handbook*.

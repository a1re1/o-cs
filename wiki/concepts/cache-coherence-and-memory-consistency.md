---
title: Cache coherence and memory consistency — MESI, snooping vs directories, sequential consistency, TSO, and fences
type: concept
section: "4.1"
level: 400
tags: [cache-coherence, memory-consistency, mesi, snooping, directory-protocol, invalidation, false-sharing, sequential-consistency, tso, relaxed-memory-models, fences, memory-barriers, atomics, store-buffer, happens-before, data-race, c11-memory-model]
sources: [patterson-hennessy-cod, architecture-seminal-papers]
summary: Coherence makes every core eventually see one value per memory location (MESI-style invalidation protocols via bus snooping or directories; writes invalidate other copies, causing coherence misses and false sharing), while consistency defines what order writes to different locations may become visible — sequential consistency is the intuitive model, x86-TSO lets stores be delayed in a store buffer past later loads, ARM/POWER/RISC-V reorder far more — so correct lock-free code needs fences/atomics with acquire–release semantics, and languages (C11/C++11, Java, Rust) define data-race-free programs as the ones that appear sequentially consistent.
---
# Cache coherence and memory consistency

**In one sentence.** Coherence: one location, all cores agree eventually. Consistency: many
locations, what orders may cores observe — and the hardware answer is "fewer than you assume",
so synchronization must say what it needs.

## Coherence (COD 5.10, CA:AQA 5.2–5.4)
Private caches mean a write by core A can leave stale copies in B. Protocols keep one writer or
many readers per line: **MESI** states Modified (dirty, exclusive), Exclusive (clean, only copy),
Shared, Invalid (+ Owned in MOESI, Forward in MESIF). A write requires ownership: broadcast an
invalidate (**snooping** on a shared bus/ring — scales to ~10s of cores) or ask the line's home
**directory** which tracks sharers (scales to 100s/NUMA). Consequences: **coherence misses** (the
4th C); **false sharing** — unrelated variables in one 64 B line bounce between cores — pad or
separate per-thread data; atomic read-modify-write (`lock cmpxchg`, LR/SC) is implemented by
holding the line in M state. Migratory data patterns and ping-pong on contended locks are why
lock-free ≠ contention-free ([[synchronization-primitives]]).

## Consistency models
- **Sequential consistency (SC)** (Lamport): all cores see one interleaving consistent with each
  program order. Simple; hardware rarely provides it because store buffers and OoO reorder.
- **x86-TSO**: stores go into a FIFO store buffer; a later load may execute before an earlier
  store to a different address becomes visible (store→load reordering only). Dekker's algorithm
  breaks without `mfence`/locked instructions.
- **ARM/POWER/RISC-V (RVWMO)**: loads and stores reorder freely unless dependencies or fences
  (`dmb`, `fence r,rw`) constrain them; also non-multi-copy-atomic on POWER (different cores may
  see stores in different orders).
- **Litmus tests** (store buffering, message passing, load buffering, IRIW) characterize models;
  tools (herd, litmus) run them on real hardware.

## Language-level models
C11/C++11/Rust `std::sync::atomic`, Java's JMM: programs without **data races** (conflicting
accesses not ordered by synchronization) behave as SC ("DRF-SC"); racy programs are undefined (C)
or weakly defined (Java). Atomic orderings: `Relaxed` (atomicity only — counters), `Acquire` (on
load: later accesses stay after), `Release` (on store: earlier accesses stay before) — together
they build **happens-before** across threads (message passing: publish data, release-store a
flag; acquire-load, then read data); `SeqCst` for global ordering (Dekker-style). Locks and
channels are acquire/release pairs; compilers must not reorder across them either. Volatile is
not atomic (C/C++) ([[undefined-behavior]], [[ownership-and-borrowing]] — Send/Sync).

## Practical rules
1. Use locks, channels, and library atomics; write lock-free code only with a model-checker
   habit (loom, CDSChecker, TLA+).
2. Default to acquire/release for flags and SeqCst when unsure; never Relaxed for
   synchronization.
3. Pad hot per-core counters to cache-line size; batch updates locally, publish rarely.
4. Reason with happens-before, not with "the CPU will probably…" — the reordering that bites
   appears under load, on ARM, in production.

## Related
- [[synchronization-primitives]], [[caches-and-memory-hierarchy]], [[parallel-architectures-simd-gpu]],
  [[undefined-behavior]], [[ownership-and-borrowing]], [[distributed-systems-basics]] (consistency
  models reappear at datacenter scale).

## Sources
COD 5.10; CA:AQA ch. 5; Sorin, Hill & Wood *A Primer on Memory Consistency and Cache Coherence*; Sewell et al. x86-TSO; C++11 memory model.

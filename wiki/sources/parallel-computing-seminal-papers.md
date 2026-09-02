---
title: Parallel computing seminal papers — Amdahl (1967), Lamport sequential consistency (1979), Gustafson (1988), Herlihy & Wing linearizability (1990), Herlihy wait-free synchronization (1991), Adve & Gharachorloo memory consistency tutorial (1996), Blumofe & Leiserson Cilk work stealing (1999), Frigo et al. cache-oblivious algorithms (1999), Williams et al. Roofline (2009), Dean & Barroso The Tail at Scale (2013), CUDA (2008)
type: source
section: "4.7"
level: 500
tags: [amdahl, gustafson, sequential-consistency, linearizability, herlihy-wing, wait-free, consensus-hierarchy, consensus-number, adve-gharachorloo, memory-consistency, cilk, work-stealing, blumofe-leiserson, cache-oblivious, frigo, roofline, williams-waterman-patterson, tail-at-scale, dean-barroso, cuda, nickolls]
sources: []
authors: [Gene Amdahl, Leslie Lamport, John Gustafson, Maurice Herlihy, Jeannette Wing, Sarita Adve, Kourosh Gharachorloo, Robert Blumofe, Charles Leiserson, Matteo Frigo, Harald Prokop, Sridhar Ramachandran, Samuel Williams, Andrew Waterman, David Patterson, Jeffrey Dean, Luiz Barroso, John Nickolls]
year: 1967
institution: various
url: https://cs.brown.edu/~mph/Herlihy91/p124-herlihy.pdf
license: various
format: pdf
summary: Amdahl bounded speedup by the serial fraction (1/(s + (1−s)/p)) and Gustafson answered that problems scale with machines (scaled speedup); Lamport defined sequential consistency for multiprocessors; Herlihy & Wing defined linearizability as the correctness condition for concurrent objects (each operation appears to take effect at one instant between call and return; composable, unlike serializability); Herlihy's wait-free synchronization built the consensus hierarchy — read/write registers have consensus number 1, test-and-set and fetch-and-add 2, compare-and-swap ∞ — proving which primitives can implement which objects without locks and that CAS is universal; Adve & Gharachorloo explained relaxed memory models and why programmers want sequential consistency for data-race-free programs; Blumofe & Leiserson proved randomized work stealing achieves expected time T₁/P + O(T∞) with bounded space; Frigo, Leiserson, Prokop & Ramachandran gave algorithms optimal for every cache level without knowing its parameters; Williams, Waterman & Patterson's Roofline plots attainable GFLOP/s against arithmetic intensity to show whether a kernel is compute- or memory-bound; Dean & Barroso showed how latency tails compound across fan-out and how hedged and tied requests tame them; and Nickolls et al. introduced CUDA's scalable SIMT model.
---
# Parallel computing seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Amdahl, "Validity of the Single Processor Approach…" (1967); Gustafson, "Reevaluating Amdahl's Law" (1988) | Speedup ≤ 1/(s + (1−s)/p): the serial fraction dominates; Gustafson: with fixed time and growing problem size, scaled speedup = s + p(1−s) | [[performance-equation-and-amdahl]], [[parallel-programming-models]] |
| Lamport, "How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs" (1979) | **Sequential consistency**: results as if all operations executed in some sequential order consistent with each processor's program order | [[cache-coherence-and-memory-consistency]] |
| Herlihy & Wing, "Linearizability: A Correctness Condition for Concurrent Objects" (1990) | Each operation appears to take effect instantaneously between invocation and response; **local/composable** (linearizable components compose), non-blocking as a property; verification by linearization points | [[lock-free-programming]], [[consistency-models]] |
| Herlihy, "Wait-Free Synchronization" (1991) | Wait-free: every process completes in finitely many steps regardless of others; reduction to consensus gives the **consensus hierarchy** (registers 1; TAS, FAA, queues, stacks 2; CAS, LL/SC ∞); universal construction from a consensus object | [[lock-free-programming]] |
| Adve & Gharachorloo, "Shared Memory Consistency Models: A Tutorial" (1996) | Why hardware relaxes (write buffers, reordering), the models (SC, TSO, PC, PSO, weak, release consistency), and the programmer's contract: **SC for data-race-free programs** | [[cache-coherence-and-memory-consistency]] |
| Blumofe & Leiserson, "Scheduling Multithreaded Computations by Work Stealing" (1999) | Randomized work stealing: expected time T₁/P + O(T∞), space ≤ S₁·P, communication bounded — the Cilk scheduler's guarantee | [[work-stealing-and-fork-join]] |
| Frigo, Leiserson, Prokop & Ramachandran, "Cache-Oblivious Algorithms" (1999) | Ideal-cache model; recursive algorithms (matrix multiply, FFT, funnelsort, B-trees via van Emde Boas layout) with optimal cache complexity at every level with no tuning parameters | [[cache-oblivious-algorithms]] |
| Nickolls, Buck, Garland & Skadron, "Scalable Parallel Programming with CUDA" (2008) | Hierarchy of threads, blocks, grids; shared memory and barriers; SIMT execution — scalable across GPU sizes | [[gpu-programming-cuda]] |
| Williams, Waterman & Patterson, "Roofline: An Insightful Visual Performance Model" (2009) | Attainable performance = min(peak FLOP/s, bandwidth × arithmetic intensity); ceilings for missing optimizations (SIMD, ILP, prefetching, NUMA) show which to attempt first | [[roofline-model]] |
| Dean & Barroso, "The Tail at Scale" (2013) | Tail latency amplified by fan-out (1 in 100 slow → 63 % of 100-way requests slow); causes (shared resources, GC, queueing, power); cures — hedged requests, tied requests, micro-partitions, selective replication, latency-induced probation, canary requests | [[tail-latency-at-scale]] |

## Why read them
Amdahl and Roofline are the two graphs every performance engineer redraws; Herlihy's
hierarchy tells you why CAS is in every ISA; Blumofe–Leiserson is the reason "just spawn tasks"
works; Dean & Barroso is why p99 matters more than mean.

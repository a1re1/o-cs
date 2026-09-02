---
title: Parallel programming models — shared address space (threads/OpenMP), message passing (MPI), data parallel (ISPC/SIMD), and the decomposition–assignment–orchestration–mapping recipe
type: concept
section: "4.7"
level: 400
tags: [parallel-programming, shared-address-space, threads, openmp, message-passing, mpi, data-parallel, spmd, ispc, simd, gangs, decomposition, assignment, orchestration, mapping, static-assignment, dynamic-assignment, load-balance, granularity, locality, communication, contention, arithmetic-intensity, amdahl, gustafson, speedup, efficiency, isoefficiency, strong-scaling, weak-scaling, false-sharing, collective-operations, reduction, scan, halo-exchange, stencil]
sources: [stanford-cs149-and-cmu-15-418, parallel-programming-texts, parallel-computing-seminal-papers]
summary: Parallel programs are written against three abstractions — a shared address space (threads communicating through memory with locks/atomics; OpenMP pragmas for loops and tasks; the hardware keeps caches coherent), message passing (MPI: private memories, explicit send/receive and collectives — broadcast, reduce, scatter/gather, all-to-all; the model that scales to supercomputers), and data parallelism (the same function over every element, SPMD gangs in ISPC, SIMD lanes, CUDA threads; map/reduce/scan as primitives) — and the work of parallelizing is a fixed recipe: decompose into tasks (enough for the machine, Amdahl's serial fraction is the ceiling), assign tasks to workers (static for predictable work, dynamic/work-stealing for irregular), orchestrate communication and synchronization (reduce it, batch it, overlap it), and map to hardware (locality, NUMA, avoid contention and false sharing); performance is then a matter of load balance, communication-to-computation ratio (arithmetic intensity), and whether you measure strong scaling (fixed problem) or weak scaling (fixed per-processor work, Gustafson).
---
# Parallel programming models

**In one sentence.** Three ways to say "these can happen at once" — share memory, pass
messages, or apply one function everywhere — and one recipe for turning a program into any of
them without losing to communication.

## Why parallelism, why efficiency (CS149 L1–2)
Single-thread performance stalled (power wall, ILP limits — [[pipelining-and-hazards]]); the
transistors went to multi-core, SIMD (wide vector units), and hardware multithreading to hide
memory latency; bandwidth, not FLOPs, is the usual limit ([[roofline-model]]). **Speedup**
S(p) = T₁/T_p; **efficiency** S/p; **Amdahl**: S ≤ 1/(s + (1−s)/p) — 5 % serial caps at 20×;
**Gustafson**: scale the problem with p (weak scaling) and the serial fraction shrinks;
**isoefficiency** (Grama): how fast the problem must grow to hold efficiency. Superlinear
speedup = cache effects.

## The three models (CS149 L3–4; Grama ch. 3, 6–7)
| Model | Communication | Sync | Tools | Fits |
|---|---|---|---|---|
| **Shared address space** | loads/stores to shared variables; hardware coherence ([[cache-coherence-and-memory-consistency]]) | locks, atomics, barriers, condition variables ([[synchronization-primitives]]) | pthreads, OpenMP (`#pragma omp parallel for`, reductions, tasks, schedule(static/dynamic)), Java/C++ threads, Cilk/TBB | multicores, NUMA nodes |
| **Message passing** | explicit `send`/`recv` between private address spaces; collectives (broadcast, reduce/all-reduce, scatter/gather, all-to-all, barrier) | message completion; blocking vs non-blocking (`MPI_Isend` + `MPI_Wait`) for overlap | MPI (SPMD ranks, communicators, derived datatypes, one-sided RMA), Erlang/actors, Go channels ([[async-and-event-driven-concurrency]]) | clusters, supercomputers; also disciplined design on shared memory |
| **Data parallel** | implicit — the same operation on each element; gather/scatter | implicit barriers between phases | ISPC (SPMD on SIMD — `foreach`, gangs, uniform/varying), CUDA/OpenCL ([[gpu-programming-cuda]]), NumPy/JAX, SQL, Spark ([[mapreduce-and-dataflow]]), Halide | regular loops over arrays; map, reduce, scan, filter, sort, groupByKey compose into most numerical and analytics code |
Hybrid MPI + OpenMP + CUDA is the HPC norm. Data-parallel primitives (CS149 L8): **scan**
(prefix sum — Blelloch's work-efficient up/down sweep, O(n) work, O(log n) span) underlies
stream compaction, radix sort, segmented operations.

## The recipe (CS149 L4–6; Culler & Singh)
1. **Decomposition** into tasks — find enough independent work (data, functional, recursive,
   exploratory decomposition — Grama); dependencies form a DAG; Amdahl's serial parts.
2. **Assignment** of tasks to workers — **static** (blocked/interleaved; cheap; needs predictable
   cost) vs **dynamic** (work queues, task granularity vs overhead, work stealing —
   [[work-stealing-and-fork-join]]); load balance; a few big tasks at the end hurt (schedule
   long ones first).
3. **Orchestration** — structure communication and synchronization: reduce it (larger grains,
   replication, privatization then reduce), batch it, **overlap** it with computation (non-
   blocking sends, pipelining, double buffering); barriers vs point-to-point; inherent vs
   artifact communication; the **communication-to-computation ratio** / arithmetic intensity
   grows with block size (surface-to-volume: halo exchange in stencils).
4. **Mapping** to hardware — threads to cores, ranks to nodes, locality (NUMA first-touch, cache
   blocking), avoid **contention** (hot locks, atomics on one address, false sharing of cache
   lines — pad to 64 B, memory-controller/bank conflicts).
Case studies: grid solver (red-black ordering to remove dependencies; barrier count), ocean
simulation, Barnes–Hut (cost estimation for assignment), ray tracing (dynamic).

## Measuring (CS149, 6.172, Grama ch. 5)
Fix the baseline (best sequential, not 1-thread parallel); report strong and weak scaling;
profile where time goes (compute vs sync vs communication); check bandwidth vs peak
([[roofline-model]], [[profiling-and-performance]]); beware measurement noise and
frequency scaling ([[tail-latency-at-scale]] for distributed).

## Pitfalls
- Parallelizing before optimizing the serial code (6.172's 50,000× matmul story).
- Fine-grained tasks whose overhead exceeds their work; global barriers everywhere.
- False sharing and contended atomics silently serializing "parallel" loops.
- Data races in shared-memory code (use race detectors; prefer data-parallel structure).
- Reporting speedup against a slow baseline.

## Related
- [[gpu-programming-cuda]], [[work-stealing-and-fork-join]], [[lock-free-programming]],
  [[roofline-model]], [[cache-coherence-and-memory-consistency]], [[parallel-architectures-simd-gpu]],
  [[synchronization-primitives]], [[processes-and-threads]], [[performance-equation-and-amdahl]],
  [[mapreduce-and-dataflow]].

## Sources
CS149 L1–8; 15-418; Grama et al. ch. 2–7; Culler, Singh & Gupta; Amdahl 1967; Gustafson 1988; Blelloch "Prefix Sums and Their Applications" 1990.

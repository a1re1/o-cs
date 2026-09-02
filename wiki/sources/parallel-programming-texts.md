---
title: Parallel programming texts — Kirk & Hwu Programming Massively Parallel Processors, Grama et al. Introduction to Parallel Computing, Herlihy & Shavit The Art of Multiprocessor Programming, McKenney Is Parallel Programming Hard (free), and McCool/Reinders/Robison Structured Parallel Programming
type: source
section: "4.7"
level: 400
tags: [pmpp, kirk-hwu, cuda-textbook, grama, introduction-to-parallel-computing, mpi, herlihy-shavit, art-of-multiprocessor-programming, lock-free, mckenney, perfbook, rcu, structured-parallel-programming, patterns]
sources: []
authors: [David Kirk, Wen-mei Hwu, Ananth Grama, Anshul Gupta, George Karypis, Vipin Kumar, Maurice Herlihy, Nir Shavit, Paul McKenney, Michael McCool, James Reinders, Arch Robison]
year: 2022
institution: various
url: https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html
license: mixed (McKenney free)
format: pdf
summary: Kirk & Hwu (4th ed.) is the CUDA textbook — heterogeneous computing, the CUDA execution model, memory hierarchy and tiling, performance considerations (coalescing, occupancy, divergence), parallel patterns (convolution, stencil, histogram, reduction, scan, merge, sort, sparse, graph), dynamic parallelism, and applications; Grama et al. is the classical parallel algorithms text — models (PRAM, network topologies), decomposition and mapping, analytical models (speedup, efficiency, isoefficiency), MPI and threads, and algorithms for matrix operations, sorting, graphs, search and dynamic programming; Herlihy & Shavit is the concurrent data structures book — mutual exclusion, linearizability, the consensus hierarchy, spin locks, monitors, linked lists (coarse/fine/optimistic/lazy/lock-free), queues, stacks, counting networks, hash maps, skip lists, priority queues, barriers, transactional memory; McKenney's perfbook (free) is the Linux-kernel view — hardware costs, counting, partitioning, locking, data ownership, deferred processing (reference counting, hazard pointers, sequence locks, RCU), memory ordering, validation; and Structured Parallel Programming catalogs the patterns (map, reduce, scan, fork-join, pipeline, stencil) with TBB, Cilk Plus and OpenCL examples.
---
# Parallel programming texts

## What they are
- **Kirk & Hwu, PMPP**: part I fundamentals (heterogeneous computing, data parallelism and
  CUDA C, scalable execution — blocks, warps, scheduling; memory architecture — global/shared/
  constant/registers, tiled matrix multiply; performance — coalescing, control divergence,
  occupancy, DRAM banks); part II patterns (convolution, stencil, histogram with atomics/
  privatization, reduction, prefix sum/scan — Kogge–Stone/Brent–Kung, merge, sort — radix,
  sparse matrix formats — CSR/ELL/JDS, graph traversal — BFS frontiers); part III advanced
  (dynamic parallelism, streams and multi-GPU, CUDA-aware MPI, deep learning); part IV
  applications and outlook.
- **Grama, Gupta, Karypis, Kumar**: parallel platforms (implicit parallelism, memory
  limits, interconnects, communication costs), principles of parallel algorithm design
  (decomposition — recursive, data, exploratory, speculative; mapping), basic communication
  operations (broadcast, reduction, scatter/gather, all-to-all), analytical modelling (overhead,
  speedup, efficiency, Amdahl/Gustafson, isoefficiency, scalability), programming with MPI and
  with threads/OpenMP, dense matrix algorithms, sorting, graph algorithms, discrete
  optimization/search, dynamic programming, FFT.
- **Herlihy & Shavit, TAMP**: principles — mutual exclusion (Peterson, bakery, lower bounds),
  concurrent objects and linearizability, the foundations of shared memory (registers,
  snapshots), the relative power of primitives (consensus numbers, universality of CAS);
  practice — spin locks and contention (TAS/TTAS, backoff, queue locks — MCS/CLH), monitors,
  linked lists (coarse, fine, optimistic, lazy, lock-free), concurrent queues and the ABA
  problem, stacks and elimination, counting networks, hashing and natural parallelism, skip
  lists, priority queues, futures and work stealing, barriers, transactional memory.
- **McKenney, perfbook**: hardware and its habits (cache misses cost hundreds of cycles),
  tools of the trade, counting (the simplest hard problem), partitioning and synchronization
  design, locking (deadlock, livelock, lock types), data ownership, deferred processing
  (reference counting, hazard pointers, sequence locks, **RCU** — grace periods, read-side
  zero cost), data structures, validation (why concurrent code is hard to test), formal
  verification (Promela/spin, litmus tests), memory ordering (the Linux kernel memory model),
  putting it together, advanced synchronization, parallel real-time.
- **Structured Parallel Programming**: pattern language — nesting, map, collectives (reduce,
  scan), data reorganization (gather, scatter, pack), stencil/recurrence, fork-join, pipeline;
  examples in TBB, Cilk Plus, OpenMP, ArBB, OpenCL.

## Key ideas → pages
[[gpu-programming-cuda]], [[parallel-programming-models]], [[lock-free-programming]],
[[work-stealing-and-fork-join]], [[synchronization-primitives]], [[cache-coherence-and-memory-consistency]].

## What they add
PMPP for GPUs, Grama for the theory of speedup, Herlihy & Shavit for the correctness of
concurrent objects, McKenney for how a kernel actually scales.

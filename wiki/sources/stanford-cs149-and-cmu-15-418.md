---
title: Stanford CS149 / CMU 15-418 Parallel Computing (Fatahalian, Olukotun, Mowry), MIT 6.172 Performance Engineering (Leiserson), Berkeley CS267, and UIUC ECE408 / NVIDIA CUDA teaching kit
type: source
section: "4.7"
level: 400
tags: [cs149, 15-418, parallel-computing-course, fatahalian, 6-172, performance-engineering, leiserson, cs267, ece408, cuda-course, ispc, cilk, openmp, mpi]
sources: []
institution: Stanford / CMU / MIT / Berkeley
year: 2024
url: https://gfxcourses.stanford.edu/cs149/fall24/
license: open-course (slides and videos public)
format: html
summary: CS149 and its CMU twin 15-418 teach parallel computing from the hardware up — why parallelism and efficiency; the modern multicore (multi-core, SIMD, hardware multithreading; latency vs bandwidth); programming abstractions (ISPC, shared address space, message passing, data parallel); parallelizing a program (decomposition, assignment, orchestration, mapping); performance optimization (work distribution and scheduling, Cilk work stealing; locality, communication, contention); GPU architecture and CUDA; data-parallel thinking (map, reduce, scan, groupByKey); Spark; efficient DNN evaluation; hardware specialization and accelerators; cache coherence (MSI/MESI, false sharing), memory consistency, lock implementations and lock-free programming, transactional memory — with assignments on a quad-core CPU, task-graph scheduling, a CUDA renderer, a DNN accelerator, and OpenMP graph processing; 6.172 is the single-machine performance course (Bentley rules, bit hacks, cache-efficient and cache-oblivious algorithms, Cilk and race detection, vectorization, profiling), CS267 the HPC/scientific-computing course (MPI, UPC, dense/sparse linear algebra, roofline), and ECE408 the CUDA course behind Kirk & Hwu.
---
# CS149 / 15-418 and related courses

## What it is
**CS149 Fall 2024** (also 15-418 Spring 2024): 1 why parallelism, why efficiency; 2 a modern
multi-core processor — multi-core, SIMD, multithreading, latency hiding; 3 ISPC and
programming abstractions; 4 parallel programming basics — the decomposition/assignment/
orchestration/mapping recipe, data-parallel vs shared-address-space vs message-passing models,
the ocean and grid solver case study; 5 work distribution and scheduling — static/dynamic
assignment, work stealing (Cilk); 6 locality, communication, contention — message passing,
blocking vs async, pipelining, arithmetic intensity, reducing communication; 7 GPU
architecture and CUDA; 8 data-parallel thinking — map, reduce, scan, prefix sum, segmented
scan, groupByKey; 9 Spark; 10 efficiently evaluating DNNs; 11–12 hardware specialization;
13–14 cache coherence (MSI/MESI, false sharing, directories in 15-418); 15 locks, fine-grained
synchronization, lock-free programming; 16 relaxed consistency and domain-specific systems
(Halide, graph DSLs); 17–18 transactional memory. 15-418 adds interconnection networks,
workload-driven evaluation, heterogeneous parallelism, parallel deep learning (data/model/
pipeline parallelism). Assignments: analyzing performance on a quad-core (ISPC, threads), task
graphs, CUDA renderer, DNN accelerator, OpenMP graphs (PageRank/BFS).
**MIT 6.172** (Leiserson, Shun): introduction and matrix multiplication (from Python to
vectorized C — 50,000× speedup), Bentley's rules for optimizing work, bit hacks, computer
architecture and assembly, C to assembly, multicore programming (Cilk), races and parallelism
(work/span, race detection), analysis of multithreaded algorithms, what compilers can and
cannot do, measurement and timing, storage allocation, parallel storage allocation, cache-
efficient algorithms, cache-oblivious algorithms, synchronization without locks, DSLs and
autotuning, speculative parallelism, tuning a TSP algorithm, graph optimization.
**CS267** (Demmel, Yelick): parallel machines and models, shared memory (OpenMP), distributed
memory (MPI), UPC/GPUs, sources of parallelism in simulation, dense linear algebra (BLAS,
LAPACK, communication-avoiding algorithms), sparse/structured grids/particle methods (N-body,
FMM), FFT, load balancing, roofline, big data and ML at scale.
**ECE408 / PMPP kit**: CUDA basics, memory and tiling, convolution, reduction, scan,
histogram, sparse, dynamic parallelism, streams.

## Key ideas → pages
[[parallel-programming-models]], [[gpu-programming-cuda]], [[work-stealing-and-fork-join]],
[[lock-free-programming]], [[roofline-model]], [[cache-oblivious-algorithms]],
[[tail-latency-at-scale]], [[profiling-and-performance]], [[cache-coherence-and-memory-consistency]].

## What it adds
CS149 is the map from hardware to abstraction; 6.172 the discipline of measuring; CS267 the
numerical HPC lineage.

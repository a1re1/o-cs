---
title: Computer Organization and Design RISC-V Edition (Patterson & Hennessy) and Computer Architecture: A Quantitative Approach
type: source
section: "4.1"
level: 300
tags: [computer-architecture, risc-v, isa, datapath, pipelining, hazards, caches, memory-hierarchy, virtual-memory, parallelism, gpus, quantitative-approach, amdahl, benchmarks, ilp, tlp, dlp, warehouse-scale, domain-specific-architectures]
sources: []
authors: [David A. Patterson, John L. Hennessy]
year: 2020
institution: Berkeley / Stanford
url: https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-820331-6
license: proprietary
format: book
summary: COD (the undergraduate text behind CS61C and many others) walks from the eight great ideas (Moore's law, abstraction, make the common case fast, parallelism, pipelining, prediction, memory hierarchy, dependability via redundancy) through performance (CPU time = instructions × CPI × cycle time; Amdahl), the RISC-V ISA, arithmetic (integer, IEEE floating point), the processor (single-cycle datapath, pipelining, hazards, forwarding, branch prediction, exceptions, ILP), the memory hierarchy (caches, virtual memory, TLBs, coherence), parallel processors (multicore, SIMD, GPUs, clusters); CA:AQA is the graduate sequel — quantitative principles, memory hierarchy design, ILP (out-of-order, speculation), DLP (vector, SIMD, GPU), TLP (coherence, consistency), warehouse-scale computers, and domain-specific architectures.
---
# Computer Organization and Design / Computer Architecture: A Quantitative Approach

## What it is
**COD RISC-V** ch. 1 computer abstractions and technology (great ideas; below your program;
under the covers; performance — the CPU performance equation, power wall, the switch to
multicore; benchmarks (SPEC); fallacies — Amdahl's law, MIPS as a metric); 2 instructions:
language of the computer (RISC-V operations, operands, registers, memory, immediates, signed/
unsigned, encoding, logical ops, branches, procedures and the stack, characters/strings,
addressing modes, synchronization (LR/SC), translating and starting a program — compiler,
assembler, linker, loader — with x86 and ARM contrasts); 3 arithmetic (add/sub, multiply,
divide, IEEE 754 floating point and its pitfalls, subword parallelism); 4 the processor (logic
design conventions, building a datapath, single-cycle implementation, **pipelining** — the
laundry analogy, pipelined datapath and control, **data hazards** with forwarding and stalls,
**control hazards** with prediction, exceptions, ILP — superscalar, dynamic scheduling, speculation;
Intel Core i7 and ARM Cortex-A53 case studies; fallacies); 5 large and fast: the memory
hierarchy (locality, cache basics — direct-mapped, sets, blocks; measuring and improving
performance — AMAT, associativity, multilevel; dependable memory (ECC, RAID); **virtual
memory** — pages, page tables, TLBs, protection; a common framework — the four questions: where
can a block go, how is it found, which is replaced, what happens on a write; cache coherence;
cache blocking for matrix multiply); 6 parallel processors (difficulty, SISD/SIMD/MIMD,
multithreading, multicore/shared memory, GPUs, clusters and warehouse-scale, network topologies,
benchmarks/roofline). Appendices: logic design, graphics processors.
**CA:AQA** (6th ed.) ch. 1 fundamentals of quantitative design (trends, power, cost,
dependability, measuring performance, quantitative principles: Amdahl, the processor performance
equation, locality, parallelism); 2 memory hierarchy design (ten advanced optimizations, VM and
virtual machines); 3 ILP (compiler techniques, branch prediction, dynamic scheduling/Tomasulo,
speculation, multiple issue, limits on ILP, SMT); 4 DLP (vector architectures, SIMD extensions,
GPUs, loop-level parallelism); 5 TLP (centralized vs distributed shared memory, snooping and
directory coherence, synchronization, memory consistency); 6 warehouse-scale computers; 7
domain-specific architectures (TPU, Pixel Visual Core, Microsoft Catapult); appendices on
pipelining, ISA principles, memory hierarchy review, storage, networks, vector processors.

## Key ideas → pages
[[isa-and-assembly]], [[pipelining-and-hazards]], [[caches-and-memory-hierarchy]],
[[virtual-memory]], [[performance-equation-and-amdahl]], [[parallel-architectures-simd-gpu]],
[[cache-coherence-and-memory-consistency]], [[floating-point]].

## What it adds
The standard vocabulary and the quantitative habit (measure, model, then design); [[csapp-15-213]]
is the programmer's-eye version, [[nand2tetris]] the build-it-yourself version.

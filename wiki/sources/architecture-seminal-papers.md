---
title: Architecture seminal papers — von Neumann's EDVAC report (1945), Tomasulo (1967), Patterson & Ditzel "The Case for the RISC" (1980), Hennessy & Patterson "A New Golden Age" (2019), Spectre/Meltdown (2018), Moore and Dennard
type: source
section: "4.1"
level: 400
tags: [von-neumann, edvac, stored-program, tomasulo, out-of-order, reservation-stations, register-renaming, risc, cisc, patterson-ditzel, golden-age, domain-specific-architectures, spectre, meltdown, speculative-execution, side-channels, moores-law, dennard-scaling, history]
sources: []
authors: [John von Neumann, Robert Tomasulo, David Patterson, David Ditzel, John Hennessy, Paul Kocher, Moritz Lipp, Gordon Moore, Robert Dennard]
year: 1945
institution: various
url: https://web.mit.edu/STS.035/www/PDFs/edvac.pdf
license: various
format: pdf
summary: Six landmarks — von Neumann's First Draft fixed the stored-program architecture (memory holding both instructions and data, a control unit, an arithmetic unit, I/O; the serial fetch–execute cycle that Backus later called the bottleneck); Tomasulo's IBM 360/91 algorithm introduced reservation stations, register renaming via tags and a common data bus — the template for every out-of-order core; Patterson & Ditzel argued that simpler instruction sets exploited compilers and pipelining better than microcoded CISC (measurements over intuitions); Hennessy & Patterson's Turing lecture explains why the end of Dennard scaling and Moore's law makes domain-specific architectures, open ISAs (RISC-V) and agile hardware design the new opportunity; Spectre and Meltdown showed speculative execution leaks secrets through cache side channels, breaking the ISA-as-contract assumption; Moore's 1965 doubling and Dennard's 1974 constant-power scaling were the tailwinds whose end explains the last two decades.
---
# Architecture seminal papers

| Paper | Contribution | Page |
|---|---|---|
| von Neumann, "First Draft of a Report on the EDVAC" (1945) | Stored-program computer: CA (arithmetic), CC (control), M (memory), I/O; binary; sequential execution — the von Neumann architecture and its bottleneck | [[isa-and-assembly]], [[backus-can-programming-be-liberated]] |
| Tomasulo, "An Efficient Algorithm for Exploiting Multiple Arithmetic Units" (1967) | Reservation stations, tag-based register renaming, common data bus: dynamic scheduling that removes WAR/WAW hazards and tolerates variable latencies; basis of modern OoO with a reorder buffer for precise exceptions | [[pipelining-and-hazards]] |
| Patterson & Ditzel, "The Case for the Reduced Instruction Set Computer" (1980) | Complex instructions are rarely used by compilers, slow the common case, and complicate pipelining; simple load/store ISAs with many registers and single-cycle instructions win on measured workloads — RISC I/II, MIPS, SPARC, ARM, RISC-V descend from it | [[isa-and-assembly]] |
| Hennessy & Patterson, "A New Golden Age for Computer Architecture" (Turing lecture, CACM 2019) | History (CISC vs RISC, VLIW's failure), the end of Dennard scaling (2004) and slowing Moore's law, security's rethink after Spectre; opportunities: domain-specific architectures (TPU: 30–80× perf/W), domain-specific languages, open ISAs (RISC-V), agile hardware development | [[parallel-architectures-simd-gpu]], [[performance-equation-and-amdahl]] |
| Kocher et al., "Spectre Attacks"; Lipp et al., "Meltdown" (2018) | Speculative and out-of-order execution leave microarchitectural traces (cache state) that timing side channels read, leaking memory across privilege boundaries; mitigations (KPTI, retpoline, fences) cost performance | [[pipelining-and-hazards]], [[caches-and-memory-hierarchy]], [[security-principles]] |
| Moore (1965), Dennard et al. (1974) | Transistor count doubling ~2 years; scaling voltage with dimensions keeps power density constant — until leakage ended it (~2005), forcing multicore and specialization | [[performance-equation-and-amdahl]] |

## Why read them
Each names a constraint that still governs design: the fetch bottleneck, hazards vs latency,
compilers as the ISA's real customer, physics ending free speedups, and speculation's security
cost.

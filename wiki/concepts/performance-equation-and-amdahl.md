---
title: The processor performance equation, Amdahl's law, benchmarks, and the power wall
type: concept
section: "4.1"
level: 200
tags: [performance, cpu-time, instruction-count, cpi, clock-cycle, amdahl, speedup, benchmarks, spec, mips-fallacy, power-wall, dennard-scaling, moores-law, multicore, roofline, energy-efficiency, latency-throughput, great-ideas]
sources: [patterson-hennessy-cod, architecture-seminal-papers]
summary: CPU time = instruction count × cycles per instruction × cycle time — the compiler/ISA, the microarchitecture, and the technology each own one factor — and Amdahl's law (speedup = 1 / ((1 − f) + f/s)) caps any optimization by the fraction it touches; performance must be measured on real programs (SPEC), not MIPS or clock rate, and since Dennard scaling ended (~2005) power, not transistors, limits designs, which is why single-thread gains slowed and cores, SIMD, and accelerators took over — the "eight great ideas" (abstraction, common case fast, parallelism, pipelining, prediction, memory hierarchy, redundancy, Moore's law) organize the whole field.
---
# Performance equation, Amdahl's law, and the power wall

**In one sentence.** Only *time* is performance; decompose it, find the biggest factor you can
change, and remember that the untouched fraction sets the ceiling.

## The equation (COD 1.6)
CPU time = **instructions** × **CPI** × **clock period** (= IC × CPI / f).
- Instruction count: algorithm, compiler, ISA ([[isa-and-assembly]], [[compiler-optimizations]]).
- CPI: microarchitecture — pipelining, hazards, cache misses (CPI = base CPI + memory stall
  cycles per instruction) ([[pipelining-and-hazards]], [[caches-and-memory-hierarchy]]).
- Clock: technology and pipeline depth ([[digital-logic-and-the-alu]]).
Fallacies: clock rate or MIPS as performance (a RISC executes more, simpler instructions); one
subset benchmark; "peak" numbers. Use **execution time of real workloads** — SPEC CPU (geometric
mean of normalized times), SPECpower, MLPerf, or your own traces. Latency vs throughput:
optimize what the user waits for; tail latency for services ([[profiling-and-performance]]).

## Amdahl's law
Speedup_overall = 1 / ((1 − f) + f / s) for fraction f sped up by s. With f = 0.9 and s → ∞,
speedup → 10. Corollaries: make the **common case fast**; parallel speedup on p processors is
bounded by 1/(1 − f) (Gustafson's reply: problems grow with p, so f grows); optimizing a 5%
phase 10× yields 4.7%. The same law governs [[profiling-and-performance]] decisions.

## Technology trends
- **Moore's law** (1965): transistors per chip double ≈ every 2 years — slowing since ~2015
  (cost per transistor flat, nodes at 3 nm are marketing units).
- **Dennard scaling** (1974): shrinking transistors keeps power density constant — ended ~2005
  when leakage current dominated; clocks stalled at ~3–5 GHz. Power ≈ C·V²·f + leakage: the
  **power wall**. Result: multicore (2005), dark silicon, DVFS, and specialization.
- Hennessy–Patterson's "golden age": with general-purpose gains at ~3%/year, **domain-specific
  architectures** (TPUs, GPUs for ML, video codecs), DSLs to program them, open ISAs (RISC-V)
  and agile chip design are where the 10–100× wins now come from
  ([[parallel-architectures-simd-gpu]]).
- **Roofline model**: attainable FLOP/s = min(peak compute, arithmetic intensity × memory
  bandwidth) — tells whether a kernel is compute- or memory-bound.

## The eight great ideas (COD 1.2)
Design for Moore's law; use abstraction to simplify design; make the common case fast;
performance via parallelism; via pipelining; via prediction; hierarchy of memories;
dependability via redundancy. Nearly every later page in §4 is one of these.

## Pitfalls
- Reporting speedup without saying the baseline and the fraction affected.
- Comparing across machines with different compilers/flags; benchmarking debug builds.
- Energy: perf/W and perf/$ often matter more than peak; mobile and datacenters optimize
  energy per task.

## Related
- [[profiling-and-performance]], [[pipelining-and-hazards]], [[caches-and-memory-hierarchy]],
  [[parallel-architectures-simd-gpu]], [[asymptotic-notation]], [[isa-and-assembly]].

## Sources
COD ch. 1; CA:AQA ch. 1; Hennessy & Patterson Turing lecture 2019; Moore 1965; Dennard 1974.

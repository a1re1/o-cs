---
title: Pipelining, hazards, branch prediction, and out-of-order execution
type: concept
section: "4.1"
level: 300
tags: [pipelining, pipeline-stages, hazards, data-hazards, control-hazards, structural-hazards, forwarding, stalls, branch-prediction, speculation, out-of-order, tomasulo, register-renaming, reorder-buffer, superscalar, ilp, smt, exceptions, precise-exceptions, spectre]
sources: [patterson-hennessy-cod, architecture-seminal-papers, csapp-15-213]
summary: Pipelining overlaps instruction stages (fetch, decode, execute, memory, writeback) to raise throughput without changing latency, but dependencies create hazards — data (fix with forwarding, stall for load-use), control (predict branches; flush on mispredict), structural (duplicate resources) — and modern cores go further with superscalar issue, dynamic scheduling (Tomasulo's reservation stations and register renaming), speculation with a reorder buffer for precise exceptions, and simultaneous multithreading; the same machinery is why Spectre exists and why branchy, pointer-chasing code is slow.
---
# Pipelining and hazards

**In one sentence.** Do laundry with the washer and dryer running at once: throughput rises
toward one instruction per cycle, and every complication in a modern core is about keeping
the pipeline full when instructions depend on each other.

## The five-stage RISC pipeline (COD ch. 4)
IF (fetch) → ID (decode, read registers) → EX (ALU) → MEM (load/store) → WB (write register).
Pipeline registers between stages; ideal speedup = number of stages; cycle time set by the
slowest stage plus register overhead ([[digital-logic-and-the-alu]]). RISC ISAs pipeline well
because instructions are uniform length, few formats, load/store only, aligned operands
([[isa-and-assembly]]).

## Hazards and their fixes
| Hazard | Cause | Fix |
|---|---|---|
| **Structural** | two instructions need the same unit (single memory for IF and MEM) | separate I/D caches; more ports/units |
| **Data (RAW)** | instruction needs a result not yet written back | **forwarding/bypassing** from EX/MEM outputs to EX inputs; **load-use** still needs a 1-cycle stall (compilers schedule an independent instruction into the slot) |
| **Control** | branch outcome known late | resolve early (ID), **predict** (static: backward-taken; dynamic: 2-bit saturating counters, global/local history, tournament, TAGE), flush on mispredict (penalty ≈ pipeline depth to resolution, 15–20 cycles on modern cores); delayed branches (MIPS, obsolete) |
| WAR/WAW (name dependences) | reuse of register names | register renaming in OoO cores |
**Exceptions** must be precise: the pipeline flushes younger instructions and saves the PC of
the faulting one (SEPC/SCAUSE in RISC-V) so the OS can handle and resume ([[processes-and-threads]]).

## Instruction-level parallelism (COD 4.11, CA:AQA ch. 3)
- **Superscalar**: fetch/issue 2–8 instructions per cycle; static (VLIW/Itanium — compiler
  packs bundles, failed commercially) vs dynamic.
- **Dynamic scheduling (Tomasulo 1967)**: instructions wait in reservation stations for
  operands; results broadcast on a common data bus with tags; **register renaming** (physical
  register file) eliminates WAR/WAW; instructions execute out of order as operands arrive.
- **Speculation**: execute past predicted branches; a **reorder buffer** commits results in
  program order, giving precise exceptions and easy squash. Memory disambiguation, store
  buffers, load speculation.
- **SMT/hyperthreading**: multiple hardware threads share one OoO core's units to fill bubbles.
- Limits: dependences (critical path), branch mispredicts, cache misses (a miss to DRAM ≈ hundreds
  of cycles — the memory wall), power. Hence the shift to multicore and DLP
  ([[parallel-architectures-simd-gpu]]).

## What programmers can do
Reduce unpredictable branches (branchless selects, sorting data to make branches predictable —
the famous "why is sorted array faster" effect); unroll and interleave independent work to expose
ILP; avoid long dependency chains (reductions with multiple accumulators); keep hot loops small;
measure with `perf stat` (IPC, branch-misses) ([[profiling-and-performance]],
[[compiler-optimizations]]).

## Security: Spectre and Meltdown
Speculatively executed instructions are squashed architecturally but leave cache footprints;
an attacker trains the predictor to speculate into a bounds-violating load whose value indexes
a probe array, then times the cache to read the secret. Mitigations: fences (lfence), retpolines,
KPTI, hardware fixes — costing 5–30%. The lesson: the ISA is not the whole contract
([[caches-and-memory-hierarchy]], [[security-principles]]).

## Related
- [[isa-and-assembly]], [[digital-logic-and-the-alu]], [[caches-and-memory-hierarchy]],
  [[performance-equation-and-amdahl]], [[parallel-architectures-simd-gpu]], [[compiler-optimizations]],
  [[profiling-and-performance]].

## Sources
COD ch. 4; CA:AQA ch. 3; Tomasulo 1967; Kocher et al. 2018.

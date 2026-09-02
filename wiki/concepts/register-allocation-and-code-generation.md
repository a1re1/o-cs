---
title: Code generation — instruction selection, instruction scheduling, and register allocation by graph colouring or linear scan
type: concept
section: "4.3"
level: 400
tags: [code-generation, instruction-selection, tree-pattern-matching, instruction-scheduling, list-scheduling, register-allocation, graph-coloring, chaitin, briggs, interference-graph, liveness, spilling, coalescing, linear-scan, live-ranges, calling-convention, prologue-epilogue, peephole, target-description]
sources: [dragon-book-and-compiler-texts, compiler-seminal-papers, cs6120-and-compiler-courses]
summary: The back end maps IR to a target — instruction selection covers the IR tree/DAG with machine instructions (maximal munch, dynamic-programming tree matching, or SelectionDAG/GlobalISel pattern tables), scheduling orders instructions to hide latencies and fill issue slots (list scheduling over a dependence DAG, respecting the pipeline model), and register allocation assigns unbounded virtual registers to the few real ones — Chaitin/Briggs graph colouring builds an interference graph from liveness, simplifies nodes with degree < K, spills when stuck and coalesces copies, while linear scan (and its JIT-friendly variants) sweeps live intervals in order for speed — then prologues/epilogues, calling conventions and stack frames are emitted.
---
# Code generation and register allocation

**In one sentence.** Three NP-hard problems in a row — pick instructions, order them, fit
values into registers — each solved by a good heuristic and mutually entangled.

## Instruction selection (Dragon 8.9, Appel ch. 9)
The IR is a tree/DAG of operations; the target ISA offers instructions that cover several nodes
(x86 `lea`, addressing modes `[base + idx*8 + disp]`, fused multiply-add). **Maximal munch**:
greedily cover with the largest matching pattern top-down; **dynamic programming** (optimal
tiling with costs, BURS/`burg`); LLVM's **SelectionDAG** legalizes and pattern-matches per block
from TableGen descriptions, **GlobalISel** works on the whole function; peephole cleanups after.
RISC targets make selection easy; CISC and vector ISAs make it valuable ([[isa-and-assembly]]).

## Instruction scheduling
Reorder within a block (or across, with trace/superblock scheduling) so dependent instructions
are far apart: build the dependence DAG (true, anti, output dependences through registers and
memory — alias analysis again), then **list scheduling** by priority (critical path height,
resource usage) subject to a machine model (latencies, issue width, ports). Software pipelining
(modulo scheduling) for loops. Modern out-of-order cores reduce the payoff; in-order cores, GPUs
and VLIW depend on it ([[pipelining-and-hazards]]).

## Register allocation
- Inputs: virtual registers with **live ranges** from liveness analysis
  ([[dataflow-analysis]]); two ranges **interfere** if live simultaneously (and not copies of
  the same value).
- **Graph colouring** (Chaitin 1982; Briggs 1994; George–Appel): interference graph; repeatedly
  remove ("simplify") a node with degree < K onto a stack (it can always be coloured); if none,
  choose a spill candidate (cost/degree heuristic) — Briggs *optimistically* pushes it anyway and
  may still colour; pop and assign colours; on actual spill, insert loads/stores around uses,
  rebuild, repeat. **Coalescing** merges copy-related nodes (conservative: Briggs' or George's
  criteria to avoid creating spills); pre-coloured nodes for calling-convention registers
  ([[calling-conventions-and-the-stack]]); callee-saved handling via spilling at entry.
  Quality is high; cost is O(n²) graph construction — used at -O2 in GCC (IRA), LLVM's greedy
  allocator is a priority-based global allocator with live-range splitting.
- **Linear scan** (Poletto–Sarkar; Wimmer's extensions): sort live intervals by start; sweep,
  expiring finished intervals and assigning free registers; spill the interval ending last when
  none free. Near-linear time — JIT compilers (HotSpot C1, V8's early tiers, Cranelift).
- SSA-based allocation: interference graphs of SSA programs are **chordal**, so colouring is
  polynomial and spilling can be decided before assignment (Hack, Bouchez).
- Live-range **splitting** to spill only in cold regions; **rematerialization** (recompute cheap
  values instead of reloading constants/addresses); register pressure feeds back into scheduling
  and unrolling decisions.

## Frame layout and the rest
Prologue/epilogue (save callee-saved registers, adjust SP, frame pointer), stack slots for spills
and locals, alignment, red zone, exception tables/unwind info (DWARF CFI), debug info, relocations
for the linker ([[linking-and-loading]], [[memory-layout-stack-heap]]).

## Pitfalls
- Coalescing aggressively then spilling more than you saved.
- Ignoring that calls clobber caller-saved registers (split ranges around calls).
- Scheduling that raises register pressure and forces spills; the two must be tuned together.
- Assuming the allocator will fix bad IR (huge live ranges from hoisting everything).

## Related
- [[calling-conventions-and-the-stack]], [[dataflow-analysis]], [[intermediate-representations-and-ssa]],
  [[isa-and-assembly]], [[pipelining-and-hazards]], [[np-completeness-and-reductions]] (graph colouring),
  [[linking-and-loading]].

## Sources
Chaitin 1982; Briggs, Cooper & Torczon 1994; Poletto & Sarkar 1999; Dragon Book ch. 8, 10; Appel ch. 9–11; CS143 register allocation lecture.

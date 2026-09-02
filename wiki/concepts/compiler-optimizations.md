---
title: Compiler optimizations — local, global, loop, interprocedural, and what the optimizer can and cannot do
type: concept
section: "4.3"
level: 400
tags: [compiler-optimizations, constant-folding, constant-propagation, dead-code-elimination, common-subexpression-elimination, value-numbering, gvn, copy-propagation, strength-reduction, inlining, loop-invariant-code-motion, induction-variables, loop-unrolling, vectorization, peephole, partial-redundancy-elimination, tail-call, devirtualization, lto, pgo, undefined-behavior, proebstings-law]
sources: [dragon-book-and-compiler-texts, cs6120-and-compiler-courses, compiler-seminal-papers, csapp-15-213]
summary: Optimizations are semantics-preserving rewrites justified by analyses — local (within a block: constant folding, local value numbering, peephole), global (across the CFG via dataflow/SSA: constant propagation, GVN, DCE, copy propagation, partial redundancy elimination), loop (invariant code motion, induction-variable strength reduction, unrolling, fusion/fission, interchange, vectorization), and interprocedural (inlining — the enabler of everything else, devirtualization, LTO, profile-guided) — and the optimizer's blind spots (aliasing, calls to unknown code, floating-point rules, and the licence it takes from undefined behaviour) are what programmers must understand to write fast code without fighting it.
---
# Compiler optimizations

**In one sentence.** The optimizer is a theorem prover with a budget: it rewrites what it can
*prove* equivalent, and the language's semantics (aliasing, UB, FP) decide how much it can prove.

## Local (within a basic block — CS6120 lesson 3)
**Constant folding** (`2*3 → 6`), **algebraic simplification** and strength reduction (`x*8 →
x<<3`, `x/2` for unsigned), **local value numbering** (number each computed value; identical
value numbers → CSE; also catches copy and constant propagation), **dead code elimination**
(unused pure results), **peephole** on the final instructions (redundant moves, branch chains).

## Global (across the CFG — Dragon ch. 9)
**Constant propagation** and **SCCP** (on SSA, also removes unreachable branches),
**global value numbering** (dominator-based or hash-based GVN + PRE), **common subexpression
elimination** via available expressions, **copy propagation**, **dead store / dead code
elimination** via liveness and SSA use counts, **partial redundancy elimination** (Morel–Renvoise;
lazy code motion — subsumes CSE and loop-invariant motion), **jump threading**, **tail-call
elimination**, **switch lowering** (jump tables, binary search), **branch simplification**.
All rest on [[dataflow-analysis]] and [[intermediate-representations-and-ssa]].

## Loops (CS6120 lesson 8)
**Loop-invariant code motion** (hoist computations that dominate all exits and whose operands
are invariant), **induction-variable** recognition and **strength reduction** (`a[i]` addresses
→ pointer increments), **loop unrolling** (fewer branches, more ILP, enables scheduling), **loop
fusion/fission**, **interchange** and **tiling** for locality ([[caches-and-memory-hierarchy]]),
**vectorization** (auto-SIMD when trips are independent and aliasing is disproven —
[[parallel-architectures-simd-gpu]]), **software pipelining**, loop unswitching, idiom
recognition (memset/memcpy), polyhedral transformations (affine loops, Dragon ch. 11).

## Interprocedural
**Inlining** — the most important optimization: removes call overhead and exposes callee code
to every other pass; heuristics by size/hotness; **devirtualization** (class hierarchy analysis,
speculative with guards), **interprocedural constant propagation**, **escape analysis**
(stack-allocate objects; remove locks), **link-time optimization** (whole-program view),
**profile-guided optimization** (layout, inlining, branch weights from real runs — 10–30%),
BOLT/Propeller post-link layout.

## Backend-adjacent
Instruction selection and scheduling, register allocation, and machine-specific peepholes
([[register-allocation-and-code-generation]]); target features (`-march=native`).

## What the optimizer cannot do (and what UB lets it do)
- **Aliasing**: `void f(int *a, int *b)` — writes through `a` may change `*b`, blocking reordering
  and vectorization; `restrict`, type-based alias analysis (strict aliasing), Rust's `&mut`
  guarantee help ([[pointers-and-memory]]).
- **Opaque calls**: any call may modify globals/memory unless the callee is known/pure
  (`__attribute__((pure))`, LTO).
- **Floating point**: no reassociation without `-ffast-math` (changes results —
  [[floating-point]]).
- **Undefined behaviour** is treated as impossible: signed-overflow checks and null checks get
  deleted, loops assumed finite ([[undefined-behavior]]). Sanitizers instead of relying on
  luck.
- Algorithmic complexity is untouched — compilers do not change data structures
  ([[profiling-and-performance]]). Proebsting's law: optimization doubles performance every ~18
  years.

## Working with the optimizer (CSAPP ch. 5)
Hoist loop-invariant loads to locals yourself when aliasing blocks it; avoid function calls in
loop conditions (`strlen`); use local accumulators (multiple to break dependence chains); prefer
arrays of primitives; check with `-O2 -Rpass=…`, Compiler Explorer, `perf annotate`.

## Related
- [[dataflow-analysis]], [[intermediate-representations-and-ssa]], [[register-allocation-and-code-generation]],
  [[undefined-behavior]], [[caches-and-memory-hierarchy]], [[profiling-and-performance]],
  [[bytecode-vms-and-jit]] (speculative optimization at run time).

## Sources
Dragon Book ch. 8–11; Cooper & Torczon ch. 8–10; CS6120 lessons 3–9; CSAPP ch. 5; LLVM passes documentation.

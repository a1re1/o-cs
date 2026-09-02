---
title: Dataflow analysis — lattices, transfer functions, the worklist algorithm, and the classic analyses
type: concept
section: "4.3"
level: 400
tags: [dataflow-analysis, lattice, transfer-function, meet, join, fixed-point, worklist-algorithm, reaching-definitions, live-variables, available-expressions, constant-propagation, sccp, forward-analysis, backward-analysis, may-must, monotone-framework, kildall, abstract-interpretation, alias-analysis, interprocedural]
sources: [dragon-book-and-compiler-texts, cs6120-and-compiler-courses, compiler-seminal-papers]
summary: A dataflow analysis assigns each program point a value from a lattice (sets of definitions, expressions, constants, …), propagates values through blocks with monotone transfer functions and merges at joins with meet/join, and iterates a worklist to the least fixed point — forward analyses (reaching definitions, available expressions, constant propagation) push facts along control flow, backward analyses (live variables, very busy expressions) pull them; may vs must analyses choose union vs intersection; the framework generalizes to SSA-sparse SCCP, alias and interprocedural analysis, and is a special case of abstract interpretation, always sound and necessarily approximate.
---
# Dataflow analysis

**In one sentence.** Pick a domain of facts, say how each instruction changes them and how
branches combine them, then iterate until nothing changes — the same recipe yields liveness,
constants, available expressions, and the analyses behind every optimizer.

## The framework (Kildall 1973; Dragon 9.2–9.3; CS6120 lesson 4)
A dataflow problem = (direction, domain D with a partial order and meet ⊓, transfer functions
f_B : D → D per block, initial value at entry/exit, boundary value). Equations for forward
analysis: `in[B] = ⊓ out[P] over predecessors P`, `out[B] = f_B(in[B])`. Solve by the
**worklist algorithm**: initialize all to ⊤ (or ⊥), push all blocks, pop, recompute, push
successors if the output changed. Terminates when D has finite height and f is **monotone**;
gives the **maximal fixed point** (MFP), which equals the meet-over-all-paths (MOP) solution
when transfer functions **distribute** over ⊓ (the "gen/kill" bit-vector problems do; constant
propagation doesn't, so MFP is a safe over-approximation). Complexity O(blocks × height) with
reverse-postorder visiting; bit-vector implementations for set problems.

## The classic four
| Analysis | Direction | Domain / meet | Transfer | Use |
|---|---|---|---|---|
| **Reaching definitions** | forward | sets of defs, ∪ (may) | gen defs, kill same-variable defs | def-use chains, loop-invariant detection |
| **Live variables** | backward | sets of vars, ∪ (may) | use ∪ (in − def) | dead-store elimination, register allocation interference |
| **Available expressions** | forward | sets of exprs, ∩ (must) | gen computed exprs, kill on redefinition | global CSE |
| **Very busy / anticipated expressions** | backward | ∩ (must) | | code hoisting, partial redundancy elimination |
Others: **constant propagation** (lattice ⊤ > constants > ⊥ per variable; non-distributive),
**sparse conditional constant propagation** (SCCP, Wegman–Zadeck: on SSA, propagate constants
and executability of edges together — proves branches dead), copy propagation, sign/range/
nullness analysis, definite assignment (Java), escape analysis, taint tracking.

## Precision and cost
- **May vs must**: union over paths says "possibly" (needed for safety when a fact enables
  removal of a check); intersection says "definitely" (needed when a fact enables reuse).
- **Flow-sensitive** (per program point) vs **flow-insensitive** (one fact per variable — cheap,
  used for alias analysis at scale); **context-sensitive** interprocedural analysis (call strings,
  summaries, k-CFA) vs a call-graph-wide merge; **path-sensitive** (symbolic execution, SMT) for
  bug finding. **Alias analysis** (Andersen's inclusion-based O(n³), Steensgaard's
  unification-based near-linear) decides whether two pointers may refer to the same memory — the
  gate for most memory optimizations ([[pointers-and-memory]]).
- **Abstract interpretation** (Cousot & Cousot) is the general theory: an abstract domain
  (intervals, octagons, polyhedra) with Galois connections to concrete semantics; widening for
  infinite-height lattices; tools like Astrée prove absence of runtime errors
  ([[program-verification]]).

## Pitfalls
- Wrong initialization (⊤ vs ⊥) or boundary conditions yields unsound results.
- Non-monotone transfer functions loop forever; missing widening on infinite domains.
- Ignoring exceptions/indirect calls/signals in the CFG (hidden edges).
- Sound but useless: over-approximation that kills every optimization — invest in alias
  precision where it matters.

## Related
- [[intermediate-representations-and-ssa]], [[compiler-optimizations]], [[register-allocation-and-code-generation]]
  (liveness), [[graph-search]], [[induction]] (fixed-point arguments), [[program-verification]],
  [[type-systems]] (type inference as a fixed point).

## Sources
Dragon Book ch. 9; CS6120 lessons 3–5, 9–10; Kildall 1973; Allen & Cocke 1976; Wegman & Zadeck 1991.

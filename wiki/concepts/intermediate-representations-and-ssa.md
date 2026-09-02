---
title: Intermediate representations — three-address code, control flow graphs, SSA form, dominators, and LLVM IR
type: concept
section: "4.3"
level: 400
tags: [intermediate-representation, ir, three-address-code, basic-blocks, control-flow-graph, ssa, phi-nodes, dominators, dominator-tree, dominance-frontier, renaming, out-of-ssa, llvm-ir, mlir, cps, sea-of-nodes, bril, def-use-chains]
sources: [dragon-book-and-compiler-texts, cs6120-and-compiler-courses, compiler-seminal-papers]
summary: The middle end works on a linear three-address IR grouped into basic blocks connected in a control flow graph; static single assignment gives every variable exactly one definition, inserting φ-functions where control paths merge (placed minimally at dominance frontiers by Cytron et al.'s algorithm, then renamed along the dominator tree), which makes def-use chains explicit and turns global optimizations (constant propagation, value numbering, DCE, GVN) into simple sparse passes; LLVM IR is the industrial typed-SSA IR, and dominators, loops and reducibility are the graph facts every pass relies on.
---
# Intermediate representations and SSA

**In one sentence.** Choose a representation in which the facts an optimization needs are
explicit — SSA makes "where was this value defined" a pointer, not an analysis.

## Linear IRs and the CFG (Dragon ch. 6, 8.4; CS6120 lesson 2)
**Three-address code**: `t1 = a + b; t2 = t1 * c; if t2 < 0 goto L1` — one operation per
instruction, unlimited temporaries. Instructions group into **basic blocks** (single entry at
the top, single exit at the bottom — a label starts one, a jump ends one); blocks and their
jumps form the **control flow graph**. Other shapes: stack-based bytecode (JVM, CPython — compact,
easy to generate), register-based bytecode (Lua, Dalvik), tree IRs (GCC GIMPLE trees, Appel's
IR trees), sea of nodes (HotSpot C2, V8 TurboFan — control and data as one graph), CPS
(continuation-passing style — functional compilers; equivalent to SSA), MLIR's dialect stack
for domain-specific lowering. Bril is CS6120's minimal JSON IR.

## Dominators and loops (CS6120 lesson 5)
Block A **dominates** B if every path from entry to B goes through A; the **dominator tree**
(immediate dominators) is computed by iterative dataflow or Lengauer–Tarjan; A **strictly**
dominates B if A ≠ B. The **dominance frontier** DF(A) = blocks B where A dominates a predecessor
of B but not B itself — the places where A's influence ends. **Natural loops**: a back edge
n → h with h dominating n; the loop is all nodes that reach n without passing h; reducible CFGs
(structured code) have only natural loops. Post-dominators give control dependence.

## SSA form (Cytron et al. 1991; SSA Book ch. 1–3)
Every variable is assigned exactly once; at join points a **φ-function** `x3 = φ(x1, x2)` picks
the value from the incoming edge. Construction: (1) insert φ for variable v at every block in
the iterated dominance frontier DF⁺ of v's definition blocks (minimal SSA; pruned SSA skips
dead φs); (2) rename by a DFS over the dominator tree with a stack of versions per variable,
filling φ operands at successors. **Out of SSA**: replace φs with copies on predecessor edges
(splitting critical edges; the "lost copy" and "swap" problems; Sreedhar's method). Properties:
def-use chains are trivial (one def), so **sparse** analyses (SCCP, GVN, DCE) touch only the
uses of changed values; variables are immutable — the compiler's own [[purity-and-referential-transparency]].
Memory is not in SSA (loads/stores stay; alias analysis needed; `mem2reg` promotes stack slots
to SSA registers in LLVM).

## LLVM IR (Lattner & Adve 2004)
Typed (`i32`, `ptr`, structs, vectors), SSA with explicit φ, unlimited virtual registers,
explicit control flow, `getelementptr` for address arithmetic, metadata (debug, TBAA, profile),
undefined values/poison to model UB ([[undefined-behavior]]). Text/bitcode forms; the same IR
serves compile-time, link-time (LTO) and run-time (JIT) optimization — "lifelong". Pass
manager: analysis passes (dominators, loops, alias) cached for transformation passes.

## Pitfalls
- Building optimizations on a non-SSA IR and rediscovering def-use chains per pass.
- Forgetting critical-edge splitting when leaving SSA (wrong copies).
- Treating φ as a runtime operation (it is a notational device for merge points).
- Irreducible CFGs (goto, computed jumps) break loop-based passes; node splitting or bailout.

## Related
- [[dataflow-analysis]], [[compiler-optimizations]], [[register-allocation-and-code-generation]],
  [[graph-search]] (dominators are a DFS/dataflow computation), [[compilers-overview]],
  [[purity-and-referential-transparency]].

## Sources
Cytron et al. 1991; SSA Book ch. 1–3; Dragon Book ch. 6, 8–9; CS6120 lessons 2, 5, 6, 7; LLVM Language Reference.

---
title: Cornell CS6120 Advanced Compilers (Sampson) with Stanford CS143, MIT 6.035, Berkeley CS164
type: source
section: "4.3"
level: 400
tags: [cs6120, bril, llvm, dataflow, ssa, loop-optimization, interprocedural, alias-analysis, memory-management, dynamic-compilers, program-synthesis, cs143, cool, parsing, semantic-analysis, code-generation]
sources: []
institution: Cornell / Stanford / MIT / Berkeley
year: 2023
url: https://www.cs.cornell.edu/courses/cs6120/2023fa/self-guided/
license: open-course
format: html
summary: CS6120 is a free self-guided PhD-level course with videos, notes, implementation tasks on the Bril IR, and paper discussions — representing programs (IR, CFGs), local analysis and optimization (DCE, LVN), data flow (the generic worklist framework), global analysis (dominators, natural loops), SSA (construction/destruction), LLVM (writing a pass), loop optimization (LICM), interprocedural analysis, alias analysis, memory management (GC), dynamic compilers (JITs, tracing), program synthesis, concurrency and parallelism; CS143 (free on edX/SEE) builds a full Cool compiler (lexer with flex, parser with bison, semantic analysis, code generation to MIPS) and covers LR parsing theory, runtime organization, optimization and register allocation.
---
# CS6120 Advanced Compilers and undergraduate compiler courses

## What it is
**CS6120 lessons**: 1 welcome and overview (why compilers; the semester's arc); 2 representing
programs (Bril — a JSON-based teaching IR; basic blocks; control flow graphs); 3 local analysis
and optimization (dead code elimination, **local value numbering** — CSE, copy/constant
propagation in one framework); 4 **data flow** (reaching definitions; the general framework —
direction, domain, transfer, merge; the worklist algorithm; live variables, constant propagation);
5 global analysis (**dominators**, dominator trees and frontiers; natural loops, reducibility); 6
**static single assignment** (φ-nodes, construction via dominance frontiers, out-of-SSA); 7 LLVM
(writing a pass; the IR and infrastructure); 8 loop optimization (loop-invariant code motion,
induction variables, strength reduction); 9 interprocedural analysis (call graphs, context
sensitivity, inlining); 10 alias analysis (may/must, Andersen vs Steensgaard, flow sensitivity);
11 memory management (garbage collection, reference counting, Bacon et al.'s unified theory); 12
dynamic compilers (JIT, speculation, tracing — Deutsch & Schiffman, Hölzle's inline caches); 13
program synthesis (sketching, CEGIS); 14 concurrency and parallelism (memory models, auto-
parallelization). Papers interleaved: Cytron et al. SSA, Lattner & Adve LLVM, Chaitin,
"Superoptimizer", etc.
**CS143** (Stanford): lexical analysis and finite automata, parsing (recursive descent, LL(1),
bottom-up, LR/SLR/LALR), semantic analysis (scope, types, type checking for Cool, self types),
runtime organization (activation records, objects, dispatch tables), code generation (stack
machine to MIPS), operational semantics, local/global optimization, register allocation, GC.
**6.035**, **CS164**, **CSE401** follow the same arc with a decaf/Chocopy-style project.

## What it adds
The lesson sequence is the modern middle-end curriculum for [[dataflow-analysis]],
[[intermediate-representations-and-ssa]], [[compiler-optimizations]], [[bytecode-vms-and-jit]],
[[garbage-collection]]; CS143 anchors [[lexing-and-parsing]] and
[[register-allocation-and-code-generation]].

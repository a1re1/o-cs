---
title: Compiler seminal papers — Cytron et al. SSA (1991), Chaitin register allocation (1982), Lattner & Adve LLVM (2004), Deutsch & Schiffman Smalltalk-80 JIT (1984), Hölzle inline caching (1991), Allen & Cocke dataflow, Knuth LR parsing (1965), Cheney copying GC (1970), Bacon et al. GC unified theory (2004), Proebsting's law
type: source
section: "4.3"
level: 500
tags: [ssa, cytron, dominance-frontiers, chaitin, graph-coloring, register-allocation, llvm, lattner, jit, deutsch-schiffman, inline-caching, holzle, self, dataflow, allen-cocke, knuth-lr, lr-parsing, cheney, copying-gc, bacon-gc, proebstings-law, history]
sources: []
authors: [Ron Cytron, Jeanne Ferrante, Barry Rosen, Mark Wegman, Kenneth Zadeck, Gregory Chaitin, Chris Lattner, Vikram Adve, Peter Deutsch, Alan Schiffman, Urs Hölzle, Frances Allen, John Cocke, Donald Knuth, C. J. Cheney, David Bacon, Perry Cheng, V. T. Rajan, Todd Proebsting]
year: 1991
institution: various
url: https://dl.acm.org/doi/10.1145/115372.115320
license: various
format: pdf
summary: The papers that fixed the vocabulary — Knuth invented LR(k) parsing and showed deterministic bottom-up parsing of most programming-language grammars; Allen & Cocke systematized dataflow analysis on control-flow graphs; Chaitin cast register allocation as graph colouring with spilling; Cytron et al. gave the efficient SSA construction via dominance frontiers that every optimizer uses; Cheney's two-finger algorithm made copying GC iterative in constant space; Deutsch & Schiffman's Smalltalk-80 implementation introduced dynamic translation to native code with caching (the first practical JIT) and Hölzle's Self work added polymorphic inline caches and type feedback; Lattner & Adve's LLVM defined a typed SSA IR usable across the whole program lifetime; Bacon, Cheng & Rajan showed tracing and reference counting are duals; Proebsting's law observes compiler optimizations double performance only every 18 years.
---
# Compiler seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Knuth, "On the Translation of Languages from Left to Right" (1965) | LR(k) grammars and parsers; deterministic bottom-up parsing; the basis of yacc/bison's LALR | [[lexing-and-parsing]] |
| Allen & Cocke, "A Program Data Flow Analysis Procedure" (1976); Kildall (1973) | Dataflow analysis over CFGs with lattices and iteration to a fixed point; intervals and reducibility | [[dataflow-analysis]] |
| Chaitin et al., "Register Allocation via Coloring" (1981/82) | Build an interference graph from liveness; colour with K registers; spill and rebuild; coalescing; Briggs' optimistic colouring and George–Appel iterated coalescing refine it | [[register-allocation-and-code-generation]] |
| Cytron, Ferrante, Rosen, Wegman, Zadeck, "Efficiently Computing Static Single Assignment Form and the Control Dependence Graph" (1991) | Dominance frontiers give minimal φ-placement in near-linear time; renaming by DFS over the dominator tree; SSA makes def-use chains explicit and sparse optimizations simple | [[intermediate-representations-and-ssa]] |
| Cheney, "A Nonrecursive List Compacting Algorithm" (1970) | Breadth-first copying collection with a scan pointer and a free pointer — no recursion stack; the basis of semispace and generational nursery collectors | [[garbage-collection]] |
| Bacon, Cheng & Rajan, "A Unified Theory of Garbage Collection" (2004) | Tracing computes liveness from roots, reference counting computes deadness from decrements; every real collector is a hybrid; the design space is a matrix | [[garbage-collection]] |
| Deutsch & Schiffman, "Efficient Implementation of the Smalltalk-80 System" (1984) | Dynamic translation of bytecode to native code cached per method, inline caching of sends, volatile contexts — the first JIT in production | [[bytecode-vms-and-jit]] |
| Hölzle, Chambers & Ungar, "Optimizing Dynamically-Typed Object-Oriented Languages with Polymorphic Inline Caches" (1991) | PICs record receiver types at call sites; type feedback drives speculative inlining; deoptimization keeps semantics — V8, HotSpot, LuaJIT descend from Self | [[bytecode-vms-and-jit]] |
| Lattner & Adve, "LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation" (2004) | A typed, SSA-based, target-independent IR with explicit control flow; passes at compile, link, install and run time; the infrastructure behind clang, Rust, Swift, Julia | [[intermediate-representations-and-ssa]], [[compiler-optimizations]] |
| Proebsting's law (1998) | Compiler advances double program performance every ~18 years vs Moore's 2 — a sobering estimate of optimization's marginal value | [[compiler-optimizations]] |

## Why read them
Each is the primary statement of an idea that textbooks compress: dominance frontiers, PICs and
deoptimization in particular are best understood from the source.

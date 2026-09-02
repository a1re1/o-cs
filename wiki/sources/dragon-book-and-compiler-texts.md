---
title: Compilers: Principles, Techniques, and Tools (Dragon Book), Engineering a Compiler (Cooper & Torczon), Modern Compiler Implementation (Appel), and the SSA Book
type: source
section: "4.3"
level: 400
tags: [dragon-book, compilers, lexical-analysis, syntax-analysis, lr-parsing, lalr, syntax-directed-translation, type-checking, intermediate-code, runtime-environments, code-generation, dataflow-analysis, optimization, register-allocation, instruction-scheduling, ssa, dominance-frontiers, appel, cooper-torczon]
sources: []
authors: [Alfred Aho, Monica Lam, Ravi Sethi, Jeffrey Ullman, Keith Cooper, Linda Torczon, Andrew Appel]
year: 2006
institution: Stanford / Rice / Princeton
url: https://suif.stanford.edu/dragonbook/
license: proprietary (SSA book free)
format: book
summary: The Dragon Book (2nd ed.) is the reference — lexical analysis (regexes to DFAs), syntax analysis (grammars, top-down LL(1), bottom-up LR(0)/SLR/LALR/LR(1), yacc), syntax-directed translation, intermediate code (three-address code, control flow, backpatching), runtime environments (stack frames, heap, GC), code generation (instruction selection, register allocation), machine-independent optimizations (dataflow analysis frameworks, constant propagation, partial redundancy elimination, loops, region analysis), instruction-level parallelism, parallelism/locality (polyhedral), interprocedural analysis; Cooper & Torczon is the practical modern text (scanning, parsing, context-sensitive analysis, IRs, procedure abstraction, code shape, instruction selection/scheduling/allocation, SSA-based optimization); Appel's "Tiger" books build a complete compiler with the theory attached; the free SSA Book (Rastello et al.) covers SSA construction (dominance frontiers, φ placement, renaming), properties, destruction, and SSA-based analyses and allocation.
---
# The Dragon Book and friends

## What it is
**Dragon Book**: 1 introduction (structure of a compiler, the science of building one); 2 a
simple syntax-directed translator; 3 **lexical analysis** (tokens, regular expressions, lex, NFA →
DFA, minimization); 4 **syntax analysis** (context-free grammars, ambiguity, top-down — FIRST/
FOLLOW, LL(1), recursive descent; bottom-up — shift-reduce, LR(0) items, SLR, canonical LR(1),
LALR, yacc; error recovery); 5 syntax-directed translation (attribute grammars, S- and L-
attributed); 6 intermediate-code generation (DAGs, three-address code, types and declarations,
expressions, control flow with backpatching); 7 **run-time environments** (stack allocation,
access links, heap management, GC — reference counting, mark-sweep, copying, generational); 8
**code generation** (target machine, basic blocks and flow graphs, simple generator, peephole,
register allocation by graph colouring, tree-based instruction selection via dynamic
programming); 9 **machine-independent optimizations** (dataflow analysis — reaching definitions,
live variables, available expressions; foundations — lattices, monotone frameworks; constant
propagation, partial-redundancy elimination, loops and dominators, region-based analysis,
symbolic analysis); 10 ILP (scheduling, software pipelining); 11 parallelism and locality
(affine transforms); 12 interprocedural analysis (pointer analysis, Datalog).
**Cooper & Torczon**: adds the IR taxonomy, procedure abstraction, code shape, and a modern
back end with SSA-based optimization and Chaitin–Briggs allocation. **Appel**: a project-driven
compiler for Tiger (lexing, parsing, semantic analysis, activation records, IR trees, canonical
trees, instruction selection, liveness, register allocation) plus advanced topics (GC, OOP, FP,
polymorphism, dataflow, loops, SSA, pipelining, cache-aware). **SSA Book**: definition and
informal semantics, properties (strictness, minimality, pruned, conventional), construction via
dominance frontiers, destruction, advanced construction, and SSA-based optimizations.

## Key ideas → pages
[[lexing-and-parsing]], [[intermediate-representations-and-ssa]], [[dataflow-analysis]],
[[compiler-optimizations]], [[register-allocation-and-code-generation]], [[garbage-collection]].

## What it adds
Proof-level depth and the classic algorithms; [[crafting-interpreters]] is the hands-on
counterpart, [[cs6120-and-compiler-courses]] the modern research-oriented course.

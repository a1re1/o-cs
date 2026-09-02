---
title: Crafting Interpreters (Nystrom) with Writing an Interpreter/Compiler in Go (Ball)
type: source
section: "4.3"
level: 300
tags: [crafting-interpreters, lox, scanning, parsing, recursive-descent, tree-walking-interpreter, resolver, closures, classes, bytecode, virtual-machine, stack-vm, compiler, garbage-collection, mark-sweep, hash-tables, jlox, clox, go-interpreter]
sources: []
authors: [Robert Nystrom, Thorsten Ball]
year: 2021
institution: independent
url: https://craftinginterpreters.com/
license: CC-BY-NC-ND (free online)
format: html
summary: Two complete implementations of the Lox language — jlox, a tree-walking interpreter in Java (scanner, recursive-descent parser with precedence climbing, AST via the Visitor pattern, evaluation, statements and state, control flow, functions and closures with environments, a resolver pass for static scoping, classes and inheritance) and clox, a bytecode VM in C (chunks, a stack VM, single-pass Pratt-parser compiler emitting bytecode, string interning and hash tables, globals/locals, jumps, calls and frames, closures with upvalues, mark–sweep garbage collection, classes, method dispatch with inline caching flavour, optimization) — preceded by "A Map of the Territory"; Ball's Go books do the same for the Monkey language.
---
# Crafting Interpreters

## What it is
Part I: 1 introduction; 2 **a map of the territory** — the mountain: scanning → parsing → static
analysis (binding/resolution, type checking; results stored as AST attributes, symbol tables, or
a new IR) → intermediate representations (CFG, SSA, CPS, three-address code) → optimization →
code generation (native vs bytecode) → virtual machine → runtime (GC, type info); shortcuts and
alternate routes: single-pass compilers, tree-walking interpreters, transpilers, JIT; compilers
vs interpreters; 3 the Lox language. Part II **jlox**: 4 scanning (tokens, lexemes, regular
languages, maximal munch), 5 representing code (context-free grammars, the AST, the Visitor
pattern/expression problem), 6 parsing expressions (ambiguity, precedence and associativity,
recursive descent, error recovery via panic mode and synchronization), 7 evaluating, 8 statements
and state (environments, scope), 9 control flow, 10 functions (calls, native functions, closures
capturing environments, return via exceptions), 11 resolving and binding (a static pass that
resolves each variable to a fixed environment depth — fixing the closure-in-loop semantics), 12
classes, 13 inheritance. Part III **clox**: 14 chunks of bytecode, 15 a virtual machine (the
value stack, dispatch loop), 16 scanning on demand, 17 compiling expressions (**Pratt parsing**),
18 types of values, 19 strings (heap objects), 20 hash tables (open addressing, FNV-1a, string
interning), 21 global variables, 22 local variables (compile-time stack slots), 23 jumping back
and forth (backpatching), 24 calls and functions (call frames), 25 closures (upvalues, open/
closed), 26 **garbage collection** (mark–sweep, roots, tricolor, GC pacing), 27 classes and
instances, 28 methods and initializers, 29 superclasses, 30 optimization (NaN boxing, fast
hashing). Ball's *Writing an Interpreter in Go* / *Compiler in Go*: Monkey lexer, Pratt parser,
evaluator, then a bytecode compiler and VM with closures.

## Key ideas → pages
[[compilers-overview]], [[lexing-and-parsing]], [[interpreters-eval-apply]],
[[closures-and-environment-model]], [[bytecode-vms-and-jit]], [[garbage-collection]],
[[hash-tables]].

## What it adds
The end-to-end build that the Dragon Book ([[dragon-book-and-compiler-texts]]) and CS6120
([[cs6120-and-compiler-courses]]) assume; clox's bytecode VM is the shape of CPython, Lua and the
JVM interpreter.

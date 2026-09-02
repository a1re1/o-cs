---
title: Compiler and interpreter architecture — the pipeline from source to machine code
type: concept
section: "4.3"
level: 300
tags: [compilers, interpreters, compiler-pipeline, front-end, middle-end, back-end, scanning, parsing, semantic-analysis, symbol-table, ir, optimization, code-generation, bytecode, virtual-machine, transpiler, jit, aot, runtime, toolchain]
sources: [crafting-interpreters, dragon-book-and-compiler-texts, cs6120-and-compiler-courses, nand2tetris]
summary: Every language implementation climbs the same mountain — scanning characters into tokens, parsing tokens into a syntax tree, static analysis (name resolution, scoping, type checking) recorded in AST attributes or symbol tables, lowering to an intermediate representation, machine-independent optimization, then descending through code generation (native, bytecode for a VM, or another source language) to a runtime with garbage collection and dynamic support — and the differences between compilers, interpreters, JITs and transpilers are choices of where to stop and when to run each phase.
---
# Compilers and interpreters: the pipeline

**In one sentence.** Front end understands the source, middle end improves an IR, back end
speaks to the machine; interpreters and JITs are compilers that run some of the phases late.

## The mountain (Crafting Interpreters ch. 2)
1. **Scanning / lexing**: characters → tokens (identifiers, literals, operators); regular
   languages; drops whitespace/comments ([[lexing-and-parsing]], [[finite-automata-and-regular-languages]]).
2. **Parsing**: tokens → parse tree / **AST** per a context-free grammar; reports syntax errors
   with recovery ([[lexing-and-parsing]], [[context-free-grammars]]).
3. **Static analysis**: **binding/resolution** of names to declarations (scope), **type
   checking** for static languages, definite assignment, escape analysis. Results live as AST
   attributes, in a **symbol table**, or in a new IR ([[type-systems]],
   [[closures-and-environment-model]]).
   — summit: the compiler knows what the program *means*.
4. **Intermediate representation**: source- and target-independent — three-address code, control
   flow graphs, **SSA**, CPS; the interface that lets m front ends share n back ends (GCC GIMPLE/
   RTL, LLVM IR, MLIR) ([[intermediate-representations-and-ssa]]).
5. **Optimization**: semantics-preserving rewrites — constant folding, CSE, DCE, inlining, loop
   transformations, vectorization ([[compiler-optimizations]], [[dataflow-analysis]]).
6. **Code generation**: instruction selection, scheduling, **register allocation**, emitting
   assembly/object code ([[register-allocation-and-code-generation]]) — or **bytecode** for a
   virtual machine.
7. **Virtual machine / runtime**: bytecode interpreter or JIT; the runtime provides GC, exceptions,
   type info, dynamic dispatch, reflection ([[bytecode-vms-and-jit]], [[garbage-collection]]).

## Routes and shortcuts
- **Single-pass compilers** (Pascal, C's design constraints; clox) emit code during parsing —
  no IR, limited optimization.
- **Tree-walking interpreters** (jlox, early Ruby) evaluate the AST directly — simple, slow.
- **Bytecode + VM** (CPython, Lua, JVM interpreter, clox) — portable, decent speed.
- **JIT** (V8, HotSpot, PyPy, LuaJIT) — compile hot code at runtime with profile information.
- **Transpilers** (TypeScript → JS, Nim → C) — another language as the back end.
- **AOT with a shared IR** (clang/rustc/swiftc → LLVM → x86/ARM/wasm).
"Compiler" vs "interpreter": compiling translates to another form without running; interpreting
runs it — most implementations do both (CPython compiles to bytecode, then interprets).

## The toolchain around it
Preprocessor, assembler, linker, loader ([[linking-and-loading]], [[isa-and-assembly]]); build
systems drive them ([[build-systems-and-make]]); debuggers need debug info (DWARF) mapping
machine code back to source; sanitizers instrument during compilation ([[undefined-behavior]]).
Nand2Tetris compresses the whole stack into Jack → VM → assembly → Hack.

## Design tensions
Compile time vs run-time performance; language semantics that enable optimization (no aliasing
in Fortran/Rust; UB in C) vs safety; separate compilation vs whole-program optimization (LTO);
error messages and IDE support (incremental, error-tolerant front ends — rust-analyzer, Roslyn).

## Related
- [[lexing-and-parsing]], [[intermediate-representations-and-ssa]], [[dataflow-analysis]],
  [[compiler-optimizations]], [[register-allocation-and-code-generation]], [[bytecode-vms-and-jit]],
  [[garbage-collection]], [[interpreters-eval-apply]], [[linking-and-loading]].

## Sources
Crafting Interpreters ch. 2; Dragon Book ch. 1; CS6120 lesson 1; Nand2Tetris part II.

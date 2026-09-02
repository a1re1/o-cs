---
title: Bytecode virtual machines and JIT compilation — stack vs register VMs, dispatch, inline caches, tiering, speculation and deoptimization
type: concept
section: "4.3"
level: 400
tags: [bytecode, virtual-machine, stack-machine, register-machine, dispatch-loop, threaded-code, superinstructions, jit, tiered-compilation, baseline-jit, optimizing-jit, inline-caching, polymorphic-inline-cache, type-feedback, speculation, deoptimization, on-stack-replacement, tracing-jit, hidden-classes, shapes, v8, hotspot, pypy, luajit, nan-boxing, wasm]
sources: [crafting-interpreters, compiler-seminal-papers, cs6120-and-compiler-courses]
summary: A bytecode VM interprets a compact instruction set for an abstract machine (stack-based like the JVM/CPython/clox or register-based like Lua/Dalvik) with a dispatch loop whose branch cost is cut by threaded code and superinstructions; a JIT compiles hot code at run time using information only available then — inline caches record receiver types at call sites (Deutsch–Schiffman, Hölzle's PICs), type feedback drives speculative inlining and unboxing, guards protect assumptions, and deoptimization falls back to the interpreter when they fail — organized in tiers (interpreter → baseline → optimizing) with on-stack replacement for long loops; tracing JITs (LuaJIT, PyPy) record hot paths instead of methods.
---
# Bytecode VMs and JIT compilation

**In one sentence.** Compile once to a portable, compact bytecode, interpret it cheaply, and let
runtime profiles tell an optimizing compiler which assumptions are worth betting on.

## Bytecode and the interpreter (clox ch. 14–15, 22–25)
- **Stack VM**: instructions push/pop an operand stack (`OP_CONSTANT 3; OP_ADD`); compact, easy
  to compile to (postfix), locals in stack slots addressed by index (resolved at compile time);
  JVM, CPython, WebAssembly, clox. **Register VM**: three-operand instructions on virtual
  registers (Lua 5, Dalvik); fewer instructions and dispatches, larger encoding.
- **Dispatch**: `switch` in a loop → indirect-branch mispredictions; **direct threading**
  (computed goto per instruction) and **superinstructions** (fused common sequences) help;
  quickening rewrites bytecodes with cached info (CPython 3.11's specializing interpreter).
- Values: tagged unions or **NaN boxing** (pack pointers/ints into doubles — clox ch. 30);
  strings interned; objects with **shapes/hidden classes** so property access can be cached by
  offset (V8, JSC) instead of hash lookup ([[hash-tables]]).
- Calls: frames on the value stack with a return address/IP; **closures** as objects capturing
  **upvalues** (open while the variable is on the stack, closed on scope exit);
  ([[closures-and-environment-model]]); exceptions via handler tables; the GC integrates with
  the stack as roots ([[garbage-collection]]).

## JIT compilation
- **Why**: interpreters cost 10–100× native; static compilation of dynamic languages is stuck
  because types, shapes and call targets are unknown until run time. The JIT observes then
  specializes.
- **Inline caching** (Deutsch & Schiffman 1984): at a send site, cache the receiver class and
  the resolved method; a **polymorphic inline cache** (Hölzle 1991) holds a few (class, target)
  pairs; megamorphic sites fall back to a hash. The caches double as **type feedback**.
- **Speculative optimization**: assume the observed types/shapes (monomorphic call → inline it;
  small ints → unboxed arithmetic; property at offset 3), insert **guards**; on guard failure
  **deoptimize**: reconstruct interpreter frames from the optimized state (deopt metadata) and
  continue in the baseline tier. Invalidation when class hierarchies change (dependency
  tracking).
- **Tiering**: interpreter (profiles) → baseline JIT (template/copy-and-patch, fast to generate)
  → optimizing JIT (SSA, inlining, escape analysis, GVN, register allocation — the full
  [[compiler-optimizations]] pipeline under a time budget) — HotSpot C1/C2, V8 Ignition/Sparkplug/
  Maglev/TurboFan, .NET tiered compilation. **On-stack replacement** enters optimized code in
  the middle of a hot loop.
- **Tracing JITs** (TraceMonkey, LuaJIT, PyPy's meta-tracing of the interpreter): record the
  instructions executed along a hot loop path into a linear trace, optimize it heavily, guard the
  side exits; excellent for tight loops, weaker for branchy code.
- Costs: warm-up time, memory for multiple code versions, code cache management, security (JIT
  spraying, W^X), and complexity; AOT (GraalVM native image, Swift, Go) and interpreters with
  specialization are the alternatives for startup-sensitive contexts. WebAssembly is the modern
  portable bytecode with streaming tiered compilation.

## Design lessons (Self → V8)
Dynamic languages became fast not by better static analysis but by feedback: measure, guess,
guard, recover. The same pattern appears in branch predictors ([[pipelining-and-hazards]]),
adaptive query optimizers ([[query-optimization]]) and PGO.

## Pitfalls
- Polymorphic call sites in hot loops (megamorphic → slow path); shape churn from adding
  properties in different orders.
- Benchmarks that never warm up or that measure the interpreter tier.
- Deopt storms (guards flapping) — check with `--trace-deopt`/JIT logs.
- Semantics that defeat optimization: `eval`, `with`, monkey-patching builtins, reflection on
  everything.

## Related
- [[compilers-overview]], [[interpreters-eval-apply]], [[closures-and-environment-model]],
  [[garbage-collection]], [[compiler-optimizations]], [[polymorphism-and-dispatch]], [[hash-tables]].

## Sources
Crafting Interpreters part III; Deutsch & Schiffman 1984; Hölzle, Chambers & Ungar 1991; CS6120 lesson 12; V8 and HotSpot design documents.

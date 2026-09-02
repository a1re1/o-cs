---
title: Closures, environments and continuations — the environment model of evaluation, lexical vs dynamic scope, closure conversion, tail calls, CPS and first-class continuations, and "Lambda the Ultimate"
type: concept
section: "5.4"
level: 300
tags: [closures, environment-model, environments, frames, lexical-scope, static-scope, dynamic-scope, substitution-model, variable-lookup, free-variables, closure-conversion, lambda-lifting, flat-closures, linked-closures, upvalues, funarg-problem, tail-calls, tail-call-optimization, proper-tail-calls, loops-as-recursion, continuations, continuation-passing-style, cps, call-cc, delimited-continuations, generators, coroutines, exceptions-via-continuations, defunctionalization, secd, cek, lambda-the-ultimate, steele-sussman, objects-as-closures, callbacks, javascript-closures, python-late-binding]
sources: [pierce-tapl-and-pl-theory-texts, pl-theory-seminal-papers, sicp]
summary: The environment model replaces textual substitution with a chain of frames mapping names to values, and a closure is a function packaged with the environment where it was created — the mechanism that makes lexical (static) scope work when functions escape (the upward funarg problem), that compilers implement by closure conversion (flat or linked closure records, lambda lifting when nothing escapes), and that Steele and Sussman showed subsumes objects ("a closure is a poor man's object and vice versa"), loops (tail calls, which a proper implementation runs in constant space) and control flow; making the continuation — "the rest of the computation" — explicit via continuation-passing style gives a compiler IR in which every call is a jump, and reifying it as a first-class value (call/cc, delimited shift/reset) expresses exceptions, generators, coroutines, backtracking and async/await, while defunctionalizing continuations yields the explicit stacks of abstract machines (CEK) and of hand-written interpreters.
---
# Closures, environments and continuations

**In one sentence.** A function value is code plus the variables it can see; the
continuation is everything that happens after it returns; once both are first-class, every
control structure is a library.

## The environment model (SICP 3.2; PLAI; EOPL ch. 3)
Substitution semantics ([[lambda-calculus]]) is correct but copies terms; interpreters use
**environments**: a frame binds names to values and points to its enclosing frame; variable
lookup walks the chain. `(define (make-adder n) (lambda (x) (+ x n)))` — evaluating the inner
`lambda` creates a **closure** ⟨code, env⟩ capturing the frame where n is bound; applying it
extends *that* environment, not the caller's — which is exactly **lexical/static scope**
(binding determined by program text). **Dynamic scope** (early Lisp, `let` in Emacs Lisp,
shell variables, Perl `local`) looks names up in the *caller's* environment — cheap to
implement, impossible to reason about modularly; Steele/Sussman's Scheme (1975) made
lexical scope standard. Assignment makes environments mutable stores of boxes
(SICP's `set!` and the need for the environment model), and closures over loop variables
capture the *variable*, not its value (the JavaScript `var` loop bug, Python's late binding
in lambdas). Shadowing, `let` = application of a λ, `letrec` = closures whose environment
contains themselves (a knot tied by mutation or a fixed point).

## Implementation: closure conversion (Appel; Steele's RABBIT)
Compilers make closures explicit: **closure conversion** turns each λ into a record {code
pointer, captured free variables} and rewrites calls to pass the record as an extra argument
(the receiver). **Flat closures** copy each free variable (O(1) access, more copying, GC-
friendly) vs **linked closures** (pointer to parent frame — cheap creation, space leaks by
retaining whole frames); Lua's **upvalues** and Java's captured `final` copies are the flat
strategy; C++ lambdas' capture lists make it explicit. **Lambda lifting** (Johnsson): when a
function doesn't escape, pass free variables as parameters instead of allocating.
**Escape analysis** allocates non-escaping closures on the stack. The **funarg problem**
(1960s): downward funargs (passing a function down) work with a stack; **upward** funargs
(returning one) need heap-allocated environments — the reason Pascal/C lacked true closures
and why "closures need garbage collection" ([[garbage-collection]],
[[memory-layout-stack-heap]]). Objects: a closure with several entry points is an object; an
object with one method is a closure ("the venerable master Qc Na" koan); method calls =
applying a closure stored in a dictionary ([[polymorphism-and-dispatch]], [[design-patterns-catalog]]
— Strategy/Command are closures).

## Tail calls and loops (Steele & Sussman 1976)
A call in **tail position** (nothing left to do after it returns) can reuse the caller's
frame: **proper tail calls** turn recursion into iteration in constant space — Scheme
requires it, so `loop` is just a tail-recursive function; ML/OCaml/Haskell/Lua/Elixir have it;
JVM/Python/JavaScript (except Safari) don't (trampolines as the workaround). "Lambda: The
Ultimate GOTO": a tail call is a jump with arguments; `goto`, loops, and state machines are
mutually tail-recursive functions ([[isa-and-assembly]]); accumulator passing makes
non-tail recursion tail-recursive ([[fold-and-structural-recursion]]).

## Continuations and CPS (Reynolds 1972; Plotkin 1975; Appel 1992)
The **continuation** of an expression is the rest of the computation as a function of its
value. **Continuation-passing style**: every function takes an extra argument k and never
returns — `fact n k = if n=0 then k 1 else fact (n−1) (λv. k (n × v))`; all calls are tail
calls, evaluation order is explicit, the stack becomes a chain of closures. As a compiler IR
(RABBIT, SML/NJ, older GHC): control flow and data flow unified, optimizations are
β-reductions; ANF is the direct-style equivalent ([[intermediate-representations-and-ssa]] —
SSA and CPS are the same thing, Kelsey/Appel). **First-class continuations**: `call/cc`
captures the current continuation as a procedure — escapes/exceptions (invoke k early),
generators and coroutines (save k, resume later), backtracking (amb), cooperative threads;
`dynamic-wind` for cleanup. **Delimited continuations** (`shift`/`reset`, Danvy & Filinski;
effect handlers in OCaml 5/Koka) capture only up to a marker — composable, the modern form
behind async/await, generators and algebraic effects
([[async-and-event-driven-concurrency]]). Classical logic ↔ call/cc
([[curry-howard-correspondence]]). Web servers "capture the continuation" across requests
(PLT web server) — the idea behind stateful-vs-stateless debates.

## Defunctionalization and abstract machines (Reynolds 1972; Danvy)
Replace first-class functions by data: each λ becomes a constructor carrying its free
variables and an `apply` function dispatches — how to compile closures to languages without
them, and how CPS-transforming an interpreter and defunctionalizing its continuations
mechanically derives the **CEK machine** with an explicit stack of frames
([[operational-and-denotational-semantics]]); generators/async in Rust and C# compile to
defunctionalized state machines by the same transformation.

## Pitfalls
- Capturing a mutable loop variable; closures retaining large frames (leaks — linked
  closures, JavaScript's DOM listeners).
- Deep recursion without tail calls (stack overflow); assuming TCO exists in your language.
- Callback hell as manual CPS; using call/cc where delimited continuations/effects are safer.
- Dynamic scope (or `this` in JavaScript, which is dynamically bound) surprising lexical
  intuitions.

## Related
- [[lambda-calculus]], [[operational-and-denotational-semantics]], [[sicp]],
  [[fold-and-structural-recursion]], [[streams-and-lazy-evaluation]], [[polymorphism-and-dispatch]],
  [[intermediate-representations-and-ssa]], [[garbage-collection]], [[memory-layout-stack-heap]],
  [[async-and-event-driven-concurrency]], [[curry-howard-correspondence]].

## Sources
SICP 3.2; PLAI (functions, state, continuations); EOPL ch. 3, 5–6; Steele & Sussman "Lambda the Ultimate" papers 1975–77; Steele, RABBIT 1978; Reynolds 1972; Plotkin 1975; Appel, *Compiling with Continuations* 1992; Danvy & Filinski 1990; Danvy "A Rational Deconstruction of Landin's SECD Machine" 2004.

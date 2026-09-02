---
title: Purity, referential transparency, and equational reasoning
type: concept
section: "2.4"
level: 200
tags: [purity, referential-transparency, side-effects, immutability, equational-reasoning, functional-core-imperative-shell, idempotence, testability, memoization, parallelism, point-free]
sources: [hughes-why-fp-matters, backus-can-programming-be-liberated, wadler-monads, sicp]
summary: A pure expression can be replaced by its value anywhere without changing the program (referential transparency), which lets you reason by substitution, memoize, reorder, parallelize and test without setup; effects are pushed to the edges (functional core, imperative shell) or made explicit in types (monads), and Backus's algebra of programs shows why variable-free composition has clean laws.
---
# Purity and referential transparency

**In one sentence.** If `f 3` always means the same thing, you can substitute it, cache it, run it
anywhere, and prove things about it — that is what "no side effects" buys.

## Definitions
- **Pure** function: output depends only on inputs; no observable effects (mutation of shared state,
  I/O, time, randomness, exceptions as control flow).
- **Referential transparency**: an expression may be replaced by its value (or by any equal
  expression) without changing behaviour — "equals can be substituted for equals". Lost as soon as
  assignment appears ([[assignment-state-and-environments]], SICP 3.1.3).
- **Immutability** of data is the usual mechanism; persistent structures make it cheap
  ([[persistent-data-structures]]).

## What it enables
- **Equational reasoning**: rewrite programs with laws (`map f . map g = map (f . g)`,
  monad laws) — Backus's "algebra of programs"; compilers use it for fusion and inlining.
- **Modularity/glue** (Hughes): pure producers and consumers compose because neither depends on
  when the other runs — lazy evaluation is safe only because evaluation order can't be observed
  ([[streams-and-lazy-evaluation]]).
- **Memoization** and caching are valid; **parallelism** needs no locks (no shared mutable state —
  [[synchronization-primitives]]); **testing** needs no mocks or setup ([[unit-testing]]);
  **replay/undo** are free.
- Idempotent, deterministic pipelines in data engineering and infrastructure-as-code are the same
  principle at system scale ([[mapreduce-and-dataflow]]).

## Living with effects
- **Functional core, imperative shell**: compute pure values, perform I/O at the boundary.
- Make effects explicit in the type: `Result`, `IO`, `State s a`, async ([[monads]]); or pass them as
  values (dependency injection of clocks/randomness).
- Local mutation that never escapes (a loop counter, an in-place sort of a fresh buffer) preserves
  observational purity — Rust's ownership makes "never escapes" checkable ([[ownership-and-borrowing]]).

## Pitfalls
- Hidden effects: logging, global caches, `Date.now()`, exceptions, laziness + I/O ordering.
- Purity at the cost of clarity or performance (immutable updates in a hot loop; monad towers).
- "Pure" functions that depend on mutable inputs by reference (aliasing).

## Related
- [[higher-order-functions]], [[monads]], [[streams-and-lazy-evaluation]], [[assignment-state-and-environments]],
  [[persistent-data-structures]], [[unit-testing]].

## Sources
Hughes §1–2, 4; Backus 1978; Wadler §1; SICP 3.1.

---
title: Data abstraction, abstraction barriers, tagged data, and the expression problem
type: concept
section: "2.1"
level: 100
tags: [data-abstraction, abstraction-barriers, constructors, selectors, representation-independence, tagged-data, data-directed-programming, message-passing, dispatch, expression-problem, generic-operations, closures-as-data]
sources: [sicp, composing-programs]
summary: Define a data type by the operations (constructor + selectors) and the conditions they satisfy, hide the representation behind an abstraction barrier so it can change, and choose between data-directed dispatch (tables keyed by type) and message passing (objects) — the two halves of the expression problem — when adding types and operations.
---
# Data abstraction

**In one sentence.** Programs above the barrier use only `make-rat`, `numer`, `denom`; programs below
implement them however they like; nobody crosses the line — so representations can change without
touching users.

## Abstraction barriers (SICP 2.1)
Layers: programs that use rational numbers → `add-rat`, `sub-rat` → `make-rat`, `numer`, `denom` →
pairs (`cons`, `car`, `cdr`) → however pairs are implemented. Each horizontal line is a barrier: the
procedures at a level are the *interface*. Benefits: maintainability (change gcd-normalization from
construction time to selection time without touching callers), deferred design decisions, and the
possibility of multiple implementations. **Abstraction barrier violation** (Composing Programs): a
caller that uses `car` on a rational because it "knows" it is a pair — fragile and forbidden.

## What is meant by data? (SICP 2.1.3)
Data is defined by the constructor, the selectors, and the *conditions* they must satisfy
(`(numer (make-rat n d)) / (denom (make-rat n d)) = n/d`). Anything satisfying the contract is a valid
representation — including pure procedures: `cons` can be a closure that dispatches on 0/1, and Church
numerals encode numbers as functions. Hence "data" and "procedure" are not fundamentally distinct
([[lambda-calculus]]). In modern terms: an abstract data type is a specification, and a
representation invariant plus abstraction function connect it to concrete values (§2.2,
[[specifications-and-invariants]]).

## Multiple representations (SICP 2.4)
Complex numbers as rectangular *and* polar: attach a **type tag** and dispatch.
- **Data-directed programming**: a 2-D table (operation × type) of procedures; `apply-generic` looks
  up (op, tag). Adding a type = add a column of entries; adding an operation = add a row.
- **Message passing**: each object is a procedure that takes an operation name and dispatches
  internally; adding a type is easy (one new dispatcher), adding an operation touches every type.
- **Explicit dispatch** (if/else on tags) is the anti-pattern: every operation knows every type.
This is the **expression problem**: OO languages make new types easy (subclass), functional languages
with pattern matching make new operations easy; type classes/traits, multimethods, and visitors are
the workarounds ([[objects-and-classes]], [[algebraic-data-types]]).

## Generic operations with coercion (SICP 2.5)
A tower of types (integer ⊂ rational ⊂ real ⊂ complex) with `raise` and `drop` lets one table handle
mixed arguments — the design that numeric libraries and Julia's promotion rules follow.

## Pitfalls
- Leaky abstractions: exposing performance or representation quirks through the interface.
- Over-abstraction: a barrier with one implementation and no volatility is ceremony; add it when the
  representation is likely to change or is used from many places.
- Tags must be checked consistently; untagged unions are a source of silent bugs.

## Related
- [[higher-order-functions]], [[objects-and-classes]], [[specifications-and-invariants]],
  [[algebraic-data-types]], [[interpreters-eval-apply]].

## Sources
SICP 2.1–2.5; Composing Programs 2.2–2.7.

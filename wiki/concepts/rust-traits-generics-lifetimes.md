---
title: Rust traits, generics, trait objects, and error handling with Result
type: concept
section: "2.3"
level: 300
tags: [rust, traits, generics, monomorphization, trait-objects, dyn, static-dispatch, dynamic-dispatch, result, option, question-mark-operator, error-handling, iterators, closures, enums, pattern-matching]
sources: [rust-book]
summary: Traits are interfaces with default methods and associated types; generics with trait bounds are monomorphized (zero-cost static dispatch) while `dyn Trait` objects give dynamic dispatch; enums with exhaustive `match` model data as sums of cases; `Option`/`Result` with `?` make absence and failure explicit values instead of nulls and exceptions; iterators and closures compile to loops.
---
# Rust traits, generics, and error handling

**In one sentence.** Rust's abstraction toolkit is traits (behaviour), generics (parametric code
specialized at compile time), enums (data with cases), and `Result` (failure as data) — no
inheritance, no null, no exceptions.

## Traits and generics (Rust Book ch. 10, 18)
- `trait Shape { fn area(&self) -> f64; fn describe(&self) -> String { … default … } }`; implement for
  any type, including foreign types (orphan rule: trait or type must be local). Associated types
  (`Iterator::Item`), operator overloading via `std::ops`, `derive` for common traits
  (`Debug, Clone, PartialEq, Eq, Hash, Ord`) — the [[equality-and-hashing]] contract enforced by pairing.
- `fn total<T: Shape>(xs: &[T])` — **monomorphized**: one copy per concrete T, fully inlined, no
  runtime cost; `impl Trait` in argument/return position; `where` clauses.
- `Box<dyn Shape>` / `&dyn Shape` — **trait objects**: vtable dispatch, heterogeneous collections;
  object safety rules (no generics/`Self` returns in dispatched methods). Choose static dispatch by
  default, dynamic when you need heterogeneity or to cut code size.
- Traits play the role of Haskell type classes and Java interfaces; compare [[type-systems]].

## Enums and pattern matching (ch. 6, 19)
`enum Shape { Circle(f64), Rect { w: f64, h: f64 } }` — a sum type; `match` must be exhaustive, so
adding a variant produces compile errors at every unhandled site (the functional half of the
expression problem — [[data-abstraction]], [[algebraic-data-types]]). Patterns destructure structs,
tuples, slices, references; `if let`/`let else`/`while let` for single cases.

## Error handling (ch. 9)
- `Option<T>` = `Some(T) | None`: no null; force the caller to handle absence (`unwrap` panics — for
  prototypes and truly impossible cases; `?` propagates; `map`/`and_then`/`unwrap_or` combinators).
- `Result<T, E>` = `Ok(T) | Err(E)`; the `?` operator returns early with the error converted via
  `From` — so a function's error path is visible in its signature.
- `panic!` for bugs/invariant violations (unrecoverable, unwinds); `Result` for expected failures
  (I/O, parsing, validation). Libraries define error enums (`thiserror`); applications use a boxed
  dynamic error (`anyhow`) with context ([[error-handling-strategies]]).

## Closures and iterators (ch. 13)
Closures capture by reference, mutable reference, or move (`move ||`); traits `Fn`/`FnMut`/`FnOnce`
encode how the captured state is used. Iterators are lazy adapters (`map`, `filter`, `zip`, `take`,
`chain`, `collect`) that compile to the same code as hand loops — the [[higher-order-functions]]
pipeline at zero cost ([[streams-and-lazy-evaluation]]).

## Pitfalls
- Overusing `unwrap`/`clone` to appease the compiler; fix ownership instead ([[ownership-and-borrowing]]).
- `dyn Trait` with generics or `Self`-returning methods is not object-safe.
- Trait coherence errors when implementing foreign traits for foreign types — wrap in a newtype.
- `String` vs `&str`, `Vec<T>` vs `&[T]`: accept borrowed slices in APIs, own in structs.

## Related
- [[ownership-and-borrowing]], [[algebraic-data-types]], [[error-handling-strategies]], [[type-systems]],
  [[higher-order-functions]], [[equality-and-hashing]].

## Sources
Rust Book ch. 6, 9, 10, 13, 18–20; CS110L lectures 3–5.

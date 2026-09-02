---
title: ML modules, signatures, and functors
type: concept
section: "2.4"
level: 300
tags: [modules, signatures, structures, functors, ocaml, standard-ml, abstract-types, encapsulation, sealing, parameterized-modules, compilation-units, expression-problem]
sources: [cs3110-ocaml]
summary: An ML module (structure) bundles types and values; a signature is its interface, and sealing a structure with a signature hides the representation (an abstract type); a functor is a function from modules to modules — e.g. a Set built from any Ordered type — giving parameterization over types *and* the operations on them, which traits/typeclasses/generics approximate.
---
# ML modules and functors

**In one sentence.** Signatures are ADT interfaces, structures are implementations, and functors let
you write an implementation once for every module that satisfies an interface.

## Pieces (CS3110 ch. 5)
- **Structure**: `module Stack = struct type 'a t = 'a list  let empty = []  let push x s = x :: s
  … end`.
- **Signature**: `module type STACK = sig type 'a t  val empty : 'a t  val push : 'a -> 'a t -> 'a t …
  end`. Sealing `module ListStack : STACK = struct … end` makes `'a t` **abstract** — clients cannot
  see it is a list; rep changes cannot break them ([[data-abstraction]],
  [[abstract-data-types-and-rep-invariants]]). `with type` re-exposes when needed.
- Compilation units: `foo.ml` is a structure, `foo.mli` its signature — encapsulation at file level.
- **Functor**: `module MakeSet (Ord : ORDERED) : SET with type elt = Ord.t = struct … end`;
  `module IntSet = MakeSet (Int)`. A functor is a *function*, not inheritance: its output can differ
  arbitrarily from its input (CS3110's warning: it is not Java `extends`). Applicative vs generative
  functors govern whether two applications share type identity.
- `include` for extension/mixins; first-class modules pack a structure into a value.

## Why it matters
- Separates *interface satisfaction* from *type membership*: an `int` can be ordered several ways by
  passing different `ORDERED` modules — where a typeclass forces one instance per type
  ([[rust-traits-generics-lifetimes]], [[type-systems]]).
- Large-scale program structure: dependency injection at compile time with full type checking;
  the "functor over a signature" pattern is how Jane Street and the OCaml compiler organize code.
- The type-checker can hide invariants behind abstract types (phantom types, typestate).

## Pitfalls
- Over-sealing: forgetting `with type` makes the abstract type unusable with existing values.
- Functor application boilerplate; deep functor towers hurt compile errors and readability.
- Confusing a module (a namespace/compile-time object) with a value; use first-class modules only
  when runtime choice is really needed.

## Related
- [[data-abstraction]], [[abstract-data-types-and-rep-invariants]], [[modularity-and-information-hiding]],
  [[rust-traits-generics-lifetimes]], [[type-systems]], [[algebraic-data-types]].

## Sources
CS3110 ch. 5 (modules, encapsulation, functors, includes) and ch. 6.

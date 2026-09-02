---
title: Polymorphism and dispatch — subtype, parametric, ad hoc; static vs dynamic; vtables and double dispatch
type: concept
section: "2.5"
level: 300
tags: [polymorphism, subtype-polymorphism, parametric-polymorphism, ad-hoc-polymorphism, overloading, dynamic-dispatch, static-dispatch, vtable, virtual-methods, double-dispatch, visitor, multimethods, duck-typing, monomorphization, expression-problem]
sources: [gof-design-patterns, rust-book, cs3110-ocaml, sicp]
summary: Polymorphism lets one interface serve many types: subtype (a Shape reference may hold a Circle; resolved at runtime via a vtable), parametric (generics/templates, one definition for all types, monomorphized or erased), and ad hoc (overloading/typeclasses chosen by the static type); single dispatch picks the method by the receiver only, so operations over two types need double dispatch (Visitor) or pattern matching — the two halves of the expression problem.
---
# Polymorphism and dispatch

**In one sentence.** "Which code runs for `x.draw()`?" has three answers — the receiver's runtime
class (subtype), the instantiated type parameter (parametric), or the static overload/instance (ad
hoc) — and each has a cost model.

## Three kinds (Cardelli & Wegner)
- **Subtype** polymorphism: a variable of type T holds any subtype; the method is looked up at
  runtime — **dynamic dispatch**. Implementation: each object holds a pointer to its class's
  **vtable** (array of function pointers); call = load vtable, load slot, indirect call. Cost: an
  indirect branch (predictable when monomorphic; JITs inline via speculative devirtualization). C
  simulates it with structs of function pointers ([[function-pointers-and-generic-c]]); Rust `dyn`,
  Java interfaces, Python attribute lookup (dictionary, slower but the same idea).
- **Parametric** polymorphism: `fn max<T: Ord>(a: T, b: T)`. Static: one definition, type-checked
  once. Implementation: **monomorphization** (C++ templates, Rust — fast, code bloat) or **type
  erasure** (Java generics, OCaml — uniform representation, boxing). See [[type-systems]].
- **Ad hoc** polymorphism: overloading (`+` on ints and strings), typeclasses/traits resolved by the
  static type (Haskell `Show`, Rust `impl Display for X`, C++ concepts, C11 `_Generic`). Dispatch
  happens at compile time with dictionary passing or monomorphization.
- Duck typing (Python/JS) = subtype polymorphism with no declared interface; structural typing
  (Go interfaces, TypeScript) = interface conformance by shape, checked statically.

## Single vs double dispatch
OO languages dispatch on the receiver only. `collide(asteroid, ship)` needs both types: **Visitor**
(GoF) simulates double dispatch — `element.accept(visitor)` dispatches on the element, then
`visitor.visitX(this)` dispatches on the visitor. Multimethods (CLOS, Julia, Clojure) dispatch on all
arguments. In languages with [[algebraic-data-types]], a `match` on a pair does it directly. SICP's
data-directed programming (operation × type table) is the explicit form ([[data-abstraction]]).

## The expression problem
Rows = data cases, columns = operations. Classes make adding a row easy (new subclass) and a column
hard (touch every class); ADTs + functions the reverse. Visitor moves OO to the ADT side. Solutions
that do both (typeclasses with open extension, object algebras, tagless final) are advanced
[[type-systems]] territory.

## Practical guidance
- Dynamic dispatch where the set of types is open (plugins, heterogeneous collections); static
  dispatch where performance or inlining matters.
- Don't pay for a vtable when an enum + match is clearer and closed.
- Avoid overloading that changes semantics by argument type; keep overloads as convenience.

## Related
- [[objects-and-classes]], [[inheritance-vs-composition]], [[design-patterns-catalog]],
  [[rust-traits-generics-lifetimes]], [[type-systems]], [[function-pointers-and-generic-c]].

## Sources
GoF (Visitor, Strategy); Rust Book ch. 10, 18; CS3110 ch. 5, 8; SICP 2.4.

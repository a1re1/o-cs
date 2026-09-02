---
title: Subtyping and the Liskov substitution principle (subtypes vs subclasses)
type: concept
section: "2.2"
level: 300
tags: [subtyping, liskov-substitution, behavioral-subtyping, subclassing, inheritance, interfaces, contravariance, covariance, spec-strength, history-constraint, composition-over-inheritance]
sources: [mit-6-102-software-construction, effective-java]
summary: B is a subtype of A iff every B satisfies A's specification — weaker or equal preconditions, stronger or equal postconditions, preserved invariants and history constraints — which is a statement about specs, not reps; subclassing without behavioural subtyping (Square extends Rectangle, mutable subclass of immutable type) breaks clients, so favour composition and interfaces.
---
# Subtyping and the Liskov substitution principle

**In one sentence.** "B is a subtype of A" means "every B is an A" — every value of B satisfies the
spec of A — so client code written against A keeps working when handed a B.

## The rule (Liskov & Wing 1994, as taught in 6.102)
A subtype's methods, compared with the supertype's:
- may **weaken preconditions** (accept more) but not strengthen them;
- may **strengthen postconditions** (promise more) but not weaken them;
- must preserve the supertype's **invariants** (an immutable supertype's subtype must be immutable);
- must respect the **history constraint**: no new mutators that change state the supertype declared fixed;
- return types covariant, parameter types contravariant (what type checkers enforce is only the
  signature part; the behavioural part is on you).
Equivalently: the subtype's spec is *stronger* than the supertype's ([[specifications-and-invariants]]).

## Classic violations
- `Square extends Rectangle` with `setWidth`/`setHeight`: Rectangle's spec lets width change alone;
  Square can't — history constraint broken. Fix: immutable shapes, or no inheritance.
- A subclass that throws `UnsupportedOperationException` for an inherited mutator (Java's unmodifiable
  collections are a documented exception — a smell nonetheless).
- Overriding `equals` in a subclass adds fields → symmetry breaks (Bloch item 10); prefer composition.
- Subclass that strengthens a precondition ("only accepts positive ints").

## Subclassing ≠ subtyping (6.102 reading 08)
Subclassing inherits the *rep* and implementation; subtyping is about *specs*. Interfaces give
subtyping without sharing reps; inheritance shares reps and creates fragile coupling: subclass
correctness depends on the superclass's self-use of overridable methods (Bloch item 18, "design and
document for inheritance or else prohibit it"). Hence **composition over inheritance**: wrap, delegate,
implement the interface.

## Why it matters for tooling
Type checkers verify signatures, not behaviour; tests written against the supertype's spec and run
against each subtype (contract tests) are how you check LSP. Variance annotations in generics (Java
wildcards PECS, Kotlin `in`/`out`, Scala `+`/`-`) encode covariance/contravariance in the type system
([[type-systems]]).

## Related
- [[specifications-and-invariants]], [[abstract-data-types-and-rep-invariants]], [[objects-and-classes]],
  [[design-patterns]], [[type-systems]].

## Sources
6.102 reading 08 (Interfaces & Subtyping); Effective Java items 10, 18–20; Liskov & Wing, "A Behavioral Notion of Subtyping" (1994, to be ingested in §2.5).

## The formal version (Liskov & Wing 1994, added §2.5)
The **Subtype Requirement**: every property provable of T-objects from T's specification must hold
of S-objects. Signature rules (contravariant arguments, covariant results) prevent type errors only
— a stack and a queue with identical `put`/`get` signatures would each be a subtype of the other.
The behavioral rules: (1) **methods rule** — `pre_T ⇒ pre_S` and `post_S ⇒ post_T` for each
inherited method, via an abstraction function from S values to T values; (2) **invariant rule** —
S's invariant implies T's; (3) **constraint/history rule** — S's history constraint implies T's, so
a subtype may add methods but not ones that produce state transitions T forbids (a mutable Bag is
not a subtype of an immutable Bag; a Square is not a subtype of a resizable Rectangle). Source:
[[liskov-wing-1994]]; consequences in [[inheritance-vs-composition]] and [[solid-principles]].

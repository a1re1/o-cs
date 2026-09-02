---
title: Inheritance vs composition, delegation, and interfaces
type: concept
section: "2.5"
level: 300
tags: [inheritance, composition, delegation, interfaces, subtyping, code-reuse, fragile-base-class, is-a, has-a, mixins, traits, refused-bequest, favor-composition]
sources: [gof-design-patterns, liskov-wing-1994, fowler-refactoring, effective-java]
summary: Inheritance couples a subclass to its parent's implementation (white-box reuse) and forces an is-a relation that must satisfy behavioral subtyping, while composition reuses by holding and delegating to another object behind an interface (black-box reuse) — so favor composition for reuse, use inheritance only for genuine substitutable subtypes, and reach for interfaces/traits to get polymorphism without either.
---
# Inheritance vs composition

**In one sentence.** Inherit to *be* a substitutable subtype; compose to *use* another object; use
an interface to be *treated as* one kind of thing.

## The two reuse mechanisms (GoF ch. 1.6)
- **Class inheritance**: white-box reuse — the subclass sees the parent's internals; defined at
  compile time; easy to modify by overriding; but "inheritance breaks encapsulation": changes to the
  parent ripple into subclasses (**fragile base class**); the subclass inherits the parent's
  representation and cannot swap it at runtime; deep hierarchies become rigid.
- **Object composition**: black-box reuse — objects are assembled via well-defined interfaces;
  delegation lets a Window forward `area()` to its Rectangle; behaviour can be changed at runtime;
  more objects, fewer classes; the design focuses on interfaces. GoF's second principle: *favor object
  composition over class inheritance*.
- **Interfaces/traits/typeclasses** give subtype polymorphism without sharing implementation —
  most of what inheritance is used for ([[polymorphism-and-dispatch]], [[rust-traits-generics-lifetimes]]).

## When inheritance is right
- The subtype genuinely satisfies the supertype's *specification* — invariants and history
  properties included (Liskov & Wing: an immutable type cannot have a mutable subtype; a Square
  that is-a mutable Rectangle breaks `setWidth`) — [[liskov-substitution]].
- Template Method / framework extension points where the base class *is designed for* extension
  and documents its self-use (Effective Java item 19: "design and document for inheritance or else
  prohibit it").
- Modeling closed, stable hierarchies (AST nodes, exceptions) — though sealed ADTs often fit better.

## Smells and fixes (Fowler)
Refused bequest (subclass ignores inherited members) → Replace Subclass with Delegate; a class that
inherits only for reuse → Replace Superclass with Delegate; parallel hierarchies → move behaviour;
`instanceof` cascades → polymorphism or a discriminated union.

## Interop notes
Rust/Go have no implementation inheritance: composition + traits/interfaces + embedding; Java 8+
default methods and Kotlin/Scala mixins recover shared behaviour on interfaces; "composition over
inheritance" is the design rule in game engines (entity–component systems) and UI frameworks.

## Related
- [[liskov-substitution]], [[polymorphism-and-dispatch]], [[design-patterns-catalog]],
  [[solid-principles]], [[objects-and-classes]], [[data-abstraction]].

## Sources
GoF ch. 1.6–1.7; Liskov & Wing §1, §5; Fowler ch. 3, 12; Effective Java items 18–19.

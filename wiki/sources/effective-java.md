---
title: Effective Java (Bloch)
type: source
section: "2.2"
level: 300
tags: [java, api-design, immutability, equals-hashcode, builder-pattern, generics, enums, interfaces, composition-over-inheritance, defensive-copies, exceptions]
sources: []
authors: [Joshua Bloch]
year: 2018
institution: Google / Sun
url: https://www.oreilly.com/library/view/effective-java/9780134686097/
license: proprietary-open-access
format: pdf
summary: Ninety numbered items (3rd ed., 2018) of API-design wisdom from the author of the Java collections — static factories and builders, singletons, dependency injection, equals/hashCode/toString contracts, immutability, composition over inheritance, interfaces over abstract classes, generics and PECS, enums, lambdas and streams, defensive copies, exceptions — most of which transfer to any statically typed OO language.
---
# Effective Java (Bloch, 3rd ed.)

## What it is
Chapters: creating and destroying objects (static factories, builders, singletons, dependency
injection, avoid finalizers, try-with-resources); methods common to all objects (`equals` contract:
reflexive/symmetric/transitive/consistent; always override `hashCode` with `equals`; `toString`;
`Comparable`); classes and interfaces (minimize accessibility, accessors not public fields,
**minimize mutability**, **favor composition over inheritance**, design and document for inheritance or
prohibit it, prefer interfaces to abstract classes, static member classes); generics (don't use raw
types, lists over arrays, bounded wildcards — PECS: producer-extends, consumer-super); enums and
annotations; lambdas and streams; methods (check parameters, defensive copies, overloading care,
return empty collections not null, Optional); general programming; exceptions (checked vs unchecked,
don't ignore, failure atomicity); concurrency (synchronize access, executors over threads,
`ConcurrentHashMap`); serialization (avoid).

## Key ideas → pages
- `equals`/`hashCode` contract and the pitfalls of overriding `equals` with inheritance (symmetry
  breaks) — [[equality-and-hashing]].
- Immutability: no mutators, final fields, defensive copies in and out; immutable objects are simple,
  thread-safe, shareable — [[abstract-data-types-and-rep-invariants]].
- Composition over inheritance; inheritance breaks encapsulation (self-use of overridable methods) —
  [[liskov-substitution]], [[design-patterns-catalog]].
- Builder for many parameters; static factory methods with names — [[design-patterns-catalog]].
- Fail-fast parameter checking, failure atomicity — [[specifications-and-invariants]].

## What it adds
Language-level mechanics for the principles in [[mit-6-102-software-construction]]; the `equals`
items are the canonical treatment.

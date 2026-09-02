---
title: SOLID and the classic OO design principles
type: concept
section: "2.5"
level: 300
tags: [solid, single-responsibility, open-closed, liskov-substitution, interface-segregation, dependency-inversion, dependency-injection, coupling, cohesion, law-of-demeter, dry, yagni, command-query-separation]
sources: [gof-design-patterns, fowler-refactoring, liskov-wing-1994, ousterhout-philosophy-of-software-design]
summary: SOLID — single responsibility (one reason to change), open–closed (extend without modifying), Liskov substitution (subtypes honor supertype contracts), interface segregation (small client-specific interfaces), dependency inversion (depend on abstractions, inject concretions) — plus cohesion/coupling, Demeter, DRY and YAGNI are heuristics for isolating change; they are useful as smells to look for and dangerous as rules applied mechanically (class explosion, needless indirection).
---
# SOLID and OO design principles

**In one sentence.** Every principle here is a way of asking "what happens when this changes?" — and
the answer should be "one place".

## The five
- **S — Single Responsibility**: a module should have one reason to change (one actor it answers
  to). Smells: divergent change, large class. Not "does one tiny thing": a *deep* module can have a
  broad, simple interface and still one responsibility ([[managing-complexity-in-software-design]]).
- **O — Open–Closed** (Meyer): open for extension, closed for modification — add behaviour by adding
  code (new subclass, strategy, plugin), not by editing tested code. Achieved through abstraction
  points ([[design-patterns-catalog]]); over-applied it produces speculative generality.
- **L — Liskov Substitution**: subtypes must be usable wherever the supertype is expected —
  preconditions no stronger, postconditions no weaker, invariants and history properties preserved
  ([[liskov-substitution]], [[liskov-wing-1994]]).
- **I — Interface Segregation**: clients should not depend on methods they don't use; split fat
  interfaces into roles (`Readable`, `Writable`). Go/Rust idiom: many one- or two-method interfaces.
- **D — Dependency Inversion**: high-level policy should not depend on low-level detail; both depend
  on abstractions, and concretions are supplied from outside (**dependency injection**, by
  constructor or parameter) — which is what makes code testable with fakes ([[unit-testing]]).

## The rest of the toolbox
- **Coupling and cohesion** (Constantine): minimize dependencies between modules, maximize
  relatedness within — the metric behind [[modularity-and-information-hiding]].
- **Law of Demeter** ("only talk to your friends"): avoid `a.b().c().d()` message chains that
  hard-code structure.
- **DRY** (one authoritative representation of each piece of knowledge) vs **duplication is cheaper
  than the wrong abstraction** — dedupe *knowledge*, not incidental similar code.
- **YAGNI / KISS**: no speculative generality; **Command–Query Separation** (Meyer): a method either
  changes state or returns a value ([[specifications-and-invariants]]).
- **Composition over inheritance** ([[inheritance-vs-composition]]); **program to interfaces**.

## Critique
SOLID is a checklist for object-oriented Java-era code; applied literally it yields tiny classes,
interface-per-class, and factories for everything — the "classitis" Ousterhout warns about. Use the
principles to diagnose change-pain, weigh against simplicity, and prefer the language's cheaper
mechanisms (functions, modules, ADTs).

## Related
- [[liskov-substitution]], [[modularity-and-information-hiding]], [[design-patterns-catalog]],
  [[inheritance-vs-composition]], [[refactoring]], [[managing-complexity-in-software-design]].

## Sources
GoF ch. 1; Meyer OOSC (open–closed, CQS); Liskov & Wing 1994; Fowler ch. 3; Ousterhout ch. 4–5.

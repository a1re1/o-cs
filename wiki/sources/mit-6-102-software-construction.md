---
title: MIT 6.102 Software Construction (formerly 6.031/6.005)
type: source
section: "2.2"
level: 200
tags: [software-construction, specifications, abstract-data-types, rep-invariants, abstraction-functions, immutability, testing, code-review, subtyping, equality, recursive-data-types, concurrency, typescript]
sources: []
authors: [Rob Miller, Max Goldman]
year: 2025
institution: MIT
url: https://web.mit.edu/6.102/www/
license: CC-BY-SA
format: html
summary: MIT's software construction course with all 19 readings open (TypeScript since 2022, Java before) — static checking, testing, code review, specifications, designing specs, ADTs, abstraction functions & rep invariants, interfaces & subtyping, functional programming, equality, recursive data types, grammars & parsing, debugging, concurrency, promises, mutual exclusion, callbacks/GUIs, message passing, little languages — organized around three goals: safe from bugs, easy to understand, ready for change.
---
# MIT 6.102 Software Construction

## What it is
Level 200 (after 6.100 intro programming and alongside 6.1200 discrete math). Each reading is a
long web page with embedded exercises; problem sets are graded in alpha/code-review/beta rounds; the
term ends with a team project (Star Battle puzzle app). Readings, Spring 2025: 01 static checking;
02 testing; 03 code review; 04 specifications; 05 designing specifications; 06 abstract data types;
07 abstraction functions & rep invariants; 08 interfaces & subtyping; 09 functional programming;
10 equality; 11 recursive data types; 12 grammars & parsing; 13 debugging; 14 concurrency;
15 promises; 16 mutual exclusion; 17 callbacks & GUIs; 18 message passing & networking; 19 little
languages. Every reading is judged against the course's three measures: **safe from bugs, easy to
understand, ready for change**.

## Key ideas → pages
- Specs as contracts (requires/effects); behavioural equivalence is defined *by the spec*, so the
  spec must exist before clients depend on the implementation (write S, T, then I) —
  [[specifications-and-invariants]].
- Designing specs: deterministic vs underdetermined, declarative vs operational, stronger vs weaker
  (weaker precondition or stronger postcondition); prefer declarative; make preconditions the caller's
  problem only when checking is expensive — [[specifications-and-invariants]].
- ADTs: creators, producers, observers, mutators; "an ADT preserves its own invariants"; representation
  exposure; abstraction function + rep invariant, `checkRep()` — [[abstract-data-types-and-rep-invariants]].
- Subtyping is about specs (B is a subtype of A iff every B satisfies A's spec — Liskov), subclassing is
  about reps; interfaces separate the two — [[liskov-substitution]], [[abstract-data-types-and-rep-invariants]].
- Immutability as the default; functional programming with map/filter/reduce; equality: reference vs
  observational; `equals` must be an equivalence relation consistent with `hashCode` and with the
  abstraction function — [[equality-and-hashing]].
- Recursive data types (immutable lists/trees as interfaces with variants; the interpreter pattern) —
  [[algebraic-data-types]].
- Testing: partition the input space, choose boundary values, black-box vs glass-box, coverage,
  test-first — [[unit-testing]].
- Code review: DRY, comments where needed, no magic numbers, one purpose per variable, don't use global
  variables, return results don't print them, avoid special-case code — [[code-review]].
- Concurrency readings: shared memory vs message passing, races, mutual exclusion, deadlock —
  [[synchronization-primitives]] (§4.2).

## Notable claims & quotes
- "Specifications are the linchpin of teamwork."
- "The final, and perhaps most important, property of a good abstract data type is that it preserves
  its own invariants."
- On safety: "a bug that takes down a program is better than one that silently corrupts data" (fail fast).

## What it adds
The operational definitions (spec, RI, AF, subtype) that make [[data-abstraction]] from SICP checkable
in code, and the testing/code-review discipline the rest of §7 builds on.

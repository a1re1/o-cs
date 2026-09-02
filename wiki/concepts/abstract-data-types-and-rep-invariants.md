---
title: Abstract data types, representation invariants, and abstraction functions
type: concept
section: "2.2"
level: 200
tags: [abstract-data-types, adt, rep-invariant, abstraction-function, representation-exposure, immutability, checkrep, creators-producers-observers-mutators, interfaces, defensive-copies, representation-independence]
sources: [mit-6-102-software-construction, effective-java, sicp]
summary: An ADT is defined by its operations (creators, producers, observers, mutators); a class implementing it must state its rep invariant (which concrete values are legal), its abstraction function (what each legal rep means), and a "safety from rep exposure" argument — and preserve its own invariants by hiding the rep, copying defensively, and preferring immutability; checkRep() turns the invariant into a runtime assertion.
---
# Abstract data types, rep invariants, abstraction functions

**In one sentence.** Clients see values and operations; the implementer chooses a representation and
must document two things — RI: which reps are valid, AF: what each valid rep denotes — and ensure no
operation (or leaked reference) can break RI.

## Operations classification (6.102 reading 06)
Creators (`new`, `of`), producers (`concat` returns a new value), observers (`size`, `get`),
mutators (`add`, `set`). Immutable types have no mutators; producers replace them. Immutability is an
invariant clients can rely on: no aliasing bugs, thread-safe, safe as hash keys, and "you can rule
out mutation when debugging" ([[assignment-state-and-environments]]).

## RI and AF (reading 07)
```
// Rep: private readonly chars: Array<string>; private readonly counts: Map<string, number>
// Rep invariant: every key of counts appears in chars; all counts > 0; chars has no duplicates
// Abstraction function: AF(chars, counts) = the multiset containing each c in chars counts.get(c) times
// Safety from rep exposure: fields are private and readonly; observers return copies or immutable views
```
- **RI**: a predicate on the rep; constructors establish it, every operation preserves it — the
  [[invariant-principle]] for objects. Write `checkRep()` and call it at the end of every constructor,
  producer and mutator (cheap ones always; expensive ones in debug builds). A violated RI is caught
  where it happens, not where it explodes.
- **AF**: a function from valid reps to abstract values; many reps may map to one value (a set as an
  unsorted array). AF defines **equality** of ADT values ([[equality-and-hashing]]) and decides what
  each operation must compute.
- **Rep exposure**: returning or accepting a mutable rep object lets clients break RI (return
  `this.items` → caller mutates it). Fixes: private fields, `readonly`/`final`, defensive copies on the
  way in and out, immutable collections, or expose only immutable views. State the argument in a
  comment.

## Interfaces and multiple reps (reading 08)
Define the ADT as an interface (only operations; no rep, no RI/AF) and implement it with classes;
several reps can coexist (`ArrayList`/`LinkedList`), and clients can't accidentally depend on a rep.
Generic types (`List<T>`) define families; enumerations define small finite ADTs.

## Design rules
- ADTs preserve their own invariants — never rely on clients to keep a structure consistent.
- Minimize mutability (Bloch item 17); if mutable, document exactly which operations mutate.
- Representation independence: clients that use only the operations keep working when the rep
  changes ([[data-abstraction]]).
- Fail fast: throw on violated preconditions and RI, don't silently repair.

## Pitfalls
- Getters that return internal mutable arrays/maps (most common rep exposure).
- Rep invariants that are documented but never checked; or checkRep that is O(n²) and left on in production.
- Two reps mapping to the same abstract value but `equals` comparing reps — inconsistent equality.

## Related
- [[specifications-and-invariants]], [[equality-and-hashing]], [[liskov-substitution]],
  [[data-abstraction]], [[invariant-principle]], [[unit-testing]].

## Sources
6.102 readings 06–08; Effective Java items 15–17, 50; SICP 2.1.

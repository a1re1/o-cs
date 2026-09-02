---
title: Equality — reference vs observational, equals/hashCode contract, equality of mutable types
type: concept
section: "2.2"
level: 200
tags: [equality, equivalence-relation, reference-equality, observational-equality, behavioral-equality, hashcode, equals-contract, hashing, immutable, mutable, abstraction-function]
sources: [mit-6-102-software-construction, effective-java]
summary: Equality on a type must be an equivalence relation (reflexive, symmetric, transitive) and, for an ADT, is defined by the abstraction function — two reps are equal iff they denote the same abstract value; equal objects must hash equal; for mutable types choose between observational equality (same now) and behavioural equality (same forever, i.e. reference), and never use a mutable object as a hash key.
---
# Equality and hashing

**In one sentence.** For immutable types define `equals` by the abstraction function; for mutable
types use reference equality (behavioural equality) unless you have a very good reason; whatever you
choose, `hashCode` must agree.

## Requirements (6.102 reading 10, Bloch item 10)
`equals` must be an **equivalence relation**: reflexive, symmetric, transitive; consistent (same answer
while unchanged); `x.equals(null)` false. Reference equality (`==`/`is`) trivially satisfies this;
value equality must be written carefully:
```java
@Override public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Point)) return false;    // instanceof, not getClass, unless you forbid subclassing
    Point p = (Point) o;
    return x == p.x && y == p.y;                 // compare via AF, not raw rep (a set as an unsorted array!)
}
@Override public int hashCode() { return Objects.hash(x, y); }   // equal objects => equal hashes
```
- **Hash contract**: equal ⇒ same hash; unequal may collide. Forgetting `hashCode` makes hash sets
  and maps silently fail to find equal keys ([[hash-tables]]). Python: define `__eq__` and `__hash__`
  together (defining `__eq__` alone makes the class unhashable); Rust: `PartialEq`/`Eq` and `Hash`
  must agree (derive both).
- Compare through the **abstraction function**: two reps that denote the same abstract value must be
  equal even if their bytes differ ([[abstract-data-types-and-rep-invariants]]).
- Floating point: `NaN != NaN` breaks reflexivity; `Double.equals` in Java uses bit patterns instead —
  pick the semantics deliberately ([[floating-point]]).

## Mutable types
- **Observational equality**: equal if no observer can distinguish them *now* (two lists with the same
  elements). **Behavioural equality**: equal if no sequence of operations, including mutators, can
  distinguish them — for mutable objects that is reference equality.
- Java's `List.equals` is observational; this is why a list used as a `HashMap` key breaks when
  mutated (its hash changes, the entry is lost). Rule: **mutable objects use reference equality**, or
  are never mutated while used as keys.
- Immutable types get the clean story: observational = behavioural, and structural equality is safe.

## Related concepts
- Interning/canonicalization (`String.intern`, small-integer caching) makes reference equality
  coincide with value equality — but only for interned values (Python `is` on small ints is a trap).
- `compareTo`/ordering should be consistent with `equals` for sorted collections (Bloch item 14).
- Deep vs shallow equality for nested structures; cyclic structures need visited sets.

## Related
- [[abstract-data-types-and-rep-invariants]], [[assignment-state-and-environments]], [[hash-tables]],
  [[objects-and-classes]].

## Sources
6.102 reading 10 (Equality); Effective Java items 10–14.

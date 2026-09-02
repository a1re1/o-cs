---
title: Sets, relations, functions, and cardinality
type: concept
section: "1.1"
level: 200
tags: [sets, relations, functions, bijection, injection, surjection, cardinality, countable, diagonalization, equivalence-relations, power-set]
sources: [mcs-lehman-leighton-meyer, hammack-book-of-proof, berkeley-cs70]
summary: The vocabulary underneath everything else — set operations and proofs by double inclusion, relations and their properties, functions as total/partial, injective/surjective/bijective, the mapping rules that drive counting, and countable vs uncountable via Cantor's diagonal argument.
---
# Sets, relations, functions, cardinality

## Sets
- Membership, subset, equality (A = B iff A ⊆ B and B ⊆ A — prove set equalities by **double
  inclusion**). Operations ∪ ∩ − complement, power set pow(A) with |pow(A)| = 2^|A|, product A × B.
- Set-builder notation {x ∈ D | P(x)} is a predicate ([[propositional-logic]]) over a domain; Russell's
  paradox shows why the domain is required.

## Relations
A binary relation R ⊆ A × B. On one set, the properties worth checking:
reflexive, symmetric, antisymmetric, transitive. **Equivalence relation** = reflexive + symmetric +
transitive; it partitions the set into equivalence classes (e.g. congruence mod n,
[[modular-arithmetic]]). **Partial order** = reflexive + antisymmetric + transitive, strict partial
order = irreflexive + transitive (see [[dags-and-partial-orders]]). The **transitive closure** of a
relation is its walk relation in graph terms.

## Functions
f: A → B assigns ≤ 1 element of B to each element of A (partial) or exactly one (total).
- **Injective** (one-to-one): distinct inputs, distinct outputs ⇒ |A| ≤ |B|.
- **Surjective** (onto): every b hit ⇒ |A| ≥ |B|.
- **Bijective**: both ⇒ |A| = |B|. This is the **Bijection Rule** of [[counting-rules]] and, in its
  contrapositive, the [[pigeonhole-principle]] (|A| > |B| ⇒ no injection).
- Composition, inverse (exists iff bijective), image and preimage.

## Cardinality (finite and infinite)
- |A| = |B| iff there is a bijection. A is **countable** if there is a surjection N → A (finite or
  countably infinite). N, Z, Q, N × N, finite strings over a finite alphabet, and *programs* are
  countable.
- **Cantor's diagonal argument**: pow(N), infinite bit strings, and R are uncountable — given any list
  of infinite bit strings, flip the diagonal to build one not on the list. Consequence: there are
  uncountably many functions N → {0,1} but only countably many programs, so **most functions are
  uncomputable**; the halting problem is the concrete example (MCS 7.2, §5.1).
- Schröder–Bernstein: injections both ways ⇒ bijection.

## Pitfalls
- "f is well-defined" must be checked when defining a function on equivalence classes via representatives.
- Injective ≠ "one input one output" (that is just being a function); it is "different inputs never collide".
- pow(A) vs A: |pow(A)| > |A| for every set, finite or not.

## Related
- [[counting-rules]], [[pigeonhole-principle]] — mapping rules applied to finite sets.
- [[graph-theory-basics]] — a graph is a symmetric relation.
- [[dags-and-partial-orders]] — orders as relations.

## Sources
MCS ch. 4 and 7; Book of Proof part IV; CS70 Notes on countability.

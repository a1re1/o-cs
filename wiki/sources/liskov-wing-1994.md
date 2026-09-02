---
title: A Behavioral Notion of Subtyping (Liskov & Wing, 1994)
type: source
section: "2.5"
level: 400
tags: [liskov-substitution, subtyping, behavioral-subtyping, invariants, history-properties, contravariance, covariance, specifications, abstraction-function, constraint-rule]
sources: []
authors: [Barbara Liskov, Jeannette Wing]
year: 1994
institution: MIT / CMU
url: https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf
license: ACM-open
format: pdf
summary: Defines subtyping behaviorally — S is a subtype of T if every property provable about T-objects holds for S-objects — going beyond signature contra/covariance (which would make stacks and queues subtypes of each other) with a methods rule (preconditions may weaken, postconditions must strengthen), an invariant rule, and a history/constraint rule (a subtype may not add mutations that violate the supertype's history properties), and shows how to prove a subtype relation from formal specifications.
---
# A Behavioral Notion of Subtyping

## What it is
§1 motivation: `x: T := E` is legal when E's type is a subtype of T, and the program is expected to
keep working — contra/covariance rules only prevent *type errors*, not misbehaviour (stack vs
queue with the same `put`/`get` signatures). The **Subtype Requirement**: any property φ(x)
provable about objects of type T must hold for objects of subtype S. The properties are safety
properties: **invariants** (over single states) and **history properties** (over pairs of states —
e.g. "a bag's bound never changes"). §2 model of computation (shared mutable objects, possibly
concurrent). §3 type specifications (Larch-style: invariant, constraint, methods with requires/
ensures). §4 the subtype relation: an **abstraction function** from S values to T values; a
**renaming map** from T's methods to S's; **methods rule** — for each supertype method, the
subtype's precondition is implied by the supertype's (weaker) and the subtype's postcondition
implies the supertype's (stronger), with contravariant argument / covariant result types;
**constraint rule** — the subtype's history constraint implies the supertype's. Extra methods are
allowed provided they respect the constraint (an *immutable* type's subtype cannot add a mutator).
§5 examples (bag/stack, sets with different iteration guarantees, elephant/ mutable vs immutable
points); §6 ramifications (multiple implementations, the role of type checking); §7 related work.

## Notable claims
- Signatures are necessary, behaviour is what matters; the definition is *constructive*: a few
  lemmas from the two specifications prove the relation.
- Two formulations (constraint-based and extension-map-based) that satisfy the requirement.

## What it adds
Formal ground for [[liskov-substitution]] and for "spec strength ordering" in
[[specifications-and-invariants]]; the history rule explains why `MutableList` is not a subtype of
`ImmutableList`, a lesson repeated in [[inheritance-vs-composition]].

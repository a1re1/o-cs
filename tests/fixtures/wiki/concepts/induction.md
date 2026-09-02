---
title: Mathematical Induction
type: concept
section: "1.1"
level: 200
tags: [logic, proofs, induction, sets, number-theory]
sources: [mit-6.042j, lehman-mcs]
summary: Induction proves a statement P(n) for all n by showing a base case and that P(k) implies P(k+1); variants include strong and structural induction.
---

# Mathematical Induction

**In one sentence.** Induction proves that a predicate P(n) holds for every natural number n by establishing a base case and an inductive step from P(k) to P(k+1).

## How it works

The weak induction principle has two parts:

1. **Base case:** prove P(0) (or P(1)) directly.
2. **Inductive step:** assume the **inductive hypothesis** P(k) and prove P(k+1).

By the **well-ordering principle** — every nonempty set of naturals has a least
element — this suffices: if some n violates P, the least such n cannot be a
base case and its predecessor violates the step, a contradiction.

A clean template: to prove `sum_{i=0..n} i = n(n+1)/2`, check n = 0, then add
(n+1) to the hypothesis for k and simplify.

## Variants

- **Strong induction** assumes P(0)..P(k) all hold; needed when the step uses
  more than the immediate predecessor (e.g. every integer > 1 has a prime
  factorization, via a prime or a smaller factor).
- **Structural induction** proves properties of recursively defined objects —
  trees, formulas, lists — by induction on the constructor rules instead of
  numbers. It is the standard proof tool for compiler correctness and parser
  invariants.
- **Induction on a well-founded relation** generalizes both: any relation with
  no infinite descending chain supports an induction principle.

## Pitfalls & gotchas

- Forgetting the base case: "all horses are one color" fails exactly there.
- The inductive hypothesis must be stated and *used*; restating the goal is not
  a proof.
- Off-by-one domain slips: strong induction over n ≥ 2 needs two base cases.

## Related

[[bm25]] — term-frequency saturation and length normalization, the retrieval analogue of tuning an inductive parameter.
[[raft]] — safety arguments for replicated logs are typically inductive on the log index.

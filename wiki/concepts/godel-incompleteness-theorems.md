---
title: Gödel's incompleteness theorems
type: concept
section: "1.5"
level: 400
tags: [incompleteness, godel, arithmetization, godel-numbering, diagonal-lemma, fixed-point, representability, consistency, tarski-undefinability, lob-theorem, peano-arithmetic]
sources: [open-logic-project]
summary: Any consistent, effectively axiomatized theory strong enough to represent computable functions leaves some true arithmetic sentences unprovable (first theorem) and cannot prove its own consistency (second); the proof is Cantor's diagonal argument run inside arithmetic via Gödel numbering and the fixed-point lemma, and it is the same construction as the halting problem.
---
# Gödel's incompleteness theorems

**In one sentence.** Arithmetic can talk about its own proofs, so it can build a sentence G that says
"G is not provable"; if the theory is consistent G is true but unprovable, and consistency itself is
unprovable.

## Ingredients (Open Logic Part 6)
1. **Arithmetization**: assign numbers to symbols, formulas, and derivations (Gödel numbering);
   "x is the code of a proof of the formula coded by y" is a computable relation Prf(x, y).
2. **Representability**: every computable function/relation is definable in Peano arithmetic (PA), even
   in the weak theory Q — so PA proves Prf(m, n) exactly when it is true.
3. **Diagonal (fixed-point) lemma**: for any formula φ(x) there is a sentence ψ with
   PA ⊢ ψ ↔ φ(⌜ψ⌝). (The self-reference is achieved by a substitution function, like a quine.)
4. Let Prov(y) := ∃x Prf(x, y) and take G with PA ⊢ G ↔ ¬Prov(⌜G⌝).

## The theorems
- **First** (Gödel 1931, Rosser 1936 form): if T ⊇ Q is consistent and effectively axiomatized, T is
  incomplete — some sentence is neither provable nor refutable. Proof sketch: if T ⊢ G then T proves
  Prov(⌜G⌝) and ¬Prov(⌜G⌝), contradiction; if T ⊢ ¬G then (with ω-consistency, or Rosser's trick)
  another contradiction.
- **Second**: T cannot prove Con(T) (the sentence ¬Prov(⌜0=1⌝)), because the first theorem's proof
  formalizes inside T to give T ⊢ Con(T) → G.
- **Tarski**: arithmetic truth is not definable in arithmetic (else the diagonal lemma yields a liar
  sentence). Löb's theorem: if T ⊢ Prov(⌜φ⌝) → φ then T ⊢ φ.

## Computability view (same theorem, different clothes)
The set of theorems of T is r.e.; if T were complete and consistent, it would be decidable (search for
a proof of φ or ¬φ), hence the halting problem would be decidable via representability. So
incompleteness follows from undecidability ([[computability-and-halting-problem]]); Cantor's
diagonal, the halting proof, Gödel's G, and Tarski's liar are one construction
([[sets-relations-functions]]).

## What it does and does not mean
- Does: no single consistent axiomatic system captures all of arithmetic; consistency of PA/ZFC must be
  assumed or proved in a stronger system; Hilbert's program in its original form fails.
- Does not: undermine ordinary mathematics or verification — proof assistants prove *specific*
  theorems, and Gödel sentences are contrived; also concrete independent statements exist (Goodstein's
  theorem, Paris–Harrington, Continuum Hypothesis over ZFC) and are studied, not feared.
- Adding G as an axiom gives a new theory with a new Gödel sentence; incompleteness is not a gap you
  can fill.

## Related
- [[soundness-and-completeness]] (completeness of the logic vs incompleteness of theories),
  [[computability-and-halting-problem]], [[first-order-logic]].

## Sources
Open Logic Part 6 (arithmetization of syntax, representability in Q, the incompleteness theorems, Löb's theorem).

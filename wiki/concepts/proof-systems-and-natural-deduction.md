---
title: Proof systems (natural deduction, sequent calculus, Hilbert systems, resolution)
type: concept
section: "1.5"
level: 300
tags: [natural-deduction, sequent-calculus, hilbert-system, fitch, resolution, tableaux, derivations, inference-rules, cut-elimination, proof-assistants]
sources: [open-logic-project, forall-x-calgary]
summary: The four standard ways to define "derivable" — natural deduction (introduction/elimination rules and subproofs, what proof assistants use), sequent calculus (symmetric rules, cut elimination), Hilbert axiom systems (few rules, many axioms, easy to reason about), and resolution/tableaux (mechanical refutation, what automated provers use) — and why they all define the same consequence relation.
---
# Proof systems

**In one sentence.** A proof system is a finite set of syntactic rules for building derivations;
different systems trade human readability against ease of metatheory or automation, but by
[[soundness-and-completeness]] they prove exactly the valid consequences.

## Natural deduction (Gentzen/Fitch)
Each connective has **introduction** and **elimination** rules: ∧I (from A, B infer A ∧ B), ∧E,
→I (assume A in a subproof, derive B, discharge to get A → B), →E (modus ponens), ¬I/¬E via ⊥,
∨I, ∨E (case analysis), ∀I (prove for an arbitrary fresh variable), ∀E (instantiate), ∃I, ∃E (assume
a witness with a fresh name). Subproofs track assumptions; reductio ad absurdum / excluded middle
distinguish classical from intuitionistic logic (drop them and you get constructive proofs, which
correspond to programs — [[curry-howard-correspondence]]). Lean, Coq, Isabelle, and Agda are
natural-deduction engines with a type theory attached ([[interactive-theorem-proving]]).

## Sequent calculus
Judgments Γ ⇒ Δ ("some formula in Δ follows from all of Γ"), left/right rules per connective, and the
**cut rule** (lemma use). Gentzen's *Hauptsatz*: cut can be eliminated, so every provable sequent has
a proof mentioning only subformulas of the goal — the basis of proof search, consistency proofs, and
interpolation.

## Hilbert (axiomatic) systems
Axiom schemas (e.g. A → (B → A)) plus modus ponens and generalization. Painful to use, easy to prove
things *about* (soundness by a two-line induction; Gödel's incompleteness is stated for such a system).

## Resolution and tableaux (automation)
Convert to clausal form ([[first-order-logic]]); resolution rule: from (A ∨ C) and (¬A ∨ D) infer
(C ∨ D); derive the empty clause to refute. With unification (Robinson 1965) this is complete for FOL
and underlies Prolog (SLD resolution) and modern provers; propositional resolution with unit
propagation and learning is CDCL ([[sat-and-smt-solvers]]). Tableaux systematically try to build a
counter-model and close branches on contradictions.

## Why it matters to programmers
- Type checkers *are* proof checkers; a typing derivation is a natural-deduction proof.
- Understanding which rules discharge assumptions explains why `assert`-based reasoning about code
  needs case splits and why "for arbitrary x" proofs cannot use properties of a specific x.
- Automated reasoning tools (SMT, Datalog, model checkers) trade the expressive power of full FOL for
  decidable fragments.

## Related
- [[first-order-logic]], [[soundness-and-completeness]], [[propositional-logic]], [[proof-techniques]].

## Sources
Open Logic Part 3 chapters on sequent calculus, natural deduction, tableaux, axiomatic deduction; forall x: Calgary Parts 3 and 6.

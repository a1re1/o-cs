---
title: Soundness, completeness, compactness, and Löwenheim–Skolem
type: concept
section: "1.5"
level: 300
tags: [soundness, completeness-theorem, compactness, lowenheim-skolem, henkin-construction, godel-completeness, consequence, derivability, nonstandard-models, expressiveness]
sources: [open-logic-project]
summary: Soundness (whatever is derivable is valid) is a routine induction on derivations; Gödel's completeness theorem (whatever is valid is derivable) is proved by building a model from a maximal consistent set (Henkin); compactness and Löwenheim–Skolem fall out and explain what first-order logic cannot say (finiteness, reachability, "the" natural numbers).
---
# Soundness and completeness

**In one sentence.** For first-order logic, Γ ⊢ φ iff Γ ⊨ φ: proof search and truth-in-all-models
agree, which is what makes automated theorem proving meaningful — but the same theorem implies
strong limits on what first-order axioms can pin down.

## Soundness (⊢ ⇒ ⊨)
Induction on the derivation: each rule preserves truth under every structure and assignment. The only
subtle rules are the quantifier rules with freshness conditions (∀-introduction on a variable that
appears in an undischarged assumption is unsound). Soundness is what you check when you add a rule to a
type system or a verifier: does the rule ever prove something false?

## Completeness (⊨ ⇒ ⊢), Gödel 1929 / Henkin 1949
Contrapositive: if Γ ⊬ φ then Γ ∪ {¬φ} is consistent; extend it to a **maximally consistent** set
(Lindenbaum's lemma) that is **witness-complete** (for each ∃xψ it contains ψ(c) for some new
constant — Henkin constants); read off a structure whose domain is the terms (modulo provable
equality) and where a sentence is true iff it is in the set (the *truth lemma*, by induction on
formulas). This structure satisfies Γ and ¬φ, so Γ ⊭ φ. For propositional logic the same argument
with truth assignments gives completeness of truth-table reasoning.

## Corollaries that matter
- **Compactness**: Γ has a model iff every finite subset does (because derivations are finite).
  Consequences: no first-order sentence set characterizes "finite" structures, "connected" graphs,
  or "reachable" — add constants c ≠ 0, ≠ 1, ≠ 2, … and compactness gives a nonstandard model with an
  "infinite" element. So Peano arithmetic has **nonstandard models**, and transitive closure /
  reachability need fixpoint logic or induction (Datalog, second-order logic).
- **Löwenheim–Skolem**: a countable theory with an infinite model has models of every infinite
  cardinality; downward version yields a countable model of set theory (Skolem's "paradox").
- **Semi-decidability**: valid FOL sentences are recursively enumerable (enumerate proofs) but validity
  is undecidable (Church–Turing) — provers may run forever on non-theorems
  ([[computability-and-halting-problem]]).

## Contrast with incompleteness
Completeness is about the *logic* (every valid consequence is provable); Gödel's *incompleteness* is
about *theories* like arithmetic (some true sentences are not consequences of the axioms). No conflict:
the unprovable Gödel sentence is false in some nonstandard model ([[godel-incompleteness-theorems]]).

## Related
- [[first-order-logic]], [[proof-systems-and-natural-deduction]], [[godel-incompleteness-theorems]],
  [[computability-and-halting-problem]].

## Sources
Open Logic Part 3 "Completeness" (Henkin construction, compactness, Löwenheim–Skolem), Part 4 model theory.

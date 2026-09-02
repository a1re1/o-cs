---
title: forall x: Calgary (Magnus, Button, Thomas-Bolduc, Zach)
type: source
section: "1.5"
level: 100
tags: [logic, propositional-logic, first-order-logic, natural-deduction, truth-tables, symbolization, fitch]
sources: []
authors: [P. D. Magnus, Tim Button, Aaron Thomas-Bolduc, Richard Zach]
year: 2024
institution: University of Calgary / Open Logic Project
url: https://forallx.openlogicproject.org/
license: CC-BY
format: pdf
summary: Free introductory formal logic text — arguments and validity, truth-functional logic with truth tables, first-order logic with identity, symbolizing English, and Fitch-style natural deduction for both, plus soundness, functional completeness and modal logic; comes with solutions and the Carnap proof checker.
---
# forall x: Calgary

## What it is
Level 100 (no prerequisites). Parts: key notions (validity, consequence); truth-functional logic (TFL):
symbolization, truth tables, entailment; natural deduction for TFL (Fitch style); first-order logic
(FOL) with identity: symbolization, interpretations; natural deduction for FOL; advanced topics
(normal forms, functional completeness, soundness proof, modal logic). Exercises with solutions;
Carnap.io checks proofs interactively.

## Key ideas → pages
- Rules of natural deduction (introduction/elimination for each connective and quantifier), and the
  discipline of subproofs — [[proof-systems-and-natural-deduction]].
- Truth-table semantics and entailment for propositional logic — [[propositional-logic]].
- Symbolizing English into FOL: "all A are B" is ∀x(A(x) → B(x)); "some A is B" is ∃x(A(x) ∧ B(x)) —
  the classic mistake is mixing → and ∧ — [[first-order-logic]].

## What it adds
The gentlest route into formal proofs; the same rules drive proof assistants (Lean, Coq) in §5.4/§5.5.

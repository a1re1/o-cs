---
title: The Open Logic Text (Open Logic Project)
type: source
section: "1.5"
level: 300
tags: [logic, first-order-logic, model-theory, proof-systems, completeness, computability, incompleteness, set-theory, natural-deduction, sequent-calculus]
sources: []
authors: [Richard Zach, Aldo Antonelli, Andrew Arana, Jeremy Avigad, others]
year: 2024
institution: Open Logic Project
url: https://openlogicproject.org/
license: CC-BY
format: pdf
summary: A modular, CC-BY graduate-level logic text built from LaTeX source — sets/relations/functions and sizes of sets, propositional and first-order logic (syntax, semantics, models and theories, four proof systems, completeness), model theory, computability (recursive functions, Turing machines), and Gödel's incompleteness theorems — remixable into custom course textbooks.
---
# The Open Logic Text

## What it is
Level 300–400 (upper undergraduate/graduate logic for philosophy, math, and CS). Parts:
1 Sets, relations, functions, size of sets (enumerability, diagonalization, Schröder–Bernstein),
arithmetization, the infinite; 2 Propositional logic; 3 First-order logic (syntax, semantics, models
and theories, proof systems: sequent calculus, natural deduction, tableaux, axiomatic; completeness;
beyond first-order); 4 Model theory (models of arithmetic, interpolation, Lindström's theorem);
5 Computability (recursive functions, computability theory, Turing machines); 6 Incompleteness
(arithmetization of syntax, representability, Gödel's theorems, Löb's theorem); plus set theory,
modal logic, intuitionistic logic, counterfactuals. Everything is a chapter you can include or omit —
the *forall x: Calgary* intro text ([[forall-x-calgary]]) is built from the same project.

## Key ideas → pages
- First-order syntax vs semantics; satisfaction in a structure; logical consequence Γ ⊨ φ vs
  derivability Γ ⊢ φ — [[first-order-logic]].
- Proof systems as different presentations of the same consequence relation; **soundness** (⊢ ⇒ ⊨)
  proved by induction on derivations; **completeness** (⊨ ⇒ ⊢, Gödel 1929) via Henkin's construction of a
  model from a maximal consistent set; **compactness** and Löwenheim–Skolem as corollaries —
  [[soundness-and-completeness]].
- Computability: partial recursive functions = Turing-computable; the halting problem; Rice's theorem
  — [[computability-and-halting-problem]].
- Incompleteness: arithmetize syntax (Gödel numbering), the diagonal/fixed-point lemma, "this sentence
  is unprovable", second theorem (consistency unprovable), Tarski's undefinability of truth —
  [[godel-incompleteness-theorems]].

## What it adds
Rigor and the connections (diagonalization appears in Cantor, halting, and Gödel — one idea, three
theorems) that the undergraduate sources gesture at. Its computability part links directly to §5.1.

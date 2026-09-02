---
title: First-order logic (syntax, semantics, quantifiers, models)
type: concept
section: "1.5"
level: 300
tags: [first-order-logic, predicate-logic, quantifiers, structures, models, satisfaction, logical-consequence, symbolization, prenex-normal-form, skolemization, theories]
sources: [open-logic-project, forall-x-calgary, stanford-cs103]
summary: The language of mathematics and of specifications — terms, predicates, ∀/∃ over a domain — with Tarski's satisfaction semantics, the distinction between consequence (⊨) and derivability (⊢), symbolization rules of thumb, and the normal forms that SAT/SMT solvers and theorem provers use.
---
# First-order logic

**In one sentence.** First-order logic adds variables, functions, predicates, and the quantifiers
∀ and ∃ to [[propositional-logic]], and interprets them in a *structure* (a domain plus meanings for
the symbols), so a sentence is true or false only relative to a structure.

## Syntax
Signature: constants c, function symbols f (arity n), predicate symbols P (arity n), plus = (usually
built in). **Terms**: variables, constants, f(t₁…tₙ). **Atomic formulas**: P(t₁…tₙ), t₁ = t₂.
**Formulas**: closed under ¬, ∧, ∨, →, ∀x, ∃x. Free vs bound variables; a **sentence** has no free
variables. A **theory** is a set of sentences (e.g. Peano arithmetic, ZFC, the theory of groups).

## Semantics (Tarski)
A structure M = (D, interpretation) assigns each constant an element of D, each n-ary function symbol
a function Dⁿ → D, each predicate a relation ⊆ Dⁿ. Satisfaction M ⊨ φ[s] is defined by recursion on
φ with variable assignment s; ∀xφ holds iff φ holds for every assignment of x. **Logical consequence**
Γ ⊨ φ: every structure satisfying all of Γ satisfies φ. **Validity**: true in every structure.
Contrast with **derivability** Γ ⊢ φ in a proof system; the two coincide by
[[soundness-and-completeness]].

## Symbolization rules of thumb (forall x, CS103)
- "All A are B": ∀x (A(x) → B(x)). "Some A is B": ∃x (A(x) ∧ B(x)). Mixing these up is the #1 error
  (∀x (A(x) ∧ B(x)) says everything is an A and a B; ∃x (A(x) → B(x)) is trivially true if anything is not an A).
- Quantifier order: ∀x∃y Loves(x,y) ≠ ∃y∀x Loves(x,y).
- Negation pushes through quantifiers and flips them: ¬∀x φ ≡ ∃x ¬φ.
- "Exactly one": ∃x (P(x) ∧ ∀y (P(y) → y = x)). Counting needs equality.
- Uniqueness, "at least two", functions being injective — all expressible; "finitely many",
  "reachable in some number of steps" (transitive closure) are **not** first-order expressible
  (compactness, [[soundness-and-completeness]]) — which is why Datalog/fixpoint logics exist.

## Normal forms (what solvers use)
- **Prenex form**: all quantifiers in front. **Skolemization**: replace ∃y inside ∀x by a fresh function
  y = f(x); equisatisfiable, not equivalent. Then clausal form (CNF of the matrix) — the input of
  resolution theorem provers (Vampire, E) and, with theories, of SMT solvers ([[sat-and-smt-solvers]]).
- Herbrand's theorem: a universal sentence is unsatisfiable iff some finite set of ground instances is
  propositionally unsatisfiable — the bridge from FOL to SAT.
- Quantifier-free fragments with decidable theories (linear arithmetic, arrays, bit-vectors,
  uninterpreted functions) are where automated verification lives ([[model-checking]]).

## In programming
Specifications and contracts (`forall i < n: a[i] <= a[i+1]`), database queries (relational calculus
is first-order over finite structures; SQL adds aggregation — [[relational-model]]), type systems
(∀ in polymorphic types is second-order — [[type-systems]]), and property-based test generators
express first-order claims and check finite instances.

## Related
- [[propositional-logic]], [[soundness-and-completeness]], [[proof-systems-and-natural-deduction]],
  [[godel-incompleteness-theorems]], [[sets-relations-functions]].

## Sources
Open Logic Part 3 (syntax, semantics, models & theories); forall x: Calgary Parts 4–5; CS103 lectures 2–3.

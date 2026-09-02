---
title: The Curry–Howard correspondence — propositions as types, proofs as programs, constructive logic, dependent types, and proof assistants (Rocq/Coq, Agda, Lean, Idris)
type: concept
section: "5.4"
level: 500
tags: [curry-howard, propositions-as-types, proofs-as-programs, constructive-logic, intuitionistic-logic, natural-deduction, implication-as-function, conjunction-as-product, disjunction-as-sum, false-as-empty-type, negation, law-of-excluded-middle, continuations-and-classical-logic, dependent-types, pi-types, sigma-types, identity-type, martin-lof-type-theory, calculus-of-constructions, inductive-types, universes, totality, termination-checking, proof-assistants, coq, rocq, agda, lean, idris, tactics, proof-irrelevance, extraction, certified-programming, homotopy-type-theory, univalence, cubical, strong-normalization-consistency]
sources: [pierce-tapl-and-pl-theory-texts, pl-theory-seminal-papers]
summary: Curry and Howard noticed that the typing rules of the simply typed λ-calculus are the inference rules of intuitionistic natural deduction — implication is the function type, conjunction the product, disjunction the sum, falsity the empty type, and a proof of a proposition is a program of the corresponding type, with proof normalization as evaluation — which makes strong normalization the same fact as logical consistency and explains why a Turing-complete language is an inconsistent logic; extending to quantifiers gives dependent types (Π-types for ∀, Σ-types for ∃, identity types for equality) and Martin-Löf type theory / the calculus of inductive constructions, in which specifications are types and verified programs are their inhabitants — the foundation of proof assistants (Rocq/Coq, Agda, Lean, Idris) where tactics build terms, inductive types define both data and propositions, totality is enforced by termination checking, and proofs can be extracted to running code (CompCert, seL4's Isabelle cousin, mathlib), while classical logic corresponds to control operators (call/cc) and homotopy type theory reinterprets equality proofs as paths.
---
# The Curry–Howard correspondence

**In one sentence.** A proof is a program and the proposition it proves is its type — so type
checking is proof checking, running is normalizing, and a language whose types are rich
enough can state and verify its own specifications.

## The correspondence (SF ProofObjects; PFPL ch. 12)
| Logic (intuitionistic natural deduction) | Types (typed λ-calculus) |
|---|---|
| proposition P | type P |
| proof of P | term t : P |
| P ⊃ Q (implication) | P → Q (function) |
| P ∧ Q | P × Q (pair) |
| P ∨ Q | P + Q (sum; a proof says *which* side — constructive) |
| ⊤, ⊥ | unit, empty type (Void; `absurd : ⊥ → A`) |
| ¬P | P → ⊥ |
| modus ponens | application |
| ⊃-introduction (assume P, derive Q) | λ-abstraction |
| ∀x:A. P(x) | Π(x:A). P(x) dependent function |
| ∃x:A. P(x) | Σ(x:A). P(x) dependent pair (witness + proof) |
| a = b | identity type Id_A(a, b) with refl |
| proof normalization (cut elimination) | β-reduction |
Consequences: **consistency = strong normalization** (a closed term of type ⊥ cannot exist if
every term normalizes to a canonical form, and ⊥ has none) — so the simply typed calculus
and System F are consistent logics, and adding general recursion (`fix : (A→A)→A` proves
everything) makes the "logic" trivial: **a Turing-complete language is an inconsistent
logic**, which is why proof assistants demand totality. Constructivity: a proof of ∃ carries a
witness; **excluded middle** P ∨ ¬P has no inhabitant in general (it would decide every
proposition — [[decidability-and-reductions]]); Griffin (1990): classical logic corresponds to
**control operators** — call/cc has type ((P → Q) → P) → P (Peirce's law), so continuations
are classical proofs ([[closures-and-environment-model]]). Linear logic ↔ linear types
([[type-systems]]); modal logics ↔ staged computation/effects; the "Propositions as Types"
essay (Wadler 2015) tells the history (Brouwer, Heyting, Gentzen, Curry, Howard, de Bruijn,
Martin-Löf).

## Dependent types (ATTAPL ch. 2; PFPL; Martin-Löf 1984)
Types may depend on values: `Vec A n` (vectors of length n), `append : Vec A m → Vec A n →
Vec A (m + n)` — the type is the specification. **Π-types** generalize → and ∀; **Σ-types**
generalize × and ∃; **inductive types** with dependent elimination (induction principles as
recursors — [[induction]], [[fold-and-structural-recursion]]); **universes** Type₀ : Type₁ : …
to avoid Girard's paradox; **identity types** and the J eliminator; propositions as a
universe `Prop` (Coq, proof-irrelevant) or just types (Agda). Systems: Martin-Löf type theory,
the Calculus of (Inductive) Constructions (Coquand & Huet; Rocq), Lean's CIC with quotients,
Agda's. Costs: type checking needs evaluation (decidable only because of totality —
**termination checking** by structural recursion or well-founded measures; **positivity** for
inductive types), equality is intensional (`n + 0 = n` needs a proof; the setoid hell that
HoTT/cubical address), annotations and proof burden.

## Proof assistants in practice
- **Rocq/Coq** (renamed 2025): Gallina terms, **tactics** (`intros`, `induction`, `rewrite`,
  `auto`, `omega/lia`, Ltac/Ltac2 automation) build proof terms checked by a small kernel
  (de Bruijn criterion); **extraction** to OCaml/Haskell. Landmarks: **CompCert** (verified C
  compiler — [[compilers-overview]]), the four-color theorem, Feit–Thompson, Verified
  Software Toolchain, Fiat-Crypto (verified elliptic-curve code in BoringSSL —
  [[public-key-cryptography]]), Software Foundations as the textbook.
- **Isabelle/HOL** (classical higher-order logic, Sledgehammer automation): seL4 microkernel
  ([[os-kernels-and-virtualization]]), CakeML.
- **Lean 4**: a programming language and prover; **mathlib** (the largest formal math library),
  Liquid Tensor Experiment, growing use with LLM-generated proofs.
- **Agda** (dependently typed programming, Unicode, no tactics), **Idris 2** (quantitative
  types — linearity + dependency for real programs), F* (refinement + effects; HACL* verified
  crypto in Firefox/Linux), Dafny/Why3 (auto-active verification via SMT —
  [[program-verification]]).
Engineering lessons: proofs are code (maintenance, refactoring, CI); automation vs trust
(small kernels); the specification is the weak point (what did you prove?); costs of ~10×
the code size, dropping with automation.

## Homotopy type theory (HoTT book 2013)
Read types as spaces, terms as points, proofs of a = b as **paths**; higher inductive types
(circle, quotients); Voevodsky's **univalence** — equivalent types are equal (A ≃ B) ≃ (A = B)
— which validates transporting proofs along isomorphisms; cubical type theory (Cubical Agda)
computes with it. Foundations for mathematics and a cleaner account of equality and
quotients in programming.

## Pitfalls
- Reading Curry–Howard as "all programs are proofs of something interesting" — most are
  proofs of trivial propositions (Int → Int); the correspondence bites when types are precise.
- Adding axioms (excluded middle, functional extensionality, UIP) without checking
  consistency and computational behaviour.
- Proving the wrong theorem (weak spec), or trusting unverified extraction/compilation.
- Fighting the termination checker with `unsafe`/`Admitted` and forgetting to remove them.

## Related
- [[type-systems]], [[lambda-calculus]], [[polymorphism-and-type-inference]],
  [[program-verification]], [[propositional-logic]], [[first-order-logic]], [[proof-techniques]],
  [[induction]], [[decidability-and-reductions]], [[closures-and-environment-model]].

## Sources
Howard 1980; Wadler "Propositions as Types" 2015; Martin-Löf 1984; Coquand & Huet 1988; SF ProofObjects/IndPrinciples; PFPL ch. 12–15; ATTAPL ch. 2; CPDT ch. 1–4; HoTT book ch. 1–2; Griffin 1990.

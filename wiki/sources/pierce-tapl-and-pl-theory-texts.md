---
title: Types and Programming Languages (Pierce), Software Foundations (Pierce et al. — free, Rocq/Coq), Practical Foundations for Programming Languages (Harper — free draft), PLAI (Krishnamurthi — free), EOPL (Friedman & Wand), Van Roy & Haridi's CTM, Chlipala's CPDT (free), the HoTT book (free), and CMU 15-312/15-814, Penn CIS500, Brown CS1730, MIT 6.820, Stanford CS242, Cornell CS4110, OPLSS
type: source
section: "5.4"
level: 400
tags: [tapl, pierce, software-foundations, rocq, coq, pfpl, harper, plai, krishnamurthi, eopl, friedman-wand, ctm, van-roy, cpdt, chlipala, hott-book, homotopy-type-theory, 15-312, 15-814, cis500, cs1730, 6-820, cs242, cs4110, oplss, programming-language-theory]
sources: []
authors: [Benjamin Pierce, Robert Harper, Shriram Krishnamurthi, Daniel Friedman, Mitchell Wand, Peter Van Roy, Seif Haridi, Adam Chlipala]
year: 2002
institution: Penn / CMU / Brown
url: https://softwarefoundations.cis.upenn.edu/
license: mixed (Software Foundations, PFPL draft, PLAI, CPDT, HoTT free)
format: html
summary: TAPL is the standard type-systems text — untyped and simply typed lambda calculus, type soundness via progress and preservation, references and exceptions, subtyping, recursive types, polymorphism (System F, existential types, type reconstruction/Hindley–Milner), bounded quantification, higher-order systems (F-omega, kinds); Software Foundations (free) teaches the same material inside the Rocq (formerly Coq) proof assistant — Logical Foundations (functional programming, inductive proofs, polymorphism, tactics, logic, inductively defined propositions), Programming Language Foundations (Imp, Hoare logic, small-step semantics, STLC, type soundness, subtyping, references), Verified Functional Algorithms, QuickChick, Verifiable C, Separation Logic; Harper's PFPL (free draft) builds languages from judgments and rules — statics/dynamics, function/product/sum types, inductive/coinductive types, System F and parametricity, recursive types, dynamic typing, subtyping, dispatch, control (exceptions, continuations), state, laziness, parallelism, concurrency, modules, and equational reasoning — with the thesis that types are the central organizing principle; PLAI (free) teaches PL by writing interpreters in Racket/Plait (desugaring, environments, closures, mutation, continuations, garbage collection, objects, types); EOPL likewise via a sequence of interpreters; CTM by a kernel language grown with concepts (declarative, lazy, message-passing, stateful, OO, constraint); CPDT is Coq for real proofs with dependent types; the HoTT book is the univalent foundations; 15-312/15-814 (Harper), CIS500 (SF), CS1730 (PLAI), 6.820, CS242, CS4110 and the OPLSS lectures are the courses.
---
# PL theory texts and courses

## What they are
- **TAPL** (Pierce 2002): I untyped systems (untyped arithmetic, the untyped λ-calculus,
  nameless representation — de Bruijn indices, ML implementation); II simple types (typed
  arithmetic, simply typed λ-calculus, extensions — base types, unit, sequencing, ascription,
  let, pairs, records, sums, variants, general recursion, lists; normalization; references;
  exceptions); III subtyping (subtyping, metatheory of subtyping, imperative objects,
  featherweight Java case study); IV recursive types (iso/equi-recursive, metatheory); V
  polymorphism (type reconstruction — constraint-based typing, unification, let-polymorphism;
  universal types — System F, erasure, parametricity; existential types — ADTs and modules;
  bounded quantification — F<:; case study on imperative objects); VI higher-order systems
  (type operators and kinding — F-omega, higher-order subtyping, higher-order polymorphism).
  *Advanced Topics in TAPL* (2005) adds substructural (linear) types, dependent types, effect
  types, type-based program analysis, ML modules, type definitions, and the metatheory of
  Featherweight Java/proof-carrying code.
- **Software Foundations** (Pierce et al., Rocq): vol. 1 Logical Foundations — functional
  programming in Rocq, induction, lists, polymorphism, tactics, logic, inductive propositions,
  total and partial maps, the Imp language and its evaluation, program equivalence; vol. 2
  Programming Language Foundations — Hoare logic (I, II), small-step semantics, type systems
  (typed arithmetic), simply typed λ-calculus and its properties, MoreStlc, subtyping,
  records, references, normalization, Curry–Howard; vol. 3 Verified Functional Algorithms; vol.
  4 QuickChick (property-based testing); vol. 5 Verifiable C; vol. 6 Separation Logic
  Foundations.
- **PFPL** (Harper, 2nd ed. 2016): judgments and rules (abstract syntax, inductive
  definitions, hypothetical/general judgments); statics and dynamics (type safety); total
  functions (T, primitive recursion); finite data (products, sums); types and propositions
  (constructive logic, classical logic); infinite data (inductive/coinductive); variable types
  (System F, abstract types, higher kinds); partiality and recursive types (PCF, FPC);
  dynamic types (the untyped λ-calculus as a uni-typed language, hybrid typing); subtyping;
  dynamic dispatch and inheritance; control flow (exceptions, continuations); symbolic
  computation (symbols, fluid binding); mutable state (Modernized Algol, assignable references);
  parallelism (nested data parallelism, futures); concurrency and distribution (process
  calculus, concurrent Algol, distributed Algol); modularity (type abstraction, hierarchy,
  parameterization); equational reasoning (equational reasoning for T and PCF, parametricity,
  representation independence).
- **PLAI** (Krishnamurthi, free): interpreters for a growing language — arithmetic,
  functions, desugaring, environments vs substitution, closures, mutation and boxes,
  recursion, objects, memory management/GC, representation choices, laziness, continuations
  (web programming, generators), type checking and inference, checking vs typing, safety.
- **EOPL** (3rd ed.): inductive data, data abstraction, expressions, state, continuation-
  passing interpreters, CPS transformation, types and type inference, modules, objects.
- **CTM** (Van Roy & Haridi): declarative computation model → declarative concurrency →
  message passing → explicit state → object orientation → shared-state concurrency →
  relational programming (Oz); the "concepts, not languages" map.
- **CPDT** (Chlipala, free): Coq proof engineering with dependent types, reflection,
  automation. **HoTT book** (2013): types as spaces, univalence, higher inductive types.

## Key ideas → pages
[[lambda-calculus]], [[operational-and-denotational-semantics]], [[type-systems]],
[[polymorphism-and-type-inference]], [[curry-howard-correspondence]],
[[closures-and-environment-model]], [[program-verification]].

## What they add
TAPL for the definitions and proofs, SF for doing them in a proof assistant, PFPL for the
uncompromising "types organize everything" view, PLAI/EOPL for learning by building
interpreters.

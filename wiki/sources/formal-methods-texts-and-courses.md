---
title: Formal methods texts and courses — Clarke, Grumberg & Peled's Model Checking, Baier & Katoen's Principles of Model Checking, Lamport's Specifying Systems (TLA+, free) and video course, Nipkow & Klein's Concrete Semantics (Isabelle, free), The Little Prover, Theorem Proving in Lean 4, Dafny tutorials, MIT 6.826, CMU 15-414, Stanford CS357
type: source
section: "5.5"
level: 400
tags: [model-checking-book, clarke-grumberg-peled, baier-katoen, principles-of-model-checking, specifying-systems, lamport, tla-plus, tlc, pluscal, concrete-semantics, nipkow-klein, isabelle, little-prover, theorem-proving-in-lean, lean-4, dafny, 6-826, lampson, 15-414, bug-catching, cs357, formal-methods-course]
sources: []
authors: [Edmund Clarke, Orna Grumberg, Doron Peled, Christel Baier, Joost-Pieter Katoen, Leslie Lamport, Tobias Nipkow, Gerwin Klein, Daniel Friedman, Carl Eastlund, Butler Lampson]
year: 2002
institution: various
url: https://lamport.azurewebsites.net/tla/book.html
license: mixed (Specifying Systems, Concrete Semantics, Lean docs free)
format: pdf
summary: Clarke, Grumberg & Peled (2nd ed. 2018 with Henzinger, Veith, Bloem's handbook) and Baier & Katoen are the model-checking texts — Kripke structures, LTL and CTL, automata-theoretic checking (Büchi), symbolic checking with BDDs, bounded model checking with SAT, partial-order reduction, abstraction and CEGAR, timed and probabilistic models; Lamport's Specifying Systems (free) teaches TLA+ by specifying a clock, an asynchronous interface, a FIFO, a caching memory (with linearizability and a write-through cache), then advice on what to specify and "the grain of atomicity", liveness and fairness, real time, composition, and the TLC model checker, with the free video course and PlusCal for programmers; Concrete Semantics (free) teaches Isabelle/HOL by formalizing IMP's semantics, type systems, compilers, and program analyses (abstract interpretation included); The Little Prover teaches induction proofs in the Little-Schemer style; Theorem Proving in Lean 4 is the official Lean tutorial; the Dafny tutorials cover auto-active verification; and 6.826 (Lampson — specs and refinement for systems), 15-414 (bug catching with model checking and SAT/SMT) and CS357 (advanced topics in formal methods) are the courses.
---
# Formal methods texts and courses

## What they are
- **Clarke, Grumberg & Peled, Model Checking**: modeling systems (Kripke structures, first-
  order representations, fairness), temporal logics (CTL*, CTL, LTL), model checking
  algorithms (explicit-state CTL, LTL via tableau/automata), BDDs and symbolic model
  checking (fixpoint characterizations, SMV), model checking for the μ-calculus, partial
  order reduction, equivalences and preorders (bisimulation, simulation), compositional
  reasoning, abstraction (cone of influence, CEGAR), symmetry, infinite families, timed
  systems, and case studies (the IEEE Futurebus+ bug). The 2018 *Handbook of Model Checking*
  updates it (SAT/SMT-based, IC3/PDR, software model checking).
- **Baier & Katoen, Principles of Model Checking** (2008): transition systems, linear-time
  properties (safety, liveness, fairness), regular properties and NBAs, LTL (semantics,
  automata translation, complexity), CTL (algorithms, CTL vs LTL), equivalences and
  abstraction, partial-order reduction, timed automata (UPPAAL), probabilistic systems
  (Markov chains, MDPs, PCTL — PRISM). The best textbook treatment of the theory.
- **Lamport, Specifying Systems** (2002, free): I getting started — a little simple math
  (propositional/predicate logic, sets), specifying a simple clock (behaviors as sequences
  of states; Init ∧ □[Next]_v), an asynchronous interface, a FIFO (instantiation, hiding with
  ∃), a caching memory (functions, a linearizable memory, a write-through cache, invariance,
  proving implementation via refinement mappings), some more math (CHOOSE, recursion),
  writing a specification: some advice (why and what to specify, **the grain of atomicity**,
  when and how); II advanced — liveness and fairness (weak/strong fairness, machine closure),
  real time, composing specifications, open systems; III tools — the Syntactic Analyzer,
  TLATeX, **TLC** (the model checker; how it works, finite models, symmetry); IV the
  language (operators, modules, proofs). Companion: **PlusCal** (algorithm language that
  translates to TLA+), the TLA+ video course, TLAPS proof system, Apalache (SMT-based).
- **Nipkow & Klein, Concrete Semantics** (free): Isabelle/HOL programming and proving; IMP —
  big-step, small-step, equivalence; a compiler and its correctness; a type system and
  soundness; program analysis — definite initialization, constant folding, live-variable
  analysis; **abstract interpretation** (a verified abstract interpreter); Hoare logic (partial
  and total correctness, VCG, soundness and completeness).
- **The Little Prover** (Friedman & Eastlund): induction proofs about recursive functions in
  the Q&A style, using the J-Bob prover (ACL2 flavour).
- **Theorem Proving in Lean 4**; Mathematics in Lean; the Lean Functional Programming book.
- **Dafny** (Leino): tutorials and *Program Proofs* (2023) — pre/postconditions, loop
  invariants, termination measures, ghost state, verified data structures.
- Courses: **6.826** (Lampson: specifications, abstraction functions, refinement, for
  distributed systems and file systems — the "Handouts" are a classic), **15-414** (model
  checking, SAT/SMT, symbolic execution, Why3), **CS357** (advanced formal methods).

## Key ideas → pages
[[program-verification]], [[model-checking]], [[sat-and-smt-solvers]], [[abstract-interpretation]],
[[curry-howard-correspondence]], [[operational-and-denotational-semantics]].

## What they add
Baier & Katoen for the theory, Specifying Systems for the practice that industry actually
adopted, Concrete Semantics for mechanizing the whole §5.4–5.5 story in one book.

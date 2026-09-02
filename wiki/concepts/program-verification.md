---
title: Program verification — Hoare logic, weakest preconditions, loop invariants and termination, separation logic and the frame rule, auto-active verifiers (Dafny, Why3, Boogie), interactive proof (CompCert, seL4), refinement, and what "verified" buys
type: concept
section: "5.5"
level: 400
tags: [program-verification, hoare-logic, hoare-triples, preconditions, postconditions, partial-correctness, total-correctness, loop-invariants, termination, variants, ranking-functions, weakest-precondition, dijkstra, predicate-transformers, verification-conditions, vcg, separation-logic, frame-rule, ownership, heap, reynolds, ohearn, dafny, why3, boogie, viper, auto-active, ghost-state, interactive-theorem-proving, isabelle, coq, refinement, abstraction-function, simulation, compcert, sel4, trusted-computing-base, specification, design-by-contract, assertions, verified-software, iris, concurrent-separation-logic, rustbelt]
sources: [formal-methods-texts-and-courses, formal-methods-seminal-papers, pl-theory-seminal-papers]
summary: Verification proves a program meets a specification for all inputs: Hoare logic states {P} C {Q} and gives a rule per construct — the while rule needs a loop invariant, total correctness adds a decreasing variant — and Dijkstra's weakest-precondition calculus mechanizes it into verification conditions discharged by SMT solvers (the auto-active style of Dafny, Why3/Boogie, Viper, Frama-C: the programmer writes contracts, invariants and ghost state, the tool checks); separation logic (Reynolds, O'Hearn) makes heap programs tractable with the separating conjunction and the frame rule (a proof about part of the heap holds in any larger heap), scaling to concurrent code (Iris, RustBelt) and industrial bug-finding (Infer); interactive proof assistants carry the largest results — CompCert's semantics-preserving compiler and seL4's kernel refined from spec to C — by refinement (an abstraction function from concrete to abstract states, simulation of every step); the payoff is proportional to the specification's precision and the size of the trusted computing base (spec, checker, compiler, hardware), and the cost, from contracts on critical modules to full functional correctness, spans two orders of magnitude.
---
# Program verification

**In one sentence.** State what the program must do as a logical formula, then show — by
hand, by SMT, or in a proof assistant — that every execution satisfies it; the hard parts
are the invariants nobody wrote down and the specification nobody questioned.

## Hoare logic (Hoare 1969; SF Hoare; Concrete Semantics ch. 12)
**Triple** {P} C {Q}: if P holds before C and C terminates, Q holds after (**partial
correctness**); **total** correctness [P] C [Q] adds termination. Rules: assignment
{Q[e/x]} x := e {Q} (backwards!), sequencing, conditional, consequence (strengthen P, weaken
Q), and **while**: {I ∧ b} C {I} ⊢ {I} while b do C {I ∧ ¬b} — the loop **invariant** I is the
creative step ([[invariant-principle]]); termination by a **variant**/ranking function
decreasing in a well-founded order each iteration. Soundness w.r.t. operational semantics
and (relative) completeness (Cook 1978) are theorems ([[operational-and-denotational-semantics]]).
**Weakest preconditions** (Dijkstra 1975): wp(C, Q) — the predicate transformer computing the
weakest P; wp(x := e, Q) = Q[e/x]; wp(C₁; C₂, Q) = wp(C₁, wp(C₂, Q)); loops need the invariant
supplied; then verification = proving P ⇒ wp(C, Q). A **verification-condition generator**
turns an annotated program into formulas for an SMT solver ([[sat-and-smt-solvers]]) —
the architecture of Boogie, Why3, Dafny, Frama-C/WP, SPARK, JML/OpenJML, and of
[[design-by-contract]]'s runtime-checked cousin (Eiffel, `assert`). Program logics for
exceptions, procedures (modular verification via contracts), and object invariants follow.

## Separation logic (Reynolds 2002; O'Hearn)
Heap-manipulating programs break Hoare logic's assignment rule (aliasing). Assertions
describe heaps: `emp`, `x ↦ v`, and the **separating conjunction** P ∗ Q (the heap splits
into disjoint parts satisfying P and Q); the **frame rule** {P} C {Q} ⊢ {P ∗ R} C {Q ∗ R}
(C doesn't touch R's heap) enables **local reasoning** and modular specs of data structures
(`list(x)`, trees, inductive predicates); ownership transfer for concurrency (**concurrent
separation logic**, O'Hearn/Brookes: locks own heap; Iris (Jung et al.) generalizes with
ghost state, invariants and step-indexing, and **RustBelt** proved Rust's type system and
unsafe libraries sound in it — [[ownership-and-borrowing]] is separation logic as a type
system). Tools: VeriFast, Viper, VST (Coq, for C), Iris/Coq, and **Infer** (Facebook: bi-
abduction infers specs automatically at scale for memory and resource bugs). Symbolic
execution (KLEE, [[fuzzing]]'s cousin) explores paths with an SMT solver — verification's
bug-finding twin.

## Auto-active verification (Dafny, Why3, Boogie, F*)
Write `requires`/`ensures`/`invariant`/`decreases` plus **ghost** variables and lemmas; the
tool generates VCs and calls Z3; the loop is "add an invariant/assertion until it goes
through". Idioms: recursive functions as specs, `calc` proofs, triggers for quantifiers,
bounded quantifiers to help the solver, termination measures. Successes: IronFleet/IronClad
(verified distributed systems in Dafny — Paxos with liveness), AWS (Cedar policy language in
Lean/Dafny, s2n-tls proofs), Microsoft's Everest/HACL* (F* — verified TLS crypto in Firefox and
Linux), SPARK Ada in avionics, Frama-C in rail/nuclear. Costs: ~2–10× the code in
annotations; brittleness of SMT (timeouts, "verified yesterday"); spec/impl coupling.

## Interactive proof and refinement (CompCert; seL4; 6.826)
When automation runs out: Coq/Rocq, Isabelle/HOL, Lean, HOL4, ACL2 ([[curry-howard-correspondence]]).
**Refinement**: specify an abstract state machine; show the implementation **simulates** it
via an abstraction function/relation (Lampson's 6.826 method; Abadi–Lamport refinement
mappings in TLA+ — [[model-checking]]); layers compose (seL4: abstract spec ← executable
Haskell spec ← C ← binary; CertiKOS: dozens of layers). **CompCert** (Leroy 2009): each of ~20
passes preserves the observable behaviour of the source (semantic preservation proved per
pass; Csmith found no bugs in verified parts); **seL4** (Klein 2009): 8,700 lines of C,
~200k lines of Isabelle, ~20 person-years, later proofs of integrity/confidentiality and
worst-case execution time ([[os-kernels-and-virtualization]], [[real-time-scheduling]]);
**CakeML** (verified ML compiler down to machine code), **Fiat-Crypto** (verified field
arithmetic in BoringSSL), **Verified Software Toolchain** (C programs with VST + CompCert —
end-to-end). Proof engineering: automation (Sledgehammer, tactics), proof maintenance,
extraction.

## What "verified" means
A proof relates a **specification** to an **implementation** under a **model** of the
environment, checked by a **trusted computing base** (the spec itself, the proof checker's
kernel, the compiler unless verified, the hardware model, the unverified boundary code).
Failures come from the spec (wrong or weak — "we proved the sorting routine returns a sorted
list" but not a permutation), from the model (timing side channels, hardware bugs), and from
the TCB. Verification complements testing ([[unit-testing]],
[[property-based-testing]]) and does not replace review of requirements. Levels of
assurance: types → contracts and runtime assertions → auto-active proofs of key properties
(memory safety, absence of panics, functional correctness of core modules) → full functional
correctness → end-to-end refinement.

## Pitfalls
- Loop invariants that are true but too weak (not inductive); missing termination measures.
- Specs that restate the code; forgetting the frame (what must *not* change).
- Trusting timeouts as "no counterexample"; brittle SMT proofs in CI.
- Verifying against an idealized model (no integer overflow, infinite memory — check the
  language semantics: [[undefined-behavior]]).
- Assuming a verified component removes the need to verify its integration.

## Related
- [[invariant-principle]], [[model-checking]], [[sat-and-smt-solvers]], [[abstract-interpretation]],
  [[curry-howard-correspondence]], [[operational-and-denotational-semantics]], [[type-systems]],
  [[ownership-and-borrowing]], [[compilers-overview]], [[os-kernels-and-virtualization]],
  [[design-by-contract]], [[property-based-testing]].

## Sources
Hoare 1969; Dijkstra 1975; Reynolds 2002; O'Hearn "Separation Logic" (CACM 2019); Leroy 2009; Klein et al. 2009; SF Hoare/Hoare2; Concrete Semantics ch. 12; Leino, *Program Proofs*; Jung et al. "Iris from the ground up" 2018; Hawblitzel et al. "IronFleet" 2015; 6.826 handouts.

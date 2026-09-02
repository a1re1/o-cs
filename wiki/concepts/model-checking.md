---
title: Model checking — Kripke structures, LTL and CTL, safety vs liveness, explicit-state and symbolic (BDD) checking, bounded model checking and IC3, abstraction and CEGAR, TLA+/TLC and PlusCal, Spin, Alloy, and how industry uses it
type: concept
section: "5.5"
level: 400
tags: [model-checking, kripke-structure, transition-system, state-space, temporal-logic, ltl, ctl, ctl-star, safety, liveness, fairness, buchi-automata, automata-theoretic, explicit-state, state-explosion, partial-order-reduction, symmetry-reduction, symbolic-model-checking, bdd, fixpoint, mu-calculus, bounded-model-checking, k-induction, ic3, pdr, abstraction, cegar, predicate-abstraction, software-model-checking, tla-plus, tlc, pluscal, refinement-mapping, spin, promela, alloy, small-scope-hypothesis, nusmv, uppaal, prism, probabilistic-model-checking, timed-automata, counterexamples, aws-formal-methods, specification, design-verification]
sources: [formal-methods-texts-and-courses, formal-methods-seminal-papers]
summary: Model checking (Clarke & Emerson, Queille & Sifakis 1981) states a property in temporal logic — LTL over paths (□ always, ◇ eventually, ○ next, U until: safety "nothing bad" vs liveness "something good", with fairness assumptions) or CTL over the branching tree (AG, EF, AF …) — and decides it algorithmically over a finite-state model, producing a counterexample trace when it fails; the algorithms are explicit-state graph search (Spin, TLC) with partial-order and symmetry reduction against state explosion, symbolic fixpoint computation on BDDs (SMV, hardware), SAT-based bounded model checking (unroll k steps; k-induction and IC3/PDR for unbounded proofs), and abstraction with counterexample-guided refinement (SLAM/BLAST for device drivers, predicate abstraction, software model checkers like CBMC), plus timed (UPPAAL) and probabilistic (PRISM) variants; in practice engineers write designs in TLA+ (behaviors as state sequences, Init ∧ □[Next]_v, refinement mappings, PlusCal for algorithms) or Alloy (relational logic with small-scope analysis) and let TLC/the analyzer find the 35-step interleaving that review and testing never would — which is how AWS, MongoDB, CockroachDB and Intel use it — while proofs of liveness and of code-level correspondence remain the hard part.
---
# Model checking

**In one sentence.** Write the design as a state machine and the requirement as a temporal
formula; let a program enumerate or symbolically cover every reachable state and hand you
the exact trace that breaks it — the one your intuition rated "impossible".

## Models and properties (Baier & Katoen ch. 2–6)
**Kripke structure / transition system**: states labelled with atomic propositions, initial
states, transitions; behaviours = infinite paths. Concurrency modelled by interleaving —
the choice of **grain of atomicity** (Lamport) decides what interleavings exist and is the
most common modelling error. Properties over paths: **safety** ("nothing bad ever happens";
violated by a finite prefix — mutual exclusion, no deadlock, invariants) vs **liveness**
("something good eventually happens"; needs infinite counterexamples — every request served,
termination); **fairness** assumptions (weak: a continuously enabled action eventually
happens; strong: infinitely often enabled ⇒ infinitely often taken) exclude unrealistic
starvation. **LTL**: □φ, ◇φ, ○φ, φ U ψ over each path from the initial states; **CTL**: path
quantifiers A/E on temporal operators (AG safe, AF done, EF reachable, AG(req → AF grant));
**CTL\*** subsumes both (LTL and CTL are incomparable: fairness needs LTL; "always possible
to reset" AG EF reset needs CTL). μ-calculus underlies them all. Equivalences (bisimulation
preserves CTL*, trace equivalence preserves LTL — [[operational-and-denotational-semantics]]).

## Algorithms (Clarke et al. ch. 4–6, 9; Baier & Katoen ch. 4–7)
- **Explicit-state**: CTL by labelling states bottom-up with fixpoints (EF p = μZ. p ∨ EX Z) —
  O(|M|·|φ|); LTL via the **automata-theoretic** approach (Vardi–Wolper): translate ¬φ to a
  Büchi automaton, take the product with the model, search for an accepting cycle (nested
  DFS) — PSPACE-complete in |φ| ([[complexity-classes]], [[finite-automata-and-regular-languages]]);
  Spin/TLC do this with hashing, bitstate hashing, and **partial-order reduction** (don't
  explore interleavings of independent actions) and **symmetry reduction**.
- **Symbolic** (McMillan 1992): represent state sets and the transition relation as **BDDs**
  ([[sat-and-smt-solvers]]) and compute fixpoints with image/pre-image operations — 10²⁰
  states for hardware (SMV/NuSMV, Cadence/Synopsys tools). Variable ordering is everything.
- **Bounded model checking** (Biere 1999): ∃ path of length ≤ k violating φ as a SAT/SMT
  formula; complete for safety up to the diameter; **k-induction** and **IC3/PDR** (Bradley
  2011: incrementally strengthen inductive invariants from counterexamples-to-induction)
  give unbounded proofs and dominate hardware verification; CBMC/ESBMC/Kind 2 for software
  and Lustre.
- **Abstraction**: cone-of-influence, **predicate abstraction** + **CEGAR** (Clarke et al.
  2000): abstract, check, if the counterexample is spurious refine with new predicates —
  SLAM (Microsoft's Static Driver Verifier), BLAST, CPAchecker; software model checking via
  interpolants and lazy abstraction ([[abstract-interpretation]] is the semantic framework).
- **Timed** automata with clock zones (UPPAAL, [[real-time-scheduling]] protocols);
  **probabilistic** (PRISM/Storm — Markov chains, MDPs, PCTL: "probability of failure within
  10 steps ≤ 10⁻⁹" — [[markov-chains]]); **stateless/systematic concurrency testing** (CHESS,
  Jepsen-style, deterministic simulation) as model checking of implementations.

## TLA+ and Alloy in practice (Lamport; Jackson; Newcombe et al. 2015)
**TLA+**: a specification is a temporal formula Init ∧ □[Next]_vars ∧ Fairness over
behaviours (sequences of states); state = assignment of values to variables; Next is a
disjunction of actions written in ordinary set theory and predicate logic (no types — TLC
checks type invariants); **refinement mappings** show a lower-level spec implements a higher
one (∃ hidden variables); **PlusCal** gives algorithm-style syntax; **TLC** explores finite
instances (bounded sets, symmetry); TLAPS proves; Apalache uses SMT. AWS: engineers with no
formal background specified S3, DynamoDB, EBS, a lock manager; found design bugs (a 35-step
trace in DynamoDB's replication), used specs as precise documentation and to reason about
optimizations; TLA+ chosen for expressiveness, simple math, tools; liveness and code
correspondence were the limits. Also: MongoDB (Raft variants), CockroachDB, Azure Cosmos DB,
Intel, XBox 360 memory (a cache-coherence bug found before tapeout). **Alloy**: relational
logic (sets, relations, join, transitive closure), signatures and facts, the **small-scope
hypothesis** — check all instances up to size 5–7 with a SAT solver (Kodkod); ideal for data
models, access control, protocols; Alloy 6 adds temporal operators. **Spin/Promela** for
protocols; **P** (Microsoft/AWS) for event-driven systems with systematic testing.

## Using it well
Model the *design*, not the code: a few hundred lines capturing the essential concurrency
and failure cases; choose the grain of atomicity honestly (network delays, crashes, retries
— [[distributed-systems-basics]]); check invariants first (fast, most bugs), then liveness;
keep instances small (2–3 nodes, 2 keys) — bugs are small ([[replication-and-partitioning]]
protocols are the sweet spot); treat the spec as living documentation and re-check on every
design change; connect to code by conformance testing (trace validation against the spec,
model-based test generation) when full refinement proofs are out of budget
([[program-verification]]).

## Pitfalls
- State explosion from over-detailed models; modelling every message field.
- Checking only what you expect to fail; forgetting fairness (spurious liveness failures) or
  adding fairness the system doesn't have (masking real bugs).
- Believing a finite-instance check proves the general case; believing the code matches the
  model.
- Atomicity too coarse (hides races) or too fine (unrealistic interleavings).

## Related
- [[program-verification]], [[sat-and-smt-solvers]], [[abstract-interpretation]],
  [[finite-automata-and-regular-languages]], [[distributed-systems-basics]], [[consensus-paxos-raft]],
  [[cyber-physical-systems-and-models-of-computation]], [[markov-chains]], [[complexity-classes]].

## Sources
Clarke & Emerson 1981; Queille & Sifakis 1982; Vardi & Wolper 1986; Bryant 1986; McMillan 1992; Biere et al. 1999; Clarke et al. CEGAR 2000; Bradley 2011; Lamport, *Specifying Systems* ch. 2–8 (ToC read); Newcombe et al. 2015 (introduction read); Jackson, *Software Abstractions*; Baier & Katoen ch. 2–7; Holzmann, *The Spin Model Checker*.

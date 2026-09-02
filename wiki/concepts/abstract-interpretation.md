---
title: Abstract interpretation — concrete and abstract semantics, lattices and Galois connections, fixpoints, widening and narrowing, classic domains (signs, intervals, octagons, polyhedra), soundness, and industrial static analyzers (Astrée, Infer, Frama-C)
type: concept
section: "5.5"
level: 500
tags: [abstract-interpretation, cousot, static-analysis, soundness, over-approximation, concrete-semantics, collecting-semantics, abstract-domain, lattice, complete-lattice, partial-order, join, meet, galois-connection, abstraction-function, concretization-function, best-transformer, fixpoint, kleene-iteration, monotone-framework, widening, narrowing, convergence, signs-domain, intervals, congruences, octagons, polyhedra, relational-domains, non-relational, shape-analysis, points-to, numerical-abstract-domains, reduced-product, astree, frama-c, infer, sparrow, clang-static-analyzer, false-positives, precision-vs-cost, dataflow-analysis, type-inference-as-abstract-interpretation, rice-theorem]
sources: [formal-methods-texts-and-courses, formal-methods-seminal-papers]
summary: Abstract interpretation (Cousot & Cousot 1977) is the theory of sound approximation: the concrete (collecting) semantics computes the exact set of reachable states as a least fixpoint over a lattice, which is uncomputable (Rice), so one chooses an abstract domain — a lattice of properties (signs, intervals, congruences, or relational domains like octagons and polyhedra; points-to and shape graphs for the heap) related to concrete sets by a Galois connection (α abstracts, γ concretizes, and the best abstract transformer is α∘f∘γ) — and computes the abstract fixpoint instead, guaranteed by monotonicity to over-approximate every real behaviour, accelerating infinite ascending chains with widening (jump to a bound) and refining with narrowing; every dataflow analysis, type inference, and model-checking abstraction is an instance, the precision/cost trade is chosen by domain (non-relational cheap, relational expressive, reduced products combine them), and the payoff is analyzers that prove the absence of runtime errors — Astrée on Airbus flight code with zero false alarms after tuning, Frama-C/EVA, Facebook's Infer, Google's and Mozilla's linters — with false positives, not missed bugs, as the engineering problem.
---
# Abstract interpretation

**In one sentence.** Run the program on descriptions of values instead of values, in a
lattice where the loop must stop, and what you compute is guaranteed to contain everything
the real program can do — Rice's theorem says you can't be exact, so be sound instead.

## From concrete to abstract (Cousot & Cousot 1977; Concrete Semantics ch. 13)
**Collecting semantics**: at each program point, the set of states that can reach it —
defined as the least fixpoint of the transfer functions over the powerset lattice (Kleene:
lfp = ⋃ Fⁿ(∅) — [[operational-and-denotational-semantics]]); exact but uncomputable in
general ([[decidability-and-reductions]]). **Abstract domain** (A, ⊑, ⊔, ⊓, ⊥, ⊤): a lattice
of properties; **Galois connection** α : P(States) → A, γ : A → P(States) with α(S) ⊑ a ⇔
S ⊆ γ(a) — α gives the *best* abstraction, γ its meaning. **Soundness**: an abstract
transformer f♯ is sound if f∘γ ⊆ γ∘f♯; the best one is α∘f∘γ. Then lfp f ⊆ γ(lfp f♯) — the
abstract fixpoint over-approximates reality (Cousot's fixpoint transfer theorem), so "no
error state is in γ(result)" is a proof. Precision is lost at joins (paths merging) and by
non-relational domains (variables abstracted independently); completeness (no loss) is rare.
Cousot's insight: analyses aren't ad hoc — they're constructed from the semantics by
choosing α, and their soundness is by construction.

## Making it terminate: widening and narrowing
Ascending chains in domains like intervals are infinite ([0,0] ⊑ [0,1] ⊑ [0,2] …), so
iteration may not converge. **Widening** ∇: an operator that over-approximates the join and
guarantees stabilization in finitely many steps (intervals: an unstable bound jumps to ±∞,
or to the next threshold — "loop counter i ∈ [0, +∞)"); apply at loop heads (a cut set of
the CFG). **Narrowing** Δ then recovers precision by a bounded descending iteration (i ∈ [0,
+∞) ∧ i < n ⇒ [0, n−1]). Widening is the price for analysing loops without invariants —
and the reason results depend on iteration strategy (worklist order, delayed widening,
loop unrolling). Compare [[dataflow-analysis]]: the classic bit-vector analyses are abstract
interpretations over finite-height lattices where no widening is needed; the monotone
framework is the special case.

## Domains
| Domain | Elements | Cost | Catches |
|---|---|---|---|
| Signs, parity, constants | {−, 0, +}, {even, odd}, k | trivial | constant propagation, division by zero hints |
| **Intervals** | [l, u] per variable | linear | array bounds, overflow ([[integer-representation-and-bits]]) |
| Congruences | a mod m | | alignment, strides |
| **Octagons** (Miné) | ±x ± y ≤ c | O(n³) | loop bounds relating two variables |
| **Polyhedra** (Cousot–Halbwachs) | linear inequalities | exponential | precise linear invariants; templates/zones as cheaper cousins |
| Points-to / alias | abstract heap graphs | | null dereference, aliasing for other analyses |
| **Shape** (TVLA, separation-logic-based) | summarized heap cells | expensive | list/tree structure, memory safety ([[program-verification]]) |
| Numerical + symbolic products | | | Astrée's reduced products (intervals × octagons × filters × floating-point rounding) |
Types are abstract interpretations of values ([[type-systems]] — Cousot 1997 "Types as
abstract interpretations"); model-checking abstractions (predicate abstraction, CEGAR)
choose finite domains ([[model-checking]]); trace partitioning and path sensitivity trade
cost for precision; **reduced product** shares information between domains.

## In practice
**Astrée** (Cousot et al.): proves absence of runtime errors (overflow, division by zero,
out-of-bounds, floating-point issues) in embedded C — Airbus A340/A380 flight control, with
domain tuning to reach zero false alarms; **Frama-C/EVA**, **Polyspace**, **CodeSonar** in
safety-critical industries; **Infer** (Facebook/Meta — separation logic + bi-abduction for
null/resource/race bugs, run at diff time on millions of lines; tuned for low false-positive
rate at the cost of soundness); **Clang Static Analyzer**, SpotBugs, Semgrep as lighter
cousins; compilers' own analyses (value range, alias — [[compiler-optimizations]]); binary
analyzers (BAP, angr); **taint analysis** for security ([[security-principles]]); WCET
analysis of cache and pipeline states ([[real-time-scheduling]]) is an abstract
interpretation of hardware. The perennial trade: sound tools generate false positives that
developers must triage, "unsound" bug finders miss bugs but get adopted — the "soundiness"
manifesto; both are abstract interpretations with different domains and choices.

## Pitfalls
- Confusing "no warnings" from an unsound tool with a proof.
- Widening too early (imprecision) or never (non-termination); joining at every point
  when path-sensitivity was needed.
- Domains that ignore the language's real semantics (integer wraparound, floating point,
  undefined behaviour — [[undefined-behavior]]).
- Ignoring the environment model (library stubs, inputs) — the analysis is only as sound
  as its model of the outside world.

## Related
- [[dataflow-analysis]], [[program-verification]], [[model-checking]], [[type-systems]],
  [[decidability-and-reductions]], [[compiler-optimizations]], [[integer-representation-and-bits]],
  [[real-time-scheduling]], [[security-principles]].

## Sources
Cousot & Cousot 1977, 1979, 1992; Miné "The Octagon Abstract Domain" 2006; Cousot et al. "The ASTRÉE Analyzer" 2005; Concrete Semantics ch. 13; Nielson, Nielson & Hankin, *Principles of Program Analysis*; Rival & Yi, *Introduction to Static Analysis* (2020); Livshits et al. "In Defense of Soundiness" 2015.

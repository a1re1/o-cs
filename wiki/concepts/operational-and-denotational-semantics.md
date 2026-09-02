---
title: Programming language semantics — structural operational semantics (small-step, big-step), evaluation contexts, denotational semantics and domains, axiomatic semantics, program equivalence, and abstract machines
type: concept
section: "5.4"
level: 400
tags: [semantics, operational-semantics, structural-operational-semantics, plotkin, small-step, big-step, natural-semantics, reduction-semantics, evaluation-contexts, felleisen, judgments, inference-rules, inductive-definitions, statics, dynamics, denotational-semantics, domains, scott, least-fixed-point, continuity, strachey, compositionality, axiomatic-semantics, hoare-logic, program-equivalence, contextual-equivalence, bisimulation, abstract-machines, secd, cek, cek-machine, krivine, cps, definitional-interpreters, language-specification, k-framework, redex]
sources: [pierce-tapl-and-pl-theory-texts, pl-theory-seminal-papers]
summary: A language's meaning can be given three ways that must agree: operationally — Plotkin's structural operational semantics defines a transition relation by inference rules on syntax, small-step (t → t', with evaluation contexts E[·] fixing where reduction happens, or congruence rules) or big-step (t ⇓ v), and abstract machines (SECD, CEK, Krivine) make the search for the next redex explicit; denotationally — Scott–Strachey map each phrase compositionally to a mathematical object (functions on domains, with recursion as the least fixed point of a continuous function on a CPO, and ⊥ for divergence); and axiomatically — Hoare triples specify what programs guarantee; the operational style dominates modern definitions because it scales to effects, concurrency and mechanization (Rocq/Coq, K, PLT Redex) and underlies the progress-and-preservation proof of type soundness, while denotational ideas survive as the theory of program equivalence (contextual equivalence, logical relations, bisimulation) and as the meaning of recursion, and executable definitional interpreters connect all of them to working code.
---
# Operational and denotational semantics

**In one sentence.** Say precisely what a program means — by how it steps, by what
mathematical object it denotes, or by what it guarantees — because "whatever the compiler
does" is not a specification and cannot be proved anything about.

## Judgments and rules (PFPL ch. 1–3)
A language definition is a set of **inductive definitions**: judgments like `t : T` (statics)
and `t → t'` (dynamics) defined by inference rules; derivations are trees; proofs are by
**rule induction** ([[induction]], [[fold-and-structural-recursion]] — a derivation is a
tree, so structural recursion applies). Hypothetical judgments (Γ ⊢ t : T) carry contexts;
abstract binding trees handle variables and α-equivalence. The statics/dynamics split: the
statics restricts the programs, the dynamics says what they do, and **type safety** links
them ([[type-systems]]).

## Operational semantics (Plotkin 1981; TAPL ch. 3; SF Smallstep)
- **Small-step** (structural): t → t' one step at a time; rules like E-IfTrue: `if true then
  t₂ else t₃ → t₂` plus congruence rules E-If: `t₁ → t₁' ⇒ if t₁ … → if t₁' …` that say where
  evaluation may proceed; multi-step →*; values are the normal forms we want; **stuck**
  terms (neither value nor reducible — `if 0 then …`) are the runtime errors types exclude.
  **Reduction semantics with evaluation contexts** (Felleisen & Hieb): E ::= [·] | E t | v E
  | if E then … — one rule `E[r] → E[r']` replaces all congruence rules and makes control
  operators (exceptions, continuations, call/cc) definable by manipulating E
  ([[closures-and-environment-model]]).
- **Big-step** (natural semantics, Kahn): t ⇓ v directly; closer to interpreters, shorter
  proofs, but cannot distinguish divergence from stuckness or describe concurrency/interleaving.
  Equivalence of the two is a standard theorem.
- **Abstract machines**: SECD (Landin 1964), **CEK** (control, environment, continuation —
  Felleisen), Krivine (call-by-name), CAM, ZAM — refine the rules into a state transition
  system with explicit environments and continuations; derivable systematically from
  interpreters by CPS + defunctionalization (Reynolds 1972; Danvy's "functional
  correspondence") — the path from semantics to [[bytecode-vms-and-jit]].
- Extensions: stores for state (σ, t → σ', t'), labels/events for concurrency (process
  calculi, CCS/π — [[async-and-event-driven-concurrency]]), cost semantics for complexity
  (PFPL parallelism chapter), probabilistic semantics.

## Denotational semantics (Scott & Strachey 1971; Winskel)
⟦·⟧ maps syntax to mathematics **compositionally** (⟦t₁ + t₂⟧ = ⟦t₁⟧ + ⟦t₂⟧), so equal
denotations justify substitution anywhere. Commands denote state transformers Σ → Σ⊥
(**⊥** = divergence); **while** denotes the **least fixed point** of F(f) = λσ. if ⟦b⟧σ then
f(⟦c⟧σ) else σ, which exists because domains are CPOs and F is continuous (Kleene: lfp = ⊔
Fⁿ(⊥) — the unrolling of the loop; [[recurrences-and-fixed-points]] if present, else
[[invariant-principle]]). The untyped λ-calculus needs a domain D ≅ D → D (Scott's D∞) —
the first real mathematical model of self-application. Full abstraction (denotational
equality = contextual equivalence) failed for PCF with plain domains (Plotkin 1977 —
parallel-or) and was recovered by game semantics (1990s); denotational methods remain
central for reasoning (domain theory, categorical semantics, monads — [[monads]] came from
Moggi's semantics of effects) even as definitions moved operational.

## Axiomatic semantics
Hoare logic ({P} c {Q}), weakest preconditions (Dijkstra), separation logic for heaps —
specifications rather than models; sound with respect to the operational semantics
([[program-verification]]). SF's Hoare chapters prove the rules from the small-step
definition of Imp.

## Program equivalence
**Contextual (observational) equivalence**: t ≅ t' iff no program context can tell them apart
— the gold standard, hard to prove directly; techniques: **logical relations** (type-indexed
relations by induction on types — Tait's normalization, Reynolds' parametricity,
[[polymorphism-and-type-inference]]), **bisimulation** (coinductive — from process calculi,
[[consistency-models]]'s trace notions are cousins), applicative bisimulation (Abramsky),
denotational equality (sound, sometimes incomplete). Compiler correctness (CompCert) is a
semantics-preservation theorem between source and target semantics
([[compiler-optimizations]]).

## Tools and practice
Executable semantics: **PLT Redex** (reduction semantics with random testing), the **K
framework** (semantics of C, Java, EVM, executable and analyzable), Rocq/Isabelle
mechanizations (SF, CompCert, CakeML), Ott/Lem for specs; language standards moving from
prose to formal semantics (WebAssembly's spec is a typed small-step semantics — a first for
an industrial language; JavaScript's ECMA-262 pseudo-code; Rust's RustBelt/MiniRust).
Definitional interpreters (Reynolds) as executable specifications — the SICP/PLAI method
([[sicp]]).

## Pitfalls
- Defining a language by its reference implementation (behaviour = bugs + UB —
  [[undefined-behavior]] exists because C's semantics was prose).
- Big-step semantics for concurrent or non-terminating features.
- Confusing syntactic equality of terms with semantic equivalence; forgetting that
  optimizations must preserve *contextual* equivalence including effects and termination.
- Treating denotational ⊥ as an exception rather than divergence.

## Related
- [[lambda-calculus]], [[type-systems]], [[closures-and-environment-model]],
  [[program-verification]], [[polymorphism-and-type-inference]], [[monads]],
  [[compiler-optimizations]], [[bytecode-vms-and-jit]], [[undefined-behavior]], [[invariant-principle]].

## Sources
Plotkin 1981; TAPL ch. 3, 8; PFPL ch. 1–7; SF Smallstep/Imp/Equiv; Winskel, *The Formal Semantics of Programming Languages* (1993); Felleisen, Findler & Flatt, *Semantics Engineering with PLT Redex* (2009); Scott & Strachey 1971; Reynolds "Definitional Interpreters" 1972.

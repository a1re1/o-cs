---
title: Turing machines and the Church–Turing thesis — the model, variants (multi-tape, nondeterministic, RAM, λ-calculus), universality, code as data, and what "computable" means
type: concept
section: "5.1"
level: 300
tags: [turing-machines, tape, configurations, transition-function, halting, recognizable, decidable, recursively-enumerable, multi-tape, nondeterministic-turing-machine, enumerators, church-turing-thesis, effective-calculability, lambda-calculus, ram-model, universal-turing-machine, code-as-data, self-reference, cellular-automata, turing-completeness, nand-tm, simulation, robustness]
sources: [sipser-and-theory-of-computation-courses, theory-of-computation-seminal-papers]
summary: Turing's 1936 machine — a finite control (finitely many "m-configurations", because "the human memory is necessarily limited") reading and writing one square at a time on an unbounded tape and moving left or right — is the definition of computation: a language is Turing-recognizable if some machine accepts exactly its strings (possibly looping on others) and decidable if the machine always halts; every reasonable change (multiple tapes, two-way infinite tape, nondeterminism, random-access memory, λ-calculus, cellular automata, NAND-TM programs, your favourite language) yields the same class of computable functions, which is the evidence for the Church–Turing thesis that this class is what "effectively calculable by finite means" means; and because a machine's description is a finite string, a universal machine can simulate any machine from its description — code is data — which is both the stored-program computer and the hook on which the halting problem and Gödel's incompleteness hang.
---
# Turing machines and the Church–Turing thesis

**In one sentence.** Finite control, unbounded scratch paper, one symbol at a time — that
is all any computer can do, every other model is a notational convenience, and one machine
can run them all from a description.

## The model (Turing 1936; Sipser 3.1)
Turing's argument: a person computing works with finitely many mental states and a finite
number of distinguishable symbols, observes a bounded region at a time, and changes only
finitely much per step — so idealize: **M = (Q, Σ, Γ, δ, q₀, q_accept, q_reject)** with tape
alphabet Γ ⊇ Σ ∪ {␣}, transition δ: Q×Γ → Q×Γ×{L,R}; the tape is infinite to the right and
starts with the input. A **configuration** uqv (tape contents, state, head position) evolves
by δ; the machine **accepts**, **rejects**, or **loops**. L(M) is the set of accepted inputs; a
language is **Turing-recognizable** (recursively enumerable) if some M accepts exactly it, and
**decidable** (recursive) if some M accepts it and rejects everything else — the distinction
between "yes has a finite certificate" and "yes and no both do". Turing's own framing:
computable numbers are those whose decimals a machine prints, and they include π, e, all
algebraic numbers, yet are countable.

## Robustness: the variants (Sipser 3.2; Barak ch. 8)
Multi-tape ⇒ single tape (interleave tracks; quadratic slowdown); two-way infinite tape;
**nondeterministic** TMs (accept if some branch accepts; simulate by breadth-first search
over the computation tree — same languages, exponential time); enumerators (a language is
recognizable iff some machine enumerates it); **RAM machines** with registers and indirect
addressing (polynomially related — the model behind [[asymptotic-notation]]); counter
machines; **λ-calculus** (Church — [[lambda-calculus]]; functions, application, β-reduction);
cellular automata (Rule 110); Post systems; Barak's NAND-TM/NAND-RAM; and every general-
purpose programming language. All equivalent in what they compute — "Turing complete". The
proofs are simulations, and simulation is the field's basic tool.

## The Church–Turing thesis (Sipser 3.3; Turing §9)
The informal notion "algorithm / effectively calculable / computable by finite means" equals
Turing-machine computability. Not a theorem (it relates an intuition to a definition) but
supported by the convergence of every proposed model since 1936 — Turing's appendix already
proved equivalence with Church's λ-definability. Consequences: we can describe algorithms in
prose or pseudocode and still reason rigorously about computability; physical variants
(quantum computers) change *efficiency*, not computability ([[quantum-computing]] — the
extended, complexity-theoretic thesis is the contested one). Hilbert's tenth problem
(Diophantine equations — Matiyasevich 1970) is the classic "algorithm" that turned out not to
exist.

## Universality and code as data (Turing §6–7; Barak ch. 5, 9)
Encode a machine M as a string ⟨M⟩; the **universal Turing machine** U on input ⟨M, w⟩
simulates M on w. This is the stored-program computer ([[isa-and-assembly]]), the interpreter
([[bytecode-vms-and-jit]]), and the reason programs can analyse, compile and quine themselves
— and, by the same token, why they cannot decide their own halting
([[decidability-and-reductions]]). Barak's ordering makes the point early: even for
finite functions, a universal *circuit* exists, and counting circuits gives the first
lower bound (most functions need exponential circuits).

## Working with TMs
Levels of description: formal (transition table), implementation (head movements, tape
tracks), high-level ("mark the first unmarked 0…"). Standard tricks: subroutines, marking,
tape as multiple tracks, storing a finite amount in the state, shifting. A **linear-bounded
automaton** (tape limited to the input) recognizes context-sensitive languages
([[context-free-grammars]]). Complexity refines the model with time and space bounds
([[complexity-classes]]).

## Pitfalls
- Confusing recognizable with decidable (a recognizer may loop on "no").
- Reading the thesis as a theorem, or as a claim about physical speed.
- Assuming nondeterministic TMs are "faster" — they define the same class; the cost is the
  simulation.
- Fighting formal transition tables when a high-level description suffices (Sipser's rule).

## Related
- [[decidability-and-reductions]], [[complexity-classes]], [[lambda-calculus]],
  [[finite-automata-and-regular-languages]], [[context-free-grammars]], [[isa-and-assembly]],
  [[bytecode-vms-and-jit]], [[asymptotic-notation]].

## Sources
Turing 1936 §1–7, 9; Sipser ch. 3 (18.404 L5–6); Barak ch. 3–5, 7–9; Church 1936; Davis, *The Universal Computer*.

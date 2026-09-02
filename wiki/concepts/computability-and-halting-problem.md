---
title: Computability, the halting problem, and reductions (overview)
type: concept
section: "1.5"
level: 300
tags: [computability, halting-problem, decidable, recursively-enumerable, church-turing-thesis, rice-theorem, reductions, undecidability, diagonalization, turing-machines]
sources: [stanford-cs103, open-logic-project, mcs-lehman-leighton-meyer]
summary: The Church–Turing thesis fixes what "algorithm" means; the halting problem is undecidable by diagonalization; Rice's theorem says every non-trivial semantic property of programs is undecidable; and mapping reductions transfer undecidability — the facts that bound what static analyzers, verifiers, and compilers can promise.
---
# Computability and the halting problem

**In one sentence.** No program can decide, for every program and input, whether it halts — and
by Rice's theorem the same holds for every non-trivial question about what a program *does*.

## Definitions
- A **decidable** (recursive) language: some algorithm halts on every input with yes/no.
  **Recognizable** (recursively enumerable, RE): an algorithm says yes on members and may loop on
  non-members. R ⊂ RE; L ∈ R iff both L and its complement are RE.
- **Church–Turing thesis**: Turing machines, λ-calculus, partial recursive functions, and any
  physically realizable programming language compute the same partial functions
  ([[turing-machines]], [[lambda-calculus]]).

## The halting problem is undecidable
Suppose H(P, x) decides whether P halts on x. Define D(P) = "if H(P, P) then loop forever else halt".
Then D(D) halts iff H(D, D) says it does not — contradiction. This is Cantor's diagonal argument with
programs as rows ([[sets-relations-functions]]); counting gives the same conclusion: countably many
programs, uncountably many languages, so most languages are undecidable.

## Reductions and Rice's theorem
- **Mapping reduction** A ≤ₘ B: a computable f with x ∈ A ⇔ f(x) ∈ B. If A is undecidable so is B
  (contrapositive: a decider for B would decide A). Standard chain: HALT ≤ₘ "accepts ε" ≤ₘ "language
  is empty" ≤ₘ "two programs are equivalent"; also Post's correspondence problem, tiling, Hilbert's
  10th problem (Diophantine equations), FOL validity.
- **Rice's theorem**: any property of the *language/behaviour* of a program that is neither always
  true nor always false is undecidable. Properties of the *text* (has fewer than 100 lines) are fine;
  properties of *behaviour* (never dereferences null, is equivalent to this spec, terminates) are not.
- The same reasoning gives semantic limits for compilers (perfect dead-code elimination), static
  analyzers (must over-approximate — [[abstract-interpretation]]), and virus scanners (Cohen 1987).

## Practical consequences
- Verifiers and analyzers are sound-but-incomplete or complete-but-unsound, or restrict the language
  (total languages like Agda, decidable fragments in SMT — [[sat-and-smt-solvers]], [[model-checking]]).
- Termination checkers use ranking functions and give up on hard cases ([[invariant-principle]]).
- Type systems reject some correct programs precisely because they must be decidable.
- Timeouts are the engineering answer to undecidability.

## Related
- [[turing-machines]], [[decidability-and-reductions]], [[godel-incompleteness-theorems]],
  [[soundness-and-completeness]], [[p-vs-np]].

## Sources
CS103 lectures 11–13; Open Logic Part 5; MCS 7.2 (The Halting Problem).

---
title: Decidability and undecidability — diagonalization, the halting problem, mapping reductions, Rice's theorem, the computation-history method, the recursion theorem, and what it means for software
type: concept
section: "5.1"
level: 400
tags: [decidability, undecidability, halting-problem, diagonalization, cantor, countable, uncountable, acceptance-problem, mapping-reduction, many-one-reduction, turing-reduction, rice-theorem, computation-history, post-correspondence-problem, recursion-theorem, self-reference, quines, co-recognizable, unrecognizable, godel-incompleteness, entscheidungsproblem, hilbert-tenth-problem, static-analysis-limits, semi-decidable]
sources: [sipser-and-theory-of-computation-courses, theory-of-computation-seminal-papers]
summary: There are uncountably many languages but only countably many Turing machines, so most problems have no algorithm at all, and diagonalization exhibits a concrete one — the machine that halts iff it would not halt on itself — making the halting and acceptance problems undecidable (though recognizable), their complements unrecognizable, and a language decidable iff both it and its complement are recognizable; from there, mapping reductions (a computable f with w ∈ A ⇔ f(w) ∈ B) spread undecidability to emptiness, equivalence, regularity of a machine's language and, by Rice's theorem, to every non-trivial semantic property of programs, while the computation-history method reaches problems about grammars and tilings (Post's correspondence problem, CFG ambiguity, Hilbert's tenth) and the recursion theorem shows programs can obtain their own code (quines, viruses, and a two-line halting-problem proof); the same self-reference gives Gödel's incompleteness and Turing's answer to the Entscheidungsproblem, and its engineering face is that every static analysis, verifier, or optimizer must approximate.
---
# Decidability and reductions

**In one sentence.** A program that answers questions about programs can be handed itself,
and that one move makes "does it halt", "are these equivalent", and every other interesting
question about behaviour unanswerable in general — so all analysis is approximation.

## Counting (Sipser 4.2; Turing §8)
Turing machines are finite strings, hence **countable**; languages over Σ are subsets of Σ*,
hence **uncountable** (Cantor's diagonal argument on infinite binary sequences —
[[sets-relations-functions]]). So almost every language is unrecognizable — non-computability
is the rule; the interesting part is finding *natural* examples.

## The halting problem (Turing 1936 §8; Sipser 4.2)
A_TM = {⟨M, w⟩ : M accepts w} is **recognizable** (run the universal machine) but
**undecidable**: suppose decider H; build D that on ⟨M⟩ runs H(⟨M, ⟨M⟩⟩) and does the
opposite; D(⟨D⟩) accepts iff it rejects. Turing's original version: no machine decides whether
a machine is "circle-free" (prints infinitely many digits). HALT_TM likewise (reduce A_TM to
it). Consequences: **co-recognizable** languages (complement recognizable); a language is
decidable ⇔ recognizable and co-recognizable; the complement of A_TM is not recognizable —
there are three tiers, not two. The diagonal trick is the same one behind Russell's paradox,
Gödel, Cantor, and the time hierarchy theorem ([[complexity-classes]]).

## Reductions (Sipser 5.1, 5.3)
**Mapping (many-one) reduction** A ≤ₘ B: a computable f with w ∈ A ⇔ f(w) ∈ B. If B is decidable
so is A; contrapositive: A undecidable ⇒ B undecidable. Standard chain from A_TM: HALT_TM,
E_TM (emptiness — build M' that runs M on the fixed w), REGULAR_TM, EQ_TM (neither
recognizable nor co-recognizable). **Turing reductions** (oracle access) are the more general
notion; complexity theory restricts both to polynomial time ([[np-completeness-and-reductions]]).
Reductions run *in the direction of hardness*: to show B is hard, reduce a known-hard A *to* B
— the direction every student gets backwards once.

## Rice's theorem (1953)
Any property of the *language* of a machine (semantic, not syntactic) that some machines have
and some lack is undecidable — "does this program ever output 0", "is it equivalent to that
one", "does it use more than 1 GB", "is this function pure". Proof: reduce A_TM by building a
machine whose language is trivial or a fixed member depending on whether M accepts w.
Engineering corollary: compilers' optimizations, type checkers, linters, malware detectors,
termination checkers and verifiers all decide a *conservative approximation* — soundness with
false positives, or completeness with false negatives, never both
([[abstract-interpretation]], [[program-verification]], [[compiler-optimizations]],
[[type-systems]]). Syntactic properties ("has more than 100 states") stay decidable.

## The computation-history method (Sipser 5.1; 18.404 L10)
An accepting computation history is the sequence of configurations C₁…Cₖ; checking that a
string *is* such a history needs only local consistency between adjacent configurations —
which linear-bounded automata, and even the *complement* of a CFG, can do. Hence: A_LBA is
decidable but E_LBA is not; ALL_CFG (is L(G) = Σ*?) is undecidable; **Post's correspondence
problem** (dominos with top/bottom strings — a match spells out a computation history) is
undecidable, and PCP reduces to CFG ambiguity, CFG intersection emptiness, and tiling
problems; Hilbert's tenth (Diophantine equations — Matiyasevich) and the word problem for
groups fall the same way. The same encoding trick, made polynomial, is Cook–Levin
([[p-vs-np]]).

## Self-reference: the recursion theorem (Sipser 6.1; 18.404 L11)
Every machine can be written to "obtain its own description" — for any computable t(⟨M⟩, w)
there is R with R(w) = t(⟨R⟩, w). Constructively: a machine that prints another machine that
prints the first (quines — [[purity-and-referential-transparency]]'s mirror image). Uses:
a two-line proof that A_TM is undecidable (R: get ⟨R⟩, ask H whether R accepts w, do the
opposite); minimal machines are unrecognizable; self-replicating programs and viruses are
inevitable; **Gödel's first incompleteness theorem** as a corollary (the sentence "this
statement is unprovable" — or Barak/Sipser: provability in a sound system is recognizable, so
if every true statement about halting were provable, halting would be decidable —
[[first-order-logic]], [[proof-techniques]]).

## What it means in practice
Halting/termination checkers succeed on structured subsets (ranking functions, size-change);
totality checkers in dependently typed languages reject some terminating programs;
"undecidable" problems are routinely solved *for the instances that arise* (SAT/SMT solvers,
model checkers with bounded state — [[sat-and-smt-solvers]], [[model-checking]]); the theorems
say no *uniform* procedure exists, not that you cannot answer today's question. Turing's
1936 lesson stands: Hilbert's dream of a decision procedure for mathematics is dead, and
computer science was born in the wreckage.

## Pitfalls
- Reducing in the wrong direction; reductions that are not computable.
- Concluding "undecidable, so give up" instead of "approximate or restrict the inputs".
- Confusing "undecidable" with "hard": some undecidable problems have trivial instances,
  some decidable ones are intractable ([[complexity-classes]]).
- Reading Rice's theorem as applying to syntactic properties.

## Related
- [[computability-and-halting-problem]] (the §1.5 introduction this page extends), [[turing-machines]], [[complexity-classes]], [[p-vs-np]], [[np-completeness-and-reductions]],
  [[context-free-grammars]], [[abstract-interpretation]], [[program-verification]],
  [[sets-relations-functions]], [[first-order-logic]], [[kolmogorov-complexity]].

## Sources
Turing 1936 §8, 11; Sipser ch. 4–6 (18.404 L7–11); Barak ch. 9, 11; Rice 1953; Post 1946; Matiyasevich 1970.

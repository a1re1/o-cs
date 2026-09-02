---
title: P vs NP — what the question asks, Cook–Levin, why it is hard to resolve (relativization, natural proofs, algebrization), Ladner's intermediate problems, and what a resolution would mean
type: concept
section: "5.1"
level: 400
tags: [p-vs-np, p, np, cook-levin, sat, certificates, verifiers, nondeterminism, polynomial-time-reduction, np-complete, np-hard, conp, ladner-theorem, np-intermediate, factoring, graph-isomorphism, relativization, baker-gill-solovay, natural-proofs, algebrization, barriers, one-way-functions, cryptography, exponential-time-hypothesis, what-if-p-equals-np, impagliazzo-worlds, millennium-prize, phase-transitions, sat-solvers]
sources: [sipser-and-theory-of-computation-courses, theory-of-computation-seminal-papers]
summary: P vs NP asks whether every problem whose solutions can be checked in polynomial time can also be solved in polynomial time — whether search is no harder than verification — and Cook–Levin makes it concrete by showing SAT is NP-complete (any polynomial-time verifier's computation tableau is encoded as a CNF formula of polynomial size), so P = NP iff SAT has a polynomial algorithm; the consensus is P ≠ NP because thousands of NP-complete problems have resisted fifty years of effort, because P = NP would collapse cryptography (no one-way functions) and make finding proofs as easy as checking them, and because Ladner's theorem promises a rich structure of intermediate problems (factoring, graph isomorphism are candidates) if P ≠ NP; yet proof techniques hit barriers — relativization (Baker–Gill–Solovay: diagonalization cannot do it), natural proofs (Razborov–Rudich: combinatorial lower bounds would break pseudorandom generators), algebrization — and stronger conjectures (ETH, SETH) now parametrize algorithms research, while in practice SAT solvers, approximation, parameterization and heuristics handle the instances that arise.
---
# P vs NP

**In one sentence.** Is recognizing a right answer fundamentally easier than finding one? We
think so, cannot prove it, and have learned exactly why our proof tools are too weak.

## The question (Sipser 7.2–7.4; Barak ch. 14–16)
**P**: decided in polynomial time. **NP**: strings with polynomial-size certificates checkable
in polynomial time (equivalently, nondeterministic polynomial time: guess the certificate).
Every NP problem can be solved in exponential time by trying all certificates; the question
is whether the exponential is necessary. Framed by Cook (1971), Karp (1972), Levin (1973), and
in Gödel's 1956 letter to von Neumann ("if such a machine existed, the mental work of a
mathematician concerning yes-or-no questions could be completely replaced"). A Millennium
Prize problem. Note P ⊆ NP trivially; also NP ⊆ PSPACE ⊆ EXP ([[complexity-classes]]).

## Cook–Levin (18.404 L16)
SAT ∈ NP obviously. For any L ∈ NP with verifier V and certificate length nᵏ, build a formula
that says "there is a certificate c such that V(w, c) accepts": lay out the nᵏ × nᵏ **tableau**
of V's computation, with variables x_{i,j,s} ("cell (i,j) holds symbol s"), and clauses
enforcing (1) exactly one symbol per cell, (2) the first row is the start configuration with w
and free certificate cells, (3) some row accepts, (4) every 2×3 window is consistent with V's
transition function — locally checkable, so polynomially many constant-size clauses. Satisfying
assignments ↔ accepting computations. Hence SAT is **NP-complete**; 3SAT by clause splitting;
then Karp's reductions spread it ([[np-completeness-and-reductions]]). The tableau is the
computation-history method from computability made polynomial
([[decidability-and-reductions]]).

## Why we believe P ≠ NP
Thousands of NP-complete problems across every field with no polynomial algorithm for any;
the *structure* it would destroy: **one-way functions** and all of public-key cryptography
([[cryptography-basics]]) require P ≠ NP (and more); theorem-proving would become mechanical
(NP contains "is there a proof of length ≤ n"); optimization would be as easy as evaluation.
Impagliazzo's five worlds (Algorithmica, Heuristica, Pessiland, Minicrypt, Cryptomania)
map what different answers would mean — we hope to live in Cryptomania. Stronger working
hypotheses: **ETH** (3SAT needs 2^{Ω(n)}) and **SETH** (SAT needs 2^{(1−ε)n}) — the basis of
fine-grained complexity ("no n^{2−ε} edit distance unless SETH fails").

## Structure if P ≠ NP
**Ladner's theorem** (1975): if P ≠ NP there exist **NP-intermediate** problems (in NP, neither in
P nor NP-complete), built by delayed diagonalization — artificial, but natural candidates exist:
**integer factoring** (in NP ∩ coNP; polynomial on a quantum computer — [[quantum-computing]]),
**graph isomorphism** (quasipolynomial, Babai 2015), discrete log, lattice problems. NP vs coNP
(is UNSAT checkable?) and the polynomial hierarchy refine the question
([[complexity-theory-advanced]]).

## Why it's hard to prove: barriers
- **Relativization** (Baker, Gill & Solovay 1975): there are oracles with P^A = NP^A and P^B ≠
  NP^B, so any proof that works verbatim with oracles — diagonalization, simulation — fails.
  (IP = PSPACE is a non-relativizing result, so such proofs exist.)
- **Natural proofs** (Razborov & Rudich 1994): "natural" circuit lower-bound techniques
  (constructive, large) would break pseudorandom generators, which we believe exist.
- **Algebrization** (Aaronson & Wigderson 2008): arithmetization tricks relativize too.
Progress lives in restricted models (monotone circuits, AC⁰, ACC⁰ — Williams 2011) and in
GCT (geometric complexity theory). The problem is not "we haven't tried hard enough".

## Living with NP-hardness (see [[np-completeness-and-reductions]])
Exact exponential algorithms with better bases, **SAT/SMT solvers** that solve industrial
instances with millions of variables ([[sat-and-smt-solvers]]), approximation
([[approximation-algorithms]]), parameterized algorithms, average-case ease and phase
transitions (random 3SAT is hard only near clause ratio 4.27), heuristics and local search.
Worst-case hardness is the theory's statement; engineering asks about *your* distribution.

## Pitfalls
- "NP = exponential time" or "NP-complete = unsolvable".
- Thinking a fast solver on benchmarks says anything about P vs NP.
- Proposed proofs that relativize; proofs that P = NP via a "polynomial" algorithm with a
  hidden exponential.
- Assuming P ≠ NP implies cryptography is safe (that needs average-case hardness, one-way
  functions).

## Related
- [[np-completeness-and-reductions]], [[complexity-classes]], [[decidability-and-reductions]],
  [[cryptography-basics]], [[sat-and-smt-solvers]], [[approximation-algorithms]],
  [[quantum-computing]], [[complexity-theory-advanced]].

## Sources
Cook 1971; Karp 1972; Ladner 1975; Baker, Gill & Solovay 1975; Razborov & Rudich 1994; Sipser ch. 7 (18.404 L14–16, 22); Barak ch. 14–16; Aaronson "P =? NP" (2016 survey); Fortnow "The Status of the P versus NP Problem" (CACM 2009).

---
title: Complexity classes — time and space bounds, P, NP, coNP, EXP, PSPACE, L and NL, Savitch's theorem, hierarchy theorems, the class picture and what separates what
type: concept
section: "5.1"
level: 400
tags: [complexity-classes, time-complexity, space-complexity, big-o-on-turing-machines, p, np, conp, exp, nexp, pspace, npspace, savitch-theorem, l, nl, nl-equals-conl, immerman-szelepcsenyi, path-problem, tqbf, pspace-complete, generalized-geography, games, time-hierarchy, space-hierarchy, diagonalization, relativization, oracles, bpp, rp, zpp, complexity-zoo, polynomial-hierarchy, cook-levin, reductions, log-space-reductions]
sources: [sipser-and-theory-of-computation-courses, theory-of-computation-seminal-papers]
summary: Bounding a Turing machine's steps or tape cells as a function of input size gives the complexity classes: P (polynomial time — the model-independent notion of "efficient", because all reasonable models are polynomially related), NP (nondeterministic polynomial time = polynomial-time verifiable certificates) and coNP, EXP; PSPACE (polynomial space, which equals NPSPACE by Savitch's s² simulation and contains NP and coNP; TQBF and generalized games are complete for it), and the sublinear-space classes L and NL (logarithmic space; PATH is NL-complete; NL = coNL by Immerman–Szelepcsényi's inductive counting); the known inclusions L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXP with the hierarchy theorems proving (by diagonalization) that more time or space strictly helps — so P ≠ EXP and NL ≠ PSPACE — while every adjacent pair remains open, and relativization (Baker–Gill–Solovay) shows why diagonalization alone cannot separate P from NP; randomized classes (BPP, RP, ZPP) sit between P and PSPACE, and the whole picture organizes which problems can be attacked how.
---
# Complexity classes

**In one sentence.** Once everything computable is on the table, ask how much time and
space it costs — and discover that "polynomial" is the robust line, that space is stranger
than time, and that the questions between adjacent classes are almost all open.

## Measuring (Sipser 7.1; Barak ch. 12–13)
TIME(t(n)) / SPACE(s(n)): languages decided by a (deterministic) TM within t(n) steps / s(n)
cells on inputs of length n; NTIME/NSPACE for nondeterministic machines (max over branches).
Model matters up to polynomials: k-tape → 1-tape squares time; RAM ↔ TM polynomial;
nondeterministic → deterministic exponential. So classes closed under polynomial changes are
model-independent — the reason **P** = ∪ₖ TIME(nᵏ) is the definition of "efficient" (the
Cobham–Edmonds thesis), even though n¹⁰⁰ is not practical. Notation from
[[asymptotic-notation]]; algorithms from §3 live inside P.

## The main classes
| Class | Definition | Complete problems | Notes |
|---|---|---|---|
| **L** | deterministic O(log n) space (read-only input) | — | pointers into the input; undirected PATH ∈ L (Reingold 2005) |
| **NL** | nondeterministic log space | PATH (directed reachability), 2SAT | NL = coNL (Immerman–Szelepcsényi 1988: count reachable vertices inductively) |
| **P** | polynomial time | circuit value, linear programming, Horn-SAT, PATH under log-space reductions | closed under complement, composition |
| **NP** | polynomial-time verifiable certificates (= NTIME(poly)) | SAT, 3SAT, clique, Hamiltonian path, subset sum… ([[np-completeness-and-reductions]]) | [[p-vs-np]] |
| **coNP** | complements of NP (certificates for "no") | tautology, UNSAT | NP ≠ coNP would imply P ≠ NP |
| **PSPACE** | polynomial space | TQBF, generalized geography, Go/checkers on n×n boards, regular-expression equivalence with squaring | = NPSPACE (Savitch); games with alternating quantifiers |
| **EXP** | 2^{poly} time | generalized chess (with some rules), succinct problems | P ≠ EXP (time hierarchy) |
| **NEXP** | nondeterministic exponential | succinct SAT | |
| **BPP / RP / ZPP** | bounded-error / one-sided / zero-error polynomial randomized | primality was here before AKS | BPP ⊆ Σ₂ ∩ Π₂; conjectured = P ([[randomized-algorithms]]) |
Known: **L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXP ⊆ NEXP**, NL ⊆ P via reachability on the
configuration graph, NP ⊆ PSPACE by trying all certificates, PSPACE ⊆ EXP by counting
configurations. Proven strict: NL ≠ PSPACE, P ≠ EXP (hierarchy theorems). Everything between
neighbours is open. The **polynomial hierarchy** (Σₖ/Πₖ — alternating quantifiers) sits inside
PSPACE; #P counts certificates (permanent; Toda's theorem) — [[complexity-theory-advanced]].

## Space (Sipser 8; 18.404 L17–20)
**Savitch's theorem** (1970): NSPACE(s) ⊆ SPACE(s²) for s ≥ log n — decide "can C₁ reach C₂ in
2ᵗ steps" recursively via a midpoint, reusing space; hence PSPACE = NPSPACE (nondeterminism
buys little in space, unlike — apparently — in time). **TQBF** (true fully quantified Boolean
formulas) is PSPACE-complete: PSPACE ⊆ TQBF by encoding Savitch's recursion as ∀∃-quantified
formulas; games are the natural PSPACE problems (a winning strategy = ∃ my move ∀ your move
∃ … — [[search-algorithms-ai]] minimax). **Log space**: L can hold O(1) pointers; NL's
complete problem PATH under **log-space reductions** (which are what separates NL from P
meaningfully); NL = coNL shows non-reachability has short "certificates" if you count.
Space reuse is why time and space differ: a computation can revisit the same configuration
in time but not usefully in space.

## Hierarchy theorems and relativization (Sipser 9; 18.404 L21–22)
**Time hierarchy**: for time-constructible t, TIME(o(t/log t)) ⊊ TIME(t) — diagonalize
against all machines running in the smaller bound with a universal simulator; **space
hierarchy** similarly (tighter, no log). Consequences: P ⊊ EXP, NL ⊊ PSPACE, and hence some
problems (EXP-complete ones like generalized chess, EXPSPACE-complete regular-expression
equivalence with exponentiation) are *provably* intractable. **Relativization** (Baker, Gill &
Solovay 1975): with oracle access, P^A = NP^A for some A and P^B ≠ NP^B for others; since
diagonalization and simulation arguments go through unchanged with oracles, they cannot
settle P vs NP — the first "barrier" (natural proofs and algebrization are the others —
[[complexity-theory-advanced]]).

## Beyond decision problems
Function/optimization versions reduce to decision by binary search; **circuit complexity**
(P/poly, non-uniform, Barak's starting point); **communication complexity**; **average-case**
and **parameterized** complexity refine "hard" ([[np-completeness-and-reductions]]);
**interactive proofs** (IP = PSPACE, Shamir 1990; PCP) and **quantum** BQP
([[quantum-computing]]) extend the picture ([[complexity-theory-advanced]]).

## Pitfalls
- Reading P as "practical" (n¹⁰⁰) or NP as "not polynomial" (it means *nondeterministic*
  polynomial; P ⊆ NP).
- Assuming space classes behave like time classes (nondeterminism is nearly free in space).
- Using polynomial-time reductions for classes inside P (they trivialize — use log-space).
- "Hard in the worst case" ≠ hard on your inputs.

## Related
- [[p-vs-np]], [[np-completeness-and-reductions]], [[turing-machines]],
  [[decidability-and-reductions]], [[asymptotic-notation]], [[randomized-algorithms]],
  [[complexity-theory-advanced]], [[search-algorithms-ai]], [[quantum-computing]].

## Sources
Sipser ch. 7–10 (18.404 L12–24); Barak ch. 12–13, 17, 20; Arora & Barak ch. 1–4; Savitch 1970; Immerman 1988; Szelepcsényi 1988; Hartmanis & Stearns 1965; Baker, Gill & Solovay 1975.

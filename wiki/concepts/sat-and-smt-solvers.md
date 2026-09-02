---
title: SAT and SMT solvers — CNF and DPLL, CDCL (unit propagation, conflict analysis, clause learning, restarts, VSIDS), BDDs, SMT with theories (DPLL(T), Nelson–Oppen, arithmetic, bit-vectors, arrays), Z3 and friends, and where solvers are used
type: concept
section: "5.5"
level: 400
tags: [sat, satisfiability, cnf, tseitin, dpll, cdcl, unit-propagation, boolean-constraint-propagation, two-watched-literals, conflict-analysis, implication-graph, clause-learning, first-uip, non-chronological-backtracking, restarts, vsids, phase-saving, preprocessing, resolution, proof-complexity, minisat, cadical, kissat, sat-competition, bdd, binary-decision-diagrams, smt, satisfiability-modulo-theories, dpll-t, theory-solvers, nelson-oppen, linear-arithmetic, simplex, bit-vectors, bit-blasting, arrays, uninterpreted-functions, equality-and-uninterpreted-functions, congruence-closure, quantifiers, e-matching, z3, cvc5, yices, smt-lib, max-sat, optimization, symbolic-execution, bounded-model-checking, verification-conditions, planning, scheduling, package-dependency-resolution, phase-transition]
sources: [formal-methods-texts-and-courses, formal-methods-seminal-papers, p-vs-np]
summary: SAT is NP-complete yet modern solvers decide industrial formulas with millions of clauses: encode with Tseitin to CNF, then CDCL — unit propagation with two-watched literals, decisions guided by activity heuristics (VSIDS/VMTF) and phase saving, conflict analysis on the implication graph producing a learned clause (first UIP) and non-chronological backjumping, restarts and clause-database management — a search whose learned clauses form a resolution proof (so proof-complexity lower bounds like pigeonhole are its hard cases); BDDs offer a canonical alternative for quantification-heavy hardware problems; SMT lifts SAT to richer logics by DPLL(T) — a SAT core over Boolean skeletons cooperating with theory solvers for equality and uninterpreted functions (congruence closure), linear arithmetic (simplex), bit-vectors (bit-blasting), arrays, strings, with Nelson–Oppen combining them and E-matching/MBQI handling quantifiers — as implemented by Z3, cvc5, Yices and the SMT-LIB standard; solvers now underlie verification (VC discharge, bounded model checking, symbolic execution), program synthesis, package dependency resolution, scheduling, hardware equivalence checking, and cryptanalysis.
---
# SAT and SMT solvers

**In one sentence.** The canonical NP-complete problem turned out to be, on the instances
people actually generate, the most useful solved problem in computer science — because
learning from every conflict makes exponential search pay only for genuinely hard cores.

## SAT (Biere et al., *Handbook of Satisfiability*; Knuth TAOCP 7.2.2.2)
Input: CNF — a conjunction of clauses (disjunctions of literals); any circuit/formula
converts linearly by **Tseitin** encoding (fresh variable per subformula). Worst-case
exponential ([[p-vs-np]]); **DPLL** (1962): unit propagation, pure literals, split on a
variable, backtrack. **CDCL** (GRASP 1996, Chaff 2001, MiniSat 2003) turns DPLL into learning:
1. **Unit propagation (BCP)** with **two watched literals** per clause — no work on
   backtracking, cache-friendly; 80–90 % of runtime.
2. **Decision**: pick a variable by **VSIDS** (activity bumped on conflicts, decayed) or
   VMTF/LRB; **phase saving** (reuse the last polarity).
3. **Conflict analysis**: on an empty clause, walk the **implication graph** backwards to the
   **first unique implication point**; derive a **learned clause** (asserting after backjump)
   by resolution; **non-chronological backjumping** to the second-highest level in it.
4. **Restarts** (Luby or glucose-style dynamic) with phase saving; **clause deletion** by
   LBD/activity; inprocessing (subsumption, variable elimination, vivification).
Learned clauses are resolution derivations — CDCL is a (restricted) resolution proof search,
so resolution lower bounds (pigeonhole, random k-SAT near the threshold ratio ≈4.27 —
[[complexity-theory-advanced]]) are exactly where it dies; structured industrial instances
have small "backdoors". State of the art: CaDiCaL, Kissat, CryptoMiniSat (XOR reasoning);
parallel portfolios and cube-and-conquer (Pythagorean triples: a 200 TB proof); DRAT proof
logging for checkable unsat proofs. **BDDs** (Bryant 1986): canonical DAGs for Boolean
functions under a variable order; apply, quantify, and equality in O(size); great for
hardware and image computation ([[model-checking]]), exponential for multipliers; ZDDs for
combinatorics (Knuth). Local search (WalkSAT) for random satisfiable instances; MaxSAT and
pseudo-Boolean/optimization variants; #SAT and knowledge compilation (d-DNNF) for counting
([[complexity-theory-advanced]]).

## SMT (de Moura & Bjørner 2008; Barrett et al. handbook chapter)
Formulas over theories: **EUF** (equality + uninterpreted functions — congruence closure,
union-find — [[union-find]]), **linear integer/real arithmetic** (simplex for reals, branch-
and-bound/cuts for integers, difference logic with Bellman–Ford — [[linear-programming-and-duality]]), **bit-vectors** (bit-blast to SAT after word-level
rewriting; the theory behind checking machine code and overflow — [[integer-representation-and-bits]]),
**arrays** (read/write axioms via lemmas on demand), **strings/regex**, **floating point**,
**algebraic datatypes**. **DPLL(T)**: the SAT core assigns Boolean abstractions of atoms;
the theory solver checks consistency of the partial assignment incrementally, explains
conflicts as clauses, propagates implied literals; **Nelson–Oppen** combines disjoint
stably-infinite theories by exchanging equalities. **Quantifiers** are the frontier:
E-matching on triggers (Z3 in Dafny/Boogie — instantiation heuristics decide whether a VC
verifies), MBQI, and the incompleteness that makes verification "brittle". **SMT-LIB** is
the standard format and benchmark library; solvers: **Z3** (Microsoft; APIs, optimization
νZ, fixed points/Datalog), **cvc5** (proofs, syntax-guided synthesis), Yices, Bitwuzla,
Boolector, MathSAT. Interpolants and unsat cores feed CEGAR and IC3 ([[model-checking]]).

## Where solvers are used
Verification-condition discharge (Dafny, Why3, F*, Frama-C, SPARK — [[program-verification]]),
bounded model checking of hardware and C (CBMC), **symbolic execution** (KLEE, angr, SAGE —
path constraints solved for inputs; Microsoft's SAGE found a third of Windows 7 fuzzing bugs
— [[fuzzing]]), equivalence checking of circuits, **program synthesis** (SyGuS, Sketch,
Rosette), test generation, type inference for refinement types ([[type-systems]]),
**dependency resolution** (apt's, Cargo's, and Conda's resolvers; Eclipse p2 uses SAT;
Debian's package conflicts are SAT), scheduling and timetabling, planning (SATPlan), EDA
placement/routing, cryptanalysis (SAT-based attacks on reduced ciphers), math (Pythagorean
triples, Keller's conjecture, Schur number 5), AI (neuro-symbolic reasoning). The
engineering pattern: reduce your problem to SAT/SMT, get a solver that improves for free
each year ([[np-completeness-and-reductions]] — reductions in the *useful* direction).

## Pitfalls
- Bad encodings (no Tseitin sharing, symmetric models that explode, unary vs binary
  encodings of integers); forgetting symmetry breaking.
- Quantifier triggers that never fire or loop (matching loops); trusting timeouts.
- Assuming SMT for non-linear arithmetic or strings is decidable/complete.
- Using a general SMT solver where a specialized algorithm (LP, max-flow, CSP) is
  polynomial and better.

## Related
- [[np-completeness-and-reductions]], [[p-vs-np]], [[program-verification]], [[model-checking]],
  [[complexity-theory-advanced]], [[union-find]], [[integer-representation-and-bits]],
  [[fuzzing]], [[propositional-logic]], [[first-order-logic]].

## Sources
Davis, Logemann & Loveland 1962; Marques-Silva & Sakallah (GRASP) 1996; Moskewicz et al. (Chaff) 2001; Eén & Sörensson (MiniSat) 2003; Bryant 1986; Nelson & Oppen 1979; de Moura & Bjørner 2008; *Handbook of Satisfiability* (2nd ed. 2021); Knuth TAOCP vol. 4 fasc. 6; Barrett & Tinelli "Satisfiability Modulo Theories" 2018.

---
title: Theory of computation seminal papers — Turing (1936), Church (1936), Rice (1953), Savitch (1970), Cook (1971), Karp (1972), Ladner (1975), Baker–Gill–Solovay (1975), Immerman–Szelepcsényi (1988)
type: source
section: "5.1"
level: 500
tags: [turing-1936, on-computable-numbers, entscheidungsproblem, church, lambda-calculus, effective-calculability, rice-theorem, savitch, cook-levin, karp-21-problems, ladner, np-intermediate, baker-gill-solovay, relativization, immerman-szelepcsenyi, nl-conl, history]
sources: []
authors: [Alan Turing, Alonzo Church, Henry Gordon Rice, Walter Savitch, Stephen Cook, Leonid Levin, Richard Karp, Richard Ladner, Theodore Baker, John Gill, Robert Solovay, Neil Immerman, Róbert Szelepcsényi]
year: 1936
institution: various
url: https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf
license: various
format: pdf
summary: Turing defined computable numbers as those "calculable by finite means" via a machine with finitely many m-configurations scanning a tape, proved a universal machine exists, showed the computable numbers are enumerable yet no machine decides whether a machine halts or prints infinitely many digits (diagonalization), and thereby that Hilbert's Entscheidungsproblem has no solution — with an appendix proving equivalence to Church's λ-definability (the Church–Turing thesis in embryo); Rice's theorem shows every non-trivial semantic property of programs is undecidable; Savitch showed nondeterministic space s can be simulated in deterministic space s² (so PSPACE = NPSPACE); Cook (and independently Levin) proved SAT is NP-complete by encoding a polynomial-time nondeterministic computation as a formula, and Karp showed 21 natural problems are too, establishing reductions as the tool; Ladner proved that if P ≠ NP there are NP-intermediate problems; Baker, Gill & Solovay showed there are oracles relative to which P = NP and P ≠ NP, so diagonalization alone cannot settle it; and Immerman and Szelepcsényi independently proved NL = coNL by inductive counting.
---
# Theory of computation seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936) | The machine model (m-configurations, tape, scanned symbol; "the human memory is necessarily limited"); computable numbers are enumerable; the universal machine; diagonalization applied "correctly" shows no machine decides circularity/halting; the Entscheidungsproblem is unsolvable; appendix: equivalence with Church's effective calculability | [[turing-machines]], [[decidability-and-reductions]] |
| Church, "An Unsolvable Problem of Elementary Number Theory" (1936) | λ-definability as effective calculability; the same unsolvability by a different route | [[lambda-calculus]], [[turing-machines]] |
| Rice, "Classes of Recursively Enumerable Sets and Their Decision Problems" (1953) | Any non-trivial property of the *language* (behaviour) of a program is undecidable — the theorem behind "no perfect static analysis" | [[decidability-and-reductions]], [[abstract-interpretation]] |
| Savitch, "Relationships Between Nondeterministic and Deterministic Tape Complexities" (1970) | NSPACE(s) ⊆ DSPACE(s²) by recursive reachability with a midpoint; PSPACE = NPSPACE | [[complexity-classes]] |
| Cook, "The Complexity of Theorem-Proving Procedures" (1971); Levin (1973) | SAT is NP-complete: a polynomial-time verifier's tableau encoded as a CNF formula; polynomial-time (Turing) reducibility | [[p-vs-np]], [[np-completeness-and-reductions]] |
| Karp, "Reducibility Among Combinatorial Problems" (1972) | 21 NP-complete problems (clique, vertex cover, Hamiltonian cycle, 3-coloring, knapsack, partition…) via many-one reductions; the reduction-graph picture of complexity | [[np-completeness-and-reductions]] |
| Ladner, "On the Structure of Polynomial Time Reducibility" (1975) | If P ≠ NP, NP contains problems neither in P nor NP-complete (delayed diagonalization); candidates: factoring, graph isomorphism | [[p-vs-np]] |
| Baker, Gill & Solovay, "Relativizations of the P =? NP Question" (1975) | Oracles A, B with P^A = NP^A and P^B ≠ NP^B — proof techniques that relativize (diagonalization, simulation) cannot resolve P vs NP | [[p-vs-np]], [[complexity-theory-advanced]] |
| Immerman (1988); Szelepcsényi (1988) | NL = coNL via inductive counting of reachable vertices; nondeterministic space is closed under complement | [[complexity-classes]] |

## Why read them
Turing 1936 is readable and still the best explanation of *why* the model is the right one;
Cook and Karp together are the birth of "NP-complete" as an engineer's word; Baker–Gill–
Solovay explains why the problem is still open.

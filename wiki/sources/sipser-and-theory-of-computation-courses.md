---
title: Sipser's Introduction to the Theory of Computation and MIT 18.404J/6.840J, with Barak's Introduction to Theoretical Computer Science (free), Rich, Arora & Barak (free draft), Stanford CS103/CS154, Berkeley CS172, Harvard CS121
type: source
section: "5.1"
level: 300
tags: [sipser, theory-of-computation, 18-404, 6-840, barak, introtcs, arora-barak, computational-complexity, cs103, cs154, cs172, cs121, automata, computability, complexity, textbook]
sources: []
authors: [Michael Sipser, Boaz Barak, Elaine Rich, Sanjeev Arora]
year: 2012
institution: MIT / Harvard / Princeton
url: https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/
license: mixed (Sipser commercial; Barak CC-BY-NC-ND; Arora & Barak draft free; OCW lectures CC)
format: html
summary: Sipser's book and his MIT 18.404 course (full lectures on OCW) are the canonical arc — automata and regular languages (DFA/NFA equivalence, closure, regular expressions, pumping lemma), context-free grammars and pushdown automata, Turing machines and the Church–Turing thesis, decidability and undecidability (diagonalization, the halting problem, reductions, the computation-history method, Rice's theorem, the recursion theorem), and complexity (time — P, NP, NP-completeness via Cook–Levin; space — PSPACE, Savitch, TQBF, games, L/NL and Immerman–Szelepcsényi; hierarchy theorems; oracles and relativization; BPP; interactive proofs); Barak's free Introduction to Theoretical Computer Science (Harvard CS121) reorders the story around Boolean circuits and "code as data" before automata, then Turing/RAM machines, uncomputability, restricted models, and complexity, randomized and quantum computing, and cryptography; Rich's text is the gentler alternative; Arora & Barak is the graduate complexity reference; CS103 is Stanford's proofs-and-theory gateway, CS154 the automata/complexity course, CS172 Berkeley's.
---
# Sipser and the theory-of-computation courses

## What it is
**Sipser / 18.404 (Fall 2020, 26 lectures)**: 1 introduction, finite automata, regular
expressions; 2 nondeterminism, closure properties, RE → FA; 3 the regular pumping lemma,
FA → RE, CFGs; 4 pushdown automata, CFG ↔ PDA; 5 the CF pumping lemma, Turing machines; 6 TM
variants, the Church–Turing thesis; 7 decision problems for automata and grammars; 8
undecidability; 9 reducibility; 10 the computation history method; 11 the recursion theorem and
logic; 12 time complexity; 14 P and NP, SAT, polynomial-time reducibility; 15 NP-completeness;
16 the Cook–Levin theorem; 17 space complexity, PSPACE, Savitch's theorem; 18 PSPACE-
completeness; 19 games, generalized geography; 20 L and NL, NL = coNL; 21 hierarchy theorems;
22 provably intractable problems, oracles; 23–24 probabilistic computation, BPP; 25–26
interactive proof systems, IP, coNP ⊆ IP. The book (3rd ed.) follows the same three parts —
automata and languages, computability, complexity — with the clearest proofs in print
(pumping lemmas, Cook–Levin via tableaux, Savitch).
**Barak, Introduction to Theoretical Computer Science** (Harvard CS121): 0 introduction; 1
mathematical background; 2 computation and representation; **part I finite computation** —
3 defining computation (Boolean circuits, NAND), 4 syntactic sugar and computing every finite
function, 5 code as data, data as code (universal circuits, counting lower bound); **part II
uniform computation** — 6 functions with infinite domains, automata and regular expressions,
7 loops and infinity (NAND-TM, Turing machines), 8 equivalent models (RAM, λ-calculus, cellular
automata), 9 universality and uncomputability (halting, Rice), 10 restricted computational
models (context-free grammars, semantics of programs), 11 is every theorem provable? (Gödel
via uncomputability); **part III efficient algorithms** — 12 efficient computation, 13 modeling
running time (time hierarchy, P vs EXP), 14 polynomial-time reductions, 15 NP, NP-
completeness and the Cook–Levin theorem, 16 what if P = NP?, 17 space bounded computation;
**part IV randomized computation** — 18 probability theory 101, 19 probabilistic computation,
20 modeling randomized computation (BPP, derandomization, pseudorandom generators); **part V
advanced** — 21 cryptography, 22 proofs and algorithms, 23 quantum computing.
**Arora & Barak, Computational Complexity: A Modern Approach**: the graduate sequel
([[complexity-theory-advanced]]). **Rich**: Automata, Computability and Complexity — the same
ground with many worked examples. **CS103**: sets, proofs, induction, graphs, then DFAs/
regular languages, CFGs, Turing machines, P/NP — Stanford's discrete-math-plus-theory gateway.

## Key ideas → pages
[[finite-automata-and-regular-languages]], [[context-free-grammars]], [[turing-machines]],
[[decidability-and-reductions]], [[complexity-classes]], [[p-vs-np]],
[[np-completeness-and-reductions]].

## What it adds
Sipser for the proofs; Barak for the modern framing (circuits first, "code as data" as the
recurring theme) and for being free; 18.404's videos for the lectures themselves.

---
title: Advanced complexity seminal papers — Valiant #P (1979), Håstad's switching lemma (1986), Toda (1991), Shamir IP = PSPACE (1992), the PCP theorem (Arora–Safra, ALMSS 1992/1998), Razborov–Rudich natural proofs (1994), Impagliazzo's five worlds (1995), Dinur's combinatorial PCP (2007), Williams' ACC lower bounds (2011)
type: source
section: "5.2"
level: 500
tags: [valiant, sharp-p, permanent, hastad, switching-lemma, parity-ac0, toda, polynomial-hierarchy, shamir, ip-pspace, arithmetization, pcp-theorem, arora-safra, almss, hardness-of-approximation, razborov-rudich, natural-proofs, impagliazzo, five-worlds, dinur, gap-amplification, williams, acc, algorithms-to-lower-bounds]
sources: []
authors: [Leslie Valiant, Johan Håstad, Seinosuke Toda, Adi Shamir, Sanjeev Arora, Shmuel Safra, Carsten Lund, Rajeev Motwani, Madhu Sudan, Mario Szegedy, Alexander Razborov, Steven Rudich, Russell Impagliazzo, Irit Dinur, Ryan Williams]
year: 1979
institution: various
url: https://www.wisdom.weizmann.ac.il/~dinuri/mypapers/combpcp.pdf
license: various
format: pdf
summary: Valiant defined #P and showed the permanent is #P-complete though the determinant is easy; Håstad's switching lemma proved parity needs exponential-size constant-depth circuits (parity ∉ AC⁰); Toda showed the whole polynomial hierarchy reduces to counting (PH ⊆ P^{#P}); Shamir arithmetized TQBF to prove IP = PSPACE — interactive proofs with a randomized verifier decide everything in polynomial space; the PCP theorem (Arora–Safra; Arora, Lund, Motwani, Sudan, Szegedy) showed every NP proof can be rewritten so a verifier reading O(1) random bits of it catches false proofs with constant probability (NP = PCP(log n, 1)), which is equivalent to NP-hardness of approximating MAX-3SAT and launched hardness of approximation; Razborov and Rudich explained why circuit lower-bound techniques stall — any "natural" (constructive, large) property distinguishing hard functions would break pseudorandom generators; Impagliazzo's five worlds map what the truth about average-case hardness and one-way functions would mean; Dinur reproved PCP combinatorially by gap amplification on expander-structured constraint systems, doubling the unsat-value each round; and Williams broke a 20-year stall by turning a slightly-faster satisfiability algorithm for ACC circuits into the lower bound NEXP ⊄ ACC.
---
# Advanced complexity seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Valiant, "The Complexity of Computing the Permanent" (1979) | #P: counting accepting paths; permanent is #P-complete although determinant is in P — counting can be hard when decision is easy; #P-completeness of counting perfect matchings, satisfying assignments of monotone 2-CNF | [[complexity-theory-advanced]] |
| Håstad, "Almost Optimal Lower Bounds for Small Depth Circuits" (1986); Furst–Saxe–Sipser (1984), Ajtai (1983) | **Switching lemma**: a random restriction collapses a DNF/CNF to a short decision tree with high probability; hence parity requires size 2^{Ω(n^{1/(d−1)})} at depth d — parity ∉ AC⁰ | [[circuit-complexity-and-lower-bounds]] |
| Toda, "PP is as Hard as the Polynomial-Time Hierarchy" (1991) | PH ⊆ P^{#P} (= P^{PP}): one counting oracle query simulates any constant number of quantifier alternations, via randomized reductions (Valiant–Vazirani) and arithmetization | [[complexity-theory-advanced]] |
| Shamir, "IP = PSPACE" (1992); Lund–Fortnow–Karloff–Nisan (1990) | Arithmetize TQBF into a low-degree polynomial identity checked by the sum-check protocol; the verifier needs only randomness and one prover; a non-relativizing result | [[interactive-proofs-and-pcp]] |
| Arora & Safra (1992); Arora, Lund, Motwani, Sudan & Szegedy (1992/1998) | **PCP theorem**: NP = PCP(O(log n), O(1)); equivalently there is ε > 0 such that approximating MAX-3SAT within 1+ε is NP-hard (Feige et al. for clique); proof by algebraic encodings (low-degree testing, composition) | [[interactive-proofs-and-pcp]], [[approximation-algorithms]] |
| Razborov & Rudich, "Natural Proofs" (1994) | Known lower bounds use properties that are constructive (checkable in poly time from the truth table) and large (hold for a random function); any such property separating P/poly would give a distinguisher breaking pseudorandom functions — so if strong PRFs exist, natural proofs cannot prove P ≠ NP | [[circuit-complexity-and-lower-bounds]], [[p-vs-np]] |
| Impagliazzo, "A Personal View of Average-Case Complexity" (1995) | Five worlds — Algorithmica (P = NP), Heuristica (NP hard in worst case, easy on average), Pessiland (average-case hard, no one-way functions), Minicrypt (one-way functions, no public-key), Cryptomania (public-key crypto) — organising what remains unknown | [[complexity-theory-advanced]], [[cryptography-basics]] |
| Dinur, "The PCP Theorem by Gap Amplification" (2007) | Combinatorial proof: view PCP as a constraint-satisfaction system; alternate a **graph-powering** step on an expander (doubles the unsat-value with linear blowup, raises alphabet size) with a composition step (shrinks the alphabet); O(log n) rounds give a constant gap; also near-linear-size PCPs | [[interactive-proofs-and-pcp]] |
| Williams, "Non-Uniform ACC Circuit Lower Bounds" (2011) | NEXP ⊄ ACC⁰ — first lower bound against constant-depth circuits with arbitrary MOD_m gates; method: a faster-than-brute-force satisfiability algorithm for ACC circuits (via rectangular matrix multiplication) implies the lower bound — "algorithms to lower bounds" | [[circuit-complexity-and-lower-bounds]] |

## Why read them
Shamir and the PCP papers for the arithmetization idea that reappears in modern zk-SNARKs
([[cryptography-basics]]); Razborov–Rudich for why lower bounds are stuck; Williams for the
one way out that has worked; Impagliazzo for the clearest one-page map of the open questions.

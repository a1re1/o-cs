---
title: Arora & Barak's Computational Complexity: A Modern Approach (free draft), Papadimitriou's Computational Complexity, Moore & Mertens' The Nature of Computation, Goldreich's texts, and the advanced complexity courses (MIT 6.841/18.405, Berkeley CS278, Stanford CS254, Princeton COS522)
type: source
section: "5.2"
level: 500
tags: [arora-barak, computational-complexity-modern-approach, papadimitriou, moore-mertens, nature-of-computation, goldreich, complexity-course, 6-841, 18-405, cs278, cs254, cos522]
sources: []
authors: [Sanjeev Arora, Boaz Barak, Christos Papadimitriou, Cristopher Moore, Stephan Mertens, Oded Goldreich]
year: 2009
institution: Princeton / Berkeley / Weizmann
url: https://theory.cs.princeton.edu/complexity/book.pdf
license: mixed (Arora & Barak draft free; Goldreich drafts free)
format: pdf
summary: Arora & Barak is the standard graduate text in three parts — basic classes (the model and why it doesn't matter, NP and Cook–Levin as "computation is local", diagonalization and its limits, space, the polynomial hierarchy and alternation, Boolean circuits, randomized computation, interactive proofs, cryptography, quantum computation, PCP and hardness of approximation), lower bounds on concrete models (decision trees, communication complexity, circuit lower bounds — parity ∉ AC⁰ via the switching lemma, monotone circuits, proof complexity, algebraic computation), and advanced topics (counting and #P with Toda's theorem, average-case complexity, hardness amplification and error-correcting codes, derandomization, pseudorandom constructions — expanders and extractors, the proofs of the PCP theorem, natural proofs); Papadimitriou (1994) is the earlier classic with logic and Turing-machine grounding; Moore & Mertens is the wide, readable physicist's tour (from Euclid to phase transitions and quantum computing); Goldreich's Computational Complexity: A Conceptual Perspective and his pseudorandomness/cryptography books supply the conceptual framing; the courses read these plus the primary papers.
---
# Arora & Barak and the complexity texts

## What they are
- **Arora & Barak** (2009; free 2007 draft): I *basic complexity classes* — 1 the computational
  model and why it doesn't matter; 2 NP and NP-completeness (Cook–Levin: computation is
  local; the web of reductions; decision vs search); 3 diagonalization (hierarchy theorems,
  Ladner, oracles and the limits of diagonalization); 4 space complexity; 5 the polynomial
  hierarchy and alternations; 6 Boolean circuits (P/poly, Karp–Lipton, NC and parallel
  computation); 7 randomized computation (BPP, Sipser–Gács, Adleman); 8 interactive proofs
  (IP = PSPACE, public coins, graph non-isomorphism); 9 cryptography (one-way functions,
  pseudorandom generators, zero knowledge); 10 quantum computation (Grover, Shor); 11 PCP
  theorem and hardness of approximation; II *lower bounds on concrete models* — 12 decision
  trees, 13 communication complexity, 14 circuit lower bounds (parity ∉ AC⁰, Razborov–Smolensky
  for ACC with prime moduli, monotone circuits for clique), 15 proof complexity, 16 algebraic
  computation; III *advanced topics* — 17 counting complexity (#P, permanent, Toda's theorem),
  18 average-case complexity (Levin's theory), 19 hardness amplification and error-correcting
  codes (Yao's XOR lemma, list decoding), 20 derandomization (Nisan–Wigderson, hardness vs
  randomness), 21 pseudorandom constructions (expanders, extractors, Reingold's SL = L), 22
  proofs of the PCP theorem and the Fourier transform technique (Dinur's gap amplification,
  Håstad's 3-bit PCP), 23 why are circuit lower bounds so difficult? (natural proofs).
- **Papadimitriou** (1994): logic (propositional, first-order, second-order — Fagin's theorem),
  Turing machines and undecidability, P/NP and the classic completeness results, logspace,
  randomized and parallel classes, the polynomial hierarchy, counting, cryptography, PCP.
- **Moore & Mertens, The Nature of Computation** (2011): the basics through NP-completeness,
  memory/space, optimization and approximation, randomized algorithms, the phase
  transitions in random k-SAT, counting, quantum computation — long, discursive, and full of
  physics intuition.
- **Goldreich**: *Computational Complexity: A Conceptual Perspective* (2008), *Foundations of
  Cryptography* I–II, *Pseudorandomness* — the "why these definitions" companion.
- Courses: MIT 18.405/6.841 (Williams — circuit lower bounds, algorithms-to-lower-bounds),
  Berkeley CS278, Stanford CS254 (Tan/Trevisan lineage), Princeton COS522 (Arora/Barak's own).

## Key ideas → pages
[[complexity-theory-advanced]], [[interactive-proofs-and-pcp]], [[circuit-complexity-and-lower-bounds]],
[[pseudorandomness-and-derandomization]], [[complexity-classes]], [[p-vs-np]].

## What they add
Arora & Barak is the map of everything past Sipser; Moore & Mertens is the one you can read
in bed; Goldreich tells you what the definitions are *for*.

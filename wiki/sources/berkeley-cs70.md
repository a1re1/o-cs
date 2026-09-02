---
title: Berkeley CS70 Discrete Mathematics and Probability Theory
type: source
section: "1.1"
level: 200
tags: [discrete-math, proofs, induction, modular-arithmetic, number-theory, probability-discrete, error-correcting-codes]
sources: []
institution: UC Berkeley
year: 2026
url: https://www.eecs70.org/
license: unknown
format: html
summary: Berkeley's discrete math + probability course; open lecture notes (Notes 0–25) that move fast from proof techniques through modular arithmetic, RSA, polynomials and secret sharing, graphs, countability, then a full half-semester of probability.
---
# Berkeley CS70 Discrete Mathematics and Probability Theory

## What it is
Level 200, required for Berkeley EECS. The website publishes numbered lecture notes each term; the
canonical sequence (Fall 2026 schedule, Hug & Sabin) is: direct proofs → propositional logic & proof
techniques → [[induction]] → [[modular-arithmetic]] → Euclid, Fermat's little theorem, Chinese
remainder theorem → RSA → polynomials → secret sharing & error-correcting codes (Reed–Solomon) →
graphs → countability & computability → then probability (counting, conditional probability, random
variables, expectation, variance, concentration, Markov chains, continuous distributions).

## Key ideas that differ from the MIT sequencing
- Polynomials over finite fields as a unifying tool: a degree-d polynomial is determined by d+1 points
  (Lagrange interpolation), which yields Shamir secret sharing and Reed–Solomon codes in two lectures.
  (Cross-links to [[number-theory-basics]] and to cryptography in §5.3.)
- Countability and the halting problem appear early (before probability), so students see
  diagonalization before the theory course.
- Probability is half the course, with explicit weekly quizzes; the MIT text treats it in Part IV.

## What it adds
Confirms the standard CS discrete-math core: proofs, induction, modular arithmetic/RSA, graphs, counting,
probability. Its polynomial/secret-sharing unit is the one topic not covered by [[mcs-lehman-leighton-meyer]].

---
title: Advanced complexity theory — the polynomial hierarchy, counting (#P, Toda), average-case complexity and Impagliazzo's worlds, fine-grained complexity, communication complexity, and the map of what is known
type: concept
section: "5.2"
level: 500
tags: [complexity-theory, polynomial-hierarchy, alternation, sigma-2, karp-lipton, sharp-p, permanent, toda-theorem, pp, counting-complexity, valiant-vazirani, unique-sat, average-case-complexity, distributional-problems, impagliazzo-five-worlds, one-way-functions, fine-grained-complexity, seth, 3sum, apsp, orthogonal-vectors, communication-complexity, decision-trees, proof-complexity, parameterized-complexity, quantum-complexity, bqp, complexity-zoo]
sources: [arora-barak-and-complexity-texts, complexity-theory-seminal-papers, sipser-and-theory-of-computation-courses]
summary: Beyond P, NP and PSPACE the theory refines "hard" along several axes — quantifier alternation (the polynomial hierarchy Σₖ/Πₖ, which collapses if NP ⊆ P/poly by Karp–Lipton), counting (#P, where Valiant's permanent is complete though the determinant is easy, and Toda's theorem puts the entire hierarchy inside P^{#P}), average-case hardness (Levin's distributional problems and Impagliazzo's five worlds tying it to one-way functions and cryptography), fine-grained hardness inside P (SETH, 3SUM and APSP conjectures explaining why edit distance, orthogonal vectors and many graph problems seem stuck at their textbook exponents), and concrete models where lower bounds can actually be proved (decision trees, communication complexity, proof complexity, circuits) — with quantum (BQP) and parameterized complexity as further axes; the honest summary is that almost every separation we want remains open, but the structure among the conjectures is rich and predictive.
---
# Advanced complexity theory

**In one sentence.** After P vs NP the questions multiply — how many alternations, how many
solutions, how hard on average, how hard *within* P, and in which restricted model can we
prove anything — and the answers form a web of conjectures whose consistency is itself the
evidence.

## The polynomial hierarchy (Arora & Barak ch. 5)
Σ₁ = NP, Π₁ = coNP, Σ₂ = ∃∀ (e.g. "is this the smallest circuit computing f?"), Σₖ with k
alternations; PH = ∪Σₖ ⊆ PSPACE (TQBF has unbounded alternation). Equivalent views:
alternating Turing machines (AP = PSPACE, APSPACE = EXP), oracle machines (Σ₂ = NP^NP).
If any two levels coincide the hierarchy **collapses** to that level; Σ₂ ≠ Π₂ is a standard
"unlikely" hypothesis. **Karp–Lipton**: NP ⊆ P/poly (polynomial-size circuits) ⇒ PH = Σ₂ —
why we believe SAT has no small circuits ([[circuit-complexity-and-lower-bounds]]). BPP ⊆ Σ₂
∩ Π₂ (Sipser–Gács). Structural results at this level are mostly of the form "X would collapse
PH".

## Counting: #P and Toda (ch. 17)
#P: functions counting accepting paths of an NP machine — #SAT, number of perfect matchings
= the **permanent** of a 0/1 matrix, which Valiant proved #P-complete even though the
determinant (its signed twin) is polynomial: counting can be hard when decision is easy
(perfect matching ∈ P). PP (majority of paths) is the decision face; **Toda's theorem**: PH ⊆
P^{#P} — one counting query answers any constant number of alternations, via
**Valiant–Vazirani** (isolate a unique satisfying assignment with random hash constraints:
SAT ≤ UniqueSAT under randomized reductions) and arithmetization. Approximate counting is
easier: FPRAS for #DNF, permanent of non-negative matrices (Jerrum–Sinclair–Vigoda via MCMC
— [[markov-chains]]); sampling ≈ counting (Jerrum–Valiant–Vazirani). Holographic algorithms
and dichotomy theorems classify counting CSPs.

## Average-case complexity (ch. 18; Impagliazzo 1995)
Worst-case hardness says little about typical instances. **Levin**: distributional problems
(L, D) with polynomial-time-samplable D; distNP; a complete problem (tiling); average-case
reductions must preserve distributions (domination). **Impagliazzo's five worlds**:
Algorithmica (P = NP or fast heuristics for all of NP), Heuristica (NP hard in the worst case
but easy on average — no cryptography either), Pessiland (average-case hard problems but no
one-way functions — the worst world), Minicrypt (one-way functions ⇒ private-key crypto,
signatures, PRGs), Cryptomania (public-key encryption, OT — where we hope we live). The
existence of **one-way functions** is equivalent to most of private-key cryptography
([[cryptography-basics]], [[pseudorandomness-and-derandomization]]); worst-case-to-average-
case reductions are known for lattices (Ajtai, Regev) — the basis of post-quantum crypto —
and for the permanent, PSPACE- and EXP-complete problems, but not for NP-complete problems
(Bogdanov–Trevisan barriers). Random k-SAT phase transitions (Moore & Mertens) show
"hard on average" is distribution-specific.

## Fine-grained complexity (Williams, Vassilevska Williams)
Inside P: assume **SETH** (k-SAT needs 2^{(1−o(1))n}), the **3SUM** conjecture (no n^{2−ε}),
the **APSP** conjecture (no n^{3−ε}); then via fine-grained reductions: **orthogonal vectors**
needs n^{2−o(1)} (SETH), hence edit distance, LCS, Fréchet distance, regex matching, and
diameter (approx.) cannot be solved in truly subquadratic time; APSP-equivalent problems
(negative triangle, radius, replacement paths); 3SUM-hard geometry. Explains why decades of
[[dynamic-programming]] textbook bounds are tight and guides which speedups to attempt
([[string-algorithms]], [[shortest-paths]]). Companion: **parameterized complexity** (FPT vs
W[1]-hard: vertex cover is 2ᵏ·n, clique is not unless FPT = W[1]; ETH gives tight exponents
like no 2^{o(k)} for vertex cover; treewidth) — [[np-completeness-and-reductions]].

## Concrete models and lower bounds (part II)
Where proofs exist: **decision-tree complexity** (evasiveness, sensitivity — Huang 2019
proved the sensitivity conjecture), **communication complexity** (Yao's two-party model;
equality needs n bits deterministically, O(log n) randomized; set disjointness Ω(n) even
randomized — lower bounds for streaming ([[streaming-and-sketching]]), data structures, VLSI,
and circuits via Karchmer–Wigderson), **proof complexity** (resolution lower bounds for
pigeonhole — why SAT solvers struggle on some instances, [[sat-and-smt-solvers]]), **algebraic
complexity** (VP vs VNP — permanent vs determinant, Valiant's algebraic P vs NP), and
**circuit lower bounds** ([[circuit-complexity-and-lower-bounds]]). Interactive proofs and
PCPs ([[interactive-proofs-and-pcp]]) and derandomization
([[pseudorandomness-and-derandomization]]) are the other pillars. Quantum: BQP contains
factoring, sits in PP (and PSPACE); relative to oracles BQP ⊄ PH (Raz–Tal 2018)
([[quantum-computing]]).

## The picture (what is known vs conjectured)
Proven separations come only from diagonalization across large gaps (P ≠ EXP, NL ≠ PSPACE),
from restricted circuit classes (AC⁰, ACC, monotone), and from concrete models.
Conjectured: P ≠ NP ≠ coNP, PH infinite, P = BPP, NP ⊄ P/poly, SETH, one-way functions
exist, P ≠ PSPACE. The consistency of this web — each conjecture implying or explaining
others — is the field's working confidence, and the Complexity Zoo lists 500+ classes
mapping it.

## Pitfalls
- Reading "#P-hard" as "NP-hard" (it's much stronger — PH ⊆ P^{#P}).
- Applying worst-case results to average-case claims (or cryptography) without a reduction.
- Ignoring fine-grained lower bounds and hunting subquadratic edit distance.
- Believing a collapse result is a separation (Karp–Lipton is conditional).

## Related
- [[complexity-classes]], [[p-vs-np]], [[interactive-proofs-and-pcp]],
  [[circuit-complexity-and-lower-bounds]], [[pseudorandomness-and-derandomization]],
  [[np-completeness-and-reductions]], [[cryptography-basics]], [[markov-chains]],
  [[quantum-computing]], [[streaming-and-sketching]].

## Sources
Arora & Barak ch. 5, 12–13, 15–18; Valiant 1979; Toda 1991; Impagliazzo 1995; Vassilevska Williams "On some fine-grained questions in algorithms and complexity" (2018); Papadimitriou ch. 17–18; Moore & Mertens ch. 14.

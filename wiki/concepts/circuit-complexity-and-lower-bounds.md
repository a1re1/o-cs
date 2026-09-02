---
title: Circuit complexity and lower bounds — P/poly, NC and AC, parity ∉ AC⁰ via the switching lemma, monotone lower bounds, natural proofs, and algorithms-to-lower-bounds
type: concept
section: "5.2"
level: 500
tags: [circuit-complexity, boolean-circuits, non-uniform, p-poly, advice, karp-lipton, nc, ac0, acc0, tc0, parallel-computation, circuit-lower-bounds, parity, switching-lemma, random-restrictions, hastad, razborov-smolensky, polynomial-method, monotone-circuits, clique, approximation-method, natural-proofs, razborov-rudich, pseudorandom-functions, williams, algorithms-to-lower-bounds, nexp-acc, formula-size, khrapchenko, shannon-counting-argument, gct]
sources: [arora-barak-and-complexity-texts, complexity-theory-seminal-papers]
summary: Circuits (AND/OR/NOT gates, one circuit per input length) are the non-uniform model where lower bounds ought to be provable — Shannon's counting argument shows almost every function needs 2ⁿ/n gates, yet the best explicit lower bound for a function in NP is barely above 3n; the structured classes NC (polylog depth, parallel algorithms), AC⁰ (constant depth, unbounded fan-in), ACC⁰ (plus MOD gates), TC⁰ (threshold gates — neural-network-like) are where results exist: Håstad's switching lemma (a random restriction collapses any small-depth circuit to a shallow decision tree) proves parity needs exponential-size constant-depth circuits, Razborov–Smolensky's polynomial method handles MOD_p gates, Razborov's approximation method gives superpolynomial monotone lower bounds for clique; the reason progress stalls is Razborov–Rudich's natural-proofs barrier — any lower-bound property that is constructive and holds for most functions would distinguish pseudorandom functions from random ones — and the way around it so far is Williams' program: a faster-than-2ⁿ satisfiability algorithm for a circuit class implies that NEXP has no small circuits in that class, which gave NEXP ⊄ ACC⁰ in 2011.
---
# Circuit complexity and lower bounds

**In one sentence.** Count the gates instead of the steps, hope that a fixed input length
makes hardness provable — and learn that the tools that work on tiny classes are exactly the
ones that cannot work on the big ones.

## The model (Arora & Barak ch. 6)
A circuit family {Cₙ} with size s(n) and depth d(n) computes a function per input length;
**non-uniform** — the family may be arbitrary per n (equivalently, Turing machines with
polynomial **advice**, P/poly). P ⊆ P/poly (unroll the tableau); P/poly contains undecidable
unary languages, so it's about counting gates, not computability. **Karp–Lipton**: NP ⊆ P/poly
⇒ PH = Σ₂, so NP ⊄ P/poly is the expected route to P ≠ NP — and Shannon (1949) shows a random
function needs Θ(2ⁿ/n) gates, so hard functions are everywhere; explicit ones are the
problem (best known: ~3.1n for functions in NP, Find et al. 2016). Formula size (fan-out 1):
n² for parity (Khrapchenko), n³ for Andreev's function (Håstad); KRW conjecture would give
superpolynomial formulas. **Parallel classes**: NCⁱ = polynomial size, O(logⁱ n) depth (NC =
"efficiently parallelizable" — [[parallel-programming-models]]); NC¹ ⊆ L ⊆ NL ⊆ NC² ⊆ P;
P-complete problems (circuit value, LP) are believed inherently sequential. **AC⁰** (constant
depth, unbounded fan-in AND/OR): addition, but not parity or majority; **ACC⁰** adds MOD_m
gates; **TC⁰** adds majority/threshold gates — computes multiplication, division, and is the
natural class of constant-depth neural networks ([[neural-network-training]]); TC⁰ vs NP is
open (we can't even show NEXP ⊄ TC⁰).

## Parity ∉ AC⁰: the switching lemma (Håstad 1986; ch. 14)
**Random restriction**: fix each variable to 0/1 with probability 1 − p, leave it free with
probability p. **Switching lemma**: a k-DNF hit by a random p-restriction becomes a decision
tree of depth ≥ t with probability ≤ (5pk)ᵗ — so a bottom layer of ANDs/ORs "switches" to the
other kind, letting two layers merge. Iterating d − 1 times with p ≈ n^{−1/d} collapses a
size-s depth-d circuit to a constant-depth-tree function of n^{1/d}·Ω(1) still-free variables,
but parity on any free variables is still parity — contradiction unless s ≥ 2^{Ω(n^{1/(d−1)})}.
Corollaries: AC⁰ can't compute majority; PARITY ∉ AC⁰ relativizes to an oracle separating PH
from PSPACE; AC⁰ is learnable and fooled by polylog-independence (Braverman) —
[[pseudorandomness-and-derandomization]]. **Razborov–Smolensky** (1987): circuits with MOD_p
gates are approximated by low-degree polynomials over F_p, but MOD_q (q ≠ p) and majority are
not — so parity ∉ AC⁰[MOD 3]; the **polynomial method**, which also underlies Williams'
algorithms and modern algorithm design.

## Monotone circuits (Razborov 1985; ch. 14.3)
Without NOT gates, the **approximation method** shows CLIQUE needs 2^{Ω(n^{1/3})} monotone
gates (Alon–Boppana): replace each gate by an approximating "plausible" function via the
sunflower lemma, track how many test inputs each step can mis-classify. Tardos: a monotone
function in P (via Lovász theta) needs exponential monotone circuits — so monotone lower
bounds don't transfer to general circuits. Communication-complexity views (Karchmer–
Wigderson: depth = communication complexity of a relation) give monotone depth bounds
(matching needs Ω(n) monotone depth).

## Why we're stuck: natural proofs (Razborov & Rudich 1994; ch. 23)
Examine the known techniques: each identifies a property of Boolean functions that (1)
**constructive** — decidable in time polynomial in the truth table 2ⁿ, (2) **large** — holds
for a random function with noticeable probability, (3) **useful** — fails for every function
with small circuits in the class. Theorem: a natural property useful against P/poly would
distinguish a **pseudorandom function** (which looks random but has small circuits) from a
truly random one, breaking PRFs, hence one-way functions with 2^{n^ε} security. So if
cryptography is possible, P ≠ NP has no natural proof; the switching lemma and approximation
method are natural, which is why they stop at AC⁰/monotone. Together with relativization
and algebrization ([[p-vs-np]]) this delimits every known technique; GCT (geometric
complexity theory — Mulmuley) and proofs exploiting non-largeness are the proposed escapes.

## The way out that worked: algorithms to lower bounds (Williams 2011)
Contrapositive strategy: if a class C had circuits for every NEXP language, then
nondeterministic exponential-time machines could guess small circuits and simulate them;
a **circuit-satisfiability algorithm for C running in 2ⁿ/n^{ω(1)}** would then let you decide
NEXP faster than the nondeterministic time hierarchy allows. Williams gave such an algorithm
for ACC⁰ (via Yao–Beigel–Tarui's representation of ACC circuits as symmetric functions of
polynomials plus fast rectangular matrix multiplication and dynamic programming), yielding
**NEXP ⊄ ACC⁰** — the first new frontier in 20 years; extended to NQP ⊄ ACC⁰ (Murray–Williams
2018). Moral: designing algorithms *is* proving lower bounds; the "hardness magnification"
line shows tiny improvements would separate major classes. This is not a natural proof (it
isn't large).

## Pitfalls
- Confusing uniform (P) and non-uniform (P/poly) statements; P/poly ⊄ decidable.
- Assuming monotone or restricted-depth bounds transfer to general circuits.
- Trying to prove P ≠ NP with a large, constructive property (Razborov–Rudich says no).
- Thinking "no known small circuit" is a lower bound.

## Related
- [[complexity-theory-advanced]], [[p-vs-np]], [[pseudorandomness-and-derandomization]],
  [[complexity-classes]], [[digital-logic-and-the-alu]], [[parallel-programming-models]],
  [[neural-network-training]], [[sat-and-smt-solvers]].

## Sources
Arora & Barak ch. 6, 14, 23; Håstad 1986; Razborov 1985; Razborov & Smolensky 1987; Razborov & Rudich 1994; Williams 2011 (abstract read); Jukna, Boolean Function Complexity; Shannon 1949.

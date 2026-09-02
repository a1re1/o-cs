---
title: Interactive proofs and probabilistically checkable proofs — IP = PSPACE by arithmetization and sum-check, zero knowledge, the PCP theorem, and hardness of approximation
type: concept
section: "5.2"
level: 500
tags: [interactive-proofs, ip, prover-verifier, completeness-soundness, arthur-merlin, public-coins, graph-non-isomorphism, arithmetization, sum-check-protocol, ip-pspace, shamir, mip, mip-nexp, zero-knowledge, pcp-theorem, pcp-log-n-1, probabilistically-checkable-proofs, gap-problems, hardness-of-approximation, max-3sat, label-cover, unique-games-conjecture, hastad-3-bit-pcp, dinur-gap-amplification, expanders, low-degree-testing, linearity-testing, snarks, verifiable-computation]
sources: [arora-barak-and-complexity-texts, complexity-theory-seminal-papers]
summary: Letting a polynomial-time verifier flip coins and talk to an all-powerful but untrusted prover changes what "proof" means: interactive proofs (completeness — true statements convince; soundness — false ones almost never do) capture graph non-isomorphism, and Shamir's IP = PSPACE shows they decide everything in polynomial space by arithmetizing a quantified formula into a low-degree polynomial and running the sum-check protocol, where the verifier checks a claimed sum by asking for univariate restrictions and testing at random points; zero-knowledge proofs convince without revealing anything beyond truth, and multi-prover proofs reach NEXP; the PCP theorem (NP = PCP(O(log n), O(1))) says every NP witness can be re-encoded so a verifier reading a constant number of randomly chosen bits rejects false proofs with constant probability — proved algebraically (low-degree and linearity testing plus composition) and later combinatorially by Dinur's gap amplification on expander graphs — and, being equivalent to the NP-hardness of distinguishing satisfiable MAX-3SAT instances from those where a constant fraction of clauses must fail, it is the engine of hardness of approximation (Håstad's optimal 7/8 for MAX-3SAT, label cover, the unique games conjecture) and the theoretical ancestor of succinct verifiable computation and zk-SNARKs.
---
# Interactive proofs and PCPs

**In one sentence.** Give the verifier randomness and let the proof be a conversation — or a
long string of which it reads a few bits — and "checkable proof" grows from NP to PSPACE and
turns approximation into a hardness question with a constant gap.

## Interactive proofs (Arora & Barak ch. 8; 18.404 L25–26)
Verifier V (probabilistic polynomial time) exchanges messages with prover P (unbounded).
L ∈ **IP** if: **completeness** — x ∈ L ⇒ some prover makes V accept with probability ≥ 2/3;
**soundness** — x ∉ L ⇒ every prover convinces V with probability ≤ 1/3. NP is the one-message,
deterministic case. **Graph non-isomorphism** ∈ IP (V randomly permutes one of the two graphs
and asks which it was — a prover can only answer reliably if they are non-isomorphic) though
GNI is not known to be in NP. Public-coin (Arthur–Merlin, AM) vs private-coin: equivalent up to
rounds (Goldwasser–Sipser); AM[k] = AM[2] for constants k. GNI ∈ AM implies graph
isomorphism is not NP-complete unless PH collapses.

## IP = PSPACE (Shamir 1992; LFKN 1990)
IP ⊆ PSPACE by computing the optimal prover. For PSPACE ⊆ IP: **arithmetize** a TQBF formula —
∧ → ×, ∨ → 1 − (1−a)(1−b), ¬ → 1 − x, ∀x → ∏_{x∈{0,1}}, ∃x → 1 − ∏(1 − ·), over a large prime
field, with degree reduction so polynomials stay low-degree — then the formula is true iff a
polynomial expression equals a nonzero value. The **sum-check protocol**: to verify
Σ_{x₁…xₙ ∈ {0,1}} g(x) = K, the prover sends the univariate g₁(X) = Σ_{x₂…} g(X, x₂, …); V checks
g₁(0) + g₁(1) = K, picks random r₁, and recurses on g(r₁, ·); after n rounds V evaluates g at a
random point itself. Soundness by Schwartz–Zippel: a lying prover must send a wrong low-
degree polynomial that agrees with the truth at a random point with probability ≤ d/|F|
([[randomized-algorithms]], [[polynomial-identity-testing]]). Consequences: **non-relativizing**
(so arithmetization escapes Baker–Gill–Solovay, until algebrization); coNP ⊆ IP (#SAT via
sum-check); **MIP = NEXP** (two non-communicating provers; MIP* = RE, 2020, for entangled
provers). Sum-check is now the core of practical **verifiable computation** (GKR, SNARKs —
[[cryptography-basics]]).

## Zero knowledge (Goldwasser, Micali & Rackoff 1985)
An interactive proof is zero-knowledge if the verifier's view can be simulated without the
prover — it learns nothing but the truth of the statement. Graph isomorphism and 3-coloring
have perfect/computational ZK proofs (the latter using commitments — so every NP statement
has a ZK proof if one-way functions exist); NIZK with a common reference string; the
cryptographic side is in [[cryptography-basics]].

## The PCP theorem (Arora–Safra, ALMSS 1992; ch. 11, 22)
**PCP(r, q)**: verifier uses r random bits, reads q bits of a proof, complete and sound (error
≤ 1/2). Trivially NP = PCP(0, poly). **Theorem**: NP = PCP(O(log n), O(1)) — every NP
statement has a polynomially long proof of which reading a *constant* number of bits (3 with
Håstad's optimal construction) detects falsehood with constant probability. Proof ingredients
(algebraic route): encode assignments with error-correcting codes (Hadamard/Reed–Muller —
[[channel-capacity-and-error-correction]]), **linearity testing** (BLR: f(x)+f(y) = f(x+y) on
random x, y — Fourier analysis) and **low-degree testing**, arithmetize the constraints, then
**proof composition** (a PCP verifier's own check is verified by an inner PCP) to reduce
query complexity. **Dinur's route** (2007): a PCP is a constraint graph; define unsat(G) =
min fraction of violated constraints; alternate (a) preprocessing to a constant-degree
**expander**, (b) **graph powering** G^t — constraints on walks of length t — which multiplies
unsat by ~√t at the cost of a larger alphabet, (c) alphabet reduction by composition with a
constant-size assignment tester; O(log n) rounds double the gap each time from 1/n to a
constant with linear blowup per round. Near-linear PCPs (n·polylog n) follow.

## Hardness of approximation
Equivalent form: there is ε > 0 such that it is NP-hard to distinguish satisfiable 3SAT
instances from those where every assignment violates ≥ ε of the clauses — so no PTAS for
MAX-3SAT unless P = NP (the **gap** problem is hard). From this, gap-preserving reductions
give: **Håstad (2001)** MAX-3SAT hard to approximate beyond 7/8 + ε (matching the trivial random
assignment — [[approximation-algorithms]]), clique hard within n^{1−ε}, set cover within
(1−ε) ln n (Feige/Dinur–Steurer), vertex cover within 1.36 (Dinur–Safra), label cover and
parallel repetition (Raz) as the standard starting points; the **unique games conjecture**
(Khot 2002) would make many known algorithms optimal (Goemans–Williamson's 0.878 for MAX-CUT,
2 for vertex cover) — 2-to-2 games proved (2018), UGC itself open. The theorem thus draws the
exact boundary between §3.3's approximation algorithms and impossibility.

## Pitfalls
- Confusing IP's randomness (essential) with NP's determinism; forgetting soundness must hold
  against *every* prover.
- Reading PCP as "proofs are short" — they are longer; the *verification* is local.
- Assuming approximation hardness transfers without a gap-preserving reduction.
- Treating UGC-based hardness as unconditional.

## Related
- [[complexity-theory-advanced]], [[p-vs-np]], [[approximation-algorithms]],
  [[randomized-algorithms]], [[cryptography-basics]], [[channel-capacity-and-error-correction]],
  [[expander-graphs]], [[polynomial-identity-testing]].

## Sources
Arora & Barak ch. 8, 11, 22; Shamir 1992; Lund, Fortnow, Karloff & Nisan 1990; Goldwasser, Micali & Rackoff 1985; Arora & Safra 1998; ALMSS 1998; Dinur 2007 (abstract and §1 read); Håstad 2001; Khot 2002; 18.404 L25–26.

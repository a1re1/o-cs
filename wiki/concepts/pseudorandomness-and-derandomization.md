---
title: Pseudorandomness and derandomization — BPP vs P, pseudorandom generators from hardness (Nisan–Wigderson), expanders, extractors, k-wise independence, and the hardness-vs-randomness trade
type: concept
section: "5.2"
level: 500
tags: [pseudorandomness, derandomization, bpp, rp, zpp, pseudorandom-generators, nisan-wigderson, hardness-vs-randomness, impagliazzo-wigderson, yao-xor-lemma, hardness-amplification, k-wise-independence, pairwise-independence, method-of-conditional-expectations, small-bias-spaces, expander-graphs, expander-walks, extractors, min-entropy, seeded-extractors, reingold-sl-l, polynomial-identity-testing, kabanets-impagliazzo, cryptographic-prg, blum-micali-yao, list-decoding, error-correcting-codes]
sources: [arora-barak-and-complexity-texts, complexity-theory-seminal-papers]
summary: Randomized algorithms (BPP) are believed to be no more powerful than deterministic ones because randomness can be manufactured: a pseudorandom generator stretches a short seed into a long string no small circuit can distinguish from random, and Nisan–Wigderson build one from any function that is hard on average for small circuits (using combinatorial designs so the seed is reused), with Impagliazzo–Wigderson's hardness amplification (Yao's XOR lemma, list-decodable codes) showing that if E needs exponential circuits then P = BPP — hardness versus randomness, with the converse Kabanets–Impagliazzo result that derandomizing polynomial identity testing would itself prove circuit lower bounds; unconditional tools derandomize specific algorithms — pairwise/k-wise independence and the method of conditional expectations for MAX-CUT and hashing, small-bias spaces, expander walks that reduce error with few random bits, and extractors that purify weak randomness — while Reingold's SL = L (undirected reachability in log space via the zig-zag product) is the flagship unconditional result, and cryptographic PRGs (Blum–Micali–Yao, from one-way functions) are the same idea with security against all polynomial-time adversaries.
---
# Pseudorandomness and derandomization

**In one sentence.** Randomness is a resource you can usually fake — provably, if you have a
hard function to fake it from, and unconditionally for the specific structures most
algorithms actually use.

## Randomized classes and the conjecture (Arora & Barak ch. 7)
RP (one-sided error), coRP, ZPP = RP ∩ coRP (expected polynomial time), **BPP** (two-sided
bounded error; amplify by repetition — Chernoff, [[probability-and-statistics-for-cs]]);
BPP ⊆ P/poly (Adleman: a good random string exists for all inputs of length n), BPP ⊆ Σ₂ ∩ Π₂
(Sipser–Gács). Examples that were in BPP before P: primality (AKS 2002), and still: polynomial
identity testing (Schwartz–Zippel — [[polynomial-identity-testing]]). Conjecture: **P = BPP** —
supported by the hardness-vs-randomness connection below; the practical view is that
randomness matters for *efficiency* of specific algorithms ([[randomized-algorithms]]) more
than for the class.

## Pseudorandom generators from hardness (ch. 20; Nisan–Wigderson 1994)
A **PRG** G: {0,1}^ℓ → {0,1}^n **ε-fools** circuits of size s if |Pr[C(G(z)) = 1] − Pr[C(U) = 1]| ≤ ε.
If a PRG with ℓ = O(log n) fooling size-n^c circuits is computable in poly(n) time, then BPP = P:
enumerate all 2^ℓ seeds. **Nisan–Wigderson**: given f hard on average for size-s circuits
(no circuit agrees with f on more than 1/2 + ε of inputs), take a combinatorial **design**
of sets S₁…Sₙ ⊂ [ℓ] with small pairwise intersections and output f(z|S₁)…f(z|Sₙ); a
distinguisher yields a next-bit predictor (Yao), which after fixing the other seed bits
becomes a small circuit approximating f. **Impagliazzo–Wigderson (1997)**: if some language in
E = DTIME(2^{O(n)}) requires circuits of size 2^{Ω(n)} (worst-case), then P = BPP — via
**hardness amplification**: worst-case → mild average-case (self-correction using
error-correcting codes / low-degree extension), mild → strong via **Yao's XOR lemma**
(direct product, list-decodable codes — [[channel-capacity-and-error-correction]]). Trade-off
curve: stronger hardness ↔ more derandomization. Converse (**Kabanets–Impagliazzo 2004**):
a deterministic polynomial-time PIT algorithm implies either NEXP ⊄ P/poly or the permanent
has no polynomial-size arithmetic circuits — derandomization *is* lower bounds
([[circuit-complexity-and-lower-bounds]]). Cryptographic PRGs (Blum–Micali, Yao, HILL: from
any one-way function) must fool *all* polynomial-time tests with polynomial stretch, so they
need poly-time seeds; complexity-theoretic PRGs may take longer than their adversaries.

## Unconditional derandomization tools (ch. 21)
- **Pairwise / k-wise independence**: hash families (a·x + b mod p) give n pairwise-independent
  bits from O(log n) truly random ones; enough for expectation/variance arguments — Chebyshev-
  based algorithms, universal hashing ([[hash-tables]]), MAX-CUT's ½-approximation by
  enumerating a pairwise-independent space; k-wise independence fools AC⁰ (Braverman 2010).
- **Method of conditional expectations**: fix random bits one at a time keeping the
  conditional expectation of the objective ≥ its mean — derandomizes the probabilistic
  method ([[approximation-algorithms]], MAX-3SAT 7/8).
- **Small-bias spaces** (Naor–Naor): fool all parity tests with O(log n) seed; ε-biased sets
  from codes.
- **Expander graphs** ([[expander-graphs]]): constant-degree graphs with spectral gap; a random
  walk of length t uses log n + O(t) random bits yet the fraction of steps in a bad set of
  density β is ≈ β with exponentially small deviation (expander Chernoff) — error reduction
  for BPP with few random bits; explicit constructions (Margulis, Ramanujan/LPS, **zig-zag
  product** of Reingold–Vadhan–Wigderson).
- **Extractors**: functions Ext(x, seed) that output nearly uniform bits from any source with
  enough **min-entropy** (weak physical randomness, or as a tool for PRGs via Trevisan's
  construction from list-decodable codes); dispersers, condensers, two-source extractors
  (Chattopadhyay–Zuckerman 2016).
- **Reingold's theorem (2005)**: SL = L — undirected s–t connectivity in deterministic log
  space, by repeatedly zig-zag-powering the graph into an expander whose diameter is
  logarithmic, then exhaustively searching short paths ([[graph-search]],
  [[complexity-classes]]). Derandomizes the random-walk algorithm of Aleliunas et al.

## Practical face
Pseudorandom number generators in software (Mersenne Twister, PCG, xoshiro — statistical,
not cryptographic) vs CSPRNGs (ChaCha20, /dev/urandom — [[cryptography-basics]]); hashing-
based sketches rely on limited independence ([[streaming-and-sketching]]); Monte Carlo
simulation and quasi-random (low-discrepancy) sequences ([[monte-carlo-methods]]); property
testing and locally testable codes descend from the same toolbox.

## Pitfalls
- Using a statistical PRNG where an adversary exists; seeding from time.
- Assuming full independence is needed when pairwise suffices (and vice versa —
  Chernoff needs more than pairwise).
- Reading P = BPP as "randomized algorithms are pointless" — the polynomial can be worse.
- Confusing extractors (need a seed or two sources) with deterministic "randomness from
  nothing" (impossible from a single weak source in general).

## Related
- [[complexity-theory-advanced]], [[circuit-complexity-and-lower-bounds]], [[randomized-algorithms]],
  [[expander-graphs]], [[polynomial-identity-testing]], [[hash-tables]],
  [[channel-capacity-and-error-correction]], [[cryptography-basics]], [[monte-carlo-methods]].

## Sources
Arora & Barak ch. 7, 19–21; Nisan & Wigderson 1994; Impagliazzo & Wigderson 1997; Kabanets & Impagliazzo 2004; Reingold 2005; Vadhan, Pseudorandomness (2012); Hoory, Linial & Wigderson "Expander graphs and their applications" (2006).

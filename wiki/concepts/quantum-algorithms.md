---
title: Quantum algorithms — Deutsch–Jozsa, Bernstein–Vazirani and Simon (query complexity), the quantum Fourier transform and phase estimation, Shor's factoring via period finding, Grover's search and its optimality (BBBV), amplitude amplification, Hamiltonian simulation, HHL, variational algorithms, and BQP
type: concept
section: "5.6"
level: 500
tags: [quantum-algorithms, query-complexity, oracle, deutsch-jozsa, bernstein-vazirani, simon-algorithm, hidden-subgroup, quantum-fourier-transform, qft, phase-estimation, period-finding, order-finding, shor-algorithm, factoring, discrete-log, continued-fractions, grover-algorithm, amplitude-amplification, bbbv, quantum-lower-bounds, polynomial-method, adversary-method, quantum-walks, hamiltonian-simulation, hhl, linear-systems, vqe, qaoa, variational, bqp, qma, quantum-supremacy, random-circuit-sampling, speedups, dequantization]
sources: [quantum-computing-texts-and-courses]
summary: Quantum speedups come from interference over structured problems: in the query model Deutsch–Jozsa, Bernstein–Vazirani and Simon show exponential separations from classical algorithms by putting a function's global property (constant vs balanced, a hidden linear string, a hidden XOR period) into the phases and reading it out with Hadamards; the quantum Fourier transform (O(n²) gates for 2ⁿ amplitudes) and phase estimation generalize this, and Shor's algorithm factors N by reducing to finding the period of aˣ mod N, computing it in superposition, applying the QFT and reading the period from a measurement via continued fractions — polynomial time against the best classical subexponential — which also breaks discrete logs and elliptic curves; Grover's algorithm searches N unstructured items in O(√N) queries by rotating amplitude toward marked states, provably optimal (BBBV), giving only quadratic speedups for NP problems and generalizing to amplitude amplification and estimation; Hamiltonian simulation (Feynman's original motivation, now with optimal algorithms), quantum walks, and HHL for linear systems (with caveats and later dequantization) round out the provable toolkit, while NISQ-era variational algorithms (VQE, QAOA) trade guarantees for feasibility; the class BQP sits between BPP and PSPACE, and supremacy experiments demonstrate separation on sampling tasks, not useful problems.
---
# Quantum algorithms

**In one sentence.** Every quantum speedup is an interference pattern: encode a global
property of many function values into phases, transform so that wrong answers cancel, and
measure — exponentially for periodic/algebraic structure (Shor), quadratically for
unstructured search (Grover), and provably not at all for much else.

## Query complexity and the first separations (Aaronson L17–18; de Wolf ch. 2–3)
Oracle model: a black box U_f : |x⟩|b⟩ → |x⟩|b ⊕ f(x)⟩; count queries. **Phase kickback**:
querying with |−⟩ in the target puts (−1)^{f(x)} on |x⟩. **Deutsch–Jozsa**: is f constant or
balanced? Classically 2ⁿ⁻¹+1 queries deterministically; quantumly one — H^{⊗n}, query,
H^{⊗n}, measure: all-zeros iff constant (but randomized classical needs O(1) — the separation
is only against deterministic). **Bernstein–Vazirani**: f(x) = s·x — one query reveals s (the
Hadamards implement the Fourier transform over Z₂ⁿ). **Simon**: f(x) = f(x ⊕ s) — O(n) queries
vs classical Ω(2^{n/2}) even randomized: query, measure the output register, the input
register is a superposition of x and x⊕s; H^{⊗n} yields a random y with y·s = 0; n−1 such
equations give s (Gaussian elimination — [[matrices-and-linear-maps]]). This is the exponential
separation that inspired Shor: Simon's problem is period finding over Z₂ⁿ.

## The QFT, phase estimation, and Shor (Aaronson L19–21; N&C ch. 5)
**QFT** over Z_N: |x⟩ → (1/√N) Σ_y e^{2πixy/N}|y⟩ — implemented with O(n²) Hadamards and
controlled phase rotations (vs classical FFT's O(N log N) on 2ⁿ numbers — [[fft]]; but you
cannot read out the amplitudes, only sample). **Phase estimation**: given U and eigenvector
|u⟩ with eigenvalue e^{2πiφ}, estimate φ to n bits with controlled-U^{2ᵏ} and an inverse QFT.
**Shor** (1994): to factor N, pick random a; the order r of a mod N (aʳ ≡ 1) gives a factor
via gcd(a^{r/2} ± 1, N) with probability ≥ 1/2 ([[number-theory-algorithms]]); find r by
preparing Σ|x⟩|aˣ mod N⟩ (modular exponentiation in superposition — the dominant cost),
measuring the second register (the first collapses to a periodic superposition with period
r), applying the QFT, and measuring y ≈ k·2ⁿ/r; **continued fractions** recover r from y/2ⁿ.
Total O(n³) gates (n = log N) vs the number field sieve's exp(O(n^{1/3})) — the reason for
post-quantum migration ([[public-key-cryptography]]); resource estimates: ~20 million noisy
qubits for RSA-2048 in hours (Gidney–Ekerå 2019), falling with better codes. The same
machinery solves discrete log (including elliptic curves) and the abelian **hidden subgroup
problem**; the non-abelian HSP (graph isomorphism, lattice problems via dihedral HSP) resists
— why lattices are the post-quantum bet.

## Grover and amplitude amplification (Aaronson L22–23; N&C ch. 6)
Unstructured search among N items with one marked: classical Θ(N), quantum **O(√N)**:
start from uniform superposition; repeat ~ (π/4)√N times: phase-flip marked items (oracle),
then reflect about the mean (diffusion H^{⊗n}(2|0⟩⟨0| − I)H^{⊗n}); each iteration rotates the
state by ~2/√N toward the marked subspace (a rotation in a 2-D plane — the clean geometric
proof). **BBBV** (Bennett, Bernstein, Brassard, Vazirani 1997): Ω(√N) queries are necessary —
so relative to an oracle NP ⊄ BQP, and quantum computers give at most quadratic speedups for
brute-force NP search (3SAT: 2^{n/2}); no exponential speedup for generic NP problems.
Generalizations: **amplitude amplification** (boost any success probability p to ~1 in
O(1/√p) — quadratic speedups for many randomized algorithms), **amplitude/phase estimation**
for counting (quadratic speedup for Monte Carlo — [[monte-carlo-methods]]), collision
finding (N^{1/3}), element distinctness (N^{2/3}, quantum walks), minimum finding, and
Grover on symmetric crypto (AES-128 → 2⁶⁴; hence AES-256). Lower-bound methods: the
**polynomial method** (acceptance probability is a low-degree polynomial in the input bits)
and the **adversary method** (Ambainis) — [[complexity-theory-advanced]].

## Simulation, linear algebra, and heuristics (de Wolf ch. 9–11; Preskill)
**Hamiltonian simulation** — Feynman's reason for quantum computers: evolving e^{−iHt} for
local H with Trotter–Suzuki product formulas, then qubitization/quantum signal processing
(optimal): chemistry (FeMoco, catalysts), materials, lattice field theory — the most
credible exponential-advantage application. **HHL** (2009): prepare |x⟩ ∝ A⁻¹|b⟩ in polylog
time given sparse well-conditioned A and quantum access to b — with caveats (state
preparation, readout, condition number; Aaronson's "fine print") and **dequantization**
(Tang 2018: classical sampling algorithms match several "quantum ML" speedups). Quantum
walks (exponential speedup on the glued-trees graph; element distinctness). **NISQ
heuristics**: **VQE** (variational eigensolver — parameterized circuit + classical
optimizer), **QAOA** (approximate optimization with alternating cost/mixer unitaries); no
proven advantage, barren plateaus, noise limits depth ([[quantum-error-correction-and-nisq]]).
Sampling-based supremacy (random circuit sampling, boson sampling) is hard classically
(assuming the polynomial hierarchy doesn't collapse) but not useful.

## Complexity (Aaronson L24; de Wolf ch. 13)
**BQP**: bounded-error quantum polynomial time. BPP ⊆ BQP ⊆ PP ⊆ PSPACE (Adleman–DeMarrais–
Huang; simulation by summing amplitudes — Feynman path integral); relative to oracles
BQP ⊄ PH (Raz–Tal 2018) and NP ⊄ BQP (BBBV); factoring ∈ BQP but not believed NP-complete
([[p-vs-np]]). **QMA** = quantum NP (local Hamiltonian problem is QMA-complete — Kitaev);
QIP = PSPACE; MIP* = RE. Postselection: PostBQP = PP (Aaronson) — explains why sampling is
hard.

## Pitfalls
- Claiming exponential speedups for search/optimization (Grover is quadratic; BBBV is tight).
- Ignoring state preparation and readout costs (HHL, quantum ML).
- Treating NISQ heuristics as algorithms with guarantees.
- Confusing "supremacy" on sampling with useful advantage.

## Related
- [[quantum-computing]], [[quantum-error-correction-and-nisq]], [[public-key-cryptography]],
  [[number-theory-algorithms]], [[fft]], [[complexity-classes]], [[p-vs-np]],
  [[complexity-theory-advanced]], [[monte-carlo-methods]], [[matrices-and-linear-maps]].

## Sources
Shor 1994/1997 (abstract read); Grover 1996; BBBV 1997; Simon 1994; Deutsch & Jozsa 1992; Aaronson lecture notes 17–24; de Wolf ch. 2–13; Nielsen & Chuang ch. 5–6; Harrow, Hassidim & Lloyd 2009; Tang 2018; Gidney & Ekerå 2019.

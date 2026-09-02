---
title: Quantum computing fundamentals — qubits and amplitudes, measurement, unitary gates and circuits, entanglement and Bell states, no-cloning, teleportation and superdense coding, mixed states, and BB84 key distribution
type: concept
section: "5.6"
level: 400
tags: [quantum-computing, qubit, amplitudes, superposition, measurement, born-rule, bloch-sphere, unitary, quantum-gates, hadamard, pauli-gates, cnot, toffoli, phase-gate, t-gate, universal-gate-set, quantum-circuits, tensor-product, entanglement, bell-states, epr, bell-inequality, chsh, nonlocal-games, no-cloning, teleportation, superdense-coding, mixed-states, density-matrix, decoherence, interference, quantum-parallelism, reversible-computing, extended-church-turing-thesis, bb84, quantum-key-distribution, quantum-money, qiskit, simulation-cost]
sources: [quantum-computing-texts-and-courses]
summary: A qubit's state is a unit vector of complex amplitudes (α|0⟩ + β|1⟩; n qubits need 2ⁿ amplitudes, which is why classical simulation is exponential) that evolves by unitary (reversible, norm-preserving) gates — Hadamard, Pauli X/Y/Z, phase/T, CNOT, Toffoli; a small set is universal — and collapses on measurement to an outcome with probability |amplitude|² (Born rule), so quantum computation is "probability with minus signs": amplitudes interfere, and algorithms arrange for wrong answers to cancel; entanglement (Bell states like (|00⟩+|11⟩)/√2) gives correlations no local classical model can produce (Bell/CHSH inequality, nonlocal games), the no-cloning theorem forbids copying unknown states (and enables BB84 quantum key distribution and quantum money), teleportation moves a qubit with two classical bits plus a shared Bell pair, superdense coding sends two bits with one qubit, mixed states and density matrices describe partial knowledge and decoherence — and the whole model challenges the extended Church–Turing thesis without changing what is computable.
---
# Quantum computing fundamentals

**In one sentence.** Replace probabilities with complex amplitudes that can cancel, keep
evolution reversible, and pay 2ⁿ numbers to describe n bits — then look for problems where
the cancellation can be engineered.

## Qubits, amplitudes, measurement (Aaronson L2–3; N&C ch. 1–2)
A classical probabilistic bit is a vector (p₀, p₁) with p ≥ 0, Σp = 1, evolved by stochastic
matrices; a **qubit** is α|0⟩ + β|1⟩ with complex α, β, |α|² + |β|² = 1, evolved by
**unitary** matrices (U†U = I — norm-preserving, hence reversible; [[matrices-and-linear-maps]]).
**Measurement** in the computational basis gives 0 with probability |α|², 1 with |β|² (**Born
rule**) and leaves the qubit in the outcome; measuring in other bases is a rotation first.
Global phase is unobservable; relative phase is everything (|+⟩ = (|0⟩+|1⟩)/√2 vs |−⟩ differ
only in sign yet are orthogonal). The **Bloch sphere** pictures a qubit as a point on a
sphere. n qubits: the **tensor product** space of dimension 2ⁿ — a state is 2ⁿ amplitudes, so
describing 300 qubits exceeds atoms in the universe; that is the resource, and the reason
simulating quantum systems is hard classically (Feynman's motivation).

## Gates and circuits (Aaronson L4, L16; N&C ch. 4)
Single-qubit: Pauli **X** (NOT), **Z** (phase flip), Y, **Hadamard** H = (1/√2)[[1,1],[1,−1]]
(creates superposition; H² = I), phase S, **T** = diag(1, e^{iπ/4}). Two-qubit: **CNOT**
(reversible XOR, creates entanglement with H), controlled-U, SWAP; **Toffoli** (CCNOT) is
universal for reversible classical computation — any classical circuit runs on a quantum
computer with ancillas and uncomputation (garbage must be uncomputed to allow interference).
**Universal gate sets**: {H, T, CNOT} approximates any unitary (Solovay–Kitaev: polylog
overhead); Clifford gates alone ({H, S, CNOT}) are classically simulable (Gottesman–Knill) —
T gates are the expensive resource. Circuits: wires = qubits, time left to right; **quantum
parallelism** — applying U_f to a superposition evaluates f on all inputs at once, but
measuring returns one random value; algorithms need **interference** to concentrate
amplitude on the answer ([[quantum-algorithms]]). Quantum Zeno effect; the cost of
simulation (state-vector 2ⁿ, tensor networks for low entanglement).

## Entanglement and nonlocality (Aaronson L10–14)
**Bell states**: |Φ⁺⟩ = (|00⟩+|11⟩)/√2 — not a product state; measuring one qubit fixes the
other's outcome regardless of distance, yet no information is transmitted (no-signalling:
the marginal is uniform). **Bell/CHSH inequality**: local hidden-variable theories win the
CHSH game with probability ≤ 3/4; quantum strategies reach cos²(π/8) ≈ 0.854 — experimentally
confirmed (Aspect; loophole-free 2015; Nobel 2022): the world is not locally realistic.
**Nonlocal games**, device-independent randomness ("Einstein-certified"), MIP* = RE
([[interactive-proofs-and-pcp]]). Entanglement is a resource: measures (entropy of
entanglement), monogamy; GHZ states.

## No-cloning and its uses (Aaronson L7–10; BB84)
**No-cloning theorem**: no unitary maps |ψ⟩|0⟩ → |ψ⟩|ψ⟩ for all ψ (linearity: it would have to
clone superpositions incorrectly). Consequences: no classical-style backups or fan-out of
quantum data; error correction must be cleverer ([[quantum-error-correction-and-nisq]]);
**quantum money** (Wiesner) and **BB84 quantum key distribution** — Alice sends qubits in
random bases, Bob measures in random bases, they publicly compare bases and keep matching
ones; an eavesdropper must measure and disturbs the states detectably (information-
disturbance trade-off) — security from physics, not computational assumptions
([[cryptography-basics]]; deployed over fiber and satellite, limited by distance/trusted
nodes). **Teleportation**: with a shared Bell pair, Alice's Bell measurement plus 2 classical
bits lets Bob reconstruct her qubit (the original is destroyed — consistent with no-cloning);
entanglement swapping builds quantum repeaters. **Superdense coding**: one qubit + shared
entanglement carries 2 classical bits (the dual). Holevo's bound: n qubits carry at most n
classical bits without prior entanglement.

## Mixed states and decoherence (Aaronson L6; N&C ch. 2.4, 8)
Uncertainty about which pure state: **density matrix** ρ = Σ pᵢ|ψᵢ⟩⟨ψᵢ|; measurement
probabilities Tr(Πρ); unitary evolution UρU†; the reduced state of half an entangled pair is
maximally mixed (I/2) — entanglement with the environment looks like noise; **decoherence**
is the leakage of a system's phase information into the environment, turning superpositions
into mixtures — the enemy every physical implementation fights (T1/T2 times; superconducting
transmons, trapped ions, photonics, neutral atoms). General noise as quantum channels (Kraus
operators); fidelity and trace distance.

## Where it fits
Computability is unchanged (a classical computer can simulate any quantum one — slowly);
efficiency may not be: Shor's factoring is the challenge to the **extended Church–Turing
thesis** ([[turing-machines]], [[quantum-algorithms]]); BQP ⊆ PSPACE ([[complexity-classes]]).
Programming: Qiskit/Cirq/Q#/PennyLane build circuits, transpile to hardware gate sets and
connectivity, run on simulators and cloud devices; classical control and hybrid variational
loops dominate NISQ practice.

## Pitfalls
- "Tries all answers at once": parallelism without interference yields a random answer.
- Faster-than-light communication from entanglement (no-signalling forbids it).
- Treating qubits as classical bits with probabilities (missing the sign/phase).
- Expecting exponential speedups generically — they exist for specific structures
  ([[quantum-algorithms]]).

## Related
- [[quantum-algorithms]], [[quantum-error-correction-and-nisq]], [[matrices-and-linear-maps]],
  [[complexity-classes]], [[cryptography-basics]], [[public-key-cryptography]],
  [[probability-and-statistics-for-cs]], [[interactive-proofs-and-pcp]].

## Sources
Aaronson lecture notes 1–16; Nielsen & Chuang ch. 1–2, 4, 8; de Wolf ch. 1–2, 15; Bennett & Brassard 1984; Deutsch 1985; Preskill Ph219 ch. 2–4.

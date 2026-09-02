---
title: Quantum error correction and the road to fault tolerance — why errors are continuous but correctable, the 3-qubit, Shor and Steane codes, stabilizer codes, the surface/toric code, the threshold theorem, magic states, NISQ devices, supremacy experiments, and hardware platforms
type: concept
section: "5.6"
level: 500
tags: [quantum-error-correction, qec, decoherence, bit-flip, phase-flip, discretization-of-errors, syndrome-measurement, 3-qubit-code, shor-code, steane-code, css-codes, stabilizer-codes, stabilizer-formalism, gottesman-knill, toric-code, surface-code, topological, kitaev, logical-qubit, code-distance, threshold-theorem, fault-tolerance, magic-state-distillation, t-gates, transversal-gates, eastin-knill, qldpc, nisq, preskill, error-mitigation, quantum-supremacy, random-circuit-sampling, sycamore, superconducting-qubits, transmon, trapped-ions, neutral-atoms, photonics, coherence-times, gate-fidelity, decoders, resource-estimates]
sources: [quantum-computing-texts-and-courses]
summary: Quantum states decohere and gates are imperfect, and no-cloning forbids naive redundancy, yet Shor and Steane showed in 1995–96 that errors can be corrected: entangle the logical qubit with ancillas, measure stabilizers (parity checks) that reveal the error syndrome without revealing the state, and because measurement discretizes continuous errors into Pauli X/Z flips, correcting those suffices — the 3-qubit codes fix one type each, Shor's 9-qubit code both, Steane's 7-qubit CSS code and the stabilizer formalism generalize classical linear codes; Kitaev's toric/surface code arranges qubits on a lattice with local checks, tolerates ~1 % physical error, and is what superconducting and neutral-atom roadmaps use (Google's 2023–24 below-threshold demonstrations); the threshold theorem says arbitrarily long computation is possible if physical error rates are below a constant, at polylog overhead, with non-Clifford T gates supplied by magic-state distillation (the dominant cost, thousands of physical qubits per logical); meanwhile Preskill's NISQ era — 50–1000 noisy qubits without correction, error mitigation, variational algorithms, and sampling-based supremacy experiments — explores what unprotected devices can do while trapped ions, superconducting transmons, neutral atoms and photonics compete on coherence, fidelity, connectivity and scale.
---
# Quantum error correction and NISQ

**In one sentence.** You cannot copy a qubit, and its errors are continuous — and error
correction works anyway, because measuring the right parities collapses any error into a
few discrete flips you can undo without ever learning the state.

## Why it seemed impossible, and why it isn't (N&C ch. 10; Aaronson L27)
Obstacles: no-cloning (no triplicate-and-vote), errors are continuous rotations (not just
flips), and measuring to check destroys the superposition. Resolution: encode |ψ⟩ = α|0⟩ +
β|1⟩ into an entangled **logical qubit** across several physical ones; measure **stabilizer**
operators (e.g. Z₁Z₂, Z₂Z₃ — parities) whose outcomes (the **syndrome**) identify *which*
qubit was flipped but reveal nothing about α, β; the measurement **discretizes** any error
(a small rotation becomes "no error" or "X on qubit 2" with some probabilities) —
correcting Pauli errors X, Z (and Y = iXZ) suffices for everything (they span all
single-qubit operators).
- **3-qubit bit-flip code**: |0⟩ → |000⟩, |1⟩ → |111⟩ corrects one X; the **phase-flip code**
  uses |+++⟩/|−−−⟩ (Hadamard basis) for one Z.
- **Shor's 9-qubit code** (1995): concatenate them — corrects any single-qubit error.
- **Steane's 7-qubit code** (1996): a **CSS code** built from the classical Hamming code
  ([[channel-capacity-and-error-correction]]) — corrects one error, and Clifford gates act
  **transversally** (bitwise), which is why it's fault-tolerance friendly.
- **Stabilizer formalism** (Gottesman): a code is the joint +1 eigenspace of commuting Pauli
  operators; [[n, k, d]] parameters (n physical, k logical, distance d corrects ⌊(d−1)/2⌋
  errors); the quantum Hamming/Singleton bounds; **Gottesman–Knill**: stabilizer circuits
  are classically simulable (so error-correction bookkeeping is cheap; magic comes from T).

## Topological codes and the threshold (Kitaev; Preskill Ph219 ch. 7)
**Toric/surface code**: qubits on lattice edges; stabilizers are 4-body local checks
(vertex X-type, plaquette Z-type); logical operators are non-contractible loops; distance d
grows with lattice size; errors form chains detected at their endpoints and corrected by
matching (minimum-weight perfect matching — [[network-flow]]; neural/union-find decoders for
speed). **Threshold ~1 %** per gate — the highest of practical codes — with only nearest-
neighbour connectivity: the architecture of choice for superconducting and neutral-atom
machines. **Threshold theorem** (Aharonov–Ben-Or, Kitaev, Knill–Laflamme–Zurek 1996–98):
if physical error rate p < p_th, concatenated/topological codes achieve logical error rates
decreasing exponentially in code distance with polylogarithmic overhead — arbitrarily long
reliable computation, the quantum analogue of von Neumann's reliable computation from
unreliable components. Costs: **Eastin–Knill** — no code has a universal transversal gate
set, so non-Clifford **T gates** need **magic-state distillation** (prepare noisy |T⟩
states, distill to high fidelity with many copies) — the dominant space-time cost (a
logical qubit at distance ~25 needs ~1000 physical qubits; RSA-2048 ~ millions of physical
qubits). Newer **qLDPC codes** (2020s) promise constant-rate encoding with long-range
connectivity (IBM's bivariate bicycle codes). Experiments: Google 2023 (distance-3 vs 5
surface code, logical error improving with size), 2024 Willow (below threshold, d=7);
Quantinuum/Harvard–QuEra logical qubits on ions/neutral atoms (2023–24).

## NISQ (Preskill 2018) and supremacy
**Noisy Intermediate-Scale Quantum**: 50–1000 qubits without error correction; gate errors
10⁻²–10⁻³ limit circuit depth to hundreds of gates; useful for exploring many-body physics,
possibly for optimization/chemistry heuristics — Preskill's warning that "quantum computers
with 50–100 qubits may be able to perform tasks which surpass today's classical computers,
but noise … will limit the size of circuits that can be executed reliably". Techniques:
**error mitigation** (zero-noise extrapolation, probabilistic error cancellation, symmetry
verification — reduce bias at exponential sampling cost, not scalable), variational
algorithms (VQE/QAOA — [[quantum-algorithms]]), circuit compilation for connectivity and
noise. **Quantum supremacy/advantage**: Arute et al. 2019 — Sycamore's 53 qubits sampled
random circuits in 200 s, claimed 10,000 years classically; tensor-network simulations
later cut that to days/hours (an arms race — [[parallel-programming-models]]); boson sampling
(USTC Jiuzhang); these are sampling tasks with no known use but rest on solid complexity
assumptions ([[complexity-theory-advanced]]). Practical advantage for a useful problem (likely
chemistry/materials simulation) is the open milestone; error-corrected machines are the
2030s target per most roadmaps.

## Hardware platforms
| Platform | Qubit | Strengths | Challenges |
|---|---|---|---|
| Superconducting (Google, IBM, Rigetti) | transmon circuits at ~15 mK | fast gates (ns), lithographic scaling | short coherence (~100 μs), 2D nearest-neighbour, cryogenics, wiring |
| Trapped ions (Quantinuum, IonQ) | hyperfine states of ions | highest fidelities (99.9 %+), all-to-all within a trap, long coherence | slow gates (μs–ms), scaling traps/shuttling |
| Neutral atoms (QuEra, Pasqal, Atom Computing) | Rydberg atoms in optical tweezers | thousands of qubits, reconfigurable connectivity | gate fidelity, atom loss, speed |
| Photonics (PsiQuantum, Xanadu) | photons | room temperature, networking | probabilistic gates, loss |
| Spins in silicon, topological (Majorana) | | CMOS compatibility / intrinsic protection | early stage / contested |
Control stacks: classical FPGAs/ASICs for pulses and real-time decoding ([[microcontrollers-and-embedded-programming]]), compilers (Qiskit, Cirq, tket) for routing and error-aware
scheduling ([[compilers-overview]]).

## Pitfalls
- "Errors are analog so QEC can't work" (discretization by syndrome measurement).
- Counting physical qubits as logical ones; ignoring T-gate and decoding costs.
- Treating error mitigation as error correction.
- Reading supremacy headlines as practical advantage; ignoring classical algorithm
  improvements.

## Related
- [[quantum-computing]], [[quantum-algorithms]], [[channel-capacity-and-error-correction]],
  [[raid-and-erasure-coding]] (classical analogue), [[network-flow]], [[complexity-theory-advanced]],
  [[public-key-cryptography]], [[microcontrollers-and-embedded-programming]].

## Sources
Shor 1995; Steane 1996; Gottesman 1997; Kitaev 2003; Aharonov & Ben-Or 1997; Preskill 2018 (abstract read); Arute et al. 2019; Nielsen & Chuang ch. 10; Preskill Ph219 ch. 7; Aaronson L27; Google Quantum AI 2023/2024 (Nature); Gidney & Ekerå 2019.

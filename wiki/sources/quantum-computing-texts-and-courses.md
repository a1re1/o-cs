---
title: Quantum computing texts, courses and seminal papers — Nielsen & Chuang, Aaronson's lecture notes (free), de Wolf's notes (free), Preskill's Ph219 notes (free), the Qiskit textbook, Hidary, Yanofsky & Mannucci, MIT 8.370 / Berkeley CS191; Deutsch (1985), BB84 (1984), Shor (1994), Grover (1996), Shor/Steane codes (1995–96), Kitaev's toric code, Preskill's NISQ (2018), Arute et al. quantum supremacy (2019)
type: source
section: "5.6"
level: 400
tags: [nielsen-chuang, mike-and-ike, aaronson, quantum-computing-since-democritus, de-wolf-notes, preskill-notes, ph219, qiskit-textbook, hidary, yanofsky-mannucci, 8-370, cs191, deutsch, bb84, bennett-brassard, shor, grover, steane, kitaev, toric-code, nisq, quantum-supremacy, arute, sycamore]
sources: []
authors: [Michael Nielsen, Isaac Chuang, Scott Aaronson, Ronald de Wolf, John Preskill, Jack Hidary, Noson Yanofsky, Mirco Mannucci, David Deutsch, Charles Bennett, Gilles Brassard, Peter Shor, Lov Grover, Andrew Steane, Alexei Kitaev, Frank Arute]
year: 2000
institution: various
url: https://www.scottaaronson.com/qclec.pdf
license: mixed (Aaronson, de Wolf, Preskill notes and Qiskit textbook free)
format: pdf
summary: Nielsen & Chuang ("Mike and Ike") is the reference — fundamentals (qubits, quantum circuits, the quantum Fourier transform, quantum search, physical realizations), quantum information (noise and quantum operations, distance measures, error correction, entropy, information theory); Aaronson's Quantum Information Science notes (free) build from probability theory to quantum mechanics as "probability with minus signs" through mixed states, no-cloning, quantum money and QKD, superdense coding and teleportation, Bell inequalities and nonlocal games, universal gate sets, query complexity (Deutsch–Jozsa, Bernstein–Vazirani, Simon), RSA and Shor via the QFT and continued fractions, Grover and the BBBV lower bound, quantum complexity theory, Hamiltonians and the adiabatic algorithm, and error correction; de Wolf's notes are the compact rigorous CS treatment (algorithms, complexity, error correction, cryptography, lower bounds); Preskill's Ph219 notes go deepest on error correction and fault tolerance; the Qiskit textbook and Hidary teach by programming real devices; and the seminal papers are Deutsch's universal quantum computer, BB84 key distribution, Shor's factoring and discrete-log algorithm ("a digital computer is generally believed to be an efficient universal computing device … this may not be true when quantum mechanics is taken into consideration"), Grover's √N search, the Shor and Steane codes, Kitaev's topological toric code, Preskill's NISQ framing (50–100 noisy qubits, useful before fault tolerance), and Google's Sycamore supremacy experiment.
---
# Quantum computing texts, courses and seminal papers

## What they are
- **Nielsen & Chuang** (2000/2010): I fundamentals — introduction, quantum mechanics
  (postulates, density operators), computer science background; II quantum computation —
  quantum circuits (universal gates, simulation), the quantum Fourier transform and its
  applications (phase estimation, order finding, factoring, discrete log, hidden subgroup),
  quantum search (Grover, counting, speeding up NP problems, optimality), physical
  realizations (harmonic oscillator, optical, ion trap, NMR); III quantum information —
  quantum noise and quantum operations, distance measures, quantum error correction
  (3-qubit codes, Shor code, stabilizer codes, fault tolerance, threshold theorem), entropy,
  quantum information theory (Holevo bound, Schumacher compression, channel capacity).
- **Aaronson, Introduction to Quantum Information Science** (lecture notes, free): 1 the
  extended Church–Turing thesis; 2 probability theory and QM; 3 basic rules of QM; 4 gates
  and circuits, quantum Zeno; 5 distinguishability, multi-qubit states; 6 mixed states; 7
  Bloch sphere, no-cloning; 8 quantum money and QKD; 9 superdense coding; 10 teleportation,
  entanglement swapping, GHZ; 11 quantifying entanglement; 12 interpretations; 13 hidden
  variables and Bell's inequality; 14 nonlocal games; 15 Einstein-certified randomness;
  16 universal gate sets; 17 query complexity and Deutsch–Jozsa; 18 Bernstein–Vazirani and
  Simon; 19 RSA and Shor; 20 the QFT; 21 continued fractions and Shor wrap-up; 22 Grover;
  23 BBBV and Grover applications; 24 quantum complexity theory; 25 Hamiltonians; 26 the
  adiabatic algorithm; 27 quantum error correction; plus *Quantum Computing Since Democritus*.
- **de Wolf, Quantum Computing: Lecture Notes** (free, CWI/Amsterdam): the quantum model,
  simple algorithms, Simon's algorithm, the QFT, Shor, hidden subgroup problem, Grover,
  amplitude amplification and estimation, HHL, quantum walks, Hamiltonian simulation, query
  lower bounds (polynomial and adversary methods), complexity (BQP, QMA), error correction,
  quantum cryptography (BB84, uncloneability), communication complexity.
- **Preskill, Ph219/CS219 notes** (free): foundations, density matrices, entanglement,
  quantum algorithms, quantum error correction (stabilizer formalism, toric code, threshold),
  quantum information theory. **Qiskit textbook** and **Hidary, Quantum Computing: An
  Applied Approach**: circuits on hardware, variational algorithms (VQE, QAOA), noise.
  **Yanofsky & Mannucci**: for programmers, linear algebra first. Courses: MIT 8.370/18.435
  (Shor, Chuang), Berkeley CS191 (Vazirani).
- **Seminal papers**: Deutsch 1985 (universal quantum computer, quantum parallelism);
  Bennett & Brassard 1984 (BB84 QKD from no-cloning); Shor 1994/1997 (polynomial-time
  factoring and discrete log — the abstract questions the extended Church–Turing thesis);
  Grover 1996 (O(√N) unstructured search); Shor 1995 and Steane 1996 (first QEC codes,
  showing decoherence is correctable); Kitaev 1997/2003 (toric code, topological QC);
  Preskill 2018 (NISQ); Arute et al. 2019 (Sycamore: 53 qubits, random circuit sampling in
  200 s vs claimed 10,000 years — later reduced by classical improvements).

## Key ideas → pages
[[quantum-computing]], [[quantum-algorithms]], [[quantum-error-correction-and-nisq]],
[[public-key-cryptography]] (why Shor matters), [[complexity-classes]] (BQP).

## What they add
Aaronson for intuition ("QM is probability with minus signs"), de Wolf for the rigorous CS
core in 200 pages, Nielsen & Chuang for everything, Preskill for error correction, Qiskit
for touching a device.

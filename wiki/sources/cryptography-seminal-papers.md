---
title: Cryptography seminal papers — Diffie & Hellman (1976), RSA (1978), Merkle (1979), Shamir secret sharing (1979), Goldwasser & Micali (1984), Goldwasser–Micali–Rackoff zero knowledge (1985), Yao garbled circuits (1986), Bellare & Rogaway random oracles (1993), Shor (1994), Regev LWE (2005), Gentry FHE (2009), Groth16 (2016), Signal's Double Ratchet, TLS 1.3 (RFC 8446)
type: source
section: "5.3"
level: 500
tags: [diffie-hellman, new-directions, rsa, merkle, merkle-tree, merkle-puzzles, shamir-secret-sharing, goldwasser-micali, probabilistic-encryption, semantic-security, zero-knowledge, gmr, yao, garbled-circuits, millionaires-problem, bellare-rogaway, random-oracle-model, shor-algorithm, regev, lwe, learning-with-errors, gentry, fully-homomorphic-encryption, groth16, zk-snarks, signal, double-ratchet, x3dh, tls-1-3, rfc-8446]
sources: []
authors: [Whitfield Diffie, Martin Hellman, Ron Rivest, Adi Shamir, Leonard Adleman, Ralph Merkle, Shafi Goldwasser, Silvio Micali, Charles Rackoff, Andrew Yao, Mihir Bellare, Phillip Rogaway, Peter Shor, Oded Regev, Craig Gentry, Jens Groth, Trevor Perrin, Moxie Marlinspike, Eric Rescorla]
year: 1976
institution: various
url: https://ee.stanford.edu/~hellman/publications/24.pdf
license: various
format: pdf
summary: Diffie and Hellman announced "a revolution in cryptography" — public-key cryptosystems that need no secure key-distribution channel, digital signatures, and the key-exchange protocol over discrete logarithms; RSA realized public-key encryption and signatures from factoring; Merkle gave puzzles, hash trees and hash-based signatures; Shamir's polynomial secret sharing split a secret among n parties so any t reconstruct; Goldwasser & Micali defined semantic security and showed encryption must be randomized; Goldwasser, Micali & Rackoff defined zero-knowledge proofs and interactive proof systems; Yao's garbled circuits made any function securely computable by two mutually distrusting parties; Bellare & Rogaway's random-oracle model gave a heuristic for proving practical schemes (OAEP, FDH); Shor's quantum algorithm factors and takes discrete logs in polynomial time, dooming RSA/DH once large quantum computers exist; Regev's learning-with-errors problem, with a worst-case-to-average-case reduction from lattice problems, became the basis of post-quantum encryption (Kyber) and of Gentry's first fully homomorphic encryption scheme (computing on ciphertexts via bootstrapping); Groth16 gave the shortest zk-SNARKs; and the Double Ratchet (Signal) and TLS 1.3 are the protocols in which all of this reaches billions of devices.
---
# Cryptography seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Diffie & Hellman, "New Directions in Cryptography" (1976) | "We stand today on the brink of a revolution": cheap digital hardware; teleprocessing needs systems that minimize secure key channels and supply the equivalent of a written signature; **public-key cryptosystems** and **one-way authentication**; the DH key exchange over discrete logs; computational complexity as the foundation ("changing this ancient art into a science") | [[public-key-cryptography]], [[cryptography-basics]] |
| Rivest, Shamir & Adleman, "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems" (1978) | Trapdoor permutation from factoring: e·d ≡ 1 mod φ(N); encryption and signatures; textbook RSA is insecure without padding | [[public-key-cryptography]], [[number-theory-algorithms]] |
| Merkle, "Secrecy, Authentication, and Public Key Systems" (1979); "Protocols for Public Key Cryptosystems" (1980) | Merkle puzzles (the first public-key idea, 1974), **hash trees** (Merkle trees), one-time signatures and hash-based signatures | [[hash-functions-cryptographic]], [[git-data-model]] |
| Shamir, "How to Share a Secret" (1979); Blakley (1979) | (t, n) threshold sharing with a degree-(t−1) polynomial; information-theoretic; the basis of threshold signatures and MPC | [[cryptographic-protocols-and-zero-knowledge]] |
| Goldwasser & Micali, "Probabilistic Encryption" (1984) | **Semantic security** / indistinguishability; deterministic public-key encryption cannot be secure; encryption from quadratic residuosity | [[cryptography-basics]], [[public-key-cryptography]] |
| Goldwasser, Micali & Rackoff, "The Knowledge Complexity of Interactive Proof Systems" (1985) | Interactive proofs; **zero knowledge** via simulation; quadratic residuosity ZK proof | [[cryptographic-protocols-and-zero-knowledge]], [[interactive-proofs-and-pcp]] |
| Yao, "How to Generate and Exchange Secrets" (1986) | The millionaires' problem; **garbled circuits** + oblivious transfer ⇒ secure two-party computation of any function | [[cryptographic-protocols-and-zero-knowledge]] |
| Bellare & Rogaway, "Random Oracles are Practical" (1993) | Model hash functions as random functions to prove practical schemes (OAEP, FDH, Fiat–Shamir); Canetti–Goldreich–Halevi showed schemes secure only in the ROM | [[hash-functions-cryptographic]], [[cryptography-basics]] |
| Shor, "Algorithms for Quantum Computation: Discrete Logarithms and Factoring" (1994) | Quantum period finding via the QFT breaks RSA, DH, ECC in polynomial time — the reason for post-quantum migration | [[quantum-computing]], [[public-key-cryptography]] |
| Regev, "On Lattices, Learning with Errors, Random Linear Codes, and Cryptography" (2005) | **LWE**: solving noisy linear equations mod q is as hard as worst-case approximate lattice problems (quantumly); public-key encryption from LWE; basis of Kyber/ML-KEM, Dilithium, FHE | [[public-key-cryptography]] |
| Gentry, "Fully Homomorphic Encryption Using Ideal Lattices" (2009) | Somewhat-homomorphic scheme + **bootstrapping** (homomorphically evaluate its own decryption) ⇒ arbitrary computation on ciphertexts; BGV/BFV/CKKS/TFHE followed | [[cryptographic-protocols-and-zero-knowledge]] |
| Groth, "On the Size of Pairing-Based Non-interactive Arguments" (2016) | 3-group-element **zk-SNARK** with a trusted setup (QAP arithmetization, pairings); Zcash, rollups; PLONK/STARKs remove or universalize the setup | [[cryptographic-protocols-and-zero-knowledge]] |
| Perrin & Marlinspike, "The Double Ratchet Algorithm" and X3DH (Signal, 2016) | Asynchronous authenticated key agreement (X3DH) then per-message keys from a DH ratchet + symmetric KDF ratchet: forward secrecy and post-compromise security; WhatsApp, Signal, Messenger | [[cryptographic-protocols-and-zero-knowledge]] |
| Rescorla, RFC 8446 TLS 1.3 (2018) | 1-RTT handshake, (EC)DHE only (forward secrecy), AEAD only, 0-RTT resumption, formally analyzed (Tamarin, ProVerif) | [[dns-http-and-the-web-stack]], [[cryptographic-protocols-and-zero-knowledge]] |

## Why read them
Diffie–Hellman for the vision (and its clarity), Goldwasser–Micali for what "secure" must
mean, GMR and Yao for the two ideas (zero knowledge, garbling) that became industries,
Shor and Regev for why the public-key layer is being replaced.

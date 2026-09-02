---
title: Boneh & Shoup's A Graduate Course in Applied Cryptography (free), Katz & Lindell, Rosulek's The Joy of Cryptography (free), Goldreich's Foundations, Aumasson's Serious Cryptography, Wong's Real-World Cryptography, Cryptopals, and Stanford CS255 / MIT 6.875 / Berkeley CS276 / UMD CMSC456
type: source
section: "5.3"
level: 400
tags: [boneh-shoup, cryptobook, katz-lindell, introduction-to-modern-cryptography, joy-of-cryptography, rosulek, goldreich, foundations-of-cryptography, serious-cryptography, aumasson, real-world-cryptography, wong, cryptopals, cs255, boneh-coursera, 6-875, cs276, cmsc456, katz]
sources: []
authors: [Dan Boneh, Victor Shoup, Jonathan Katz, Yehuda Lindell, Mike Rosulek, Oded Goldreich, Jean-Philippe Aumasson, David Wong]
year: 2023
institution: Stanford / MIT / Oregon State
url: https://toc.cryptobook.us/
license: mixed (Boneh & Shoup and Rosulek free; Cryptopals free)
format: pdf
summary: Boneh & Shoup's free graduate text is the reference — part I secret-key (encryption, stream ciphers, block ciphers, chosen-plaintext attacks, message integrity from universal and collision-resistant hashing, authenticated encryption), part II public-key (tools, encryption, CCA security, signatures, fast signatures from one-way functions, elliptic curves and pairings, attacks on number-theoretic assumptions, post-quantum lattices), part III protocols (identification and login, sigma protocols, zero knowledge, authenticated key exchange, threshold cryptography, secure multi-party computation) — every construction carrying a game-based security definition and reduction; Katz & Lindell is the undergraduate provable-security text (private-key then public-key, with the reductions spelled out); Rosulek's Joy of Cryptography (free) teaches the same "define, construct, prove by hybrids" discipline with library-style code; Goldreich's Foundations is the theory (one-way functions → PRGs → PRFs → encryption, signatures, zero knowledge, general MPC); Aumasson and Wong are the practitioner's tours (what's actually deployed and how it breaks); Cryptopals is the hands-on attack course (48 challenges from XOR to padding oracles to RSA); CS255 (Boneh's Coursera Crypto I/II) and 6.875 (Vaikuntanathan/Goldwasser) are the reference courses.
---
# Boneh & Shoup and the cryptography texts

## What they are
- **Boneh & Shoup** (2023 draft, free): 1 introduction; **I secret-key** — 2 encryption
  (perfect secrecy, semantic security), 3 stream ciphers (PRGs, security as
  indistinguishability, RC4/Salsa/ChaCha), 4 block ciphers (PRPs, AES, DES, Feistel, Luby–
  Rackoff), 5 chosen-plaintext attacks (modes: CBC, CTR; nonce-based encryption), 6 message
  integrity (MACs, PRF-based, CBC-MAC, PMAC), 7 integrity from universal hashing (Carter–
  Wegman, Poly1305, GMAC), 8 integrity from collision-resistant hashing (Merkle–Damgård,
  SHA-2/3, HMAC), 9 authenticated encryption (encrypt-then-MAC, GCM, ChaCha20-Poly1305,
  padding-oracle and other attacks); **II public-key** — 10 public-key tools (trapdoor
  permutations, DH, CDH/DDH, hardness), 11 public-key encryption (ElGamal, RSA-OAEP, hybrid
  encryption/KEMs), 12 CCA-secure PKE (Cramer–Shoup, Fujisaki–Okamoto), 13 digital signatures
  (RSA-FDH, PSS, Schnorr, ECDSA/EdDSA), 14 signatures from one-way functions (Lamport,
  Merkle, hash-based/SPHINCS), 15 elliptic curves and pairings (BLS, IBE), 16 attacks on
  number-theoretic assumptions (factoring, discrete log — index calculus, Pollard rho), 17
  post-quantum from lattices (LWE, Regev, Kyber-style); **III protocols** — 18 identification
  and login (passwords, one-time passwords, challenge–response), 19 sigma protocols
  (Schnorr identification, Fiat–Shamir), 20 proving properties in zero knowledge, 21
  authenticated key exchange (TLS-like handshakes, forward secrecy), 22 threshold
  cryptography (Shamir sharing, threshold signatures), 23 secure MPC (garbled circuits, GMW).
- **Katz & Lindell** (3rd ed.): perfect secrecy; private-key encryption and pseudorandomness;
  MACs and hash functions; practical constructions (stream/block ciphers); theoretical
  foundations (one-way functions ⇒ everything private-key); number theory; public-key
  encryption and signatures; advanced topics (ZK, MPC, post-quantum).
- **Rosulek, The Joy of Cryptography** (free): one-time pad, provable security via libraries
  and hybrids, secret sharing, PRGs/PRFs/PRPs, security against chosen plaintext, block
  cipher modes, chosen ciphertext, MACs, hashes, authenticated encryption, RSA, Diffie–
  Hellman, public-key encryption, signatures.
- **Goldreich, Foundations of Cryptography** I (basic tools: one-way functions, pseudorandomness,
  zero knowledge), II (basic applications: encryption, signatures, general MPC).
- **Aumasson, Serious Cryptography**: encryption, randomness, security notions, block ciphers,
  stream ciphers, hashes, keyed hashing, authenticated encryption, hard problems, RSA, DH,
  elliptic curves, TLS, quantum and post-quantum — the applied engineer's guide with failure
  stories. **Wong, Real-World Cryptography**: the same ground plus end-to-end encryption,
  hardware, cryptocurrencies, ZKPs. **Cryptopals** (Matasano): 8 sets — basics, block crypto
  (ECB/CBC attacks, padding oracles), stream/randomness (CTR, MT19937), hashes/MACs (length
  extension), Diffie–Hellman and RSA attacks, Bleichenbacher, abstract algebra.
- Courses: CS255 (Boneh: the Coursera Crypto I/II sequence), 6.875 (foundations), CS276
  (Berkeley theory), CMSC456 (Katz).

## Key ideas → pages
[[cryptography-basics]], [[symmetric-encryption-and-authenticated-encryption]],
[[hash-functions-cryptographic]], [[public-key-cryptography]], [[cryptographic-protocols-and-zero-knowledge]].

## What they add
Boneh & Shoup for definitions and proofs of everything deployed; Katz & Lindell/Rosulek for
learning the proof style; Aumasson/Wong/Cryptopals for what breaks; Goldreich for why the
definitions are the right ones.

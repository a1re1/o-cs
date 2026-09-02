---
title: Cryptography basics — goals, Kerckhoffs's principle, the primitive map (symmetric, hash, MAC, public-key, signatures), security definitions and reductions, the random-oracle model, and how real systems compose primitives
type: concept
section: "5.3"
level: 400
tags: [cryptography, confidentiality, integrity, authenticity, non-repudiation, kerckhoffs-principle, threat-model, adversary, symmetric-key, public-key, hash-function, mac, digital-signature, key-exchange, provable-security, security-game, indistinguishability, semantic-security, ind-cpa, ind-cca, reduction, hybrid-argument, one-way-functions, prg, prf, prp, random-oracle-model, standard-model, perfect-secrecy, one-time-pad, computational-security, key-management, crypto-agility, dont-roll-your-own, misuse-resistance, side-channels, constant-time]
sources: [boneh-shoup-and-crypto-texts, cryptography-seminal-papers]
summary: Cryptography provides confidentiality, integrity, authenticity and non-repudiation against an adversary who knows everything but the key (Kerckhoffs), and modern cryptography is a science because each primitive comes with a precise definition as a game between challenger and adversary (a scheme is secure if no efficient adversary wins non-negligibly — indistinguishability/semantic security for encryption, unforgeability for MACs and signatures, collision resistance for hashes) and a reduction proving that breaking the scheme would solve an assumed-hard problem (factoring, discrete log, LWE, or the existence of one-way functions, from which PRGs, PRFs and all of symmetric cryptography follow); the primitive map is small — symmetric encryption, hashes, MACs, authenticated encryption, key exchange, public-key encryption/KEMs, signatures — and almost all real systems are compositions (hybrid encryption, TLS, Signal) where the failures come from misuse (nonce reuse, unauthenticated encryption, textbook RSA, side channels, bad randomness) rather than broken primitives, hence the rules: use vetted libraries and misuse-resistant APIs, never design your own, and get key management right.
---
# Cryptography basics

**In one sentence.** The enemy knows the system; security must rest on the key alone, be
defined as a game the adversary cannot win, and be proved by reduction to a problem we
believe hard — then engineered so that no one has to think about it.

## Goals and the adversary (Boneh & Shoup ch. 1; Katz & Lindell ch. 1)
**Confidentiality** (eavesdroppers learn nothing about the message), **integrity** (tampering
is detected), **authenticity** (you know who sent it), **non-repudiation** (a signer cannot
deny), plus availability, anonymity, deniability as needed. **Kerckhoffs's principle** (1883):
the algorithm is public, only the key is secret — because algorithms leak, and public
scrutiny is the only validation that works ("don't roll your own"). A **threat model** says
what the adversary can see and do: passive eavesdropper, chosen-plaintext (can encrypt),
chosen-ciphertext (can decrypt others), active man-in-the-middle, compromised endpoints,
side channels. The history: classical ciphers broken by frequency analysis; Enigma by
Rejewski/Turing via structure and cribs; Shannon's 1949 theory; Diffie–Hellman 1976 ("the
brink of a revolution … changing this ancient art into a science").

## Definitions: what "secure" means
- **Perfect secrecy** (Shannon): ciphertext is independent of plaintext — the **one-time
  pad** achieves it, and needs a key as long as the message, used once (two-time pad breaks
  by XOR); so practical secrecy must be *computational*.
- **Security games**: challenger vs probabilistic polynomial-time adversary; **advantage** =
  |Pr[win] − ½|; secure if negligible in the security parameter. **Semantic security /
  IND-CPA** (Goldwasser–Micali 1984): adversary picks m₀, m₁, gets the encryption of one,
  can't tell which better than guessing, even with an encryption oracle — implies encryption
  must be *randomized*. **IND-CCA**: also a decryption oracle (except the challenge) — needed
  against active attackers (padding oracles); AEAD gives it. **EUF-CMA** for MACs/signatures:
  can't forge a new valid tag after seeing many. **Collision resistance**, **preimage
  resistance** for hashes.
- **Reductions**: "if A breaks the scheme with advantage ε, then B solves problem X with
  advantage ε/poly" — security is *relative* to assumptions: one-way functions (minimal for
  all private-key crypto — Impagliazzo's Minicrypt), factoring/RSA, discrete log/CDH/DDH in
  groups and curves, LWE/lattices ([[complexity-theory-advanced]]). The **hybrid argument**
  swaps components one at a time; the **random-oracle model** (Bellare–Rogaway 1993) idealizes
  hashes as random functions to prove practical schemes (OAEP, Fiat–Shamir) — a heuristic,
  with known counterexamples, versus standard-model proofs. Concrete security tracks the
  actual bit-security (birthday bounds, GCM's 2³² message limit).

## The primitive map
| Primitive | Gives | Built from | Page |
|---|---|---|---|
| PRG → stream cipher; PRF/PRP → block cipher, modes | confidentiality (IND-CPA) | one-way functions (theory); AES, ChaCha20 (practice) | [[symmetric-encryption-and-authenticated-encryption]] |
| MAC | integrity/authenticity with a shared key | PRFs, universal hashing (Poly1305, GMAC), HMAC | same |
| **AEAD** | IND-CCA confidentiality + integrity | encrypt-then-MAC; AES-GCM, ChaCha20-Poly1305 | same |
| Hash function | fingerprints, commitments, Merkle trees, KDFs, passwords | SHA-2, SHA-3, BLAKE3; Argon2/scrypt for passwords | [[hash-functions-cryptographic]] |
| Key exchange / KEM | shared key over a public channel | DH, ECDH (X25519), ML-KEM (Kyber) | [[public-key-cryptography]] |
| Public-key encryption | encrypt to a public key; in practice **hybrid**: KEM + AEAD | RSA-OAEP, ElGamal/ECIES, Kyber | same |
| Digital signature | authenticity + non-repudiation | RSA-PSS, ECDSA, Ed25519, ML-DSA (Dilithium), hash-based (SPHINCS+) | same |
| Protocols | authenticated key exchange, ZK, MPC, FHE, secret sharing | compositions | [[cryptographic-protocols-and-zero-knowledge]] |
Theory ladder (Goldreich): OWF ⇒ PRG (HILL) ⇒ PRF (GGM) ⇒ PRP (Luby–Rackoff) ⇒ CPA
encryption, MACs, signatures (Lamport/Merkle, Rompel) — all of Minicrypt from one assumption;
public-key needs structured assumptions (Cryptomania) ([[pseudorandomness-and-derandomization]]).

## Engineering rules (Aumasson; Wong; Cryptopals)
1. Use a high-level library with **misuse-resistant** APIs (libsodium/NaCl `secretbox`/`box`,
   Tink, Go `crypto`, age, Noise) — not raw primitives.
2. Authenticate everything: unauthenticated encryption (CBC alone) is broken in practice
   (padding oracles, bit flipping); sign-then-encrypt vs encrypt-then-sign pitfalls.
3. **Nonces**: unique per key, never reuse (GCM catastrophic; use XChaCha20 with random
   nonces or AES-GCM-SIV); **randomness** from the OS CSPRNG only ([[pseudorandomness-and-derandomization]]).
4. Key management is the hard part: generation, storage (HSM, KMS, secure enclave), rotation,
   separation by purpose (derive with HKDF), revocation; **crypto agility** for algorithm
   migration (post-quantum).
5. **Side channels**: constant-time code (no secret-dependent branches or memory access),
   timing/cache/power attacks (Spectre-class, [[caches-and-memory-hierarchy]]), fault
   injection; compression + encryption leaks (CRIME/BREACH); error messages leak (Bleichenbacher).
6. Passwords: slow salted hashes (Argon2id), PAKEs (OPAQUE) — never encrypt passwords.
7. Don't invent protocols; when you must, model them (Tamarin/ProVerif — [[program-verification]]).
Failures are almost always composition or implementation, not AES.

## Pitfalls
- "Encryption" without integrity; ECB mode (the penguin); textbook RSA; MD5/SHA-1 for
  collision-resistant uses; `rand()` for keys.
- Comparing MACs with early-exit string comparison (timing); logging secrets.
- Assuming a proof in the random-oracle model with a non-random hash is airtight — but also
  refusing to use ROM-proven standards.
- Mistaking hashing for encryption (hashes are public and deterministic) or encoding (base64)
  for either.

## Related
- [[symmetric-encryption-and-authenticated-encryption]], [[hash-functions-cryptographic]],
  [[public-key-cryptography]], [[cryptographic-protocols-and-zero-knowledge]],
  [[security-principles]], [[dns-http-and-the-web-stack]], [[pseudorandomness-and-derandomization]],
  [[complexity-theory-advanced]], [[entropy-and-information]].

## Sources
Boneh & Shoup ch. 1–2; Katz & Lindell ch. 1–3; Rosulek ch. 1–5; Diffie & Hellman 1976 (abstract, §I read); Goldwasser & Micali 1984; Bellare & Rogaway 1993; Aumasson ch. 1–3; Cryptopals sets 1–2; Anderson, Security Engineering ch. 5.

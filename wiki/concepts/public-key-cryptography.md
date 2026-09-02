---
title: Public-key cryptography — Diffie–Hellman, RSA, ElGamal, elliptic curves, digital signatures, hybrid encryption and KEMs, the number-theoretic attacks, and post-quantum lattices (LWE, Kyber, Dilithium)
type: concept
section: "5.3"
level: 400
tags: [public-key-cryptography, asymmetric, diffie-hellman, discrete-logarithm, cdh, ddh, rsa, factoring, trapdoor-permutation, oaep, pss, elgamal, elliptic-curves, ecdh, x25519, curve25519, ecdsa, eddsa, ed25519, schnorr, digital-signatures, hybrid-encryption, kem, key-encapsulation, pki, certificates, forward-secrecy, index-calculus, pollard-rho, number-field-sieve, bleichenbacher, small-exponent, nonce-reuse-ecdsa, invalid-curve, post-quantum, lattices, lwe, learning-with-errors, kyber, ml-kem, dilithium, ml-dsa, sphincs, shor, harvest-now-decrypt-later, pairings, bls-signatures]
sources: [boneh-shoup-and-crypto-texts, cryptography-seminal-papers]
summary: Public-key cryptography (Diffie–Hellman 1976) lets parties who share no secret agree on one (g^{ab} from g^a and g^b — hard if discrete logs are), encrypt to a published key, and sign so that anyone can verify: RSA from the factoring trapdoor (e·d ≡ 1 mod φ(N); secure only with OAEP/PSS padding), ElGamal and modern elliptic-curve schemes (X25519 key exchange, ECDSA/Ed25519 signatures with 256-bit keys matching 3072-bit RSA), in practice always as hybrid encryption — a KEM produces a symmetric key and an AEAD encrypts the data — inside a PKI that binds keys to names; the attacks are mostly on misuse (textbook RSA, Bleichenbacher's padding oracle, small exponents, ECDSA nonce reuse that leaked Sony's PS3 key, invalid-curve points, weak randomness) and on parameters (index calculus and the number field sieve set RSA/DH sizes; Pollard rho bounds curves), and since Shor's algorithm breaks all of them on a large quantum computer, the migration is to lattice schemes built on learning with errors (ML-KEM/Kyber, ML-DSA/Dilithium) and hash-based signatures (SLH-DSA/SPHINCS+), deployed today in hybrid mode against harvest-now-decrypt-later.
---
# Public-key cryptography

**In one sentence.** Some mathematical problems are easy forward and hard backward unless
you hold a secret — exponentiate, multiply primes, add noise to linear equations — and
that asymmetry lets strangers establish trust over a public wire.

## Key exchange: Diffie–Hellman (1976; Boneh & Shoup ch. 10)
Public group G = ⟨g⟩ of prime order q. Alice sends g^a, Bob g^b; both compute g^{ab}. Security
rests on the **discrete-log** problem and its relatives: **CDH** (compute g^{ab}) and **DDH**
(distinguish g^{ab} from random — needed for using the result as a key; fails in groups with
pairings or small subgroups). Groups: Z_p* (safe primes, 2048–3072 bits; Logjam showed 512-bit
export DH broken and 1024-bit precomputable by nation-states), **elliptic curves** (points on
y² = x³ + ax + b over F_p; group law by chord-and-tangent; 256-bit curves give 128-bit
security because only generic Pollard-rho attacks (√q) apply — no index calculus);
**Curve25519/X25519** (Bernstein: Montgomery ladder, constant-time, no invalid-curve issues,
rigid parameters vs NIST P-256's unexplained seeds). Unauthenticated DH falls to
man-in-the-middle — hence **authenticated key exchange** with signatures or long-term keys
(TLS, Signal's X3DH — [[cryptographic-protocols-and-zero-knowledge]]); ephemeral keys give
**forward secrecy**.

## Encryption (ch. 11–12)
- **RSA** (1978): N = pq, e·d ≡ 1 (mod φ(N)), c = mᵉ, m = cᵈ; a **trapdoor permutation** —
  inverting without d is believed as hard as factoring (not proven). Textbook RSA is
  deterministic (no IND-CPA), malleable (c·rᵉ), and leaks for small messages — use **RSA-OAEP**
  (IND-CCA in the ROM); PKCS#1 v1.5 padding suffers **Bleichenbacher's** million-message
  padding-oracle attack (1998; ROBOT 2017 still found it). Keys 2048–4096 bits; e = 65537.
- **ElGamal** / hashed ElGamal / ECIES: c = (g^r, m · h^r) — IND-CPA under DDH, randomized by
  design; CCA versions (Cramer–Shoup, or KEM/DEM with a hash).
- **Hybrid encryption / KEMs**: public-key operations are ~1000× slower than AES and size-
  limited, so encapsulate: KEM.Encaps(pk) → (key, ct); then AEAD(key, data). HPKE (RFC 9180)
  standardizes it; **Fujisaki–Okamoto** transforms turn CPA KEMs into CCA ones (used by Kyber).

## Signatures (ch. 13–15)
Sign with sk, verify with pk; EUF-CMA. **RSA-FDH/PSS** (hash then apply the trapdoor; PSS
provable); **Schnorr** (sigma protocol + Fiat–Shamir: R = gᵏ, s = k + H(R, m)·x — elegant,
provable, linear ⇒ multi-signatures MuSig2); **ECDSA** (Schnorr's patent-avoiding cousin —
requires a *fresh, secret, uniform nonce k per signature*; reuse or bias leaks the key:
Sony PS3 2010, Bitcoin wallet thefts, Minerva); **EdDSA/Ed25519** (deterministic nonces from
the hash of the key and message; fast, constant-time, the default today); BLS (pairing-
based; aggregatable — Ethereum consensus); **hash-based** (Lamport one-time ⇒ Merkle ⇒
XMSS/SPHINCS+) — [[hash-functions-cryptographic]]. **PKI**: certificates bind names to keys
(X.509, CAs, chains, revocation, certificate transparency — [[dns-http-and-the-web-stack]]);
web of trust (PGP), TOFU (SSH), key transparency.

## Attacks on the mathematics (ch. 16)
Factoring: trial division → Pollard rho/p−1 → quadratic sieve → **number field sieve**
(subexponential L[1/3]; RSA-250 (829 bits) factored 2020) ⇒ 2048-bit minimum; discrete log
in Z_p*: **index calculus**/NFS (same complexity — Logjam precomputation); on curves: only
generic Pollard rho (O(√q)) — so 256-bit curves suffice; small-subgroup and **invalid-curve**
attacks (validate points), twist security; weak/shared primes (factoring RSA keys with common
factors across the internet, 2012); low-entropy key generation (Debian OpenSSL 2008, ROCA
2017); side channels on modular exponentiation (constant-time Montgomery ladders, blinding).
Number theory background: [[number-theory-algorithms]] (modular exponentiation, extended
Euclid, CRT, primality testing).

## Post-quantum (ch. 17; Regev 2005; NIST 2024)
**Shor's algorithm** solves factoring and discrete log (any abelian group, curves included)
in polynomial time on a fault-tolerant quantum computer ([[quantum-computing]]); Grover only
halves symmetric security (use AES-256). **Harvest-now-decrypt-later** makes key exchange
urgent. **Learning with errors**: given A and b = As + e (mod q) with small noise e, find s —
Regev's worst-case-to-average-case reduction from approximate lattice problems (GapSVP)
grounds it; Module-LWE/Ring-LWE for efficiency. NIST standards (FIPS 203–205, 2024):
**ML-KEM (Kyber)** key encapsulation (~1 KB keys/ciphertexts, fast), **ML-DSA (Dilithium)**
and **SLH-DSA (SPHINCS+)** signatures; FN-DSA (Falcon). Deployed hybrid X25519 + ML-KEM in
TLS (Chrome/Cloudflare 2024), Signal's PQXDH, SSH. Lessons: SIKE (isogenies) was broken
classically in 2022 after reaching the final round — diversity and hybrids matter.

## Pitfalls
- Textbook RSA; PKCS#1 v1.5 encryption; e = 3 with small messages; sharing an RSA key
  between signing and encryption.
- ECDSA with repeated or biased nonces; not validating curve points; custom curves.
- Unauthenticated DH; static DH without forward secrecy; 1024-bit anything.
- Rolling your own PKI or ignoring revocation; trusting a key without a binding to identity.
- Deploying post-quantum alone (not hybrid) too early, or classical alone too late.

## Related
- [[cryptography-basics]], [[cryptographic-protocols-and-zero-knowledge]],
  [[hash-functions-cryptographic]], [[symmetric-encryption-and-authenticated-encryption]],
  [[number-theory-algorithms]], [[quantum-computing]], [[dns-http-and-the-web-stack]],
  [[complexity-theory-advanced]].

## Sources
Diffie & Hellman 1976; RSA 1978; Boneh & Shoup ch. 10–17; Katz & Lindell ch. 9–13; Bleichenbacher 1998; Adrian et al. "Imperfect Forward Secrecy" (Logjam) 2015; Regev 2005; NIST FIPS 203–205; Bernstein "Curve25519" 2006; Cryptopals sets 5–6.

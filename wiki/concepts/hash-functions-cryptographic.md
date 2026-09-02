---
title: Cryptographic hash functions — collision and preimage resistance, Merkle–Damgård and length extension, SHA-2/SHA-3/BLAKE3, HMAC and HKDF, password hashing, commitments and Merkle trees, and the random-oracle idealization
type: concept
section: "5.3"
level: 400
tags: [cryptographic-hash, collision-resistance, preimage-resistance, second-preimage, birthday-attack, birthday-bound, merkle-damgard, length-extension, sponge, keccak, sha-1, sha-2, sha-256, sha-3, blake2, blake3, md5, hmac, hkdf, key-derivation, password-hashing, salt, argon2, scrypt, bcrypt, pbkdf2, commitments, merkle-tree, hash-chains, content-addressing, random-oracle-model, fiat-shamir, hash-based-signatures, integrity, checksums, crc-vs-hash]
sources: [boneh-shoup-and-crypto-texts, cryptography-seminal-papers]
summary: A cryptographic hash maps arbitrary input to a fixed digest such that finding collisions (two inputs, one digest) is infeasible — birthday attacks cap security at half the output length, so 256-bit digests give 128-bit collision resistance — along with preimage and second-preimage resistance; Merkle–Damgård designs (MD5, SHA-1, SHA-2) iterate a compression function and suffer length extension (H(m‖x) computable from H(m) without m), which is why HMAC exists and why SHA-3's sponge and BLAKE2/3's tree designs are extension-free; MD5 and SHA-1 have practical collisions (Flame, SHAttered) and are unsafe wherever collisions matter, though HMAC-SHA1 survives; hashes underpin HMAC and HKDF (extract-then-expand key derivation), Merkle trees and content addressing (Git, IPFS, certificate transparency, blockchains), commitments and Fiat–Shamir, hash-based signatures, and — slowed deliberately and salted — password storage (Argon2id, scrypt, bcrypt), with the random-oracle model as the idealization under which many practical schemes are proved.
---
# Cryptographic hash functions

**In one sentence.** A short, public, deterministic fingerprint that nobody can forge a
twin for — the primitive that turns "the same bytes" into a checkable claim everywhere from
Git to TLS to passwords.

## Definitions (Boneh & Shoup ch. 8)
H: {0,1}* → {0,1}ⁿ. **Collision resistance**: infeasible to find m ≠ m' with H(m) = H(m')
(formally for keyed families, since a fixed function has a hard-coded collision).
**Preimage resistance** (one-wayness): given y, find m with H(m) = y. **Second-preimage
resistance**: given m, find m' ≠ m colliding. Generic attacks: brute force 2ⁿ for preimages,
**birthday attack** ~2^{n/2} for collisions (√ of the space — [[probability-and-statistics-for-cs]])
— so SHA-256 gives 128-bit collision security, 256-bit preimage; 128-bit hashes (MD5) are
collision-broken by design. Not to be confused with non-cryptographic hashes (CRC,
MurmurHash, xxHash — fast, for [[hash-tables]] and error detection, forgeable) or with
[[raid-and-erasure-coding]]'s integrity checksums (which use CRC or cryptographic hashes as
suits the threat).

## Constructions
- **Merkle–Damgård** (MD5, SHA-1, SHA-2): pad with length, iterate a compression function
  h(chainᵢ₋₁, blockᵢ); collision resistance of h ⇒ of H (Merkle–Damgård theorem). Flaw:
  **length extension** — from H(m) and |m| anyone computes H(m ‖ pad ‖ x), so H(k ‖ m) is a
  broken MAC (Flickr API attack) — use HMAC. **SHA-256/512**: 64/80 rounds of ARX + message
  schedule; hardware acceleration common. **SHA-1** (160-bit): theoretical breaks 2005, real
  collision 2017 (SHAttered, 2⁶³ work), chosen-prefix 2020 — dead for signatures/certificates;
  **MD5**: collisions in seconds; chosen-prefix collision forged a CA certificate (2008) and
  Windows Update signatures (Flame 2012).
- **Sponge** (SHA-3/Keccak 2015): absorb blocks into a 1600-bit state with a permutation,
  squeeze output; no length extension; variable output (SHAKE); the same permutation gives
  authenticated encryption and PRFs (KMAC). **BLAKE2** (ARX, faster than MD5 in software) and
  **BLAKE3** (tree hashing — parallel, streaming, XOF; ~10× SHA-256 in software) — the choice for
  content addressing and dedup ([[distributed-file-and-object-storage]]).
- Compression from block ciphers (Davies–Meyer: h(c, m) = E_m(c) ⊕ c).

## Uses
- **HMAC** (RFC 2104): PRF/MAC from any hash, immune to length extension; proven from
  compression-function PRF-ness — [[symmetric-encryption-and-authenticated-encryption]].
- **Key derivation**: **HKDF** (extract a uniform key from input keying material with a salt,
  then expand with labels/info) for TLS 1.3, Signal; domain separation via labels; PBKDF2 is
  the legacy password-based KDF.
- **Password hashing**: salted, slow and memory-hard so offline guessing costs — **Argon2id**
  (PHC winner), **scrypt**, **bcrypt**; never fast hashes; peppers in HSMs; rainbow tables are
  what salts defeat ([[security-principles]]).
- **Commitments**: publish H(m ‖ r), open later — hiding and binding (in the ROM); Fiat–Shamir
  turns interactive sigma protocols into signatures/NIZKs by hashing the transcript
  ([[cryptographic-protocols-and-zero-knowledge]]).
- **Merkle trees** (1979): leaves hashed, internal nodes hash of children; membership proof of
  O(log n) hashes; consistency proofs for append-only logs — Git and content-addressed
  storage ([[git-data-model]]), certificate transparency, Bitcoin blocks and SPV,
  Dynamo/Cassandra anti-entropy ([[replication-and-partitioning]]), IPFS, BitTorrent,
  verifiable data structures; **hash chains** for logs and blockchains
  ([[byzantine-fault-tolerance-and-blockchains]]).
- **Hash-based signatures** (Lamport one-time, Merkle trees, XMSS, **SPHINCS+**/SLH-DSA) — post-
  quantum with only hash assumptions ([[public-key-cryptography]]).
- Integrity of downloads (with an authenticated channel for the digest), dedup, fingerprints,
  proof-of-work ([[byzantine-fault-tolerance-and-blockchains]]), the embedding cache in this
  wiki's search engine (blake3).

## The random-oracle model (Bellare & Rogaway 1993)
Analyse a scheme as if H were a truly random function all parties query; yields clean proofs
for RSA-OAEP, FDH signatures, Fiat–Shamir, HKDF-style constructions. Uninstantiable
counterexamples exist (Canetti–Goldreich–Halevi), but no deployed ROM-proven scheme has
failed *because* of the ROM; treat it as strong heuristic evidence, and prefer standard-model
proofs when they're cheap ([[cryptography-basics]]).

## Pitfalls
- MD5/SHA-1 where collisions matter (signatures, certificates, dedup with untrusted input).
- H(key ‖ message) as a MAC; unsalted or fast password hashes; hashing to "encrypt".
- Truncating digests to 64 bits and calling it collision-resistant.
- Hashing without domain separation (same hash for two purposes — cross-protocol attacks).
- Trusting a checksum published on the same untrusted channel as the file.

## Related
- [[cryptography-basics]], [[symmetric-encryption-and-authenticated-encryption]],
  [[public-key-cryptography]], [[cryptographic-protocols-and-zero-knowledge]], [[git-data-model]],
  [[hash-tables]], [[security-principles]], [[byzantine-fault-tolerance-and-blockchains]].

## Sources
Boneh & Shoup ch. 8; Katz & Lindell ch. 6; Merkle 1979; Bellare, Canetti & Krawczyk 1996; RFC 2104, 5869; Stevens et al. "The first collision for full SHA-1" 2017; Aumasson ch. 6–7; Cryptopals set 4.

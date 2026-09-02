---
title: Symmetric encryption and authenticated encryption — stream ciphers and PRGs, block ciphers as PRPs (AES), modes of operation, chosen-plaintext security, MACs (HMAC, CMAC, Poly1305/GMAC), and AEAD (GCM, ChaCha20-Poly1305) with nonce discipline
type: concept
section: "5.3"
level: 400
tags: [symmetric-encryption, stream-cipher, prg, chacha20, salsa20, rc4, block-cipher, prp, prf, aes, des, feistel, substitution-permutation-network, luby-rackoff, modes-of-operation, ecb, cbc, ctr, xts, nonce, iv, ind-cpa, ind-cca, padding-oracle, bit-flipping, mac, hmac, cbc-mac, cmac, pmac, universal-hashing, carter-wegman, poly1305, gmac, authenticated-encryption, aead, encrypt-then-mac, mac-then-encrypt, aes-gcm, chacha20-poly1305, aes-gcm-siv, nonce-misuse-resistance, key-wrap, disk-encryption, birthday-bound]
sources: [boneh-shoup-and-crypto-texts, cryptography-seminal-papers]
summary: With a shared key, confidentiality comes from a stream cipher (a PRG expanding key+nonce into a keystream XORed with the message — ChaCha20; never reuse a keystream) or a block cipher used in a mode — a block cipher like AES is a pseudorandom permutation, ECB leaks patterns, CBC and CTR are IND-CPA with unpredictable IVs / unique nonces, and CTR turns the block cipher into a stream cipher — but encryption alone is malleable, so integrity needs a MAC (PRF-based HMAC or CMAC, or the faster Carter–Wegman universal-hash MACs Poly1305 and GMAC), and the correct composition is authenticated encryption with associated data: encrypt-then-MAC, packaged as AES-GCM or ChaCha20-Poly1305, which gives IND-CCA security and defeats padding-oracle and bit-flipping attacks, provided nonces are never repeated under a key (GCM leaks the authentication key on repeat; AES-GCM-SIV and XChaCha20 mitigate) and message counts stay below birthday bounds.
---
# Symmetric encryption and authenticated encryption

**In one sentence.** XOR the message with something that looks random and never repeats,
then tag the result so nobody can change it — and get both from one well-tested AEAD call.

## Stream ciphers (Boneh & Shoup ch. 3)
Idealize the one-time pad: a **PRG** G(key, nonce) → keystream; c = m ⊕ keystream. Security =
PRG indistinguishability; **keystream reuse is fatal** (c₁ ⊕ c₂ = m₁ ⊕ m₂; the WEP/Venona
failure) — hence the nonce. Designs: RC4 (broken biases; retired), Salsa20/**ChaCha20**
(ARX — add-rotate-XOR, 20 rounds, 256-bit key, 96-bit nonce, constant-time in software),
AES-CTR as a stream cipher. Malleability: flipping a ciphertext bit flips the plaintext bit —
no integrity.

## Block ciphers (ch. 4)
A keyed permutation E_k: {0,1}ⁿ → {0,1}ⁿ that should be a **PRP** (indistinguishable from a random
permutation; PRF/PRP switching lemma up to the birthday bound q²/2ⁿ). **AES** (Rijndael 2001):
128-bit blocks, 128/192/256-bit keys, 10–14 rounds of a substitution–permutation network
(SubBytes S-box, ShiftRows, MixColumns, AddRoundKey); hardware AES-NI makes it ~1 cycle/byte;
software table lookups leak via cache timing (hence bitsliced or ChaCha). **DES** (1977):
Feistel network, 56-bit key — brute-forced in 1998; 3DES retired. **Luby–Rackoff**: a 3/4-
round Feistel network with PRF round functions is a PRP — theory meets DES. Cryptanalysis
notions: differential and linear cryptanalysis (Biham–Shamir, Matsui — AES designed against
them), related-key, meet-in-the-middle (why 2DES isn't 112-bit).

## Modes of operation (ch. 5)
| Mode | How | Properties |
|---|---|---|
| **ECB** | encrypt each block independently | leaks equal blocks (the penguin); never for data |
| **CBC** | cᵢ = E(mᵢ ⊕ cᵢ₋₁), random unpredictable IV | IND-CPA; sequential encryption; needs padding (PKCS#7) → **padding-oracle** attacks (Vaudenay; POODLE, Lucky13) when unauthenticated; predictable IV breaks it (BEAST) |
| **CTR** | keystream = E(nonce‖counter) | IND-CPA with unique nonces; parallel, seekable, no padding; malleable |
| **XTS** | tweakable, sector-based | disk encryption (no integrity — by design; deterministic per sector) |
| CFB/OFB | legacy stream modes | |
Nonce-based encryption (Rogaway): the caller supplies a unique nonce; a random 96-bit nonce
collides after ~2⁴⁸ messages (birthday) — counters are safer, random needs 192-bit
(XChaCha20). **Deterministic**/**format-preserving** encryption for database fields trades
IND-CPA for searchability (SIV mode, FF1).

## Message authentication codes (ch. 6–7)
MAC(k, m) → tag; **EUF-CMA**: no forgeries after chosen-message queries. Constructions: any
PRF is a MAC for fixed-length messages; **CBC-MAC** (secure only for fixed length; **CMAC**
fixes with key-derived masks), PMAC (parallel), **HMAC** = H((k ⊕ opad) ‖ H((k ⊕ ipad) ‖ m))
(Bellare–Canetti–Krawczyk; safe against length extension — [[hash-functions-cryptographic]]);
**Carter–Wegman** universal-hash MACs: tag = UH_r(m) + F_k(nonce) with an ε-almost-universal
hash — **Poly1305** (polynomial evaluation mod 2¹³⁰ − 5) and **GMAC/GHASH** (polynomial over
GF(2¹²⁸)) — fast, but the nonce must be unique or the hash key r leaks. Verify tags in
constant time.

## Authenticated encryption (ch. 9)
Goal: IND-CCA confidentiality + ciphertext integrity in one primitive, with **associated
data** (headers) authenticated but not encrypted — **AEAD**. Composition results (Bellare–
Namprempre): **encrypt-then-MAC** is always secure (MAC the ciphertext and AD); MAC-then-
encrypt (old TLS) and encrypt-and-MAC (SSH) are not generically secure. Standards: **AES-GCM**
(CTR + GHASH; hardware-fast; 96-bit nonce; nonce reuse reveals the GHASH key ⇒ universal
forgery; ~2³² records per key in TLS), **ChaCha20-Poly1305** (RFC 8439; constant-time in
software; mobile/TLS/SSH/WireGuard), **AES-GCM-SIV** and **XChaCha20-Poly1305** (nonce-
misuse resistant / large random nonces), OCB (patents expired), AES-CCM (constrained
devices), Ascon (NIST lightweight 2023). Key wrapping (AES-KW) for keys; **key commitment**
issues (a ciphertext decrypting validly under two keys — partitioning-oracle attacks; fix by
committing to the key). Chunked AEAD/streams (STREAM, libsodium secretstream) for large
files — a truncation of a stream must be detectable.

## Pitfalls
- Nonce reuse (GCM, ChaCha, CTR) — the single most common catastrophic bug; random 96-bit
  nonces at scale.
- CBC without a MAC; MAC-then-encrypt; comparing tags with `memcmp`.
- ECB for anything; CBC-MAC on variable-length messages; using the same key for encryption
  and MAC without domain separation.
- Encrypting compressible secrets alongside attacker-controlled data (CRIME).
- Forgetting that AEAD does not hide length or protect against replay/reordering (protocols
  add sequence numbers — [[cryptographic-protocols-and-zero-knowledge]]).

## Related
- [[cryptography-basics]], [[hash-functions-cryptographic]], [[public-key-cryptography]],
  [[cryptographic-protocols-and-zero-knowledge]], [[pseudorandomness-and-derandomization]],
  [[dns-http-and-the-web-stack]] (TLS record layer), [[security-principles]].

## Sources
Boneh & Shoup ch. 3–9; Katz & Lindell ch. 3–5; Rogaway "Nonce-based symmetric encryption" 2004; Bellare & Namprempre 2000; RFC 8439; Cryptopals sets 2–3; Aumasson ch. 4–8.

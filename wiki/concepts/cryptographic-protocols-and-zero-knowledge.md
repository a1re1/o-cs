---
title: Cryptographic protocols — authenticated key exchange (TLS 1.3, Signal), sigma protocols and zero-knowledge proofs, zk-SNARKs, secret sharing and threshold cryptography, secure multi-party computation (garbled circuits, GMW), homomorphic encryption, and how protocols fail
type: concept
section: "5.3"
level: 500
tags: [cryptographic-protocols, authenticated-key-exchange, tls-1-3, handshake, forward-secrecy, post-compromise-security, signal, x3dh, double-ratchet, noise-protocol, wireguard, sigma-protocols, schnorr-identification, fiat-shamir, zero-knowledge, simulation, nizk, zk-snarks, groth16, plonk, starks, arithmetization, r1cs, secret-sharing, shamir, threshold-signatures, multi-party-computation, mpc, garbled-circuits, oblivious-transfer, gmw, homomorphic-encryption, fhe, bootstrapping, ckks, commitments, pake, opaque, password-authentication, replay-attacks, downgrade-attacks, protocol-verification, tamarin, proverif]
sources: [boneh-shoup-and-crypto-texts, cryptography-seminal-papers]
summary: Protocols compose primitives into goals no primitive gives alone — authenticated key exchange (TLS 1.3's signed ephemeral DH in one round trip; Signal's X3DH for asynchronous first contact plus the Double Ratchet for forward secrecy and post-compromise security; Noise/WireGuard patterns), identification and zero knowledge (Schnorr's sigma protocol — commit, challenge, respond — proven by simulation; Fiat–Shamir hashes the challenge to make it non-interactive; zk-SNARKs like Groth16/PLONK and STARKs compress any computation's correctness into a short proof by arithmetizing it into polynomial constraints), secret sharing (Shamir polynomials) and threshold signing, secure multi-party computation (Yao's garbled circuits with oblivious transfer for two parties; GMW/BGW secret-shared arithmetic for many) and fully homomorphic encryption (Gentry's bootstrapping; BGV/BFV/CKKS/TFHE) for computing on encrypted data, and password-authenticated key exchange (OPAQUE) — while the failure modes are protocol-level (replay, reflection, downgrade, cross-protocol and key-compromise attacks), which is why serious protocols are now machine-checked in Tamarin or ProVerif.
---
# Cryptographic protocols and zero knowledge

**In one sentence.** The primitives are solved problems; the protocols that stitch them
together — who proves what to whom, in what order, with which freshness — are where the
subtle failures and the astonishing capabilities both live.

## Authenticated key exchange (Boneh & Shoup ch. 21; RFC 8446)
Goal: two parties end with a shared key, each sure of the other's identity, secret against
active adversaries, with **forward secrecy** (past sessions safe after long-term key
compromise). **TLS 1.3**: ClientHello (key shares, supported groups/ciphers) → ServerHello
(key share) → derive handshake keys (HKDF — [[hash-functions-cryptographic]]) → encrypted
certificate + CertificateVerify (signature over the transcript) + Finished (MAC over the
transcript) → application data after 1 RTT; **0-RTT** resumption with PSKs (replayable — only
idempotent requests); transcript hashing binds every message, killing the downgrade and
renegotiation attacks of TLS 1.2 (FREAK, Logjam, POODLE, Triple Handshake); formally verified
during design ([[dns-http-and-the-web-stack]]). **Signal**: **X3DH** — identity key, signed
prekey, one-time prekeys published to a server so a first message can be sent while the peer
is offline, three or four DHs mixed into the initial secret; **Double Ratchet** — a DH ratchet
(new ephemeral keys with each reply → **post-compromise security**) plus symmetric KDF chains
(per-message keys, forward secrecy, out-of-order delivery); safety numbers for identity
verification; PQXDH adds ML-KEM. **Noise** protocol framework (patterns like `IK`, `XX`)
underlies WireGuard, Lightning, WhatsApp; SSH; Kerberos (symmetric, tickets);
**PAKEs** (OPAQUE, SRP): authenticate by password without the server learning it and without
offline dictionary attacks ([[security-principles]]).

## Sigma protocols and zero knowledge (ch. 19–20; GMR 1985)
**Schnorr identification**: prover knows x with h = gˣ; sends commitment R = gᵏ; verifier
sends random challenge c; prover responds s = k + c·x; verifier checks gˢ = R·hᶜ. Properties:
**completeness**, **special soundness** (two transcripts with the same R and different c
yield x — so a cheating prover "knows" x: proof of knowledge), **honest-verifier zero
knowledge** (a simulator picks s, c first and computes R — the transcript distribution is
identical without x). **Zero knowledge** in general (Goldwasser–Micali–Rackoff): the
verifier's view is simulatable, so nothing beyond the statement's truth leaks; every NP
statement has a ZK proof given commitments (3-coloring, Goldreich–Micali–Wigderson);
theory in [[interactive-proofs-and-pcp]]. **Fiat–Shamir**: replace the verifier's challenge by
H(R, m) → non-interactive proofs and **Schnorr signatures** (secure in the ROM). Sigma-
protocol algebra: AND/OR compositions (ring signatures), range proofs (Bulletproofs),
anonymous credentials.

## SNARKs and verifiable computation
Prove "I know w such that C(x, w) = 1" with a proof of a few hundred bytes verified in
milliseconds regardless of C's size. Pipeline: circuit → **arithmetization** (R1CS/QAP,
PLONKish constraint systems, AIR) → polynomial identities → polynomial commitment (KZG with
pairings and a trusted setup — **Groth16** (2016, 3 group elements), **PLONK** (universal
setup); FRI/Merkle-based — **STARKs**, transparent and post-quantum, larger proofs) →
Fiat–Shamir. Descendants of PCPs and the sum-check protocol; deployed in Zcash (private
transactions), Ethereum rollups (validity proofs), and verifiable ML/cloud computation.
Costs: prover time and memory (10⁶–10⁹ constraints), trusted setups (ceremonies), circuit
bugs (soundness holes — under-constrained circuits are the main real-world failure).

## Secret sharing and threshold cryptography (ch. 22; Shamir 1979)
**Shamir**: secret s = f(0) for a random degree-(t−1) polynomial over a field; share i is
f(i); any t shares interpolate (Lagrange), t−1 reveal nothing (information-theoretic —
[[polynomial-identity-testing]]'s cousin). Verifiable secret sharing (Feldman/Pedersen
commitments), proactive resharing; **threshold signatures** (FROST for Schnorr, threshold
ECDSA) and distributed key generation — custody, validators, HSM clusters; the same math
gives Reed–Solomon codes ([[raid-and-erasure-coding]]).

## Secure multi-party computation (ch. 23; Yao 1986)
Parties compute f(x₁, …, xₙ) learning only the output. **Yao's garbled circuits** (two-party):
the garbler encrypts each gate's truth table under wire labels; the evaluator obtains its
input labels via **oblivious transfer** (get one of two messages without the sender learning
which) and evaluates gate by gate; semi-honest security, with cut-and-choose or
authenticated garbling for malicious; free-XOR and half-gates make it practical (AES in
milliseconds). **GMW/BGW/SPDZ**: secret-share every wire, add locally, multiply with
interaction (Beaver triples from preprocessing); honest-majority information-theoretic (BGW)
or dishonest-majority with MACs (SPDZ). Applications: private set intersection (contact
discovery), auctions, joint statistics, threshold wallets, privacy-preserving ML.

## Homomorphic encryption (Gentry 2009)
Encryptions you can compute on: partially (RSA multiplies, Paillier adds), **fully**
(arbitrary circuits) via lattice/LWE schemes whose noise grows per operation and is reset by
**bootstrapping** (homomorphically evaluating decryption). Families: BGV/BFV (exact
integers), **CKKS** (approximate reals — ML inference), **TFHE** (fast Boolean bootstrapping).
Overheads 10³–10⁶× but shrinking (GPUs, ASICs); used for private inference, encrypted
databases, and with MPC in "confidential computing" alongside hardware enclaves
([[os-kernels-and-virtualization]]).

## How protocols fail (and how to check them)
**Replay** (no freshness — add nonces/sequence numbers), **reflection**, **man-in-the-middle**
on unauthenticated DH, **downgrade** (negotiation not authenticated), **key-compromise
impersonation**, **cross-protocol** and **type-confusion** attacks (Needham–Schroeder's
17-year-old flaw found by Lowe with model checking), unknown-key-share, message-order and
identity-binding mistakes, 0-RTT replays, padding/timing oracles at the protocol level. The
discipline: explicit goals, symbolic verification (**Tamarin**, **ProVerif** — [[model-checking]])
and computational proofs (CryptoVerif, EasyCrypt), standardized patterns (Noise), and
implementation in verified or memory-safe code ([[program-verification]]).

## Pitfalls
- Designing a handshake ad hoc; skipping transcript binding; reusing keys across protocols.
- Fiat–Shamir without hashing the *whole* statement (weak Fiat–Shamir — real SNARK breaks).
- Trusting a SNARK circuit without auditing constraints; ignoring trusted-setup assumptions.
- MPC/FHE "solving privacy" while inputs/outputs leak everything (output privacy is separate).

## Related
- [[cryptography-basics]], [[public-key-cryptography]], [[hash-functions-cryptographic]],
  [[symmetric-encryption-and-authenticated-encryption]], [[interactive-proofs-and-pcp]],
  [[dns-http-and-the-web-stack]], [[security-principles]], [[model-checking]],
  [[byzantine-fault-tolerance-and-blockchains]], [[raid-and-erasure-coding]].

## Sources
Boneh & Shoup ch. 18–23; Goldwasser, Micali & Rackoff 1985; Yao 1986; Shamir 1979; Gentry 2009; Groth 2016; Perrin & Marlinspike (Signal specs); RFC 8446; Lowe 1996; Thaler, *Proofs, Arguments, and Zero-Knowledge* (2022).

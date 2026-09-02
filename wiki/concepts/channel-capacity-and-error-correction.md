---
title: Channel capacity and error-correcting codes
type: concept
section: "1.7"
level: 400
tags: [channel-capacity, noisy-channel-coding-theorem, error-correcting-codes, hamming-code, hamming-distance, parity, ldpc, reed-solomon, crc, checksums, gaussian-channel, coding-gain, erasure-codes]
sources: [shannon-1948, mackay-itila, berkeley-cs70]
summary: Shannon's noisy-channel theorem: any rate below capacity C = max I(X;Y) is achievable with vanishing error using long random-like codes, and nothing above it; practical codes (Hamming, CRC, Reed–Solomon, LDPC, fountain codes) trade redundancy for detected/corrected errors, and the same ideas power RAID, storage, and network protocols.
---
# Channel capacity and error correction

**In one sentence.** Redundancy defeats noise: below capacity you can make the error probability as
small as you like at a fixed rate; the art is designing codes that are decodable in practice.

## Capacity
- Discrete memoryless channel: C = max_{p(x)} I(X;Y) bits per use. Binary symmetric channel with flip
  probability f: C = 1 − H₂(f) (BSC(0.1): 0.53 bits). Binary erasure channel: C = 1 − f.
- Band-limited Gaussian channel: C = W log₂(1 + S/N) bits/s — the reason SNR and bandwidth trade
  off, and the target every modem/Wi-Fi/5G standard chases.
- **Theorem** (Shannon 1948): rates R < C achievable with error → 0 as block length → ∞; R > C
  impossible. Proof by *random coding*: pick 2^{NR} random codewords; typical-set decoding fails with
  vanishing probability. Non-constructive — it took until the 1990s (turbo, LDPC) to approach C in practice.

## Codes
| Code | Idea | Detect/correct | Where |
|---|---|---|---|
| Repetition (R₃) | send each bit 3× | corrects 1 of 3; rate 1/3 | intuition only |
| Parity bit | XOR of block | detects 1 error | memory, protocols |
| **Hamming(7,4)** | 3 parity bits cover overlapping subsets | corrects 1 error; rate 4/7 | ECC RAM (SECDED variant) |
| **CRC** | remainder mod a generator polynomial over GF(2) | detects bursts ≤ degree; not correcting | Ethernet, zip, storage |
| **Reed–Solomon** | message = polynomial over GF(2⁸) evaluated at n points; any k suffice | corrects (n−k)/2 symbol errors or n−k erasures | CDs, QR codes, RAID-6, storage erasure coding |
| **LDPC / turbo** | sparse random parity checks; iterative belief-propagation decoding | within 0.1 dB of capacity | Wi-Fi, 5G, satellite, SSDs |
| Polar codes | channel polarization | provably capacity-achieving | 5G control channels |
| Fountain (LT/Raptor) | rateless: any ≈k of unlimited packets rebuild | erasures | multicast, storage |

Minimum **Hamming distance** d between codewords: detects d−1 errors, corrects ⌊(d−1)/2⌋. Linear codes
[n, k, d]: generator and parity-check matrices; syndrome decoding. Singleton bound d ≤ n − k + 1
(Reed–Solomon meets it, "MDS").

## Systems view
- Erasure coding in distributed storage (Reed–Solomon (n, k) replaces 3× replication with 1.5× overhead
  at equal durability — [[raid-and-erasure-coding]]).
- Checksums vs cryptographic hashes: CRC detects random corruption, not adversaries
  ([[hash-functions-cryptographic]]).
- Retransmission (ARQ) vs forward error correction: TCP uses ARQ; QUIC/video/satellite use FEC where
  latency matters ([[tcp]]).

## Pitfalls
- Capacity is a limit on *rate*, not on latency; near-capacity codes need long blocks.
- A code corrects errors only up to its distance; beyond that it decodes to the wrong codeword silently.
- CRC polynomials must be chosen for the block length (Koopman's tables).

## Related
- [[entropy-and-information]], [[source-coding-and-compression]], [[number-theory-basics]] (finite
  fields for Reed–Solomon, via CS70), [[raid-and-erasure-coding]].

## Sources
Shannon 1948 Parts II and IV; MacKay ch. 1, 9–11, 13, 47–50; CS70 error-correcting codes notes.

---
title: Number-theoretic algorithms — sieves, gcd, modular exponentiation and inverses, CRT, primality, combinatorics mod p
type: concept
section: "3.4"
level: 300
tags: [number-theory-algorithms, sieve-of-eratosthenes, euclid, extended-euclid, modular-exponentiation, modular-inverse, fermat-little-theorem, euler-totient, chinese-remainder-theorem, miller-rabin, pollard-rho, binomial-coefficients-mod-p, lucas, discrete-log, factorization, diophantine]
sources: [competitive-programmers-handbook, clrs, dpv-algorithms]
summary: Working mod a large prime (10⁹+7, 998244353) makes counting problems tractable — fast exponentiation gives modular powers and inverses (Fermat: a^{p−2}), extended Euclid gives inverses for any coprime modulus and solves linear Diophantine equations, the Chinese remainder theorem combines congruences, sieves list primes and smallest prime factors in O(n log log n), Miller–Rabin tests primality probabilistically (deterministic witnesses up to 2⁶⁴) and Pollard's rho factors, and precomputed factorials give binomials mod p in O(1) — the toolkit behind RSA and contest combinatorics.
---
# Number-theoretic algorithms

**In one sentence.** Everything reduces to fast modular exponentiation, Euclid's algorithm, and a
sieve — plus knowing which theorem (Fermat, Euler, CRT, Lucas) unlocks the problem.

## Core routines
- **Binary exponentiation** `a^e mod m` in O(log e): square-and-multiply; also for matrices
  (linear recurrences in O(k³ log n)) and permutations.
- **gcd** (Euclid, O(log min)) and **extended Euclid** returning x, y with ax + by = gcd(a, b) →
  modular inverse when gcd(a, m) = 1; solutions of ax + by = c (linear Diophantine).
- **Modular inverse**: a^{−1} ≡ a^{p−2} (mod p) by Fermat for prime p; extended Euclid in general;
  inverses of 1..n in O(n) via inv[i] = −⌊p/i⌋·inv[p mod i].
- **Sieve of Eratosthenes** O(n log log n); linear sieve O(n) also yields smallest prime factor
  (fast factorization of many numbers), φ(n), μ(n), divisor counts. Segmented sieve for ranges.
- **Euler's totient** φ(n) = n Π(1 − 1/p); Euler's theorem a^{φ(m)} ≡ 1 for gcd(a, m) = 1 — exponent
  reduction; primitive roots and discrete logs (baby-step giant-step O(√m)).
- **Chinese remainder theorem**: x ≡ aᵢ (mod mᵢ) with coprime moduli has a unique solution mod
  Π mᵢ; construct with inverses; Garner's algorithm for many moduli; used in RSA-CRT and
  reconstructing big integers from residues ([[modular-arithmetic]]).
- **Primality**: trial division to √n; **Miller–Rabin** — write n−1 = 2ˢd, check a^d, a^{2d}, …;
  composite fails with probability ≤ ¼ per random base; bases {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
  31, 37} are deterministic below 3.3·10²⁴ ([[randomized-algorithms]]). **Pollard's rho** factors
  64-bit numbers in ~n^{1/4} expected using Floyd cycle detection on x² + c; combine for full
  factorization.
- **Combinatorics mod p**: precompute fact[i], invfact[i] → C(n, k) in O(1); Lucas' theorem for
  C(n, k) mod small p; Catalan, Stirling, inclusion–exclusion, Burnside counting
  ([[counting-rules]]).
- Big integers: schoolbook/Karatsuba/FFT multiplication ([[fft]]); Python ints for contests that
  allow it.

## Why it matters beyond contests
RSA (modular exponentiation, φ(n), CRT speedup), Diffie–Hellman (discrete log hardness), hashing
(polynomial rolling hashes mod primes — [[string-algorithms]]), random number generators (LCGs,
Mersenne), checksums (CRC as polynomial arithmetic mod 2), and the NTT ([[cryptography-basics]],
[[number-theory-basics]]).

## Pitfalls
- Overflow in `a * b % m` for 64-bit m (use 128-bit or `__int128`/mulmod by doubling).
- Negative remainders in C++/Java (`((a % m) + m) % m`).
- Fermat inverse when the modulus is not prime (use extended Euclid); dividing before reducing.
- Sieve memory for n ~ 10⁹ (segmented sieve, bitset).

## Related
- [[number-theory-basics]], [[modular-arithmetic]], [[counting-rules]], [[randomized-algorithms]],
  [[fft]], [[string-algorithms]], [[cryptography-basics]].

## Sources
CPH ch. 21–23; CLRS ch. 31; DPV ch. 1.

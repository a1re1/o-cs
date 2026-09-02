---
title: Number theory basics (divisibility, gcd, Euclid, Bézout, primes, RSA)
type: concept
section: "1.1"
level: 200
tags: [number-theory, gcd, euclidean-algorithm, bezout, primes, fundamental-theorem-of-arithmetic, rsa, fermat-little-theorem, euler-theorem, chinese-remainder-theorem]
sources: [mcs-lehman-leighton-meyer, berkeley-cs70]
summary: Divisibility, the Euclidean algorithm and its extended form (Bézout coefficients), unique prime factorization, Fermat/Euler theorems, the Chinese remainder theorem, and how these assemble into RSA — the number theory a programmer actually uses.
---
# Number theory basics

## Divisibility and gcd
- a | b means b = ka. gcd(a, b) is the largest common divisor; gcd(a, 0) = a.
- **Euclidean algorithm**: gcd(a, b) = gcd(b, a mod b). Invariant: the gcd of the pair never changes;
  the second argument strictly decreases ⇒ terminates ([[invariant-principle]]). Runs in O(log min(a,b))
  divisions (the worst case is consecutive Fibonacci numbers).
- **Bézout / extended Euclid**: gcd(a, b) = sa + tb for integers s, t; the algorithm that computes them:

```
def egcd(a, b):            # returns (g, s, t) with g = gcd(a,b) = s*a + t*b
    if b == 0: return (a, 1, 0)
    g, s, t = egcd(b, a % b)
    return (g, t, s - (a // b) * t)
```
- Consequence: a has a multiplicative inverse mod n iff gcd(a, n) = 1 ([[modular-arithmetic]]).
- Linear combination view: the set {sa + tb} is exactly the multiples of gcd(a,b) (used for Die Hard jug puzzles).

## Primes
- **Fundamental Theorem of Arithmetic**: every integer > 1 factors uniquely into primes. Proof uses
  the lemma "if p | ab then p | a or p | b", which follows from Bézout.
- Infinitely many primes (Euclid); prime number theorem π(n) ~ n / ln n, so a random n-bit number is prime
  with probability ≈ 1/(0.69 n) — this is why generating RSA keys by trial-and-test works.
- Primality testing: Miller–Rabin (randomized, fast) is what libraries use; AKS is polynomial but slow.
  Factoring, by contrast, has no known polynomial algorithm — the asymmetry RSA relies on.

## Fermat, Euler, CRT
- **Fermat's little theorem**: p prime, p ∤ a ⇒ a^{p−1} ≡ 1 (mod p).
- **Euler's theorem**: gcd(a, n) = 1 ⇒ a^{φ(n)} ≡ 1 (mod n), φ(n) = #{k < n : gcd(k,n)=1};
  φ(pq) = (p−1)(q−1) for distinct primes.
- **Chinese remainder theorem**: if m, n coprime, x mod mn is determined by (x mod m, x mod n) and every
  pair occurs — a bijection Z_{mn} ↔ Z_m × Z_n. Used to speed RSA decryption and in hashing/scheduling.

## RSA (MCS 8.11)
Keys: choose large primes p, q; n = pq; pick e coprime to (p−1)(q−1); d = e^{−1} mod (p−1)(q−1).
Public (e, n), private d. Encrypt m ↦ m^e mod n; decrypt c ↦ c^d mod n. Correctness: ed = 1 + k(p−1)(q−1),
so m^{ed} ≡ m by Euler/Fermat (handle gcd(m,n) ≠ 1 via CRT). Security rests on the hardness of factoring n
(and, more precisely, the RSA problem); textbook RSA is *not* secure without padding (§5.3).
Fast exponentiation (repeated squaring) makes m^e mod n cost O(log e) multiplications.

## Pitfalls
- gcd(0, 0) is conventionally 0; watch division by zero in egcd.
- `%` in C/Java/Rust returns negative remainders for negative operands; Python's is always non-negative.
- Do not confuse Fermat's *little* theorem with Fermat's last theorem; Carmichael numbers fool the
  Fermat test, hence Miller–Rabin.

## Related
- [[modular-arithmetic]] — the ring Z_n and inverses.
- [[induction]] — well ordering gives existence of prime factorizations.
- [[invariant-principle]] — Euclid's correctness.

## Sources
MCS ch. 8; CS70 Notes 5–7 (modular arithmetic, Euclid/FLT/CRT, RSA).

---
title: Modular arithmetic
type: concept
section: "1.1"
level: 200
tags: [modular-arithmetic, congruence, multiplicative-inverse, fast-exponentiation, hashing, wraparound, z-n]
sources: [mcs-lehman-leighton-meyer, berkeley-cs70]
summary: Congruence mod n as an equivalence relation, the ring Z_n, when inverses exist and how to compute them with extended Euclid, fast modular exponentiation, and where the same arithmetic shows up in hashing, checksums, ring buffers and integer overflow.
---
# Modular arithmetic

**In one sentence.** a ≡ b (mod n) iff n | (a − b); congruence respects + and ×, so we can compute
in Z_n = {0, …, n−1} and reduce whenever convenient.

## Rules
- Reduce anytime: (a + b) mod n = ((a mod n) + (b mod n)) mod n; same for ×. Not for ÷ or exponent
  reduction: a^k mod n ≠ a^{k mod n} mod n in general (exponents reduce mod φ(n) when gcd(a,n)=1, by
  Euler — [[number-theory-basics]]).
- **Cancellation**: ax ≡ ay (mod n) ⇒ x ≡ y only if gcd(a, n) = 1. In Z_p (p prime) every nonzero
  element is invertible, so Z_p is a field.
- **Inverse**: a^{−1} mod n exists iff gcd(a, n) = 1; compute via extended Euclid (s in sa + tn = 1), or,
  for prime p, a^{p−2} mod p by Fermat.
- **Fast exponentiation** (square-and-multiply), O(log k) multiplications, each reduced mod n:

```
def powmod(a, k, n):
    r = 1; a %= n
    while k:
        if k & 1: r = r * a % n
        a = a * a % n; k >>= 1
    return r
```
- Chinese remainder theorem lets you split work across coprime moduli.

## Where it appears in code
- Hash tables and hash functions: index = h(key) mod m; polynomial rolling hashes (Rabin–Karp) are
  arithmetic mod a large prime.
- Ring buffers, cyclic counters, clock arithmetic: (i + 1) mod capacity.
- Machine integers *are* Z_{2^64}: overflow is wraparound; signed overflow is undefined behaviour in C,
  wraps in Rust release / panics in debug.
- Checksums (ISBN mod 11, Luhn mod 10), error-correcting codes over Z_p (Reed–Solomon, CS70), RSA and
  Diffie–Hellman (§5.3).

## Pitfalls
- Negative operands: in C/Java/Rust `-7 % 3 == -1`; normalise with `((a % n) + n) % n`. Python and Ruby
  return `2`.
- Multiplying two 64-bit residues overflows before the mod; use 128-bit intermediates or Montgomery/
  Barrett reduction.
- Dividing by a non-invertible residue silently gives nonsense; check gcd.

## Related
- [[number-theory-basics]] — Euclid, Bézout, Fermat/Euler, RSA.
- [[sets-relations-functions]] — congruence is an equivalence relation with n classes.
- [[hash-tables]] — the main consumer in data structures.

## Sources
MCS 8.6–8.10; CS70 Notes 5–6.

---
title: Recurrences and generating functions
type: concept
section: "1.1"
level: 200
tags: [recurrences, linear-recurrences, characteristic-equation, generating-functions, closed-form, guess-and-verify, fibonacci, master-theorem]
sources: [mcs-lehman-leighton-meyer, levin-dmoi]
summary: How to solve recurrences that arise from recursive definitions and algorithms — guess-and-verify by induction, characteristic roots for linear recurrences, generating functions as formal power series — and where the Master theorem takes over for divide-and-conquer.
---
# Recurrences and generating functions

**In one sentence.** A recurrence defines a sequence by earlier terms; solving it means finding a
closed form (or an asymptotic bound) and *proving* it, usually by [[induction]].

## Methods
1. **Unroll and guess, then verify by induction.** T(n) = T(n−1) + n → T(n) = n(n+1)/2. Always finish
   with the induction; the guess is not a proof.
2. **Linear recurrences with constant coefficients** (Levin §2.4, MCS 15.4):
   a_n = c₁a_{n−1} + … + c_k a_{n−k}. Substitute a_n = r^n to get the characteristic polynomial
   r^k − c₁r^{k−1} − … − c_k = 0; with distinct roots r_i the general solution is Σ A_i r_i^n
   (repeated roots contribute n·r^n, n²·r^n, …); fix constants from base cases.
   Fibonacci: r² = r + 1 ⇒ φ, ψ = (1 ± √5)/2 ⇒ F_n = (φ^n − ψ^n)/√5 = Θ(φ^n).
   Inhomogeneous term f(n): particular solution of the same shape as f (polynomial, exponential)
   plus the homogeneous solution.
3. **Generating functions** (MCS ch. 15): encode ⟨a₀, a₁, …⟩ as G(x) = Σ a_n x^n. Shifting, scaling,
   adding, and multiplying sequences become algebra on G; a linear recurrence becomes a rational
   function, and partial fractions read off the closed form. Also count things: the coefficient of
   x^n in (1 + x + x² + …)^k = 1/(1−x)^k is C(n+k−1, k−1) — stars and bars from [[counting-rules]].
4. **Divide and conquer**: T(n) = aT(n/b) + f(n) — use the Master theorem / recursion-tree method
   ([[master-theorem]], §3.2). T(n) = 2T(n/2) + n ⇒ Θ(n log n).

## Pitfalls
- Floors/ceilings and base cases rarely change the asymptotics but can break an exact closed form.
- Guessing T(n) = O(n) and "proving" T(n) ≤ cn + d by induction: the induction must reproduce the
  *same* form; lower-order slack (+d) must be accounted for or subtracted ("strengthen the hypothesis").
- A recurrence with a non-constant number of terms (T(n) = Σ_{i<n} T(i) + n) needs the "difference
  trick" (subtract consecutive instances) to turn it into a fixed-order one.

## Worked example
Towers of Hanoi: T(n) = 2T(n−1) + 1, T(1) = 1. Unroll: T(n) = 2^n − 1. Verify: 2(2^{n−1} − 1) + 1 = 2^n − 1. ∎
Characteristic approach: homogeneous root 2, particular constant −1.

## Related
- [[asymptotic-notation]] — what the bounds mean.
- [[master-theorem]] — divide-and-conquer recurrences (§3.2).
- [[induction]], [[counting-rules]].

## Sources
MCS ch. 15 (generating functions, solving linear recurrences); Levin §2.4; MCS problems on Hanoi.

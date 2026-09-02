---
title: Asymptotic notation (big-O, Ω, Θ, o, ~)
type: concept
section: "1.1"
level: 200
tags: [asymptotics, big-o, theta, omega, little-o, growth-rates, complexity-analysis, sums, harmonic-numbers, stirling]
sources: [mcs-lehman-leighton-meyer, levin-dmoi]
summary: Precise definitions of O, Ω, Θ, o, ω and ~, the growth-rate hierarchy (log ≪ polynomial ≪ exponential), rules for sums and products, and the traps — abusing "=" in O(·), ignoring constants that matter, and confusing asymptotically faster with actually faster.
---
# Asymptotic notation

**In one sentence.** f = O(g) means f is eventually bounded above by a constant multiple of g; the
notation lets us compare algorithms while ignoring machine-specific constants and small inputs.

## Definitions (f, g: R → R, g ≥ 0)
| Notation | Meaning | Limit form (when the limit exists) |
|---|---|---|
| f ~ g | same growth | lim f/g = 1 |
| f = o(g) | strictly smaller | lim f/g = 0 |
| f = O(g) | at most | ∃c, x₀: ∀x ≥ x₀, \|f(x)\| ≤ c·g(x)  (equivalently lim sup f/g < ∞) |
| f = Ω(g) | at least | g = O(f) |
| f = Θ(g) | same order | f = O(g) and f = Ω(g) |
| f = ω(g) | strictly larger | g = o(f) |

MCS defines O via lim sup so that oscillating ratios (between 3 and 5) still count as O.

## The hierarchy
1 ≪ log log n ≪ log n ≪ log^k n ≪ n^ε (any ε > 0) ≪ n ≪ n log n ≪ n² ≪ n^k ≪ 2^n ≪ n! ≪ n^n.
Key lemmas: log x = o(x^ε) for every ε > 0; x^b = o(a^x) for a > 1. Polynomials are Θ of their
leading term. Bases of logarithms differ by constants, so O(log n) needs no base; but 2^n and 3^n are
*not* Θ of each other, and 2^(2n) = 4^n ≠ O(2^n).

## Rules that make analysis quick
- Sums: Σ_{i=1}^{n} i^k = Θ(n^{k+1}); Σ 1/i = ln n + γ + o(1) (harmonic numbers, H_n = Θ(log n));
  geometric series with ratio < 1 are Θ(first term), with ratio > 1 Θ(last term).
- Approximate sums by integrals (MCS 13.3): ∫₁ⁿ f ≤ Σ ≤ f(1) + ∫₁ⁿ f for increasing f; this gives the
  Θ bounds above and Stirling's n! ~ √(2πn)(n/e)^n, so log n! = Θ(n log n).
- Products: take logs, sum, exponentiate.
- Max rule: O(f + g) = O(max(f, g)).

## Pitfalls & gotchas
- The "=" in f = O(g) is one-directional set membership. O(x) = O(x²) is true; O(x²) = O(x) is false.
  Never cancel O-terms across an equation.
- **Constants matter in practice.** MCS's example: an O(n^2.55) matrix multiply is "almost never used"
  because it only wins on impractically large matrices; likewise many "galactic" algorithms.
- O is an upper bound: "the algorithm is O(n²)" says nothing about it being slow. Say Θ when you mean tight.
- Worst-case vs average-case vs amortized are separate questions from the notation ([[amortized-analysis]]).
- Hidden dependence on other parameters (word size, alphabet, dimension) — state what n is.

## Worked example
T(n) = 3n² + 100n + 10. Then T ~ 3n², T = Θ(n²), T = O(n³), T ≠ O(n). To show T = O(n²): choose c = 113,
x₀ = 1; for n ≥ 1, 3n² + 100n + 10 ≤ 3n² + 100n² + 10n² = 113n².

## Related
- [[recurrences]] — solving for T(n) in recursive algorithms.
- [[counting-rules]] — where the sums come from.
- [[amortized-analysis]] — bounding sequences of operations (§3.1).

## Sources
MCS ch. 13 (sums, approximating sums, asymptotic notation); Levin §2.

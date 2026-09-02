---
title: Integrals, Riemann sums, and bounding sums by integrals
type: concept
section: "1.3"
level: 100
tags: [integrals, riemann-sums, fundamental-theorem-of-calculus, integral-test, harmonic-series, expectation-continuous, numerical-integration, monte-carlo]
sources: [strang-calculus, mcs-lehman-leighton-meyer]
summary: The integral as a limit of sums and the fundamental theorem that makes it computable; the integral bounds on monotone sums (harmonic numbers, log n!, Σ i^k) that algorithm analysis uses constantly; and the basics of numerical/Monte Carlo integration and continuous expectation.
---
# Integrals and sums

**In one sentence.** ∫ₐᵇ f = lim Σ f(xᵢ)Δx, and for monotone f the sum Σ_{i=1}^{n} f(i) is
sandwiched between two integrals — which is how Σ1/i = Θ(log n) and log n! = Θ(n log n) are proved.

## Fundamental theorem
If F′ = f then ∫ₐᵇ f = F(b) − F(a); d/dx ∫ₐˣ f = f(x). Substitution and integration by parts are the
chain and product rules run backwards. Standard: ∫xⁿ = xⁿ⁺¹/(n+1), ∫1/x = ln x, ∫eˣ = eˣ,
∫₀^∞ e^{−x} = 1, ∫_{−∞}^{∞} e^{−x²/2} = √(2π) (normal distribution).

## Sums vs integrals (MCS 13.3)
For f increasing on [1, n]: ∫₁ⁿ f ≤ Σ_{i=1}^{n} f(i) ≤ f(n) + ∫₁ⁿ f; for decreasing f swap the roles.
- Harmonic: ln(n+1) ≤ H_n ≤ 1 + ln n; H_n = ln n + γ + O(1/n). Appears in quicksort's expected
  comparisons (2n ln n), coupon collector (nH_n), and skip-list/treap analyses.
- Σ_{i=1}^{n} i^k = n^{k+1}/(k+1) + O(n^k).
- log n! = Σ log i = n log n − n + O(log n) (Stirling), so comparison sorting needs Ω(n log n).
- Integral test for series convergence: Σ 1/n^p converges iff p > 1.
Also Euler–Maclaurin for higher precision, and the "geometric series dominates" rule: Σ arⁱ is Θ of its
largest term when r ≠ 1 ([[asymptotic-notation]]).

## Continuous probability preview
For a density p, Pr[a ≤ X ≤ b] = ∫ₐᵇ p; E[g(X)] = ∫ g(x)p(x)dx; the CDF is the integral of the density
and the density the derivative of the CDF ([[random-variables-expectation]]).

## Numerical integration
Trapezoid (error O(h²)), Simpson (O(h⁴)), Gaussian quadrature for smooth 1-D integrands; in high
dimensions use **Monte Carlo**: average f at N random points, error O(1/√N) independent of dimension
([[monte-carlo-methods]]).

## Pitfalls
- Off-by-one endpoints when converting a sum to an integral change constants (not asymptotics).
- Improper integrals (∫1/x diverges at both 0 and ∞) — check convergence before using the bound.

## Related
- [[asymptotic-notation]], [[derivatives-and-gradients]], [[recurrences]].

## Sources
Strang Calculus ch. 5, 7, 10; MCS 13.3 (Approximating Sums).

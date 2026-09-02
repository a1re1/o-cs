---
title: Floating-point arithmetic, rounding error, conditioning, and numerical stability
type: concept
section: "1.6"
level: 300
tags: [floating-point, ieee-754, rounding-error, machine-epsilon, catastrophic-cancellation, conditioning, backward-stability, numerical-stability, kahan-summation, nan, denormals, ulp]
sources: [mit-18-335-numerical-methods, boyd-vmls]
summary: IEEE 754 doubles carry ~16 significant digits and every operation rounds (relative error ≤ 2⁻⁵³), so identities fail by tiny amounts, subtracting nearly equal numbers destroys digits (cancellation), and the accuracy of a computation ≈ condition number × algorithm's backward error — with the standard fixes: reformulate to avoid cancellation, sum carefully, use stable (orthogonal) algorithms, never test floats for equality.
---
# Floating point

**In one sentence.** A double is ±(1.f)·2ᵉ with 52 fraction bits: relative spacing 2⁻⁵² ≈ 2.2·10⁻¹⁶
(machine epsilon), so fl(a ⊕ b) = (a + b)(1 + δ) with |δ| ≤ 2⁻⁵³ — small per operation, but errors
compound and cancel.

## IEEE 754 essentials
- Formats: binary32 (24-bit significand, ~7 digits), binary64 (53 bits, ~16 digits), bfloat16/fp16/fp8
  for ML (range vs precision trade-offs; bf16 keeps float32's exponent).
- Special values: ±0, ±∞, NaN (NaN ≠ NaN; propagates; use `isnan`), subnormals (gradual underflow,
  slow on some hardware — flush-to-zero flags).
- Rounding: round-to-nearest-even by default; results are deterministic given the same operation order,
  but **not associative**: (a + b) + c ≠ a + (b + c); compilers may not reorder without `-ffast-math`,
  which also breaks NaN handling. Parallel reductions give run-to-run differences.
- Integers up to 2⁵³ are exact in doubles; 0.1 is not representable (0.1 + 0.2 ≠ 0.3). Use decimal
  types for money; integers for counters.

## Where digits die
- **Catastrophic cancellation**: x − y with x ≈ y keeps the absolute error but the result is tiny, so
  relative error explodes. Examples: variance via E[X²] − E[X]² (use Welford's online algorithm),
  quadratic formula for b² ≫ 4ac (use q = −(b + sign(b)√(b²−4ac))/2, x₂ = c/q), 1 − cos x for small x
  (use 2 sin²(x/2)), log(1 + x) (use `log1p`), eˣ − 1 (`expm1`).
- **Summation**: naive Σ of n terms has error O(nε); pairwise summation O(ε log n); Kahan compensated
  summation O(ε). Python's `math.fsum` is exact-rounded.
- **Overflow/underflow**: e^{1000} = ∞; products of probabilities → 0 ([[log-probabilities]]);
  ‖x‖ via `hypot` scales to avoid overflow.

## Conditioning vs stability (Trefethen & Bau)
- **Condition number** of a *problem*: how much the exact answer changes per unit relative perturbation
  of the input (κ(A) = ‖A‖‖A⁻¹‖ for solving Ax = b — [[svd-and-pca]]). Ill-conditioned problems lose
  log₁₀ κ digits no matter the algorithm.
- **Backward stable** *algorithm*: the computed result is the exact result for a slightly perturbed input
  (perturbation O(ε)). Forward error ≲ κ · backward error. Gaussian elimination with partial pivoting,
  Householder QR, and SVD are backward stable; classical Gram–Schmidt and the normal equations are not
  ([[orthogonality-and-projections]], [[least-squares]]).
- Rule: do not judge a method by a single test case; reason about κ and stability.

## Comparing floats
Never `a == b`. Use |a − b| ≤ atol + rtol·max(|a|, |b|) (numpy `isclose`), choose tolerances from the
problem's κ, and remember that `<` and `==` on NaN are always false (sort keys with NaN break ordering).

## Related
- [[gaussian-elimination-lu]], [[svd-and-pca]], [[gradient-descent]], [[log-probabilities]],
  [[vectors-and-inner-products]].

## Sources
18.335 lectures 1–3 (floating point, conditioning, stability); VMLS 1.5; Goldberg, "What Every Computer Scientist Should Know About Floating-Point Arithmetic" (1991, not yet ingested).

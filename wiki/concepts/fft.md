---
title: The fast Fourier transform and polynomial multiplication
type: concept
section: "3.2"
level: 400
tags: [fft, fast-fourier-transform, dft, polynomial-multiplication, convolution, roots-of-unity, cooley-tukey, butterfly, evaluation-interpolation, ntt, signal-processing, big-integer-multiplication]
sources: [dpv-algorithms, clrs, kleinberg-tardos-skiena]
summary: Multiplying polynomials (= convolution) is O(n²) in coefficient form but O(n) in point-value form, so evaluate both at the 2n-th roots of unity, multiply pointwise, and interpolate back — the FFT does each evaluation/interpolation in O(n log n) by splitting a polynomial into even and odd parts and exploiting ω² being an (n/2)-th root of unity; the inverse is the same algorithm with ω⁻¹ and a 1/n factor; applications span big-integer multiplication, signal processing, image filtering, string matching with wildcards, and the number-theoretic transform for exact integer results.
---
# The fast Fourier transform

**In one sentence.** Change representation: polynomials as *values at roots of unity* multiply
pointwise, and the change of basis costs only n log n because the roots of unity have a
divide-and-conquer structure.

## Setup (DPV 2.6, CLRS ch. 30)
- Polynomial A(x) = Σ aⱼxʲ of degree < n; product C = A·B has coefficients cₖ = Σ aⱼ b_{k−j}
  (**convolution**): O(n²) directly.
- Point-value representation at n distinct points determines a degree-<n polynomial uniquely
  (Vandermonde invertibility — [[matrices-and-linear-maps]]); multiplication is pointwise O(n)
  (need 2n points for the product).
- Choose the points to be the n-th **complex roots of unity** ωⁿ = e^{2πi/n}: ω^k for k = 0..n−1.
  Key facts: (ω_n^k)² = ω_{n/2}^k (halving), and Σ_k ω^{jk} = 0 for j ≢ 0 (cancellation) — this is
  what makes the DFT matrix orthogonal (up to √n) and the inverse just the conjugate.

## The algorithm (Cooley–Tukey, radix 2)
Split A(x) = A_even(x²) + x·A_odd(x²) with A_even, A_odd of degree < n/2. Evaluating A at all n
roots of unity needs A_even and A_odd at the n/2 roots ω_{n/2}^k — two half-size problems:
`A(ω^k) = A_e(ω^{2k}) + ω^k A_o(ω^{2k})`, `A(ω^{k+n/2}) = A_e(ω^{2k}) − ω^k A_o(ω^{2k})` (the
**butterfly**). T(n) = 2T(n/2) + O(n) = O(n log n) ([[divide-and-conquer]]). Iterative version:
bit-reversal permutation then log n passes of butterflies — the standard hardware/library form
(FFTW, cuFFT). **Inverse DFT**: the DFT matrix M_n(ω) has inverse (1/n)·M_n(ω⁻¹): run the same
FFT with ω⁻¹ and scale. Polynomial multiplication: pad to 2n, FFT both, multiply, inverse FFT,
round — O(n log n).

## Applications
- **Big-integer multiplication** (digits as coefficients; Schönhage–Strassen, Harvey–van der
  Hoeven O(n log n)); Python's `int` uses Karatsuba, GMP uses FFT above ~10⁴ digits.
- Signal processing: spectrum analysis, filtering as multiplication in frequency space, fast
  convolution/correlation, audio/image compression (DCT in JPEG/MP3 — [[source-coding-and-compression]]),
  OFDM radio (Wi-Fi, LTE).
- Algorithms: string matching with wildcards, counting sum pairs (subset-sum convolution),
  polynomial interpolation/division, all-pairs distance histograms.
- **NTT**: roots of unity modulo a prime p = c·2ᵏ + 1 (998244353) for exact integer convolution;
  used in lattice cryptography (Kyber) and competitive programming.

## Pitfalls
- Floating-point error with large coefficients (use NTT or split into 15-bit limbs).
- Forgetting to pad to a power of two ≥ 2n (circular convolution wraps around).
- Off-by-one in the inverse scaling (1/n) and the sign of the exponent conventions.

## Related
- [[divide-and-conquer]], [[matrices-and-linear-maps]], [[orthogonality-and-projections]] (the DFT
  is an orthogonal basis change), [[source-coding-and-compression]], [[number-theory-basics]] (NTT).

## Sources
DPV 2.6; CLRS ch. 30; K&T 5.6.

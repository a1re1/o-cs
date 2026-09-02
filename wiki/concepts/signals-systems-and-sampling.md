---
title: Signals, Systems, and Sampling
type: concept
section: "11.3"
level: 400
tags: [fourier-transform, sampling-theorem, nyquist, aliasing, convolution, lti-systems, filters, spectrogram]
sources: [signal-processing-texts-and-papers]
summary: The core DSP toolkit — the Fourier transform and frequency domain, LTI systems and convolution, the Nyquist-Shannon sampling theorem and aliasing, and filtering and spectrograms.
---

# Signals, Systems, and Sampling
**In one sentence.** Any signal can be decomposed into a sum of sinusoids (the Fourier
transform), linear time-invariant systems act on it by convolution, and a continuous
signal can be perfectly reconstructed from samples taken above twice its highest
frequency (Nyquist-Shannon).

## Why it matters
The time/frequency duality is one of the most reused ideas in all of computing: it turns
convolution into multiplication, explains aliasing artifacts in graphics and audio, and
is the basis of every codec, filter, and spectrogram feeding audio ML. Sampling theory
is literally the bridge from the analog world to digital.

## How it works
**The frequency domain.** The **Fourier transform** expresses a signal as a
superposition of sinusoids: `X(f)` gives the amplitude and phase of each frequency. The
same information, two views — time and frequency. For sampled signals the discrete
version is the **DFT**, computed efficiently by the [[fft]] in O(n log n).

**LTI systems and convolution.** A **linear time-invariant** system is fully described
by its **impulse response** `h`; its output is the **convolution** `y = x * h`. The
**convolution theorem** is the key lever: convolution in time = **multiplication in
frequency**, `Y(f) = X(f)·H(f)`. So filtering is just scaling each frequency by the
filter's response — and fast convolution is done via the FFT.

**Sampling (Nyquist-Shannon).** Sampling a continuous signal at rate `fs` replicates its
spectrum every `fs`. If the signal's highest frequency `fmax < fs/2` (the **Nyquist
frequency**), the copies don't overlap and the original is perfectly recoverable. If
`fmax ≥ fs/2`, the copies overlap: high frequencies masquerade as low ones —
**aliasing** — an irreversible corruption. The fix is an **anti-aliasing (low-pass)
filter** before sampling.

**Filters.** Low-pass (keep low frequencies), high-pass, band-pass, notch — designed by
their frequency response. FIR filters are convolutions with a finite kernel; IIR filters
use feedback for sharper response at lower cost but risk instability.

**Spectrograms.** Real signals change over time, so apply the **Short-Time Fourier
Transform** — FFT over sliding windows — to get a time-frequency image (the spectrogram),
the standard input representation for speech and audio ML. This exposes a
time-frequency **resolution trade-off**: a short window localizes time but blurs
frequency, and vice versa (an uncertainty principle).

## Complexity & trade-offs
- FFT-based convolution is O(n log n) vs O(n²) direct — decisive for long signals/kernels.
- STFT window length trades time vs frequency resolution; there is no window that is
  sharp in both.
- IIR filters are cheap and sharp but can be unstable and have nonlinear phase; FIR
  filters are stable with linear phase but need more taps.

## Pitfalls & gotchas
- **Aliasing** — sampling (or downscaling an image) without a low-pass prefilter folds
  high frequencies into false low ones; the moiré and wagon-wheel effects. Irreversible.
- **Spectral leakage** — FFT of a non-integer number of periods smears energy across
  bins; apply a **window** (Hann, Hamming) to reduce it.
- **Assuming periodicity** — the DFT treats the signal as periodic; edge discontinuities
  create artifacts.

## Worked example
A 20 kHz tone sampled at 30 kHz: Nyquist is 15 kHz, so the tone aliases to
`30 − 20 = 10` kHz — you hear a 10 kHz tone that was never there. Sampling at 44.1 kHz
(CD rate, Nyquist 22.05 kHz) with an anti-aliasing filter captures the full audible band
without aliasing.

## Related
- [[fft]] — the fast algorithm behind DFT/convolution/spectrograms.
- [[speech-and-audio-processing]] — spectrograms feed speech ML.
- [[convolutional-neural-networks]] — convolution in the ML setting.
- [[entropy-and-information]] — Shannon founded both sampling and information theory.

## Sources
Distilled from [[signal-processing-texts-and-papers]] (Oppenheim; Downey *Think DSP*;
Nyquist 1928 / Shannon 1949).

---
title: Signal Processing, Audio & Speech — Texts and Papers
type: source
section: "11.3"
level: 400
tags: [signal-processing, fourier, sampling, dft-fft, speech-recognition, audio-ml]
authors: Oppenheim; Downey; J.O. Smith; Jurafsky & Martin
year: 2016
institution: MIT, Stanford CCRMA
url: https://www.dspguide.com/
license: mixed
format: texts+courses+papers
sources: []
summary: The signal-processing and speech canon — Oppenheim's Signals and Systems, Downey's Think DSP, J.O. Smith's CCRMA texts, and the seminal work from Cooley-Tukey's FFT and Nyquist-Shannon sampling to CTC, wav2vec, and Whisper.
---

# Signal Processing, Audio & Speech — Texts and Papers

## What it is
The theory and practice of representing, transforming, and analyzing signals — sound,
images, sensor data — in time and frequency. It underpins audio, communications,
control, imaging, and modern speech ML.

## Key ideas
- **Fourier analysis & sampling** — decomposing signals into frequencies; the sampling
  theorem. See [[signals-systems-and-sampling]].
- **The DFT and FFT** — fast frequency analysis of sampled signals. See [[fft]].
- **Filtering** — shaping a signal's spectrum (low/high/band-pass). See
  [[signals-systems-and-sampling]].
- **Speech & audio ML** — recognition and synthesis with neural models. See
  [[speech-and-audio-processing]].

## Chapter / lecture map
- **Oppenheim & Willsky, *Signals and Systems* / MIT 6.003** — LTI systems, convolution,
  Fourier/Laplace/Z transforms.
- **Downey, *Think DSP* (free)** — DSP by programming, spectra and filtering hands-on.
- **J.O. Smith (CCRMA), *Mathematics of the DFT* / *Spectral Audio Signal Processing*
  (free)** — audio DSP depth.
- **Stanford EE261 (Fourier transform); Coursera Audio Signal Processing for Music.**
- **Jurafsky & Martin, *Speech and Language Processing*** — the speech chapters.

## Notable claims & quotes
- **Nyquist-Shannon**: to reconstruct a signal exactly you must sample at more than
  twice its highest frequency — the bridge between the analog and digital worlds.
- Cooley & Tukey's FFT (1965) reduced the DFT from O(n²) to O(n log n), arguably one of
  the most consequential algorithms ever (see [[fft]]).

## Seminal papers
- **Cooley & Tukey, FFT (1965)** — see [[fft]].
- **Nyquist (1928) / Shannon (1949)** — the sampling theorem.
- **Rabiner, HMM tutorial (1989)** — HMMs for speech; see [[bayesian-networks-and-hmms]].
- **Graves et al., CTC (2006)** — alignment-free sequence labeling for speech.
- **Baevski et al., wav2vec 2.0 (2020)** — self-supervised speech representations.
- **Radford et al., Whisper (2022)** — robust large-scale supervised speech recognition.

## What it adds
The frequency-domain lens that recurs across CS — [[fft]] in algorithms,
convolution in [[convolutional-neural-networks]], sampling in graphics and audio. It
connects to [[transformers-and-attention]] and [[self-supervised-and-contrastive-learning]]
(modern audio ML) and [[entropy-and-information]] (Shannon).

---
title: Speech and Audio Processing
type: concept
section: "11.3"
level: 400
tags: [speech-recognition, ctc, wav2vec, whisper, asr, tts, audio-ml, spectrogram]
sources: [signal-processing-texts-and-papers]
summary: How machines recognize and generate speech — features (spectrograms/MFCCs), the classic HMM pipeline, CTC for alignment-free training, self-supervised wav2vec, and end-to-end models like Whisper.
---

# Speech and Audio Processing
**In one sentence.** Automatic speech recognition (ASR) turns an audio waveform into
text by extracting time-frequency features and mapping them to words — evolving from
HMM pipelines to CTC and attention-based end-to-end neural models.

## Why it matters
Speech is a primary human-computer interface (assistants, dictation, captioning), and
its arc — hand-engineered features + HMMs → deep learning → self-supervision → large
end-to-end models — mirrors the whole ML field. It ties [[signals-systems-and-sampling]]
to [[transformers-and-attention]].

## How it works
**Features.** Convert the waveform to a **spectrogram** via the Short-Time Fourier
Transform (see [[signals-systems-and-sampling]]); classic pipelines further compress it
to **MFCCs** (mel-frequency cepstral coefficients) matching human pitch perception.
Modern models often learn features directly from the waveform.

**The classic pipeline (pre-deep-learning).** An **acoustic model** (Gaussian-mixture
HMMs; see [[bayesian-networks-and-hmms]]) maps features to phonemes, a **pronunciation
lexicon** maps phonemes to words, and an **n-gram language model** scores word
sequences; a decoder searches the combined space. Powerful but complex and requiring
frame-level alignments.

**CTC — Connectionist Temporal Classification (Graves 2006).** The core problem is that
audio frames vastly outnumber output characters and aren't aligned. CTC lets a network
output a per-frame distribution over characters plus a **blank** symbol, and defines the
sequence probability by summing over *all* alignments that collapse (remove blanks and
repeats) to the target — trainable end to end with no frame labels. It made
alignment-free neural ASR practical.

**Self-supervised pretraining — wav2vec 2.0 (2020).** Pretrain on unlabeled audio with a
[[self-supervised-and-contrastive-learning]] objective (predict masked latent speech
units), then fine-tune on a little labeled data. Slashes the transcribed-data
requirement — key for low-resource languages.

**End-to-end attention models — Whisper (2022).** A [[transformers-and-attention]]
encoder-decoder trained on a huge, weakly-supervised, multilingual corpus. It maps
spectrogram → text directly (with language ID, timestamps, translation) and is notably
**robust** to noise and accents because of scale and data diversity.

**Text-to-speech (TTS)** runs the reverse: text → acoustic features (Tacotron) → waveform
via a **neural vocoder** (WaveNet/HiFi-GAN), now near-human quality.

## Complexity & trade-offs
- Classic HMM pipelines are modular and data-efficient but brittle and complex; end-to-end
  neural models are simpler and far more accurate but data- and compute-hungry.
- CTC assumes conditional independence of outputs (weak language modeling), so it is often
  paired with an external LM or replaced by attention decoders that model output
  dependencies.
- Self-supervision (wav2vec) buys accuracy on little labeled data at the cost of a large
  unlabeled pretraining run.

## Pitfalls & gotchas
- **Domain/accent mismatch** — models trained on clean read speech fail on
  spontaneous/noisy/accented speech; diversity in training data (Whisper's approach) is
  the fix.
- **CTC's independence assumption** overproduces without a language model.
- **Feature/sample-rate mismatch** between training and inference silently degrades
  accuracy; match the front-end exactly.
- **Streaming vs offline** — attention over the whole utterance isn't causal; streaming
  ASR needs restricted attention or chunking.

## Worked example
Transcribing "hello": the STFT yields a spectrogram, a CTC-trained network emits per
-frame character posteriors like `h,h, blank,e,l,l,blank,l,o,o`, and the CTC collapse
rule (merge repeats, drop blanks) reduces it to "hello" — summing over all such
frame-alignments during training so no per-frame labels were ever needed.

## Related
- [[signals-systems-and-sampling]] — spectrograms are the input features.
- [[transformers-and-attention]] — Whisper and modern ASR are attention-based.
- [[self-supervised-and-contrastive-learning]] — wav2vec pretraining.
- [[bayesian-networks-and-hmms]] — the classic HMM acoustic models.

## Sources
Distilled from [[signal-processing-texts-and-papers]] (Jurafsky & Martin; Graves CTC 2006;
wav2vec 2.0 2020; Whisper 2022).

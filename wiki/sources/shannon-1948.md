---
title: A Mathematical Theory of Communication (Shannon, 1948)
type: source
section: "1.7"
level: 400
tags: [information-theory, entropy, channel-capacity, source-coding, noisy-channel-coding, classic-papers, shannon]
sources: []
authors: [Claude E. Shannon]
year: 1948
institution: Bell Labs
url: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
license: proprietary-open-access
format: pdf
summary: The founding paper of information theory — defines entropy H = −Σ p log p as the unique measure of information satisfying natural axioms, proves the source coding theorem (compress to H bits/symbol) and the noisy-channel coding theorem (reliable communication up to capacity C), introduces mutual information, Markov sources, and the Gaussian channel capacity formula.
---
# A Mathematical Theory of Communication (Shannon, 1948)

## What it is
Bell System Technical Journal, July and October 1948; ~55 pages. Part I discrete noiseless systems
(capacity of a channel as log of the number of allowed sequences, Markov sources, the entropy of a
source and its axiomatic characterization, English as an n-gram source, coding theorem for a
noiseless channel). Part II discrete channel with noise (equivocation, capacity C = max(H(X) − H(X|Y)),
the fundamental theorem: rates below C achievable with arbitrarily small error; proof by random
coding). Part III continuous information; Part IV continuous channel: C = W log(1 + S/N) for the
band-limited Gaussian channel; Part V rate of a continuous source (rate–distortion in embryo).

## Key ideas → pages
- Entropy, conditional entropy, mutual information, and the chain rules — [[entropy-and-information]].
- Source coding theorem and the n-gram model of English (redundancy ≈ 50%) — [[source-coding-and-compression]].
- Noisy-channel coding theorem, capacity, random coding argument, Gaussian channel —
  [[channel-capacity-and-error-correction]].
- Markov sources and the entropy rate of a chain — [[markov-chains]].

## Notable claims & quotes
- "The fundamental problem of communication is that of reproducing at one point either exactly or
  approximately a message selected at another point."
- Semantic aspects "are irrelevant to the engineering problem" — information is about the set of
  possible messages, not their meaning.

## What it adds
The original definitions; [[mackay-itila]] is the modern textbook treatment, but the paper is short
enough to read in full and its n-gram experiments are the ancestors of language models (§6.4).

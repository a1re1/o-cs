---
title: Information Theory, Inference, and Learning Algorithms (MacKay)
type: source
section: "1.7"
level: 400
tags: [information-theory, entropy, source-coding, channel-coding, error-correcting-codes, hash-codes, bayesian-inference, message-passing, monte-carlo, variational-methods, neural-networks]
sources: []
authors: [David J. C. MacKay]
year: 2003
institution: University of Cambridge
url: https://www.inference.org.uk/itila/
license: proprietary-open-access
format: pdf
summary: MacKay's free 600-page classic (with 16 open Cambridge video lectures) uniting information theory and machine learning — source coding theorem and typical sets, symbol/stream/integer codes, noisy-channel coding theorem, LDPC and turbo codes, hash codes, then inference (clustering, MLE, exact marginalization, Laplace, Monte Carlo, variational), neural networks and Gaussian processes.
---
# Information Theory, Inference, and Learning Algorithms (MacKay, 2003)

## What it is
Level 400. Intro (1–3: repetition/Hamming codes, probability & entropy, inference). **I Data
compression** (4 source coding theorem, 5 symbol codes/Huffman, 6 stream codes/arithmetic coding &
Lempel–Ziv, 7 codes for integers). **II Noisy-channel coding** (8 dependent variables, 9–10 channel
capacity and the noisy-channel coding theorem, 11 error-correcting codes and real channels).
**III Further topics** (12 hash codes, 13 binary codes, 14 very good linear codes exist, 16 message
passing, 17 constrained channels, 18 crosswords and codebreaking, 19 evolution). **IV Probabilities
and inference** (20–22 clustering & MLE, 23 useful distributions, 24–26 exact marginalization
including trellises and graphs, 27 Laplace's method, 28 model comparison and Occam's razor, 29–30 Monte
Carlo and MCMC, 31 Ising models, 32 exact sampling, 33 variational methods, 34 ICA, 35 random inference
topics, 36 decision theory, 37 Bayesian vs frequentist). **V Neural networks** (38–46: single neuron,
capacity, Hopfield nets, Boltzmann machines, supervised nets, Gaussian processes, deconvolution).
**VI Sparse graph codes** (47 LDPC, 48 convolutional & turbo, 49 repeat-accumulate, 50 digital fountain).

## Key ideas → pages
- Entropy as the answer to "how many bits, on average"; the source coding theorem via typical sets:
  N symbols compress to ≈ NH bits, no more, no less — [[entropy-and-information]], [[source-coding-and-compression]].
- Symbol codes (Kraft inequality, Huffman optimal among prefix codes, within 1 bit of H) vs stream
  codes (arithmetic coding gets arbitrarily close to H and separates modelling from coding; LZ is
  universal) — [[source-coding-and-compression]].
- Channel capacity C = max I(X;Y); reliable communication below C at arbitrarily small error, with
  random codes as the proof; practical near-capacity codes (LDPC) decoded by message passing —
  [[channel-capacity-and-error-correction]].
- Inference chapters preview §6.7: message passing = sum-product on factor graphs; Monte Carlo;
  variational free energy; Occam's razor from the Bayesian evidence — [[markov-chains]].

## Notable claims & quotes
- "Information theory and machine learning are two sides of the same coin" — the compression of data
  is the same problem as its modelling.
- On the source coding theorem: "regardless of our specific allowance for error, the number of bits per
  symbol needed to specify x is H bits; no more and no less."

## What it adds
The bridge between §1.7 information theory and §6 learning: minimum description length, evidence
framework, and the fact that a good predictive model *is* a good compressor.

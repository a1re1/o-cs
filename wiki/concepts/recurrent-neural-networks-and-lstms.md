---
title: Recurrent neural networks and LSTMs — sequence modelling with a hidden state, backpropagation through time, vanishing/exploding gradients, LSTM gates and the constant-error carousel, GRUs, bidirectional and stacked RNNs, sequence-to-sequence with encoder–decoder, teacher forcing and exposure bias, and why attention and transformers replaced them (and where state-space models bring recurrence back)
type: concept
section: "6.3"
level: 400
tags: [rnn, recurrent-neural-network, sequence-modeling, hidden-state, unrolling, backpropagation-through-time, bptt, truncated-bptt, vanishing-gradients, exploding-gradients, gradient-clipping, lstm, forget-gate, input-gate, output-gate, cell-state, constant-error-carousel, gru, bidirectional-rnn, stacked-rnn, language-model, character-rnn, seq2seq, encoder-decoder, teacher-forcing, exposure-bias, beam-search, attention, sequence-length, parallelism, state-space-models, mamba, s4, linear-rnn, time-series]
sources: [deep-learning-texts-courses-and-seminal-papers]
summary: An RNN processes a sequence one step at a time with a hidden state hₜ = tanh(W_h hₜ₋₁ + W_x xₜ + b) shared across steps (weight sharing in time, as CNNs share in space), and is trained by unrolling and backpropagation through time; the product of many Jacobians makes gradients vanish (long-range dependencies unlearnable) or explode (fixed by clipping), and the LSTM (Hochreiter & Schmidhuber 1997) fixes vanishing with an additive cell state guarded by learned forget, input and output gates — gradient flows along the cell like a residual connection ("constant error carousel") — with the GRU as the cheaper two-gate variant; bidirectional and multi-layer RNNs, character/word language models (Karpathy's char-rnn), and sequence-to-sequence encoder–decoders (Sutskever 2014) for translation trained with teacher forcing and decoded with beam search were the state of the art until the fixed-size bottleneck was relieved by attention (Bahdanau 2014) and then removed by transformers, whose parallel training over sequence length beat the RNN's inherently sequential computation; recurrence returns in linear/state-space models (S4, Mamba) that offer O(1)-per-token inference and long contexts.
---
# Recurrent neural networks and LSTMs

**In one sentence.** Share one transition function across time steps and you can model
sequences of any length with a fixed number of parameters — at the cost of a
sequential computation whose gradients vanish unless a gated additive state (LSTM) carries
them, which is why attention eventually won.

## Vanilla RNNs and BPTT (Goodfellow ch. 10; CS231n lecture 7; D2L ch. 9)
hₜ = tanh(W_hh hₜ₋₁ + W_xh xₜ + b), yₜ = W_hy hₜ; the same W at every step. Modes: many-to-one
(sentiment), one-to-many (captioning), many-to-many aligned (tagging) or unaligned (seq2seq).
**Unroll** the graph over T steps and backpropagate — **BPTT**: ∂L/∂W sums contributions from
every step; ∂hₜ/∂hₖ = Π_{i=k+1}^{t} W_hhᵀ diag(tanh'(·)) — a product of t − k Jacobians, so
gradients **vanish** (largest singular value of W_hh < 1, tanh' ≤ 1) or **explode** (> 1);
dependencies beyond ~10–20 steps are unlearnable for vanilla RNNs (Bengio et al. 1994).
Fixes: **gradient clipping** by norm (exploding — [[neural-network-training]]); **truncated
BPTT** (carry hₜ forward, backprop only k steps — bounded memory); orthogonal init; and the
gating that solves vanishing. Memory: activations for all T steps (O(T) for the backward
pass). Character-level RNNs (Karpathy's char-rnn 2015) learn Shakespeare, LaTeX, Linux
source — the demonstration that a hidden state can carry syntax and long-range structure.

## LSTM and GRU (Hochreiter & Schmidhuber 1997; Cho et al. 2014)
**LSTM** adds a **cell state** cₜ with gates from σ(W [hₜ₋₁, xₜ] + b): forget fₜ, input iₜ,
output oₜ, and a candidate g̃ₜ = tanh(·): cₜ = fₜ ⊙ cₜ₋₁ + iₜ ⊙ g̃ₜ, hₜ = oₜ ⊙ tanh(cₜ). The cell
update is **additive** — ∂cₜ/∂cₜ₋₁ = diag(fₜ), no repeated W multiplication — so gradients
flow along the cell across hundreds of steps when the forget gate stays near 1 (initialize
its bias to 1–2): the **constant error carousel**, structurally the same idea as ResNet's
skip connection a decade later. 4× the parameters of a vanilla RNN. **GRU**: reset and
update gates, no separate cell — hₜ = (1 − zₜ) ⊙ hₜ₋₁ + zₜ ⊙ h̃ₜ; comparable accuracy, cheaper.
Variants (peepholes, layer-normalized LSTMs) matter less than the gating idea. Neither fixes
exploding gradients (still clip).

## Architectures and applications (D2L ch. 10; Prince ch. 12)
**Stacked** RNNs (2–4 layers; dropout between layers, not across time — or variational
dropout with a shared mask); **bidirectional** RNNs (forward and backward passes concatenated
— for tagging/encoding where the whole sequence is available, not for generation); **language
models** P(xₜ | x<ₜ) with softmax over the vocabulary, trained by cross-entropy — perplexity as
the metric ([[nlp-fundamentals]]); **seq2seq** (Sutskever, Vinyals & Le 2014): an encoder
LSTM compresses the source into its final state, a decoder LSTM generates the target
conditioned on it — machine translation, summarization, speech (with CTC loss for
unaligned outputs), captioning (CNN encoder). **Teacher forcing**: feed the gold previous
token during training — fast, but **exposure bias** at test time when the model conditions on
its own errors (scheduled sampling, sequence-level losses mitigate). Decoding: greedy, **beam
search** (keep k partial hypotheses; length normalization), sampling with temperature/top-k/
nucleus ([[large-language-models]]).

## From attention to transformers (Bahdanau, Cho & Bengio 2014; Vaswani et al. 2017)
The seq2seq bottleneck — a whole sentence in one vector — was relieved by **attention**: at
each decoder step compute alignment scores between the decoder state and every encoder
state, softmax them into weights, and feed the weighted sum (a learned soft alignment; the
weights visualize as translation alignments). Then the observation that attention alone,
with positional encodings, models sequences without recurrence: **transformers** train in
parallel across all positions (one matmul over T × T instead of T sequential steps —
[[gpu-programming-cuda]] utilization), have O(1) path length between any two positions (no
vanishing over distance), and scale ([[transformers-and-attention]]). RNNs remain in
small/edge models, some time-series and control tasks, and as the ancestor of **linear
RNNs / state-space models** (S4 2021, Mamba 2023): recurrences with structured, input-
dependent transitions that can be computed as a parallel scan ([[prefix-sums-and-scans]])
in training and as O(1)-per-token recurrence at inference — the current attempt to have
transformer training with RNN inference ([[efficient-transformers-and-long-context]]).

## Pitfalls
- Vanilla tanh RNN for anything with dependencies beyond a few tokens.
- No gradient clipping; forget-gate bias at zero (LSTM forgets everything early in training).
- Dropout masks resampled at each time step; bidirectional encoders used for generation.
- Evaluating with teacher forcing only (hides exposure bias); greedy decoding for
  translation.
- Padding without masking in batched sequences (loss and attention over pad tokens).

## Related
- [[deep-learning-basics]], [[neural-network-training]], [[transformers-and-attention]],
  [[nlp-fundamentals]], [[large-language-models]], [[bayesian-networks-and-hmms]] (HMMs as
  the probabilistic ancestor), [[prefix-sums-and-scans]], [[gpu-programming-cuda]],
  [[efficient-transformers-and-long-context]], [[convolutional-neural-networks]].

## Sources
Goodfellow ch. 10 (ToC read); CS231n lecture 7 (schedule read); D2L ch. 9–10; Prince ch. 12; Hochreiter & Schmidhuber 1997; Bengio, Simard & Frasconi 1994; Cho et al. 2014; Sutskever et al. 2014; Bahdanau et al. 2014; Karpathy, "The Unreasonable Effectiveness of RNNs" 2015; Gu et al. 2021 (S4); Gu & Dao 2023 (Mamba).

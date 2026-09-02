---
title: NLP fundamentals — tokenization (words, subwords, BPE/WordPiece/SentencePiece), n-gram language models and smoothing, perplexity, text classification (naive Bayes, logistic regression, bag of words/TF-IDF), word embeddings (word2vec skip-gram with negative sampling, GloVe, analogies, bias), sequence labelling (POS, NER — HMMs/CRFs to BiLSTM/transformers), parsing, and evaluation (BLEU, ROUGE, F1, human eval)
type: concept
section: "6.4"
level: 400
tags: [nlp, natural-language-processing, tokenization, word-tokens, subword, bpe, byte-pair-encoding, wordpiece, sentencepiece, unigram-lm, vocabulary, oov, normalization, stemming, lemmatization, regular-expressions, n-gram, language-model, markov-assumption, smoothing, laplace, kneser-ney, backoff, interpolation, perplexity, cross-entropy, bag-of-words, tf-idf, naive-bayes, sentiment, text-classification, word-embeddings, distributional-hypothesis, word2vec, skip-gram, cbow, negative-sampling, glove, co-occurrence, analogies, embedding-bias, contextual-embeddings, elmo, sequence-labeling, pos-tagging, ner, hmm, crf, bilstm-crf, parsing, dependency-parsing, constituency, treebank, coreference, machine-translation, bleu, rouge, evaluation, jurafsky-martin]
sources: [nlp-and-llm-courses-texts-and-seminal-papers]
summary: Text becomes numbers in stages that still shape every LLM: tokenization (whitespace and regex rules gave way to subword vocabularies learned by byte-pair encoding — merge the most frequent adjacent pair repeatedly — or WordPiece/SentencePiece, which bound vocabulary size, handle any string, and explain why models struggle with spelling and arithmetic), language modelling as next-token prediction (n-gram models with the Markov assumption, counted from corpora and smoothed by Laplace, interpolation/backoff and Kneser–Ney; evaluated by perplexity = exp(cross-entropy per token), the same metric LLMs report), text classification by bag-of-words features with naive Bayes or logistic regression (TF-IDF weighting, the sentiment baseline), and distributional word embeddings (word2vec's skip-gram with negative sampling learns vectors whose dot products predict co-occurrence; GloVe factorizes the log co-occurrence matrix; analogies like king − man + woman ≈ queen fall out, as do the corpus's social biases) which contextual embeddings (ELMo, BERT) then made position-dependent; classical structure tasks — POS tagging and NER by HMMs/CRFs then BiLSTM-CRFs, dependency and constituency parsing, coreference — are now mostly solved by fine-tuned or prompted transformers but define the evaluation vocabulary (token-level F1, LAS/UAS), and generation is scored by BLEU/ROUGE/chrF against references, with human evaluation the ground truth.
---
# NLP fundamentals

**In one sentence.** Turn text into tokens, tokens into vectors, and vectors into
predictions — the classical pipeline (BPE, n-grams, perplexity, embeddings, tagging,
parsing, BLEU) is what the LLM era inherited as its tokenizer, its loss, its evaluation,
and its vocabulary of failure modes.

## Tokenization and normalization (SLP3 ch. 2; CS336 assignment 1)
Words are not given: contractions, hyphens, Chinese/Japanese (no spaces), emoji, code.
Classical: regex tokenizers, case folding, **stemming** (Porter) vs **lemmatization**,
stop words; **out-of-vocabulary** words break word-level models. **Subword** tokenization:
**BPE** (Sennrich et al. 2016; from the 1994 compression algorithm) — start from bytes/
characters, repeatedly merge the most frequent adjacent pair into a new symbol until the
vocabulary reaches V (32k–200k); tokenize new text by applying merges in order. Byte-level
BPE (GPT-2) can encode any string; **WordPiece** (BERT) merges by likelihood gain;
**SentencePiece**/**unigram LM** (T5, LLaMA) treats whitespace as a symbol and prunes a
large vocabulary by likelihood. Consequences: frequent words are single tokens, rare ones
are pieces; English ≈ 0.75 words/token, other languages and code cost more (fairness and
context-length effects); models see "strawberry" as ~2–3 pieces, so letter counting and
arithmetic on digit chunks are hard; tokenizer and model are inseparable (vocabulary
size trades embedding parameters against sequence length). Building one from scratch is
CS336's first assignment.

## N-gram language models and perplexity (SLP3 ch. 3; Shannon 1951)
P(w₁…wₙ) = Π P(wᵢ | w₁…wᵢ₋₁); the **Markov assumption** truncates the history to n−1 words:
bigram P(wᵢ | wᵢ₋₁) = count(wᵢ₋₁ wᵢ)/count(wᵢ₋₁). Unseen n-grams get zero probability →
**smoothing**: Laplace add-one (too much mass to unseen), add-k, **interpolation** (λ-weighted
mix of trigram/bigram/unigram, λ tuned on held-out data), **backoff** (Katz), and **Kneser–Ney**
(absolute discounting plus a continuation probability — how many contexts a word appears in
— the best classical smoother; the basis of Google's 2007 web-scale "stupid backoff" 5-gram
models with 10¹² tokens). **Perplexity** PP = exp(−(1/N) Σ log P(wᵢ | context)) = 2^{cross-
entropy in bits} — the effective branching factor; lower is better; compare only with the
same tokenization and test set ([[entropy-and-information]]; Shannon's estimate of ~1 bit/
character for English). n-grams: no generalization across similar words, exponential
sparsity in n — the motivation for neural LMs ([[recurrent-neural-networks-and-lstms]]),
whose loss — cross-entropy per token — and metric are the same ([[large-language-models]]).
Sampling from an LM and the generalization/memorization tension appear already here.

## Text classification (SLP3 ch. 4–5)
**Bag of words**: a document as a count (or binary, or **TF-IDF** — term frequency × inverse
document frequency, from IR: [[tf-idf-and-vector-space-model]]) vector over the vocabulary;
n-gram features; **naive Bayes** (multinomial event model, add-one smoothing, log-space
computation — [[linear-models-logistic-regression-and-glms]]) as the baseline for sentiment
and spam; **logistic regression** with regularization as the stronger linear model; then
CNN/LSTM classifiers, and now fine-tuned BERT or prompted LLMs. Evaluation: accuracy,
precision/recall/**F1** per class, macro vs micro; cross-validation; statistical significance
via bootstrap; error analysis on a confusion matrix ([[machine-learning-basics]]). Lexicons
(sentiment word lists), negation handling, and the fact that "not good" defeats bag of
words motivate sequence models.

## Word embeddings (SLP3 ch. 6; Mikolov et al. 2013; Pennington et al. 2014)
**Distributional hypothesis** (Firth: "you shall know a word by the company it keeps"):
represent a word by its contexts. Sparse: word–word co-occurrence counts, PPMI weighting,
LSA/SVD reduction ([[svd-and-pca]]). Dense **word2vec**: **skip-gram** predicts context words
from the centre word; softmax over V is too expensive → **negative sampling** — a logistic
classifier distinguishing true (w, c) pairs from k random ones (a noise-contrastive
objective), trained by SGD over a corpus; CBOW predicts the centre from the context.
Result: 300-d vectors where cosine similarity = semantic/syntactic similarity and vector
offsets encode relations (**analogies**: vec(king) − vec(man) + vec(woman) ≈ vec(queen);
Levy & Goldberg showed SGNS implicitly factorizes a shifted PMI matrix). **GloVe** fits
wᵢᵀw̃ⱼ + bᵢ + b̃ⱼ = log Xᵢⱼ on the co-occurrence matrix with a weighting function; fastText
adds character n-grams (subword generalization, morphology). Uses: features for downstream
models, similarity/retrieval ([[dense-retrieval-and-embeddings]]), visualization (t-SNE —
caveats). **Bias**: embeddings encode corpus stereotypes (man:programmer :: woman:homemaker;
Bolukbasi 2016; Caliskan 2017 WEAT) — debiasing is partial and the bias propagates
downstream ([[fairness-in-machine-learning]]). Limitation: one vector per type — "bank" is
one point — fixed by **contextual embeddings** (ELMo 2018: biLSTM LM states; BERT: transformer
layers), which is the embedding story becoming the LLM story.

## Structure: tagging, parsing, and beyond (SLP3 Vol. III; appendices A, E, F)
**Sequence labelling**: POS tagging (Penn Treebank's 45 tags; ~97 % accuracy), **NER** (BIO
tagging of spans; entity-level F1); models: **HMMs** with Viterbi ([[bayesian-networks-and-hmms]]),
MEMMs and **CRFs** (discriminative, global normalization — avoid the label-bias problem),
BiLSTM-CRFs (2015–16), fine-tuned BERT (2018 → ~93 F1 on CoNLL). **Parsing**: constituency
(CFGs — [[context-free-grammars]]; PCFGs with CKY — [[dynamic-programming]]; treebanks) and
**dependency** parsing (head–dependent arcs; transition-based shift-reduce parsers with a
neural classifier — Chen & Manning 2014, the CS224N assignment — vs graph-based maximum
spanning tree — [[minimum-spanning-trees]]; metrics UAS/LAS). Semantics: semantic role
labelling, word senses (WordNet), **coreference** (mention detection + antecedent ranking),
discourse. Applications: **machine translation** (statistical phrase-based → neural seq2seq
→ transformer; **BLEU** = modified n-gram precision × brevity penalty against references;
chrF, COMET as learned metrics), summarization (**ROUGE** recall of n-grams), question
answering (extractive span F1/EM on SQuAD; open-domain with retrieval — [[large-language-models]]),
dialogue, speech (ASR with CTC/attention, TTS). All of these are now "prompt or fine-tune a
transformer", but their datasets and metrics are how progress is measured, and their
linguistics explains what the models get wrong.

## Pitfalls
- Comparing perplexities across different tokenizers or vocabularies.
- BLEU on a single reference or on short texts; ROUGE as a quality measure for abstractive
  summaries; any automatic metric without a human-eval sanity check.
- Assuming subword tokens align with morphemes or that the model "sees" characters.
- Treating embedding analogies as semantics (they are corpus statistics with biases).
- Training/test leakage through pretraining data contamination (benchmark answers in the
  corpus).

## Related
- [[large-language-models]], [[transformers-and-attention]],
  [[recurrent-neural-networks-and-lstms]], [[bayesian-networks-and-hmms]],
  [[linear-models-logistic-regression-and-glms]], [[entropy-and-information]],
  [[tf-idf-and-vector-space-model]], [[dense-retrieval-and-embeddings]], [[svd-and-pca]],
  [[context-free-grammars]], [[dynamic-programming]], [[machine-learning-basics]],
  [[fairness-in-machine-learning]], [[string-algorithms]].

## Sources
SLP3 2026 draft (chapter list read; content from earlier drafts); CS224N lectures 1–6, 9; CS336 assignment 1 (read); Shannon 1951; Mikolov et al. 2013; Pennington et al. 2014; Levy & Goldberg 2014; Sennrich et al. 2016; Kudo & Richardson 2018 (SentencePiece); Chen & Manning 2014; Papineni et al. 2002 (BLEU).

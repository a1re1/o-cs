---
title: NLP and LLM courses, texts and seminal papers — Jurafsky & Martin SLP3 (2026 draft, Volume I "Large Language Models"), Stanford CS224N, CS324, CS25, CS336 Language Modeling from Scratch, CMU 11-711, Hugging Face course, nanoGPT, Raschka; Shannon n-grams, word2vec, GloVe, seq2seq, Transformer, BERT, GPT-1/2/3, Kaplan scaling laws, Chinchilla, InstructGPT/RLHF, chain-of-thought, RAG, LoRA, FlashAttention, LLaMA, DPO, Constitutional AI, mixture-of-experts, test-time compute
type: source
section: "6.4"
level: 500
tags: [jurafsky-martin, slp3, speech-and-language-processing, cs224n, manning, cs324, cs25, cs336, language-modeling-from-scratch, 11-711, neubig, hugging-face-course, nanogpt, mingpt, karpathy, raschka, build-llm-from-scratch, shannon, n-gram, word2vec, mikolov, glove, pennington, seq2seq, vaswani, bert, devlin, gpt, radford, brown, kaplan, scaling-laws, chinchilla, hoffmann, instructgpt, ouyang, rlhf, chain-of-thought, wei, rag, lewis, lora, hu, flashattention, dao, llama, touvron, dpo, rafailov, constitutional-ai, rlaif, mixture-of-experts, shazeer, fedus, test-time-compute]
sources: []
authors: [Dan Jurafsky, James Martin, Christopher Manning, Percy Liang, Tatsunori Hashimoto, Graham Neubig, Andrej Karpathy, Sebastian Raschka, Claude Shannon, Tomas Mikolov, Jeffrey Pennington, Ilya Sutskever, Ashish Vaswani, Jacob Devlin, Alec Radford, Tom Brown, Jared Kaplan, Jordan Hoffmann, Long Ouyang, Jason Wei, Patrick Lewis, Edward Hu, Tri Dao, Hugo Touvron, Rafael Rafailov, Yuntao Bai, Noam Shazeer, William Fedus]
year: 2026
institution: Stanford / CMU
url: https://web.stanford.edu/~jurafsky/slp3/
license: mixed (SLP3 draft, course notes, HF course, nanoGPT free)
format: html
summary: Jurafsky & Martin's Speech and Language Processing 3rd edition (draft released August 2026) has been reorganized around language models — Volume I "Large Language Models" (words/tokenization, n-grams, naive Bayes and logistic regression for text, vector semantics and embeddings, neural LMs merged with the transformer chapter, fine-tuning and masked LMs, alignment, a new interpretability chapter), Volume II advanced LLM topics and tools, Volume III annotating linguistic structure (POS/NER, parsing, semantics, coreference, discourse), with HMMs and CFGs moved to appendices; CS224N (Manning) is the canonical NLP-with-deep-learning course (word vectors → RNNs → attention/transformers → pretraining → prompting/RLHF → interpretability), CS324 the LLM survey course (capabilities, harms, data, scaling, training, adaptation), CS336 the build-it-yourself course (assignments: basics — tokenizer/transformer/training loop from scratch; systems — profiling, FlashAttention in Triton, distributed training; scaling; data; alignment and reasoning RL), CMU 11-711 (Neubig) the research-oriented one; and the seminal papers run from Shannon's n-gram entropy estimates through word2vec/GloVe embeddings, seq2seq and the Transformer, BERT and GPT-1/2/3 (pretraining, in-context learning), Kaplan's scaling laws ("loss scales as a power law with model size, dataset size and compute … larger models are significantly more sample-efficient") and Chinchilla's compute-optimal correction, InstructGPT/RLHF, chain-of-thought prompting, RAG, LoRA, FlashAttention, LLaMA, DPO, Constitutional AI and RLAIF, mixture-of-experts, and the 2024–25 test-time-compute/reasoning-RL papers.
---
# NLP and LLMs: courses, texts, and seminal papers

## What they are
- **Jurafsky & Martin, SLP3** (draft Aug 2026; free): the field's textbook, rewritten
  around LLMs: **Vol. I Large Language Models** — introduction (new); words, tokens and
  regular expressions; n-gram language models; naive Bayes and sentiment; logistic
  regression; vector semantics and embeddings; neural networks and LLMs with transformers
  (the former ch. 7–8 merged); masked LMs and fine-tuning; model alignment, prompting and
  RLHF; interpretability (new, half-written); **Vol. II Advanced LLM topics and tools** —
  machine translation, question answering and retrieval/RAG, dialogue and chatbots,
  speech (phonetics, ASR, TTS); **Vol. III Annotating linguistic structure** — sequence
  labelling (POS, NER), dependency and constituency parsing, semantic roles, lexical
  semantics/WordNet, coreference, discourse; appendices: HMMs, naive Bayes, spelling
  correction/noisy channel, statistical parsing, CFGs, CCG. (The authors note using Claude
  Opus 5 to suggest exercises — the textbook is now partly written with its subject.)
- **CS224N** (Manning; videos 2017–2024): word vectors (word2vec, GloVe), neural
  classifiers, backprop, dependency parsing, RNNs/LSTMs, seq2seq + attention, transformers,
  pretraining (BERT/GPT/T5), NLG, prompting/RLHF, efficient adaptation, interpretability,
  multimodal, ethics. **CS324 LLMs** (Liang, Hashimoto, Ré; notes open): capabilities, harms
  (toxicity, bias, disinformation), data, security, legality, modelling, training,
  parallelism, scaling laws, selective architectures (MoE, retrieval), adaptation, environment
  impact. **CS25 Transformers United**: guest lectures. **CS336 Language Modeling from
  Scratch** (Liang, Hashimoto; 2025): five assignments — basics (BPE tokenizer, transformer,
  AdamW, training loop, no PyTorch modules), systems (profiling, FlashAttention-2 in Triton,
  distributed data parallel, optimizer sharding), scaling (fit scaling laws on a budget),
  data (filtering/dedup for pretraining, leaderboard), alignment and reasoning RL (SFT,
  DPO/GRPO on math). **CMU 11-711** (Neubig): research methods, modelling, data, evaluation.
  **Hugging Face NLP course**: tokenizers, transformers library, fine-tuning, datasets.
  **nanoGPT/minGPT** (Karpathy): GPT-2 reproduced in ~300 lines + training on OpenWebText;
  **Raschka, Build an LLM from Scratch**: the same in book form. **Manning, Raghavan &
  Schütze, IIR**: [[manning-irb]] (§10.3).
- **Seminal**: Shannon 1948/1951 (n-gram models, entropy of English); Mikolov et al. 2013
  (**word2vec**: skip-gram with negative sampling, analogies); Pennington et al. 2014
  (**GloVe**: co-occurrence factorization); Sutskever et al. 2014 (seq2seq); Vaswani et al.
  2017; Devlin et al. 2018 (**BERT**); Radford et al. 2018/2019, Brown et al. 2020 (**GPT-1/2/3**:
  generative pretraining; zero-shot task transfer; 175 B parameters and **in-context
  learning**); Kaplan et al. 2020 (**scaling laws**); Hoffmann et al. 2022 (**Chinchilla**: tokens
  should scale with parameters — ~20 tokens/param); Ouyang et al. 2022 (**InstructGPT**: SFT +
  reward model + PPO — **RLHF**); Wei et al. 2022 (**chain-of-thought** prompting; emergent
  abilities); Lewis et al. 2020 (**RAG**); Hu et al. 2021 (**LoRA**); Dao et al. 2022
  (**FlashAttention**); Touvron et al. 2023 (**LLaMA**: open weights, Chinchilla-plus training);
  Rafailov et al. 2023 (**DPO**: RLHF without a reward model or RL); Bai et al. 2022
  (**Constitutional AI**, RLAIF); Shazeer et al. 2017 / Fedus et al. 2021 (**mixture-of-
  experts**, Switch); Snell et al. 2024, OpenAI o1, DeepSeek-R1 2025 (**test-time compute**
  and reasoning RL with verifiable rewards).

## Key ideas → pages
[[nlp-fundamentals]], [[large-language-models]], [[scaling-laws]],
[[llm-post-training-sft-rlhf-dpo]], [[transformers-and-attention]],
[[recurrent-neural-networks-and-lstms]], [[dense-retrieval-and-embeddings]].

## What they add
SLP3 for the linguistics and the classical methods that still matter (tokenization,
n-grams, evaluation), CS224N for the deep-NLP arc, CS336 for the engineering (you cannot
understand LLM cost without building the tokenizer, the attention kernel, and the data
pipeline), CS324 for the harms and the economics; the paper sequence shows the field
collapsing from many tasks and architectures into one pretrained model plus prompting.

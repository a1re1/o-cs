---
title: Transfer Learning and Fine-Tuning
type: concept
section: "6.3"
level: 400
tags: [transfer-learning, fine-tuning, pretraining, lora, peft, domain-adaptation]
sources: [deep-learning-texts-courses-and-seminal-papers]
summary: Reusing a model pretrained on a large corpus for a new task — feature extraction vs full fine-tuning, parameter-efficient methods (LoRA/adapters), catastrophic forgetting, and when transfer helps.
---

# Transfer Learning and Fine-Tuning
**In one sentence.** Transfer learning reuses representations learned by a model
pretrained on a large, general dataset and adapts them to a new, usually smaller task —
the default recipe behind modern deep learning and LLMs.

## Why it matters
Training a large model from scratch needs enormous data and compute; most practitioners
never do it. Instead they start from a pretrained backbone (ImageNet CNN, BERT, a
foundation LLM) and adapt it, getting strong results from little task data. It is the
economic engine of applied ML and the reason [[large-language-models]] are useful across
tasks they were never explicitly trained on.

## How it works
**The pretrain → adapt paradigm.** Pretrain once on a huge corpus (supervised or, now
usually, [[self-supervised-and-contrastive-learning]]) to learn general features; then
adapt to the downstream task. Adaptation options, from cheapest to most expensive:
- **Feature extraction / linear probing** — freeze the backbone, train only a new head
  on top of its features. Fast, little data, but limited.
- **Fine-tuning** — continue training some or all backbone weights on the new task, with
  a small learning rate. More powerful, needs more data and care.
- **Parameter-efficient fine-tuning (PEFT)** — update only a tiny set of new parameters:
  **LoRA** (learn low-rank updates `ΔW = BA` to frozen weight matrices), **adapters**
  (small bottleneck layers), or **prompt/prefix tuning**. Gets most of full fine-tuning's
  quality at a fraction of the memory and produces small, swappable task deltas.

**Why it works.** Early layers learn general features (edges, syntax) that transfer
broadly; later layers are task-specific. The closer the target domain to the pretraining
domain, the more transfers.

**Instruction tuning & RLHF** (for LLMs) are transfer learning at the alignment stage:
fine-tune a pretrained model on instruction-following data and human preferences to make
its general knowledge usable and safe.

## Complexity & trade-offs
- Full fine-tuning gives the best fit but costs a full copy of optimizer state and risks
  overfitting on small data; PEFT (LoRA) cuts trainable parameters by 100–1000× with
  minor quality loss and keeps the base model shared.
- Feature extraction is cheapest and safest on tiny data but caps performance.

## Pitfalls & gotchas
- **Catastrophic forgetting** — aggressive fine-tuning erases pretrained knowledge; use a
  small learning rate, freeze early layers, or PEFT.
- **Domain mismatch** — transfer helps only if source and target share structure;
  distant domains can transfer *negatively*.
- **Data leakage from pretraining** — the pretrained model may have seen your test data;
  evaluate carefully.
- **Overfitting a small head** on a huge backbone; regularize and use early stopping.

## Worked example
A hospital has 2,000 labeled chest X-rays — far too few to train a CNN from scratch.
Starting from an ImageNet-pretrained ResNet, freezing the convolutional base and training
a new classifier head reaches high accuracy in minutes; unfreezing the top block with a
low learning rate squeezes out a further gain — the general visual features transferred.

## Related
- [[deep-learning-basics]] — the networks being transferred.
- [[self-supervised-and-contrastive-learning]] — how modern backbones are pretrained.
- [[large-language-models]] — fine-tuning and instruction tuning of foundation models.
- [[efficient-transformers-and-long-context]] — adapting big models cheaply.

## Sources
Distilled from [[deep-learning-texts-courses-and-seminal-papers]] (CS231n transfer learning; LoRA;
instruction tuning literature).

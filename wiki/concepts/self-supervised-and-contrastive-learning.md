---
title: Self-supervised and contrastive learning — pretext tasks, contrastive objectives (InfoNCE, SimCLR, MoCo with momentum encoders and queues), non-contrastive methods (BYOL, DINO self-distillation), masked modelling (BERT, MAE), CLIP's image–text contrastive pretraining and zero-shot transfer, foundation models and linear probing vs fine-tuning, and why representation learning without labels works
type: concept
section: "6.5"
level: 500
tags: [self-supervised-learning, ssl, representation-learning, pretext-tasks, contrastive-learning, infonce, noise-contrastive, simclr, augmentations, positive-pairs, negatives, temperature, moco, momentum-encoder, queue, byol, collapse, dino, self-distillation, masked-autoencoder, mae, masked-image-modeling, beit, clip, image-text, zero-shot, prompt-templates, foundation-models, linear-probe, fine-tuning, transfer, dinov2, sam, multimodal, alignment-uniformity, word2vec, bert]
sources: [computer-vision-texts-courses-and-seminal-papers]
summary: Self-supervised learning gets the supervision from the data itself — predict a masked part from the rest, or make two augmented views of the same image agree — so that representations can be pretrained on unlabeled web-scale data and then transferred with a linear probe or fine-tuning; contrastive methods (InfoNCE loss: pull positive pairs together, push apart negatives in a temperature-scaled softmax over similarities — the same objective as word2vec's negative sampling) include SimCLR (strong augmentations, large batches of in-batch negatives, a projection head) and MoCo (a momentum-updated encoder and a queue of negatives to decouple batch size from negative count); non-contrastive methods avoid negatives and prevent collapse by asymmetry — BYOL's predictor + stop-gradient target, DINO's self-distillation into a centred, sharpened teacher, whose ViT features segment objects without labels (DINOv2 is the default vision backbone); masked modelling (BERT for text, MAE for images: mask 75 % of patches, reconstruct pixels with a light decoder) scales without augmentations; CLIP contrasts 400 M image–caption pairs so that natural-language prompts become classifiers (zero-shot ImageNet, and the text encoder for Stable Diffusion, DALL·E, and vision-language models); and the general lesson is that a good pretext task forces the model to encode the invariances and structure the downstream tasks need, turning labels from the bottleneck into a small last-mile cost.
---
# Self-supervised and contrastive learning

**In one sentence.** Manufacture the labels — agreement between two views, or a masked
piece from its context — and the representation learned to solve that task transfers to
tasks you never labelled; contrastive learning is word2vec's trick applied to any
modality, and CLIP applies it across modalities so language becomes the label space.

## Why and how (CS231n lecture 12; Szeliski §5.4.6)
Labels are expensive; raw images/text/video are free. A **pretext task** must be solvable
only by understanding content: predicting rotation, relative patch position, colourization,
jigsaw, inpainting (2015–18 era) — each worked somewhat; two families won: **contrastive/
joint-embedding** (invariance to augmentations) and **masked/generative modelling**
(predict missing content). Evaluate by **linear probe** on frozen features (kNN accuracy on
ImageNet), fine-tuning, and transfer to detection/segmentation/depth; representation quality
is judged by **alignment** (positives close) and **uniformity** (features spread on the sphere).

## Contrastive learning (van den Oord 2018 CPC; Chen et al. 2020 SimCLR; He et al. 2020 MoCo)
**InfoNCE**: for an anchor z and its positive z⁺ among N candidates, L = −log
[exp(sim(z, z⁺)/τ) / Σⱼ exp(sim(z, zⱼ)/τ)] — a softmax classification of "which is my
positive", a lower bound on mutual information; temperature τ (~0.1) controls hardness;
cosine similarity on ℓ2-normalized features. Negatives are the other examples in the batch
(the same construction as word2vec's negative sampling — [[nlp-fundamentals]]).
**SimCLR**: two random **augmentations** (crop + resize, colour jitter, blur — the
augmentation choice *is* the specification of the invariances) of each image → encoder →
MLP **projection head** (contrast on the head's output, use the encoder's features
downstream); needs large batches (4k–8k) for enough negatives; long training. **MoCo**:
a **queue** of past keys as negatives and a **momentum encoder** (EMA of the query encoder)
for consistency — small batches, same quality; MoCo v3 for ViTs. Supervised contrastive,
hard-negative mining, multi-crop (SwAV) refine it. Failure mode: **collapse** (all outputs
identical satisfies alignment) — negatives prevent it here.

## Non-contrastive: BYOL and DINO (Grill et al. 2020; Caron et al. 2021; Oquab et al. 2023)
**BYOL**: online network with a predictor head regresses the target network's projection of
the other view; the target is an EMA of the online network; no negatives, and the
predictor + stop-gradient asymmetry empirically avoids collapse (SimSiam shows stop-gradient
alone suffices). **DINO**: self-**distillation** with no labels — student and EMA teacher
output softmax distributions over K prototypes; the teacher's output is **centred** (avoid
one-dimension collapse) and **sharpened** (avoid uniform collapse); trained on ViTs, its
attention maps segment foreground objects with no supervision, and kNN on its features
rivals supervised training. **DINOv2** (142 M curated images, larger ViTs, patch-level
objectives) is the general-purpose frozen vision backbone (depth, segmentation, retrieval
work off its features). Related: Barlow Twins/VICReg (redundancy-reduction losses, no EMA).

## Masked modelling (Devlin 2018 BERT; He et al. 2021 MAE)
**BERT** for text ([[transformers-and-attention]]): mask 15 % of tokens, predict them —
bidirectional context, the pretraining that made NLP transfer. **MAE** for images: mask
**75 %** of patches, encode only the visible ones (cheap), reconstruct pixels with a
lightweight decoder, discard the decoder — scales to ViT-Huge, needs no augmentations,
fine-tunes better than contrastive methods though its linear probes are worse (pixels are
a low-level target; BEiT/iBOT use tokens or self-distilled targets — DINOv2 combines both).
Masked modelling extends to audio, video (VideoMAE), point clouds, proteins; autoregressive
next-token prediction is the same idea for sequences — LLM pretraining is self-supervised
learning ([[large-language-models]]).

## CLIP and multimodal contrast (Radford et al. 2021)
Image encoder (ResNet/ViT) and text encoder (transformer) trained on **400 M** web image–
caption pairs with a symmetric InfoNCE over the N×N batch similarity matrix — match each
image to its caption among N. Result: a shared embedding space; **zero-shot
classification** by embedding prompt templates ("a photo of a {class}") and picking the
nearest — 76 % ImageNet top-1 with no ImageNet training, robust to distribution shift
(sketches, adversarial sets) where supervised models fail; text-driven retrieval; the text
encoder conditions Stable Diffusion/DALL·E 2 ([[deep-generative-models]]); the image
encoder feeds vision-language models (LLaVA, GPT-4V — [[large-language-models]]). Caveats:
web-data bias, poor at counting/spatial relations/fine-grained text, and prompt sensitivity.
Open reproductions: OpenCLIP/LAION-5B; SigLIP (sigmoid loss, no global softmax).
Segment Anything (SAM) is the prompted-segmentation counterpart: 1 B masks, promptable by
points/boxes/text — a foundation model for masks ([[computer-vision-fundamentals]]).

## Foundation models and transfer
Pretrain once at scale (self-supervised, or weakly supervised via captions), then adapt:
frozen features + linear/kNN probe (cheapest, tests representation), **fine-tuning**
(best accuracy, needs care — LR, layer-wise decay), parameter-efficient adapters
(LoRA/prompt tuning — [[llm-post-training-sft-rlhf-dpo]], [[transfer-learning-and-fine-tuning]]),
distillation to small models. Scaling behaves like language ([[scaling-laws]]); data
curation (dedup, diversity) matters more than architecture. The conceptual point: the
pretext task defines which invariances (augmentation) or which structure (masking,
captions) the representation encodes — choosing it *is* choosing the inductive bias
([[machine-learning-basics]]).

## Pitfalls
- Weak augmentations in contrastive learning (the task becomes trivial) or augmentations
  that destroy the downstream signal (colour jitter for a colour-sensitive task).
- Small batches in SimCLR without MoCo-style queues; evaluating with the projection head.
- Collapse in non-contrastive methods when the asymmetry (EMA, predictor, centring) is
  removed.
- Reading CLIP zero-shot accuracy as understanding (prompt/template sensitivity; counting
  and relations fail).
- Fine-tuning a self-supervised backbone with the same LR as a supervised one.

## Related
- [[computer-vision-fundamentals]], [[convolutional-neural-networks]],
  [[transformers-and-attention]], [[large-language-models]], [[nlp-fundamentals]]
  (word2vec, BERT), [[deep-generative-models]], [[transfer-learning-and-fine-tuning]],
  [[llm-post-training-sft-rlhf-dpo]], [[scaling-laws]], [[machine-learning-basics]],
  [[dense-retrieval-and-embeddings]] (contrastively trained retrievers),
  [[entropy-and-information]] (InfoNCE as an MI bound).

## Sources
Chen et al. 2020 (SimCLR); He et al. 2020 (MoCo); van den Oord et al. 2018 (CPC/InfoNCE); Grill et al. 2020 (BYOL); Chen & He 2021 (SimSiam); Caron et al. 2021 (DINO); Oquab et al. 2023 (DINOv2); He et al. 2021 (MAE); Radford et al. 2021 (CLIP); Kirillov et al. 2023 (SAM); Wang & Isola 2020 (alignment/uniformity); CS231n lecture 12 (schedule read).

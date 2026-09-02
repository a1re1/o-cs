---
title: Deep learning texts, courses and seminal papers — Goodfellow–Bengio–Courville, Dive into Deep Learning, Prince's Understanding Deep Learning, Nielsen, Fleuret's Little Book; CS231n, CS224N, MIT 6.S191, NYU DL, Michigan EECS 498, Karpathy's Zero to Hero, fast.ai; McCulloch–Pitts, Rosenblatt, backprop (1986), LeNet, LSTM, AlexNet, VGG, ResNet, BatchNorm, Adam, Dropout, GANs, VAEs, Bahdanau attention, "Attention Is All You Need", "rethinking generalization"
type: source
section: "6.3"
level: 400
tags: [goodfellow, deep-learning-book, d2l, dive-into-deep-learning, prince, understanding-deep-learning, nielsen, fleuret, little-book, cs231n, cs224n, 6-s191, nyu-deep-learning, lecun, eecs-498, karpathy, zero-to-hero, fast-ai, mcculloch-pitts, rosenblatt, rumelhart-hinton-williams, backpropagation, lenet, lstm, hochreiter, alexnet, vgg, resnet, batchnorm, adam, dropout, gan, vae, bahdanau, vaswani, attention-is-all-you-need, rethinking-generalization, pytorch, jax]
sources: []
authors: [Ian Goodfellow, Yoshua Bengio, Aaron Courville, Aston Zhang, Zachary Lipton, Mu Li, Alex Smola, Simon Prince, Michael Nielsen, François Fleuret, Fei-Fei Li, Justin Johnson, Andrej Karpathy, Yann LeCun, Geoffrey Hinton, David Rumelhart, Ronald Williams, Sepp Hochreiter, Jürgen Schmidhuber, Alex Krizhevsky, Kaiming He, Sergey Ioffe, Diederik Kingma, Nitish Srivastava, Ashish Vaswani, Dzmitry Bahdanau, Chiyuan Zhang]
year: 2016
institution: MIT Press / Stanford / NYU / Michigan
url: https://www.deeplearningbook.org/
license: mixed (all listed texts free online; courses open)
format: html
summary: Goodfellow, Bengio & Courville's Deep Learning (2016) is the reference in three parts — applied math and ML basics (linear algebra, probability and information theory, numerical computation, ML basics), modern practical deep networks (deep feedforward networks, regularization, optimization for training deep models, convolutional networks, sequence modelling with recurrent and recursive nets, practical methodology, applications), and research (linear factor models, autoencoders, representation learning, structured probabilistic models, Monte Carlo methods, the partition function, approximate inference, deep generative models); Dive into Deep Learning (interactive, PyTorch/JAX/TF) and Prince's Understanding Deep Learning (2023, the modern successor with transformers, diffusion, and the ethics chapter) are the free teaching texts, Nielsen and Fleuret the short ones; CS231n (2025: linear classifiers, regularization and optimization, backprop, CNNs and architectures, RNNs, attention and transformers, detection/segmentation, video, large-scale distributed training, self-supervised learning, generative models, 3D, vision-language, world models) and Karpathy's Zero to Hero (micrograd → makemore → GPT from scratch) are the courses that teach by building; and the seminal papers trace the line from McCulloch–Pitts neurons (1943) and Rosenblatt's perceptron (1958) through backpropagation (Rumelhart, Hinton & Williams 1986), LeNet (1998), LSTM (1997), AlexNet (2012 — GPUs, ReLU, dropout; the ImageNet moment), VGG, ResNet (2015 — residual connections make 100+ layers trainable), BatchNorm, Adam, Dropout, GANs and VAEs (2013–14), Bahdanau attention (2014), the Transformer (2017), and Zhang et al.'s "rethinking generalization" (2017 — networks memorize random labels, so classical capacity measures don't explain why they generalize).
---
# Deep learning: texts, courses, and seminal papers

## What they are
- **Goodfellow, Bengio & Courville** (2016; free): I applied math & ML basics (2 linear
  algebra, 3 probability and information theory, 4 numerical computation, 5 ML basics);
  II modern practical deep networks (6 deep feedforward networks, 7 regularization, 8
  optimization for training deep models, 9 convolutional networks, 10 sequence modelling:
  recurrent and recursive nets, 11 practical methodology, 12 applications); III research
  (13 linear factor models, 14 autoencoders, 15 representation learning, 16 structured
  probabilistic models, 17 Monte Carlo methods, 18 confronting the partition function,
  19 approximate inference, 20 deep generative models). Pre-transformer, but Parts I–II
  remain the cleanest statement of the fundamentals.
- **Dive into Deep Learning** (Zhang, Lipton, Li, Smola; free, runnable): preliminaries,
  linear/softmax regression, MLPs, builders' guide, CNNs and modern CNNs, RNNs and modern
  RNNs, attention mechanisms and transformers, optimization algorithms, computational
  performance, computer vision, NLP pretraining and applications, RL, GPs, hyperparameter
  optimization, GANs, recommender systems. Every concept ships with code in PyTorch/JAX/TF.
- **Prince, Understanding Deep Learning** (2023; free): supervised learning, shallow and deep
  networks, loss functions, fitting (SGD, Adam), gradients and initialization, measuring
  performance, regularization, CNNs, residual networks, transformers, graph neural
  networks, unsupervised learning, GANs, normalizing flows, VAEs, diffusion models, RL,
  why does deep learning work?, ethics. Best figures in the field.
- **Nielsen, Neural Networks and Deep Learning** (free): backprop derived slowly, the
  universal approximation visual proof, why deep nets are hard to train (vanishing
  gradients). **Fleuret, The Little Book of Deep Learning** (free, phone-sized): the whole
  field in 160 pages. **Deep Learning with PyTorch** (Stevens, Antiga, Viehmann).
- **Courses**: **CS231n** (Stanford; 2025 schedule: image classification with linear
  classifiers; regularization and optimization; neural networks and backprop; CNNs; CNN
  architectures; RNNs; attention and transformers (ViT); detection, segmentation,
  visualization (DETR); video; large-scale distributed training; self-supervised learning
  (DINO); generative models 1–2 (ELBO, diffusion); 3D vision; vision and language; world
  models); **CS224N** (NLP with deep learning — [[nlp-and-llm-courses-texts-and-seminal-papers]]);
  **MIT 6.S191** (one-week bootcamp); **NYU Deep Learning** (LeCun & Canziani — energy-based
  models, self-supervised learning); **Michigan EECS 498-007** (Johnson — the CS231n
  successor with more depth on attention and generative models); **UvA notebooks**;
  **Karpathy, Neural Networks: Zero to Hero** (micrograd autograd engine → makemore
  bigram/MLP/WaveNet character models → building GPT and a tokenizer from scratch);
  **fast.ai** part 2 (diffusion from scratch); **CMU 11-785**.
- **Seminal**: McCulloch & Pitts 1943 (threshold neurons compute logic); Rosenblatt 1958
  (perceptron and its learning rule; Minsky–Papert 1969 XOR limits); Rumelhart, Hinton &
  Williams 1986 ("Learning representations by back-propagating errors" — hidden units learn
  features); LeCun et al. 1998 (LeNet-5: convolution + pooling + gradient-based learning on
  MNIST); Hochreiter & Schmidhuber 1997 (LSTM: gated constant-error carousel against
  vanishing gradients); Krizhevsky, Sutskever & Hinton 2012 (AlexNet: 8 layers, ReLU,
  dropout, two GPUs, ImageNet top-5 error 15.3 % vs 26.2 %); Simonyan & Zisserman 2014
  (VGG: 3×3 convolutions stacked deep); He et al. 2015 (ResNet: identity skip connections,
  152 layers, 3.57 %); Ioffe & Szegedy 2015 (BatchNorm); Kingma & Ba 2014 (Adam);
  Srivastava et al. 2014 (Dropout); Goodfellow et al. 2014 (GANs); Kingma & Welling 2013
  (VAEs); Bahdanau, Cho & Bengio 2014 (attention for translation); Vaswani et al. 2017
  ("Attention Is All You Need"); Zhang et al. 2017 ("Understanding deep learning requires
  rethinking generalization": standard nets fit random labels perfectly, so VC/Rademacher
  bounds and explicit regularizers cannot be the explanation).

## Key ideas → pages
[[deep-learning-basics]], [[neural-network-training]], [[convolutional-neural-networks]],
[[recurrent-neural-networks-and-lstms]], [[transformers-and-attention]],
[[deep-generative-models]]; theory in [[generalization-bias-variance-and-regularization]]
and [[statistical-learning-theory]]; hardware in [[gpu-programming-cuda]].

## What they add
Goodfellow for the math and the pre-2016 canon; D2L for runnable everything; Prince for the
post-transformer field and the "why does it work" chapter; Karpathy for building each piece
by hand; CS231n as the course whose syllabus tracks the field year by year (its 2025 version
is half transformers, self-supervision, and generative models).

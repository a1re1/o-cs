---
title: Training deep networks — SGD with momentum, RMSProp and Adam/AdamW, learning-rate schedules and warmup, batch size, initialization (Xavier/He), vanishing and exploding gradients, gradient clipping, normalization (BatchNorm, LayerNorm), residual connections, regularization (weight decay, dropout, data augmentation, early stopping), mixed precision, debugging recipes, and why over-parameterized nets generalize
type: concept
section: "6.3"
level: 400
tags: [neural-network-training, optimization, sgd, minibatch, momentum, nesterov, rmsprop, adagrad, adam, adamw, weight-decay, learning-rate, learning-rate-schedule, warmup, cosine-schedule, batch-size, initialization, xavier-init, he-init, vanishing-gradients, exploding-gradients, gradient-clipping, batchnorm, batch-normalization, layernorm, layer-normalization, residual-connections, skip-connections, regularization, dropout, data-augmentation, early-stopping, label-smoothing, mixed-precision, bf16, fp16, loss-scaling, hyperparameter-tuning, debugging, overfit-one-batch, loss-curves, rethinking-generalization, implicit-bias, flat-minima, loss-landscape, checkpointing]
sources: [deep-learning-texts-courses-and-seminal-papers]
summary: Deep networks are trained by minibatch stochastic gradient descent on a non-convex loss, and the practical art is making that converge: momentum smooths noisy gradients, Adam (per-parameter adaptive step sizes from running first and second moment estimates, with bias correction) is the robust default and AdamW decouples weight decay from the adaptive scaling; learning rate is the hyperparameter that matters most, with warmup then cosine/step decay, and batch size interacts with it (linear scaling); depth makes gradients vanish or explode multiplicatively, which is countered by initialization that preserves activation variance (Xavier for tanh, He for ReLU), by normalization layers (BatchNorm normalizes per-feature over the batch — with train/test statistics mismatch and batch-size dependence — LayerNorm normalizes per example and is the transformer default), by residual connections that give gradients an identity path (ResNet: the reason 100+ layers train at all), and by gradient clipping for RNNs/transformers; regularization is weight decay, dropout (randomly zero units in training, scale at test), data augmentation, early stopping and label smoothing, with mixed precision (bf16/fp16 with loss scaling) for speed; the recipe for debugging is overfit a single batch first, watch loss curves and gradient norms, and change one thing at a time; and the theoretical puzzle is that nets with enough capacity to memorize random labels still generalize on real data — explained by the implicit bias of SGD toward simple (flat, low-norm, max-margin) solutions rather than by classical capacity control.
---
# Training deep networks

**In one sentence.** Minibatch SGD on a non-convex loss works if you keep the gradient
signal alive through depth (good init, normalization, residuals, clipping), scale the step
per parameter (Adam) with a warmup-then-decay schedule, and regularize with weight decay,
dropout and augmentation — then verify each piece by overfitting one batch before trusting
a run.

## Optimizers (Goodfellow ch. 8; D2L ch. 12; CS231n lecture 3)
**Minibatch SGD**: θ ← θ − η ∇̂L on a batch of B examples (gradient noise is a feature —
regularizes and escapes saddles; B from 32 to thousands, limited by memory and by the
diminishing returns of larger batches). **Momentum**: v ← βv + ∇̂L, θ ← θ − ηv (β = 0.9) —
averages gradients, accelerates along consistent directions, damps oscillation in ravines
(Nesterov looks ahead). **AdaGrad** divides by the root of accumulated squared gradients
(good for sparse features, decays to zero); **RMSProp** uses an exponential moving average
instead. **Adam** (Kingma & Ba 2014): m ← β₁m + (1−β₁)g, v ← β₂v + (1−β₂)g², bias-correct
m̂ = m/(1−β₁ᵗ), v̂ = v/(1−β₂ᵗ), θ ← θ − η m̂/(√v̂ + ε) with β₁ = 0.9, β₂ = 0.999 — per-parameter
step sizes, robust to gradient scale; the default for transformers and most new problems.
**AdamW** (Loshchilov & Hutter 2017): apply weight decay directly to θ instead of through
the adaptive gradient (L2 and weight decay differ under Adam) — the standard now. SGD +
momentum can generalize slightly better for CNNs with a tuned schedule; Adam wins on
convenience and on transformers. Second-order/K-FAC/Shampoo, LAMB/LARS for huge batches,
Lion, Muon are the research frontier. The optimizer is not the bottleneck — the **learning
rate** is: too high diverges or plateaus high, too low crawls; sweep on a log scale.
**Schedules**: linear **warmup** (avoids early Adam instability with large v̂ variance —
essential for transformers), then step decay, **cosine** annealing to ~0, or inverse-sqrt;
one-cycle; restarts. **Batch size**: larger batches → larger η (linear scaling rule, Goyal et
al. 2017) up to a critical batch size beyond which steps stop getting more useful
([[distributed-training-and-ml-systems]]).

## Keeping gradients alive through depth
The gradient at layer ℓ is a product of L − ℓ Jacobians; if their singular values are
< 1 it **vanishes** (early layers don't learn; sigmoid/tanh saturation makes it worse), if
> 1 it **explodes** (NaNs; RNNs over long sequences — [[recurrent-neural-networks-and-lstms]]).
- **Initialization**: zero init breaks symmetry (all units identical) — use random; too
  large saturates, too small vanishes. **Xavier/Glorot** Var(w) = 2/(n_in + n_out) (for
  tanh/linear) and **He** Var(w) = 2/n_in (for ReLU, which halves the variance) keep
  activation and gradient variance constant across layers; orthogonal init for RNNs;
  biases zero; final layer small (or zero for residual branches — "fixup"). Depth-scaled
  init (µP / maximal-update parameterization) makes hyperparameters transfer across widths.
- **Normalization**: **BatchNorm** (Ioffe & Szegedy 2015) — per feature, subtract the batch
  mean and divide by batch std, then learn scale γ and shift β; smooths the loss landscape,
  allows higher η, regularizes slightly; needs running statistics at test time (the
  train/test mismatch bug), couples examples in a batch (bad for small batches, RNNs,
  contrastive setups); placed after the linear map, before/after the activation.
  **LayerNorm** (Ba et al. 2016) — normalize over the features of each example: batch-
  independent, the choice for transformers and RNNs (pre-LN ordering is stabler than
  post-LN; RMSNorm drops the mean); GroupNorm/InstanceNorm for vision with small batches.
- **Residual connections** (He et al. 2015): y = x + F(x) — the identity path gives every
  layer a direct gradient route (∂y/∂x = I + ∂F/∂x), turns depth into an ensemble of
  shallower paths, and made 152–1000-layer networks trainable; ubiquitous (ResNets,
  transformers, U-Nets). Highway networks, DenseNet variants.
- **Gradient clipping**: rescale the gradient to a max norm (1.0 typical) — mandatory for
  RNNs and transformers to survive rare exploding steps.

## Regularization (Goodfellow ch. 7; Srivastava et al. 2014)
**Weight decay** (L2 / AdamW's decoupled version — 0.01–0.1 for transformers); **dropout**:
during training zero each unit with probability p (0.1–0.5) and scale survivors by 1/(1−p)
("inverted dropout"), at test use the full network — prevents co-adaptation, approximates
an ensemble of 2ⁿ thinned nets; **data augmentation** (crops, flips, colour jitter, mixup,
CutMix, RandAugment for images; SpecAugment; back-translation and token dropout for text) —
the cheapest large gain in vision; **early stopping** on validation loss; **label
smoothing** (targets 0.9/0.1 instead of 1/0 — better calibration); stochastic depth;
noise; **multi-task and pretraining** as regularizers ([[transfer-learning-and-fine-tuning]]).
The theory: [[generalization-bias-variance-and-regularization]].

## Mixed precision, memory, and throughput
**bf16/fp16** compute with fp32 master weights ([[floating-point]]): halves memory and
doubles-to-quadruples tensor-core throughput; fp16 needs **loss scaling** (multiply the loss
so small gradients don't underflow, unscale before the update), bf16 has fp32's exponent
range and usually doesn't; fp8 for the largest models. Memory = weights + gradients +
optimizer state (Adam: 2 extra copies → 16 bytes/param in mixed precision) + activations
(dominant; reduce with gradient checkpointing, smaller batches, activation offload).
Throughput: fuse kernels, use channels-last/tensor cores, data-loader parallelism, profile
before guessing ([[gpu-programming-cuda]], [[profiling-and-performance]]); scale across
devices with data/tensor/pipeline parallelism and ZeRO/FSDP ([[distributed-training-and-ml-systems]]).

## The recipe (Karpathy 2019; Goodfellow ch. 11)
1. Inspect the data; build a dumb baseline; fix seeds. 2. **Overfit one batch** to ~0 loss —
if you can't, the model/loss/backprop is broken. 3. Verify the initial loss (log k for
k-class CE), inputs and augmentations by eye, that the data isn't leaking. 4. Get a decent
model to overfit the full training set, then regularize (more data, augmentation, dropout,
weight decay, smaller model) until validation improves. 5. Tune η first, then the rest,
by random search over log-uniform ranges; one change at a time; keep loss curves, gradient
norms, and update/weight ratios (~1e-3) on a dashboard. 6. Ensemble / average checkpoints
(SWA, EMA weights). Common NaN sources: η too high, no clipping, fp16 overflow, log(0),
division by a zero norm.

## Why does it generalize? (Zhang et al. 2017; Prince ch. 20)
Standard nets fit **random labels** to 100 % training accuracy, so their capacity is enough
to memorize anything, and explicit regularizers are neither necessary nor sufficient for
generalization — yet on real labels the same nets generalize. The explanation is the
**implicit bias** of the training procedure: SGD from small init finds solutions that are
low-norm / max-margin (for logistic loss the direction converges to the max-margin
separator), flat (noise in SGD prefers wide minima, which are robust to parameter
perturbation — connected to PAC-Bayes and compression bounds), and learns simple functions
first (spectral bias toward low frequencies); real data is learnable by such simple
functions and random labels are not, so training on real data is faster and lands in a
generalizing basin. Double descent, the neural tangent kernel (infinite-width limit), and
lottery tickets are the surrounding theory ([[statistical-learning-theory]],
[[generalization-bias-variance-and-regularization]]); the honest summary is that
optimization and generalization are entangled and the classical separation into
"capacity" and "search" does not hold for deep nets.

## Pitfalls
- No warmup with Adam on transformers (divergence); no clipping on RNNs.
- BatchNorm with tiny batches or in `train()` mode at inference.
- Weight decay applied to biases/LayerNorm gains; L2 with Adam instead of AdamW.
- Tuning ten things at once; reporting the best of many seeds without saying so.
- Assuming a lower training loss means a better model (check validation; check calibration).

## Related
- [[deep-learning-basics]], [[gradient-descent]], [[convexity]] (what you lose),
  [[convolutional-neural-networks]], [[recurrent-neural-networks-and-lstms]],
  [[transformers-and-attention]], [[generalization-bias-variance-and-regularization]],
  [[statistical-learning-theory]], [[floating-point]], [[gpu-programming-cuda]],
  [[profiling-and-performance]], [[distributed-training-and-ml-systems]],
  [[transfer-learning-and-fine-tuning]].

## Sources
Goodfellow ch. 7–8, 11 (ToC read); D2L ch. 12; Prince ch. 6–9, 20; CS231n lecture 3 (schedule read); Kingma & Ba 2014; Loshchilov & Hutter 2017; Ioffe & Szegedy 2015; Ba et al. 2016; He et al. 2015 (ResNet and He init); Glorot & Bengio 2010; Srivastava et al. 2014; Zhang et al. 2017; Karpathy, "A Recipe for Training Neural Networks" 2019; Goyal et al. 2017.

---
title: Deep learning basics — neurons and layers, activations (sigmoid, tanh, ReLU and variants), multilayer perceptrons and the universal approximation theorem, depth vs width, loss functions (cross-entropy, MSE), forward and backward passes, backpropagation as reverse-mode automatic differentiation, computational graphs, and PyTorch/JAX autograd
type: concept
section: "6.3"
level: 400
tags: [deep-learning, neural-networks, neuron, perceptron, mlp, multilayer-perceptron, feedforward, hidden-layers, activation-functions, sigmoid, tanh, relu, leaky-relu, gelu, swish, softmax, universal-approximation, depth-vs-width, representation-learning, loss-functions, cross-entropy, mse, logits, forward-pass, backward-pass, backpropagation, chain-rule, computational-graph, automatic-differentiation, reverse-mode, forward-mode, jacobian-vector-product, autograd, pytorch, jax, micrograd, vectorization, gpu, dead-relu, xor]
sources: [deep-learning-texts-courses-and-seminal-papers]
summary: A neural network composes affine maps with elementwise nonlinearities — h = σ(Wx + b), stacked — so that hidden layers learn features instead of engineers designing them; a single hidden layer can approximate any continuous function (universal approximation), but depth buys exponential efficiency for compositional structure, which is why "deep" matters; ReLU replaced sigmoid/tanh because it doesn't saturate (no vanishing gradient for positive inputs) and is cheap, with GELU/SiLU variants in transformers; the output layer plus loss follows the GLM logic (softmax + cross-entropy for classification, linear + MSE for regression); training minimizes the loss by gradient descent, and the gradient of a scalar loss with respect to millions of parameters is computed in one backward pass by backpropagation — the chain rule applied in reverse topological order over the computational graph, caching forward activations and propagating vector–Jacobian products, which costs about as much as the forward pass (reverse-mode automatic differentiation; forward mode costs one pass per input dimension) — and frameworks (PyTorch, JAX) build that graph dynamically, so a practitioner writes the forward function and gets gradients for free, which Karpathy's micrograd shows fits in 100 lines.
---
# Deep learning basics

**In one sentence.** Stack affine maps and nonlinearities, define a differentiable loss, and
let reverse-mode automatic differentiation hand you the gradient of every parameter at the
cost of one backward pass — everything else in deep learning is about what to stack and
how to make that gradient descent work.

## From perceptron to MLP (Goodfellow ch. 6; Nielsen ch. 1–2; D2L ch. 5)
A **neuron** computes σ(wᵀx + b); a **layer** computes σ(Wx + b) for all neurons at once
(matrix multiply — [[matrices-and-linear-maps]]); an **MLP** stacks layers: h₁ = σ(W₁x + b₁),
h₂ = σ(W₂h₁ + b₂), …, ŷ = W_L h_{L−1} + b_L. Without nonlinearities the composition is one
affine map (no gain from depth); with them, hidden units become learned **features** —
Rumelhart, Hinton & Williams' point, and the difference from [[linear-models-logistic-regression-and-glms]]
with hand-built feature maps. The perceptron's XOR failure (Minsky–Papert) is solved by one
hidden layer. Output layer + loss by task, as in GLMs: linear + **MSE** (Gaussian), sigmoid +
binary cross-entropy (Bernoulli), **softmax + cross-entropy** (multinomial; compute
log-softmax stably — subtract the max; [[floating-point]]), and the raw outputs are **logits**.

## Activations
**Sigmoid** σ(z) = 1/(1+e^{−z}) and **tanh** saturate: gradients ≤ 0.25 (σ) vanish through
many layers ([[neural-network-training]]); **ReLU** max(0, z) (Nair & Hinton 2010; AlexNet)
— non-saturating for z > 0, sparse, cheap; risks **dead ReLUs** (units stuck at 0 forever,
from large negative bias or a big learning rate) → Leaky ReLU, PReLU, ELU; **GELU**
z·Φ(z) and **SiLU/Swish** z·σ(z) — smooth ReLUs used in BERT/GPT/transformers; softplus.
Rule of thumb: ReLU for CNNs/MLPs, GELU in transformers, tanh/sigmoid only for gates and
outputs.

## Universal approximation and why depth (Goodfellow 6.4; Nielsen ch. 4; Prince ch. 3–4)
**Universal approximation** (Cybenko 1989, Hornik 1991): one hidden layer with enough units
approximates any continuous function on a compact set to any accuracy — with sigmoid or
ReLU (a ReLU network is piecewise linear; more units → more pieces). But "enough" can be
exponential: **depth** represents compositional / hierarchical functions with exponentially
fewer units than a shallow net (Montúfar et al. 2014 — the number of linear regions grows
exponentially with depth, polynomially with width; Telgarsky 2016 separation). Deep nets are
a prior that the function is a composition of simpler functions — right for images
(edges → textures → parts → objects — [[convolutional-neural-networks]]), speech, language.
Representation learning: the last hidden layer is a learned feature space in which a linear
classifier works — the reason for transfer learning and linear probes.

## Backpropagation (Goodfellow 6.5; Nielsen ch. 2; CS231n lecture 4; Karpathy micrograd)
Loss L(θ) over a minibatch; need ∂L/∂θ for every parameter. **Computational graph**: nodes
are operations, edges carry tensors; the **forward pass** computes values and caches them;
the **backward pass** applies the **chain rule** in reverse topological order — each node
receives ∂L/∂(its output) (the "upstream gradient"), multiplies by its local Jacobian, and
passes ∂L/∂(its inputs) downstream, summing contributions when an output fans out. For a
layer h = σ(Wx + b) with upstream δ = ∂L/∂h: ∂L/∂z = δ ⊙ σ'(z), ∂L/∂W = (∂L/∂z) xᵀ,
∂L/∂b = ∂L/∂z, ∂L/∂x = Wᵀ(∂L/∂z). Never form Jacobians explicitly — compute **vector–
Jacobian products** (for matmul, sigmoid, ReLU, softmax-cross-entropy the VJPs are simple
closed forms; the softmax + CE gradient is just p − y). Cost: the backward pass ≈ 2× the
forward FLOPs; memory holds all activations (the training-memory bottleneck; gradient
checkpointing recomputes them). **Reverse-mode AD** computes the gradient of one scalar
output with respect to n inputs in one pass — ideal for training; **forward-mode** (dual
numbers, JVPs) costs one pass per input direction — ideal for few inputs / many outputs;
Hessian-vector products combine both. Numerical gradient checking (finite differences,
[[floating-point]] step choice) verifies hand-written backward functions.

## Frameworks: PyTorch and JAX
**PyTorch**: tensors with `requires_grad`; a **dynamic graph** recorded during the forward
call (define-by-run — control flow is plain Python); `loss.backward()` accumulates `.grad`;
`torch.nn.Module` for layers, `torch.optim` for updates, `torch.compile`/TorchScript for
fusion; distributed via DDP/FSDP ([[distributed-training-and-ml-systems]]). **JAX**:
pure-functional NumPy with composable transforms — `grad`, `jit` (XLA compilation), `vmap`
(auto-batching), `pmap`/`shard_map`; explicit PRNG keys; Flax/Haiku/Equinox for modules;
favoured for TPUs and research on new training algorithms. Both lower to GPU kernels —
matmuls and fused elementwise ops ([[gpu-programming-cuda]]); **vectorize** over the batch
(one matmul per layer, never a Python loop over examples). **Micrograd** (Karpathy): a scalar
`Value` with `.data`, `.grad`, `_backward`, and a topological sort — the whole idea of
autograd in ~100 lines; makemore then builds a character-level MLP and, by hand, the
Batch-Norm and backward passes ("becoming a backprop ninja").

## Pitfalls
- Sigmoid hidden layers in deep nets (vanishing gradients); ReLU with a large learning rate
  (dead units); unscaled inputs.
- Computing softmax then log (overflow/underflow) instead of log-softmax.
- Forgetting to zero gradients between steps (PyTorch accumulates) or to call `.eval()`
  for dropout/BatchNorm at test time.
- Believing a universal approximator will *learn* the function — approximation ≠
  optimization ≠ generalization ([[neural-network-training]],
  [[generalization-bias-variance-and-regularization]]).

## Related
- [[neural-network-training]] (optimization, initialization, normalization, regularization),
  [[convolutional-neural-networks]], [[recurrent-neural-networks-and-lstms]],
  [[transformers-and-attention]], [[deep-generative-models]],
  [[linear-models-logistic-regression-and-glms]], [[gradient-descent]],
  [[derivatives-and-gradients]], [[matrices-and-linear-maps]], [[floating-point]],
  [[gpu-programming-cuda]], [[distributed-training-and-ml-systems]], [[machine-learning-basics]].

## Sources
Goodfellow ch. 6 (ToC read); Nielsen ch. 1–4; D2L ch. 5; Prince ch. 3–4, 7; CS231n lectures 2–4 (schedule read); Karpathy, micrograd & makemore; Rumelhart, Hinton & Williams 1986; Cybenko 1989; Montúfar et al. 2014.

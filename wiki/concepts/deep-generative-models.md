---
title: Deep generative models — autoencoders and representation learning, variational autoencoders (ELBO, reparameterization), generative adversarial networks (minimax game, mode collapse, WGAN, StyleGAN), autoregressive models (PixelCNN, WaveNet, LLMs), normalizing flows, diffusion models (forward noising, denoising score matching, DDPM/DDIM, classifier-free guidance, latent diffusion), energy-based models, and how to evaluate generation
type: concept
section: "6.3"
level: 500
tags: [generative-models, autoencoder, denoising-autoencoder, latent-space, representation-learning, vae, variational-autoencoder, elbo, reparameterization-trick, posterior-collapse, gan, generative-adversarial-network, discriminator, generator, minimax, jensen-shannon, mode-collapse, wgan, wasserstein, spectral-normalization, stylegan, autoregressive, pixelcnn, wavenet, normalizing-flows, invertible, change-of-variables, realnvp, glow, diffusion-models, ddpm, ddim, score-matching, denoising, noise-schedule, classifier-free-guidance, latent-diffusion, stable-diffusion, u-net, dit, energy-based-models, likelihood, fid, inception-score, precision-recall, sampling-speed, text-to-image]
sources: [deep-learning-texts-courses-and-seminal-papers]
summary: Generative models learn a distribution p(x) from samples so they can sample new x (images, audio, text, molecules) or score likelihoods, and the deep-learning families differ in what they optimize — autoencoders compress to a latent code and reconstruct (representation learning, not a generative model until the latent is given a prior); VAEs maximize the ELBO (reconstruction − KL to a prior) with an encoder network and the reparameterization trick, giving a proper likelihood bound and smooth latents but blurry samples; GANs pit a generator against a discriminator in a minimax game whose optimum matches the data distribution (Jensen–Shannon), producing sharp samples at the cost of unstable training, mode collapse and no likelihood (WGAN, spectral normalization, progressive growing and StyleGAN tamed it); autoregressive models factor p(x) = Π p(xᵢ | x<ᵢ) exactly (PixelCNN, WaveNet, and language models — the family that scaled), with slow sequential sampling; normalizing flows chain invertible maps with tractable Jacobians for exact likelihood and fast sampling at the cost of architectural constraints; and diffusion models (2020–) gradually noise data to Gaussian and learn to reverse it step by step by predicting the noise (denoising score matching; an ELBO on a chain of latents), which are stable to train, produce state-of-the-art images/audio/video, and are steered by classifier-free guidance and made affordable by working in a compressed latent space (Stable Diffusion) with U-Net or transformer (DiT) denoisers — evaluated by FID, precision/recall and human preference since likelihood and sample quality disagree.
---
# Deep generative models

**In one sentence.** Every deep generative model is a way to turn a simple noise distribution
into the data distribution — by decoding a latent (VAE), by fooling a critic (GAN), one
dimension at a time (autoregressive), by an invertible map (flow), or by learning to undo
noise one small step at a time (diffusion) — and the families trade likelihood, sample
quality, sampling speed, and training stability.

## Autoencoders and VAEs (Goodfellow ch. 14, 20; CS231n lecture 13; Prince ch. 17)
**Autoencoder**: encoder z = f(x), decoder x̂ = g(z), minimize reconstruction; a low-
dimensional or sparse/denoising/contractive bottleneck forces a useful representation
(PCA when linear — [[svd-and-pca]]); used for pretraining, compression, anomaly detection —
but sampling z at random gives garbage because the latent space has no prior. **VAE**
(Kingma & Welling 2013): p(z) = N(0, I), decoder p_θ(x | z), encoder q_φ(z | x) = N(μ_φ(x),
diag σ_φ²(x)); maximize the **ELBO** E_q[log p_θ(x | z)] − KL(q_φ(z | x) ‖ p(z)) — derivation
in [[unsupervised-learning-em-and-mixture-models]]; the **reparameterization trick** z = μ +
σ ⊙ ε makes the expectation differentiable; sample by decoding z ~ N(0, I). Properties: a
likelihood bound, smooth interpolable latents, disentanglement with β-VAE, fast sampling;
**blurry** samples (Gaussian likelihood averages modes) and **posterior collapse** (a strong
decoder ignores z — KL annealing, free bits). **VQ-VAE** quantizes the latent into a codebook
(discrete tokens for images/audio — the tokenizer under DALL·E 1, Parti, and audio LMs).

## GANs (Goodfellow et al. 2014; CS231n lecture 14)
Generator G(z) maps noise to samples; discriminator D(x) estimates P(real). **Minimax**:
min_G max_D E_x[log D(x)] + E_z[log(1 − D(G(z)))]; for the optimal D the objective equals
2·JS(p_data ‖ p_G) − log 4, so the equilibrium is p_G = p_data. Training alternates D and
G steps (non-saturating G loss −log D(G(z)) for gradient early). Problems: **mode collapse**
(G covers a few modes), oscillation, vanishing D gradients when supports don't overlap, no
likelihood, hard evaluation. Fixes: **WGAN** (Wasserstein/earth-mover distance via a
1-Lipschitz critic — weight clipping → gradient penalty; meaningful loss curves), **spectral
normalization**, two-timescale updates, DCGAN architecture rules, progressive growing,
**StyleGAN** (mapping network, adaptive instance norm, style mixing — photorealistic faces at
1024², disentangled latents), BigGAN (class-conditional at ImageNet scale), conditional GANs
(pix2pix, CycleGAN with cycle consistency for unpaired translation). GANs give sharp samples
and fast sampling (one forward pass) and still power super-resolution and some real-time
uses; diffusion replaced them for general synthesis.

## Autoregressive models and flows
**Autoregressive**: p(x) = Π_i p(x_i | x_{<i}) — exact likelihood, trained by teacher forcing
with masking (**PixelCNN**/PixelRNN over pixels, **WaveNet** with dilated causal convolutions
over audio samples, transformers over tokens — [[large-language-models]] are the
autoregressive family that scaled); sampling is sequential (T forward passes), which is why
images/audio moved to diffusion or discrete tokens + transformers (VQ-VAE + LM). **Normalizing
flows** (NICE/RealNVP/Glow): x = f(z) with f invertible and log|det ∂f/∂x| tractable
(coupling layers, affine transforms, 1×1 invertible convs); exact log-likelihood by change
of variables, fast sampling and inference; constrained architectures, large models for
modest quality; continuous flows (neural ODEs) and **flow matching** (2022) now unify flows
with diffusion — regress a velocity field that transports noise to data along straight
paths.

## Diffusion models (Sohl-Dickstein 2015; Ho, Jain & Abbeel 2020 DDPM; Song et al. 2021)
**Forward process**: x_t = √(ᾱ_t) x₀ + √(1 − ᾱ_t) ε over T ≈ 1000 steps with a variance
schedule β_t, ending at pure Gaussian noise (a fixed Markov chain — [[markov-chains]]).
**Reverse process**: learn p_θ(x_{t−1} | x_t) as a Gaussian whose mean is given by a network
ε_θ(x_t, t) predicting the noise; the ELBO on this chain of latents reduces (DDPM) to the
simple loss E‖ε − ε_θ(x_t, t)‖² — **denoising score matching**: ε_θ ∝ −∇_x log p_t(x), the
**score**; sampling runs the learned reverse chain (ancestral sampling) or solves the
equivalent probability-flow ODE (**DDIM**, DPM-Solver: 10–50 steps instead of 1000;
consistency/distillation models: 1–4 steps). Stable to train (a regression loss, no
adversary), covers modes, scales; slow to sample. **Conditioning**: class labels or text
embeddings (CLIP/T5) via cross-attention in the denoiser ([[transformers-and-attention]]);
**classifier-free guidance** — train with the condition randomly dropped, then sample with
ε = ε(∅) + w·(ε(c) − ε(∅)), w ≈ 7, trading diversity for fidelity/adherence. **Latent
diffusion** (Rombach et al. 2022, Stable Diffusion): diffuse in the 8× downsampled latent
of a pretrained VAE — 50× cheaper; denoisers are **U-Nets** ([[convolutional-neural-networks]])
or **diffusion transformers (DiT)**; text-to-image (DALL·E 2/3, Imagen, SDXL, Midjourney),
video (Sora), audio, molecules/proteins (RFdiffusion), and planning; image editing via
inpainting/SDEdit/ControlNet. CS229's 2026 notes cover diffusion before LLMs
([[ml-courses-texts-and-seminal-papers]]).

## Energy-based models and evaluation (Goodfellow ch. 16–18; NYU DL)
**EBMs**: p(x) ∝ e^{−E_θ(x)} — any scalar network is a density up to the intractable partition
function; train by contrastive divergence / MCMC ([[monte-carlo-methods]]) or score matching
(which is where diffusion came from); LeCun's framing of self-supervised learning as
energy shaping. **Evaluation**: likelihood (bits/dim — only for AR/flows/VAE bounds; poorly
correlated with sample quality); **Inception Score** and **FID** (Fréchet distance between
Inception-feature Gaussians of real and generated sets; sensitive to sample count and
domain); precision/recall for fidelity vs coverage; CLIP score for text alignment; human
preference (ELO arenas); for LLMs perplexity plus downstream evals ([[llm-evaluation-and-benchmarks]]).
Memorization and data provenance, deepfakes, and watermarking are the ethics surface
([[ai-safety-and-alignment]]).

## Pitfalls
- Sampling an autoencoder's latent without a prior; ignoring posterior collapse in VAEs.
- Judging GAN training by the loss (uninformative without WGAN); mode collapse unnoticed
  without diversity metrics.
- Diffusion with too few sampling steps and the wrong sampler; guidance scale too high
  (saturated, low-diversity images).
- Comparing FID across different sample sizes/resolutions/feature extractors.

## Related
- [[unsupervised-learning-em-and-mixture-models]] (ELBO, EM), [[svd-and-pca]],
  [[transformers-and-attention]], [[convolutional-neural-networks]], [[large-language-models]],
  [[markov-chains]], [[monte-carlo-methods]], [[neural-network-training]],
  [[llm-evaluation-and-benchmarks]], [[ai-safety-and-alignment]], [[game-theory]] (GAN
  minimax), [[computer-vision-fundamentals]].

## Sources
Goodfellow ch. 14, 16–20 (ToC read); CS231n lectures 13–14 (schedule read); Prince ch. 14–18; Kingma & Welling 2013; Goodfellow et al. 2014; Arjovsky et al. 2017 (WGAN); Karras et al. 2019 (StyleGAN); van den Oord et al. 2016 (PixelCNN, WaveNet); Dinh et al. 2017 (RealNVP); Ho et al. 2020 (DDPM); Song et al. 2021 (score SDEs); Ho & Salimans 2022 (CFG); Rombach et al. 2022 (latent diffusion); Peebles & Xie 2023 (DiT); Lipman et al. 2022 (flow matching).

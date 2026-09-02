---
title: Variational inference — posterior inference as optimization (KL(q‖p), the ELBO, and why it's a lower bound), mean-field factorization and coordinate-ascent VI, the exponential-family/conjugate case, stochastic VI for big data, black-box VI with score-function and reparameterization gradients, amortized inference (VAEs), expectation propagation, Bethe/loopy BP as variational, and VI vs MCMC
type: concept
section: "6.7"
level: 500
tags: [variational-inference, vi, elbo, evidence-lower-bound, kl-divergence, reverse-kl, forward-kl, mode-seeking, mean-field, factorized-approximation, cavi, coordinate-ascent, conjugate, exponential-family, natural-gradient, stochastic-variational-inference, svi, lda, topic-models, black-box-vi, score-function-estimator, reinforce, reparameterization-trick, pathwise-gradient, normalizing-flows-posterior, amortized-inference, encoder, vae, inference-network, amortization-gap, expectation-propagation, ep, bethe-free-energy, loopy-bp, marginal-polytope, underestimating-variance, importance-weighted, iwae, vi-vs-mcmc, pyro, numpyro, stan-advi, jordan-1999, blei-2017]
sources: [pgm-and-bayesian-texts-courses-and-seminal-papers]
summary: Variational inference turns the intractable posterior p(z|x) into an optimization problem — choose a tractable family Q and find q* = argmin KL(q(z) ‖ p(z|x)), which equals maximizing the ELBO E_q[log p(x, z)] − E_q[log q(z)] = log p(x) − KL(q ‖ p(z|x)), a lower bound on the log evidence that is tight when q is exact (the EM derivation of §6.2 is the special case where q is the exact posterior); with the mean-field family q = Π qⱼ(zⱼ), coordinate ascent (CAVI) sets each factor to exp(E_{−j}[log p(x, z)]) in closed form for conditionally conjugate exponential-family models (LDA's topic model is the classic), stochastic VI subsamples data and follows natural gradients to scale to millions of documents, and black-box VI removes the model-specific math by Monte Carlo gradients of the ELBO — the score-function (REINFORCE) estimator works for any model but is noisy, the reparameterization trick (z = g(ε, φ), pathwise gradients) is low-variance for continuous latents and is what makes VAEs train — with amortized inference (an encoder network q_φ(z|x) shared across data points) and richer families (normalizing flows, importance-weighted bounds) closing the gap; the reverse KL is mode-seeking and systematically underestimates posterior variance, expectation propagation minimizes the forward KL locally instead, and loopy belief propagation is VI on the Bethe free energy; compared with MCMC, VI is faster, scalable, and deterministic but biased — the choice is bias for speed.
---
# Variational inference

**In one sentence.** Can't compute the posterior? Pick a family of distributions you can
handle, and move within it to maximize a lower bound on the evidence — the gap is the KL
divergence to the truth, and every trick (mean field, natural gradients, reparameterization,
amortization, flows) is about making that gap small or the optimization cheap.

## The variational principle (Jordan et al. 1999; Blei, Kucukelbir & McAuliffe 2017)
Posterior p(z | x) = p(x, z)/p(x) with p(x) = ∫ p(x, z) dz intractable. For any q(z):
log p(x) = **ELBO**(q) + KL(q(z) ‖ p(z | x)), ELBO(q) = E_q[log p(x, z)] − E_q[log q(z)] =
E_q[log p(x | z)] − KL(q(z) ‖ p(z)) ("expected log-likelihood minus a complexity penalty").
Since KL ≥ 0, ELBO ≤ log p(x), with equality iff q = p(z | x); maximizing the ELBO over Q
minimizes KL(q ‖ p(z | x)) without ever evaluating p(x). Derivation via Jensen's inequality
([[convexity]]) and the EM connection: EM is exact-posterior VI alternating q and θ
([[unsupervised-learning-em-and-mixture-models]]); "variational EM" uses an approximate q.
The ELBO is also a model-selection score (approximate evidence — [[bayesian-inference]])
and a free energy (physics: variational free energy; the Gibbs inequality).
**Reverse vs forward KL**: VI minimizes KL(q ‖ p) — **mode-seeking**/zero-forcing (q avoids
regions where p ≈ 0, so it locks onto one mode and **underestimates variance**); minimizing
KL(p ‖ q) — moment-matching/mass-covering — is what expectation propagation and MLE do.

## Mean field and CAVI (CS228 variational; Bishop ch. 10)
**Mean-field** family: q(z) = Π_j q_j(z_j) (independent factors; or structured mean field
with tractable blocks). Optimizing one factor with the others fixed gives the closed form
**q_j*(z_j) ∝ exp(E_{q_{−j}}[log p(x, z)])** — the expected log-joint under the other factors;
**CAVI** iterates over j (coordinate ascent — monotone in the ELBO, converges to a local
optimum; initialization matters). For **conditionally conjugate** exponential-family models
(each complete conditional is in the exponential family) the update sets q_j's natural
parameter to the expected natural parameter of the complete conditional — closed form for
Gaussian mixtures, LDA, matrix factorization, HMMs (variational Bayes for hidden Markov
models), Bayesian linear regression. **LDA** (Blei, Ng & Jordan 2003): documents as mixtures
of topics, topics as distributions over words; mean-field over topic proportions and
per-word assignments; the archetypal VI showcase and the paper that popularized the method
([[nlp-fundamentals]]). Mean field's independence assumption is the source of its variance
underestimation (posterior correlations are ignored).

## Scaling and generality: SVI and black-box VI (Hoffman et al. 2013; Ranganath et al. 2014; Kingma & Welling 2013)
**Stochastic VI**: for models with global parameters β and per-datum locals zᵢ, sample a
minibatch, optimize locals, take a **natural-gradient** step on β's variational parameters
(natural gradients — the Fisher-metric preconditioning — are free for exponential families:
the gradient in natural parameters is just the expected-sufficient-statistics difference —
[[gradient-descent]]); Robbins–Monro step sizes; LDA on millions of documents. **Black-box
VI**: differentiate the ELBO by Monte Carlo without model-specific derivations
([[monte-carlo-methods]]) — two estimators:
- **Score-function / REINFORCE**: ∇_φ E_{q_φ}[f(z)] = E_{q_φ}[f(z) ∇_φ log q_φ(z)] — works for
  discrete z and any f, high variance (control variates, Rao-Blackwellization needed;
  the same estimator as the policy gradient — [[deep-reinforcement-learning]]).
- **Reparameterization / pathwise**: z = g(ε, φ), ε ~ p(ε) (Gaussian: z = μ + σ ⊙ ε) so
  ∇_φ E[f(z)] = E_ε[∇_φ f(g(ε, φ))] — low variance, needs continuous z and differentiable f;
  Gumbel-softmax/straight-through for discrete relaxations.
Automatic differentiation VI (ADVI in Stan, Pyro/NumPyro `SVI`, TensorFlow Probability)
applies a Gaussian (full or diagonal) q in an unconstrained transformed space to any
differentiable model.

## Amortized inference and richer families (Kingma & Welling 2013; Rezende & Mohamed 2015; Burda et al. 2016)
**Amortization**: instead of per-datum variational parameters, learn an **inference network**
q_φ(z | x) mapping data to variational parameters — one optimization shared across all x,
fast at test time; the **VAE** is exactly amortized reparameterized VI with a neural
likelihood p_θ(x | z) ([[deep-generative-models]]); the **amortization gap** (encoder
suboptimality) and the **approximation gap** (family too small) both lower the bound.
Richer families: **normalizing flows** for the posterior (invertible transforms of a simple
q — planar/radial/IAF flows), mixtures, hierarchical/auxiliary variables, semi-implicit
distributions; **importance-weighted bounds** (IWAE: log of an average of K weights —
tighter as K grows, at the cost of gradient signal to the encoder); **variational
sequential Monte Carlo**; and deep-learning-scale objectives (β-VAE, InfoVAE) that reweight
the KL term for representation learning.

## Other variational methods (K&F ch. 11; Minka 2001; Yedidia et al. 2003)
**Expectation propagation**: approximate each factor by an exponential-family term chosen to
match moments of the tilted distribution — local forward-KL projection; better variance
estimates than mean field, no convergence guarantee (damping); Gaussian process
classification's standard method ([[bayesian-inference]]). **Bethe free energy and loopy BP**:
loopy BP's fixed points are stationary points of the Bethe approximation to the free energy
over locally consistent pseudo-marginals (the local polytope relaxes the **marginal
polytope**) — so message passing on cyclic graphs is variational too; tree-reweighted BP is a
convex version giving an upper bound on log Z ([[probabilistic-graphical-models]]).
Mean-field/Bethe/Kikuchi form a hierarchy of region-based approximations.

## VI vs MCMC (Blei et al. 2017)
| | Variational inference | MCMC ([[monte-carlo-methods]]) |
|---|---|---|
| output | a fitted q; deterministic | samples; asymptotically exact |
| bias | yes (family + reverse KL; variance underestimated) | none asymptotically |
| speed/scale | fast, minibatch-able, GPU-friendly | slower; harder to subsample |
| diagnostics | ELBO convergence (not accuracy); PSIS-based checks | R̂, ESS, trace plots |
| use when | large data, many models to compare, embedded in a neural model | accurate uncertainty matters, model is moderate, multimodality suspected |
Hybrids: variational proposals for MCMC, MCMC refinement of VI, SVGD (particle-based
variational).

## Pitfalls
- Reading mean-field posterior variances as calibrated (they are too small).
- A rising ELBO taken as a good posterior (it measures the bound, not the gap).
- Score-function gradients without variance reduction; reparameterization on discrete
  latents without a relaxation.
- Posterior collapse in VAEs (the KL term wins; the decoder ignores z) — KL annealing,
  free bits, weaker decoders.
- Comparing ELBOs across models with different likelihood parameterizations/data scales.

## Related
- [[unsupervised-learning-em-and-mixture-models]] (EM, ELBO), [[deep-generative-models]]
  (VAEs), [[monte-carlo-methods]] (MCMC, estimators), [[probabilistic-graphical-models]]
  (Bethe, loopy BP), [[bayesian-inference]] (evidence, model comparison),
  [[gradient-descent]] (natural gradients), [[convexity]] (Jensen),
  [[entropy-and-information]] (KL), [[deep-reinforcement-learning]] (REINFORCE),
  [[nlp-fundamentals]] (LDA).

## Sources
Jordan, Ghahramani, Jaakkola & Saul 1999; Blei, Kucukelbir & McAuliffe 2017 (review); Blei, Ng & Jordan 2003 (LDA); Hoffman et al. 2013 (SVI); Ranganath et al. 2014 (BBVI); Kingma & Welling 2013; Rezende & Mohamed 2015 (flows); Burda et al. 2016 (IWAE); Minka 2001 (EP); Yedidia et al. 2003; Kucukelbir et al. 2017 (ADVI); CS228 variational notes (read); Bishop ch. 10.

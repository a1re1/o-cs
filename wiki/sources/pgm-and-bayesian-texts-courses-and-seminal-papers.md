---
title: Probabilistic graphical models and Bayesian methods — Koller & Friedman's PGM, Barber's Bayesian Reasoning and ML (free), Gelman et al.'s Bayesian Data Analysis (free), Rasmussen & Williams' Gaussian Processes for ML (free), MacKay's Information Theory, Inference, and Learning Algorithms (free); Stanford CS228 notes (Ermon), CMU 10-708, MIT 6.438; Pearl 1988, Lauritzen & Spiegelhalter, Jordan et al. variational inference, Blei LDA, Metropolis–Hastings, Geman & Geman Gibbs, Neal HMC, Hoffman & Gelman NUTS
type: source
section: "6.7"
level: 500
tags: [koller-friedman, pgm, barber, bayesian-reasoning-and-machine-learning, gelman, bayesian-data-analysis, bda3, rasmussen-williams, gaussian-processes-for-ml, mackay, information-theory-inference-learning, cs228, ermon, 10-708, 6-438, pearl, lauritzen-spiegelhalter, junction-tree, jordan, variational-inference, blei, lda, metropolis-hastings, geman-geman, gibbs-sampling, neal, hmc, hamiltonian-monte-carlo, hoffman-gelman, nuts, stan]
sources: []
authors: [Daphne Koller, Nir Friedman, David Barber, Andrew Gelman, Carl Rasmussen, Christopher Williams, David MacKay, Stefano Ermon, Judea Pearl, Steffen Lauritzen, David Spiegelhalter, Michael Jordan, David Blei, Nicholas Metropolis, W. K. Hastings, Stuart Geman, Donald Geman, Radford Neal, Matthew Hoffman]
year: 2009
institution: Stanford / CMU / MIT / Cambridge
url: https://ermongroup.github.io/cs228-notes/
license: mixed (CS228 notes, Barber, BDA3, GPML, MacKay free; Koller & Friedman commercial)
format: html
summary: Stanford's CS228 notes (Ermon) give the field's spine in four parts — representation (Bayesian networks and their independencies; Markov random fields, undirected vs directed, CRFs), inference (variable elimination and its complexity; belief propagation and the junction tree, loopy BP; MAP inference by max-sum, graph cuts, LP relaxations, dual decomposition; sampling — forward, rejection, importance, MCMC; variational inference — lower bounds, mean field, the marginal polytope), learning (MLE in directed models; exponential families and gradient learning in undirected models with partition-function estimation; latent variables and EM; Bayesian learning with conjugate priors; structure learning — Chow–Liu, AIC/BIC, Bayesian structure search), and "bringing it together" with the variational autoencoder; Koller & Friedman (2009, 1200 pp) is the exhaustive reference for the same map; Barber and MacKay are the free, readable Bayesian-ML books (MacKay uniquely unites coding theory, inference, and neural nets); Gelman et al.'s BDA is applied Bayesian statistics (hierarchical models, model checking, computation with Stan); Rasmussen & Williams is the Gaussian-process reference; and the seminal papers are Pearl's Bayesian networks and belief propagation (1988), Lauritzen & Spiegelhalter's junction tree (1988), Jordan et al.'s variational methods (1999), Blei's LDA (2003 — the canonical latent-variable model and VI showcase), Metropolis (1953) and Hastings (1970), Geman & Geman's Gibbs sampler (1984), Neal's Hamiltonian Monte Carlo (2011) and Hoffman & Gelman's NUTS (2014) that made HMC automatic in Stan/PyMC.
---
# Probabilistic graphical models and Bayesian methods: sources

## What they are
- **CS228 notes** (Ermon; read): Preliminaries (what is PGM; probability review; applications
  — image denoising, RNA structure, parsing, OCR); **Representation** — Bayesian networks
  (directed graphs, independencies), Markov random fields (undirected vs directed,
  independencies, conditional random fields); **Inference** — variable elimination and
  complexity; belief propagation, junction tree, exact inference in arbitrary graphs,
  loopy BP; MAP inference (max-sum, graph cuts, LP relaxations, dual decomposition);
  sampling (Monte Carlo, forward/rejection/importance sampling, MCMC); variational
  inference (lower bounds, mean field, marginal polytope and relaxations); **Learning** —
  directed models (MLE, learning-theory basics, MLE with missing data), undirected models
  (exponential families, gradient MLE, partition function), latent-variable models (GMMs,
  EM), Bayesian learning (conjugate priors), structure learning (Chow–Liu, AIC/BIC, Bayesian
  structure search); **Together** — the VAE (reparameterization, latent visual
  representations); further reading (structured SVMs, Bayesian nonparametrics).
- **Koller & Friedman, PGM: Principles and Techniques** (2009): representation (BNs, undirected
  models, local structure, template models, Gaussian networks, exponential family),
  inference (variable elimination, clique trees, loopy/variational, MAP, particle-based,
  hybrid/continuous, temporal), learning (parameter learning, structure learning, partially
  observed data, undirected learning), and decision making (utilities, influence diagrams).
- **Barber, BRML** (free): graphical models, inference, learning, approximate inference,
  with MATLAB demos. **MacKay, ITILA** (free): information theory ↔ inference — Bayesian
  model comparison, Occam factors, Monte Carlo (ch. 29–30: MH, Gibbs, slice, HMC, exact
  sampling), variational methods, neural nets as Bayesian models, error-correcting codes as
  graphical models (LDPC decoding = loopy BP). **Gelman et al., BDA3** (free): single/multi-
  parameter models, hierarchical models, model checking (posterior predictive checks),
  evaluation/comparison (WAIC, LOO), computation (MCMC, HMC), regression, nonlinear and
  nonparametric models, missing data; the **Bayesian workflow**. **Rasmussen & Williams,
  GPML** (free): GP regression and classification, covariance functions, model selection,
  approximations. Courses: CMU 10-708 (Xing/Kolter), MIT 6.438 (Willsky/Wornell — algorithms
  for inference).
- **Seminal**: Pearl 1988 (BNs, d-separation, belief propagation on polytrees — Turing Award
  2011); Lauritzen & Spiegelhalter 1988 (junction tree — exact inference by moralization,
  triangulation, clique-tree propagation); Jordan, Ghahramani, Jaakkola & Saul 1999
  (variational inference as optimization over a tractable family); Blei, Ng & Jordan 2003
  (**LDA**: topic models; mean-field VI; later stochastic VI for millions of documents);
  Metropolis et al. 1953 and Hastings 1970 (MCMC with a proposal + accept/reject);
  Geman & Geman 1984 (Gibbs sampling for image restoration, simulated annealing on MRFs);
  Neal 2011 (HMC — Hamiltonian dynamics proposals, gradient-informed, high acceptance in
  high dimensions); Hoffman & Gelman 2014 (**NUTS** — adaptive trajectory length; the Stan
  default); Kingma & Welling 2013 (VAE — amortized VI with neural nets).

## Key ideas → pages
[[probabilistic-graphical-models]], [[monte-carlo-methods]], [[variational-inference]],
[[bayesian-inference]], [[causal-inference]]; introductory versions in
[[bayesian-networks-and-hmms]] and [[unsupervised-learning-em-and-mixture-models]].

## What they add
CS228 for the map in 20 pages of notes; Koller & Friedman when a detail is needed; MacKay
for the unifying view that coding, inference, and learning are one subject; BDA for how
statisticians actually do it (priors, checks, workflow); the paper list shows inference
oscillating between exact (junction tree), sampling (MCMC → HMC/NUTS), and optimization
(VI → VAEs) as the model sizes and compute changed.

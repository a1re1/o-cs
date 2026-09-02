---
title: Unsupervised learning — mixture of Gaussians and the EM algorithm (E-step responsibilities, M-step MLE, Jensen's inequality and the ELBO, convergence, k-means as hard EM), variational inference and the VAE connection, PCA and ICA as latent-variable models, density estimation and anomaly detection, and hierarchical/spectral clustering
type: concept
section: "6.2"
level: 400
tags: [unsupervised-learning, clustering, mixture-models, gaussian-mixture, gmm, em, expectation-maximization, e-step, m-step, responsibilities, latent-variables, jensens-inequality, elbo, evidence-lower-bound, coordinate-ascent, local-optima, k-means, hard-em, variational-inference, vae, pca, ica, independent-components, cocktail-party, factor-analysis, density-estimation, kernel-density, anomaly-detection, hierarchical-clustering, agglomerative, dendrogram, spectral-clustering, dbscan, silhouette, model-selection-bic, dempster-laird-rubin]
sources: [ml-courses-texts-and-seminal-papers]
summary: Unsupervised learning finds structure in unlabeled data, and the workhorse for the probabilistic kind is the latent-variable model fitted by EM: a mixture of Gaussians says each point comes from one of k Gaussians chosen with probability φⱼ, the latent assignment z is unobserved, the log-likelihood log Σ_z p(x, z) has no closed-form maximizer, and EM alternates an E-step (compute responsibilities w⁽ⁱ⁾ⱼ = p(z = j | x⁽ⁱ⁾) under current parameters) with an M-step (maximize the expected complete-data log-likelihood — weighted MLE: means, covariances, mixing weights as responsibility-weighted averages); Jensen's inequality shows each iteration maximizes a lower bound (the ELBO) on the log-likelihood that is tight at the current parameters, so the likelihood never decreases and EM is coordinate ascent on the ELBO over (distribution q, parameters θ) — converging to a local optimum that depends on initialization (k-means is the hard-assignment, spherical-covariance limit); when the E-step posterior is intractable, restrict q to a family and optimize the ELBO variationally, which with a neural encoder/decoder and the reparameterization trick is the variational autoencoder; PCA is the linear-Gaussian latent model (maximum-variance projection), ICA finds statistically independent non-Gaussian sources (the cocktail-party problem — unmixing by maximizing non-Gaussianity, ambiguous up to permutation and scale, impossible for Gaussian sources), and hierarchical, spectral, and density-based clustering plus kernel density estimation and reconstruction-error anomaly detection round out the toolkit, with silhouette scores and BIC for choosing k.
---
# Unsupervised learning: EM, mixture models, and latent variables

**In one sentence.** Explain the data with hidden variables, then alternate between
inferring the hidden variables given the parameters (E) and fitting the parameters given
the hidden variables (M) — each step raises a lower bound on the likelihood, and every
clustering, factor, and generative model from k-means to VAEs is a variant of that loop.

## Mixture of Gaussians (CS229 ch. 11; Bishop ch. 9)
Model: z⁽ⁱ⁾ ~ Multinomial(φ), x⁽ⁱ⁾ | z = j ~ N(μⱼ, Σⱼ). If z were observed, MLE is trivial:
φⱼ = fraction of points with z = j; μⱼ, Σⱼ = sample mean/covariance of those points (like
Gaussian discriminant analysis with labels — [[linear-models-logistic-regression-and-glms]]).
With z hidden, the log-likelihood ℓ(θ) = Σᵢ log Σⱼ p(x⁽ⁱ⁾ | z = j) p(z = j) has a sum inside the
log — no closed form. **EM**: repeat — **E-step**: for each i, j compute the **responsibility**
w⁽ⁱ⁾ⱼ = p(z⁽ⁱ⁾ = j | x⁽ⁱ⁾; θ) ∝ φⱼ N(x⁽ⁱ⁾; μⱼ, Σⱼ) (soft assignment via Bayes' rule —
[[bayes-theorem-and-inference]]); **M-step**: φⱼ = (1/n) Σᵢ w⁽ⁱ⁾ⱼ, μⱼ = Σᵢ w⁽ⁱ⁾ⱼ x⁽ⁱ⁾ / Σᵢ w⁽ⁱ⁾ⱼ, Σⱼ =
responsibility-weighted covariance — the labeled MLE with fractional counts. **k-means** is
the limit: hard assignments (w ∈ {0, 1}), shared spherical covariance σ² → 0 ("hard EM";
[[k-means-clustering]]). GMMs give soft clusters, per-cluster shape, a **density** p(x) (for
anomaly scoring — low-density points), and a generative model to sample from. Degeneracies:
a component collapsing on one point (Σ → 0, likelihood → ∞) — regularize covariances or use
MAP; label switching; choose k by held-out likelihood, **BIC**, or the Dirichlet-process
prior ([[bayesian-inference]]).

## Why EM works: Jensen and the ELBO (CS229 ch. 11.2–11.3; Dempster, Laird & Rubin 1977)
For any distribution qᵢ over z: log p(x⁽ⁱ⁾; θ) = log Σ_z qᵢ(z) · p(x⁽ⁱ⁾, z; θ)/qᵢ(z) ≥ Σ_z qᵢ(z)
log [p(x⁽ⁱ⁾, z; θ)/qᵢ(z)] by **Jensen's inequality** (log is concave; [[convexity]]) — the
**evidence lower bound (ELBO)** = E_q[log p(x, z; θ)] − E_q[log q(z)] = log p(x; θ) −
KL(q ‖ p(z | x; θ)) ([[entropy-and-information]]). Equality iff qᵢ(z) = p(z | x⁽ⁱ⁾; θ) — the
posterior. **EM = coordinate ascent on the ELBO**: E-step sets q to the posterior (bound
tight at current θ); M-step maximizes the bound over θ (the expected complete-data
log-likelihood plus q's entropy, which is constant in θ). Hence ℓ(θ⁽ᵗ⁺¹⁾) ≥ ELBO(q⁽ᵗ⁾, θ⁽ᵗ⁺¹⁾) ≥
ELBO(q⁽ᵗ⁾, θ⁽ᵗ⁾) = ℓ(θ⁽ᵗ⁾): **monotone** convergence to a stationary point (local optimum —
initialize from k-means, run several restarts). Generalized EM (partial M-steps), MAP-EM,
Monte Carlo EM (sample z), and online/stochastic EM. EM is the pattern behind Baum–Welch for
HMMs, mixture-of-experts, missing-data imputation, and topic models ([[bayesian-networks-and-hmms]],
[[probabilistic-graphical-models]]).

## Variational inference and VAEs (CS229 ch. 11.5)
When p(z | x; θ) is intractable (continuous z, neural likelihoods), restrict q to a family
(mean-field factorization, or q_φ(z | x) = N(μ_φ(x), σ_φ(x)) parameterized by an encoder
network) and **maximize the ELBO over both φ and θ** by gradient ascent — approximate
posterior inference as optimization. The **variational autoencoder** (Kingma & Welling 2013):
decoder p_θ(x | z), encoder q_φ(z | x), ELBO = E_q[log p_θ(x | z)] − KL(q_φ(z | x) ‖ p(z)) —
reconstruction minus a regularizer pulling the code toward the prior; the **reparameterization
trick** (z = μ + σ ⊙ ε, ε ~ N(0, I)) makes the expectation differentiable in φ for SGD
([[deep-generative-models]]). Diffusion models are the same ELBO on a chain of latent
noising steps (CS229 ch. 14).

## PCA and ICA as latent-variable models (CS229 ch. 12–13)
**PCA**: project onto the top-k eigenvectors of the (standardized) covariance — maximum
variance / minimum reconstruction error; **probabilistic PCA / factor analysis** is the linear-
Gaussian latent model x = Λz + μ + ε fit by EM; used for compression, visualization,
denoising, decorrelating features before other learners; mechanics in [[svd-and-pca]].
**ICA**: observed x = As with **independent, non-Gaussian** sources s (the cocktail-party
problem: n microphones, n speakers); recover W = A⁻¹ by maximizing non-Gaussianity /
likelihood under a non-Gaussian source density (sigmoid CDF in CS229's derivation; FastICA
uses kurtosis/negentropy — [[entropy-and-information]]); **ambiguities**: permutation and
scaling of sources are unidentifiable, and Gaussian sources cannot be separated at all
(rotational symmetry) — non-Gaussianity is the identifying assumption; used for EEG/fMRI
artifact removal and blind source separation. Nonlinear dimensionality reduction (t-SNE,
UMAP, autoencoders) for visualization — with the caveat that t-SNE distances/cluster sizes
are not meaningful.

## Other clustering and density tools
**Hierarchical/agglomerative clustering**: merge closest clusters (single/complete/average/
Ward linkage — [[minimum-spanning-trees]] for single linkage), read clusters off the
**dendrogram** at any level; O(n² log n). **Spectral clustering**: k-means on the top
eigenvectors of the graph Laplacian of a similarity graph — finds non-convex clusters
(normalized cut — [[graph-theory-basics]]). **DBSCAN**: density-reachability with (ε, minPts) —
arbitrary shapes, noise labels, no k. Evaluation without labels: **silhouette** score,
Davies–Bouldin, stability across resamples; with labels: adjusted Rand index / NMI.
**Density estimation**: histograms, **kernel density estimation** (bandwidth by CV), GMMs;
**anomaly detection**: low density, isolation forests, reconstruction error of a PCA/
autoencoder, one-class SVMs ([[kernels-and-support-vector-machines]]).

## Pitfalls
- Running EM once from a random start and reporting the result (local optima).
- Singular covariance collapse in GMMs without regularization.
- Choosing k by training likelihood (always increases) — use BIC/held-out/silhouette.
- Applying PCA without standardizing (variance dominated by units).
- ICA on Gaussian data; interpreting t-SNE geometry literally.

## Related
- [[k-means-clustering]], [[svd-and-pca]], [[maximum-likelihood-estimation]],
  [[bayes-theorem-and-inference]], [[convexity]], [[entropy-and-information]],
  [[bayesian-networks-and-hmms]], [[probabilistic-graphical-models]], [[bayesian-inference]],
  [[deep-generative-models]], [[linear-models-logistic-regression-and-glms]],
  [[minimum-spanning-trees]], [[graph-theory-basics]], [[machine-learning-basics]].

## Sources
CS229 notes ch. 10–13 (ToC read); Dempster, Laird & Rubin 1977; Bishop ch. 9–10, 12; Kingma & Welling 2013; ESL ch. 14; Hyvärinen & Oja 2000 (ICA); von Luxburg 2007 (spectral clustering tutorial).

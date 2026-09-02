---
title: Bayesian inference and modelling — priors, likelihoods, posteriors and posterior predictive distributions, conjugate families (Beta–Binomial, Gamma–Poisson, Normal–Normal, Dirichlet–Multinomial), MAP vs full posterior, hierarchical models and partial pooling, Bayesian model comparison (marginal likelihood, Bayes factors, Occam's razor, WAIC/LOO), the Bayesian workflow (prior predictive checks, posterior predictive checks, calibration), Gaussian processes, Bayesian optimization, probabilistic programming (Stan, PyMC), and the frequentist–Bayesian relationship
type: concept
section: "6.7"
level: 500
tags: [bayesian-inference, bayes-rule, prior, likelihood, posterior, posterior-predictive, conjugate-priors, beta-binomial, gamma-poisson, normal-normal, dirichlet-multinomial, laplace-smoothing, map, credible-interval, hierarchical-models, partial-pooling, shrinkage, empirical-bayes, model-comparison, marginal-likelihood, evidence, bayes-factor, occam-razor, bic, waic, loo, cross-validation, bayesian-workflow, prior-predictive-check, posterior-predictive-check, calibration, sensitivity-analysis, gaussian-processes, kernel, gp-regression, bayesian-optimization, acquisition-function, probabilistic-programming, stan, pymc, numpyro, bayesian-neural-networks, uncertainty, frequentist-vs-bayesian, bernstein-von-mises, gelman, mackay]
sources: [pgm-and-bayesian-texts-courses-and-seminal-papers]
summary: Bayesian inference treats unknowns as random variables — posterior ∝ likelihood × prior — and answers every question by integrating over the posterior: point estimates (MAP, posterior mean), credible intervals, and the posterior predictive p(x_new | data) = ∫ p(x_new | θ) p(θ | data) dθ that accounts for parameter uncertainty; conjugate prior–likelihood pairs give closed-form posteriors whose hyperparameters read as pseudo-counts (Beta–Binomial: Laplace smoothing is a Beta(1,1) prior; Gamma–Poisson; Normal–Normal; Dirichlet–Multinomial), everything else needs MCMC or variational inference; hierarchical models share strength across groups by putting a prior on group-level parameters (partial pooling shrinks noisy estimates toward the population — the eight-schools example — with empirical Bayes as the plug-in shortcut); model comparison uses the marginal likelihood p(data | model), which automatically penalizes complexity (the Bayesian Occam's razor and Occam factor; Bayes factors; BIC as its asymptotic approximation) but is prior-sensitive, so predictive criteria (WAIC, PSIS-LOO cross-validation) are preferred in practice; the Bayesian workflow (Gelman et al.) is iterative — prior predictive checks, fitting, posterior predictive checks, calibration/simulation-based validation, sensitivity to priors, model expansion; Gaussian processes are the nonparametric Bayesian regression whose kernel encodes prior beliefs about functions with closed-form posteriors (O(n³)) and drive Bayesian optimization of expensive black-box functions; probabilistic programming languages (Stan, PyMC, NumPyro, Pyro) make the model the code and automate NUTS/VI; and the frequentist relationship is that posteriors concentrate at the MLE with the same asymptotics (Bernstein–von Mises), priors act as regularizers (MAP = penalized likelihood), and calibration is where the two philosophies meet.
---
# Bayesian inference and modelling

**In one sentence.** Put a distribution on everything you don't know, condition on what you
observe, and answer questions by averaging over what remains uncertain — the machinery is
Bayes' rule, the art is the prior and the model, and the discipline is checking the model
the way you'd check code.

## The core (Gelman et al. BDA3 ch. 1–2; MacKay ch. 2–3; [[bayes-theorem-and-inference]])
p(θ | D) = p(D | θ) p(θ) / p(D), p(D) = ∫ p(D | θ) p(θ) dθ (the **evidence/marginal likelihood**).
Outputs: the whole posterior; summaries — posterior mean/median, **MAP** (mode — the
penalized-likelihood estimate; [[maximum-likelihood-estimation]]), **credible intervals**
(95 % of posterior mass — the statement frequentist confidence intervals are mistaken for —
[[hypothesis-testing-and-confidence-intervals]]); decisions by expected loss ([[markov-decision-processes]]
utility). **Posterior predictive**: p(x̃ | D) = ∫ p(x̃ | θ) p(θ | D) dθ — predictions that
integrate out parameter uncertainty, wider than plug-in predictions, the honest object for
forecasting. **Priors**: informative (domain knowledge, previous studies), weakly informative
(regularizing scale — the recommended default), "non-informative"/flat or Jeffreys
(invariance-based; improper priors can give improper posteriors), hierarchical (priors
with their own priors); the prior matters when data are few and washes out as n grows.

## Conjugacy: closed-form posteriors (BDA3 ch. 2; Bishop ch. 2)
| Likelihood | Conjugate prior | Posterior update | Reading |
|---|---|---|---|
| Binomial/Bernoulli(θ) | Beta(α, β) | Beta(α + heads, β + tails) | α, β = pseudo-counts; Beta(1,1) → Laplace smoothing; posterior mean (α+h)/(α+β+n) |
| Poisson(λ) | Gamma(a, b) | Gamma(a + Σx, b + n) | rate with a pseudo-observations |
| Normal(μ, σ² known) | Normal(μ₀, τ²) | precision-weighted mean; precisions add | shrinkage toward μ₀ by 1/τ² vs n/σ² |
| Normal (μ, σ² both) | Normal-Inverse-Gamma / Normal-Inverse-Wishart | closed form | t-distributed predictive |
| Multinomial | Dirichlet(α) | Dirichlet(α + counts) | naive Bayes smoothing, LDA |
| Linear regression (Gaussian noise) | Gaussian on weights | Gaussian; ridge = MAP | [[linear-models-logistic-regression-and-glms]] |
The exponential family always has a conjugate prior; sequential updating = batch updating
(the posterior is the next prior — online learning). Beyond conjugacy: MCMC
([[monte-carlo-methods]]), variational inference ([[variational-inference]]), Laplace
approximation (Gaussian at the MAP with the Hessian — [[derivatives-and-gradients]]),
integrated nested Laplace (INLA).

## Hierarchical models and partial pooling (BDA3 ch. 5; Gelman & Hill)
Groups j = 1..J (schools, users, hospitals) with parameters θⱼ ~ p(θ | φ), φ ~ p(φ):
**complete pooling** (one θ) ignores group differences, **no pooling** (independent θⱼ)
overfits small groups, **partial pooling** shrinks each θⱼ toward the population mean by an
amount learned from the data (the between-group variance) — the **eight-schools** model
(treatment effects with standard errors, posterior shrinkage toward the mean); random-
effects/mixed models are the frequentist cousin; **empirical Bayes** estimates φ by maximizing
the marginal likelihood then plugs it in (James–Stein shrinkage as a special case;
[[generalization-bias-variance-and-regularization]] — shrinkage is variance reduction).
Computation: HMC with the **non-centred parameterization** (θⱼ = μ + τ ηⱼ) to avoid the
funnel geometry. Everywhere in practice: A/B testing across segments, multilevel
regression and post-stratification, recommender systems (user/item priors), topic models.

## Model comparison and the Bayesian Occam's razor (MacKay ch. 28; BDA3 ch. 7)
p(D | M) = ∫ p(D | θ, M) p(θ | M) dθ: a complex model spreads its prior predictive mass over
many possible datasets and so assigns less to any particular one — the **Occam factor**
(evidence ≈ best-fit likelihood × (posterior width / prior width)); **Bayes factors** p(D | M₁)/
p(D | M₂) compare models without a test set and penalize complexity automatically, but are
extremely **prior-sensitive** (Lindley/Jeffreys paradox: a diffuse prior can favour the null
arbitrarily) and hard to compute (bridge sampling, nested sampling, thermodynamic
integration; **BIC** = −2 log L + k log n is the large-n approximation — [[kolmogorov-complexity]]
for the MDL reading). Preferred in practice: **predictive** criteria — **WAIC** (Watanabe:
log pointwise predictive density minus an effective-parameter penalty) and **PSIS-LOO**
(leave-one-out CV computed from posterior draws with Pareto-smoothed importance weights),
both estimating out-of-sample predictive accuracy ([[machine-learning-basics]] cross-
validation with a Bayesian face); model averaging/stacking over models.

## The Bayesian workflow (Gelman et al. 2020; BDA3 ch. 6)
1. Write the generative model; 2. **prior predictive check** — simulate data from the prior;
does it look plausible? (catches priors that allow absurd scales); 3. fit (NUTS/VI); check
computation (R̂, ESS, divergences — [[monte-carlo-methods]]); 4. **posterior predictive
check** — simulate replicated data from the posterior, compare test statistics to the
observed (misfit in tails, overdispersion, zeros); 5. **calibration / simulation-based
calibration** — fit to data simulated from the model with known parameters; posteriors
should cover the truth at nominal rates; 6. sensitivity analysis to priors and likelihood;
7. compare/expand models (LOO); 8. report with uncertainty. The workflow is what separates
"Bayesian" from "I put a prior on it".

## Gaussian processes and Bayesian optimization (Rasmussen & Williams; Snoek et al. 2012)
A **GP** is a prior over functions: f ~ GP(m, k) — any finite set of function values is jointly
Gaussian with covariance k(x, x′); the kernel encodes smoothness, periodicity, scale
([[kernels-and-support-vector-machines]]: GP regression = kernel ridge regression plus
uncertainty). With Gaussian noise the posterior is closed form: mean K*(K + σ²I)⁻¹y and
variance K** − K*(K + σ²I)⁻¹K*ᵀ — O(n³), hence sparse/inducing-point and structured
approximations for n > 10⁴; hyperparameters by maximizing the marginal likelihood (an
Occam-razor model selection in closed form); classification needs Laplace/EP/VI. Uses:
small-data regression with calibrated uncertainty, spatial statistics (kriging), surrogate
models, and **Bayesian optimization**: fit a GP to expensive black-box evaluations (hyper-
parameter tuning, experiment design, chemistry), choose the next point by an **acquisition
function** (expected improvement, UCB, Thompson sampling — [[multi-armed-bandits]] in
continuous space), repeat — sample-efficient where random/grid search is not
([[neural-network-training]]). The infinite-width neural network is a GP (Neal 1996) — the
NTK story of [[statistical-learning-theory]].

## Probabilistic programming and Bayesian deep learning
**Stan** (HMC/NUTS, ADVI; the reference implementation), **PyMC**, **NumPyro/Pyro** (JAX/
PyTorch; SVI at scale), Turing.jl, Edward/TFP: write the joint density as a program, get
inference automatically; models are checked, compared, and reused as code
([[probabilistic-graphical-models]] as software). **Bayesian neural networks**: posteriors
over weights via VI (Bayes by Backprop), MC dropout, deep ensembles (the pragmatic
winner), Laplace approximations, SWAG — for calibrated uncertainty and out-of-distribution
detection ([[deep-learning-basics]], [[ai-safety-and-alignment]]); the prior over functions
implied by weight priors is poorly understood; conformal prediction is the distribution-
free alternative for calibrated intervals.

## Frequentist and Bayesian (Wasserman; Efron)
Same likelihood, different questions: frequentists fix θ and consider repeated samples
(coverage, p-values, unbiasedness — [[hypothesis-testing-and-confidence-intervals]]);
Bayesians fix the data and consider the posterior. Connections: **Bernstein–von Mises** —
for large n the posterior is approximately Normal(θ̂_MLE, I⁻¹/n), so credible and confidence
intervals coincide asymptotically; MAP = regularized MLE (ridge ↔ Gaussian prior, lasso ↔
Laplace); empirical Bayes ↔ shrinkage estimators; **calibration** (do 90 % intervals contain
the truth 90 % of the time?) is a frequentist property Bayesians should check. Bayesian
advantages: small data, hierarchical structure, decision-theoretic coherence, propagation
of uncertainty; costs: computation, prior specification, model-comparison sensitivity.

## Pitfalls
- Flat priors on scale parameters (improper posteriors; absurd prior predictives).
- Reporting MAP and calling it Bayesian; ignoring the posterior predictive.
- Bayes factors with vague priors (Lindley paradox); comparing WAIC across different data.
- Centred parameterization in hierarchical models (divergences); trusting a fit without
  posterior predictive checks.
- GPs with an unscaled kernel or fixed hyperparameters; Bayesian optimization on
  high-dimensional or noisy objectives without a matching kernel/noise model.

## Related
- [[bayes-theorem-and-inference]], [[maximum-likelihood-estimation]],
  [[hypothesis-testing-and-confidence-intervals]], [[monte-carlo-methods]],
  [[variational-inference]], [[probabilistic-graphical-models]],
  [[bayesian-networks-and-hmms]], [[kernels-and-support-vector-machines]],
  [[multi-armed-bandits]], [[generalization-bias-variance-and-regularization]],
  [[kolmogorov-complexity]], [[statistical-learning-theory]], [[neural-network-training]],
  [[probability-and-statistics-for-cs]].

## Sources
Gelman et al., BDA3 ch. 1–7, 10–12; Gelman et al. 2020 ("Bayesian workflow"); MacKay ch. 2–3, 28; Rasmussen & Williams 2006; Bishop ch. 2–3, 6; Snoek et al. 2012; Watanabe 2010 (WAIC); Vehtari, Gelman & Gabry 2017 (LOO); Neal 1996; CS228 Bayesian-learning notes (read); Wasserman, *All of Statistics*.

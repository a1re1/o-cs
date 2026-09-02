---
title: Linear models for regression and classification — least squares (LMS/gradient descent, normal equations, probabilistic interpretation), locally weighted regression, logistic regression and the perceptron, softmax, Newton's method, generalized linear models and the exponential family, generative vs discriminative classifiers (Gaussian discriminant analysis, naive Bayes)
type: concept
section: "6.2"
level: 300
tags: [linear-regression, least-squares, lms, widrow-hoff, normal-equations, gradient-descent, stochastic-gradient-descent, probabilistic-interpretation, gaussian-noise, locally-weighted-regression, logistic-regression, sigmoid, log-loss, cross-entropy, perceptron, softmax, multinomial-logistic, newtons-method, fisher-scoring, irls, glm, generalized-linear-model, exponential-family, canonical-link, poisson-regression, generative, discriminative, gaussian-discriminant-analysis, gda, lda, naive-bayes, laplace-smoothing, feature-maps, polynomial-regression, ridge, lasso, elastic-net]
sources: [ml-courses-texts-and-seminal-papers]
summary: Linear regression fits h(x) = θᵀx by minimizing squared error — solved by gradient descent (the LMS/Widrow–Hoff update θ ← θ + α(y − θᵀx)x, batch or stochastic), or in closed form by the normal equations θ = (XᵀX)⁻¹Xᵀy — and is maximum likelihood under Gaussian noise (the probabilistic interpretation that justifies squared loss); locally weighted regression fits a separate model per query with distance-based weights (non-parametric); logistic regression models P(y=1|x) = σ(θᵀx), maximizes the log-likelihood (equivalently minimizes cross-entropy), has the same-looking gradient update, is convex, and extends to softmax for k classes and to Newton's method/IRLS for fast convergence; both are generalized linear models — choose an exponential-family distribution for y (Gaussian, Bernoulli, multinomial, Poisson), let its natural parameter be θᵀx, and the canonical link and the update rule follow automatically; generative classifiers model P(x|y) and P(y) instead (Gaussian discriminant analysis with shared covariance yields a linear boundary and implies logistic form — but not conversely; naive Bayes assumes conditionally independent features with Laplace smoothing, and works surprisingly well for text) and trade stronger assumptions for data efficiency, while discriminative models are more robust when the assumptions are wrong; feature maps (polynomials, splines, basis functions) make linear models nonlinear in x, and ridge/lasso/elastic-net penalties control the resulting variance.
---
# Linear models: regression, logistic regression, GLMs, generative classifiers

**In one sentence.** Nearly every classical learner is "a linear function of features fed
through the right exponential-family likelihood": Gaussian gives least squares, Bernoulli
gives logistic regression, multinomial gives softmax, and Newton or gradient descent on the
convex log-likelihood fits them all.

## Linear regression (CS229 ch. 1)
h_θ(x) = θᵀx (x₀ = 1 for the intercept). Cost J(θ) = ½ Σ (h(x⁽ⁱ⁾) − y⁽ⁱ⁾)². **Gradient descent**
θⱼ ← θⱼ − α Σᵢ (h(x⁽ⁱ⁾) − y⁽ⁱ⁾) xⱼ⁽ⁱ⁾ — the **LMS / Widrow–Hoff** rule; batch vs **stochastic** GD
(one example per step; noisy but scales to huge n; minibatches in practice —
[[gradient-descent]]); J is convex so GD finds the global minimum. **Normal equations**:
∇J = XᵀXθ − Xᵀy = 0 → θ = (XᵀX)⁻¹Xᵀy — O(d³) (use QR/Cholesky, never invert explicitly;
[[gaussian-elimination-lu]], [[svd-and-pca]] pseudoinverse when XᵀX is singular). Choose GD
when d is large (millions of features) and the normal equations when d ≲ 10⁴. **Probabilistic
interpretation**: y = θᵀx + ε, ε ~ N(0, σ²) → the likelihood is maximized exactly by least
squares ([[maximum-likelihood-estimation]]) — squared loss is Gaussian-noise MLE, absolute
loss is Laplace-noise MLE (robust regression), and σ² doesn't affect θ̂. **Locally weighted
linear regression**: at query x, weight examples w⁽ⁱ⁾ = exp(−(x⁽ⁱ⁾ − x)²/2τ²) and solve
weighted least squares — non-parametric (keeps the training set), bandwidth τ controls
bias/variance; the ancestor of kernel smoothing and of attention's weighted averaging
([[transformers-and-attention]]).

## Classification: logistic regression, perceptron, softmax (CS229 ch. 2)
Regression on 0/1 labels is wrong (unbounded outputs, outliers drag the line). **Logistic
regression**: h(x) = σ(θᵀx) = 1/(1 + e^{−θᵀx}) interpreted as P(y = 1 | x); σ' = σ(1 − σ).
Log-likelihood ℓ(θ) = Σ y log h + (1 − y) log(1 − h) (negative = **cross-entropy / log loss**);
concave; gradient ascent gives θⱼ ← θⱼ + α (y − h(x)) xⱼ — the *same form* as LMS with a
different h (not a coincidence: both are GLMs). Decision boundary θᵀx = 0 is linear in x
(nonlinear via feature maps). Separable data → weights diverge (add regularization).
**Perceptron**: h = 1[θᵀx ≥ 0], same update — converges in finite steps if linearly separable
(Novikoff: ≤ (R/γ)² mistakes), no probabilistic interpretation, the 1958 ancestor of neural
networks ([[deep-learning-basics]]). **Multiclass**: **softmax** P(y = k | x) = e^{θₖᵀx}/Σⱼ e^{θⱼᵀx},
cross-entropy loss, gradient (1[y = k] − P(k | x)) x; one-vs-rest as the alternative.
**Newton's method**: θ ← θ − H⁻¹∇ℓ — quadratic convergence (a dozen iterations) at O(d³) per
step; for logistic regression it is **IRLS** (iteratively reweighted least squares) / Fisher
scoring — [[gradient-descent]] (second-order methods, L-BFGS as the scalable version).

## Generalized linear models (CS229 ch. 3)
The **exponential family**: p(y; η) = b(y) exp(ηᵀT(y) − a(η)) — Bernoulli (η = log φ/(1−φ), so
φ = σ(η): the sigmoid is *derived*), Gaussian, multinomial, Poisson, gamma, Dirichlet, … ;
a(η) is the log-partition function whose derivatives give mean and variance. **GLM
construction**: (1) y | x; θ ~ ExpFamily(η); (2) predict E[T(y) | x]; (3) η = θᵀx (linear in
x). Then the **canonical response** g(η) = E[y; η] follows: identity (OLS), sigmoid (logistic),
softmax (multinomial), exp (**Poisson regression** for counts); the gradient update is always
θ ← θ + α (y − h(x)) x, and the log-likelihood is concave in θ. Link functions, deviance,
overdispersion (negative binomial), and mixed models are the statistics extensions (ESL ch. 4;
[[hypothesis-testing-and-confidence-intervals]] for coefficient inference).

## Generative learning algorithms (CS229 ch. 4)
**Discriminative** models learn P(y | x) (or a boundary) directly; **generative** models learn
P(x | y) and P(y) and classify by Bayes' rule ([[bayes-theorem-and-inference]]).
- **Gaussian discriminant analysis (GDA)**: x | y ~ N(μ_y, Σ) with shared Σ — MLE gives class
  means and pooled covariance; the posterior P(y = 1 | x) is exactly a logistic function of
  x (linear boundary — LDA); with per-class Σ_y the boundary is quadratic (QDA). GDA ⇒
  logistic form but not conversely (Poisson class-conditionals also give logistic
  posteriors), so logistic regression is the weaker, more robust assumption; GDA is more
  data-efficient when the Gaussian assumption holds (asymptotically better with fewer
  samples — Ng & Jordan 2002).
- **Naive Bayes**: discrete features assumed conditionally independent given y — P(x | y) =
  Π P(xⱼ | y); parameters are counts; **Laplace smoothing** (add one to every count) avoids
  zero probabilities for unseen words; Bernoulli vs **multinomial event models** for text
  (word counts); classification is a sum of log-odds — linear in the feature vector, so naive
  Bayes is a linear classifier too, trained by counting: the standard baseline for spam and
  document classification ([[nlp-fundamentals]]); the smallest [[bayesian-networks-and-hmms]].

## Nonlinear features and regularization
**Feature maps** φ(x): polynomials, splines/basis functions, radial basis functions, interaction
terms — linear in θ, nonlinear in x; too rich a map overfits → **ridge** (L2: θ = (XᵀX +
λI)⁻¹Xᵀy — shrinks, always invertible, Gaussian prior MAP), **lasso** (L1: sparse θ, feature
selection, Laplace prior; solved by coordinate descent/LARS — Tibshirani 1996), **elastic
net** (both); λ by cross-validation ([[generalization-bias-variance-and-regularization]]).
Implicit feature maps of infinite dimension → [[kernels-and-support-vector-machines]].

## Pitfalls
- Regressing on unscaled features with GD (slow, zig-zag) — standardize.
- Interpreting logistic coefficients without accounting for correlated features; reading
  significance off a regularized model.
- Perfect separation in logistic regression (infinite weights) — regularize.
- Naive Bayes probabilities are badly calibrated (independence violated) even when its
  classifications are good.
- Using accuracy on the training set of a GLM as evidence of fit; not checking residuals.

## Related
- [[gradient-descent]], [[convexity]], [[maximum-likelihood-estimation]],
  [[gaussian-elimination-lu]], [[svd-and-pca]], [[bayes-theorem-and-inference]],
  [[bayesian-networks-and-hmms]], [[kernels-and-support-vector-machines]],
  [[generalization-bias-variance-and-regularization]], [[deep-learning-basics]],
  [[hypothesis-testing-and-confidence-intervals]], [[nlp-fundamentals]].

## Sources
CS229 notes ch. 1–4 (ToC read); ISLR ch. 3–4, 6; ESL ch. 3–4; Bishop ch. 3–4; Ng & Jordan 2002; Tibshirani 1996; Rosenblatt 1958 / Novikoff 1962 (perceptron).

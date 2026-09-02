---
title: Kernels and support vector machines — feature maps and the kernel trick, Mercer kernels (polynomial, RBF/Gaussian, string), the representer theorem, maximum-margin classification, Lagrange duality and support vectors, soft margins and the hinge loss, SMO, kernel ridge regression and Gaussian processes, and when kernels lose to trees and neural networks
type: concept
section: "6.2"
level: 400
tags: [kernels, kernel-trick, feature-map, mercer, positive-semidefinite, gram-matrix, polynomial-kernel, rbf-kernel, gaussian-kernel, string-kernel, representer-theorem, rkhs, svm, support-vector-machine, maximum-margin, functional-margin, geometric-margin, lagrange-duality, kkt, dual, support-vectors, soft-margin, slack, hinge-loss, regularization, c-parameter, smo, coordinate-ascent, kernel-ridge-regression, gaussian-processes, kernel-pca, libsvm, liblinear, scaling, cortes-vapnik]
sources: [ml-courses-texts-and-seminal-papers]
summary: A feature map φ(x) can make a linear learner nonlinear, and the kernel trick lets you use φ of enormous or infinite dimension without ever computing it: any algorithm that touches data only through inner products (LMS with features, ridge, perceptron, PCA, SVMs) can replace ⟨φ(x), φ(z)⟩ with a kernel K(x, z) — valid (Mercer) iff every Gram matrix is positive semidefinite — such as polynomial (1 + xᵀz)^d, the RBF/Gaussian exp(−‖x−z‖²/2σ²) (infinite-dimensional, universal), or kernels on strings/graphs; the support vector machine chooses the separating hyperplane with maximum geometric margin, a convex QP whose Lagrange dual depends on the data only via inner products (hence kernelizable) and whose solution is a sparse combination of support vectors (the points on or inside the margin, by the KKT conditions); soft margins with slack variables and the regularization parameter C handle non-separable data, equivalent to minimizing hinge loss plus ‖w‖², and SMO solves the dual by optimizing two multipliers at a time; kernel ridge regression and Gaussian processes are the regression counterparts, and the practical rules are scale the features, cross-validate C and σ, use a linear kernel for high-dimensional sparse data (text), and expect gradient-boosted trees and neural networks to win on large tabular and perceptual data respectively.
---
# Kernels and support vector machines

**In one sentence.** If an algorithm only ever needs inner products between examples, swap
them for a kernel and you have silently moved to a huge feature space; the SVM is the
algorithm that made this worthwhile, by maximizing the margin so that the solution depends
on a few support vectors and generalizes despite the dimension.

## Feature maps and the kernel trick (CS229 ch. 5)
Fit y ≈ θᵀφ(x) with φ(x) = all monomials up to degree 3 in d variables — O(d³) features; the
GD update θ ← θ + α Σᵢ (yᵢ − θᵀφ(xᵢ)) φ(xᵢ) shows θ stays in span{φ(xᵢ)}: write θ = Σ βᵢ φ(xᵢ),
and the update needs only ⟨φ(xᵢ), φ(xⱼ)⟩ = **K(xᵢ, xⱼ)**. For φ = degree-3 monomials, K(x, z) =
(1 + xᵀz)³ costs O(d), not O(d³). **Kernel trick**: precompute the n×n **Gram matrix**, run
the algorithm in terms of β — cost O(n²) per pass, independent of the feature dimension.
**Mercer's theorem**: K is a valid kernel (equals some ⟨φ(x), φ(z)⟩) iff every Gram matrix is
symmetric positive semidefinite. Kernels: linear, **polynomial** (xᵀz + c)^d, **RBF/Gaussian**
exp(−‖x − z‖²/(2σ²)) — corresponds to an infinite-dimensional φ, is a similarity measure,
and can fit anything (bandwidth σ controls smoothness); kernels on strings (substring
counts — used for protein/text classification), graphs, sets, and distributions; kernels
compose (sums, products, scalings). The **representer theorem**: the minimizer of empirical
loss + λ‖f‖² in the RKHS is f(x) = Σ αᵢ K(xᵢ, x) — every regularized kernel method is
a weighted sum of kernel evaluations on training points; a **kernel perceptron**, kernel
ridge regression (α = (K + λI)⁻¹y), kernel PCA, kernel k-means, and **Gaussian processes**
(kernel = covariance; Bayesian regression with closed-form uncertainty — [[bayesian-inference]])
follow. Cost is the barrier: O(n²) memory and O(n³) solves; random Fourier features and
Nyström approximations trade accuracy for scale.

## The maximum-margin classifier (CS229 ch. 6; Cortes & Vapnik 1995)
Labels y ∈ {−1, +1}, h(x) = sign(wᵀx + b). **Functional margin** γ̂ᵢ = yᵢ(wᵀxᵢ + b) (scales with
w); **geometric margin** γᵢ = γ̂ᵢ/‖w‖ (distance to the hyperplane). Choose the hyperplane
maximizing the minimum geometric margin: fix the functional margin at 1 and solve
min ½‖w‖² s.t. yᵢ(wᵀxᵢ + b) ≥ 1 — a convex quadratic program ([[convexity]],
[[linear-programming-and-duality]]). Intuition and theory: a larger margin means a smaller
effective hypothesis class (fat-margin bounds independent of dimension —
[[statistical-learning-theory]]).

## Lagrange duality and support vectors
Lagrangian L = ½‖w‖² − Σ αᵢ[yᵢ(wᵀxᵢ + b) − 1], αᵢ ≥ 0. Stationarity gives w = Σ αᵢ yᵢ xᵢ and
Σ αᵢ yᵢ = 0; substituting yields the **dual**: max Σ αᵢ − ½ Σᵢⱼ yᵢ yⱼ αᵢ αⱼ ⟨xᵢ, xⱼ⟩ s.t.
αᵢ ≥ 0, Σ αᵢ yᵢ = 0. Strong duality holds (Slater); the **KKT** complementary-slackness
condition αᵢ[yᵢ(wᵀxᵢ + b) − 1] = 0 means αᵢ > 0 only for points with margin exactly 1 — the
**support vectors**; the solution is sparse, and predictions wᵀx + b = Σ αᵢ yᵢ ⟨xᵢ, x⟩ + b
need only inner products — hence **kernel SVMs**: replace ⟨xᵢ, x⟩ with K(xᵢ, x) and classify
in an infinite-dimensional space with a few hundred support vectors.

## Soft margins, hinge loss, and SMO
Non-separable or noisy data: slack ξᵢ ≥ 0, min ½‖w‖² + C Σ ξᵢ s.t. yᵢ(wᵀxᵢ + b) ≥ 1 − ξᵢ. The
dual is the same with **0 ≤ αᵢ ≤ C** (box constraints): αᵢ = 0 (correct, outside margin),
0 < αᵢ < C (on the margin), αᵢ = C (inside or misclassified). Equivalently, minimize the
**hinge loss** Σ max(0, 1 − yᵢ(wᵀxᵢ + b)) + λ‖w‖² — a convex surrogate for 0–1 loss, which
puts SVMs in the same regularized-ERM family as logistic regression (log loss) and lets them
be trained by SGD/Pegasos on huge linear problems (LIBLINEAR). **C** trades margin width
against violations: large C → hard margin, low bias, high variance; tune C (and σ for RBF) by
cross-validation on a log grid. **SMO** (Platt 1998): coordinate ascent on the dual that must
move two αs at once (the equality constraint), with an analytic solution for the pair and
heuristics for choosing it — the algorithm behind LIBSVM; O(n²)–O(n³) in practice.
Multiclass by one-vs-rest or one-vs-one; SVR for regression (ε-insensitive loss); one-class
SVMs for anomaly detection; probability outputs via Platt scaling ([[machine-learning-basics]]).

## In practice, and versus alternatives
Standardize features (RBF distances and margins are scale-sensitive); for text and other
high-dimensional sparse data a **linear** kernel is usually enough and orders of magnitude
faster; RBF for low-dimensional dense data with n ≲ 10⁵; beyond that, approximate kernels or
switch models. SVMs dominated 1995–2010 (MNIST, text, bioinformatics) because they were
convex, kernelizable, and theoretically grounded; **gradient-boosted trees** now win most
tabular benchmarks ([[decision-trees-and-ensembles]]) and **neural networks** learn their own
features for images/audio/text ([[deep-learning-basics]]) — the NTK view shows an
infinitely wide network trains like a kernel machine, which is both why kernels remain the
theory tool and why finite networks that leave the kernel regime beat them
([[statistical-learning-theory]]).

## Pitfalls
- Unscaled features with RBF kernels; default C and σ without a grid search.
- Kernel SVM on n = 10⁶ (quadratic memory); use linear/SGD or trees.
- Treating the SVM decision value as a probability.
- Choosing a kernel by intuition rather than validation; forgetting that the Gram matrix
  must be PSD when composing custom kernels.

## Related
- [[linear-models-logistic-regression-and-glms]], [[convexity]],
  [[linear-programming-and-duality]] (Lagrangian duality, KKT), [[gradient-descent]],
  [[statistical-learning-theory]] (margin bounds, NTK), [[decision-trees-and-ensembles]],
  [[deep-learning-basics]], [[svd-and-pca]] (kernel PCA), [[bayesian-inference]] (GPs),
  [[similarity-search-and-lsh]] (kernels as similarity), [[machine-learning-basics]].

## Sources
CS229 notes ch. 5–6 (ToC read); Cortes & Vapnik 1995; Platt 1998 (SMO); Schölkopf & Smola, *Learning with Kernels* 2002; ESL ch. 12; UML ch. 15–16; Rahimi & Recht 2007 (random features).

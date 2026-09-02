---
title: Statistical learning theory — PAC learning and agnostic PAC, ERM and uniform convergence, the growth function and VC dimension (Sauer–Shelah), the fundamental theorem of statistical learning and its sample-complexity bounds, no free lunch, Rademacher complexity and symmetrization, margin bounds for SVMs and boosting, covering numbers and chaining, algorithmic stability, PAC-Bayes and compression bounds, computational hardness of learning, and deep-learning theory (norm-based bounds, implicit bias, NTK, double descent and benign overfitting)
type: concept
section: "6.8"
level: 500
tags: [statistical-learning-theory, pac-learning, agnostic-pac, realizable, sample-complexity, erm, uniform-convergence, glivenko-cantelli, growth-function, shattering, vc-dimension, sauer-shelah, fundamental-theorem, no-free-lunch, bias-complexity, structural-risk-minimization, srm, mdl, occam, rademacher-complexity, symmetrization, gaussian-complexity, margin-bounds, fat-shattering, covering-numbers, chaining, dudley, algorithmic-stability, pac-bayes, compression-bounds, computational-hardness, proper-vs-improper, weak-learning, boosting-margin, lower-bounds, minimax, deep-learning-theory, norm-based-capacity, implicit-bias, max-margin, ntk, neural-tangent-kernel, lazy-training, double-descent, benign-overfitting, interpolation, spectral-bias, vapnik, bartlett-mendelson]
sources: [learning-theory-texts-courses-and-seminal-papers]
summary: Statistical learning theory makes "generalization" a theorem: a class H is PAC-learnable if some algorithm, given m(ε, δ) i.i.d. samples, outputs a hypothesis within ε of the best in H with probability 1−δ, and the fundamental theorem says that for binary classification this holds iff H has finite VC dimension (the largest set it can shatter — label in all 2ⁿ ways), iff H has the uniform-convergence property, with ERM as the learner and sample complexity Θ((d + log(1/δ))/ε) realizable or Θ((d + log(1/δ))/ε²) agnostic — the Sauer–Shelah lemma turning a finite VC dimension into a polynomial growth function so the union bound over infinitely many hypotheses survives; no free lunch says no learner works for all distributions (an inductive bias is necessary), structural risk minimization trades class complexity against fit across a nested sequence (MDL/Occam bounds are its finite-class form), Rademacher complexity — the expected best correlation of H with random ±1 labels on the sample — gives data-dependent bounds via symmetrization that specialize to margin bounds for SVMs (complexity ∝ (R/γ)², independent of dimension) and boosting (why AdaBoost keeps improving after zero training error), covering numbers and chaining (Dudley's entropy integral) handle real-valued and infinite classes, algorithmic stability and PAC-Bayes bound generalization without any hypothesis class (stability: a small change in one sample changes the output little — SGD and regularized ERM are stable), computational hardness shows statistically learnable classes can be intractable to learn (Kearns–Valiant, cryptographic hardness, proper vs improper learning); and for deep networks — which can shatter any dataset of practical size (Zhang et al.) — the bounds shift to norms and margins (Bartlett 1998, Neyshabur), to the implicit bias of gradient descent (converges to max-margin/minimum-norm solutions), to the neural tangent kernel (infinitely wide nets train as linear models in a fixed kernel — "lazy" regime that explains convergence but not feature learning), and to double descent and benign overfitting (interpolating estimators can be consistent when the noise is absorbed by many low-variance directions), which is where the theory currently ends.
---
# Statistical learning theory

**In one sentence.** Generalization is uniform convergence — the empirical risk tracks the
true risk simultaneously for every hypothesis when the class is "small" in the right sense
(VC dimension, Rademacher complexity, margin, norm, stability) — and the open frontier is
that for deep networks the right sense is not yet known.

## PAC learning and the fundamental theorem (UML ch. 2–6; Mohri ch. 2–3)
**PAC** (Valiant 1984): H is PAC-learnable if ∃ algorithm A and m_H(ε, δ) such that for every
distribution D (realizable: some h ∈ H has zero error) and m ≥ m_H samples, with probability
≥ 1 − δ, L_D(A(S)) ≤ ε. **Agnostic PAC**: L_D(A(S)) ≤ min_{h∈H} L_D(h) + ε (no realizability).
Finite H: ERM works with m = O((log|H| + log(1/δ))/ε) (realizable) or O((log|H| + log(1/δ))/ε²)
(agnostic) — Hoeffding + union bound ([[generalization-bias-variance-and-regularization]]
derives it; [[concentration-inequalities]]). Infinite H: count *behaviours* on the sample, not
hypotheses — the **growth function** Π_H(m) = max over m points of |{(h(x₁),…,h(x_m))}| ≤ 2^m;
H **shatters** a set if all 2^m labelings are realized; **VC dimension** d = size of the largest
shattered set (thresholds on ℝ: 1; intervals: 2; halfspaces in ℝⁿ: n+1; axis-aligned
rectangles: 4; sin(ωx): ∞ despite one parameter — VC is not parameter count). **Sauer–Shelah**:
Π_H(m) ≤ Σᵢ₌₀ᵈ (m choose i) ≤ (em/d)^d — polynomial once m > d, which makes the union bound
over the ≤ (em/d)^d effective hypotheses on a double sample (**symmetrization** / ghost
sample) go through. **Fundamental theorem** (Vapnik–Chervonenkis; Blumer et al. 1989): for
binary H, TFAE — uniform convergence, agnostic PAC learnable, PAC learnable, ERM is a
successful learner, VC(H) < ∞; with m = Θ((d + log(1/δ))/ε) realizable and Θ((d + log(1/δ))/ε²)
agnostic (upper and matching lower bounds). Consequence: for a fixed class, error ≈
√(d/m) — the "d" is the quantity a practitioner should be estimating.

## No free lunch and structural risk minimization (UML ch. 5, 7)
**No free lunch**: for any learner and m < |X|/2 there is a distribution on which it fails
(error ≥ 1/4 with constant probability) while some hypothesis has zero error — learning
requires prior knowledge (a restricted H); the class of all functions has infinite VC.
**Bias–complexity decomposition**: L_D(h_S) = (approximation error: min over H) + (estimation
error: the excess of ERM over the best) — richer H lowers the first, raises the second
([[generalization-bias-variance-and-regularization]]). **Non-uniform learnability / SRM**:
nested classes H₁ ⊂ H₂ ⊂ …; minimize empirical risk + a complexity penalty ε_n(m, δ·w_n)
over n — learnable iff H is a countable union of finite-VC classes; **MDL/Occam**: with a
prefix-free description of hypotheses, L_D(h) ≤ L_S(h) + √((|h| + ln(2/δ))/2m) — shorter
descriptions generalize better ([[kolmogorov-complexity]]). Consistency (universal
consistency of k-NN, kernel rules) as the weakest guarantee.

## Rademacher complexity and margin bounds (Bartlett & Mendelson 2002; Mohri ch. 3, 5; UML ch. 26)
**Empirical Rademacher complexity** R̂_S(F) = E_σ[sup_{f∈F} (1/m) Σ σᵢ f(xᵢ)], σᵢ uniform ±1 —
how well F can correlate with random noise on the sample. Theorem: with probability
≥ 1 − δ, for all f ∈ F, E[f] ≤ Ê_S[f] + 2R_m(F) + √(ln(1/δ)/2m) — proof by McDiarmid +
symmetrization; **data-dependent** (no need for the worst-case sample), and R_m(H) ≤
√(2d ln(em/d)/m) recovers the VC bound (Massart's lemma). It composes: Lipschitz losses
(**Talagrand's contraction**), linear classes (R ≤ B·R_x/√m for ‖w‖ ≤ B, ‖x‖ ≤ R_x — dimension-
free), kernels (trace of the Gram matrix), and layer-by-layer for networks. **Margin
bounds**: for ρ-margin loss, error ≤ margin-training-error + O(R/(ρ√m)) — explains SVMs
(generalization controlled by margin over radius, not by dimension —
[[kernels-and-support-vector-machines]]) and **boosting**: AdaBoost keeps increasing the
margin distribution after training error hits zero, and the bound depends on margins, not
rounds (Schapire et al. 1998 — [[decision-trees-and-ensembles]]); the fat-shattering
dimension is the real-valued VC analogue. **Covering numbers and chaining** (Dudley's entropy
integral R_m ≤ inf_α [4α + 12∫_α^∞ √(ln N(ε, F, L₂)/m) dε]) handle infinite real-valued
classes; **Gaussian complexity**, JL/random projections, and generic chaining are the
Vershynin/Wainwright toolkit for high-dimensional statistics (sparse regression, minimax
lower bounds by Le Cam/Fano — [[entropy-and-information]]).

## Stability, PAC-Bayes, compression (Bousquet & Elisseeff 2002; McAllester 1999; UML ch. 13, 30–31)
Bounds that depend on the **algorithm**, not the class: **uniform stability** β — replacing
one training point changes the loss at any point by ≤ β ⇒ E[gen. gap] ≤ β and high-
probability bounds with β = O(1/m); Tikhonov-regularized ERM with convex Lipschitz loss is
stable with β = O(1/(λm)) (the reason regularization generalizes — [[convexity]]); SGD with
few passes is stable (Hardt, Recht & Singer 2016) — the first non-vacuous argument for deep
nets' generalization via the optimizer. **PAC-Bayes**: for a prior P over hypotheses chosen
before data and any posterior Q, E_Q[L_D] ≤ E_Q[L_S] + √((KL(Q ‖ P) + ln(2√m/δ))/2m) — bounds for
randomized/averaged predictors; gives the tightest **non-vacuous** bounds for real neural
networks (Dziugaite & Roy 2017) by optimizing Q; connects to flat minima (a Q with large
variance around a flat minimum has low KL and low loss) and to Bayesian marginal
likelihood. **Compression**: if a learner's output can be reconstructed from k of the m
samples, generalization error is Õ(k/m) (SVMs: support vectors; perceptron: mistakes;
pruned/quantized networks — Arora et al. 2018).

## Computational learning theory (UML ch. 8; Kearns & Vazirani)
Statistical learnability ≠ efficient learnability: **proper** learning (output in H) of
3-term DNF is NP-hard, while **improper** learning (output a 3-CNF) is easy; learning
parities with noise, DNFs, and intersections of halfspaces are hard under cryptographic
assumptions (Kearns & Valiant 1994: learning small circuits would break RSA — [[cryptography-basics]],
[[p-vs-np]]); the **weak-learning** question (does a slightly-better-than-chance learner imply
a strong one?) was answered by Schapire's boosting; **statistical query** model and lower
bounds (parity is hard for SQ — relevant to what gradient methods can learn); membership
queries, exact learning of automata (Angluin's L*), mistake bounds in online learning
([[online-learning-and-regret]]). ERM over neural networks is NP-hard even for tiny nets,
which is why the deep-learning theory question is about *gradient descent*, not ERM.

## Deep-learning theory (Ma STATS214 notes; Zhang 2017; Jacot 2018; Belkin 2019; Bartlett 2020)
Zhang et al.: standard nets fit random labels, so VC/Rademacher bounds on the class are
vacuous (capacity ≫ m) and explicit regularizers aren't the explanation ([[neural-network-training]]).
Responses:
- **Norm/margin-based capacity** (Bartlett 1998; Neyshabur et al.; Bartlett, Foster &
  Telgarsky 2017): Rademacher complexity bounded by products of layer norms (spectral ×
  Frobenius/(2,1)) over the margin — depends on the trained weights, not the parameter
  count; still numerically loose for real nets.
- **Implicit bias of optimization** (Soudry et al. 2018; Gunasekar et al.): GD on logistic
  loss for linearly separable data converges in direction to the **max-margin** (hard SVM)
  solution; GD from zero init on least squares to the minimum-norm interpolant; mirror
  descent / matrix factorization → low nuclear norm — the optimizer picks a simple solution
  among the interpolants ([[gradient-descent]]).
- **NTK / lazy training** (Jacot, Gabriel & Hongler 2018): as width → ∞ with standard
  parameterization the network's function evolves as kernel regression with the fixed
  neural tangent kernel K(x, x′) = ⟨∇_θ f(x), ∇_θ f(x′)⟩ — GD converges to a global minimum
  (a convex problem in disguise), generalization = kernel theory; but finite nets that
  **learn features** leave the lazy regime and beat their NTK (mean-field/µP parameterizations
  — [[scaling-laws]]), so NTK explains trainability, not the advantage of deep learning.
- **Double descent and benign overfitting** (Belkin et al. 2019; Bartlett et al. 2020; Hastie
  et al. 2019): test risk peaks at the interpolation threshold and falls beyond it
  ([[generalization-bias-variance-and-regularization]]); in linear regression the
  minimum-norm interpolant is consistent when the covariance has many small-eigenvalue
  directions that absorb the noise without hurting the signal — "benign" overfitting; kernel
  ridgeless regression and random features show the same; **spectral bias** (nets learn low
  frequencies first) gives an implicit early-stopping regularizer.
- Optimization landscape: no bad local minima for wide nets, saddle escape
  ([[gradient-descent]]); approximation theory (depth separations — [[deep-learning-basics]]);
  expressivity of transformers as circuits ([[complexity-theory-advanced]]).
The honest state: convergence of over-parameterized nets is understood in the lazy regime;
feature learning, the practical generalization of large models, and scaling laws lack a
predictive theory — [[scaling-laws]] are the empirical stand-in.

## Pitfalls
- Equating VC dimension with parameter count (sin(ωx)); using a class bound for a trained
  network and concluding nothing (vacuous ≠ wrong, but uninformative).
- Reading "PAC-learnable" as "efficiently learnable".
- Applying realizable-case sample complexity (1/ε) to noisy problems (1/ε²).
- Forgetting that Rademacher/margin bounds need the margin *and* the norm/radius scale.
- Treating NTK results as explaining feature learning; treating double descent as
  disproving bias–variance (it changes the x-axis).

## Related
- [[generalization-bias-variance-and-regularization]], [[concentration-inequalities]],
  [[online-learning-and-regret]], [[kernels-and-support-vector-machines]],
  [[decision-trees-and-ensembles]] (boosting), [[neural-network-training]],
  [[deep-learning-basics]], [[scaling-laws]], [[gradient-descent]], [[convexity]],
  [[kolmogorov-complexity]] (MDL), [[entropy-and-information]] (Fano),
  [[cryptography-basics]] and [[p-vs-np]] (hardness of learning),
  [[complexity-theory-advanced]], [[machine-learning-basics]].

## Sources
Shalev-Shwartz & Ben-David 2014 ch. 2–8, 13, 26–31; Mohri, Rostamizadeh & Talwalkar 2018 ch. 2–5, 14; Vershynin 2018; Vapnik & Chervonenkis 1971; Blumer et al. 1989; Bartlett & Mendelson 2002; Bousquet & Elisseeff 2002; McAllester 1999; Dziugaite & Roy 2017; Kearns & Valiant 1994; Schapire 1990; Schapire et al. 1998; Zhang et al. 2017; Jacot et al. 2018; Soudry et al. 2018; Belkin et al. 2019 (abstract read); Bartlett et al. 2020; Ma, STATS214/CS229M notes.

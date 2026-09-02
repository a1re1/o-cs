---
title: Maximum likelihood estimation (MLE) and MAP
type: concept
section: "1.4"
level: 300
tags: [mle, likelihood, log-likelihood, map, parameter-estimation, fisher-information, cramer-rao, bias, consistency, regularization, cross-entropy]
sources: [cs109-probability-for-computer-scientists, wasserman-all-of-statistics, blitzstein-stat110]
summary: Choose parameters that make the observed data most probable — maximize the log-likelihood of i.i.d. samples — with worked closed forms (Bernoulli, normal, Poisson), the properties that justify it (consistency, asymptotic normality with variance 1/nI(θ)), MAP as MLE plus a log-prior (= regularization), and why minimizing cross-entropy is MLE.
---
# Maximum likelihood estimation

**In one sentence.** θ̂_MLE = argmax_θ Σᵢ log f(xᵢ | θ): treat the data as fixed, the parameter as
the variable, and climb the log-likelihood.

## Recipe
1. Write the likelihood L(θ) = Π f(xᵢ | θ) for i.i.d. data; take logs (products → sums; avoids
   underflow — [[log-probabilities]]).
2. Differentiate, set to zero, check it is a maximum (or run gradient ascent if no closed form —
   [[gradient-descent]]).
3. Closed forms: Bernoulli p̂ = k/n; Normal μ̂ = x̄, σ̂² = (1/n)Σ(xᵢ − x̄)² (biased by factor (n−1)/n);
   Poisson λ̂ = x̄; Uniform(0,θ) θ̂ = max xᵢ (biased low); Exponential λ̂ = 1/x̄.
4. Linear regression with Gaussian noise: MLE = least squares ([[least-squares]]). Logistic regression:
   MLE of Bernoulli with p = σ(wᵀx); no closed form, concave log-likelihood, gradient Σ(yᵢ − pᵢ)xᵢ (§6.2).
   Classification with softmax: minimizing **cross-entropy** loss is exactly MLE of the categorical model.

## Properties (Wasserman ch. 9)
- Consistent (θ̂ → θ), asymptotically normal: √n(θ̂ − θ) → N(0, 1/I(θ)), I(θ) = Fisher information =
  −E[∂² log f/∂θ²]; asymptotically efficient (Cramér–Rao bound). Standard errors come from the
  observed information (Hessian of the negative log-likelihood at θ̂).
- Invariant: MLE of g(θ) is g(θ̂).
- Not necessarily unbiased (σ̂², max) and can overfit with few samples or many parameters (a die seen
  once gives p̂ = 1 for that face) ⇒ regularize.

## MAP and regularization
θ̂_MAP = argmax [Σ log f(xᵢ | θ) + log p(θ)]. Beta(a,b) prior on a Bernoulli p gives
p̂ = (k + a − 1)/(n + a + b − 2) (Laplace smoothing with a = b = 2). Gaussian prior on weights →
+λ‖w‖² (ridge); Laplace prior → +λ‖w‖₁ (lasso). As n → ∞ the prior washes out and MAP → MLE
([[bayes-theorem-and-inference]]).

## Model comparison
Higher likelihood always favours more parameters; penalize with AIC/BIC or use held-out likelihood /
cross-validation ([[least-squares]] validation, [[generalization-bias-variance-and-regularization]]).

## Pitfalls
- Maximizing likelihood over models of different dimension without penalty.
- Likelihood is a density: with continuous data it can exceed 1, and singular solutions exist (Gaussian
  mixture with a component collapsing on one point → infinite likelihood; needs priors/constraints,
  [[expectation-maximization]]).
- Local maxima for non-concave likelihoods; multiple restarts.

## Related
- [[bayes-theorem-and-inference]], [[least-squares]], [[log-probabilities]], [[hypothesis-testing-and-confidence-intervals]].

## Sources
CS109 reader Part 5 (Parameter Estimation, MLE, MAP); Wasserman ch. 9; Blitzstein (Beta–Binomial).

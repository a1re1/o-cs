---
title: Least squares, linear regression, and validation
type: concept
section: "1.2"
level: 200
tags: [least-squares, normal-equations, linear-regression, data-fitting, regularization, ridge, overfitting, validation, cross-validation, pseudoinverse, features]
sources: [boyd-vmls, strang-18-06]
summary: Minimize ‖Ax − b‖² — solved by the normal equations AᵀAx̂ = Aᵀb, geometrically the projection of b onto the column space, numerically via QR or SVD — and how it becomes linear regression with feature maps, regularization (ridge), and out-of-sample validation to detect overfitting.
---
# Least squares and linear regression

**In one sentence.** When Ax = b has no solution (tall A), take the x̂ that makes the residual
r = Ax − b shortest; x̂ generally does *not* satisfy Ax = b, it makes Ax̂ the projection of b onto C(A).

## Solution
- **Normal equations**: AᵀA x̂ = Aᵀb; unique when columns are independent (AᵀA invertible).
  x̂ = (AᵀA)⁻¹Aᵀb = A⁺b, the pseudoinverse. Derivation: gradient of ‖Ax − b‖² is 2Aᵀ(Ax − b) = 0,
  or geometry: residual ⊥ every column ⇒ Aᵀ(b − Ax̂) = 0.
- **Numerics**: use QR (x̂ = R⁻¹Qᵀb, ≈ 2mn² flops) or SVD; forming AᵀA squares the condition number
  ([[orthogonality-and-projections]], [[svd-and-pca]]).
- **Underdetermined** (wide A, independent rows): infinitely many solutions; the minimum-norm one is
  x = Aᵀ(AAᵀ)⁻¹b.

## Data fitting (VMLS ch. 13)
Model ŷ = θ₁f₁(x) + … + θ_pf_p(x) with basis functions f (constant, coordinates, polynomials, splines,
indicator/one-hot features, interactions). Stack N examples into an N×p matrix; least squares picks θ
to minimize RMS training error. Feature engineering = choosing f. Classification via least squares on
±1 labels works surprisingly well as a baseline (§6.2 does it properly).

## Regularization and multi-objective
Minimize ‖Ax − b‖² + λ‖x‖² (ridge / Tikhonov): equivalent to stacking √λ I under A, always has a
unique solution, shrinks coefficients, trades bias for variance; λ chosen by validation. Weighted least
squares scales rows. Constrained (Ax ≈ b subject to Cx = d) via KKT system.

## Validation (the sentence that matters)
"The goal of model fitting is not to fit the given data but to fit *new* data." Hold out a test set
(80/20), fit on the training set, compare RMS errors: train ≪ test ⇒ overfitting (too many/too flexible
features); train ≈ test ⇒ some evidence of generalization. **Cross-validation**: k folds, fit k
times, average — also shows how sensitive θ is to the data. Polynomial degree vs test error is the
canonical picture ([[bias-variance-tradeoff]]).

## Pitfalls
- Collinear features ⇒ AᵀA singular or ill-conditioned; coefficients meaningless though predictions may be fine.
- Outliers dominate squared loss; consider Huber/absolute loss (§1.6, convex optimization).
- Leaking test data into feature scaling or selection inflates validation scores.
- Extrapolation outside the training range is unsupported by any validation number.

## Related
- [[orthogonality-and-projections]] — geometry; [[svd-and-pca]] — pseudoinverse and conditioning.
- [[gradient-descent]] — iterative solution when A is huge (§1.6); [[bias-variance-tradeoff]] (§6.2).

## Sources
VMLS ch. 12–15 (least squares, data fitting, validation, classification, multi-objective); Strang lecture 16.

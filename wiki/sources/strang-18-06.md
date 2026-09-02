---
title: MIT 18.06 Linear Algebra (Strang) and Introduction to Linear Algebra
type: source
section: "1.2"
level: 200
tags: [linear-algebra, elimination, subspaces, orthogonality, eigenvalues, svd, projections, least-squares]
sources: []
authors: [Gilbert Strang]
year: 2010
institution: MIT
url: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
license: CC-BY-NC-SA
format: html
summary: Strang's canonical 34-lecture course (OCW 2010, plus 18.06SC and the 2020 "Vision of Linear Algebra" videos) built around the column picture of Ax=b, the four fundamental subspaces, orthogonality/projections, eigenvalues, and the SVD as the climax; the companion text is Introduction to Linear Algebra (6th ed.).
---
# MIT 18.06 Linear Algebra (Strang)

## What it is
The most-watched linear algebra course; level 200, no prerequisites beyond algebra. Lectures in
order: geometry of linear equations (row vs column picture) → elimination → matrix multiplication
and inverses → LU factorization → transposes, permutations, vector spaces → column space and
nullspace → solving Ax=0 and Ax=b → independence, basis, dimension → the four fundamental subspaces →
graphs and incidence matrices → orthogonality → projections → least squares → Gram–Schmidt →
determinants → eigenvalues/eigenvectors → diagonalization and powers → differential equations →
Markov matrices and Fourier → symmetric matrices and positive definiteness → similar matrices, Jordan
form → SVD → linear transformations and change of basis → pseudoinverse.

Strang's pedagogical thesis: think in terms of *column combinations* ("Ax is a combination of the
columns of A"), and every factorization (A = LU, A = QR, A = XΛX⁻¹, A = QΛQᵀ, A = UΣVᵀ) is the course.

## Key ideas → pages
- Column picture, elimination, LU — [[gaussian-elimination-lu]], [[matrices-and-linear-maps]].
- Column space, nullspace, rank, rank–nullity, the "big picture" — [[four-fundamental-subspaces]].
- Orthogonality, projection matrices P = A(AᵀA)⁻¹Aᵀ, Gram–Schmidt / QR — [[orthogonality-and-projections]].
- Least squares as projection onto the column space — [[least-squares]].
- Eigenvalues, diagonalization, Markov matrices, symmetric ⇒ orthogonal eigenvectors, positive definite
  ⇔ all pivots/eigenvalues positive — [[eigenvalues-and-eigenvectors]].
- SVD: A = UΣVᵀ, singular values as the "right" sizes, low-rank approximation — [[svd-and-pca]].

## Notable claims
- "The four fundamental subspaces" picture — row space ⊥ nullspace, column space ⊥ left nullspace — is
  the one diagram to remember.
- Determinants are taught *after* the subspaces on purpose: they are a poor computational tool
  (Cramer's rule is O(n!) naively) but a good theoretical one.

## What it adds
Geometric/algorithmic intuition that [[boyd-vmls]] takes for granted; VMLS in turn supplies the
applied side (data fitting, validation, k-means) that 18.06 only touches.

---
title: Machine learning courses, texts and seminal papers — Stanford CS229 (Ng & Ma notes, 2026 edition), Caltech Learning from Data, MIT 6.390, Cornell CS4780, Berkeley CS189; ISLR, ESL, Bishop PRML, Murphy PML, Shalev-Shwartz & Ben-David UML, Mathematics for ML, Géron; Vapnik–Chervonenkis, Valiant PAC, Cortes–Vapnik SVM, Breiman random forests and "Two Cultures", Friedman gradient boosting, XGBoost, EM, Lasso, no free lunch, Domingos
type: source
section: "6.2"
level: 400
tags: [cs229, andrew-ng, tengyu-ma, cs156, abu-mostafa, learning-from-data, 6-390, cs4780, cs189, shewchuk, islr, esl, hastie-tibshirani, bishop-prml, murphy-pml, shalev-shwartz, ben-david, understanding-machine-learning, mathematics-for-machine-learning, geron, hands-on-ml, vapnik, chervonenkis, valiant, pac, cortes-vapnik, svm, breiman, random-forests, two-cultures, friedman, gradient-boosting, xgboost, dempster, em, tibshirani, lasso, wolpert, no-free-lunch, domingos]
sources: []
authors: [Andrew Ng, Tengyu Ma, Yaser Abu-Mostafa, Gareth James, Trevor Hastie, Robert Tibshirani, Christopher Bishop, Kevin Murphy, Shai Shalev-Shwartz, Shai Ben-David, Marc Deisenroth, Aurélien Géron, Vladimir Vapnik, Leslie Valiant, Corinna Cortes, Leo Breiman, Jerome Friedman, Tianqi Chen, Arthur Dempster, David Wolpert, Pedro Domingos]
year: 2014
institution: Stanford / Caltech / MIT / Cornell / Berkeley
url: https://cs229.stanford.edu/main_notes.pdf
license: mixed (CS229 notes, ISLR, ESL, PRML, Murphy, UML, MML free; Géron commercial)
format: pdf
summary: The CS229 lecture notes (Ma & Ng; the 2026 edition read here) are the compact canon — I supervised learning (linear regression with LMS and normal equations, probabilistic interpretation, locally weighted regression; logistic regression, perceptron, softmax, Newton's method; generalized linear models from the exponential family; generative algorithms — Gaussian discriminant analysis, naive Bayes; kernel methods and the kernel trick; SVMs with margins, Lagrange duality, soft margins, SMO), II deep learning (modules, backpropagation, vectorization), III generalization and regularization (bias–variance decomposition, double descent, sample complexity for finite and infinite hypothesis classes, implicit regularization, cross-validation, Bayesian view), IV unsupervised (k-means, EM for mixtures with Jensen and the ELBO, variational inference and VAEs, PCA, ICA), V generative and foundation models (diffusion models, linear probes and LoRA, contrastive learning, retrieval-augmented generation, LLMs with tokenization/transformers/MoE/in-context learning/SFT, chain-of-thought and RLVR), VI reinforcement learning and control; Shalev-Shwartz & Ben-David's Understanding Machine Learning is the rigorous companion (PAC, ERM/SRM/MDL, no-free-lunch, VC dimension, computational complexity of learning, then algorithms and advanced theory); ISLR/ESL are the statistician's texts (ESL the reference for trees, boosting, kernels, regularization), Bishop and Murphy the probabilistic view, Abu-Mostafa the cleanest treatment of generalization; and the seminal papers give VC theory (1971), PAC learning (1984), SVMs (1995), random forests and the "two cultures" essay (2001), gradient boosting (2001) and XGBoost (2016), EM (1977), the Lasso (1996), no-free-lunch theorems, and Domingos' "A Few Useful Things to Know about Machine Learning" (2012).
---
# Machine learning: courses, texts, and seminal papers

## What they are
- **CS229 lecture notes** (Tengyu Ma & Andrew Ng; 2026 edition, ~240 pp): chapters 1–6
  supervised (linear regression, classification/logistic regression, GLMs, generative
  learning, kernels, SVMs), 7 deep learning, 8–9 generalization and regularization,
  10–13 unsupervised (k-means, EM, PCA, ICA), 14–18 diffusion, foundation models,
  representation learning, LLMs, reasoning (chain-of-thought, RLVR), 19 RL and control.
  The notes have tracked the field: the 2026 edition's Part V did not exist in 2018.
- **Abu-Mostafa, Learning from Data** (Caltech CS156, lectures open): the learning problem,
  is learning feasible (Hoeffding), the VC bound, bias–variance, linear models,
  overfitting, regularization, validation, SVMs, kernels, RBFs, three learning principles
  (Occam's razor, sampling bias, data snooping). The clearest short book on generalization.
- **ISLR** (James, Witten, Hastie, Tibshirani; 2e 2021, R and Python): regression,
  classification, resampling, model selection and regularization, beyond linearity,
  trees, SVMs, deep learning, survival, unsupervised, multiple testing. **ESL** (Hastie,
  Tibshirani, Friedman; 2e 2009): the graduate reference — linear methods, basis expansions,
  kernel smoothing, model assessment, additive models and trees, boosting, neural nets,
  SVMs, prototypes/nearest neighbours, unsupervised, random forests, ensembles, undirected
  graphical models, high-dimensional problems.
- **Bishop, PRML** (2006): Bayesian throughout — distributions, linear models, kernels,
  graphical models, mixtures/EM, approximate inference, sampling, sequential data.
  **Murphy, Probabilistic ML: An Introduction / Advanced Topics** (2022–23): the modern
  encyclopaedia. **Shalev-Shwartz & Ben-David, UML** (2014): Part I foundations (PAC, ERM,
  uniform convergence, bias–complexity trade-off, VC dimension, non-uniform learnability
  — SRM/MDL, runtime of learning), II algorithms (linear predictors, boosting, model
  selection, convex learning, regularization/stability, SGD, SVM, kernels, multiclass,
  decision trees, nearest neighbour, neural networks), III additional models (online
  learning, clustering, dimensionality reduction, generative models, feature selection),
  IV advanced theory (Rademacher complexity, covering numbers, proof of the fundamental
  theorem, multiclass learnability, compression bounds, PAC-Bayes). **Mathematics for ML**
  (Deisenroth, Faisal, Ong): linear algebra, analytic geometry, matrix decompositions, vector
  calculus, probability, continuous optimization; then regression, PCA, GMMs, SVMs as
  worked applications. **Géron**: scikit-learn/Keras practice — pipelines, feature
  engineering, evaluation, deployment.
- **Courses**: MIT 6.390 (notes open; regression, classification, neural nets, CNNs,
  transformers, clustering, MDPs/RL), Cornell CS4780 (Weinberger's lectures: k-NN, perceptron,
  MLE/MAP, logistic regression, GD, SVMs, kernels, GPs, trees, bagging, boosting, bias–variance,
  deep learning), Berkeley CS189 (Shewchuk's notes: decision theory, SVMs, GDA, regression,
  regularization, kernels, trees, NNs, PCA, clustering, spectral clustering), Google ML crash
  course, fast.ai (top-down deep learning practice).
- **Seminal**: Vapnik & Chervonenkis 1971 (uniform convergence of frequencies to
  probabilities — the VC dimension); Valiant 1984 ("A theory of the learnable" — PAC:
  polynomial samples and time, ε/δ); Cortes & Vapnik 1995 (soft-margin SVM); Breiman 2001
  (random forests: bagging + random feature subsets; and "Statistical Modeling: The Two
  Cultures" — data models vs algorithmic models, predictive accuracy as the arbiter);
  Friedman 2001 (gradient boosting machines: boosting as gradient descent in function
  space); Chen & Guestrin 2016 (XGBoost: second-order boosting, regularized objective,
  sparsity-aware split finding, cache-aware systems design); Dempster, Laird & Rubin 1977
  (EM); Tibshirani 1996 (Lasso: L1 penalty gives sparsity); Wolpert 1996 (no free lunch:
  averaged over all target functions every learner is equal — inductive bias is necessary);
  Domingos 2012 ("learning = representation + evaluation + optimization; it's generalization
  that counts; data alone is not enough; overfitting has many faces; intuition fails in high
  dimensions; theoretical guarantees are not what they seem; feature engineering is the key;
  more data beats a cleverer algorithm; learn many models, not just one; simplicity does not
  imply accuracy; representable does not imply learnable; correlation does not imply
  causation").

## Key ideas → pages
[[machine-learning-basics]], [[linear-models-logistic-regression-and-glms]],
[[kernels-and-support-vector-machines]], [[decision-trees-and-ensembles]],
[[generalization-bias-variance-and-regularization]], [[unsupervised-learning-em-and-mixture-models]];
existing: [[k-means-clustering]], [[svd-and-pca]], [[maximum-likelihood-estimation]],
[[gradient-descent]], [[convexity]].

## What they add
CS229 for the derivations in one place; Abu-Mostafa/UML for *why* learning works; ESL for
trees/boosting/regularization depth; Bishop/Murphy for the Bayesian and probabilistic
reading; Breiman's "two cultures" for the sociology — the split between explanatory
statistics and predictive ML that deep learning settled in favour of the latter.

---
title: Learning theory texts, courses and seminal papers — Shalev-Shwartz & Ben-David, Mohri–Rostamizadeh–Talwalkar's Foundations of Machine Learning (free), Vershynin's High-Dimensional Probability (free), Wainwright's High-Dimensional Statistics, Cesa-Bianchi & Lugosi's Prediction, Learning, and Games; MIT 9.520, Stanford STATS214/CS229M (Ma's notes), CMU 10-715, Berkeley CS281A; Vapnik–Chervonenkis, Bartlett & Mendelson Rademacher complexity, Belkin et al. double descent, Jacot et al. NTK, Kearns & Valiant, Schapire and Freund & Schapire boosting theory
type: source
section: "6.8"
level: 500
tags: [shalev-shwartz, ben-david, understanding-machine-learning, mohri, foundations-of-machine-learning, vershynin, high-dimensional-probability, wainwright, high-dimensional-statistics, cesa-bianchi, lugosi, prediction-learning-and-games, 9-520, poggio, stats214, cs229m, tengyu-ma, 10-715, cs281a, vapnik, chervonenkis, vc-theory, bartlett, mendelson, rademacher, belkin, double-descent, jacot, ntk, neural-tangent-kernel, kearns, valiant, weak-learning, schapire, freund, boosting, adaboost-theory, margin-theory]
sources: []
authors: [Shai Shalev-Shwartz, Shai Ben-David, Mehryar Mohri, Afshin Rostamizadeh, Ameet Talwalkar, Roman Vershynin, Martin Wainwright, Nicolò Cesa-Bianchi, Gábor Lugosi, Tomaso Poggio, Tengyu Ma, Vladimir Vapnik, Alexey Chervonenkis, Peter Bartlett, Shahar Mendelson, Mikhail Belkin, Arthur Jacot, Michael Kearns, Leslie Valiant, Robert Schapire, Yoav Freund]
year: 2014
institution: Hebrew University / NYU / UC Irvine / Berkeley / MIT / Stanford
url: https://cs.nyu.edu/~mohri/mlbook/
license: mixed (UML, Mohri et al., Vershynin, CS229M notes free)
format: pdf
summary: Learning theory asks when and how well a learner generalizes from finite samples: Shalev-Shwartz & Ben-David (PAC learning, ERM, uniform convergence, the no-free-lunch theorem, VC dimension and the fundamental theorem, non-uniform learnability via SRM/MDL, computational complexity of learning, then Rademacher complexity, covering numbers, compression and PAC-Bayes bounds) and Mohri, Rostamizadeh & Talwalkar (PAC, Rademacher/VC bounds, SVM and kernel theory, boosting, online learning, multiclass, ranking, regression, algorithmic stability, dimensionality reduction, learning automata) are the two rigorous textbooks; Vershynin's High-Dimensional Probability (sub-Gaussian/sub-exponential concentration, random matrices, covering, chaining, Johnson–Lindenstrauss, sparse recovery) and Wainwright's High-Dimensional Statistics (sparse regression, matrix estimation, minimax lower bounds) supply the probabilistic tools; Cesa-Bianchi & Lugosi is the online-learning/regret reference; MIT 9.520 (Poggio — regularization, RKHS, stability), Stanford STATS214/CS229M (Ma — concentration, uniform convergence, Rademacher, margin bounds, deep-learning theory: implicit regularization, NTK, double descent, optimization landscapes) and CMU 10-715 are the courses; and the seminal papers are Vapnik & Chervonenkis (1971, uniform convergence of empirical frequencies), Bartlett & Mendelson (2002, Rademacher and Gaussian complexities as data-dependent capacity), Belkin et al. (2019, double descent: "the bias-variance trade-off appears to be at odds with the observed behavior … very rich models are trained to exactly fit the data … and yet they often obtain high accuracy"), Jacot, Gabriel & Hongler (2018, the neural tangent kernel governing infinitely wide networks), Kearns & Valiant (weak learnability and the hardness of learning), Schapire (1990, the strength of weak learnability — boosting exists) and Freund & Schapire (1997, AdaBoost and its margin theory).
---
# Learning theory: texts, courses, and seminal papers

## What they are
- **Shalev-Shwartz & Ben-David, UML** (2014; free): Part I foundations — a gentle start (PAC),
  a formal learning model (agnostic PAC, generalized loss), learning via uniform
  convergence, the bias–complexity trade-off and **no-free-lunch**, the **VC dimension** and
  the **fundamental theorem of statistical learning** (finite VC ⇔ PAC-learnable ⇔ uniform
  convergence, with sample-complexity bounds), non-uniform learnability (SRM, MDL, Occam),
  the runtime of learning (computational hardness, proper vs improper); Part II algorithms
  (linear predictors, boosting, model selection and validation, convex learning problems,
  regularization and stability, SGD, SVM, kernels, multiclass, decision trees, nearest
  neighbour, neural networks — with their sample-complexity and hardness results); Part III
  (online learning, clustering, dimensionality reduction, generative models, feature
  selection); Part IV advanced theory (Rademacher complexities, covering numbers, proof of
  the fundamental theorem, multiclass learnability, compression bounds, PAC-Bayes).
- **Mohri, Rostamizadeh & Talwalkar, Foundations of ML** (2e 2018; free): PAC framework;
  Rademacher complexity and VC dimension; model selection; SVMs (margin bounds); kernel
  methods (PDS kernels, rational kernels); boosting (margin theory, game-theoretic view);
  on-line learning (Halving, Weighted Majority, Perceptron and Winnow mistake bounds,
  online-to-batch); multiclass; ranking (RankBoost, bipartite ranking); regression (bounds,
  kernel ridge, Lasso); maximum entropy models; conditional maxent; algorithmic stability;
  dimensionality reduction (PCA, KPCA, JL); learning automata and languages; reinforcement
  learning. Appendices: linear algebra, convex optimization, probability, concentration
  inequalities, information theory.
- **Vershynin, HDP** (2018; free): preliminaries on random variables, concentration of sums
  (Hoeffding, Chernoff, sub-Gaussian/sub-exponential, Bernstein), random vectors in high
  dimensions, random matrices (covariance estimation, nets), concentration without
  independence (Lipschitz functions, Talagrand), quadratic forms and symmetrization, random
  processes (Gaussian, Sudakov, chaining — Dudley), chaining (generic chaining, VC theory),
  Gaussian width/dimension reduction (JL), sparse recovery, Dvoretzky–Milman.
  **Wainwright, HDS** (2019): tail bounds, uniform laws, metric entropy, random matrices,
  sparse linear models, PCA, nonparametric least squares, RKHS, minimax lower bounds
  (Le Cam/Fano), graphical model estimation. **Cesa-Bianchi & Lugosi** (2006): prediction
  with expert advice, tight bounds, randomized prediction, efficient forecasters, calibration,
  games (minimax theorem via learning), bandits.
- **Courses**: **MIT 9.520** (Poggio, Rosasco: statistical learning theory as regularization —
  RKHS, stability, Tikhonov, deep nets); **Stanford STATS214 / CS229M** (Tengyu Ma; notes
  free: supervised learning formulation, asymptotic analysis, concentration, uniform
  convergence and Rademacher complexity, VC dimension, margin theory, non-convex
  optimization, implicit regularization, NTK, double descent/benign overfitting,
  unsupervised/self-supervised theory, online learning); **CMU 10-715** (Advanced intro to ML);
  **Berkeley CS281A** (statistical learning theory, graphical models).
- **Seminal**: Vapnik & Chervonenkis 1971 (uniform convergence of relative frequencies —
  the VC dimension and growth function); Valiant 1984 (PAC — [[ml-courses-texts-and-seminal-papers]]);
  Blumer, Ehrenfeucht, Haussler & Warmuth 1989 (PAC learnability ⇔ finite VC); Kearns &
  Valiant 1989/94 (cryptographic hardness of learning; the weak-learning question);
  Schapire 1990 (weak learners can be boosted to strong); Freund & Schapire 1997 (AdaBoost;
  online learning connection) and Schapire, Freund, Bartlett & Lee 1998 (boosting the
  margin — why AdaBoost doesn't overfit); Bartlett & Mendelson 2002 (Rademacher/Gaussian
  complexities: data-dependent, kernel and margin bounds); Bousquet & Elisseeff 2002
  (stability ⇒ generalization); McAllester 1999 (PAC-Bayes); Zhang et al. 2017 (rethinking
  generalization); Belkin, Hsu, Ma & Mandal 2019 (**double descent** — abstract read: the
  classical U-curve is subsumed by a curve where "increasing model capacity beyond the point
  of interpolation results in improved performance"); Bartlett, Long, Lugosi & Tsigler 2020
  (benign overfitting in linear regression); Jacot, Gabriel & Hongler 2018 (**NTK**: infinitely
  wide networks train as kernel regression with a fixed kernel); Soudry et al. 2018 (implicit
  bias of GD to max-margin); Neyshabur et al. 2015–17 (norm-based capacity for deep nets).

## Key ideas → pages
[[statistical-learning-theory]], [[online-learning-and-regret]],
[[concentration-inequalities]] (existing, §1.4), [[generalization-bias-variance-and-regularization]]
(§6.2 intro), [[decision-trees-and-ensembles]] (boosting), [[kernels-and-support-vector-machines]].

## What they add
UML for the cleanest proofs of PAC/VC/NFL; Mohri for breadth (online, ranking, stability)
and the boosting–games connection; Vershynin for the concentration/chaining toolkit that
every modern bound is built from; Ma's notes for the deep-learning theory of 2018–2024 that
the books predate; the paper list shows the field's question changing from "which classes
are learnable and how many samples" to "why do over-parameterized models trained by GD
generalize at all".

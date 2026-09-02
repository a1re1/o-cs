---
title: Probabilistic graphical models — Bayesian networks vs Markov random fields (factorization, Hammersley–Clifford, Markov blankets, I-maps, converting between them), factor graphs, conditional random fields, exact inference (variable elimination, treewidth, clique/junction trees, belief propagation — sum-product and max-product), loopy BP, MAP inference (graph cuts, LP relaxations, dual decomposition), parameter learning (MLE in directed and undirected models, the partition-function problem), structure learning (Chow–Liu, score-based, constraint-based), and where PGMs survive in the deep-learning era
type: concept
section: "6.7"
level: 500
tags: [pgm, probabilistic-graphical-models, bayesian-networks, markov-random-fields, mrf, undirected-models, hammersley-clifford, cliques, potentials, partition-function, gibbs-distribution, markov-blanket, i-map, perfect-map, moralization, factor-graphs, crf, conditional-random-fields, variable-elimination, treewidth, elimination-order, junction-tree, clique-tree, belief-propagation, sum-product, max-product, message-passing, loopy-bp, bethe, map-inference, graph-cuts, submodular, lp-relaxation, dual-decomposition, parameter-learning, mle, contrastive-divergence, pseudo-likelihood, structure-learning, chow-liu, bic, exponential-family, ising, potts, ldpc, koller-friedman, cs228]
sources: [pgm-and-bayesian-texts-courses-and-seminal-papers]
summary: A graphical model encodes a joint distribution as a product of local factors whose structure a graph makes explicit: directed Bayesian networks factor as Π P(xᵢ | parents) with independencies read by d-separation, undirected Markov random fields factor over cliques as (1/Z) Π φ_c(x_c) (Hammersley–Clifford: positive distributions satisfying the graph's Markov properties are exactly such Gibbs distributions) with independencies by simple graph separation — the two families represent different independence sets (v-structures vs cycles), and factor graphs subsume both; conditional random fields are MRFs over labels conditioned on inputs (the sequence-labelling workhorse before transformers); exact inference is variable elimination — sum out variables in an order whose cost is exponential in the induced width, minimized by the treewidth — packaged reusably as the junction tree (moralize, triangulate, build a clique tree, pass sum-product messages both ways to get all marginals at once), with belief propagation the same message passing on trees, loopy BP its approximate application to cyclic graphs (the LDPC decoder, and a fixed point of the Bethe free energy), and max-product/graph cuts/LP relaxations/dual decomposition for MAP assignments; learning fits parameters by MLE (closed-form counts in directed models; gradient methods needing the intractable partition function in undirected ones, approximated by contrastive divergence or pseudo-likelihood) and structure by Chow–Liu trees, BIC-scored search or independence tests; and although deep nets absorbed most modelling, the PGM vocabulary — factorization, message passing, treewidth, partition functions — is how variational autoencoders, energy-based models, and CRF-on-CNN pipelines are still understood.
---
# Probabilistic graphical models

**In one sentence.** Draw the independence structure as a graph, and the joint distribution
factorizes over it; inference is then message passing whose cost is set by the treewidth,
and learning is counting (directed) or fighting the partition function (undirected).

## Representation (CS228 representation; K&F ch. 3–4)
**Bayesian networks** (directed): P(x) = Π P(xᵢ | pa(xᵢ)); independencies by **d-separation**;
an **I-map** (every independence the graph asserts holds in P), perfect maps, minimal I-maps
— introduced in [[bayesian-networks-and-hmms]]. **Markov random fields** (undirected):
P(x) = (1/Z) Π_{c ∈ cliques} φ_c(x_c), Z = Σ_x Π φ_c the **partition function**; potentials are
non-negative, not probabilities; often written as a **Gibbs/energy** form P ∝ exp(−Σ E_c)
(the **Ising/Potts** models of statistical physics; log-linear/**exponential-family**
parameterization P ∝ exp(θᵀ f(x))). Independencies by **graph separation** (X ⊥ Y | Z iff Z
blocks all paths); the local Markov property (a node ⊥ rest | its neighbours — the
**Markov blanket**); **Hammersley–Clifford**: for positive P, Markov w.r.t. G ⇔ factorizes
over G's cliques. Directed vs undirected express different families: a v-structure
A → C ← B (A ⊥ B, not given C) has no undirected perfect map; a 4-cycle has no directed one.
Convert directed → undirected by **moralization** (marry parents, drop arrows; loses the
v-structure independencies). **Factor graphs** (bipartite variables–factors) make the
factorization explicit and unify both for message passing. **CRFs** (Lafferty et al. 2001):
P(y | x) = (1/Z(x)) Π φ_c(y_c, x) — discriminative MRFs over labels; linear-chain CRFs for
POS/NER ([[nlp-fundamentals]]), grid CRFs for segmentation ([[computer-vision-fundamentals]]),
CRF-as-RNN on top of CNNs. Template/plate models (HMMs, LDA, relational models) repeat
structure; Gaussian graphical models (precision-matrix sparsity = conditional independence —
the graphical lasso).

## Exact inference (CS228 inference 1–2; K&F ch. 9–10)
Queries: marginals P(xᵢ | e), MAP argmax P(x | e), partition function/likelihood. Inference is
#P-hard in general (even approximate to constant factor is NP-hard) — structure is what
makes it feasible. **Variable elimination**: multiply the factors containing the variable,
sum it out, repeat; complexity O(n · d^{w+1}) with w the **induced width** of the elimination
order; the best order achieves the **treewidth** (NP-hard to find; min-fill/min-degree
heuristics; trees have treewidth 1, grids √n, dense graphs n). **Junction (clique) tree**:
moralize → **triangulate** (chordal graph; maximal cliques) → build a clique tree satisfying
the running-intersection property → **calibrate** by passing messages (sum-product) up and
down once — all marginals of all cliques for the cost of ~2 VE runs (Lauritzen–Spiegelhalter;
Shafer–Shenoy / Hugin variants). **Belief propagation** on a tree/factor graph: variable-to-
factor and factor-to-variable messages μ; beliefs ∝ products of incoming messages; exact
after one sweep in each direction; the **forward–backward** algorithm and Viterbi are BP on a
chain; **max-product** (max-sum in log space) computes MAP with traceback ([[dynamic-programming]]
generalized to trees — [[bayesian-networks-and-hmms]] for HMMs, [[constraint-satisfaction-problems]]
for the same tree decomposition).

## Approximate inference: loopy BP and MAP methods (CS228 inference 2–3; K&F ch. 11, 13)
**Loopy BP**: run the message updates on a graph with cycles anyway — no guarantee, often
converges to good marginals; its fixed points are stationary points of the **Bethe free
energy** (Yedidia et al.), placing it among variational methods; damping, scheduling; the
turbo/LDPC decoders that approach Shannon capacity are loopy BP on code graphs
([[channel-capacity-and-error-correction]]); generalized BP on regions, tree-reweighted BP
(convex, bounds Z). **MAP inference**: max-product; for binary **submodular** pairwise
energies (attractive potentials) exact MAP by **graph cuts** / min-cut ([[network-flow]] — image
segmentation, stereo via α-expansion for multi-label); **LP relaxation** of the MAP integer
program over the local (pseudo-marginal) polytope — tight on trees, rounding and cutting
planes; **dual decomposition** (split the graph into tractable subproblems agreeing via
Lagrange multipliers, subgradient ascent — [[linear-programming-and-duality]]); ILP solvers
and simulated annealing for the rest ([[search-algorithms-ai]]). Sampling and variational
alternatives: [[monte-carlo-methods]], [[variational-inference]].

## Learning (CS228 learning 1–5; K&F ch. 17–20)
**Directed, fully observed**: MLE decomposes per CPT — counts (with Dirichlet priors for
smoothing/**Bayesian learning** — [[bayesian-inference]]); linear/logistic CPDs by regression.
**Undirected**: the log-likelihood θᵀ Σ f(x⁽ⁱ⁾) − N log Z(θ) is concave (exponential family)
but its gradient E_data[f] − E_model[f] needs model expectations = inference per step; exact
on low-treewidth graphs, else **contrastive divergence** (short Gibbs chains from the data —
RBMs/Boltzmann machines), **pseudo-likelihood** (product of conditionals — consistent, cheap),
score matching / noise-contrastive estimation ([[deep-generative-models]] energy-based
models). CRFs: gradient with conditional expectations (forward–backward per example);
L2/L1 regularization; large-margin alternatives (structured SVM). **Latent variables**:
EM ([[unsupervised-learning-em-and-mixture-models]]) — the E-step is inference, so hard
models need approximate E-steps (variational EM, MCMC-EM). **Structure learning**:
**Chow–Liu** (max-weight spanning tree on pairwise mutual information — the optimal tree
BN; [[minimum-spanning-trees]], [[entropy-and-information]]); **score-based** search
(BIC/BDe scores, greedy hill-climbing/tabu over DAGs, MMHC hybrids; the score decomposes per
family); **constraint-based** (PC algorithm: conditional-independence tests → skeleton →
orient v-structures — the entry to [[causal-inference]]); Gaussian graphical models by
graphical lasso.

## PGMs in the deep-learning era
Most classical PGM applications (speech HMMs, topic models, CRF taggers, MRF vision) were
replaced by neural nets, but the ideas persist: the VAE is a latent-variable model with
amortized variational inference; diffusion models are a fixed Markov chain with a learned
reverse model; energy-based models and score matching are undirected learning without Z;
transformers are learned message passing over a complete graph; graph neural networks
are parameterized BP (and struggle exactly where BP does); structured prediction heads
(CRF layers, CTC) still sit on deep encoders; and probabilistic programming (Stan, PyMC,
Pyro, NumPyro) makes PGMs into code with automatic MCMC/VI ([[bayesian-inference]]).
Treewidth-style reasoning is the right tool for "can I do this exactly?" in any factorized
system, including databases (join trees — [[query-optimization]]) and CSP solvers.

## Pitfalls
- Reading independence from an undirected graph with a directed-graph rule or vice versa;
  moralizing and then expecting v-structure independencies.
- Elimination in a bad order (exponential blow-up) when a min-fill order was cheap.
- Loopy BP treated as exact; MAP by max-product on graphs with cycles without checking.
- Undirected MLE with a biased/short-chain gradient and no monitoring of the log-likelihood.
- Structure learned from observational data read causally.

## Related
- [[bayesian-networks-and-hmms]], [[variational-inference]], [[monte-carlo-methods]],
  [[bayesian-inference]], [[causal-inference]], [[unsupervised-learning-em-and-mixture-models]],
  [[constraint-satisfaction-problems]], [[dynamic-programming]], [[network-flow]],
  [[linear-programming-and-duality]], [[minimum-spanning-trees]], [[entropy-and-information]],
  [[channel-capacity-and-error-correction]], [[deep-generative-models]], [[nlp-fundamentals]],
  [[computer-vision-fundamentals]], [[query-optimization]].

## Sources
CS228 notes (representation, inference, learning — read); Koller & Friedman ch. 3–4, 9–11, 13, 17–20; Pearl 1988; Lauritzen & Spiegelhalter 1988; Lafferty, McCallum & Pereira 2001 (CRFs); Yedidia, Freeman & Weiss 2003 (Bethe/GBP); Boykov, Veksler & Zabih 2001 (graph cuts); Sontag et al. 2011 (dual decomposition); Chow & Liu 1968; Spirtes, Glymour & Scheines 2000 (PC).

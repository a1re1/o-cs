# Log

Newest first. Generated from wiki/log/*.md — do not edit.

## [2026-09-01] ingest | §1.5 Logic, §1.6 Optimization & numerics, §1.7 Information theory
- Read: CS103 Summer 2026 lecture list; Open Logic Project part/chapter structure; forall x: Calgary description; Boyd & Vandenberghe contents + 9.3 (gradient descent convergence analysis: (1 − m/M) rate); MacKay ITILA contents + source coding theorem discussion (typical sets, "H bits, no more and no less"); 18.335 syllabus (from repo memory).
- Created sources: stanford-cs103, open-logic-project, forall-x-calgary, boyd-convex-optimization, mit-18-335-numerical-methods, mackay-itila, shannon-1948.
- Created concepts: first-order-logic, proof-systems-and-natural-deduction, soundness-and-completeness, godel-incompleteness-theorems, computability-and-halting-problem, convexity, linear-programming-and-duality, gradient-descent, floating-point, entropy-and-information, source-coding-and-compression, channel-capacity-and-error-correction, kolmogorov-complexity.
- Insight: diagonalization is one construction with four names (Cantor, halting, Gödel's G, Tarski's liar); each page now says so and links the others. Second insight: Boyd's (1 − m/M) rate makes "conditioning" the thread from §1.2 (κ = σ₁/σ_r) through §1.6 (Hessian) to §6.3 (why Adam/normalization help).
- Wanted pages: turing-machines, finite-automata-and-regular-languages, p-vs-np, decidability-and-reductions, sat-and-smt-solvers, model-checking, abstract-interpretation, curry-howard-correspondence, interactive-theorem-proving, type-systems, relational-model, lambda-calculus, approximation-algorithms, network-flow, support-vector-machines, congestion-control, neural-network-training, inverted-index, raid-and-erasure-coding, hash-functions-cryptographic, tcp, sorting.
- §1 (Foundations) complete: 7 sections, 20 sources, 49 concept pages.

## [2026-09-01] ingest | §1.4 Probability & statistics (CS109 reader, Stat110/Blitzstein, Think Stats, Wasserman, MCS part IV)
- Read: CS109 reader index + "Bootstrapping", "Central Limit Theorem", "Maximum Likelihood Estimation", "Algorithmic Analysis", "Log Probabilities"; CS109 Summer 2026 lecture list; Think Stats TOC; Wasserman TOC; Stat110 chapter structure; MCS ch. 19 (Markov/Chebyshev) from §1.1 pass.
- Created sources: cs109-probability-for-computer-scientists, blitzstein-stat110, think-stats-downey, wasserman-all-of-statistics.
- Created concepts: random-variables-expectation, common-distributions, bayes-theorem-and-inference, central-limit-theorem-and-lln, markov-chains, maximum-likelihood-estimation, hypothesis-testing-and-confidence-intervals, probabilistic-analysis-of-algorithms, log-probabilities. (concentration-inequalities already existed from §1.1.)
- Insight: three sources converge on one workflow for analyzing code — indicators + linearity, then law of total expectation on the first step, then a tail bound; made probabilistic-analysis-of-algorithms the hub page so §3.x algorithm pages can cite it instead of re-deriving.
- Tooling: fetch.py --start REGEX (multiline) to skip site navigation; the CS109 reader repeats a ~2.5k-char nav on every page.
- Wanted pages now include: sorting, hash-tables, randomized-algorithms, floating-point, entropy-and-information, monte-carlo-methods, gradient-descent, pagerank, expectation-maximization, bias-variance-tradeoff.

## [2026-09-01] ingest | §1.2 Linear algebra + §1.3 Calculus (Strang 18.06, Boyd VMLS, Hefferon, 3Blue1Brown, Strang Calculus)
- Read: VMLS table of contents, 1.5 (flops/floating point), 5.4 (Gram–Schmidt), 12.1 (least squares problem), 13.2 (validation); 18.06 lecture sequence (from memory of OCW; OCW page did not render to text); Strang Calculus chapter list.
- Created sources: strang-18-06, boyd-vmls, hefferon-linear-algebra, 3b1b-essence-of-linear-algebra, strang-calculus.
- Created concepts: vectors-and-inner-products, matrices-and-linear-maps, gaussian-elimination-lu, four-fundamental-subspaces, orthogonality-and-projections, least-squares, eigenvalues-and-eigenvectors, svd-and-pca, k-means-clustering, derivatives-and-gradients, integrals-and-sums.
- Insight: VMLS's "x̂ need not satisfy Ax = b" + its validation section are the cleanest bridge from linear algebra to ML; the least-squares page therefore carries regularization and train/test validation so §6.2 can link back instead of re-deriving.
- Wanted pages added: floating-point, roofline-model, ann-search, dense-retrieval, cache-oblivious-algorithms, pagerank, bias-variance-tradeoff, gradient-descent, convexity, backpropagation, automatic-differentiation, expectation-maximization, monte-carlo-methods.
- Tooling: scripts/fetch.py now strips control characters (grep treated the MCS PDF text as binary before).

## [2026-09-01] ingest | §1.1 Discrete mathematics (MCS, 6.042J, CS70, Levin, Book of Proof)
- Read: MCS ch. 1.9 (good proofs), 5.3–5.4 (induction formats, state machines, Invariant Principle), 9.5 (DAGs & scheduling), 11.6 (stable marriage), 13.7 (asymptotics), 14.8 (pigeonhole), 16.2 (four-step method), 19.1 (Markov); CS70 Fall 2026 schedule; Levin DMOI and Book of Proof tables of contents.
- Created sources: mcs-lehman-leighton-meyer, mit-6-042j, berkeley-cs70, levin-dmoi, hammack-book-of-proof.
- Created concepts: proof-techniques, induction, invariant-principle, propositional-logic, sets-relations-functions, asymptotic-notation, counting-rules, pigeonhole-principle, number-theory-basics, modular-arithmetic, graph-theory-basics, dags-and-partial-orders, stable-matching, recurrences, four-step-method, concentration-inequalities (filed under §1.4).
- Insight: MCS's Invariant Principle + "decreasing derived variable" is the same shape as the Gale–Shapley proof, Euclid's correctness, and every loop-invariant argument; made it a first-class page since it will be linked from OS/DB/distributed pages later.
- Wanted pages created by forward links: amortized-analysis, hash-tables, graph-search, master-theorem, random-variables-expectation, randomized-algorithms (all due in §1.4/§3.x).
- Open question: CS70's polynomials/secret-sharing/Reed–Solomon unit has no page yet; cover it in §5.3 or §11.x (coding theory).


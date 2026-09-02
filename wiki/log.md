# Log

Newest first. Generated from wiki/log/*.md — do not edit.

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


# Log

Newest first. Generated from wiki/log/*.md — do not edit.

---
title: Ingest §2.4 functional programming
type: log
section: "2.4"
tags: [ingest, functional-programming, ocaml, hughes, wadler, okasaki, backus]
summary: Read Hughes (folds, lazy glue), Wadler (monadic evaluator, laws), Okasaki (persistence vs amortization), CS3110 (fold derivation, functors); wrote 7 concept pages incl. wanted algebraic-data-types and amortized-analysis.
---
## [2026-09-02] ingest | §2.4 Functional programming

Read: Hughes §3–4 (foldr derivation, map as fold, treeof, Newton–Raphson/within/relative,
differentiation with elimerror), Wadler §2.2–2.9 and §3 (the three variations, monadic evaluator,
laws), Okasaki front matter and ToC (multiple futures, banker's/physicist's, scheduling, lazy
rebuilding), CS3110 4.3 (fold from sum/concat) and 5.9 (functors are functions, not `extends`).
Backus from memory.

Sources: [[cs3110-ocaml]], [[hughes-why-fp-matters]], [[wadler-monads]],
[[okasaki-purely-functional-data-structures]], [[backus-can-programming-be-liberated]].
Concepts: [[algebraic-data-types]] (wanted → filled), [[fold-and-structural-recursion]], [[monads]],
[[ml-modules-and-functors]], [[persistent-data-structures]], [[amortized-analysis]] (wanted → filled),
[[purity-and-referential-transparency]]; appended a Hughes section to [[streams-and-lazy-evaluation]].

Insights: fold = catamorphism = "one function per constructor" = the design recipe's template =
structural induction's computational twin (links §1.1 ↔ §2.1 ↔ §2.4). Okasaki's "multiple futures"
is the cleanest statement of why amortized bounds assume linear use; laziness + memoization repairs
it. Wadler's "the type M indicates the effect" is the lineage of Rust's `Result`/`?`.
Newly wanted: balanced-search-trees, union-find, parsing, mapreduce-and-dataflow, clrs (source).

---
title: Ingest §2.3 systems programming in C/C++ and Rust
type: log
section: "2.3"
tags: [ingest, c, rust, csapp, cs107, cs110l]
summary: Ingested CSAPP/15-213, CS107, the Rust Book + CS110L, Modern C + K&R; wrote 9 concept pages on pointers, memory layout, integers, UB, allocation, calling conventions, generic C, ownership, traits, memory safety.
---
## [2026-09-02] ingest | §2.3 Systems programming in C/C++ and Rust

Read: Rust Book ch. 4.1 (ownership, stack/heap), CS107 lecture list and assignments, CS110L syllabus,
Modern C table of contents (C23 edition), 15-213 Fall schedule. CSAPP chapter knowledge from memory
(the book is not freely downloadable; the site has slides/labs).

Wrote sources: [[csapp-15-213]], [[stanford-cs107]], [[rust-book]], [[modern-c-gustedt]].
Concepts: [[pointers-and-memory]], [[memory-layout-stack-heap]], [[integer-representation-and-bits]],
[[undefined-behavior]], [[dynamic-memory-allocation]], [[calling-conventions-and-the-stack]],
[[function-pointers-and-generic-c]], [[ownership-and-borrowing]], [[rust-traits-generics-lifetimes]],
[[memory-safety-and-buffer-overflows]].

Insights recorded: the same layout knowledge (frame = return address above locals) explains
debugging, performance, FFI, and stack smashing — one page serves four sections. Rust's rules are the
discipline good C already follows; C's `void*` + function pointer is a hand-built trait object.
Filled wanted pages: pointers-and-memory, undefined-behavior. Newly wanted: linking-and-loading,
garbage-collection, compiler-optimizations, caches-and-memory-hierarchy, virtual-memory, isa-and-assembly
(all §4), error-handling-strategies, algebraic-data-types, fuzzing, security-principles.

## [2026-09-02] ingest | §2.2 Program design & software construction (MIT 6.102 readings, Ousterhout, Effective Java)
- Read: 6.102 Spring 2025 reading list; readings 04 Specifications (behavioural equivalence, requires/effects, the S-T-I-C-I ordering exercise), 05 Designing Specifications (deterministic vs underdetermined, declarative vs operational, strength), 07 AF & RI (ADTs preserve their own invariants, rep exposure, Tweet example), 08 Interfaces & Subtyping (subtype = satisfies the spec; subclassing ≠ subtyping), 10 Equality (equivalence relation, AF-defined equality).
- Created sources: mit-6-102-software-construction, ousterhout-philosophy-of-software-design, effective-java.
- Created concepts: specifications-and-invariants, abstract-data-types-and-rep-invariants, liskov-substitution, equality-and-hashing, unit-testing, code-review, managing-complexity-in-software-design, modularity-and-information-hiding.
- Contradiction recorded: 6.102 "fail fast" vs Ousterhout "define errors out of existence" — resolved as a layering decision in specifications-and-invariants.
- Insight: the rep invariant is the Invariant Principle (§1.1) applied to objects, and spec strength ordering *is* Liskov substitution; the pages cross-link so a search for either finds both.
- Wanted pages: property-based-testing, software-architecture-styles, design-patterns, type-systems, algebraic-data-types.

## [2026-09-02] ingest | §2.1 Introduction to programming (SICP, Composing Programs/CS61A, HtDP, CS50, Think Python)
- Read: SICP contents; 2.1.2 (abstraction barriers), 2.2.3 (sequences as conventional interfaces — the enumerate/map/filter/accumulate signal-flow figure), 3.1.3 (costs of introducing assignment — make-simplified-withdraw vs make-decrementer); Composing Programs 3ed intro and chapter list; HtDP 2e table of contents.
- Created sources: sicp, composing-programs, htdp, harvard-cs50, think-python.
- Created concepts: substitution-and-environment-models, recursion-and-iteration, higher-order-functions, data-abstraction, assignment-state-and-environments, streams-and-lazy-evaluation, interpreters-eval-apply, design-recipe, debugging, objects-and-classes.
- Insight: SICP's "sequences as conventional interfaces" is the same idea as MapReduce, Rust iterators and SQL pipelines; and its "costs of assignment" section is the clearest argument for the pure-core/impure-shell design that §2.2/§2.4 pages will rely on. HtDP's template step is structural induction as a coding discipline — linked to [[induction]].
- Wanted pages: functional-programming-principles, specifications-and-invariants, algebraic-data-types, persistent-data-structures, lambda-calculus, compiler-pipeline, bytecode-and-virtual-machines, parsing, unit-testing, delta-debugging, undefined-behavior, pointers-and-memory, binary-search, liskov-substitution, design-patterns, mapreduce, synchronization-primitives, dynamic-programming.

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


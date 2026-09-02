# Log

Newest first. Generated from wiki/log/*.md — do not edit.

---
title: Ingest §4.2 operating systems
type: log
section: "4.2"
tags: [ingest, operating-systems, ostep, xv6, lampson]
summary: Read OSTEP ch. 2 (virtualization framing), 18 (paging), 26 (threads), 7 (scheduling), Lampson's Hints intro; UNIX paper URL gone; wrote 7 concept pages and 3 sources.
---
## [2026-09-02] ingest | §4.2 Operating systems

Read: OSTEP intro (the crux: how to virtualize; OS as virtual machine, standard library,
resource manager), paging intro (fixed-size pieces vs segmentation's fragmentation), threads
intro (multiple PCs sharing an address space; TCB; the stack per thread), scheduling intro
(workload assumptions relaxed one at a time), Lampson's Hints §1–2 (interfaces: simple, complete,
fast — the hardest part of design). Ritchie–Thompson at bell-labs.com returned 410; written from
memory. xv6 book structure from the 6.1810 site (memory).

Sources: [[ostep]], [[xv6-and-6-1810]], [[os-seminal-papers]]. Concepts: [[processes-and-threads]],
[[limited-direct-execution-and-syscalls]], [[cpu-scheduling]], [[virtual-memory]],
[[synchronization-primitives]], [[file-systems]], [[os-kernels-and-virtualization]] (filled wanted:
processes-and-threads, virtual-memory, synchronization-primitives, file-systems).

Insights: OSTEP's three pieces are three uses of one trick — a trap plus a table (trap table,
page table, lock word) — and "limited direct execution" is the OS version of Rust's zero-cost
abstractions: run at full speed, pay only at the boundary. LFS → FTL → LSM tree is one design
lineage; WAL appears in file systems, databases, and Git's reflog. Lampson's "interface = the
assumptions each side must make" matches Parnas and Liskov exactly.
Newly wanted: io-and-device-drivers, async-and-event-driven-concurrency, transactions-and-concurrency-control,
storage-engines-and-indexes, queueing-theory, garbage-collection, distributed-systems-basics.

---
title: Ingest §4.1 computer architecture and organization
type: log
section: "4.1"
tags: [ingest, computer-architecture, cod, nand2tetris, risc-v]
summary: Nand2Tetris project list read; ACM-hosted papers (Golden Age, RISC) 403'd so written from knowledge; 7 concept pages (ISA, digital logic, pipelining, caches, performance/Amdahl, parallel architectures, coherence/consistency) and 3 sources.
---
## [2026-09-02] ingest | §4.1 Computer architecture & organization

Read: Nand2Tetris project list (12 projects, hardware/software halves). Fetch failures: CACM
"A New Golden Age", ACM "Case for the RISC", CS61C schedule (CalNet login) — written from
knowledge with the papers' claims stated from memory (flag for a verification pass).

Sources: [[patterson-hennessy-cod]], [[nand2tetris]], [[architecture-seminal-papers]].
Concepts: [[isa-and-assembly]] (wanted → filled), [[digital-logic-and-the-alu]],
[[pipelining-and-hazards]], [[caches-and-memory-hierarchy]] (wanted → filled),
[[performance-equation-and-amdahl]], [[parallel-architectures-simd-gpu]],
[[cache-coherence-and-memory-consistency]].

Insights: three "clocks" set the limits — the critical path sets the cycle, hazards set CPI,
locality sets memory stalls — and the performance equation gives each a factor. The
Nand2Tetris VM's call/return protocol is the same stack discipline as x86-64's
([[calling-conventions-and-the-stack]]); Spectre is what happens when the ISA contract omits
timing. Consistency models here preview distributed consistency in §5.
Newly wanted: virtual-memory, processes-and-threads, synchronization-primitives (all §4.2),
linking-and-loading, compiler-optimizations, compilers-overview (§4.3), security-principles.

---
title: Ingest §3.4 competitive programming
type: log
section: "3.4"
tags: [ingest, competitive-programming, cph]
summary: Read CPH table of contents; wrote source + 4 concept pages (range queries, CP techniques, number-theory algorithms, computational geometry).
---
## [2026-09-02] ingest | §3.4 Competitive programming & problem solving

Read: CPH contents (30 chapters). Wrote [[competitive-programmers-handbook]] and
[[range-queries-segment-trees-fenwick]], [[competitive-programming-techniques]],
[[number-theory-algorithms]], [[computational-geometry]]. §3 (data structures & algorithms) is
now complete: 3.1–3.4.

Insight: the complexity-budget table (n → target big-O) is the contest form of
[[asymptotic-notation]]; nearly all "tricks" are amortization ([[amortized-analysis]]) or
monotonicity (binary search on the answer, two pointers) in disguise.

---
title: Ingest §3.3 advanced algorithms and data structures
type: log
section: "3.3"
tags: [ingest, cs168, 6.851, williamson-shmoys, approximation, sketching, lsh]
summary: Read CS168 schedule and Williamson–Shmoys §1.1, 6.851 lecture 1 abstract; wrote 5 concept pages (streaming/sketching, similarity search & LSH, approximation algorithms, advanced data structures, consistent hashing) and 3 sources incl. a classic-papers page.
---
## [2026-09-02] ingest | §3.3 Advanced algorithms & data structures

Read: CS168 full lecture schedule (10 weeks, week-per-idea), Williamson–Shmoys §1.1 ("Fast.
Cheap. Reliable. Choose two"; Definition 1.1; why study approximation) and the ToC (set cover as
the tour of techniques), 6.851 L1 (persistence: partial/full/confluent/functional; DSST node
copying; retroactivity mention). Fetched the W&S PDF only after adding `cryptography` to
fetch.py (AES-encrypted PDF).

Sources: [[cs168-modern-algorithmic-toolbox]], [[williamson-shmoys-approximation]],
[[karp-cook-and-classic-papers]]. Concepts: [[streaming-and-sketching]], [[similarity-search-and-lsh]],
[[approximation-algorithms]], [[advanced-data-structures]], [[consistent-hashing]].

Insights: CS168's "property-preserving lossy compression" is the unifying phrase for Bloom,
count-min, MinHash, JL and LSH — decide the query first, then compress. Approximation proofs
always compare against a computable bound on OPT (LP value/dual), never OPT — the same move as
lower bounds in [[sorting]]. The hybrid search in oasis itself is an instance of
[[similarity-search-and-lsh]] + BM25 with RRF, which I noted on the similarity page.
Newly wanted: search-engines-and-ranking, online-learning-and-regret, replication-and-partitioning,
distributed-systems-basics, augmented-data-structures.

---
title: Ingest §3.2 algorithms
type: log
section: "3.2"
tags: [ingest, algorithms, erickson, clrs, dpv, kleinberg-tardos, roughgarden]
summary: Read Erickson ch. 1 (reductions, Recursion Fairy), ch. 3 (DP recipe), ch. 4 (exchange-argument pattern); wrote 12 concept pages (DP, D&C, greedy, graph search, shortest paths, MST, sorting, flow, NP-completeness, randomized, strings, FFT) and 5 source pages.
---
## [2026-09-02] ingest | §3.2 Algorithms

Read: Erickson 1.1–1.2 (reductions are black boxes; recursion = simplify and delegate; the
Recursion Fairy is the induction hypothesis), 3.4 (the two-stage DP pattern with its six
mechanical steps; "not about filling in tables"), 4.x (general greedy proof pattern: first
difference + exchange). CLRS, DPV, K&T, Skiena, Roughgarden from memory.

Sources: [[erickson-algorithms]], [[clrs]] (wanted → filled), [[dpv-algorithms]],
[[kleinberg-tardos-skiena]], [[roughgarden-algorithms-illuminated]].
Concepts: [[dynamic-programming]], [[divide-and-conquer]], [[greedy-algorithms]], [[graph-search]],
[[shortest-paths]], [[minimum-spanning-trees]], [[sorting]], [[network-flow]],
[[np-completeness-and-reductions]], [[randomized-algorithms]], [[string-algorithms]], [[fft]]
(filled wanted: dynamic-programming, sorting, graph-search, randomized-algorithms, shortest-paths,
minimum-spanning-trees, string-algorithms, master-theorem → covered in divide-and-conquer).

Insights: the three design paradigms line up with three proof shapes — DP with induction over a
subproblem DAG, greedy with exchange arguments, D&C with recurrences; and "memoization is DFS" ties
[[dynamic-programming]] to [[graph-search]] (DPV's "DP = DAG in topological order"). Relaxation
unifies every shortest-path algorithm; reductions unify D&C (to itself), NP-hardness (to a known
problem) and flow (from everything else).
Newly wanted: complexity-classes, search-algorithms-ai, streaming-and-sketching, cryptography-basics,
linear-programming (exists as linear-programming-and-duality), stable-matching (exists).

---
title: Ingest §3.1 data structures
type: log
section: "3.1"
tags: [ingest, data-structures, sedgewick, ods, cs61b]
summary: Read Sedgewick booksite 1.5 union-find, 3.3 balanced trees, 3.4 hash tables; wrote 8 concept pages filling long-wanted hash-tables, balanced-search-trees, union-find, plus 3 sources.
---
## [2026-09-02] ingest | §3.1 Data structures

Read: Sedgewick booksite 1.5 (union-find implementations and cost model), 3.3 (2-3 trees, LLRB
encoding, rotations), 3.4 (hash functions, uniform hashing assumption, chaining). ODS, CS61B,
6.006 from memory.

Sources: [[sedgewick-algorithms-4e]], [[open-data-structures-morin]], [[berkeley-cs61b]].
Concepts: [[hash-tables]] (wanted, 12 inbound), [[balanced-search-trees]], [[union-find]],
[[binary-search-trees]], [[heaps-and-priority-queues]], [[arrays-and-linked-lists]], [[tries]],
[[graph-representations]].

Insights: the three "guarantee" mechanisms for logarithmic height — structural (2-3/B-tree
splitting), randomized (treap/skip list), amortized (splay/scapegoat) — mirror the three proof
styles in [[amortized-analysis]] and [[probabilistic-analysis-of-algorithms]]. Union-find's weighting
argument ("each link doubles your tree") is the same doubling argument as dynamic arrays.
Newly wanted: clrs (source), sorting, graph-search, shortest-paths, minimum-spanning-trees,
string-algorithms, augmented-data-structures, storage-engines-and-indexes.

---
title: Ingest §2.6 developer tooling (Missing Semester)
type: log
section: "2.6"
tags: [ingest, shell, git, make, debugging, profiling]
summary: Read Missing Semester lectures 1, 2, 6, 7; wrote sources for Missing Semester, Pro Git, TLCL/Make/Agans and concept pages on shell tools, git data model, build systems, profiling, text wrangling; enriched debugging.
---
## [2026-09-02] ingest | §2.6 Developer tooling

Read: Missing Semester — course overview/shell (`$PATH`, quoting), shell tools (variables, special
variables, exit codes, command/process substitution), version control (the data model as
pseudocode: blob/tree/commit, content addressing, references, HEAD, staging), debugging & profiling
(logs, pdb/gdb, strace, profilers). Pro Git, TLCL, Make manual, Agans from memory.

Sources: [[missing-semester]], [[pro-git]], [[tlcl-shotts]]. Concepts: [[shell-and-unix-tools]],
[[git-data-model]], [[build-systems-and-make]], [[profiling-and-performance]] (wanted → filled),
[[text-processing-and-regex]]; appended a tools section to [[debugging]].

Insights: Git's data model is a Merkle DAG — the same content-addressing that appears later in
distributed systems and blockchains; the staging area is orthogonal to the model. Make's dependency
graph is a DAG topological sort ([[dags-and-partial-orders]]) with timestamps as the change
detector — the ancestor of every incremental build system and of dataflow schedulers.

---
title: Ingest §2.5 object-oriented design and design patterns
type: log
section: "2.5"
tags: [ingest, design-patterns, parnas, liskov-wing, fowler, gof]
summary: Read Parnas 1972 (KWIC comparison) and Liskov & Wing 1994 (subtype requirement); GoF/Fowler/Meyer from memory; wrote 5 concept pages and enriched liskov-substitution and modularity pages.
---
## [2026-09-02] ingest | §2.5 OO design & design patterns

Read: Parnas 1972 (modularization 1 vs 2, the five changes, "The Criteria"); Liskov & Wing 1994
§1 (subtype requirement, invariants vs history properties, why contra/covariance is insufficient).
GoF, Head First, Fowler 2nd ed., Meyer OOSC from memory.

Sources: [[parnas-1972-criteria]], [[liskov-wing-1994]], [[gof-design-patterns]], [[fowler-refactoring]].
Concepts: [[design-patterns-catalog]], [[inheritance-vs-composition]], [[polymorphism-and-dispatch]],
[[solid-principles]], [[refactoring]]. Appended sections to [[liskov-substitution]] (formal rules) and
[[modularity-and-information-hiding]] (KWIC).

Insights: the whole section is one idea — isolate the axis of change — stated four ways (Parnas:
hide the decision; GoF: encapsulate what varies; Fowler: remove the smell that makes change
expensive; Liskov: substitutability is what makes the abstraction point safe to rely on).
Patterns table maps each GoF pattern to its FP/modern-language equivalent, linking §2.4 ↔ §2.5.
Newly wanted: profiling-and-performance, effective-java (source), ousterhout-philosophy (source
slug check), mit-6102 (slug check).

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


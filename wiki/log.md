# Log

Newest first. Generated from wiki/log/*.md — do not edit.

---
title: Ingest §5.6 quantum computing
type: log
section: "5.6"
tags: [ingest, quantum, shor, grover, qec, nisq]
summary: Read Aaronson's lecture-note ToC (27 lectures), Shor 1994 and Preskill NISQ abstracts; wrote 3 concepts (quantum-computing was wanted) and 1 combined source. §5 complete.
---
## [2026-09-02] ingest | §5.6 Quantum computing

Read: Aaronson *Introduction to Quantum Information Science* ToC (27 lectures — the arc
from "probability with minus signs" through Bell games to Shor, Grover, BBBV, adiabatic,
QEC); Shor 1994/97 abstract (the extended Church–Turing framing: "a digital computer is
generally believed to be an efficient universal computing device … this may not be true when
quantum mechanics is taken into consideration"); Preskill 2018 abstract (50–100 qubits,
noise limits circuit size). Nielsen & Chuang, de Wolf, Grover, BBBV, Steane/Shor codes,
surface code, threshold theorem, Sycamore, Willow from memory.

Source: [[quantum-computing-texts-and-courses]].
Concepts: [[quantum-computing]] (wanted), [[quantum-algorithms]],
[[quantum-error-correction-and-nisq]].

Insights: Simon → Shor is the same move as Bernstein–Vazirani → Simon: a Fourier transform
over the right group reads out a hidden subgroup, and "which groups" is exactly the line
between broken (abelian: RSA/ECC) and safe (dihedral/lattices) cryptography — §5.3's post-
quantum choice explained by §5.6. BBBV is the quantum Baker–Gill–Solovay: an oracle result
that bounds what the technique can do. Syndrome measurement discretizing continuous errors is
the deepest idea in the section — it's why the classical coding theory of §1.7 carries over
(CSS codes are pairs of classical codes). The threshold theorem is von Neumann 1956 again.
Magic-state distillation makes the T gate the "expensive instruction" of a quantum ISA — a
[[performance-equation-and-amdahl]] cost model for a machine that doesn't exist yet.

§5 (Theory) is now complete: 5.1–5.6.

---
title: Ingest §5.5 formal methods and verification
type: log
section: "5.5"
tags: [ingest, formal-methods, tla-plus, model-checking, smt, abstract-interpretation]
summary: Read Newcombe et al. (AWS formal methods) introduction and "Precise Designs" section, Specifying Systems part I ToC; wrote 4 concepts (all four were wanted slugs) and 2 sources.
---
## [2026-09-02] ingest | §5.5 Formal methods & verification

Read: Newcombe, Rath, Zhang, Munteanu, Brooker & Deardeuff, "Use of Formal Methods at Amazon
Web Services" (2014 preprint; CACM 2015) — intro and "Precise Designs" (testing inadequate
because reachable states are astronomical; Holloway's "accidents are almost always the
result of incorrect estimates of the likelihood"; TLA+ as a ladder of abstraction where
properties and designs are both steps; "the author is forced to think more clearly");
Specifying Systems part I ToC (clock → asynchronous interface → FIFO → caching memory with
linearizability and write-through cache → advice incl. "the grain of atomicity"). Clarke–
Emerson (CMU 404) and Cousot 1977 (ENS mirror returned nothing) written from memory, as were
Bryant, Biere, Z3, CompCert, seL4, Alloy, CDCL internals.

Sources: [[formal-methods-texts-and-courses]], [[formal-methods-seminal-papers]].
Concepts: [[program-verification]], [[model-checking]], [[sat-and-smt-solvers]],
[[abstract-interpretation]] — all four were long-standing wanted slugs (linked from §4.3
compilers, §4.6 distributed, §5.1–5.4).

Insights: three sections of theory collapse into one operational recipe at AWS — "write
the design in set theory, let TLC enumerate the interleavings" — and the paper's key claim is
about *human probability estimation*, i.e. [[probability-and-statistics-for-cs]] failing at
scale, not about logic. Widening is amortization's mirror image: give up precision to
guarantee termination, the same trade as the RTO timer in [[tcp-reliability-and-congestion-control]]
(bound the wait, accept false suspicion). CDCL's learned clauses are the memoization of
[[dynamic-programming]] applied to search failures. Abstract interpretation is the general
theory of which types (§5.4), dataflow (§4.3), and predicate abstraction (§5.5) are three
domains — a good synthesis candidate. Program verification's TCB argument is the end-to-end
argument once more: the guarantee is only as strong as the layer that states it.
Newly wanted: design-by-contract, property-based-testing, fuzzing, testing-strategies (§7),
linear-programming, security-principles.

---
title: Ingest §5.4 programming language theory and type systems
type: log
section: "5.4"
tags: [ingest, pl-theory, types, lambda-calculus, curry-howard, semantics]
summary: Read Software Foundations' current ToC (note: Coq is now Rocq); PFPL and Wadler PDFs failed to extract; wrote 6 concepts (lambda-calculus, type-systems, curry-howard-correspondence, closures-and-environment-model were wanted) and 2 sources.
---
## [2026-09-02] ingest | §5.4 PL theory & type systems

Read: Software Foundations vol. 1 ToC (Rocq rename; chapter sequence). PFPL 2nd-ed PDF
text extracted but the ToC grep found nothing usable; Wadler "Theorems for Free" PDF has
Type-3 fonts and extracted as noise; Wright–Felleisen at Rice 404. TAPL, PFPL, PLAI, EOPL,
Milner, Reynolds, Plotkin, Steele–Sussman, Griffin, HoTT from memory.

Sources: [[pierce-tapl-and-pl-theory-texts]], [[pl-theory-seminal-papers]].
Concepts: [[lambda-calculus]], [[operational-and-denotational-semantics]], [[type-systems]],
[[polymorphism-and-type-inference]], [[curry-howard-correspondence]],
[[closures-and-environment-model]] — four of six were wanted slugs (the SICP/§2 pages have
been linking to closures-and-environment-model and lambda-calculus since night one).

Insights: progress+preservation is the invariant method again — the type is a loop invariant
over the reduction sequence ([[invariant-principle]]). Curry–Howard makes "Turing-complete
language ⇔ inconsistent logic" a one-line theorem, which reframes the §5.1 strong-
normalization results as consistency proofs. Parametricity is Parnas's information hiding
with a proof attached, and Rice's theorem is why gradual typing has to choose between
soundness and adoption. CPS ≡ SSA closes a loop with §4.3; defunctionalized continuations
≡ the state machines Rust/C# generate for async, closing one with §2.4/§4.4 sockets. The
substructural ladder (weakening/contraction) is the theory behind [[ownership-and-borrowing]]
— finally linked from the formal side.
Newly wanted: program-verification (§5.5 next), sat-and-smt-solvers, model-checking,
abstract-interpretation (§5.5), polynomial-identity-testing, expander-graphs.

---
title: Ingest §5.3 cryptography
type: log
section: "5.3"
tags: [ingest, cryptography, diffie-hellman, boneh-shoup, zero-knowledge, post-quantum]
summary: Read Diffie–Hellman 1976 abstract and §I, Boneh & Shoup's 23-chapter ToC; wrote 5 concepts (cryptography-basics and hash-functions-cryptographic were wanted; hash-functions-and-integrity links redirected) and 2 sources.
---
## [2026-09-02] ingest | §5.3 Cryptography

Read: Diffie & Hellman 1976 abstract and §I ("brink of a revolution"; cheap digital hardware;
teleprocessing needs systems minimizing secure key channels and supplying the equivalent of
a written signature; "changing this ancient art into a science"); Boneh & Shoup ToC (23
chapters in three parts). Joy of Cryptography PDF returned nothing. Katz & Lindell, GMR,
Yao, Regev, Gentry, Groth16, Signal specs, TLS 1.3, Cryptopals from memory.

Sources: [[boneh-shoup-and-crypto-texts]], [[cryptography-seminal-papers]].
Concepts: [[cryptography-basics]] (wanted), [[symmetric-encryption-and-authenticated-encryption]],
[[hash-functions-cryptographic]] (wanted; the alias `hash-functions-and-integrity` was
redirected to it in existing pages), [[public-key-cryptography]],
[[cryptographic-protocols-and-zero-knowledge]].

Insights: the security-game/reduction style is exactly [[interactive-proofs-and-pcp]]'s
completeness/soundness pair pointed at an adversary instead of a prover; Fiat–Shamir is the
random oracle standing in for the verifier — which is why SNARKs are "PCPs plus a hash". Every
deployed catastrophe in the section (two-time pad, GCM nonce reuse, ECDSA nonce reuse) is the
same bug: reusing randomness that the proof assumed fresh — the freshness invariant is to
crypto what [[invariant-principle]] is to loops. Shamir sharing and Reed–Solomon are one
polynomial: erasure coding is secret sharing with the secrecy thrown away. Merkle trees
now link five sections (git, Dynamo anti-entropy, CT, Bitcoin, hashes).
Newly wanted: security-principles (§6? no — §7.x security), quantum-computing (§5.6),
polynomial-identity-testing, expander-graphs, information-theory-basics (check existing slug).

---
title: Ingest §5.2 advanced complexity theory
type: log
section: "5.2"
tags: [ingest, complexity, pcp, circuits, derandomization]
summary: Read Arora & Barak's part-I ToC, Dinur 2007 abstract (graph powering doubles unsat-value), Williams 2011 abstract (NEXP ⊄ ACC via faster SAT algorithms); wrote 4 concepts (complexity-theory-advanced was wanted) and 2 sources.
---
## [2026-09-02] ingest | §5.2 Advanced complexity

Read: Arora & Barak draft front matter and chapter 1–3 section list ("the computational model
— and why it doesn't matter"; "Cook–Levin: computation is local"; "oracle machines and the
limits of diagonalization"); Dinur 2007 abstract + §1 (unsat-value; amplification doubles it
with linear blowup; alphabet growth fixed by composition; expander powering); Williams 2012
abstract (NEXP ⊄ ACC; E^NP lower bounds; "design faster algorithms for circuit satisfiability,
then prove such algorithms entail lower bounds"). Toda, Shamir, Razborov–Rudich, NW/IW,
Reingold from memory. The Princeton COS522 page returned nothing useful.

Sources: [[arora-barak-and-complexity-texts]], [[complexity-theory-seminal-papers]].
Concepts: [[complexity-theory-advanced]] (wanted), [[interactive-proofs-and-pcp]],
[[circuit-complexity-and-lower-bounds]], [[pseudorandomness-and-derandomization]].

Insights: arithmetization is the through-line — Toda, IP = PSPACE, PCP, and today's SNARKs
all turn a logical statement into a low-degree polynomial identity and then use Schwartz–
Zippel; "computation is local" (Cook–Levin's 2×3 windows) is what makes the polynomial low-
degree. Natural proofs is Rice's theorem's complexity cousin: the property you'd use to
recognize hardness is itself efficiently computable, and that is exactly what makes it
useless. Williams' program inverts the whole field's instinct — the algorithmists prove the
lower bounds. Dinur's gap amplification is Cheeger/expander mixing used as an *amplifier*,
the same object that derandomizes random walks and builds extractors.
Newly wanted: expander-graphs, polynomial-identity-testing, quantum-computing (§5.6),
cryptography-basics (§5.3), monte-carlo-methods.

---
title: Ingest §5.1 automata, computability and complexity
type: log
section: "5.1"
tags: [ingest, theory, turing, sipser, barak, p-vs-np]
summary: Read Turing 1936 §1 (the model's justification), 18.404 lecture list, Barak's chapter list; wrote 6 concepts (all six were wanted slugs) and 2 sources.
---
## [2026-09-02] ingest | §5.1 Automata, computability & complexity

Read: Turing 1936 abstract and §1 ("computable numbers … calculable by finite means";
"the human memory is necessarily limited"; m-configurations, scanned square, the
justification deferred to §9; equivalence with Church noted); MIT 18.404 Fall 2020 lecture
titles (26); Barak's introtcs chapter list (0–23). Sipser proofs, Cook–Levin tableau, Savitch,
Immerman–Szelepcsényi, Ladner, BGS from memory.

Sources: [[sipser-and-theory-of-computation-courses]], [[theory-of-computation-seminal-papers]].
Concepts: [[finite-automata-and-regular-languages]], [[context-free-grammars]],
[[turing-machines]], [[decidability-and-reductions]], [[complexity-classes]], [[p-vs-np]] —
every one a slug other sections had already linked to (six wanted pages closed).

Insights: one idea, the *locally checkable computation history*, does triple duty — the
computation-history method (undecidability of ALL_CFG, PCP), the Cook–Levin tableau (NP-
completeness of SAT), and TQBF's PSPACE-completeness (Savitch's midpoint recursion as
alternating quantifiers). Diagonalization appears four times (Cantor, halting, time
hierarchy, Ladner) and BGS says exactly where it stops working. Nondeterminism is free for
DFAs, decisive for PDAs, nearly free for space (Savitch), and the whole open question for
time — a nice axis to teach along. Rice's theorem is the formal reason every §4.3 analysis
is an approximation ([[dataflow-analysis]], [[abstract-interpretation]]).

---
title: Ingest §4.9 embedded, real-time and IoT systems
type: log
section: "4.9"
tags: [ingest, embedded, real-time, cps, lee-seshia, liu-layland]
summary: Wrote 3 concepts and 1 source for §4.9 from Lee & Seshia's structure, Valvano, White, Liu & Layland (all from memory — no fetches attempted; the book's ToC is well known). Closes §4.
---
## [2026-09-02] ingest | §4.9 Embedded, real-time & IoT

Written from memory of Lee & Seshia 2nd ed. (chapter structure and the "sequential software
in a concurrent world" framing), Liu & Layland 1973 (RM optimality, n(2^{1/n}−1) bound, EDF
≤ 1), Sha–Rajkumar–Lehoczky priority ceiling, the Pathfinder story, Valvano's register-level
curriculum, White's practitioner checklist, Lee 2008.

Source: [[embedded-systems-texts-and-courses]].
Concepts: [[real-time-scheduling]], [[microcontrollers-and-embedded-programming]],
[[cyber-physical-systems-and-models-of-computation]].

Insights: RM's utilization bound is the embedded cousin of Amdahl — a closed-form ceiling that
tells you when to stop adding tasks; response-time analysis is a fixed-point iteration, the
same shape as [[dataflow-analysis]]. Priority ceiling is deadlock prevention by resource
ordering ([[synchronization-primitives]]) with priorities as the order. Lee's "abstractions
that discard time" complaint is the mirror image of the end-to-end argument: the whole
computing stack was built to hide exactly the property CPS must expose. Kahn networks are
the deterministic core that MapReduce, SDF, and Unix pipes all share — blocking reads on
FIFO channels make scheduling irrelevant to the result.

§4 (Systems) is now complete: 4.1–4.9.

---
title: Ingest §4.8 storage and datacenter systems
type: log
section: "4.8"
tags: [ingest, storage, datacenter, raid, gfs, ssd, sre, cloud]
summary: Read GFS §1 (four workload observations), Schroeder FAST'16 abstract (flash reliability findings), RAID '88 abstract; wrote 7 concepts (raid-and-erasure-coding and io-and-device-drivers were wanted) and 2 sources.
---
## [2026-09-02] ingest | §4.8 Storage & datacenter systems

Read: GFS §1 (failure is the norm; huge files; append-mostly; co-design API with
applications), Schroeder, Lagisetty & Merchant FAST 2016 abstract (RBER linear in P/E; not
predictive; UBER meaningless; SLC ≈ MLC; fewer replacements, more uncorrectable errors than
HDDs), Patterson–Gibson–Katz 1988 abstract and §1 (Amdahl's memory constant, Joy's law, I/O
squandering CPU). WSC book (Morgan & Claypool) timed out; SRE book, Ceph, Haystack, Berkeley
serverless view written from memory.

Sources: [[datacenter-and-sre-books]], [[storage-and-cloud-seminal-papers]].
Concepts: [[raid-and-erasure-coding]] (wanted), [[distributed-file-and-object-storage]],
[[ssd-and-nvme-storage]], [[io-and-device-drivers]] (wanted since §4.2; filed under 4.2),
[[warehouse-scale-computing]], [[site-reliability-engineering]], [[cloud-and-serverless]].

Insights: three storage papers, three answers to "where is the metadata" — central master
(GFS), computed placement (Ceph/CRUSH ≈ consistent hashing with failure domains), packed
index-in-memory (Haystack ≈ an LSM with one level). The FTL is the third reincarnation of
LFS (file system → SSD firmware → LSM engine), and ZNS is the industry admitting it does GC
twice. Schroeder's field results are a lesson in [[probability-and-statistics-for-cs]]:
datasheet models (exponential RBER, UBER) fail against fleet data — measure your own fleet.
SRE's error budget is a control loop on the availability/velocity trade ([[invariant-principle]]
applied to organizations); load shedding and retry budgets are [[queueing-theory]] made
policy. Newly wanted after this section: queueing-theory, markov-chains, microcontrollers-and-
embedded-programming (next section), probability-and-statistics-for-cs.

---
title: Ingest §4.7 parallel and high-performance computing
type: log
section: "4.7"
tags: [ingest, parallel, hpc, cuda, cilk, roofline, lock-free]
summary: Read Herlihy 1991 abstract/intro, CS149 Fall 2024 and 15-418 Spring 2024 schedules, Tail at Scale (from memory; Google pub page returned nav only); wrote 7 concepts (2 wanted slugs) + 3 sources + a 6.172 addendum to profiling-and-performance.
---
## [2026-09-02] ingest | §4.7 Parallel & HPC

Read: Herlihy "Wait-Free Synchronization" abstract + §1 (wait-free definition; reduction to
consensus; registers at the bottom, TAS/FAA weak, universal objects exist); CS149 Fall 2024
schedule (Fatahalian & Olukotun) and 15-418 Spring 2024 schedule; CS267 site (only the
overview loaded). Roofline PDF timed out (Berkeley), "Tail at Scale" page returned only site
navigation — both written from memory. Frigo et al., Blumofe & Leiserson, PMPP, Herlihy &
Shavit, McKenney from memory.

Sources: [[stanford-cs149-and-cmu-15-418]], [[parallel-programming-texts]],
[[parallel-computing-seminal-papers]].
Concepts: [[parallel-programming-models]], [[gpu-programming-cuda]],
[[work-stealing-and-fork-join]], [[lock-free-programming]], [[roofline-model]] (wanted),
[[cache-oblivious-algorithms]] (wanted), [[tail-latency-at-scale]]; addendum to
[[profiling-and-performance]].

Insights: the consensus hierarchy is FLP's shared-memory twin — both say "reads and writes
alone cannot agree", and CAS's infinite consensus number is why it appears in every ISA. Work/
span is Amdahl made compositional (span law = serial fraction), and the greedy bound is the
same shape as list scheduling's 2-approximation ([[approximation-algorithms]]). Roofline and
the external-memory model are two views of one quantity (bytes moved per useful operation);
cache-oblivious recursion is "divide until it fits" — the same move as work stealing's
"divide until parallel slackness", so one recursion buys both locality and parallelism. Tail
latency is the probabilistic Amdahl: the slowest of n draws.

---
title: Ingest §4.6 distributed systems
type: log
section: "4.6"
tags: [ingest, distributed-systems, lamport, raft, flp, 6-824]
summary: Read Lamport 1978 (happens-before definition), Raft §1–2 (properties of practical consensus), FLP abstract, 6.824 Spring 2025 schedule; wrote 8 concepts (3 filling wanted slugs) and 3 sources.
---
## [2026-09-02] ingest | §4.6 Distributed systems

Read: Lamport "Time, Clocks" abstract + §"The Partial Ordering" (definition of →; "a system is
distributed if the message transmission delay is not negligible compared to the time between
events"); Raft §1–2 (decomposition for understandability; the four properties practical
consensus must have — safety under non-Byzantine faults, availability with any majority, no
dependence on timing for safety, one round trip to a majority); FLP abstract; 6.824 Spring
2025 schedule and labs. Paxos, PBFT, Bitcoin, GFS, Borg, Dapper, ZooKeeper, CRDTs, chain
replication from memory.

Sources: [[mit-6-824]], [[distributed-systems-textbooks]], [[distributed-systems-seminal-papers]].
Concepts: [[distributed-systems-basics]], [[time-clocks-and-ordering]], [[consistency-models]],
[[consensus-paxos-raft]], [[replication-and-partitioning]],
[[byzantine-fault-tolerance-and-blockchains]], [[mapreduce-and-dataflow]],
[[cluster-scheduling-and-observability]] — basics / replication-and-partitioning /
mapreduce-and-dataflow fill wanted slugs.

Insights: Lamport's definition of "distributed" is a *ratio* (delay vs event spacing), which is
why a multicore CPU is a distributed system too ([[cache-coherence-and-memory-consistency]]
is consistency-models for hardware). "Any two majorities intersect" is the single fact under
Paxos, Raft, quorum replication and PBFT's 2f+1 — the field is pigeonhole all the way down.
Raft's safety argument (safety needs no timing; liveness does) is FLP's boundary drawn as a
design rule. The replicated log keeps reappearing: ARIES WAL → Raft log → Kafka → CDC — one
data structure, four sections. MapReduce's fault tolerance is possible only because its
functions are pure: [[purity-and-referential-transparency]] as an operational requirement.

---
title: Ingest §4.5 databases
type: log
section: "4.5"
tags: [ingest, databases, codd, aries, 15-445, cap]
summary: Read Codd 1970 (data independence — ordering/indexing/access-path), ARIES abstract+intro (repeating history, LSNs, CLRs), Kleppmann on CAP, 15-445 lecture list; wrote 6 concepts (4 filling wanted slugs) and 3 sources.
---
## [2026-09-02] ingest | §4.5 Databases

Read: Codd §1.1–1.2 (the three dependencies; "connection trap"), ARIES abstract and §1.1
(repeating history, page LSN, CLR chaining, fuzzy checkpoints), Kleppmann "Please stop calling
databases CP or AP" (CAP = linearizability + every-node-answers on a single register), the
15-445 Fall 2024 schedule. Hellerstein's *Architecture of a Database System* 403'd on three
mirrors; written from memory. Silberschatz, DDIA, Dynamo/Bigtable/Spanner from memory.

Sources: [[cmu-15-445]], [[database-textbooks]], [[database-seminal-papers]].
Concepts: [[relational-model]], [[storage-engines-and-indexes]], [[query-optimization]],
[[transactions-and-concurrency-control]], [[database-recovery-and-logging]],
[[distributed-databases-and-nosql]] — the first four fill long-wanted slugs.

Insights: Codd's paper is the end-to-end argument's sibling — it moves *knowledge of
representation* out of programs the way Saltzer et al. move function out of the network; both
are [[modularity-and-information-hiding]]. ARIES's "repeat history, then undo" is the same
shape as a version-control rebase: reconstruct the exact state first, then apply corrective
commits (CLRs) that are themselves history. Conflict serializability is cycle detection in
the precedence graph — the same test as deadlock detection and as the happens-before check in
[[cache-coherence-and-memory-consistency]]. The buffer pool is the OS page cache rebuilt with
application knowledge; every serious engine ends up re-implementing OS services
([[os-kernels-and-virtualization]] — exokernel argument).
Also fixed stale wanted links: tcp / congestion-control → tcp-reliability-and-congestion-control,
design-patterns → design-patterns-catalog, parsing → lexing-and-parsing, compiler-pipeline →
compilers-overview, bytecode-and-virtual-machines → bytecode-vms-and-jit, mapreduce →
mapreduce-and-dataflow.

---
title: Ingest §4.4 computer networks
type: log
section: "4.4"
tags: [ingest, networking, end-to-end, clark, jacobson, cs144]
summary: Read Saltzer–Reed–Clark, Clark 1988 (goals in order), Jacobson 1988 (packet conservation), Systems Approach ToC; wrote 6 concept pages and 3 sources.
---
## [2026-09-02] ingest | §4.4 Computer networks

Read: end-to-end arguments (abstract + the argument's statement + the file-transfer case),
Clark 1988 §2–3 (fundamental goal; second-level goals list), Jacobson 1988 intro (1986
collapse; seven algorithms; packet conservation), Peterson & Davie chapter list. K&R, CS144,
HPBN, Beej, RFCs, BBR/QUIC/OpenFlow/DCTCP from memory.

Sources: [[networking-textbooks]], [[stanford-cs144]], [[networking-seminal-papers]].
Concepts: [[internet-architecture-and-layering]], [[tcp-reliability-and-congestion-control]],
[[ip-routing-and-forwarding]], [[link-layer-and-lans]], [[dns-http-and-the-web-stack]],
[[sockets-programming]].

Insights: the end-to-end argument is Parnas's information hiding applied across a network
boundary (put the function where the knowledge is); Clark's ordered goals are a worked example of
design-by-priority — the same move as SOLID's "one reason to change" but for a whole
architecture; Jacobson's packet conservation is a flow invariant ([[invariant-principle]]),
and AIMD's convergence is a tiny dynamical-systems proof. Every web-protocol revision is
round-trip elimination — latency, not bandwidth, is the lesson HPBN hammers.
Newly wanted: queueing-theory, async-and-event-driven-concurrency, cryptography-basics,
security-principles, web-application-architecture, distributed-systems-basics.

---
title: Ingest §4.3 compilers
type: log
section: "4.3"
tags: [ingest, compilers, crafting-interpreters, cs6120, ssa, dragon-book]
summary: Read Crafting Interpreters ch. 2 (the map), CS6120 lesson list, SSA Book contents; wrote 9 concept pages (overview, lexing/parsing, IR/SSA, dataflow, optimizations, codegen/regalloc, GC, VMs/JIT, linking) and 4 sources.
---
## [2026-09-02] ingest | §4.3 Compilers

Read: Crafting Interpreters "A Map of the Territory" (the mountain; where analysis results live;
front/middle/back end; shortcuts), CS6120 self-guided lesson list (14 lessons), SSA Book ToC
(construction via dominance frontiers; properties; destruction). Dragon Book, Appel, Cooper &
Torczon, LLVM, Self/Smalltalk papers from memory.

Sources: [[crafting-interpreters]], [[dragon-book-and-compiler-texts]], [[cs6120-and-compiler-courses]],
[[compiler-seminal-papers]]. Concepts: [[compilers-overview]], [[lexing-and-parsing]],
[[intermediate-representations-and-ssa]], [[dataflow-analysis]], [[compiler-optimizations]],
[[register-allocation-and-code-generation]], [[garbage-collection]], [[bytecode-vms-and-jit]],
[[linking-and-loading]] (filled wanted: compilers-overview, parsing → lexing-and-parsing,
compiler-optimizations, garbage-collection, linking-and-loading).

Insights: SSA is the compiler's own referential transparency ([[purity-and-referential-transparency]]);
dataflow analysis, type inference and dominators are all fixed points ([[induction]]); the
JIT's measure–guess–guard–recover loop is the same shape as branch prediction and adaptive query
optimization; Bacon's tracing/RC duality is a real unification, not a slogan.
Newly wanted: context-free-grammars, type-systems (§4.4), program-verification, query-optimization,
async-and-event-driven-concurrency, io-and-device-drivers.

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


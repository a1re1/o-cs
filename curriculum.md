# Open Computer Science Curriculum & Corpus Plan
### CS100 → CS500+ across all branches of computing and software engineering

**Purpose.** A comprehensive map of openly available courses, texts, and seminal works that together cover the foundations and every major branch of computer science and software engineering. Designed to (a) be a self-study curriculum and (b) serve as the seed manifest for a CS course-search index.

**How to read levels.**
| Level | Meaning | Typical university mapping |
|---|---|---|
| 100 | Introductory / no prerequisites | CS50, CS61A, 6.100 |
| 200 | Core foundations (data structures, discrete math, systems basics) | CS61B/C, 6.006, 15-213 |
| 300 | Upper-division core (algorithms, OS, networks, DB, compilers, PL, AI) | CS161, 6.033, CS186, CS143 |
| 400 | Advanced undergrad / early grad electives | CS224N, CS231N, 15-440, 6.824 |
| 500 | Graduate seminars, research-paper-driven | 6.858, CS294, reading groups |

Each branch section lists: **Courses** (open), **Texts** (free where possible; canonical otherwise), **Seminal works** (papers worth indexing in full), **Index tags**.

---

## 0. Corpus Construction Notes (read first)

### 0.1 Primary open-course hubs to crawl
- MIT OpenCourseWare (ocw.mit.edu) — 6.xxx courses, lecture notes, psets, exams. CC BY-NC-SA.
- Stanford Engineering Everywhere / Stanford Online (see.stanford.edu, online.stanford.edu) + individual course sites (cs*.stanford.edu).
- UC Berkeley EECS course sites (inst.eecs.berkeley.edu, cs61a.org, cs61b.org, cs161.org, cs186berkeley.net, etc.) — many fully open with autograders.
- CMU course sites (15-xxx) — notes and labs; lectures often on YouTube/Panopto.
- Harvard CS50 family (cs50.harvard.edu) — CS50, CS50 AI, CS50 Web, CS50 SQL, CS50 Cybersecurity, CS50 Python.
- Carnegie Mellon / MIT / Stanford / Princeton on Coursera/edX (audit modes).
- OSSU Computer Science (github.com/ossu/computer-science) — curated path with prerequisites graph; excellent metadata source.
- Teach Yourself CS (teachyourselfcs.com) — 9-subject canonical list; useful for "best single resource" heuristics.
- Open Textbook Library (open.umn.edu/opentextbooks), OpenStax, Green Tea Press, SICP online.
- arXiv (cs.*), ACM Digital Library open-access, USENIX (all papers open), IEEE Xplore open subset, JMLR, PMLR, NeurIPS/ICML/ICLR proceedings (OpenReview), DBLP for metadata.
- Papers We Love (github.com/papers-we-love/papers-we-love) — curated seminal papers by topic.
- The Architecture of Open Source Applications (aosabook.org) — case studies of real systems.
- Awesome-lists (github.com/sindresorhus/awesome) for tooling-level material.

### 0.2 Suggested document metadata schema
```yaml
id: string                  # stable slug, e.g. mit-6.006-2020
title: string
type: course | lecture | lecture_notes | textbook | chapter | paper | problem_set | lab | video | exam | spec | rfc
level: 100 | 200 | 300 | 400 | 500
branch: [foundations, programming, systems, theory, ai, ...]   # multi-valued
topics: [tags]              # fine-grained, from the tag lists below
prerequisites: [ids]
institution: string
authors: [string]
year: int
license: CC-BY | CC-BY-NC-SA | CC-BY-SA | MIT | arXiv-nonexclusive | proprietary-open-access | unknown
url: string
canonical_url: string
format: html | pdf | mp4 | ipynb | md | tex
language: en
duration_hours: float       # est. study time
difficulty: 1-5
has_exercises: bool
has_solutions: bool
summary: string             # 2–4 sentence abstract for retrieval
embedding_chunks: int
```

### 0.3 Licensing guidance
- Index freely: CC-licensed OCW, arXiv, USENIX, RFCs, open textbooks, public GitHub course repos.
- Index metadata + abstract only (link out): ACM/IEEE/Springer paywalled papers, commercial textbooks (CLRS, Tanenbaum, etc.).
- Note NC clauses (MIT OCW is BY-NC-SA) if the index is commercial.

### 0.4 Chunking guidance for retrieval
- Courses → one doc per lecture/unit + one course-level summary doc.
- Textbooks → chapter/section granularity (~1–3k tokens).
- Papers → abstract + section-level chunks; keep figures' captions.
- Preserve prerequisite edges as graph metadata for "what should I learn before X" queries.

---

## 1. Foundations & Mathematics

### 1.1 Discrete Mathematics & Mathematical Reasoning (200)
- **Courses:** MIT 6.042J / 6.1200 Mathematics for Computer Science; Berkeley CS70 Discrete Math & Probability; CMU 15-151 / 21-127 Concepts of Mathematics.
- **Texts:** *Mathematics for Computer Science* (Lehman, Leighton, Meyer — free, MIT); *Discrete Mathematics: An Open Introduction* (Levin — free); *Book of Proof* (Hammack — free); *Concrete Mathematics* (Graham, Knuth, Patashnik).
- **Tags:** logic, proofs, induction, sets, relations, combinatorics, graph-theory, number-theory, modular-arithmetic, probability-discrete.

### 1.2 Linear Algebra (200)
- **Courses:** MIT 18.06 (Strang) + 18.06SC; Gilbert Strang's *Linear Algebra for Everyone* lectures; 3Blue1Brown *Essence of Linear Algebra*.
- **Texts:** *Introduction to Linear Algebra* (Strang); *Linear Algebra Done Right* (Axler); *Linear Algebra* (Hefferon — free); *Introduction to Applied Linear Algebra* (Boyd & Vandenberghe — free).
- **Tags:** vectors, matrices, eigenvalues, SVD, least-squares, orthogonality.

### 1.3 Calculus & Analysis for CS (100–200)
- **Courses:** MIT 18.01 / 18.02; Khan Academy calculus.
- **Texts:** *Calculus* (Strang — free, MIT); *APEX Calculus* (free).
- **Tags:** limits, derivatives, integrals, multivariable, gradients, optimization-basics.

### 1.4 Probability & Statistics (200–300)
- **Courses:** MIT 6.041 / 6.431 Probabilistic Systems Analysis; Harvard Stat 110 (Blitzstein — full lectures open); MIT 18.650 Statistics for Applications; Stanford CS109 Probability for Computer Scientists.
- **Texts:** *Introduction to Probability* (Blitzstein & Hwang — free); *Introduction to Probability* (Bertsekas & Tsitsiklis); *Probability and Statistics for Computer Science* (Forsyth); *All of Statistics* (Wasserman); *Think Stats / Think Bayes* (Downey — free).
- **Tags:** random-variables, distributions, expectation, bayes, markov-chains, estimation, hypothesis-testing, concentration-inequalities.

### 1.5 Logic & Computability (300)
- **Courses:** Stanford CS103 Mathematical Foundations of Computing; Open Logic Project.
- **Texts:** *Open Logic Text* (free); *Logic in Computer Science* (Huth & Ryan); *Forall x* (free).
- **Tags:** propositional-logic, first-order-logic, completeness, incompleteness, decidability.

### 1.6 Optimization & Numerical Methods (300–400)
- **Courses:** Stanford EE364A Convex Optimization (Boyd); MIT 18.335 Numerical Methods; MIT 6.255 Optimization Methods.
- **Texts:** *Convex Optimization* (Boyd & Vandenberghe — free); *Numerical Recipes*; *Numerical Linear Algebra* (Trefethen & Bau).
- **Tags:** convexity, gradient-descent, linear-programming, duality, conditioning, floating-point.

### 1.7 Information Theory (400)
- **Courses:** MIT 6.441; Stanford EE376A; MacKay's Cambridge lectures (open).
- **Texts:** *Information Theory, Inference, and Learning Algorithms* (MacKay — free); *Elements of Information Theory* (Cover & Thomas).
- **Seminal:** Shannon, "A Mathematical Theory of Communication" (1948).
- **Tags:** entropy, mutual-information, channel-capacity, source-coding, kolmogorov-complexity.

---

## 2. Programming & Program Design

### 2.1 Introduction to Programming (100)
- **Courses:** Harvard CS50; MIT 6.100A/B Intro to CS & Programming in Python; Berkeley CS61A Structure & Interpretation of Computer Programs (Python); Stanford CS106A/B; Georgia Tech CS1301.
- **Texts:** *SICP* (Abelson & Sussman — free; also *SICP in JavaScript*); *How to Design Programs* (Felleisen et al. — free); *Think Python* (Downey — free); *Composing Programs* (DeNero — free); *Automate the Boring Stuff* (free).
- **Tags:** variables, control-flow, functions, recursion, abstraction, higher-order-functions, debugging, testing-basics.

### 2.2 Program Design & Software Construction (200)
- **Courses:** MIT 6.102 (ex-6.031) Software Construction (notes fully open); Berkeley CS61B Data Structures (Java); Northeastern CS2500/2510 (HtDP-based).
- **Texts:** 6.102 reading notes; *Effective Java* (Bloch); *Clean Code* (Martin — read critically); *A Philosophy of Software Design* (Ousterhout).
- **Tags:** specifications, abstraction-functions, rep-invariants, immutability, interfaces, testing, code-review.

### 2.3 Systems Programming in C/C++ and Rust (200–300)
- **Courses:** Stanford CS107 Computer Organization & Systems; CMU 15-213 Intro to Computer Systems; Stanford CS110L Safety in Systems Programming (Rust); MIT 6.S081 Rust-related material; Berkeley CS61C.
- **Texts:** *The C Programming Language* (K&R); *Modern C* (Gustedt — free); *Computer Systems: A Programmer's Perspective* (Bryant & O'Hallaron); *The Rust Programming Language* (free); *Rust for Rustaceans*; *A Tour of C++* (Stroustrup).
- **Tags:** pointers, memory-layout, manual-memory, undefined-behavior, ownership, borrow-checker, ABI.

### 2.4 Functional Programming (300)
- **Courses:** University of Washington CS341 / Dan Grossman's *Programming Languages* (Coursera, ML/Racket/Ruby); Cornell CS3110 (OCaml — free textbook); Penn CIS194 Haskell (open); Edinburgh Intro to FP (Haskell).
- **Texts:** *OCaml Programming: Correct + Efficient + Beautiful* (free); *Learn You a Haskell* (free); *Real World Haskell* (free); *Purely Functional Data Structures* (Okasaki); *Programming in Haskell* (Hutton).
- **Seminal:** Backus, "Can Programming Be Liberated from the von Neumann Style?" (1978); Hughes, "Why Functional Programming Matters" (1990); Wadler, "Monads for Functional Programming" (1992).
- **Tags:** immutability, pattern-matching, ADTs, type-inference, monads, laziness, persistent-data-structures.

### 2.5 Object-Oriented Design & Design Patterns (300)
- **Texts:** *Design Patterns* (GoF); *Head First Design Patterns*; *Refactoring* (Fowler); *Object-Oriented Software Construction* (Meyer).
- **Seminal:** Liskov & Wing, "A Behavioral Notion of Subtyping" (1994); Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules" (1972).
- **Tags:** SOLID, patterns, inheritance-vs-composition, polymorphism, modularity.

### 2.6 Developer Tooling ("Missing Semester") (100–200)
- **Courses:** MIT *The Missing Semester of Your CS Education* (fully open).
- **Texts:** *Pro Git* (free); *The Linux Command Line* (Shotts — free); *Debugging* (Agans); GNU Make manual.
- **Tags:** shell, git, vim/editors, make, debugging, profiling, ssh, tmux, regex, package-managers.

---

## 3. Data Structures & Algorithms

### 3.1 Data Structures (200)
- **Courses:** Berkeley CS61B; Stanford CS106B; Princeton COS226 / Coursera *Algorithms I & II* (Sedgewick — open); MIT 6.006 Introduction to Algorithms.
- **Texts:** *Algorithms, 4th ed.* (Sedgewick & Wayne — site free); *Open Data Structures* (Morin — free); *Data Structures and Algorithm Analysis* (Weiss); *Problem Solving with Algorithms and Data Structures using Python* (free).
- **Tags:** arrays, linked-lists, stacks, queues, hash-tables, trees, BST, balanced-trees, heaps, union-find, tries, graphs-basic, amortized-analysis.

### 3.2 Algorithms (300)
- **Courses:** MIT 6.046J Design & Analysis of Algorithms; Stanford CS161; Berkeley CS170 Efficient Algorithms & Intractable Problems; Tim Roughgarden's *Algorithms Illuminated* (lectures free); CMU 15-451.
- **Texts:** *Introduction to Algorithms* (CLRS); *Algorithms* (Dasgupta, Papadimitriou, Vazirani — free draft); *Algorithms* (Jeff Erickson — free); *Algorithm Design* (Kleinberg & Tardos); *The Algorithm Design Manual* (Skiena).
- **Tags:** divide-and-conquer, dynamic-programming, greedy, graph-algorithms, shortest-paths, MST, network-flow, NP-completeness, reductions, randomized-algorithms, string-algorithms, FFT.

### 3.3 Advanced Algorithms & Data Structures (400–500)
- **Courses:** MIT 6.854 Advanced Algorithms; MIT 6.851 Advanced Data Structures (Demaine — fully open video); MIT 6.856 Randomized Algorithms; Stanford CS261 Optimization & Algorithmic Paradigms; Stanford CS168 Modern Algorithmic Toolbox.
- **Texts:** *Randomized Algorithms* (Motwani & Raghavan); *Probability and Computing* (Mitzenmacher & Upfal); *Approximation Algorithms* (Vazirani); *The Design of Approximation Algorithms* (Williamson & Shmoys — free); *Algorithmic Game Theory* (Nisan et al. — free).
- **Seminal:** Karp, "Reducibility Among Combinatorial Problems" (1972); Cook (1971) "The Complexity of Theorem-Proving Procedures"; Dijkstra (1959); Edmonds & Karp (1972); Fredman & Tarjan, Fibonacci heaps (1987); Bloom (1970) "Space/Time Trade-offs in Hash Coding"; Karger's min-cut (1993); Locality-sensitive hashing (Indyk & Motwani 1998).
- **Tags:** streaming, sketching, LSH, linear-programming-algorithms, approximation, online-algorithms, cache-oblivious, succinct-structures, persistence, parallel-algorithms.

### 3.4 Competitive Programming & Problem Solving (200–400)
- **Texts:** *Competitive Programmer's Handbook* (Laaksonen — free); *Competitive Programming 4* (Halim); *Programming Challenges* (Skiena & Revilla).
- **Resources:** Codeforces, AtCoder, LeetCode, USACO Guide (open).
- **Tags:** implementation, bit-manipulation, segment-trees, Fenwick, computational-geometry, number-theory-algos.

---

## 4. Computer Systems

### 4.1 Computer Architecture & Organization (200–400)
- **Courses:** Berkeley CS61C Great Ideas in Computer Architecture; MIT 6.191 (ex-6.004) Computation Structures; Nand2Tetris (nand2tetris.org — fully open); CMU 18-447 Computer Architecture (Mutlu — lectures open); ETH Zürich Digital Design & Computer Architecture (Mutlu — open); Stanford CS149 Parallel Computing; MIT 6.823 Computer System Architecture.
- **Texts:** *Computer Organization and Design: RISC-V Edition* (Patterson & Hennessy); *Computer Architecture: A Quantitative Approach* (Hennessy & Patterson); *The Elements of Computing Systems* (Nisan & Schocken); *Digital Design and Computer Architecture* (Harris & Harris); *Computer Systems: A Programmer's Perspective*.
- **Seminal:** von Neumann, "First Draft of a Report on the EDVAC" (1945); Tomasulo (1967); Patterson & Ditzel, "The Case for the RISC" (1980); Hennessy & Patterson Turing lecture "A New Golden Age for Computer Architecture" (2019); Spectre/Meltdown papers (2018); Dennard scaling / Moore's law papers.
- **Tags:** ISA, RISC-V, pipelining, hazards, caches, memory-hierarchy, virtual-memory, branch-prediction, out-of-order, superscalar, SIMD, GPU-architecture, multicore, coherence, memory-consistency, accelerators, domain-specific-architectures.

### 4.2 Operating Systems (300–400)
- **Courses:** MIT 6.1810 (ex-6.S081) Operating System Engineering (xv6 — fully open); Berkeley CS162; Stanford CS140/CS212 (Pintos); CMU 15-410; Georgia Tech CS6200 (Udacity — free); Wisconsin CS537 (Remzi — lectures open).
- **Texts:** *Operating Systems: Three Easy Pieces* (Arpaci-Dusseau — free); *xv6: a simple, Unix-like teaching OS* (free); *Modern Operating Systems* (Tanenbaum); *Operating System Concepts* (Silberschatz); *Linux Kernel Development* (Love); *The Design and Implementation of the FreeBSD OS*.
- **Seminal:** Ritchie & Thompson, "The UNIX Time-Sharing System" (1974); Dijkstra, "The Structure of the THE Multiprogramming System" (1968); Lampson, "Hints for Computer System Design" (1983); McKusick et al., "A Fast File System for UNIX" (1984); Rosenblum & Ousterhout, LFS (1992); Engler et al., Exokernel (1995); Liedtke, "On µ-Kernel Construction" (1995); Barham et al., Xen (2003); Bugnion et al., Disco (1997); Corbató, Multics; Mach; Plan 9 papers.
- **Tags:** processes, threads, scheduling, synchronization, locks, deadlock, virtual-memory, paging, file-systems, I/O, device-drivers, virtualization, containers, microkernels, RTOS, kernel-security.

### 4.3 Compilers (300–400)
- **Courses:** Stanford CS143 Compilers (open on edX/SEE); Cornell CS6120 Advanced Compilers (Sampson — fully open, LLVM/Bril); MIT 6.035; Berkeley CS164; UW CSE401; KAIST/"Crafting Interpreters"-based courses.
- **Texts:** *Crafting Interpreters* (Nystrom — free); *Compilers: Principles, Techniques, and Tools* (Dragon Book); *Engineering a Compiler* (Cooper & Torczon); *Modern Compiler Implementation in ML/Java/C* (Appel); *SSA Book* (free); *Writing an Interpreter/Compiler in Go* (Ball).
- **Seminal:** Cytron et al., SSA form (1991); Chaitin, graph-coloring register allocation (1982); Lattner & Adve, LLVM (2004); Deutsch & Schiffman, Smalltalk-80 JIT (1984); Hölzle, Self / inline caching; Allen & Cocke on dataflow; Knuth, LR parsing (1965); Proebsting's law; Bacon et al., GC survey; Cheney, copying GC (1970).
- **Tags:** lexing, parsing, LL/LR, ASTs, semantic-analysis, type-checking, IR, SSA, dataflow-analysis, optimization, register-allocation, codegen, JIT, garbage-collection, LLVM, MLIR.

### 4.4 Computer Networks (300–400)
- **Courses:** Stanford CS144 Introduction to Computer Networking (labs open); MIT 6.829 Computer Networks (graduate); Berkeley CS168; Princeton COS461; UW CSE461.
- **Texts:** *Computer Networking: A Top-Down Approach* (Kurose & Ross); *Computer Networks: A Systems Approach* (Peterson & Davie — free); *TCP/IP Illustrated* (Stevens); *High Performance Browser Networking* (Grigorik — free); *Beej's Guide to Network Programming* (free); key RFCs: 791, 793, 2616/9110, 1034/1035, 5246/8446, 7540, 9000.
- **Seminal:** Cerf & Kahn, "A Protocol for Packet Network Intercommunication" (1974); Saltzer, Reed, Clark, "End-to-End Arguments in System Design" (1984); Jacobson, "Congestion Avoidance and Control" (1988); Clark, "The Design Philosophy of the DARPA Internet Protocols" (1988); Floyd & Jacobson, RED (1993); Chord/Kademlia DHTs (2001/2002); Stoica et al.; McKeown et al., OpenFlow (2008); Google BBR (2016); QUIC (2017); Alizadeh et al., DCTCP (2010).
- **Tags:** layering, ethernet, IP, routing, BGP, TCP, congestion-control, DNS, HTTP, TLS, QUIC, SDN, datacenter-networks, wireless, P2P, NAT, CDNs, network-security.

### 4.5 Databases (300–400)
- **Courses:** CMU 15-445/645 Database Systems (Pavlo — fully open); CMU 15-721 Advanced Database Systems; Berkeley CS186 Intro to Database Systems (open); Stanford CS145 / Stanford DB MOOC (Widom); Harvard CS50 SQL; MIT 6.5830 (ex-6.830).
- **Texts:** *Database System Concepts* (Silberschatz); *Database Management Systems* (Ramakrishnan & Gehrke); *Readings in Database Systems* ("Red Book" — free); *Designing Data-Intensive Applications* (Kleppmann); *Architecture of a Database System* (Hellerstein et al. — free); *Transaction Processing* (Gray & Reuter); *Use The Index, Luke* (free).
- **Seminal:** Codd, "A Relational Model of Data for Large Shared Data Banks" (1970); Gray et al., "Granularity of Locks" (1976); Mohan et al., ARIES (1992); Stonebraker & Rowe, POSTGRES (1986); Bayer & McCreight, B-trees (1972); Selinger et al., System R query optimization (1979); Bernstein & Goodman, concurrency control (1981); O'Neil et al., LSM-tree (1996); Stonebraker, "One Size Fits All" (2005); Abadi et al., C-Store (2005); Dean & Ghemawat, MapReduce (2004); Chang et al., Bigtable (2006); DeCandia et al., Dynamo (2007); Corbett et al., Spanner (2012); Zaharia et al., Spark (2012); Bailis et al., HAT; Kleppmann, "Please stop calling databases CP or AP".
- **Tags:** relational-model, SQL, relational-algebra, normalization, storage, B-trees, LSM-trees, indexing, query-processing, query-optimization, joins, transactions, ACID, concurrency-control, MVCC, recovery, ARIES, distributed-databases, NoSQL, column-stores, OLAP, vector-databases, NewSQL.

### 4.6 Distributed Systems (400–500)
- **Courses:** MIT 6.5840 (ex-6.824) Distributed Systems (Raft labs — fully open); Stanford CS244B; CMU 15-440/15-640; Cambridge *Distributed Systems* (Kleppmann — lectures + notes free); Washington CSE452; Princeton COS418.
- **Texts:** *Designing Data-Intensive Applications*; *Distributed Systems* (van Steen & Tanenbaum — free); *Distributed Algorithms* (Lynch); *Introduction to Reliable and Secure Distributed Programming* (Cachin et al.); *Database Internals* (Petrov); MIT 6.824 paper list (itself a curated corpus).
- **Seminal:** Lamport, "Time, Clocks, and the Ordering of Events" (1978); Lamport, "The Part-Time Parliament" (Paxos, 1998) + "Paxos Made Simple" (2001); Ongaro & Ousterhout, Raft (2014); Fischer, Lynch, Paterson, FLP impossibility (1985); Gilbert & Lynch, CAP (2002); Brewer (2000/2012); Lamport, Shostak, Pease, "The Byzantine Generals Problem" (1982); Castro & Liskov, PBFT (1999); Ghemawat et al., GFS (2003); Schneider, state machine replication (1990); Chandra & Toueg, failure detectors (1996); Vogels, "Eventually Consistent" (2009); Shapiro et al., CRDTs (2011); ZooKeeper (2010); Burrows, Chubby (2006); Verma et al., Borg (2015); Dapper (2010); Amazon "Millions of Tiny Databases" (2020); Nakamoto, Bitcoin whitepaper (2008).
- **Tags:** RPC, consistency-models, linearizability, consensus, Paxos, Raft, replication, fault-tolerance, Byzantine, clocks, partitioning, sharding, distributed-transactions, 2PC, CRDTs, cluster-scheduling, MapReduce, stream-processing, blockchains.

### 4.7 Parallel & High-Performance Computing (400)
- **Courses:** Stanford CS149 Parallel Computing (open); CMU 15-418/618 (open); MIT 6.172 Performance Engineering of Software Systems (open, Leiserson); Berkeley CS267 Applications of Parallel Computers (open); UIUC ECE408 / NVIDIA CUDA teaching kit.
- **Texts:** *Programming Massively Parallel Processors* (Kirk & Hwu); *Introduction to Parallel Computing* (Grama et al.); *The Art of Multiprocessor Programming* (Herlihy & Shavit); *Is Parallel Programming Hard...* (McKenney — free); *Structured Parallel Programming*.
- **Seminal:** Amdahl (1967); Gustafson (1988); Herlihy, "Wait-Free Synchronization" (1991); Herlihy & Wing, Linearizability (1990); Blumofe & Leiserson, Cilk work-stealing (1999); Frigo et al., cache-oblivious algorithms (1999); Adve & Gharachorloo, memory consistency tutorial (1996); Lamport, sequential consistency (1979); Dean & Barroso, "The Tail at Scale" (2013); NVIDIA CUDA / Roofline model (Williams et al. 2009).
- **Tags:** shared-memory, message-passing, MPI, OpenMP, CUDA, GPU-programming, lock-free, work-stealing, vectorization, cache-optimization, roofline, performance-engineering, profiling.

### 4.8 Storage & Data Center Systems (400–500)
- **Courses:** MIT 6.5840 paper set; Stanford CS349D Cloud Computing Technology; Berkeley CS262A Advanced Topics in Computer Systems (Hellerstein/Stoica — reading list open).
- **Texts:** *The Datacenter as a Computer* (Barroso, Hölzle, Ranganathan — free); *Site Reliability Engineering* (Google — free); *Building Secure and Reliable Systems* (Google — free).
- **Seminal:** Patterson, Gibson, Katz, RAID (1988); Weil et al., Ceph (2006); Facebook Haystack (2010); Amazon S3 / Dynamo; Google Colossus; Borg / Omega / Kubernetes papers; Serverless papers (Berkeley "Cloud Programming Simplified" 2019).
- **Tags:** RAID, object-storage, distributed-file-systems, SSD/NVMe, cloud, serverless, containers, orchestration, SRE, observability.

### 4.9 Embedded, Real-Time & IoT Systems (300–400)
- **Courses:** Berkeley EECS149 Introduction to Embedded Systems (open); UT Austin EE319K/EE445L (Valvano — open); MIT 6.08.
- **Texts:** *Introduction to Embedded Systems: A Cyber-Physical Systems Approach* (Lee & Seshia — free); *Making Embedded Systems* (White); *Real-Time Systems* (Liu).
- **Seminal:** Liu & Layland, rate-monotonic scheduling (1973); Lee, "Cyber-Physical Systems: Design Challenges" (2008).
- **Tags:** microcontrollers, RTOS, interrupts, timing-analysis, scheduling-real-time, sensors, CPS, FPGA-basics, low-power.

---

## 5. Theory of Computation

### 5.1 Automata, Computability & Complexity (300)
- **Courses:** MIT 18.404J / 6.840J Theory of Computation (Sipser — full lectures open); Stanford CS103 + CS154; Berkeley CS172; Harvard CS121 (notes open).
- **Texts:** *Introduction to the Theory of Computation* (Sipser); *Introduction to Theoretical Computer Science* (Barak — free); *Automata, Computability, and Complexity* (Rich); *Computational Complexity: A Modern Approach* (Arora & Barak — free draft).
- **Seminal:** Turing, "On Computable Numbers" (1936); Church (1936); Rice's theorem (1953); Cook–Levin (1971); Karp (1972); Savitch (1970); Immerman–Szelepcsényi (1988); Ladner (1975); Baker–Gill–Solovay relativization (1975).
- **Tags:** DFA, NFA, regular-languages, context-free, pushdown-automata, Turing-machines, decidability, reductions, P-vs-NP, NP-completeness, PSPACE, hierarchy-theorems.

### 5.2 Advanced Complexity Theory (500)
- **Courses:** MIT 6.841 / 18.405 Advanced Complexity; Berkeley CS278; Stanford CS254; Princeton COS522.
- **Texts:** Arora & Barak; *Computational Complexity* (Papadimitriou); *The Nature of Computation* (Moore & Mertens); Goldreich's texts.
- **Seminal:** PCP theorem (Arora, Safra; Arora, Lund, Motwani, Sudan, Szegedy 1992/1998); Dinur (2007); Razborov–Rudich, "Natural Proofs" (1994); Shamir, IP=PSPACE (1992); Toda's theorem; Valiant #P; Håstad's switching lemma; Impagliazzo's "Five Worlds"; Williams, ACC lower bounds (2011).
- **Tags:** circuit-complexity, interactive-proofs, PCP, hardness-of-approximation, derandomization, pseudorandomness, communication-complexity, fine-grained-complexity, average-case, quantum-complexity.

### 5.3 Cryptography (400–500)
- **Courses:** Stanford CS255 Cryptography (Boneh — Coursera Crypto I/II open); MIT 6.875 Foundations of Cryptography; Berkeley CS276; UMD CMSC456 (Katz).
- **Texts:** *A Graduate Course in Applied Cryptography* (Boneh & Shoup — free); *Introduction to Modern Cryptography* (Katz & Lindell); *The Joy of Cryptography* (Rosulek — free); *Foundations of Cryptography* (Goldreich); *Serious Cryptography* (Aumasson); *Real-World Cryptography* (Wong); *Cryptopals* challenges (free).
- **Seminal:** Diffie & Hellman (1976); Rivest, Shamir, Adleman (1978); Goldwasser & Micali, probabilistic encryption (1984); Goldwasser, Micali, Rackoff, zero-knowledge (1985); Shamir secret sharing (1979); Merkle (1979); Bellare & Rogaway, random oracle (1993); Shor's algorithm (1994); Gentry, FHE (2009); Yao, garbled circuits (1986); Regev, LWE (2005); Groth16 / zk-SNARKs (2016); Signal / Double Ratchet spec; TLS 1.3 RFC 8446.
- **Tags:** symmetric, block-ciphers, hash-functions, MACs, public-key, RSA, elliptic-curves, key-exchange, signatures, provable-security, zero-knowledge, MPC, homomorphic-encryption, post-quantum, lattices, protocols.

### 5.4 Programming Language Theory & Type Systems (400–500)
- **Courses:** CMU 15-312 Foundations of PL (Harper) + 15-814 Types and PL; Penn CIS500 (Software Foundations — Coq); Brown CS1730 (PLAI); MIT 6.820/6.822; Stanford CS242; OPLSS summer school lectures (open); Cornell CS4110/CS6110.
- **Texts:** *Types and Programming Languages* (Pierce); *Software Foundations* (Pierce et al. — free, Coq); *Practical Foundations for PL* (Harper — free draft); *Programming Languages: Application and Interpretation* (Krishnamurthi — free); *Essentials of Programming Languages* (Friedman & Wand); *Concepts, Techniques, and Models of Computer Programming* (Van Roy & Haridi); *Certified Programming with Dependent Types* (Chlipala — free); *Homotopy Type Theory* book (free).
- **Seminal:** Church, lambda calculus (1936); Landin, "The Next 700 Programming Languages" (1966); Milner, "A Theory of Type Polymorphism in Programming" (1978); Reynolds, "Types, Abstraction and Parametric Polymorphism" (1983); Wadler, "Theorems for Free!" (1989); Plotkin, structural operational semantics (1981); Wright & Felleisen, syntactic approach to type soundness (1994); Hindley–Milner; Curry–Howard; Girard's System F; Steele & Sussman "Lambda the Ultimate" papers; Hoare, "Axiomatic Basis" (1969); Reynolds, separation logic (2002).
- **Tags:** lambda-calculus, operational-semantics, denotational-semantics, type-soundness, polymorphism, type-inference, dependent-types, linear-types, effects, continuations, program-verification, Coq, Agda, Lean, Rust-type-system.

### 5.5 Formal Methods & Verification (400–500)
- **Courses:** MIT 6.826 Principles of Computer Systems (Lampson); CMU 15-414 Bug Catching; Stanford CS357; Lean 4 "Theorem Proving in Lean" (free); TLA+ video course (Lamport — free); Dafny tutorials.
- **Texts:** *Software Foundations*; *Model Checking* (Clarke et al.); *Principles of Model Checking* (Baier & Katoen); *Specifying Systems* (Lamport, TLA+ — free); *Concrete Semantics* (Nipkow & Klein — free, Isabelle); *The Little Prover*.
- **Seminal:** Clarke & Emerson / Queille & Sifakis, model checking (1981); Cousot & Cousot, abstract interpretation (1977); Bryant, BDDs (1986); Biere et al., bounded model checking (1999); de Moura & Bjørner, Z3 (2008); Leroy, CompCert (2009); Klein et al., seL4 (2009); Newcombe et al., "How Amazon Web Services Uses Formal Methods" (2015); Jackson, Alloy.
- **Tags:** model-checking, theorem-proving, SAT/SMT, abstract-interpretation, Hoare-logic, separation-logic, refinement, TLA+, verified-compilers, verified-OS, static-analysis.

### 5.6 Quantum Computing (400–500)
- **Courses:** MIT 8.370/18.435; Berkeley CS191; Caltech Ph219 (Preskill notes — free); Qiskit textbook (free); Ronald de Wolf's lecture notes (free); Scott Aaronson's *Quantum Computing Since Democritus* lecture notes (free).
- **Texts:** *Quantum Computation and Quantum Information* (Nielsen & Chuang); *Quantum Computing: An Applied Approach* (Hidary); de Wolf notes; *Quantum Computing for Computer Scientists* (Yanofsky & Mannucci).
- **Seminal:** Deutsch (1985); Shor (1994); Grover (1996); Bennett & Brassard, BB84 (1984); Shor & Steane error correction (1995/96); Kitaev, toric code; Arute et al., "Quantum supremacy" (2019); Preskill, "NISQ" (2018).
- **Tags:** qubits, gates, entanglement, quantum-algorithms, QFT, error-correction, quantum-complexity, quantum-cryptography, NISQ.

---

## 6. Artificial Intelligence & Machine Learning

### 6.1 Introduction to AI (300)
- **Courses:** Berkeley CS188 Artificial Intelligence (fully open); Harvard CS50 AI; MIT 6.034 (Winston — open); Stanford CS221.
- **Texts:** *Artificial Intelligence: A Modern Approach* (Russell & Norvig); *Artificial Intelligence: Foundations of Computational Agents* (Poole & Mackworth — free).
- **Seminal:** Turing, "Computing Machinery and Intelligence" (1950); McCarthy et al., Dartmouth proposal (1955); Newell & Simon, GPS; Hart, Nilsson, Raphael, A* (1968); Pearl, *Heuristics* / Bayesian networks (1988); Minsky, "Steps Toward AI" (1961).
- **Tags:** search, heuristics, A*, adversarial-search, CSPs, logic-agents, planning, Bayes-nets, HMMs, MDPs, reinforcement-learning-basics, agents.

### 6.2 Machine Learning (300–400)
- **Courses:** Stanford CS229 (Ng — notes + lectures open); Andrew Ng Coursera ML Specialization; Caltech CS156 *Learning from Data* (Abu-Mostafa — open); MIT 6.036/6.390 Intro to ML (notes open); Cornell CS4780 (Weinberger — lectures open); CMU 10-701/10-601; Berkeley CS189 (Shewchuk notes free); Google ML Crash Course (free); fast.ai *Practical Deep Learning* (free).
- **Texts:** *An Introduction to Statistical Learning* (James et al. — free, R & Python); *The Elements of Statistical Learning* (Hastie et al. — free); *Pattern Recognition and Machine Learning* (Bishop — free PDF); *Machine Learning: A Probabilistic Perspective* / *Probabilistic Machine Learning* (Murphy — free); *Understanding Machine Learning* (Shalev-Shwartz & Ben-David — free); *Mathematics for Machine Learning* (Deisenroth et al. — free); *Learning from Data* (Abu-Mostafa); *Hands-On ML with Scikit-Learn, Keras & TensorFlow* (Géron).
- **Seminal:** Vapnik & Chervonenkis (1971); Valiant, PAC learning (1984); Cortes & Vapnik, SVM (1995); Breiman, random forests (2001) & "Statistical Modeling: The Two Cultures" (2001); Friedman, gradient boosting (2001); Chen & Guestrin, XGBoost (2016); Dempster et al., EM (1977); Tibshirani, Lasso (1996); Wolpert, no free lunch; Domingos, "A Few Useful Things to Know About ML" (2012).
- **Tags:** supervised, unsupervised, regression, classification, SVM, decision-trees, ensembles, boosting, kernels, clustering, dimensionality-reduction, PCA, EM, bias-variance, generalization, PAC, cross-validation, feature-engineering.

### 6.3 Deep Learning (400)
- **Courses:** Stanford CS231N (vision — open); Stanford CS224N (NLP — open); MIT 6.S191 Intro to Deep Learning (open); NYU Deep Learning (LeCun & Canziani — open); Michigan EECS 498-007 (Johnson — open); UvA Deep Learning notebooks (free); Karpathy *Neural Networks: Zero to Hero* (free); DeepLearning.AI specialization; fast.ai part 2; CMU 11-785.
- **Texts:** *Deep Learning* (Goodfellow, Bengio, Courville — free); *Dive into Deep Learning* (Zhang et al. — free, interactive); *Understanding Deep Learning* (Prince — free); *Neural Networks and Deep Learning* (Nielsen — free); *The Little Book of Deep Learning* (Fleuret — free); *Deep Learning with PyTorch*.
- **Seminal:** McCulloch & Pitts (1943); Rosenblatt, perceptron (1958); Rumelhart, Hinton, Williams, backprop (1986); LeCun et al., LeNet (1998); Hochreiter & Schmidhuber, LSTM (1997); Krizhevsky et al., AlexNet (2012); Simonyan & Zisserman, VGG; He et al., ResNet (2015); Ioffe & Szegedy, BatchNorm (2015); Kingma & Ba, Adam (2014); Srivastava et al., Dropout (2014); Goodfellow et al., GANs (2014); Kingma & Welling, VAEs (2013); Vaswani et al., "Attention Is All You Need" (2017); Bahdanau attention (2014); Zhang et al., "Understanding deep learning requires rethinking generalization" (2017); Frankle & Carbin, lottery ticket (2019); Ho et al., DDPM (2020).
- **Tags:** neural-networks, backpropagation, optimization-SGD, regularization, CNNs, RNNs, LSTMs, attention, transformers, autoencoders, GANs, diffusion-models, normalization, initialization, generalization-theory, PyTorch, JAX.

### 6.4 Natural Language Processing & Large Language Models (400–500)
- **Courses:** Stanford CS224N; Stanford CS324 Large Language Models (notes open); Stanford CS25 Transformers United (open); CMU 11-711 Advanced NLP (Neubig — open); JHU/Stanford CS336 Language Modeling from Scratch (open); Hugging Face NLP Course (free); Karpathy nanoGPT / minGPT.
- **Texts:** *Speech and Language Processing* (Jurafsky & Martin — free draft, 3rd ed.); *Natural Language Processing with Transformers*; *Introduction to Information Retrieval* (Manning et al. — free); *Build a Large Language Model (From Scratch)* (Raschka).
- **Seminal:** Shannon n-gram models; Mikolov et al., word2vec (2013); Pennington et al., GloVe (2014); Sutskever et al., seq2seq (2014); Vaswani et al. (2017); Devlin et al., BERT (2018); Radford et al., GPT-1/2/3 (2018–2020); Kaplan et al., scaling laws (2020); Hoffmann et al., Chinchilla (2022); Ouyang et al., InstructGPT / RLHF (2022); Wei et al., chain-of-thought (2022); Lewis et al., RAG (2020); Hu et al., LoRA (2021); Dao et al., FlashAttention (2022); Touvron et al., LLaMA (2023); Rafailov et al., DPO (2023); Anthropic Constitutional AI (2022); Mixture-of-experts (Shazeer 2017, Fedus 2021); Bai et al. RLAIF; scaling/test-time-compute papers (2024–25).
- **Tags:** tokenization, language-models, embeddings, transformers, pretraining, fine-tuning, RLHF, alignment, prompting, retrieval-augmented-generation, evaluation, scaling-laws, inference-optimization, agents-LLM, multimodal.

### 6.5 Computer Vision (400)
- **Courses:** Stanford CS231N; Michigan EECS 498; UCF CAP5415 (open); Georgia Tech CS4476; UIUC CS543; First Principles of Computer Vision (Nayar, Columbia — open).
- **Texts:** *Computer Vision: Algorithms and Applications* (Szeliski — free); *Multiple View Geometry* (Hartley & Zisserman); *Foundations of Computer Vision* (Torralba, Isola, Freeman); *Computer Vision: Models, Learning, and Inference* (Prince — free).
- **Seminal:** Marr (1982); Canny edge detector (1986); Lowe, SIFT (2004); Viola & Jones (2001); Dalal & Triggs, HOG (2005); Girshick et al., R-CNN → Faster R-CNN; Redmon et al., YOLO (2016); Long et al., FCN; Ronneberger et al., U-Net (2015); Dosovitskiy et al., ViT (2020); Radford et al., CLIP (2021); Mildenhall et al., NeRF (2020); Kirillov et al., SAM (2023); Rombach et al., Stable Diffusion (2022).
- **Tags:** image-formation, filtering, features, segmentation, detection, tracking, stereo, structure-from-motion, 3D-reconstruction, NeRF, vision-transformers, generative-vision.

### 6.6 Reinforcement Learning (400–500)
- **Courses:** UCL/DeepMind RL (Silver — open); Berkeley CS285 Deep RL (Levine — open); Stanford CS234 (open); Hugging Face Deep RL course (free); OpenAI *Spinning Up* (free).
- **Texts:** *Reinforcement Learning: An Introduction* (Sutton & Barto — free); *Algorithms for RL* (Szepesvári — free); *Bandit Algorithms* (Lattimore & Szepesvári — free).
- **Seminal:** Bellman (1957); Watkins, Q-learning (1989); Sutton, TD learning (1988); Williams, REINFORCE (1992); Mnih et al., DQN (2015); Silver et al., AlphaGo/AlphaZero (2016/2017); Schulman et al., TRPO/PPO (2015/2017); Lillicrap et al., DDPG; Haarnoja et al., SAC (2018); Auer et al., UCB (2002); Ng & Russell, inverse RL (2000); Chen et al., Decision Transformer (2021).
- **Tags:** MDPs, dynamic-programming, Monte-Carlo, TD, Q-learning, policy-gradients, actor-critic, exploration, bandits, model-based-RL, offline-RL, multi-agent, RLHF.

### 6.7 Probabilistic Graphical Models & Bayesian Methods (500)
- **Courses:** Stanford CS228 (notes open); CMU 10-708 (open); MIT 6.438.
- **Texts:** *Probabilistic Graphical Models* (Koller & Friedman); *Bayesian Reasoning and Machine Learning* (Barber — free); *Bayesian Data Analysis* (Gelman et al. — free); *Gaussian Processes for ML* (Rasmussen & Williams — free); *Information Theory, Inference, and Learning Algorithms* (MacKay — free).
- **Seminal:** Pearl (1988); Lauritzen & Spiegelhalter (1988); Jordan et al., variational inference (1999); Blei et al., LDA (2003); Metropolis–Hastings (1953/1970); Geman & Geman, Gibbs (1984); Neal, HMC (2011); Hoffman & Gelman, NUTS (2014).
- **Tags:** Bayesian-networks, Markov-random-fields, exact-inference, variational-inference, MCMC, Gaussian-processes, causal-inference, latent-variable-models.

### 6.8 Learning Theory & Statistical Learning (500)
- **Courses:** MIT 9.520 Statistical Learning Theory; Stanford STATS214/CS229M (Ma — notes open); CMU 10-715; Berkeley CS281A.
- **Texts:** Shalev-Shwartz & Ben-David; *Foundations of Machine Learning* (Mohri et al. — free); *High-Dimensional Probability* (Vershynin — free); *High-Dimensional Statistics* (Wainwright); *Prediction, Learning, and Games* (Cesa-Bianchi & Lugosi).
- **Seminal:** VC theory; Bartlett & Mendelson, Rademacher complexity (2002); Belkin et al., double descent (2019); Jacot et al., NTK (2018); Kearns & Valiant; boosting theory (Schapire 1990, Freund & Schapire 1997).
- **Tags:** PAC, VC-dimension, Rademacher, uniform-convergence, online-learning, regret, implicit-regularization, NTK, double-descent.

### 6.9 ML Systems, MLOps & Data Engineering (400)
- **Courses:** Stanford CS329S ML Systems Design (Huyen — notes open); CMU 10-714 Deep Learning Systems (open — build a framework from scratch); Berkeley CS294 AI-Sys reading list; Full Stack Deep Learning (free); MIT 6.5940 TinyML & Efficient DL (Han — open); Made With ML (free).
- **Texts:** *Designing Machine Learning Systems* (Huyen); *Machine Learning Engineering* (Burkov — free); *Fundamentals of Data Engineering* (Reis & Housley); *Efficient Deep Learning* (Lakshmanan et al.).
- **Seminal:** Sculley et al., "Hidden Technical Debt in ML Systems" (2015); Abadi et al., TensorFlow (2016); Paszke et al., PyTorch (2019); Chen et al., TVM (2018); Shoeybi et al., Megatron-LM; Rajbhandari et al., ZeRO (2020); Narayanan et al., pipeline parallelism; Kwon et al., vLLM/PagedAttention (2023); Frantar et al., GPTQ; Dettmers, QLoRA.
- **Tags:** training-infrastructure, distributed-training, data-pipelines, feature-stores, model-serving, inference-optimization, quantization, compilers-for-ML, monitoring, experiment-tracking, data-quality.

### 6.10 Robotics & Autonomous Systems (400)
- **Courses:** MIT 6.4210/6.4212 Robotic Manipulation (Tedrake — free text); MIT 6.832 Underactuated Robotics (Tedrake — free text); Stanford CS223A; Berkeley CS287; UPenn Robotics MOOC; Coursera Self-Driving Cars (Toronto).
- **Texts:** *Probabilistic Robotics* (Thrun, Burgard, Fox); *Modern Robotics* (Lynch & Park — free); *Planning Algorithms* (LaValle — free); *Robotic Manipulation* & *Underactuated Robotics* (Tedrake — free).
- **Seminal:** Kalman (1960); Smith, Self, Cheeseman, SLAM (1990); Thrun et al., Monte Carlo localization; LaValle, RRT (1998); Kavraki et al., PRM (1996); Levine et al., end-to-end visuomotor (2016); Brooks, subsumption architecture (1986).
- **Tags:** kinematics, dynamics, control, state-estimation, Kalman-filters, SLAM, motion-planning, manipulation, perception, learning-for-robotics.

### 6.11 AI Safety, Alignment, Ethics & Fairness (400–500)
- **Courses:** Stanford CS384 / CS221 ethics modules; MIT 6.S898; Berkeley CS294 Responsible AI; AI Safety Fundamentals (BlueDot — open); Fairness & ML book course (Barocas, Hardt, Narayanan — free).
- **Texts:** *Fairness and Machine Learning* (free); *The Alignment Problem* (Christian); *Human Compatible* (Russell); *Interpretable Machine Learning* (Molnar — free).
- **Seminal:** Amodei et al., "Concrete Problems in AI Safety" (2016); Bostrom / Russell foundational essays; Dwork et al., "Fairness Through Awareness" (2012); Hardt et al., equality of opportunity (2016); Ribeiro et al., LIME (2016); Lundberg & Lee, SHAP (2017); Anthropic interpretability series (circuits, superposition, scaling monosemanticity); Christiano et al., RL from human preferences (2017); Bender et al., "Stochastic Parrots" (2021); Bommasani et al., foundation models report (2021).
- **Tags:** alignment, interpretability, mechanistic-interpretability, robustness, adversarial-examples, fairness, privacy-ML, differential-privacy, governance, evaluation-benchmarks.

---

## 7. Software Engineering

### 7.1 Software Engineering Fundamentals (300)
- **Courses:** Berkeley CS169 Software Engineering (open, SaaS-oriented); MIT 6.102; CMU 17-313 Foundations of SE (open); UW CSE403; Georgia Tech CS3300.
- **Texts:** *Software Engineering at Google* (free); *Engineering Software as a Service* (Fox & Patterson); *The Mythical Man-Month* (Brooks); *Code Complete* (McConnell); *The Pragmatic Programmer*; *Software Engineering* (Sommerville).
- **Seminal:** Brooks, "No Silver Bullet" (1986); Parnas (1972); Royce, waterfall (1970); Agile Manifesto (2001); Conway (1968); Lehman's laws (1980); Boehm, spiral model (1988); DeMarco & Lister, *Peopleware*.
- **Tags:** requirements, specification, design, modularity, process, agile, estimation, code-review, technical-debt, maintenance, documentation.

### 7.2 Testing, Debugging & Program Analysis (300–400)
- **Courses:** Udacity Software Testing / Software Debugging (Zeller — free); CMU 17-355 Program Analysis (open notes); Georgia Tech CS6340 Software Analysis (Udacity — free).
- **Texts:** *The Debugging Book* & *The Fuzzing Book* (Zeller et al. — free, interactive); *Introduction to Software Testing* (Ammann & Offutt); *Effective Software Testing* (Aniche); *Why Programs Fail* (Zeller).
- **Seminal:** Zeller, delta debugging (2002); Claessen & Hughes, QuickCheck (2000); Miller et al., fuzz testing (1990); Godefroid et al., DART (2005); Cadar et al., KLEE (2008); AFL / libFuzzer; Beizer; mutation testing (DeMillo et al. 1978); Google's "Flaky tests" & "Testing on the Toilet".
- **Tags:** unit-testing, integration-testing, property-based-testing, mutation-testing, fuzzing, symbolic-execution, static-analysis, dynamic-analysis, coverage, debugging-techniques, test-oracles.

### 7.3 Software Architecture & System Design (400)
- **Courses:** CMU 17-655 Architectures for Software Systems; system-design primer (github.com/donnemartin/system-design-primer — open); Berkeley CS169 architecture units.
- **Texts:** *Designing Data-Intensive Applications*; *Software Architecture in Practice* (Bass et al.); *Fundamentals of Software Architecture* (Richards & Ford); *Clean Architecture* (Martin); *Domain-Driven Design* (Evans); *Building Microservices* (Newman); *Release It!* (Nygard); *Patterns of Enterprise Application Architecture* (Fowler); *The Architecture of Open Source Applications* vols 1–2 + *500 Lines or Less* (free).
- **Seminal:** Fielding, REST dissertation (2000); Garlan & Shaw, "An Introduction to Software Architecture" (1993); Kruchten, 4+1 view model (1995); Hohpe & Woolf, *Enterprise Integration Patterns*; Helland, "Life beyond Distributed Transactions" (2007); Fowler, "Microservices" (2014).
- **Tags:** architecture-styles, REST, microservices, monoliths, event-driven, CQRS, message-queues, caching, load-balancing, scalability, resilience-patterns, API-design, domain-modeling.

### 7.4 DevOps, CI/CD, SRE & Infrastructure (300–400)
- **Texts:** *Site Reliability Engineering* + *SRE Workbook* (Google — free); *Accelerate* (Forsgren et al.); *The DevOps Handbook*; *Continuous Delivery* (Humble & Farley); *The Phoenix Project*; Kubernetes documentation (free); *Infrastructure as Code* (Morris).
- **Seminal:** Humble, continuous delivery; Netflix chaos engineering (Basiri et al. 2016); Dean, "Designs, Lessons and Advice from Building Large Distributed Systems"; DORA State of DevOps reports (open).
- **Tags:** version-control-workflows, CI/CD, containers, Docker, Kubernetes, IaC, Terraform, observability, monitoring, incident-response, SLOs, chaos-engineering, cloud-platforms.

### 7.5 Web Development & Full-Stack (200–300)
- **Courses:** Harvard CS50 Web; The Odin Project (free); Full Stack Open (Helsinki — free); MIT 6.148/Web.lab; freeCodeCamp; Berkeley CS169.
- **Texts:** MDN Web Docs (free); *Eloquent JavaScript* (Haverbeke — free); *You Don't Know JS* (free); *High Performance Browser Networking* (free); *Web Application Security* (Hoffman); HTTP/HTML/CSS/DOM specs (W3C/WHATWG — free).
- **Seminal:** Berners-Lee, "Information Management: A Proposal" (1989); Fielding REST (2000); Garrett, "Ajax" (2005); React architecture papers/talks; Crockford, JSON.
- **Tags:** HTML, CSS, JavaScript, TypeScript, DOM, HTTP, browsers, frontend-frameworks, backend, REST-APIs, GraphQL, authentication, sessions, databases-web, accessibility, performance-web.

### 7.6 Mobile & Cross-Platform (300)
- **Courses:** Stanford CS193p iOS Development (open); Google Android Basics with Compose (free); CS50 Mobile.
- **Tags:** iOS, Android, SwiftUI, Jetpack-Compose, mobile-architecture, offline-first, app-lifecycle.

### 7.7 Open Source Practice & Software Ecosystems (200–400)
- **Texts:** *Producing Open Source Software* (Fogel — free); *The Cathedral and the Bazaar* (Raymond — free); *Working in Public* (Eddy); *Open Source Licensing* guides (OSI, Choose-a-License); *Software Supply Chain Security* (Chainguard/OpenSSF — free).
- **Tags:** licenses, governance, contribution-workflow, semantic-versioning, dependency-management, supply-chain, reproducible-builds, SBOM.

### 7.8 Professional Practice, Ethics & Law (100–300)
- **Courses:** Stanford CS181 Computers, Ethics, and Public Policy; Harvard Embedded EthiCS modules (open); MIT 6.805/STS courses.
- **Texts:** ACM Code of Ethics; *Weapons of Math Destruction* (O'Neil); *Ethics for the Information Age* (Quinn); *Computer Power and Human Reason* (Weizenbaum).
- **Tags:** ethics, privacy, intellectual-property, accessibility-law, professional-responsibility, policy.

---

## 8. Security & Privacy

### 8.1 Computer Security (300–400)
- **Courses:** Berkeley CS161 Computer Security (fully open, textbook + projects); MIT 6.858 Computer Systems Security (open, Zeldovich); Stanford CS155 Computer & Network Security; CMU 18-487 / 15-330; pwn.college (ASU — free, hands-on); Harvard CS50 Cybersecurity.
- **Texts:** CS161 textbook (free); *Security Engineering* (Anderson — free 2nd ed.); *Computer Security: Art and Science* (Bishop); *The Web Application Hacker's Handbook*; *Hacking: The Art of Exploitation* (Erickson); OWASP Top 10 & Cheat Sheets (free).
- **Seminal:** Saltzer & Schroeder, "The Protection of Information in Computer Systems" (1975); Thompson, "Reflections on Trusting Trust" (1984); Aleph One, "Smashing the Stack for Fun and Profit" (1996); Lampson, "A Note on the Confinement Problem" (1973); Bell–LaPadula (1973); Biba; Cowan et al., StackGuard; Shacham, ROP (2007); Kocher et al., Spectre (2018); Lipp et al., Meltdown (2018); Anderson, "Why Cryptosystems Fail" (1993); Abadi et al., CFI (2005); Chrome sandbox architecture papers; Halderman et al., cold boot (2008); Mirai botnet analysis (2017).
- **Tags:** threat-models, memory-safety, buffer-overflows, ROP, mitigations, sandboxing, access-control, authentication, web-security, XSS, CSRF, SQL-injection, network-security, TLS-in-practice, malware, side-channels, hardware-security, secure-design-principles.

### 8.2 Applied & Offensive Security, Reverse Engineering (400)
- **Resources:** pwn.college; OverTheWire (free wargames); picoCTF; CTFtime writeups; Nightmare (free RE course); *Practical Binary Analysis* (Andriesse); *Reversing* (Eilam); Ghidra & radare2 docs.
- **Tags:** exploitation, reverse-engineering, binary-analysis, malware-analysis, penetration-testing, CTF, web-pentesting, forensics.

### 8.3 Privacy & Privacy-Enhancing Technologies (400–500)
- **Courses:** Stanford CS329T/CS255 privacy units; Penn CIS700 Differential Privacy; Berkeley CS294 Privacy.
- **Texts:** *The Algorithmic Foundations of Differential Privacy* (Dwork & Roth — free); *Programming Differential Privacy* (Near & Abuah — free).
- **Seminal:** Dwork et al., differential privacy (2006); Sweeney, k-anonymity (2002); Narayanan & Shmatikov, Netflix deanonymization (2008); Chaum, mix networks (1981); Dingledine et al., Tor (2004); Abadi et al., deep learning with DP (2016); McMahan et al., federated learning (2017).
- **Tags:** differential-privacy, anonymization, Tor, federated-learning, secure-computation-privacy, privacy-law-GDPR.

### 8.4 Blockchain & Decentralized Systems (400)
- **Courses:** Berkeley Blockchain Fundamentals; Stanford CS251 Cryptocurrencies and Blockchain (Boneh — open); Princeton Bitcoin & Cryptocurrency Technologies (free textbook + Coursera).
- **Seminal:** Nakamoto (2008); Buterin, Ethereum whitepaper (2013); Wood, Yellow Paper; Eyal & Sirer, selfish mining (2014); Lightning Network (2016); Nakamoto consensus analyses (Garay et al. 2015); Zerocash (2014).
- **Tags:** consensus-blockchain, proof-of-work, proof-of-stake, smart-contracts, zero-knowledge-rollups, DeFi-security.

---

## 9. Human-Centered Computing

### 9.1 Human-Computer Interaction (300)
- **Courses:** Stanford CS147 Intro to HCI + CS247; UCSD CSE170 / Coursera Interaction Design Specialization (Klemmer); CMU 05-391 Designing Human-Centered Software; Georgia Tech CS6750 (Udacity — free).
- **Texts:** *The Design of Everyday Things* (Norman); *Designing with the Mind in Mind* (Johnson); *Interaction Design* (Sharp, Preece, Rogers); *Don't Make Me Think* (Krug); *Research Methods in HCI* (Lazar et al.); *About Face* (Cooper).
- **Seminal:** Bush, "As We May Think" (1945); Engelbart, "Augmenting Human Intellect" (1962) + "Mother of All Demos" (1968); Sutherland, Sketchpad (1963); Card, Moran, Newell, *The Psychology of HCI* (1983); Fitts's law (1954); Nielsen, heuristic evaluation (1990); Shneiderman, direct manipulation (1983); Weiser, "The Computer for the 21st Century" (1991); Kay, Dynabook (1972).
- **Tags:** user-research, prototyping, usability, heuristic-evaluation, interaction-design, cognitive-models, Fitts-law, accessibility, ubiquitous-computing, evaluation-methods.

### 9.2 Computer Graphics (300–400)
- **Courses:** CMU 15-462/662 Computer Graphics (Crane — open); Stanford CS148/CS248; MIT 6.837 (open); UC Davis ECS175; Berkeley CS184 (open); *Scratchapixel* (free); *Ray Tracing in One Weekend* series (free); TU Wien Rendering (Wojciech Jarosz / Károly Zsolnai-Fehér — open).
- **Texts:** *Fundamentals of Computer Graphics* (Marschner & Shirley); *Physically Based Rendering* (Pharr, Jakob, Humphreys — free); *Real-Time Rendering* (Akenine-Möller et al.); *Polygon Mesh Processing* (Botsch et al.); *Computer Graphics from Scratch* (Gambetta — free); *Learn OpenGL* (free); *Discrete Differential Geometry* (Crane — free).
- **Seminal:** Sutherland (1963); Gouraud (1971); Phong (1975); Blinn (1977); Whitted, ray tracing (1980); Kajiya, rendering equation (1986); Cook, Porter, Carpenter, distributed ray tracing (1984); Catmull & Clark subdivision (1978); Veach, MLT/path tracing (1997); Garland & Heckbert, mesh simplification (1997); Sorkine et al., ARAP; Mildenhall, NeRF (2020); Kerbl et al., 3D Gaussian Splatting (2023).
- **Tags:** rasterization, ray-tracing, path-tracing, shading, transforms, meshes, geometry-processing, textures, GPU-pipelines, shaders, animation, physics-simulation, real-time-rendering, neural-rendering.

### 9.3 Computer Animation, Games & Simulation (400)
- **Courses:** CMU 15-466 Computer Game Programming (open); MIT 6.S090; Stanford CS248A; Pikuma / Handmade Hero (open video).
- **Texts:** *Game Engine Architecture* (Gregory); *Game Programming Patterns* (Nystrom — free); *Physics-Based Animation* (Erleben); *Real-Time Collision Detection* (Ericson); Pixar SIGGRAPH course notes (free).
- **Seminal:** Baraff & Witkin, physically based modeling notes (SIGGRAPH — free); Müller et al., position-based dynamics (2007); Stam, "Stable Fluids" (1999); Reynolds, Boids (1987).
- **Tags:** game-loops, ECS, physics-engines, collision-detection, character-animation, fluids, procedural-generation, engines.

### 9.4 Data Visualization (300)
- **Courses:** Berkeley CS294-10 / Stanford CS448B Data Visualization (Heer — open); UW CSE442.
- **Texts:** *The Visual Display of Quantitative Information* (Tufte); *Fundamentals of Data Visualization* (Wilke — free); *Visualization Analysis and Design* (Munzner); *Interactive Data Visualization for the Web* (Murray — free).
- **Seminal:** Bertin, *Semiology of Graphics*; Cleveland & McGill (1984); Shneiderman, visual information seeking mantra (1996); Bostock et al., D3 (2011); Wickham, grammar of graphics / ggplot2; Satyanarayan et al., Vega-Lite (2017).
- **Tags:** visual-encoding, perception, chart-design, interaction-vis, D3, grammar-of-graphics, dashboards.

### 9.5 Computational Social Science & Social Computing (400)
- **Courses:** Stanford CS224W Machine Learning with Graphs (Leskovec — open); Cornell INFO 2040 Networks (Easley & Kleinberg — free text); Stanford CS278 Social Computing.
- **Texts:** *Networks, Crowds, and Markets* (Easley & Kleinberg — free); *Mining of Massive Datasets* (Leskovec, Rajaraman, Ullman — free).
- **Seminal:** Milgram small world (1967); Watts & Strogatz (1998); Barabási & Albert (1999); Page et al., PageRank (1998); Kleinberg, HITS (1999); Granovetter, weak ties (1973); Kipf & Welling, GCN (2016); Kleinberg et al. on recommendation & polarization.
- **Tags:** network-science, graph-ML, GNNs, recommender-systems, crowdsourcing, online-communities, social-network-analysis, misinformation.

---

## 10. Data & Information Systems

### 10.1 Data Science & Analytics (200–300)
- **Courses:** Berkeley Data 8 Foundations of Data Science (fully open) + Data 100 Principles & Techniques (open); Harvard CS109 Data Science (open); MIT 6.0002 Intro to Computational Thinking & Data Science (open); Johns Hopkins Data Science specialization.
- **Texts:** *Computational and Inferential Thinking* (Data 8 — free); *Principles and Techniques of Data Science* (Data 100 — free); *Python for Data Analysis* (McKinney — free); *R for Data Science* (Wickham — free); *The Art of Statistics* (Spiegelhalter).
- **Tags:** exploratory-analysis, pandas, tidyverse, visualization-basics, inference, A/B-testing, causal-basics, data-cleaning, notebooks.

### 10.2 Big Data & Data Mining (400)
- **Courses:** Stanford CS246 Mining Massive Datasets (open); Berkeley CS186/CS262A data units; UW CSE544.
- **Texts:** *Mining of Massive Datasets* (free); *Data Mining: Concepts and Techniques* (Han, Kamber, Pei); *Foundations of Data Science* (Blum, Hopcroft, Kannan — free).
- **Seminal:** MapReduce (2004); Spark (2012); Agrawal & Srikant, association rules (1994); Broder, MinHash (1997); Flajolet et al., HyperLogLog (2007); Cormode & Muthukrishnan, Count-Min sketch (2005); Stonebraker et al., Aurora/Borealis streaming; Akidau et al., Dataflow model (2015); Flink (2015).
- **Tags:** MapReduce, Spark, streaming, sketches, frequent-itemsets, similarity-search, clustering-large-scale, recommender-systems, data-lakes, lakehouses, Parquet/Arrow.

### 10.3 Information Retrieval & Search (400)
- **Courses:** Stanford CS276 Information Retrieval & Web Search (open); UIUC CS410 Text Information Systems (Coursera); Waterloo CS431/CS651 (Lin).
- **Texts:** *Introduction to Information Retrieval* (Manning, Raghavan, Schütze — free); *Search Engines: IR in Practice* (Croft, Metzler, Strohman — free); *Pretrained Transformers for Text Ranking* (Lin et al. — free); Lucene/Elasticsearch docs.
- **Seminal:** Salton, vector space model (1975); Robertson & Spärck Jones, probabilistic model / BM25 (1976/1994); Brin & Page, "The Anatomy of a Large-Scale Hypertextual Web Search Engine" (1998); Broder, "A Taxonomy of Web Search" (2002); Karpukhin et al., DPR (2020); Khattab & Zaharia, ColBERT (2020); Malkov & Yashunin, HNSW (2016); Johnson et al., FAISS (2017); Nogueira & Cho, BERT re-ranking (2019); learning-to-rank (Burges, LambdaMART).
- **Tags:** inverted-index, tokenization-IR, BM25, vector-space, relevance, evaluation-IR, web-crawling, PageRank, learning-to-rank, dense-retrieval, ANN-search, HNSW, RAG-retrieval, query-understanding, search-UX.
- **Note for this project:** this section is the theoretical backbone for your own course-search index — CS276 + Manning's IRB + the dense-retrieval papers cover both keyword and semantic indexing.

### 10.4 Knowledge Representation, Semantic Web & Ontologies (400)
- **Texts:** *Knowledge Representation and Reasoning* (Brachman & Levesque); *Semantic Web for the Working Ontologist*; W3C RDF/OWL/SPARQL specs (free); *Foundations of Semantic Web Technologies* (Hitzler et al.).
- **Seminal:** Berners-Lee, Hendler, Lassila, "The Semantic Web" (2001); Bollacker et al., Freebase (2008); Vrandečić, Wikidata (2014); Bordes et al., TransE (2013).
- **Tags:** ontologies, RDF, SPARQL, knowledge-graphs, description-logics, reasoning, entity-linking.

---

## 11. Specialized & Interdisciplinary Areas

### 11.1 Computational Biology & Bioinformatics (400)
- **Courses:** MIT 6.047/6.878 Computational Biology (Kellis — open); Coursera Bioinformatics Specialization (UCSD, Compeau & Pevzner); Rosalind (free problems).
- **Texts:** *Bioinformatics Algorithms: An Active Learning Approach* (Compeau & Pevzner); *Biological Sequence Analysis* (Durbin et al.).
- **Seminal:** Needleman–Wunsch (1970); Smith–Waterman (1981); Altschul et al., BLAST (1990); Burrows–Wheeler/BWA; Jumper et al., AlphaFold 2 (2021).
- **Tags:** sequence-alignment, genome-assembly, HMMs-bio, phylogenetics, protein-structure, single-cell-analysis.

### 11.2 Scientific Computing & Computational Physics (300–400)
- **Courses:** MIT 18.335 / 18.336; Berkeley CS267; Harvard AM205 (open); Lorena Barba's *CFD Python* (free).
- **Texts:** *Numerical Recipes*; *Scientific Computing* (Heath); *Python Programming and Numerical Methods* (free); Julia documentation & *Introduction to Computational Thinking* (MIT 18.S191 — free, Julia).
- **Tags:** ODE/PDE-solvers, finite-elements, Monte-Carlo, sparse-linear-algebra, automatic-differentiation, Julia, reproducibility.

### 11.3 Signal Processing, Audio & Speech (300–400)
- **Courses:** MIT 6.003 Signals & Systems (open); Stanford EE261 Fourier Transform; Stanford CCRMA Music 320 (Smith — free texts); Coursera Audio Signal Processing for Music Applications.
- **Texts:** *Signals and Systems* (Oppenheim); *Think DSP* (Downey — free); *Mathematics of the DFT* & *Spectral Audio Signal Processing* (J.O. Smith — free); Jurafsky & Martin speech chapters.
- **Seminal:** Cooley & Tukey, FFT (1965); Nyquist/Shannon sampling; Rabiner, HMM tutorial (1989); Graves et al., CTC (2006); Baevski et al., wav2vec 2.0 (2020); Radford et al., Whisper (2022).
- **Tags:** Fourier, sampling, filters, DFT/FFT, spectrograms, speech-recognition, TTS, audio-ML.

### 11.4 Computational Geometry (400)
- **Texts:** *Computational Geometry: Algorithms and Applications* (de Berg et al.); *Computational Geometry in C* (O'Rourke); CGAL docs.
- **Seminal:** Graham scan (1972); Fortune's sweep (1987); Delaunay/Voronoi foundations; Shewchuk, Triangle & robust predicates.
- **Tags:** convex-hull, Voronoi, Delaunay, range-searching, mesh-generation, robustness.

### 11.5 Algorithmic Game Theory, Mechanism Design & Economics of Computing (400–500)
- **Courses:** Stanford CS364A (Roughgarden — lectures + notes free); Berkeley CS294-Econ; Coursera Game Theory (Stanford/UBC).
- **Texts:** *Twenty Lectures on Algorithmic Game Theory* (Roughgarden); *Algorithmic Game Theory* (Nisan et al. — free).
- **Seminal:** Nash (1950); Vickrey (1961); Myerson (1981); Koutsoupias & Papadimitriou, price of anarchy (1999); Daskalakis, Goldberg, Papadimitriou, PPAD-completeness of Nash (2009); Edelman, Ostrovsky, Schwarz, GSP auctions (2007).
- **Tags:** equilibria, auctions, mechanism-design, price-of-anarchy, matching-markets, market-algorithms.

### 11.6 Computing History & Foundational Essays (100–500, cross-cutting)
- **Texts/Collections:** *Ideas That Created the Future: Classic Papers of Computer Science* (Lewis, ed.); ACM Turing Award lectures (free); *The Dream Machine* (Waldrop); *Where Wizards Stay Up Late*; *Hackers* (Levy); *Soul of a New Machine* (Kidder); Computer History Museum oral histories (free).
- **Essays:** Dijkstra, "Go To Statement Considered Harmful" (1968) + EWD archive (free); Knuth, "Structured Programming with go to Statements" (1974) & "Computer Programming as an Art"; Hoare, "The Emperor's Old Clothes" (1980); Brooks, "No Silver Bullet"; Hamming, "You and Your Research" (1986); Wirth, "A Plea for Lean Software" (1995); Gabriel, "Worse Is Better" (1991); Norvig, "Teach Yourself Programming in Ten Years"; Graham, "Hackers and Painters"; Sussman, "Programming for the Expression of Ideas"; Perlis, "Epigrams on Programming".
- **Tags:** history, philosophy-of-computing, research-practice, classic-papers.

---

## 12. Suggested Learning Paths (prerequisite spines)

**Core spine (everyone):**
CS50/61A → Discrete Math → Data Structures (61B) → CSAPP/15-213 → Algorithms (6.046/CS161) → OS (6.1810) → Networks (CS144) → Databases (15-445) → Theory (Sipser) → Software Construction (6.102) + Missing Semester → one of the 400-level tracks.

**Systems track:** Architecture (CS61C/Nand2Tetris) → OS → Compilers (CS143 + Crafting Interpreters) → Distributed Systems (6.5840) → Parallel (CS149) → Advanced DB (15-721) → Security (6.858) → Formal Methods.

**Theory track:** 6.042 → 6.046 → 18.404 → 6.854 → Complexity (6.841) → Cryptography (Boneh) → PL Theory (TAPL/Software Foundations) → Quantum.

**AI/ML track:** Linear Algebra + Probability → CS229 → Deep Learning (CS231N/CS224N) → RL (CS285) → Learning Theory / PGMs → ML Systems (10-714) → LLMs (CS336/CS324) → Safety & Interpretability.

**Software engineering track:** 6.102 → CS169 → Testing & Analysis (Zeller) → Architecture/DDIA → DevOps/SRE → Web/Mobile → Open-source practice.

**Human-centered track:** HCI (CS147) → Graphics (15-462) → Visualization (CS448B) → Social computing (CS224W) → Games/Animation.

**Data track:** Data 8 → Data 100 → CS186 → CS246 → CS276 IR → Distributed Data (Spark/Flink papers) → Knowledge graphs.

---

## 13. Coverage Checklist (ACM/IEEE CS2023 knowledge areas → sections here)

| Knowledge area | Sections |
|---|---|
| Algorithmic Foundations | 3, 5.1–5.2 |
| Architecture & Organization | 4.1 |
| Artificial Intelligence | 6.1–6.11 |
| Data Management | 4.5, 10.2 |
| Foundations of PL | 2.4, 4.3, 5.4 |
| Graphics & Interactive Techniques | 9.2–9.3 |
| Human-Computer Interaction | 9.1, 9.4 |
| Mathematical & Statistical Foundations | 1.1–1.7 |
| Networking & Communication | 4.4 |
| Operating Systems | 4.2 |
| Parallel & Distributed Computing | 4.6–4.8 |
| Platform-Based Development (web/mobile/embedded) | 7.5–7.6, 4.9 |
| Security | 8.1–8.4 |
| Society, Ethics & Professionalism | 7.8, 6.11 |
| Software Development Fundamentals | 2.1–2.3, 2.6 |
| Software Engineering | 7.1–7.4, 7.7 |
| Specialized Platforms / Interdisciplinary | 11.1–11.6 |

---

## 14. Next Steps for Corpus Build
1. Turn every course entry into a manifest row (schema §0.2); start with the ~40 "fully open" courses flagged above — they have crawlable syllabi, notes, psets, and video transcripts.
2. Pull the MIT 6.5840, Berkeley CS262A, Papers We Love, and Red Book reading lists as bulk paper seeds (they're already curated by topic).
3. Fetch open textbooks in source form where available (many are LaTeX/Markdown on GitHub — SICP, OSTEP, PLAI, DDIA-adjacent notes, D2L, Software Foundations).
4. Generate a prerequisite graph from OSSU + course pages; store as edges for "learning path" queries.
5. For paywalled canonical texts and ACM/IEEE papers, index metadata + abstract + tags only, and link out.
6. Tag with the `topics` vocabularies in each section; keep a controlled vocabulary file so tags are consistent across sources.

# Log

Newest first. Generated from wiki/log/*.md — do not edit.

---
title: Ingest §8.3 privacy technologies and §8.4 blockchain
type: log
section: "8.4"
tags: [ingest, privacy, differential-privacy, tor, mpc, federated-learning, blockchain, bitcoin, consensus]
summary: Read the Dwork & Roth monograph ToC, the Tor paper abstract, the Nakamoto Bitcoin paper (abstract and §1–2), and the CS251 2025 syllabus; wrote 2 concepts and 1 source, building on the existing differential-privacy (§6.11) and byzantine-fault-tolerance-and-blockchains (§4) pages rather than duplicating them. This completes §8.
---
## [2026-09-02] ingest | §8.3 Privacy & §8.4 Blockchain

Read: cis.upenn.edu Dwork & Roth privacybook.pdf full ToC (13 chapters: (ε,δ)-DP,
Laplace/exponential mechanisms, composition, sparse vector, SmallDB/private MW, boosting,
subsample-and-aggregate/propose-test-release, reconstruction lower bounds, DP+complexity,
DP+mechanism-design, DP+ML, local/pan-private/continual models); programming-dp.com
front matter; svn tor-design.html abstract (telescoping circuits, PFS, fixed cells,
directory servers, exit policies, rendezvous hidden services); bitcoin.org/bitcoin.pdf
abstract + §1–2 (double-spending, coin = chain of signatures, PoW timestamp chain,
longest chain = honest majority, "cryptographic proof instead of trust"); cs251.stanford.edu
Fall 2025 syllabus (Bitcoin mechanics, classical consensus/SMR, Nakamoto consensus, PoS
& availability-finality, EVM/Solidity, DeFi/AMM/MEV/flash-loans, zk-SNARKs/Zcash,
Lightning/rollups). Sweeney, Narayanan-Shmatikov, MPC/FHE, selfish mining, reentrancy
from memory.

Source: [[privacy-and-blockchain-texts-courses-and-seminal-papers]].
Concepts: [[privacy-enhancing-technologies]], [[blockchain-and-cryptocurrencies]].
Existing pages linked, not duplicated: [[differential-privacy]] (§6.11 — the DP mechanism
lives there; the PET page points to it), [[byzantine-fault-tolerance-and-blockchains]]
(§4 — Nakamoto/PBFT consensus; the blockchain page points to it),
[[cryptographic-protocols-and-zero-knowledge]], [[public-key-cryptography]],
[[hash-functions-cryptographic]], [[consensus-paxos-raft]].

Insights: the three privacy goals map cleanly onto three failures of "just encrypt it" —
DP for output leakage, Tor/mixnets for metadata, MPC/FHE for input secrecy — and each is
a different point in a cost/utility space, so "which PET" is a threat-model question, the
same discipline as §8.1. De-identification's failure (Sweeney, Netflix) is the empirical
motivation for DP the same way memory-safety CVE stats motivate Rust. Nakamoto consensus
is sybil-resistance bolted onto the §4 Byzantine-agreement problem by pricing votes in a
scarce resource — and PoS's accountability/slashing is what classical BFT already had
(known validators), so the blockchain design space is exactly the §4 consensus space with
open membership added. Smart-contract "gas" is the halting problem (§5) monetized;
zk-rollups are §8.3 zero-knowledge proofs (§8's crypto) solving §7.3 scalability. The
whole section reinforces that "trust-minimization" is a cost you pay, not a free lunch —
the same lesson as REST statelessness and microservices.

§8 complete (8.1–8.4). Next: §9 Human-centered computing (9.1 HCI — human-computer-
interaction is wanted from ~8 pages; create it first), then §10 IR/data, §11 specialized,
§12 paths/syntheses.

---
title: Ingest §8.1 computer security
type: log
section: "8.1"
tags: [ingest, security, threat-model, access-control, exploitation, web-security, network-security]
summary: Read the CS161 textbook ToC and its "Security Principles" chapter in full, Saltzer & Schroeder's abstract and glossary, the MIT 6.858 2023 schedule, Anderson's Security Engineering chapter list, and the OWASP Top 10:2021 list; wrote 5 concepts (security-principles and web-security were long-wanted from ~14 pages) and 1 source, linking the existing §4/§8.3 crypto and systems pages rather than duplicating.
---
## [2026-09-02] ingest | §8.1 Computer security

Read: textbook.cs161.org ToC (39 chapters, 5 parts) + ch. 1 "Security Principles" in
full (threat model + six attacker assumptions incl. the fish-tank thermometer; human
factors; security is economics; detect if you can't prevent; defense in depth; least
privilege; separation of responsibility; complete mediation; Shannon's maxim; fail-safe
defaults; design security in; TCB; TOCTTOU); Saltzer & Schroeder 1975 abstract + full
glossary (principal, ACL vs capability = list- vs ticket-oriented, confinement,
protected subsystem, TCB) — the eight principles from memory; css.csail.mit.edu 6.858
Spring 2023 schedule (24 lectures + 5 labs, full paper list); cl.cam.ac.uk Anderson 3e
chapter list; owasp.org Top 10:2021. Bell-LaPadula, Biba, ROP/Spectre, TLS/PKI, DoS,
BGP/DNS attacks from memory.

Source: [[computer-security-texts-courses-and-seminal-papers]].
Concepts: [[security-principles]] (long-wanted), [[access-control-and-isolation]],
[[software-exploitation-and-mitigations]], [[web-security]] (long-wanted),
[[network-security-attacks-and-defenses]]. Existing pages linked, not duplicated:
[[memory-safety-and-buffer-overflows]], [[undefined-behavior]], [[ownership-and-borrowing]],
[[cryptography-basics]], [[symmetric-encryption-and-authenticated-encryption]],
[[public-key-cryptography]], [[hash-functions-cryptographic]], [[web-backends-sessions-and-authentication]],
[[dns-http-and-the-web-stack]], [[containers-and-kubernetes]], [[os-kernels-and-virtualization]].

Insights: Saltzer & Schroeder's ACL-vs-capability split is the same "store the relation
with the object or with the subject" duality as adjacency-list vs adjacency-matrix and as
ACL-vs-capability in every later system; the confused deputy is CSRF is SSRF is the
compiler-writes-billing-file example — one bug class across §7.5, §8.1, §8.2. "Complete
mediation" violated in time is TOCTTOU, which is the same race as §4 concurrency's
check-then-act. Spectre is the point where §4.1 microarchitecture (speculation, caches)
becomes a §8 security boundary — abstraction leaks are security bugs. Memory safety:
§2 Rust ownership is the strategic fix for §8.2 exploitation (70% of CVEs). Kerckhoffs/
Shannon's maxim is the crypto version of "design for the adversary who knows the system"
= the threat-model discipline. Zero trust is "no ambient authority" at network scale.

Forward wanted: privacy-enhancing-technologies (§8.3 next — Tor, DP already exists,
federated learning, secure computation), blockchain-and-cryptocurrencies /
consensus-blockchain (§8.4 — byzantine-fault-tolerance-and-blockchains already exists),
computer-architecture page (referenced microarch via pipelining-and-hazards for now).

---
title: Ingest §7.8 professional practice, ethics & law
type: log
section: "7.8"
tags: [ingest, ethics, professional-responsibility, law, privacy, intellectual-property, acm-code]
summary: Read Stanford CS181's Spring 2024 syllabus (goals, Unit 1 readings), Harvard Embedded EthiCS's module index (responsibility and red-teaming modules), and confirmed the ACM code from memory after acm.org returned 403; wrote 2 concepts and 1 source. This completes §7.
---
## [2026-09-02] ingest | §7.8 Professional practice, ethics & law

Read: web.stanford.edu/class/cs181 Spring 2024 (learning goals: recognize / reason /
persuade; grading; Unit 1 risk and responsibility — NSPE + ACM codes, Therac-25 memo,
Bernstein, Hofstadter, Hormio, Patrick Racing, Iran Air 655); embeddedethics.seas.
harvard.edu modules index (taxonomy of ethics topics; "Responsibility in Software
Design: Blame, Liability, & Taking Responsibility" — three senses of responsibility,
AI responsibility gaps, Kodak Shirley cards; "Red Teaming & Responsibility").
acm.org/code-of-ethics and ethics.acm.org both 403 — the code's structure and clauses
written from memory (flagged in the source page). O'Neil, Quinn, Weizenbaum, Leveson &
Turner, case law (Oracle v. Google, Alice, Van Buren, hiQ), GDPR/CCPA from memory.

Source: [[computing-ethics-texts-courses-and-codes]].
Concepts: [[computing-ethics-and-professional-responsibility]],
[[technology-law-privacy-and-intellectual-property]].

Insights: the three-senses-of-responsibility distinction (blame / liability / taking
responsibility) is the ethics counterpart of blameless postmortems (§4.8, §7.4): stop
asking who is at fault, ask who will act. Nissenbaum's contextual integrity is
purpose limitation stated as a theory of norms — and it is exactly the property
differential privacy (§6.11) and data minimization operationalize. Oracle v. Google's
"assume copyrightable, hold fair use" leaves clean-room reimplementation the
engineering norm, the same discipline as Compaq's BIOS. Van Buren's gates-up-or-down
test is an authorization model (§8.2 access control) written by a court. Weizenbaum's
decide-vs-choose is the alignment/oversight question of §6.11 forty years early.

§7 complete (7.1–7.8). Next: §8 Security & privacy — the pages security-principles
and web-security are now wanted from ~12 pages; create them first.

---
title: Ingest §7.6 mobile & cross-platform and §7.7 open source practice & ecosystems
type: log
section: "7.7"
tags: [ingest, mobile, swiftui, compose, open-source, licensing, dependencies, supply-chain, slsa]
summary: Read CS193p's 2025 lecture list and the Android developer site structure (§7.6); Fogel's full ToC, Raymond's "Release Early, Release Often", choosealicense's license spectrum, SLSA v1.0 levels, and the Reproducible Builds definition (§7.7); wrote 1+4 concepts (dependency-management-and-packaging was wanted) and 2 sources.
---
## [2026-09-02] ingest | §7.6 Mobile and §7.7 Open source practice

§7.6 read: cs193p.stanford.edu Spring 2025 (14 lectures: Views/modifiers, Model vs UI,
Swift type system, @State/@Binding, layout and data flow, generics/ViewBuilder,
animation, protocols, List/navigation, iPad/sheets, SwiftData); developer.android.com
navigation (Compose, adaptive apps, architecture, quality, security). Apple lifecycle,
Compose state docs, RN/Flutter/KMP from memory.
Source: [[mobile-development-courses]]; concept: [[mobile-development-and-cross-platform]].

§7.7 read: producingoss.com 2e full table of contents (ch. 1–5 in detail: mission,
license choice, setting the tone, infrastructure, governance models, money);
catb.org "Release Early, Release Often" (Linus's law, users as co-developers);
choosealicense.com/licenses (AGPLv3 → Unlicense with permissions/conditions/
limitations); slsa.dev v1.0 "Security levels" (Build L0–L3); reproducible-builds.org
definition. Eghbal, SemVer, Cox on MVS, Sigstore, incidents from memory.
Source: [[open-source-practice-texts-and-seminal-papers]]; concepts:
[[open-source-practice-and-governance]], [[software-licensing]],
[[dependency-management-and-packaging]] (wanted), [[software-supply-chain-security]].

Insights: SwiftUI and Compose independently converging on UI = f(state) with
hoisted state is strong evidence the React model is the stable attractor for UI
programming; process death is the mobile form of crash-only design (§4.8) — design so
any state can be rebuilt. Fogel's "be open from day one / waiting creates an exposure
event" is the same argument as continuous integration (small public increments beat
big private batches). Dependency resolution is literally SAT (Abate et al.), and Go's
MVS is the "restrict the problem until it's polynomial" move from §5 complexity. SLSA
levels are a threat-model ladder exactly like §4.8 SLO tiers; Sigstore's transparency
log is a Merkle tree (§8.3 cryptography) doing certificate-transparency's job for
software. Reproducible builds are determinism as a security property — the same
requirement fuzzing (§7.2) and delta debugging impose for different reasons.

Forward wanted: computing-ethics-and-professional-responsibility (§7.8 next),
security-principles, web-security (§8), human-computer-interaction (§9).

---
title: Ingest §7.5 web development & full-stack
type: log
section: "7.5"
tags: [ingest, web, html, css, javascript, react, http, performance, authentication]
summary: Read MDN's HTTP overview and critical-rendering-path guide, HPBN's table of contents, Eloquent JavaScript's contents, Full Stack Open's part list; wrote 5 concepts and 1 combined source, building on the existing dns-http-and-the-web-stack (§4) and api-design (§7.3) pages.
---
## [2026-09-02] ingest | §7.5 Web development & full-stack

Read: MDN "Overview of HTTP" (client–server, user agents, proxies, extensible,
stateless-but-sessions-via-cookies, what HTTP controls); MDN "Critical rendering path"
(bytes → tokens → DOM; CSSOM; render tree; layout; paint; render-blocking CSS and
parser-blocking scripts); hpbn.co ToC (latency/bandwidth, TCP, UDP/NAT, TLS with its
optimization checklist, wireless/WiFi/mobile RRC, HTTP/1.x → /2, browser APIs);
eloquentjavascript.net 4e contents; fullstackopen.com parts 0–14. React docs, YDKJS,
OWASP cheat sheets, OAuth/OIDC RFCs, Core Web Vitals from memory.

Source: [[web-development-texts-courses-and-seminal-papers]].
Concepts: [[html-css-and-the-dom]], [[javascript-and-the-event-loop]],
[[frontend-frameworks-and-state-management]], [[web-backends-sessions-and-authentication]],
[[web-performance-and-browser-networking]]. Existing pages extended by linking:
[[dns-http-and-the-web-stack]], [[api-design]].

Insights: the JavaScript event loop is the same run-to-completion, single-queue model
as an OS interrupt-driven kernel with deferred work (microtasks ≈ softirqs); the
"task vs microtask" ordering puzzle is priority scheduling. "UI = f(state)" is the
functional-core idea from §2 applied to screens, and virtual-DOM diffing is
tree-edit-distance made cheap by heuristics (keys = identity). Web performance's
"latency not bandwidth" lesson is the memory-hierarchy lesson from §4.1 one level up:
round trips are cache misses. Sessions vs JWTs is the stateful-vs-stateless trade-off
from REST (§7.3) with revocation as the cost of statelessness. Cookies' SameSite/CSRF
story is the confused-deputy problem, which §8 will name.

Forward wanted: web-security, security-principles (§8.1–8.2 — now referenced from
seven pages; prioritize), human-computer-interaction (§9.x), mobile-development-and-
cross-platform (§7.6 next), concurrency-and-parallelism (check §4 slug — may be
parallel-programming-models).

---
title: Ingest §7.4 DevOps, CI/CD, SRE & infrastructure
type: log
section: "7.4"
tags: [ingest, devops, ci-cd, sre, kubernetes, chaos-engineering, observability, infrastructure-as-code]
summary: Read SRE book and Workbook tables of contents, SRE ch. 4 (SLOs) in full, continuousdelivery.com, the Principles of Chaos, DORA's metrics guide, and the Kubernetes concepts index; wrote 5 concepts (continuous-integration-and-delivery and containers-and-kubernetes were wanted) and 1 combined source, building on the existing §4.8 site-reliability-engineering and cluster-scheduling-and-observability pages.
---
## [2026-09-02] ingest | §7.4 DevOps, CI/CD, SRE & infrastructure

Read: sre.google ToC (34 chapters + appendices) and Workbook ToC; SRE ch. 4 (SLI/SLO/SLA
definitions, Shakespeare example, "you don't always get to choose", latency–QPS
coupling); continuousdelivery.com "What is CD" + benefits list; principlesofchaos.org
(definition, four-step experiment, five advanced principles); dora.dev metrics guide
(throughput: change lead time, deployment frequency, failed-deployment recovery time;
instability: change fail rate, deployment rework rate; "speed and stability are not
tradeoffs"); kubernetes.io Concepts index. Humble & Farley, Accelerate capabilities,
DevOps Handbook, Phoenix Project, Morris IaC, Terraform docs, Twelve-Factor, Netflix
FIT/ChAP, DiRT, Prometheus/OTel from memory.

Source: [[devops-cicd-and-sre-texts-courses-and-seminal-papers]].
Concepts: [[continuous-integration-and-delivery]] (wanted), [[containers-and-kubernetes]]
(wanted), [[infrastructure-as-code-and-devops]],
[[observability-monitoring-and-incident-response]], [[chaos-engineering-and-reliability-testing]].
Existing pages that already carried the §4.8 SRE core (SLOs, error budgets, toil,
overload, cascading failure) were linked, not duplicated: [[site-reliability-engineering]],
[[cluster-scheduling-and-observability]], [[cloud-and-serverless]].

Insights: Kubernetes' reconciliation loop is the same level-triggered control-loop idea
as GitOps and Terraform's plan/apply — declare desired state, converge — i.e. the
software-engineering form of feedback control; chaos engineering is Popperian testing
for systems (a hypothesis you try to refute against a steady-state metric), which is
also exactly the canary methodology; DORA's finding that speed and stability correlate
is the batch-size argument from lean manufacturing and, in the corpus, the same
small-increments logic as CI, delta debugging, and gradient steps. "Alert on symptoms
not causes" is SLOs pushed into the alerting layer; burn-rate alerting is a derivative
threshold on an integral — control theory again.

Forward wanted: security-principles, web-security (§8); raft (check §4 slug for
consensus); design-by-contract now exists (§7.2). Note for §7.5: dns-http-and-the-web-stack
exists — extend rather than create http page.

---
title: Ingest §7.3 software architecture & system design
type: log
section: "7.3"
tags: [ingest, software-architecture, rest, microservices, system-design, garlan-shaw, fielding]
summary: Read Garlan & Shaw 1994 (abstract, ToC, §1), Fielding ch. 5 §5.1–5.2.1 in full, Lewis & Fowler's microservices article (definition + characteristics), the system-design-primer headings, AOSA contents; wrote 4 concepts (software-architecture-and-system-design and api-design were wanted) and 1 combined source; links to §4 DDIA-derived pages rather than re-deriving them.
---
## [2026-09-02] ingest | §7.3 Software architecture & system design

Read: Garlan & Shaw CMU-CS-94-166 (abstract; the "structural issues" list; ToC — styles
§3.1–3.8, six case studies incl. KWIC four ways, oscilloscopes, compilers, PROVOX,
rule-based interpreter, Hearsay-II); Fielding ch. 5 §5.1.1–5.1.8 (null style → client-
server → stateless → cache → uniform interface → layered → code-on-demand; the induced
properties and trade-offs stated for each) and §5.2.1 opening (data elements — "move
data to the processor" vs mobile code); Lewis & Fowler 2014 (definition, monolith
contrast, componentization via services with the library/service distinction, the nine
characteristics and sidebar list); system-design-primer README headings; AOSA vol. 1
contents. Bass/Richards & Ford/Martin/Evans/Hohpe & Woolf/Kruchten/Helland/Nygard from
memory.

Source: [[software-architecture-texts-courses-and-seminal-papers]].
Concepts: [[software-architecture-and-system-design]] (wanted), [[api-design]] (wanted),
[[microservices-and-resilience-patterns]], [[scalable-system-design]].

Insights: Fielding's method — derive the architecture by adding constraints and naming
the property each induces — is the same move as Parnas (modules by decisions) and as
the end-to-end argument: name what varies, then let the structure follow. REST's
stateless constraint is the architectural form of "no shared mutable state" from §2/§4;
its uniform interface is why HTTP intermediaries (caches, CDNs, proxies) exist at all.
The primer's building blocks are mostly §4 content (replication, partitioning,
consistency, caching, queues) recombined — the page is a synthesis pointing back rather
than a re-derivation. Garlan & Shaw's KWIC-four-ways comparison table is the empirical
companion to Parnas' argument, twenty years later. Microservices = Conway's law
applied on purpose; their resilience patterns are §4 failure models with names.

Forward wanted: continuous-integration-and-delivery, containers-and-kubernetes (§7.4);
http-and-the-web, web-security (§7.5/§8); security-principles (§8); latency-and-
performance-numbers, caching-strategies, dns-and-naming, serialization-and-data-formats,
distributed-transactions-and-2pc, write-ahead-logging-and-recovery, stream-processing,
lsm-trees-and-log-structured-storage, b-trees-and-indexing, buffer-management,
data-models-relational-and-beyond, bloom-filters, web-search-and-crawling,
concurrency-control-and-transactions — check §4 slugs and remap before commit.

---
title: Ingest §7.2 testing, debugging & program analysis
type: log
section: "7.2"
tags: [ingest, testing, fuzzing, delta-debugging, symbolic-execution, quickcheck, klee, static-analysis, contracts]
summary: Read Fuzzing Book (ToC, "Fuzzing: Breaking Things with Random Inputs", "Greybox Fuzzing"), Debugging Book (ToC, "Reducing Failure-Inducing Inputs", "Statistical Debugging"), QuickCheck abstract+intro, KLEE abstract+intro; wrote 7 concepts (fuzzing and design-by-contract were wanted) and 1 combined source; found abstract-interpretation, dataflow-analysis, sat-and-smt-solvers, memory-safety-and-buffer-overflows, undefined-behavior already exist from §3/§8 prep and linked rather than duplicated.
---
## [2026-09-02] ingest | §7.2 Testing, debugging & program analysis

Read: fuzzingbook.org ToC + Fuzzer.html (RandomFuzzer/Runner architecture, bugs
fuzzers find: buffer overflows, missing error checks, rogue numbers; generic vs
program-specific checkers) + GreyboxFuzzer.html (AFL trampoline after every conditional
jump, seeds/mutators/power schedules, AFLFast energy for rare paths, AFLGo directed
distance schedule, the URL-corpus example); debuggingbook.org ToC + DeltaDebugger.html
('1 + 2 * 3 / 0' → '3/0'; min_args/max_args/min_arg_diff; reducing code and syntax trees)
+ StatisticalDebugger.html (collect_pass/collect_fail, Tarantula/Ochiai, discrete vs
continuous spectra, "how useful is ranking"); Claessen & Hughes 2000 abstract + §1
(properties as formal specs, distribution under tester control, 300 lines); Cadar, Dunbar
& Engler 2008 abstract + §1 (symbolic input "anything", path condition, 90 % Coreutils
coverage, 56 bugs, cross-checking, path explosion + environment problem). AFL whitepaper,
DART/SAGE, Tarantula, mutation testing, Coverity CACM, Meyer, Hypothesis from memory.

Source: [[testing-and-program-analysis-texts-courses-and-seminal-papers]].
Concepts: [[software-testing-fundamentals]], [[fuzzing]] (wanted), [[property-based-testing]],
[[delta-debugging-and-fault-localization]], [[symbolic-execution-and-concolic-testing]],
[[static-and-dynamic-analysis-tools]], [[design-by-contract]] (wanted).
Existing pages linked, not duplicated: [[abstract-interpretation]], [[dataflow-analysis]],
[[sat-and-smt-solvers]], [[memory-safety-and-buffer-overflows]], [[undefined-behavior]],
[[unit-testing]], [[debugging]], [[program-verification]], [[model-checking]].

Insights: the whole section is one search problem with different oracles and different
step generators — fuzzing (implicit oracle, byte mutations, coverage as fitness), PBT
(property oracle, typed generators, shrinking), symbolic execution (solver as the step
generator, assertions as oracle), delta debugging (the test as oracle, subset lattice as
the space), SBFL (coverage spectra as features), program repair (test suite as fitness
over patches — and therefore exactly as weak as the suite). Shrinking = ddmin =
Hypothesis's byte-stream reduction; the coupling effect in mutation testing is the same
bet as "small faults suffice" in the competent-programmer hypothesis. Coverity's
30 %-false-positive cliff is the Goodhart/precision-recall trade-off of §6.11 in tool
adoption clothing. Design by contract closes the loop: contracts are Hoare triples,
which are what KLEE checks per path, what Dafny proves for all paths, and what fuzzers
need to find logic bugs.

Forward wanted (still): continuous-integration-and-delivery (§7.4), web-security,
security-principles (§8), hoare-logic (check §3.x slug), exceptions-and-error-handling
(§2.x?), computability-and-undecidability (§5.1 slug?), crdts-and-eventual-consistency
(§4.x?), complexity-classes-p-np (§5.x?), binary-search (§3.1?).

---
title: Ingest §7.1 software engineering fundamentals
type: log
section: "7.1"
tags: [ingest, software-engineering, brooks, parnas, agile, technical-debt, modularity]
summary: Read the SWE at Google table of contents, the full abstract/introduction of "No Silver Bullet", the introduction of Parnas 1971, and the twelve Agile principles; wrote 3 concepts (software-engineering-fundamentals and technical-debt-and-maintenance were wanted) and 1 combined source; linked the existing §2.6 pages (code-review, refactoring, unit-testing, debugging, git-data-model, build-systems-and-make, design-patterns-catalog).
---
## [2026-09-02] ingest | §7.1 Software engineering fundamentals

Read: abseil.io SWE-book ToC (thesis chapter subsections: Hyrum's law, hash ordering,
policies that scale, compiler upgrade, shifting left, markers, distributed builds; culture
part: help me hide my code, the genius myth, hiding considered harmful, bus factor);
Brooks 1986 TR86-020 abstract and §1 (essence/accident, "unless it is more than 9/10 of all
effort", the four prescriptions, "skepticism is not pessimism"); Parnas CMU-CS-71-101
abstract and introduction ("if programmers sang hymns"; the criteria question); the twelve
Agile principles verbatim. Mythical Man-Month, Code Complete, Pragmatic Programmer,
Sommerville, Royce, Boehm, Conway, Lehman, Peopleware, Feathers, Ousterhout from memory.

Source: [[software-engineering-texts-courses-and-seminal-papers]].
Concepts: [[software-engineering-fundamentals]] (wanted), [[modularity-and-information-hiding]],
[[technical-debt-and-maintenance]] (wanted).

Insights: Parnas' "decompose by decisions likely to change, not by flowchart" is the same
argument as the end-to-end paper's "put the function where the knowledge is" and as
Codd's data independence — three fields discovering that interfaces should be chosen by
what varies. Hyrum's law is Lehman's law I seen from the API provider's side; Sculley's
CACE is Parnas violated at the feature level. "No Silver Bullet" is a falsifiable claim
with a number (10× in a decade) — the right frame for AI coding tools: they attack
accidents (typing, boilerplate, lookup) and some essence (requirements conversation,
prototyping speed), and Brooks' list says which. Royce's waterfall paper arguing against
waterfall is the field's founding misreading. Technical debt's "interest" is exactly the
amortized-cost view of [[amortized-analysis]]: a cheap operation now paid for by expensive
ones later.

Applied the question-heading rule from Finding 8 proactively? Not yet — headings here are
descriptive; will add practitioner questions if the eval flags misses.

Forward wanted slugs: continuous-integration-and-delivery, software-architecture-and-system-design
(§7.3), api-design, dependency-management-and-packaging, developer-tooling-and-workflow
(check §2.6 slug), design-by-contract (§7.2), fuzzing (§7.2), abstract-data-types-and-interfaces
(check §2 slug), database-schema-evolution, human-computer-interaction (§9?),
amortized-analysis (check §3 slug).

---
title: Ingest §6.9 ML systems, MLOps and data engineering
type: log
section: "6.9"
tags: [ingest, mlops, ml-systems, distributed-training, inference, quantization]
summary: Read the CS329S syllabus; wrote 3 concepts (mlops-and-ml-systems, distributed-training-and-ml-systems, llm-inference-and-serving — all wanted) and 1 combined source.
---
## [2026-09-02] ingest | §6.9 ML systems & MLOps

Read: Stanford CS329S syllabus (lecture sequence from "understanding ML production" through
deployment, drift/monitoring, continual learning, infrastructure, responsible AI). Huyen's
book, Sculley's hidden-technical-debt paper, 10-714, Han's 6.5940, ZeRO/Megatron/GPipe/
vLLM/GPTQ from memory (well known to me). Reis & Housley from memory.

Source: [[ml-systems-and-mlops-texts-courses-and-seminal-papers]].
Concepts: [[mlops-and-ml-systems]] (wanted), [[distributed-training-and-ml-systems]]
(wanted), [[llm-inference-and-serving]] (wanted).

Insights: three sections of the curriculum converge here. Decode is a [[roofline-model]]
problem (intensity ≈ batch size), PagedAttention is [[virtual-memory]], ring all-reduce is
the bandwidth-optimal collective of [[parallel-programming-models]], and 3D parallelism is a
placement problem the [[query-optimization]] chapter would recognize (a cost model over
partitionings). Sculley's CACE is Parnas' information hiding failing — features are a
module interface nobody declared. Speculative decoding is a rejection-sampling argument
from [[monte-carlo-methods]] used as a systems trick: the exact-distribution guarantee is what
makes it deployable. The MLOps page is the one where the wiki links back to §7–§8 topics
that don't exist yet (software-engineering-fundamentals, technical-debt-and-maintenance,
differential-privacy) — those slugs are now wanted and will be filled in §7/§8.

Forward wanted slugs: hardware-accelerators (§4.1 or §11?), memory-hierarchy-and-caches
(check §4.1 slug), software-engineering-fundamentals, technical-debt-and-maintenance (§7.1),
differential-privacy (§8.x / §6.11).

---
title: Ingest §6.8 learning theory
type: log
section: "6.8"
tags: [ingest, learning-theory, pac, vc, rademacher, online-learning, ntk, double-descent]
summary: Read Mohri's book page, the UML front matter (from §6.2), and the Belkin double-descent abstract; wrote 2 concepts (statistical-learning-theory and online-learning-and-regret — both wanted) and 1 combined source.
---
## [2026-09-02] ingest | §6.8 Learning theory

Read: Belkin, Hsu, Ma & Mandal 2019 abstract in full ("the bias-variance trade-off appears
to be at odds with the observed behavior … very rich models such as neural networks are
trained to exactly fit … and yet they often obtain high accuracy … 'double descent' curve
subsumes the textbook U-shaped curve"); Mohri's book page (1.3 kB — nav only); UML's
preface/structure (fetched in §6.2). Vershynin, Wainwright, Cesa-Bianchi & Lugosi, Ma's
STATS214 notes, and the papers from memory.

Source: [[learning-theory-texts-courses-and-seminal-papers]].
Concepts: [[statistical-learning-theory]] (wanted — referenced by seven earlier pages),
[[online-learning-and-regret]] (wanted).

Insights: the whole batch theory is one move — replace the union bound over hypotheses by a
union bound over *behaviours on the sample* (Sauer–Shelah, symmetrization) — and Rademacher
complexity is that move made data-dependent. Online learning removes the distribution
altogether and still gets √T; online-to-batch then *re-derives* SGD's statistical rate
without uniform convergence, which is the cleaner explanation of why one pass of SGD works
([[gradient-descent]]). Hedge = FTRL with entropy = mirror descent on the simplex = AdaBoost
= the multiplicative-weights LP solver of [[approximation-algorithms]] = the constructive
minimax theorem: one algorithm, five sections of the curriculum. Deep-learning theory's
state is honest in the page: NTK explains convergence in the lazy regime, implicit bias
explains which interpolant GD picks, benign overfitting explains why interpolating can be
fine, and none of them predicts [[scaling-laws]]. Littlestone dimension ⇔ private
learnability is the kind of equivalence that would have been a §5 highlight.

Section §6 is now 8 of 11 done (6.9 ML systems, 6.10 robotics, 6.11 safety remain).
Forward wanted slugs: game-theory (now referenced by ~6 pages — write it in §6.11 or the
synthesis pass), data-compression (check §1.7 slug), approximation-algorithms (check §3).

---
title: Ingest §6.7 probabilistic graphical models and Bayesian methods
type: log
section: "6.7"
tags: [ingest, pgm, mcmc, variational-inference, bayesian, causal]
summary: Read the CS228 notes' full contents page; wrote 5 concepts (probabilistic-graphical-models, monte-carlo-methods, bayesian-inference, causal-inference were wanted) plus variational-inference, and 1 combined source.
---
## [2026-09-02] ingest | §6.7 PGMs & Bayesian methods

Read: CS228 notes contents (Ermon; four parts — representation, inference, learning,
"bringing it together" with the VAE — with every subsection listed). Koller & Friedman,
MacKay, BDA3, GPML, Pearl, Neal's HMC and Hoffman–Gelman NUTS from memory (I know these
texts). Barber not fetched.

Source: [[pgm-and-bayesian-texts-courses-and-seminal-papers]].
Concepts: [[probabilistic-graphical-models]] (wanted), [[monte-carlo-methods]] (wanted —
the slug was requested by §3 and §6 pages; this page covers MC estimation, importance
sampling, MCMC/HMC/NUTS, SMC, and the randomized-algorithms sense),
[[variational-inference]], [[bayesian-inference]] (wanted), [[causal-inference]] (wanted).

Insights: inference on a factor graph is [[dynamic-programming]] over a tree decomposition
— the same treewidth that governs CSPs, database join trees, and Bayes nets; the junction
tree is "run VE once, cache all messages". MCMC and VI are the two ways to avoid computing
a partition function: run a chain that only needs ratios, or optimize a bound that only
needs expectations under q. Loopy BP being a stationary point of the Bethe free energy
ties the LDPC decoders of §1.7 to variational inference. The reverse-KL variance
underestimation is the mirror of MLE's forward-KL moment matching — the same asymmetry
that separates mode-seeking GANs from mode-covering likelihood models in §6.3. HMC is
gradient descent's Hamiltonian cousin — [[deep-learning-basics]]'s autodiff made it
practical. Pearl's do-operator is graph surgery — deleting incoming edges — the exact dual of
[[abstract-interpretation]]'s "modify the program, keep the semantics": modify the model,
ask what the data would be. The Bayesian workflow's prior/posterior predictive checks are
unit tests for models.

Forward wanted slugs: fairness-in-machine-learning, interpretability-and-explainability
(§6.11), randomized-algorithms (check §3 slug), hashing-and-randomness (check),
probability-and-statistics-for-cs (still wanted — §1.4 has specific pages;
consider a hub page in the syntheses pass).

---
title: Ingest §6.6 reinforcement learning
type: log
section: "6.6"
tags: [ingest, reinforcement-learning, td, q-learning, policy-gradient, ppo, sac, bandits]
summary: Read Spinning Up's Part 1 structure and algorithm docs list and the CS285 course page; wrote 3 concepts (reinforcement-learning-basics, deep-reinforcement-learning, multi-armed-bandits — all wanted) and 1 combined source.
---
## [2026-09-02] ingest | §6.6 Reinforcement learning

Read: OpenAI Spinning Up — Part 1 key-concepts outline (states/observations, action spaces,
deterministic vs stochastic policies, trajectories, reward and return, value functions,
optimal Q, Bellman equations, advantage), Part 2/3 titles, algorithm docs (VPG, TRPO, PPO,
DDPG, TD3, SAC); CS285 course page (Levine). Sutton & Barto's site returned only 619
bytes; the book's structure is from memory (I know it chapter by chapter). Lattimore &
Szepesvári, Silver's lectures, and the papers from memory.

Source: [[reinforcement-learning-texts-courses-and-seminal-papers]].
Concepts: [[reinforcement-learning-basics]] (wanted), [[deep-reinforcement-learning]]
(wanted), [[multi-armed-bandits]] (wanted). §6.1's [[markov-decision-processes]] remains the
MDP/value-iteration/Q-learning foundation and is linked, not repeated.

Insights: Sutton & Barto's "dimensions" (backup width × depth × on/off-policy × model)
is the cleanest algorithm taxonomy in the curriculum — every deep RL method is a point in
it plus a stabilization trick. The deadly triad is the RL name for the same instability
[[neural-network-training]] fights with target networks and clipping: a bootstrapped
target that moves with the parameters. PPO's clip, TRPO's KL, SAC's entropy, and RLHF's KL
penalty are one idea — regularize the policy toward where your data came from — which is
also offline RL's whole problem (CQL/IQL) and the reason DPO works
([[llm-post-training-sft-rlhf-dpo]]). UCB's optimism is [[concentration-inequalities]]
turned into a decision rule; Thompson sampling is [[bayesian-inference]] turned into one;
UCT is the reason [[adversarial-search-and-game-trees]] got AlphaGo. The bandit lower
bound (Lai–Robbins: log T / KL) is an information-theoretic argument of the §1.7 kind.

Forward wanted slugs: online-learning-and-regret (§6.8), bayesian-inference (§6.7),
causal-inference (§6.7/6.9), robotics-and-autonomous-systems (§6.10),
ai-safety-and-alignment (§6.11), game-theory (§3.x / §6.x).

---
title: Ingest §6.5 computer vision
type: log
section: "6.5"
tags: [ingest, computer-vision, geometry, sift, nerf, clip, self-supervised]
summary: Read Szeliski's book site (course adoption list; chapter structure from the 2e ToC); wrote 3 concepts (computer-vision-fundamentals and self-supervised-and-contrastive-learning were wanted) and 1 combined source. CS231n detection/segmentation content was already covered in §6.3's CNN page and is linked, not duplicated.
---
## [2026-09-02] ingest | §6.5 Computer vision

Read: szeliski.org/Book (2e 2022 chapter list and the ~15 courses adopting it — Cornell
Tech, MIT 6.8300, CMU 16-385, Berkeley CS194-26, Brown, Georgia Tech, Michigan EECS 498/504);
CS231n 2025 schedule (from §6.3). Hartley & Zisserman, Nayar's lectures, Torralba–Isola–
Freeman, and the paper list from memory. Detection/segmentation architectures live in
[[convolutional-neural-networks]] (§6.3) and are linked rather than repeated.

Source: [[computer-vision-texts-courses-and-seminal-papers]].
Concepts: [[computer-vision-fundamentals]] (wanted), [[multiple-view-geometry-and-3d-vision]],
[[self-supervised-and-contrastive-learning]] (wanted).

Insights: classical vision is a catalogue of hand-designed invariances (SIFT: scale,
rotation, illumination; HOG: local photometric; Viola–Jones: speed via prefix sums — the
integral image is a 2-D [[prefix-sums-and-scans]]), and self-supervised learning is the
same catalogue expressed as augmentations — "which invariances do I want" moved from the
descriptor to the data pipeline. Epipolar geometry is the rank-2 constraint that makes
two-view reconstruction a linear algebra problem; bundle adjustment is sparse
Gauss–Newton with the same Schur-complement trick as [[sparse-linear-algebra]] solvers.
NeRF and Gaussian splatting close the loop with graphics: reconstruction is now
gradient descent through a renderer ([[computer-graphics-rendering]]), the vision-side
analogue of "differentiable everything". InfoNCE = word2vec negative sampling = CLIP = the
retriever training objective behind [[dense-retrieval-and-embeddings]] — one loss across
§6.4, §6.5 and §10.3.

Forward wanted slugs: signals-and-sampling (check §1/§4 for an existing DSP page),
computational-photography, computer-graphics-rendering (§9?), nonlinear-optimization,
sparse-linear-algebra (check §1.2), prefix-sums-and-scans.

---
title: Ingest §6.4 NLP and LLMs
type: log
section: "6.4"
tags: [ingest, nlp, llm, scaling-laws, rlhf, dpo, tokenization]
summary: Read the SLP3 2026 draft's front page and volume structure, CS224N/CS336 pages (CS336's five assignments), and the Kaplan scaling-laws abstract; wrote 4 concepts (nlp-fundamentals, large-language-models, scaling-laws were wanted) plus llm-post-training-sft-rlhf-dpo, and 1 combined source.
---
## [2026-09-02] ingest | §6.4 NLP & LLMs

Read: SLP3 front page (release of 19 Aug 2026 — Volume I is now titled "Large Language
Models", transformers merged into the neural-LM chapter, a new interpretability chapter,
HMMs/CFGs demoted to appendices; the authors used Claude Opus 5 to draft exercises);
CS224N course page (video years 2017–2024); CS336 spring 2025 page — assignments basics /
systems (FlashAttention in Triton, DDP, optimizer sharding) / scaling / data / alignment &
reasoning RL; Kaplan et al. abstract in full. CS324 notes, InstructGPT, DPO, LoRA, R1 and
the rest from memory (I know these papers well).

Source: [[nlp-and-llm-courses-texts-and-seminal-papers]].
Concepts: [[nlp-fundamentals]] (wanted), [[large-language-models]] (wanted), [[scaling-laws]]
(wanted), [[llm-post-training-sft-rlhf-dpo]].

Insights: the textbook's reorganization is the clearest evidence of what happened to the
field — a book once organized by linguistic level (words → syntax → semantics → discourse)
is now organized by model stage (pretrain → fine-tune → align → interpret), with the
linguistics moved to Volume III. Three ideas recur from earlier sections: perplexity is
[[entropy-and-information]]'s cross-entropy, the KV cache is a [[roofline-model]] problem
(decode is memory-bound), and RAG is [[bm25]] + [[dense-retrieval-and-embeddings]] glued to
a prompt — the o-cs/oasis setup itself. DPO's derivation (closed-form optimum of
KL-regularized RL → reward implicit in the log-ratio) is the same move as
[[curry-howard-correspondence]]-style "the object you were searching for is already the
proof": the policy *is* the reward model. Chinchilla vs overtraining is a training-cost vs
inference-cost trade — an [[performance-equation-and-amdahl]]-style total-cost argument.
Reasoning RL (verifiable rewards) is the "self-improvement" item of the Dartmouth proposal
finally done, seventy years later.

Forward wanted slugs: llm-inference-and-serving, llm-evaluation-and-benchmarks,
llm-agents-and-tool-use (§6.4/6.9), dense-retrieval-and-embeddings / bm25 /
evaluation-of-ir-systems / tf-idf-and-vector-space-model (§10.3 — check existing bm25 page
slug), fairness-in-machine-learning (§6.11), transfer-learning-and-fine-tuning,
deep-reinforcement-learning (§6.6), web-security (§8), virtual-memory-and-paging (check §4.1
slug), string-algorithms (check §3).

---
title: Ingest §6.3 deep learning
type: log
section: "6.3"
tags: [ingest, deep-learning, cnn, rnn, transformers, diffusion, training]
summary: Read the Goodfellow ToC and the CS231n 2025 schedule (D2L and UDL sites returned nav/empty); wrote 6 concepts (deep-learning-basics, neural-network-training, transformers-and-attention, deep-generative-models were all wanted) and 1 combined source.
---
## [2026-09-02] ingest | §6.3 Deep learning

Read: deeplearningbook.org table of contents (20 chapters in three parts); CS231n spring
2025 schedule (17 lectures — half the course is now transformers, self-supervision,
generative models, 3D, vision-language and world models; suggested readings name ViT,
DETR, DINO, ELBO). D2L returned only its nav; udlbook.github.io returned 2 bytes. Nielsen,
Prince, Karpathy's Zero to Hero, and the seminal papers from memory (I have read them).

Source: [[deep-learning-texts-courses-and-seminal-papers]].
Concepts: [[deep-learning-basics]] (wanted), [[neural-network-training]] (wanted),
[[convolutional-neural-networks]], [[recurrent-neural-networks-and-lstms]],
[[transformers-and-attention]] (wanted), [[deep-generative-models]] (wanted).

Insights: three separate inventions are the same trick — LSTM's additive cell (1997),
ResNet's skip (2015), and the transformer's residual stream (2017) all give the gradient an
identity path; the field re-discovers "make the Jacobian product contain an I" every time
depth (in time, in layers) is pushed. Attention is a soft hash-table lookup, and the KV
cache is the table — so the serving-cost story is the memory-hierarchy story of §4
([[roofline-model]]) again: FlashAttention is cache-blocking. Diffusion's loss is the ELBO
of [[unsupervised-learning-em-and-mixture-models]] applied to a Markov chain of latents,
and denoising score matching is the same object as ICA's non-Gaussianity: a learned
gradient of log-density. Zhang et al. 2017 is the deep-learning counterpart of natural
proofs: a demonstration that the classical explanatory tool (capacity bounds) cannot
distinguish the good case from the bad case.

Search note: in §6.2 the paraphrase query "how many training examples do I need" ranked
10th; adding those exact words to the relevant heading moved it to rank 1 with no other
change. That is the cheapest possible "you might ask" intervention — record as a finding
and apply to future paraphrase misses.

Forward wanted slugs: distributed-training-and-ml-systems, transfer-learning-and-fine-tuning,
self-supervised-and-contrastive-learning, efficient-transformers-and-long-context,
dense-retrieval-and-embeddings, llm-evaluation-and-benchmarks, computer-vision-fundamentals,
scaling-laws, prefix-sums-and-scans (check §3), bipartite-matching (check §3).

---
title: Ingest §6.2 machine learning
type: log
section: "6.2"
tags: [ingest, machine-learning, cs229, svm, boosting, em, generalization]
summary: Read the CS229 2026 lecture-notes ToC (19 chapters incl. diffusion, LLMs, RLVR) and UML's preface; wrote 6 concepts (machine-learning-basics was wanted) and 1 combined source; linked existing k-means, SVD/PCA, MLE, gradient-descent, convexity pages.
---
## [2026-09-02] ingest | §6.2 Machine learning

Read: CS229 lecture notes (Ma & Ng, 2026 edition) full table of contents — Parts I–VI; the
notes now carry diffusion models, foundation models (LoRA, contrastive learning, RAG), LLMs
(tokenization, transformers, MoE, in-context learning, SFT) and "Reasoning in LLMs"
(chain-of-thought, RLVR) before the RL chapter, which is a useful timestamp on what "intro
ML" means in 2026; Understanding Machine Learning preface and four-part structure (PAC/ERM/
SRM/MDL/no-free-lunch → algorithms → additional models → advanced theory). ESL site returned
nothing (2 bytes). ISLR/ESL/Bishop/Murphy/Abu-Mostafa and the seminal papers from memory.

Source: [[ml-courses-texts-and-seminal-papers]].
Concepts: [[machine-learning-basics]] (wanted), [[linear-models-logistic-regression-and-glms]],
[[kernels-and-support-vector-machines]], [[decision-trees-and-ensembles]],
[[generalization-bias-variance-and-regularization]],
[[unsupervised-learning-em-and-mixture-models]]. Existing pages linked rather than
duplicated: [[k-means-clustering]], [[svd-and-pca]], [[maximum-likelihood-estimation]],
[[gradient-descent]], [[convexity]], [[entropy-and-information]].

Insights: the GLM chapter is the unifying trick of classical ML — the sigmoid, softmax and
identity links are *derived* from the exponential family, which is why LMS, logistic and
softmax regression share one update rule. EM's "coordinate ascent on the ELBO" is the same
shape as CSP/SAT propagation and value iteration: fix one half, optimize the other, prove
monotonicity by a bound. The finite-H sample-complexity bound (log k) is the argument every
practitioner should be able to reproduce; it explains why parameter count is the wrong
complexity measure and sets up double descent. XGBoost's split gain is a second-order
Newton step per leaf — Newton's method in function space, as GBM is gradient descent in
function space. Trees vs kernels vs nets maps onto heterogeneous-tabular vs small-dense vs
perceptual data; the o-cs wiki's own ranking problem is "tabular with a few features", which
is why an RRF/BM25 tweak beats a model for now.

Forward wanted slugs for later sections: statistical-learning-theory (§6.8),
deep-learning-basics / deep-generative-models / scaling-laws (§6.3), bayesian-inference and
probabilistic-graphical-models (§6.7), interpretability-and-explainability (§6.11),
mlops-and-ml-systems (§6.9), learning-to-rank / evaluation-of-ir-systems (§10.3),
concentration-inequalities, kolmogorov-complexity-and-mdl, causal-inference, hypothesis-testing.

---
title: Ingest §6.11 AI safety, alignment, ethics, fairness and interpretability
type: log
section: "6.11"
tags: [ingest, ai-safety, alignment, fairness, interpretability, differential-privacy]
summary: Read the fairmlbook contents page and the Concrete Problems abstract; wrote 4 concepts (ai-safety-and-alignment, fairness-in-machine-learning, interpretability-and-explainability, differential-privacy — all wanted) and 1 combined source. §6 (AI/ML, 11 subsections) is complete.
---
## [2026-09-02] ingest | §6.11 Safety, fairness, interpretability

Read: fairmlbook.org contents (nine chapters — legitimacy, classification criteria,
relative fairness, causality, U.S. law, testing discrimination, structural
discrimination, datasets — plus the "21 definitions and their politics" tutorial and
course list); Amodei et al. 2016 abstract in full (five problems in three causal buckets:
wrong objective / expensive objective / learning process). Molnar, Christian, Russell,
the Anthropic interpretability papers, Dwork & Roth, DP-SGD from memory (I know these
well).

Source: [[ai-safety-fairness-and-interpretability-texts-courses-and-seminal-papers]].
Concepts: [[ai-safety-and-alignment]] (wanted — referenced by 10+ pages),
[[fairness-in-machine-learning]] (wanted), [[interpretability-and-explainability]] (wanted),
[[differential-privacy]] (wanted; the §8 security tag list also names it — this page is the
ML side, §8 can add the systems/crypto side).

Insights: the fairness impossibility theorem is a base-rate identity — the same Bayes'
rule that [[bayes-theorem-and-inference]] teaches with medical tests — turned into a
normative fork: calibration or equal error rates, choose. Concrete Problems' taxonomy is
"wrong objective / expensive objective / learning process", and every later alignment
failure (RLHF sycophancy, reward-model over-optimization, goal misgeneralization) files
under one of them; Goodhart is the through-line from [[mlops-and-ml-systems]] proxies to
[[llm-post-training-sft-rlhf-dpo]] reward hacking to [[causal-inference]]'s deployed-
predictor failure. Shapley values are [[game-theory]] used as an explanation axiom set.
Superposition is [[similarity-search-and-lsh]]'s nearly-orthogonal-vectors fact
(Johnson–Lindenstrauss) read as a property of learned representations, and sparse
autoencoders are the [[unsupervised-learning-em-and-mixture-models]] dictionary-learning
idea applied to activations. Differential privacy's composition is [[concentration-inequalities]]
in reverse (bound the divergence, then compose), and the Census reconstruction attack is
Dinur–Nissim's "too many accurate answers determine the data" — an information-theoretic
argument. Prompt injection is the [[web-security]] confused-deputy problem with a model as
the deputy.

**§6 complete (11/11).** Next: §7 software engineering (7.1–7.x), then §8 security, §9
graphics/HCI?, §10 IR/data, §11 misc, §12 paths; refresh the report at the §6 boundary.
Forward wanted slugs now heavily referenced: game-theory, web-security, security-principles,
llm-agents-and-tool-use, llm-evaluation-and-benchmarks, hardware-accelerators,
software-engineering-fundamentals, technical-debt-and-maintenance, computational-geometry,
nonlinear-optimization, sparse-linear-algebra, prefix-sums-and-scans, probability-and-statistics-for-cs.

---
title: Ingest §6.10 robotics and autonomous systems
type: log
section: "6.10"
tags: [ingest, robotics, kalman, slam, motion-planning, rrt, lqr, mpc, tedrake]
summary: Read chapters 1–2 of Tedrake's Robotic Manipulation and 1–3 of Underactuated Robotics (ToC level with section titles); wrote 3 concepts (robotics-and-autonomous-systems and state-estimation-and-kalman-filters were wanted) and 1 combined source.
---
## [2026-09-02] ingest | §6.10 Robotics

Read: manipulation.csail.mit.edu (ch. 1 "manipulation is more than pick-and-place",
open-world manipulation, simulation, model-based design; ch. 2 robot description files,
position- vs torque-controlled arms, link dynamics with transmissions, Kuka iiwa, hands —
dexterous/simple/soft — sensors); underactuated.mit.edu (ch. 1 fully-actuated vs
underactuated — ASIMO vs passive walkers, birds vs aircraft, feedback equivalence, input/
state constraints, nonholonomic constraints; ch. 2 the simple pendulum — overdamped/
undamped orbits, torque-limited with energy shaping; ch. 3 acrobot, cart-pole,
quadrotors). Thrun et al., Lynch & Park, LaValle, and the papers from memory.

Source: [[robotics-texts-courses-and-seminal-papers]].
Concepts: [[robotics-and-autonomous-systems]] (wanted), [[state-estimation-and-kalman-filters]]
(wanted), [[motion-planning-and-control]].

Insights: the Kalman filter is [[bayesian-inference]]'s Normal–Normal conjugate update run
recursively, and GraphSLAM is bundle adjustment ([[multiple-view-geometry-and-3d-vision]])
with odometry factors — one sparse least-squares solver serves vision and robotics. The
Bayes filter is the HMM forward algorithm of §6.1 with continuous state; MCL is the
particle filter of [[monte-carlo-methods]]. LQR's Riccati recursion is value iteration on a
quadratic value function; MPC is receding-horizon [[markov-decision-processes]] planning
with constraints; iLQR is Newton's method in trajectory space. RRT's Voronoi bias is the
same "explore where you haven't been" that [[multi-armed-bandits]] and RND formalize.
Tedrake's fully- vs underactuated split is a clean statement of when control is trivial
(feedback linearization) and when it isn't — the reason walking robots took thirty years
longer than arms. Control barrier functions as QP safety filters are the current answer to
"how do you deploy a learned policy" — a [[program-verification]]-style invariant enforced
at runtime.

§6 (AI/ML) is now 10 of 11; §6.11 safety/fairness/interpretability next.
Forward wanted slugs: computational-geometry (check §3 slug), nonlinear-optimization,
sparse-linear-algebra (both referenced by 5+ pages now — candidates for a §1.2/§3 addendum).

---
title: Ingest §6.1 introduction to AI
type: log
section: "6.1"
tags: [ingest, ai, cs188, aima, turing, search, csp, mdp, bayes-nets]
summary: Read Turing 1950 §1–2, the Dartmouth proposal, Poole & Mackworth 3e ToC, and the CS188 Fall 2024 calendar; wrote 6 concepts (search-algorithms-ai was wanted) and 1 combined source.
---
## [2026-09-02] ingest | §6.1 Introduction to AI

Read: Turing, "Computing Machinery and Intelligence" §1–2 (the imitation game and the
critique of the new problem: "drawing a fairly sharp line between the physical and the
intellectual capacities of a man"; the sonnet/arithmetic/chess specimen dialogue); the
Dartmouth proposal (all seven agenda items — "theory of the size of a calculation" is
complexity theory in 1955; "self-improvement" is RL); Poole & Mackworth 3e full ToC (19
chapters, seven parts — causality and knowledge graphs get chapters, which AIMA lacks);
CS188 Fall 2024 calendar (lectures 1–7 with AIMA chapter mapping; later weeks from memory
of the standard sequence). A* paper (Nilsson's site) fetch failed (3 bytes); OUP Turing
failed; UMBC mirror worked.

Source: [[ai-intro-courses-texts-and-seminal-papers]].
Concepts: [[search-algorithms-ai]] (wanted), [[constraint-satisfaction-problems]],
[[adversarial-search-and-game-trees]], [[markov-decision-processes]],
[[bayesian-networks-and-hmms]], [[intelligent-agents-and-ai-history]].

Insights: the intro-AI course is really four instances of one idea — "expectimax with
structure": minimax (adversary), expectimax (chance), value iteration (expectimax with reuse
and discount), and variable elimination (sum-product on a factor graph) are all DP over a
tree/graph, and CS188's Pacman is the fixture that makes that visible. Admissible
heuristics from relaxation are the same trick as LP relaxation in [[approximation-algorithms]]
and delete relaxation in planning: drop a constraint, solve exactly, use the answer as a
bound. AC-3 + no-good learning in CSPs is CDCL before CDCL ([[sat-and-smt-solvers]]).
Turing's "child machine" and Dartmouth's "self-improvement" item mean the learning program
of §6.2–6.6 was the original plan, not a later pivot.

New wanted slugs introduced deliberately for later sections: reinforcement-learning-basics
(§6.6), deep-reinforcement-learning (§6.6), probabilistic-graphical-models (§6.7),
machine-learning-basics (§6.2), deep-learning-basics (§6.3), nlp-fundamentals /
transformers-and-attention / large-language-models (§6.4), state-estimation-and-kalman-filters
/ robotics-and-autonomous-systems (§6.10), ai-safety-and-alignment (§6.11), game-theory,
multi-armed-bandits, first-order-logic, logic-programming, knowledge-graphs-and-ontologies.

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


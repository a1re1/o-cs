# PROGRESS — overnight study hall (started 2026-09-01 19:35 EDT)

**Read this first after any compaction.** Then `git log --oneline | head`, `tail -20 wiki/log.md`.

## Mission
Build a CS knowledge wiki (this repo) by reading every resource in `curriculum.md`, distilling into
`wiki/`, searchable via `oasis`. In parallel: evals + unit tests of search quality, skills for lci,
oasis improvements (PRs to ~/src/oasis), and a running experiments report (`reports/experiments.md`
+ published artifact linked from README).

## Operating loop (repeat until curriculum exhausted)
1. Pick next `[ ]` section below. Fetch 3–6 key resources with `scripts/fetch.py`, read critically.
2. Write source pages + concept pages + log entry (see CLAUDE.md). `scripts/build_index.py`.
3. Add 3–8 eval queries for the section to `evals/queries.jsonl`; run `evals/run_eval.py`.
4. Commit on a branch `ingest/<section>`, push, `gh pr create`, `gh pr merge --squash --delete-branch`.
5. Every ~5 sections: lint pass, update `reports/experiments.md`, republish artifact, update this file.
6. Delegate grunt work to lci: `lci --profile glm-5-3-flash --skill verify-before-done --json --max-iterations 12 "<DoD contract>"` in background.

## Status legend
`[ ]` not started · `[~]` in progress · `[x]` ingested · `[e]` evals added

## Sections
### 1 Foundations
- [x] 1.1 Discrete math (MCS Lehman/Leighton/Meyer, Levin, Book of Proof, CS70)
- [x] 1.2 Linear algebra (Strang 18.06, Hefferon, Boyd VMLS)
- [x] 1.3 Calculus (Strang Calculus, APEX)
- [x] 1.4 Probability & stats (Blitzstein Stat110, Bertsekas, CS109, Wasserman, Think Stats)
- [x] 1.5 Logic & computability (Open Logic, CS103, forall x)
- [x] 1.6 Optimization & numerics (Boyd CVX, Trefethen, 18.335)
- [x] 1.7 Information theory (MacKay, Cover&Thomas, Shannon 1948)
### 2 Programming
- [x] 2.1 Intro programming (SICP, HtDP, Composing Programs, CS61A, CS50)
- [ ] 2.2 Software construction (6.102, Ousterhout, Effective Java)
- [ ] 2.3 Systems programming C/Rust (CSAPP/15-213, CS107, Rust Book, Modern C, CS110L)
- [ ] 2.4 Functional programming (CS3110 OCaml, Hughes, Wadler monads, Backus, Okasaki)
- [ ] 2.5 OO design & patterns (GoF, Fowler Refactoring, Liskov&Wing, Parnas 1972)
- [ ] 2.6 Developer tooling (Missing Semester, Pro Git, TLCL, Make)
### 3 Algorithms
- [ ] 3.1 Data structures (CS61B, Sedgewick, Open Data Structures, 6.006)
- [ ] 3.2 Algorithms (CLRS, DPV, Erickson, Kleinberg-Tardos, CS161, 6.046)
- [ ] 3.3 Advanced algorithms (6.854, 6.851 Demaine, CS168, Williamson-Shmoys, seminal papers)
- [ ] 3.4 Competitive programming (CPH Laaksonen, USACO guide)
### 4 Systems
- [ ] 4.1 Architecture (CS61C, Nand2Tetris, P&H, H&P, Mutlu, seminal papers)
- [ ] 4.2 Operating systems (OSTEP, xv6 book, 6.1810, seminal papers)
- [ ] 4.3 Compilers (Crafting Interpreters, CS143, CS6120, SSA book, seminal papers)
- [ ] 4.4 Networks (CS144, Peterson&Davie, HPBN, Beej, RFCs, seminal papers)
- [ ] 4.5 Databases (15-445, CS186, Red Book, Hellerstein Architecture of a DBMS, seminal papers)
- [ ] 4.6 Distributed systems (6.5840, Kleppmann notes, DDIA-adjacent, seminal papers)
- [ ] 4.7 Parallel & HPC (CS149, 15-418, 6.172, McKenney, seminal papers)
- [ ] 4.8 Storage & datacenter (Datacenter as a Computer, SRE book, seminal papers)
- [ ] 4.9 Embedded & real-time (Lee&Seshia, EECS149, Liu&Layland)
### 5 Theory
- [ ] 5.1 Automata/computability/complexity (Sipser 18.404, Barak, Arora-Barak, seminal papers)
- [ ] 5.2 Advanced complexity (Arora-Barak, PCP, natural proofs, IP=PSPACE)
- [ ] 5.3 Cryptography (Boneh-Shoup, Joy of Cryptography, CS255, seminal papers)
- [ ] 5.4 PL theory & types (TAPL, Software Foundations, PFPL, PLAI, seminal papers)
- [ ] 5.5 Formal methods (TLA+, model checking, abstract interpretation, seL4, CompCert)
- [ ] 5.6 Quantum computing (de Wolf notes, Preskill, Qiskit, Shor/Grover)
### 6 AI/ML
- [ ] 6.1 Intro AI (CS188, AIMA, Poole&Mackworth, A*)
- [ ] 6.2 Machine learning (CS229 notes, ISLR, ESL, Shalev-Shwartz, Murphy, seminal papers)
- [ ] 6.3 Deep learning (Goodfellow, D2L, Prince UDL, CS231N, seminal papers)
- [ ] 6.4 NLP & LLMs (Jurafsky-Martin, CS224N, CS324, CS336, seminal papers)
- [ ] 6.5 Computer vision (Szeliski, CS231N, seminal papers)
- [ ] 6.6 Reinforcement learning (Sutton&Barto, CS285, Spinning Up, seminal papers)
- [ ] 6.7 PGMs & Bayesian (Koller-Friedman, Barber, CS228 notes, MCMC papers)
- [ ] 6.8 Learning theory (Shalev-Shwartz, Mohri, Vershynin, double descent/NTK)
- [ ] 6.9 ML systems (CS329S, 10-714, Sculley tech debt, ZeRO, vLLM, TVM)
- [ ] 6.10 Robotics (Tedrake, Modern Robotics, LaValle, Thrun)
- [ ] 6.11 AI safety/fairness (Fairness&ML, Molnar, Amodei 2016, interpretability)
### 7 Software engineering
- [ ] 7.1 SE fundamentals (SWE at Google, Brooks, Parnas, Conway, Agile)
- [ ] 7.2 Testing & analysis (Fuzzing Book, Debugging Book, QuickCheck, KLEE, delta debugging)
- [ ] 7.3 Architecture & system design (DDIA, system-design-primer, Fielding REST, AOSA, 500 lines)
- [ ] 7.4 DevOps/SRE (SRE book, Accelerate, chaos engineering, k8s docs)
- [ ] 7.5 Web (MDN, Eloquent JS, HPBN, Full Stack Open, HTTP spec)
- [ ] 7.6 Mobile (CS193p, Android Compose)
- [ ] 7.7 Open source practice (Fogel, Cathedral & Bazaar, licensing, supply chain)
- [ ] 7.8 Ethics & law (ACM code, Weizenbaum, CS181)
### 8 Security
- [ ] 8.1 Computer security (CS161 textbook, 6.858, Saltzer&Schroeder, Thompson, Aleph One, Spectre)
- [ ] 8.2 Offensive security & RE (pwn.college, OverTheWire, Nightmare)
- [ ] 8.3 Privacy (Dwork&Roth, Programming DP, k-anonymity, Tor, federated learning)
- [ ] 8.4 Blockchain (Nakamoto, Princeton Bitcoin book, Ethereum, selfish mining)
### 9 Human-centered
- [ ] 9.1 HCI (Norman, Bush, Engelbart, Fitts, Nielsen heuristics)
- [ ] 9.2 Graphics (15-462 Crane, PBR book, Ray Tracing in One Weekend, Kajiya)
- [ ] 9.3 Games & animation (Game Programming Patterns, Baraff&Witkin, Stable Fluids, ECS)
- [ ] 9.4 Data visualization (Wilke, Munzner, Cleveland&McGill, D3, Vega-Lite)
- [ ] 9.5 Social computing & graph ML (Easley&Kleinberg, MMDS, CS224W, PageRank, GCN)
### 10 Data
- [ ] 10.1 Data science (Data 8, Data 100, McKinney, R4DS)
- [ ] 10.2 Big data & mining (MMDS, MapReduce, Spark, MinHash, HyperLogLog, Count-Min, Dataflow)
- [ ] 10.3 Information retrieval (Manning IIR, Croft, CS276, BM25, DPR, ColBERT, HNSW)  ← also feeds oasis tuning
- [ ] 10.4 Knowledge representation (Brachman-Levesque, RDF/SPARQL, knowledge graphs)
### 11 Specialized
- [ ] 11.1 Comp bio (Compeau-Pevzner, Needleman-Wunsch, BLAST, BWT, AlphaFold)
- [ ] 11.2 Scientific computing (Heath, 18.335, AM205, autodiff)
- [ ] 11.3 Signal processing (Think DSP, 6.003, FFT, Rabiner HMM, CTC)
- [ ] 11.4 Computational geometry (de Berg, Graham scan, Fortune, Shewchuk)
- [ ] 11.5 Algorithmic game theory (Roughgarden 20 lectures, Nisan AGT, Nash, Vickrey, PoA)
- [ ] 11.6 History & essays (Dijkstra EWD, Hamming, Brooks, Gabriel, Perlis, Turing lectures)
### 12 Paths
- [ ] Learning-path pages (core spine + 7 tracks) with prerequisite edges

## Engineering track (interleaved)
- [x] E1 scaffold: CLAUDE.md, PROGRESS.md, scripts/build_index.py, scripts/lint.py, README
- [x] E2 evals: evals/queries.jsonl + evals/run_eval.py (recall@k, MRR, nDCG@3), results history
- [ ] E3 skills/oasis-search SKILL.md for lci + Claude (how to query, how to drill in with `show`)
- [ ] E4 LLM eval: lci answers CS questions with oasis; grade tool usage + answer quality
- [ ] E5 oasis improvements (candidates, in priority order — verify with evals first):
      frontmatter-aware indexing (title/tags into every chunk), `--filter path`, `--lexical-weight`,
      `serve` (MCP) command, stats on query, dedupe near-identical chunks, BM25 field weights
- [~] E6 reports/experiments.md + published artifact, linked from README

## Handoff notes (newest first)
- 2026-09-01 20:45 — §1.1 ingested (21 pages) and pushed to main. lci building evals/ in worktree .worktrees/lci-evals (branch eng/evals). Oasis finding: frontmatter becomes its own headingless chunk with snippet "---"; fix planned (E5). Next: §1.2.
- 2026-09-01 19:55 — scaffold in progress; nothing ingested yet; repo empty on origin (first push pending).

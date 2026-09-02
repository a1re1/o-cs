---
title: Formal methods seminal papers — Cousot & Cousot abstract interpretation (1977), Clarke & Emerson / Queille & Sifakis model checking (1981), Bryant's BDDs (1986), Biere et al. bounded model checking (1999), Jackson's Alloy (2002), de Moura & Bjørner's Z3 (2008), Leroy's CompCert (2009), Klein et al. seL4 (2009), Newcombe et al. "How Amazon Web Services Uses Formal Methods" (2015)
type: source
section: "5.5"
level: 500
tags: [cousot, abstract-interpretation, galois-connection, clarke-emerson, queille-sifakis, model-checking, ctl, bryant, bdd, binary-decision-diagrams, biere, bounded-model-checking, jackson, alloy, relational-logic, de-moura, bjorner, z3, smt, leroy, compcert, verified-compiler, klein, sel4, verified-kernel, newcombe, amazon, tla-plus-in-industry]
sources: []
authors: [Patrick Cousot, Radhia Cousot, Edmund Clarke, E. Allen Emerson, Jean-Pierre Queille, Joseph Sifakis, Randal Bryant, Armin Biere, Daniel Jackson, Leonardo de Moura, Nikolaj Bjørner, Xavier Leroy, Gerwin Klein, Chris Newcombe, Marc Brooker]
year: 1977
institution: various
url: https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf
license: various
format: pdf
summary: The Cousots showed that every static analysis is an abstract interpretation — execute the program over an abstract domain related to the concrete one by a Galois connection, compute fixpoints, and accelerate with widening — giving sound approximation a theory; Clarke & Emerson and Queille & Sifakis independently invented model checking: state properties in temporal logic and check them exhaustively over a finite-state model, algorithmically; Bryant's ordered binary decision diagrams made Boolean functions with 10²⁰ states canonical and compact, enabling symbolic model checking; Biere et al. replaced BDDs with SAT by unrolling k steps (bounded model checking), which scaled with the SAT revolution; Jackson's Alloy brought lightweight relational modeling with a small-scope analyzer; Z3 became the SMT solver every verifier calls; Leroy's CompCert proved a realistic C compiler correct in Coq (and Csmith found zero bugs in its verified core); Klein et al. proved seL4's C implementation refines its specification, with security properties later; and Newcombe et al. reported that AWS engineers use TLA+ and TLC on S3, DynamoDB and other services because testing cannot find "extremely rare" combinations of events at millions of requests per second — precise designs find bugs that code review and testing cannot.
---
# Formal methods seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Cousot & Cousot, "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints" (POPL 1977) | Concrete semantics as a fixpoint over a lattice; abstract domains (signs, intervals) linked by **Galois connections**; soundness by construction; **widening/narrowing** for convergence — the theory unifying dataflow analysis, type inference and verification | [[abstract-interpretation]], [[dataflow-analysis]] |
| Clarke & Emerson, "Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic" (1981); Queille & Sifakis (1982) | **Model checking**: specify in CTL, check a finite Kripke structure by fixpoint computation in time linear in model × formula; counterexamples for free; Turing Award 2007 | [[model-checking]] |
| Bryant, "Graph-Based Algorithms for Boolean Function Manipulation" (1986) | **ROBDDs**: canonical DAG representation of Boolean functions with efficient apply/quantification — the data structure behind symbolic model checking (Burch, Clarke, McMillan 1990: 10²⁰ states and beyond) and hardware verification | [[model-checking]], [[sat-and-smt-solvers]] |
| Biere, Cimatti, Clarke & Zhu, "Symbolic Model Checking without BDDs" (1999) | **Bounded model checking**: unroll the transition relation k times into a propositional formula and hand it to a SAT solver; finds shallow bugs in huge designs; k-induction and IC3/PDR (Bradley 2011) for unbounded proofs | [[model-checking]], [[sat-and-smt-solvers]] |
| Jackson, "Alloy: A Lightweight Object Modelling Notation" (2002); *Software Abstractions* | Relational first-order logic with transitive closure; the **small-scope hypothesis** (most bugs have small counterexamples) and a SAT-based analyzer; models of designs, protocols, data structures | [[model-checking]] |
| de Moura & Bjørner, "Z3: An Efficient SMT Solver" (2008) | DPLL(T) with theories (linear arithmetic, bit-vectors, arrays, uninterpreted functions, quantifiers via E-matching); the backend of Dafny, Boogie, F*, symbolic execution, and most verification tools | [[sat-and-smt-solvers]] |
| Leroy, "Formal Verification of a Realistic Compiler" (CACM 2009) | **CompCert**: Clight → PowerPC/ARM/x86 in ~20 passes, each proved semantics-preserving in Coq; Yang et al. (Csmith 2011) found no wrong-code bugs in its verified parts vs hundreds in GCC/LLVM | [[program-verification]], [[compilers-overview]] |
| Klein et al., "seL4: Formal Verification of an OS Kernel" (SOSP 2009) | Refinement proof in Isabelle/HOL from abstract spec to Haskell prototype to C (8,700 lines of C, 200,000 lines of proof); later integrity/confidentiality and binary-level proofs; the ~20 person-year cost and the bugs found | [[program-verification]], [[os-kernels-and-virtualization]] |
| Newcombe, Rath, Zhang, Munteanu, Brooker & Deardeuff, "How Amazon Web Services Uses Formal Methods" (CACM 2015) | Since 2011 AWS used TLA+ and TLC on S3, DynamoDB, EBS, and a lock manager; found serious bugs (e.g., a 35-step trace) that design review and testing missed; "human intuition is poor at estimating the true probability of supposedly extremely rare combinations of events"; precise designs improve thinking; what didn't work (liveness, proofs) | [[model-checking]], [[distributed-systems-basics]] |

## Why read them
Cousot & Cousot and Clarke & Emerson are the two theories every static tool descends from;
Bryant and Biere are the two engineering breakthroughs that made checking scale; Leroy and
Klein prove that full verification of real artifacts is possible; the Amazon paper is the
argument that convinces engineers.

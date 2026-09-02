---
title: Testing, debugging & program analysis — Zeller et al.'s The Fuzzing Book and The Debugging Book (free, executable), Claessen & Hughes' QuickCheck (ICFP 2000), Cadar, Dunbar & Engler's KLEE (OSDI 2008), Zeller & Hildebrandt's delta debugging (1999/2002), Godefroid et al.'s DART (2005), Zalewski's AFL, Jones & Harrold's Tarantula (2005), DeMillo, Lipton & Sayward's mutation testing (1978), Cousot & Cousot's abstract interpretation (1977), Bessey et al.'s "A few billion lines of code later" (Coverity, 2010), Myers' The Art of Software Testing, Beck's Test-Driven Development, Meszaros' xUnit Test Patterns; CMU 17-355, Saarland/CISPA courses
type: source
section: "7.2"
level: 400
tags: [fuzzing-book, debugging-book, zeller, gopinath, bohme, fraser, holler, quickcheck, claessen, hughes, klee, cadar, dunbar, engler, delta-debugging, ddmin, hildebrandt, dart, godefroid, klarlund, sen, afl, zalewski, aflfast, aflgo, tarantula, jones-harrold, ochiai, mutation-testing, demillo, lipton, sayward, abstract-interpretation, cousot, coverity, bessey, myers, art-of-software-testing, beck, tdd, meszaros, xunit-patterns, 17-355, program-analysis, symbolic-execution, statistical-debugging, automatic-repair]
sources: []
authors: [Andreas Zeller, Rahul Gopinath, Marcel Böhme, Gordon Fraser, Christian Holler, Koen Claessen, John Hughes, Cristian Cadar, Daniel Dunbar, Dawson Engler, Ralf Hildebrandt, Patrice Godefroid, Nils Klarlund, Koushik Sen, Michał Zalewski, James Jones, Mary Jean Harrold, Richard DeMillo, Richard Lipton, Frederick Sayward, Patrick Cousot, Radhia Cousot, Al Bessey, Glenford Myers, Kent Beck, Gerard Meszaros]
year: 2008
institution: CISPA / Chalmers / Stanford / Saarland / Microsoft Research / Coverity
url: https://www.fuzzingbook.org/
license: CC BY-NC-SA (books); ACM/USENIX papers
format: html
summary: The Fuzzing Book (Zeller, Gopinath, Böhme, Fraser & Holler; free Jupyter chapters, read: ToC, "Fuzzing: Breaking Things with Random Inputs" — Miller's 1990 random-string fuzzer, Fuzzer/Runner architecture, the bugs fuzzers find (buffer overflows, missing error checks, rogue numbers), generic and program-specific checkers — and "Greybox Fuzzing" — AFL's mutation + splicing, coverage feedback via a trampoline after every conditional jump, seeds, mutators, power schedules, AFLFast's energy for rare paths, AFLGo's directed distance schedule) organizes test generation as lexical (random, mutation, greybox, search-based, mutation analysis), syntactic (grammars, grammar coverage, probabilistic grammars, generators, reducing failure-inducing inputs), semantic (constraints, mining grammars, information flow, concolic and symbolic fuzzing, mining specifications) and domain-specific (configurations, APIs, carving unit tests, compilers, web, GUIs), plus managing fuzzing at scale and when to stop; The Debugging Book (Zeller; read: ToC, "Reducing Failure-Inducing Inputs" — the DeltaDebugger reducing '1 + 2 * 3 / 0' to '3/0', min_args/max_args/min_arg_diff, reducing code and syntax trees — and "Statistical Debugging" — correlating covered lines with pass/fail, Tarantula and Ochiai suspiciousness, discrete vs continuous spectra, "how useful is ranking?") covers observing executions (tracing, how debuggers work, assertions), tracking failure origins (slicing), reducing failure causes (delta debugging inputs and changes), abstracting failures (statistical debugging, mining specifications, generalizing circumstances, performance), automatic repair, and debugging in the large (tracking bugs, where the bugs are); QuickCheck (read: abstract and introduction — properties as Haskell functions checked on random inputs, a generator DSL under the tester's control because "it is meaningless to talk about random testing without discussing the distribution of test data", 300 lines, and the case studies' pitfalls) founded property-based testing; KLEE (read: abstract and introduction — symbolic input "initially allowed to be anything", path conditions solved for concrete tests, coverage over 90 % per Coreutils tool beating hand-written suites, 56 bugs in 452 programs including three Coreutils bugs missed for 15 years, cross-checking BusyBox vs Coreutils, the two concerns of path explosion and the environment problem) made symbolic execution practical; and the rest are the canonical papers behind each technique — ddmin, DART's concolic execution, AFL's design, Tarantula, mutation testing's competent-programmer and coupling hypotheses, abstract interpretation as the theory of sound static analysis, and Coverity's field report on why sound-but-noisy analyzers fail commercially — with Myers, Beck and Meszaros as the craft texts on test design, TDD and test-code smells.
---
# Testing, debugging & program analysis: sources

## What they are
- **The Fuzzing Book** (2019–, read: ToC + two chapters). Part I: introduction to testing;
  II lexical fuzzing (random inputs; code coverage; mutation-based; **greybox** — AFL,
  AFLFast, AFLGo; search-based; mutation analysis); III syntactic (grammars, efficient
  grammar fuzzing, grammar coverage, parsing, probabilistic grammars, generators,
  greybox with grammars, reducing failure-inducing inputs); IV semantic (constraints,
  mining input grammars, information flow, **concolic** and **symbolic** fuzzing, mining
  function specifications); V domain-specific (configurations, APIs, carving unit tests,
  compilers, web apps, GUIs); VI managing fuzzing (in the large, when to stop). Each
  chapter is a runnable notebook building a class (`Fuzzer`, `Runner`, `GreyboxFuzzer`,
  `PowerSchedule`, `Mutator`).
- **The Debugging Book** (2021–, read: ToC + two chapters). Observing executions (tracing,
  how debuggers work, asserting expectations); flows and dependencies (tracking failure
  origins — slicing); reducing failure causes (**delta debugging** for inputs and for
  changes); abstracting failures (**statistical debugging** — Tarantula/Ochiai; mining
  function specifications; generalizing failure circumstances; learning from failures;
  performance); automatic repair; debugging in the large (tracking bugs, where the bugs
  are). Companion: Zeller's *Why Programs Fail* (the scientific method of debugging).
- **QuickCheck** (Claessen & Hughes, ICFP 2000; read): properties as executable
  specifications, random generation with tester-controlled distributions, `Arbitrary`
  instances, observing distributions (`classify`, `collect`), conditional properties and
  the danger of vacuous ones, case studies; shrinking came with QuickCheck 2 and
  Hypothesis. Hughes' later "Testing the Hard Stuff and Staying Sane" (stateful models,
  finding bugs in Volvo/Klarna/LevelDB).
- **KLEE** (Cadar, Dunbar & Engler, OSDI 2008; read): symbolic execution on LLVM
  bitcode, compact state representation with copy-on-write, constraint-solving
  optimizations (caching, independence, implied values), search heuristics (random path +
  coverage-optimized), environment modelling via a symbolic file system; Coreutils results.
  Lineage: EXE (2006), **DART** (Godefroid, Klarlund & Sen 2005 — concolic: run concretely,
  collect path constraints, negate one, solve, repeat), CUTE, **SAGE** (Microsoft's whitebox
  fuzzer, one-third of Windows 7 file-fuzzing bugs), angr, Java PathFinder.
- **Delta debugging** (Zeller & Hildebrandt 1999/2002 "Simplifying and isolating failure-
  inducing input"; Zeller 1999 "Yesterday, my program worked. Today, it does not. Why?"):
  ddmin — minimize a failing input to a 1-minimal one; dd on change sets — isolate the
  failure-inducing change (the algorithmic form of `git bisect`).
- **AFL** (Zalewski 2013–): coverage-guided greybox fuzzing with a 64 KB edge-hit-count
  bitmap, fork server, deterministic then havoc mutation stages, splicing, corpus
  culling; libFuzzer, honggfuzz, OSS-Fuzz (Google, 2016– — thousands of bugs in open
  source), AFL++; **Böhme's** AFLFast (Markov-chain view, power schedules) and AFLGo.
- **Tarantula** (Jones & Harrold 2005) and Ochiai (Abreu et al. 2006): spectrum-based
  fault localization; Liblit's CBI (statistical debugging of deployed software).
- **Mutation testing** (DeMillo, Lipton & Sayward 1978; Hamlet 1977): the competent-
  programmer and coupling-effect hypotheses; mutation score as test-suite adequacy;
  equivalent mutants; PIT, mutmut; Google's "practical mutation testing at scale" (2021).
- **Abstract interpretation** (Cousot & Cousot 1977): sound static analysis as computing
  in an abstract domain (intervals, octagons, polyhedra) with Galois connections and
  widening; Astrée (proved Airbus flight code free of runtime errors).
- **Coverity** (Bessey et al., CACM 2010, "A few billion lines of code later"): unsound but
  useful checkers; false positives above ~30 % make users ignore the tool; the build is the
  enemy; "do no harm"; social factors dominate. Related: Infer (bi-abduction, Facebook),
  Clang static analyzer, ErrorProne, sanitizers (ASan/MSan/UBSan/TSan — Serebryany).
- **Craft texts**: Myers 1979 *The Art of Software Testing* (testing is trying to break
  the program; a good test finds an error; boundary values; equivalence partitioning;
  the triangle problem); Beck 2002 *TDD by Example* (red–green–refactor); Meszaros 2007
  *xUnit Test Patterns* (test smells, doubles taxonomy); Dijkstra 1970 ("testing shows
  the presence, not the absence of bugs"). Courses: CMU 17-355 Program Analysis (Aldrich
  & Le Goues; free notes), Saarland "Software Testing"/"Debugging" (Zeller), MIT 6.102
  testing unit, Berkeley CS169.

## Key ideas → pages
[[software-testing-fundamentals]], [[fuzzing]], [[property-based-testing]],
[[delta-debugging-and-fault-localization]], [[symbolic-execution-and-concolic-testing]],
[[static-and-dynamic-analysis-tools]], [[design-by-contract]]; existing:
[[unit-testing]], [[debugging]], [[program-verification]], [[model-checking]].

## What they add
The two Zeller books are the corpus's "how it actually works" for automated testing —
every technique as a few hundred lines of Python; QuickCheck and KLEE are the two papers
that turned testing into specification (properties) and into constraint solving (path
conditions); Coverity's report is the reality check that analysis tools live or die on
false-positive rates and build integration, not on soundness.

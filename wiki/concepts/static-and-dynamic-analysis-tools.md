---
title: Static and dynamic analysis tools in practice — the soundness/completeness/precision trade-off (why every useful tool is unsound or noisy), what static analyzers check (dataflow bugs, null/resource/taint, API misuse, concurrency, style), linters and type-based checks, industrial analyzers (Coverity's "a few billion lines of code later", Infer's bi-abduction, Clang Static Analyzer, ErrorProne, CodeQL, Semgrep, Astrée), false-positive economics and developer adoption, dynamic analysis and sanitizers (ASan, MSan, UBSan, TSan, Valgrind), and integrating analysis into review and CI
type: concept
section: "7.2"
level: 400
tags: [static-analysis, dynamic-analysis, soundness, completeness, precision, false-positives, false-negatives, rice-theorem, undecidability, linters, eslint, pylint, clippy, clang-tidy, type-checkers, mypy, typescript, dataflow-bugs, null-dereference, resource-leaks, taint-analysis, injection, api-misuse, concurrency-bugs, coverity, bessey, infer, bi-abduction, separation-logic, clang-static-analyzer, errorprone, codeql, semgrep, astree, abstract-interpretation, sound-analysis, unsound-analysis, heuristic-analysis, developer-adoption, tricorder, shift-left, sanitizers, asan, msan, ubsan, tsan, valgrind, shadow-memory, race-detection, happens-before, ci-integration, code-review-integration, suppressions, baseline, ratchet]
sources: [testing-and-program-analysis-texts-courses-and-seminal-papers]
summary: Program analysis tools sit between testing (which needs inputs and finds only what runs) and verification (which needs specifications and effort): static analyzers examine code without running it, and since Rice's theorem makes every non-trivial semantic property undecidable, each tool picks a corner of the sound/complete/precise triangle — sound tools (abstract interpretation as in Astrée, which proved Airbus code free of runtime errors) report every possible bug but over-approximate and need a closed world, while industrial tools (Coverity, Infer, Clang Static Analyzer, ErrorProne, CodeQL, Semgrep) are deliberately unsound and heuristic because, as Coverity's "A few billion lines of code later" reports, adoption is governed by false-positive rate (above ~30 % developers stop reading), by "do no harm" (never break the build), by the sheer variety of build systems, compilers and dialects, and by social factors (a true bug the developer doesn't believe is a false positive); what they find are dataflow bugs (null dereference, use-after-free, resource leaks, uninitialized reads via dataflow analysis), taint flows for injection vulnerabilities, API-protocol violations (lock/unlock, open/close), concurrency patterns, and style/complexity issues (linters, which are the cheapest and most-run analyzers), with type checkers (mypy, TypeScript, Rust's borrow checker) as the sound static analyses developers actually accept because they are part of the language; dynamic analysis instruments the running program instead — AddressSanitizer's shadow memory catches out-of-bounds and use-after-free at ~2× cost, MemorySanitizer uninitialized reads, UndefinedBehaviorSanitizer overflow and misalignment, ThreadSanitizer data races via happens-before vector clocks, Valgrind via binary instrumentation at 20–50× — trading coverage of only executed paths for zero false positives, which is why sanitizers are the oracle behind fuzzing; and the engineering that makes any of this stick is integration — analyzers running in code review (Google's Tricorder: results shown as review comments, with a "not useful" button that kills noisy checks), baselines and ratchets so legacy warnings don't block new code, suppressions with justification, and CI gates on new findings only.
---
# Static and dynamic analysis tools

**In one sentence.** Static analyzers find bug *patterns* on every path without inputs
but must choose between missing bugs and drowning developers in false alarms; dynamic
analyzers (sanitizers) find real bugs with no false alarms but only on the paths you
run — and both are worthless unless they show up where developers already look.

## Soundness, completeness, precision — why is every useful analyzer unsound or noisy? (Rice; Cousot)
By **Rice's theorem** ([[computability-and-halting-problem]]) no algorithm decides a
non-trivial semantic property of programs, so an analysis must approximate. A **sound**
analysis reports every real bug (no false negatives) by over-approximating behaviours —
and so reports spurious ones; a **complete** analysis reports only real bugs (no false
positives) but can miss some. **Precision** = how tight the approximation is (fewer
false alarms for a sound tool; fewer misses for an unsound one); cost grows with
precision (flow-, path-, context-, field-sensitivity — [[dataflow-analysis]]). Sound
tools ([[abstract-interpretation]]: intervals, octagons, polyhedra with widening; Astrée
proved the absence of runtime errors in Airbus A380 flight software — a closed,
loop-bounded, no-recursion, no-dynamic-allocation C subset) need a closed world and a
domain-tuned abstraction; "soundy" industrial tools assume no reflection, no
integer overflow, well-behaved libraries, and accept misses for usable alarm rates.
Type checkers are the sound analyses everyone accepts ([[type-systems]]: null-safety,
Rust's borrow checker as an ownership analysis) because the language makes the
approximation the programmer's contract.

## What static analyzers find (and the tools)
- **Linters / style / complexity** (ESLint, pylint/ruff, clippy, clang-tidy, golint,
  checkstyle): syntax-level patterns, unused variables, suspicious constructs (`==` vs
  `===`, shadowing), complexity thresholds, formatting (delegated to formatters). Cheapest,
  run on every save; a large share of production bugs are catchable at this level.
- **Dataflow bugs** ([[dataflow-analysis]]): null/undefined dereference, use-after-free,
  double free, uninitialized reads, resource leaks (file/lock/socket not closed on every
  path), dead stores, unreachable code; **Clang Static Analyzer** (path-sensitive symbolic
  simulation of the CFG with a solver-less constraint manager); **Infer** (Facebook/Meta,
  2015–: **bi-abduction** in **separation logic** infers pre/postconditions per procedure
  compositionally, so it scales to millions of lines and to incremental diff analysis —
  null, leaks, races via RacerD, and now Pulse); **Coverity** (path-sensitive, interprocedural,
  hundreds of checkers, 1 B+ lines/day in 2010).
- **Taint / security** ([[web-security]]): sources (user input) → sinks (SQL, shell, HTML,
  file paths) without sanitizers = injection; **CodeQL** (GitHub: code as a queryable
  database; variant analysis — write a query for one CVE's pattern, find all instances),
  **Semgrep** (syntactic pattern rules with lightweight taint), FindSecBugs, Bandit.
- **API protocols and typestate**: lock/unlock pairing, open/close, iterator
  invalidation, `must-use` results; **ErrorProne** (Google Java compiler plugin: bug
  patterns like `equals` on incompatible types, missing `@Override`, format-string
  mismatches, with auto-fixes) and its Kotlin/C++ cousins.
- **Concurrency**: lock-set and happens-before approximations for data races, deadlock
  cycles in lock graphs (RacerD, ThreadSafety annotations in Clang).
- **Metrics and architecture**: cyclomatic complexity, dependency-rule checks
  ([[technical-debt-and-maintenance]] hotspots).

## Coverity's field report: "A few billion lines of code later" (Bessey et al. 2010 — key claims)
Ten lessons from commercializing a research tool: (1) **the build is the enemy** — you
must intercept every compiler invocation in every weird build; (2) there are as many C
dialects as compilers — the parser must accept whatever the customer's compiler accepts;
(3) **do no harm**: a tool that breaks the build, crashes, or slows CI is uninstalled;
(4) **false positives matter more than false negatives** — above ~30 % users lose trust and
ignore *all* results; "a true bug that the user can't understand is a false positive";
(5) rank and explain results (path, cause); (6) soundness is not what buys adoption —
"we found more bugs with unsound checkers than sound ones"; (7) social factors: users
who don't believe a report, teams that can't act on findings in code they don't own,
"if it hasn't caused a problem in ten years it's not a bug"; (8) checkers that fire
rarely but precisely beat frequent noisy ones; (9) big customers want *no* churn in
results between versions; (10) the tool's job is to find bugs that developers will
*fix*. The same sociology drives **Tricorder** (Google's analysis platform: results as
code-review comments at the diff, a "not useful" button, checks with > 10 % not-useful
rate are removed, developers can write checks) — [[code-review]] as the delivery channel
makes analysis actually change code.

## Dynamic analysis: sanitizers and instrumentation
Instrument the compiled program (compiler passes) or the binary (Valgrind's JIT/DBI, Pin)
so violations become detectable at the moment they happen; no false positives (it
happened) but only on executed paths — hence the marriage with [[fuzzing]] and test
suites ([[software-testing-fundamentals]]). **AddressSanitizer** (Serebryany 2012): every 8
bytes of application memory map to 1 byte of **shadow memory** encoding addressability;
allocations get **redzones**, frees are quarantined; every load/store checks shadow →
detects heap/stack/global out-of-bounds, use-after-free, use-after-return/scope, double
free at ~2× time, 2–3× memory — the default for fuzzing C/C++
([[memory-safety-and-buffer-overflows]]). **MemorySanitizer**: bit-precise shadow of
initializedness → uninitialized reads. **UndefinedBehaviorSanitizer**: signed overflow,
shifts, misalignment, null, bounds on known arrays, invalid enum/bool, unreachable —
cheap, catches what compilers exploit ([[undefined-behavior]]). **ThreadSanitizer**:
shadow cells per memory word with the last accesses' thread + vector clock; reports a
**data race** when two accesses aren't ordered by happens-before (5–15× slower);
**LeakSanitizer**, **HWASan** (tag-based on AArch64), **KASan**/**KMSan** in the Linux kernel;
Valgrind's Memcheck (20–50×, no recompile), Helgrind/DRD; Java's JFR, Go's `-race` (TSan),
Rust's Miri (interpreter checking UB in `unsafe`). Also dynamic taint tracking
(information flow — Fuzzing Book "Tracking Information Flow"), coverage
instrumentation, profilers ([[profiling-and-performance]]), and record/replay (`rr`).

## Making it stick: integration and the ratchet
Run linters and type checks pre-commit/in the editor (seconds); analyzers in CI on the
diff (minutes; **incremental** analysis — Infer's diff mode, Coverity's desktop analysis);
deep/sound analysis nightly. Legacy codebases: establish a **baseline** (existing findings
suppressed) and **ratchet** — fail only on *new* findings; **suppressions** require a
justification comment and are reviewed; **severity tiers** (block merge / warn / info);
track fix rate per checker and delete noisy checkers. Analysis results as review comments
([[code-review]]) beat dashboards nobody opens. Complements: **contracts and assertions**
make dynamic checks program-specific ([[design-by-contract]]); **symbolic execution** sits
between static and dynamic ([[symbolic-execution-and-concolic-testing]]); **verification**
where analysis isn't enough ([[program-verification]], [[model-checking]]).

## Pitfalls
- Judging a tool by "bugs found" without the false-positive rate or fix rate.
- Turning on 500 checkers on day one → 10 000 warnings → the tool is muted by week two.
- Assuming a clean static analysis means correctness (unsound tools, modelled libraries).
- Running tests without sanitizers; running sanitizers on a non-representative subset.
- Suppressing without justification; letting the baseline grow.

## Related
- [[abstract-interpretation]], [[dataflow-analysis]], [[type-systems]],
  [[computability-and-halting-problem]], [[memory-safety-and-buffer-overflows]],
  [[undefined-behavior]], [[fuzzing]], [[software-testing-fundamentals]],
  [[symbolic-execution-and-concolic-testing]], [[design-by-contract]],
  [[program-verification]], [[model-checking]], [[code-review]], [[web-security]],
  [[profiling-and-performance]], [[technical-debt-and-maintenance]].

## Sources
Bessey et al. 2010 (CACM); Cousot & Cousot 1977; Calcagno et al. 2011/2015 (Infer, bi-abduction); Sadowski et al. 2015/2018 (Tricorder; "Lessons from building static analysis tools at Google"); Serebryany et al. 2012 (ASan), 2009 (TSan); Stepanov & Serebryany 2015 (MSan); Nethercote & Seward 2007 (Valgrind); Aftandilian et al. 2012 (ErrorProne); Livshits et al. 2015 ("In defense of soundiness"); Zeller et al., Fuzzing Book "Tracking Information Flow" (ToC read); Aldrich & Le Goues, CMU 17-355 notes.

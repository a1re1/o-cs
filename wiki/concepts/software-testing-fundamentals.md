---
title: Software testing fundamentals — what a test is (input, oracle, expected outcome), why testing can show the presence but not the absence of bugs, levels (unit, integration, system, acceptance, end-to-end) and the test pyramid, black-box design (equivalence partitioning, boundary values, decision tables, combinatorial/pairwise), white-box coverage criteria (statement, branch, condition/MC-DC, path) and what coverage does and doesn't mean, the oracle problem and test oracles (assertions, golden/snapshot, differential, metamorphic), test-driven development, regression tests, flaky tests and test determinism, mutation analysis as the honest adequacy metric, and testing at scale (test sizes, hermetic tests, CI)
type: concept
section: "7.2"
level: 300
tags: [software-testing, test-case, test-oracle, oracle-problem, dijkstra, presence-not-absence, test-levels, unit-tests, integration-tests, system-tests, acceptance-tests, end-to-end, test-pyramid, black-box, equivalence-partitioning, boundary-value-analysis, decision-tables, combinatorial-testing, pairwise, white-box, coverage, statement-coverage, branch-coverage, condition-coverage, mc-dc, path-coverage, coverage-criteria, coverage-myths, golden-master, snapshot-tests, differential-testing, metamorphic-testing, tdd, red-green-refactor, regression-tests, flaky-tests, determinism, hermetic-tests, test-sizes, mutation-analysis, mutation-score, equivalent-mutants, test-smells, myers, beck, meszaros]
sources: [testing-and-program-analysis-texts-courses-and-seminal-papers]
summary: A test is an input plus an oracle that decides whether the observed behaviour is acceptable, and because Dijkstra's remark holds — testing shows the presence of bugs, never their absence — the discipline is about choosing inputs that are likely to reveal faults and oracles that catch them cheaply; tests are organized by level (unit tests of one component in isolation with test doubles, integration tests across component boundaries, system/end-to-end tests through the real interfaces, acceptance tests written from the user's requirements) in a pyramid that keeps most tests small and fast; black-box design derives inputs from the specification (equivalence classes, boundary values — off-by-one bugs live at boundaries, decision tables, pairwise combinations since most interaction bugs involve two parameters), while white-box coverage criteria (statement, branch, condition and MC-DC as required by avionics standards, path) measure what the code exercised — a low number proves the suite is inadequate but a high number proves nothing, because coverage measures execution not checking; the oracle problem (how do you know the right answer?) is answered by explicit assertions, golden-master/snapshot files, differential testing against a reference implementation, and metamorphic relations (sin(x) = sin(π − x)) when no reference exists; test-driven development's red–green–refactor loop uses tests as design pressure, regression tests pin every fixed bug, and mutation analysis — inject small faults and count how many the suite kills — is the honest adequacy metric that coverage isn't; and the engineering realities are flaky tests (nondeterminism from time, ordering, concurrency, network — quarantine and fix, never retry into green), hermetic tests with controlled dependencies, test sizes by resource footprint, and continuous integration that makes the suite the gate on every change.
---
# Software testing fundamentals

**In one sentence.** Testing is a search for inputs that make the program disagree with an
oracle; since no finite search proves correctness, the craft is choosing inputs by
specification structure (partitions, boundaries) and code structure (coverage), building
oracles that are cheaper than the program, and treating the suite as engineered
infrastructure — small, fast, deterministic, and the gate on every change.

## What is a test? Why can't testing prove correctness? (Myers ch. 2; Dijkstra 1970)
A test case = an **input** (arguments, state, environment) + an **oracle** (expected output or
a property of the output). "Program testing can be used to show the presence of bugs, but
never to show their absence" (Dijkstra) — the input space is effectively infinite, so a
passing suite is evidence proportional to how the inputs were chosen. Myers: a
successful test is one that finds an error; test to break, not to confirm; the
**psychology** of testing — developers test gently, so have someone (or something —
[[fuzzing]]) hostile. The trade-off against [[program-verification]] and
[[model-checking]] (which do prove absence, for a model, at far higher cost) and against
[[type-systems]] (prove the absence of a class of bugs for free at every compile).

## Levels and the pyramid (SWE at Google ch. 11–14; Fowler)
**Unit** (one function/class, milliseconds, dependencies replaced by test doubles — fakes,
stubs, mocks; [[unit-testing]]), **integration** (real collaborators: DB, message queue,
two services), **system / end-to-end** (through the UI or public API, the deployed
configuration), **acceptance** (user stories' acceptance criteria — BDD's given/when/then;
[[software-engineering-fundamentals]]). The **test pyramid**: many unit, fewer
integration, few E2E — because cost, flakiness, and diagnosis time all grow up the
pyramid; the "ice-cream cone" anti-pattern inverts it. Google's alternative axis: **test
size** (small = single process, no I/O; medium = single machine; large = anything) with
size-based limits enforced by the runner, and **hermetic** tests (no network, fixed time,
seeded randomness) so results depend only on the code. Also: smoke tests, contract
tests at service boundaries, performance/load tests ([[profiling-and-performance]]),
security tests ([[fuzzing]]), and property tests ([[property-based-testing]]).

## Choosing inputs: black-box design (Myers ch. 4)
From the spec, not the code. **Equivalence partitioning**: divide inputs into classes
the program should treat alike; one representative each (valid and invalid classes).
**Boundary-value analysis**: test at, just below, and just above every boundary — empty,
one, max, max+1, 0, −1, 2³¹−1 — because off-by-one, overflow, and fencepost bugs live
there. **Decision tables** for combinations of conditions; **state-transition** tests for
stateful components (every transition, illegal transitions); **combinatorial / pairwise
(all-pairs)** testing — empirically most interaction faults involve ≤2 parameters, so
covering every pair of values across parameters (covering arrays) finds most of them at
a fraction of the full cross-product; **error guessing** (nulls, unicode, very long,
concurrent, clock skew). Myers' triangle problem (given three sides, classify the
triangle) is the classic exercise: most engineers list < half of the ~15 cases.

## Measuring: white-box coverage and what it means (Fuzzing Book "Code Coverage")
**Statement** coverage (each line executed), **branch/decision** (each branch outcome),
**condition** (each boolean sub-expression both ways), **MC/DC** (modified condition/decision:
each condition shown to independently affect the decision — DO-178C level A avionics),
**path** (every path — exponential; loops make it infinite), plus **mutation** coverage
(below) and data-flow criteria (def–use pairs). Subsumption: path ⊃ MC/DC ⊃ branch ⊃
statement. **What coverage means**: uncovered code is definitely untested — coverage is
a good *negative* signal and the guidance signal greybox fuzzers use ([[fuzzing]]); but
covered ≠ checked (a test that calls everything and asserts nothing has 100 % coverage),
so coverage targets invite gaming (Goodhart — [[ai-safety-and-alignment]] has the same
lesson). Use coverage to find gaps, never as a quality score. Tooling: gcov/llvm-cov,
coverage.py, JaCoCo; instrument via compiler (`-fprofile-arcs`), tracing (`sys.settrace`),
or bytecode.

## The oracle problem: how do I know what the right answer is?
Explicit **assertions** on outputs and post-state (the common case); **contracts** in the
code (pre/postconditions, invariants — [[design-by-contract]]) turn every execution into a
test; **golden master / snapshot** tests (record output once, diff thereafter — cheap,
brittle, great for legacy code, [[technical-debt-and-maintenance]]); **differential
testing** (compare against a reference implementation or a previous version — KLEE
cross-checking BusyBox vs Coreutils, compiler testing against another compiler,
[[symbolic-execution-and-concolic-testing]]); **metamorphic testing** (when no oracle
exists — a search engine, an ML model, a numerical solver — check relations between
outputs: adding a filter cannot increase results, permuting inputs doesn't change a
sort's output, sin(x) = sin(π − x)); **implicit oracles** — crashes, hangs, sanitizer
errors, exceptions, resource exhaustion (what fuzzers use); **N-version** and **property**
oracles ([[property-based-testing]]).

## TDD, regression, and mutation analysis (Beck 2002; DeMillo et al. 1978)
**TDD**: write a failing test (red), the simplest code to pass (green), refactor
([[refactoring]]); benefits are design pressure (testable = decoupled), a spec-first
habit, and a regression net; costs are test-code volume and over-mocking. **Regression
tests**: every fixed bug gets a test that reproduces it first (a reduced input —
[[delta-debugging-and-fault-localization]]); CI runs the suite on every change
([[continuous-integration-and-delivery]]). **Mutation analysis**: generate **mutants**
(small syntactic changes: `<` → `<=`, drop a statement, negate a condition, swap a
constant); a mutant is **killed** if some test fails on it; **mutation score** = killed /
non-equivalent mutants — the only adequacy metric that measures *checking*; the
**competent-programmer hypothesis** (real faults are small deviations from correct code)
and the **coupling effect** (tests that catch simple faults catch complex ones) justify
it; costs are runtime (thousands of mutants × suite; mitigated by sampling, incremental
mutation on changed lines — Google surfaces surviving mutants in code review) and
**equivalent mutants** (semantically identical — undecidable in general; the noise
floor). Test smells (Meszaros): fragile tests (over-specified mocks), obscure tests,
conditional logic in tests, slow tests, test interdependence.

## Flaky tests, determinism, and scale (SWE at Google ch. 11; Luo et al. 2014)
A **flaky** test passes and fails without code change — causes, in order of frequency:
async waits/timing, test order dependence and shared state, concurrency, resource
leaks, network, randomness, time/timezones, platform. Flakes destroy the signal (a 1 %
flake rate across 10 000 tests means every CI run fails); remedy: quarantine, then fix the
root cause — never auto-retry into green as policy; design tests hermetic (fake clock,
in-memory fakes, seeded RNG, no sleeps — wait on conditions). Suites at scale: sharding,
test selection by dependency graph ([[build-systems-and-make]] — Bazel runs only
affected tests), caching results by input hash, culling never-failing expensive tests.

## Pitfalls
- Treating coverage as a quality score; asserting nothing; testing implementation
  details (mocks that restate the code).
- Only "happy path" inputs; no boundaries, no invalid classes, no concurrency.
- Retrying flaky tests instead of fixing them; sleeps; tests that depend on order.
- E2E-heavy suites that take hours and fail for reasons unrelated to the change.
- Believing a green suite means correct — it means "no counterexample among these
  inputs"; use fuzzing/property tests to widen the search.

## Related
- [[unit-testing]], [[property-based-testing]], [[fuzzing]],
  [[delta-debugging-and-fault-localization]], [[symbolic-execution-and-concolic-testing]],
  [[static-and-dynamic-analysis-tools]], [[design-by-contract]],
  [[program-verification]], [[model-checking]], [[type-systems]], [[debugging]],
  [[refactoring]], [[continuous-integration-and-delivery]], [[build-systems-and-make]],
  [[software-engineering-fundamentals]], [[technical-debt-and-maintenance]].

## Sources
Myers 1979 (ch. 2, 4); Dijkstra 1970; Beck 2002; Meszaros 2007; DeMillo, Lipton & Sayward 1978; Zeller et al., Fuzzing Book "Introduction to Software Testing", "Code Coverage", "Mutation Analysis" (ToC read); Winters et al. 2020 ch. 11–14 (ToC read); Luo et al. 2014 (flaky tests); Petrović & Ivanković 2018/2021 (mutation testing at Google); Chen et al. 2018 (metamorphic testing survey).

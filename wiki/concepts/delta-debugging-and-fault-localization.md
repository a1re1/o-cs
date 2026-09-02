---
title: Delta debugging and fault localization — ddmin (simplify a failing input to a 1-minimal one), isolating failure-inducing differences (dd on inputs, on change sets: "yesterday my program worked, today it does not" and git bisect), reducing code and syntax trees (creduce), the scientific method of debugging (hypothesis, prediction, experiment), tracing and slicing to track failure origins, spectrum-based fault localization (Tarantula, Ochiai, suspiciousness ranking and how useful it is), statistical debugging of deployed software, and automatic program repair (GenProg, search- and semantics-based, LLM repair)
type: concept
section: "7.2"
level: 400
tags: [delta-debugging, ddmin, one-minimal, input-reduction, test-case-reduction, failure-inducing-input, failure-inducing-change, isolating-changes, git-bisect, bisection, zeller, hildebrandt, creduce, hierarchical-delta-debugging, hdd, syntax-tree-reduction, scientific-method, why-programs-fail, hypothesis, tracing, slicing, dynamic-slicing, dependency-tracking, failure-origins, fault-localization, spectrum-based, sbfl, tarantula, ochiai, suspiciousness, jones-harrold, statistical-debugging, cbi, liblit, predicates, automatic-repair, apr, genprog, patch-generation, plausible-patches, overfitting-patches, semantic-repair, llm-repair, debugging-book, minimal-reproducer, mre]
sources: [testing-and-program-analysis-texts-courses-and-seminal-papers]
summary: Debugging is the systematic narrowing of a failure to its cause, and its automatable core is delta debugging (Zeller & Hildebrandt): ddmin takes a failing input and a test that says pass/fail/unresolved, splits the input into n chunks, tries each chunk and each complement, keeps whichever still fails, doubles the granularity when nothing does, and stops at a 1-minimal input (removing any single chunk makes the failure disappear) in O(n²) tests worst case but typically O(log n) — the Debugging Book's DeltaDebugger reduces '1 + 2 * 3 / 0' to '3/0' and exposes min_args, max_args (largest passing) and min_arg_diff (the minimal failure-inducing difference); the same algorithm on change sets isolates the failure-inducing change between a working and a broken version, which git bisect implements as binary search over commits assuming a monotone history, and hierarchical/syntactic variants (HDD, creduce, reducing syntax trees) reduce structured inputs and programs to minimal compiler-bug reproducers; around reduction sit the scientific method of debugging (observe, hypothesize, predict, experiment, refine — with a log), tracing and dynamic slicing that follow data and control dependencies backward from the failing statement to its origins, spectrum-based fault localization that ranks statements by suspiciousness from coverage of passing and failing runs (Tarantula = (failed/totalfailed)/((passed/totalpassed)+(failed/totalfailed)), Ochiai = failed/√(totalfailed·(failed+passed))), whose usefulness is bounded by how far down the ranking a developer will actually look, statistical debugging of deployed software from sampled predicates (Liblit's CBI), and automatic program repair that searches patch space (GenProg's genetic programming over statements, semantic repair via symbolic constraints, and now LLM-generated patches) validated against tests — with the standing problem that a patch passing the tests may still be wrong (overfitting).
---
# Delta debugging and fault localization

**In one sentence.** Turn "it fails on this huge input / after these 500 commits / somewhere
in these 50 000 lines" into "it fails on `3/0` / because of commit 4f2a / most likely at
line 212" by algorithms that run the test repeatedly and shrink the search space — then
apply the scientific method to the small thing that remains.

## Why reduce? The scientific method of debugging (Debugging Book — read; Zeller *Why Programs Fail*)
"Only a small part of the input may be responsible for the failure"; a minimal
reproducer eases debugging, states *when* the program fails (the essence of the
condition), makes a regression test, and is what bug trackers should require (the MRE).
Debugging as science: **observe** the failure; form a **hypothesis** about the defect;
**predict** an observable consequence; **experiment** (add a probe, change an input, run
the debugger); accept/refine/reject; keep a log — because the alternative is random
edits. Vocabulary (Zeller): **defect** (the wrong code) → **infection** (a wrong program
state) → **failure** (an observable wrong behaviour); debugging traces the infection chain
backward from failure to defect. Tools in the book: tracing executions (`sys.settrace`,
function-call and variable-change loggers), how debuggers work (breakpoints, stepping,
watchpoints; `pdb`/`gdb`/`lldb`), **assertions** to catch infections early
([[design-by-contract]]), and the practical craft in [[debugging]] (read the error, reproduce,
bisect, rubber-duck, sleep on it).

## ddmin: reducing failure-inducing inputs (Zeller & Hildebrandt 2002; "Reducing Failure-Inducing Inputs" — read)
Given a failing input c✗ and a test `test(c) ∈ {✗ (fails), ✓ (passes), ? (unresolved)}`:
```
ddmin(c, n=2):
  split c into n chunks Δ1..Δn
  if some chunk Δi fails:            return ddmin(Δi, 2)          # reduce to subset
  if some complement c∖Δi fails:     return ddmin(c∖Δi, max(n−1,2)) # reduce to complement
  if n < |c|:                        return ddmin(c, min(2n,|c|))  # increase granularity
  return c                                                         # 1-minimal
```
Result is **1-minimal**: removing any single chunk (at final granularity, any single
element) makes the failure go away — not globally minimal (that's exponential). Cost:
O(|c|²) tests worst case, O(log |c|) when failure is caused by a contiguous piece;
each test must be **deterministic** and the failure must be **identified precisely** (same
exception/message — otherwise you reduce to a *different* bug; the book's
`check_reproducibility`). The `DeltaDebugger` context manager wraps a failing call
(`with DeltaDebugger() as dd: myeval('1 + 2 * 3 / 0')` → `myeval(inp='3/0')`), reduces
every `len()`-able argument (strings, lists), and offers `min_args()`, `max_args()` (the
largest still-passing input — the boundary from the other side) and `min_arg_diff()`
(passing, failing, and their minimal difference — `(' 3 ', ' 3 /0', '/0')`). Variants:
**hierarchical delta debugging** (HDD — reduce a tree level by level, keeping inputs
syntactically valid); **grammar-based reduction** (reduce syntax trees; replace subtrees
by minimal derivations — the book's "Reducing Syntax Trees"; [[context-free-grammars]]);
**creduce**/**cvise** for C/C++ compiler bugs (transformation passes + ddmin, produces the
10-line reproducers on LLVM/GCC bug trackers); `afl-tmin`, `halfempty`, Hypothesis's
shrinker ([[property-based-testing]], [[fuzzing]]). Reduction applies to *any* set-like
thing the test can evaluate: inputs, configurations, thread schedules, test-suite
subsets, environment variables.

## Isolating failure-inducing changes: "Yesterday my program worked. Today it does not. Why?" (Zeller 1999)
Apply dd to the **set of changes** between a passing and a failing version: find a minimal
change set that flips pass → fail (the dd algorithm keeps both a passing and a failing
configuration and narrows the difference). **`git bisect`** is the special case where
changes are totally ordered commits and the failure is monotone: binary search over
log₂(n) builds (`git bisect start; git bisect bad; git bisect good v1.2; git bisect run
./test.sh` — [[git-data-model]]); pitfalls: non-monotone failures (flaky tests —
[[software-testing-fundamentals]]), unbuildable commits (`skip`), merges, and a "cause" that
is merely the *exposing* change, not the *defect* (the fix may belong elsewhere).
Chrome/Mozilla run automated bisection on every regression (mozregression).

## Tracking failure origins: tracing and slicing ("Tracking Failure Origins")
Follow **dependencies** backward from the failing statement: a **dynamic slice** is the set
of statements that actually influenced the value at the failure (data dependencies via
definitions/uses, control dependencies via the branches that governed execution) —
computed by instrumenting the run (the book's `DependencyTracker` rewrites the AST to
record every read/write) and giving a backward slice; **static slicing** (Weiser 1981)
over-approximates on the program dependence graph ([[dataflow-analysis]]). Slices turn
"somewhere in 10 000 lines" into "these 40 statements"; omniscient/time-travel debuggers
(`rr`, Undo) let you step *backward* along the same dependencies. Related: **assertion
mining** — infer likely invariants from passing runs (Daikon; the book's "Mining Function
Specifications") and flag the run that violates them.

## Spectrum-based fault localization: Tarantula and Ochiai ("Statistical Debugging" — read; Jones & Harrold 2005)
Collect **coverage spectra** per test (which lines executed) and outcomes (pass/fail);
compute for each line the counts failed(ℓ), passed(ℓ), totalfailed, totalpassed; rank
by **suspiciousness**:
- **Tarantula**: `(failed/totalfailed) / (passed/totalpassed + failed/totalfailed)` —
  colour lines red→green (the book's discrete and continuous spectra visualizations);
- **Ochiai**: `failed / sqrt(totalfailed · (failed + passed))` — consistently better in
  studies; also Jaccard, DStar, and learned combinations.
The `TarantulaDebugger`/`OchiaiDebugger` collect events (`with debugger.collect_pass():`
… `collect_fail()`, or `with debugger:` classifying by exception) and print a ranked
table. **How useful is ranking?** (Parnin & Orso 2011): developers don't inspect linearly;
value drops sharply beyond the top ~5–10; ranking helps most with many failing tests
that share a cause and with large suites (the book's "Using Large Test Suites"); it
localizes *suspicious lines*, not *why*. Other events beyond coverage: branch outcomes,
variable-value predicates, **CBI** (Liblit 2003–05: sample predicates cheaply in deployed
software, aggregate across thousands of runs, find predicates that predict failure —
statistical debugging at scale); training classifiers on events (decision trees over
features → the failure condition — the book's "Generalizing Failure Circumstances").

## Automatic program repair (Debugging Book "Repairing Code Automatically"; Le Goues et al.)
Given failing and passing tests: **localize** (SBFL ranking) → **generate** candidate
patches → **validate** against the suite. **GenProg** (2009–12): genetic programming over
statement-level mutations (delete, insert/replace with code from elsewhere in the
program — the "plastic surgery"/redundancy assumption), fitness = tests passed; repaired
55/105 bugs at $8 each in the 2012 study. **Semantics-based** (SemFix, Angelix, Nopol): use
[[symbolic-execution-and-concolic-testing]] to derive the constraint a fixed expression
must satisfy, then synthesize it. **Template/pattern-based** (PAR, Prophet — learned from
human patches; TBar). **LLM-based** (2022–): prompt with buggy function + failing test,
sample patches, validate; SWE-bench measures end-to-end issue fixing. The central
problem: **plausible ≠ correct** — a patch passing the tests may overfit (delete the
functionality, special-case the test); the book demonstrates a repair that "fixes" a
failing test by removing the code; mitigations: held-out tests, generated tests, patch
ranking by naturalness, human review ([[code-review]]). Repair is search over a space
where the oracle is the test suite — exactly as weak as the suite.

## Pitfalls
- Reducing with a sloppy test (any exception = fail) → reduces to a different bug.
- Non-deterministic failures under ddmin/bisect → wrong answers; fix determinism first.
- Treating the exposing commit as the defect; treating a top-ranked line as the cause.
- Automatic repairs that pass tests by deleting behaviour.
- Debugging by random edits instead of hypotheses and a log.

## Related
- [[debugging]], [[software-testing-fundamentals]], [[fuzzing]],
  [[property-based-testing]], [[symbolic-execution-and-concolic-testing]],
  [[design-by-contract]], [[dataflow-analysis]] (slicing), [[git-data-model]] (bisect),
  [[context-free-grammars]], [[static-and-dynamic-analysis-tools]], [[code-review]],
  [[binary-search-trees]] (bisect is binary search over history).

## Sources
Zeller, Debugging Book: "Reducing Failure-Inducing Inputs" (read), "Statistical Debugging" (read), ToC (read), "Isolating Failure-Inducing Changes", "Tracking Failure Origins", "Repairing Code Automatically"; Zeller & Hildebrandt 2002; Zeller 1999; Misherghi & Su 2006 (HDD); Regehr et al. 2012 (creduce); Jones & Harrold 2005; Abreu et al. 2006 (Ochiai); Parnin & Orso 2011; Liblit et al. 2005; Le Goues et al. 2012 (GenProg); Zeller 2009 (*Why Programs Fail*).

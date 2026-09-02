---
title: Fuzzing — random, mutation-based, generation-based (grammar) and coverage-guided greybox fuzzing (AFL: instrumentation trampolines, edge-coverage bitmap, seed corpus, mutators, splicing, power schedules; AFLFast, AFLGo directed fuzzing), sanitizers as oracles, the bugs fuzzers find (memory safety, missing error checks, integer overflows, hangs), crash triage and input reduction, structure-aware and protocol fuzzing, fuzzing in the large (OSS-Fuzz, libFuzzer, continuous fuzzing), when to stop (species discovery, residual risk), and how fuzzing relates to symbolic execution and property-based testing
type: concept
section: "7.2"
level: 400
tags: [fuzzing, fuzz-testing, random-testing, miller-1990, mutation-based-fuzzing, generation-based, grammar-fuzzing, grammar-coverage, probabilistic-grammar, coverage-guided, greybox, blackbox, whitebox, afl, afl-plus-plus, libfuzzer, honggfuzz, oss-fuzz, instrumentation, trampoline, edge-coverage, bitmap, seed-corpus, mutators, bit-flips, havoc, splicing, power-schedule, energy, aflfast, aflgo, directed-fuzzing, sanitizers, asan, ubsan, msan, tsan, memory-safety, buffer-overflow, integer-overflow, missing-error-checks, rogue-numbers, hangs, crash-triage, deduplication, input-reduction, structure-aware, protocol-fuzzing, stateful-fuzzing, harness, fuzz-target, corpus-minimization, when-to-stop, species-discovery, residual-risk, fuzzing-book, bohme, zalewski, zeller]
sources: [testing-and-program-analysis-texts-courses-and-seminal-papers]
summary: Fuzzing feeds a program huge numbers of automatically generated inputs and watches for crashes, hangs, or sanitizer-detected violations — Miller's 1990 experiment crashed a quarter to a third of Unix utilities with random bytes, and the Fuzzing Book's RandomFuzzer/Runner architecture, its catalogue of bugs fuzzers find (buffer overflows, missing error checks, rogue numbers/integer overflows) and its generic checkers (sanitizers, assertions) are the modern restatement; three generations sharpen the input generation: mutation-based fuzzing perturbs valid seed inputs (bit flips, byte insertions/deletions, interesting-value substitution, splicing two inputs), generation-based fuzzing derives syntactically valid inputs from a grammar or generator (with grammar coverage and probabilistic grammars to steer toward rare productions — essential for parsers and compilers where random bytes die at the lexer), and coverage-guided greybox fuzzing (AFL, libFuzzer, honggfuzz) instruments every conditional jump with a trampoline that increments an edge counter in a shared 64 KB bitmap so any input that reaches new edges is kept as a seed — turning fuzzing into an evolutionary search whose power schedule (AFLFast: more energy for inputs on rarely exercised paths; AFLGo: energy by distance to a target location for directed fuzzing) decides how many mutants each seed gets; oracles are mostly implicit (ASan/UBSan/MSan/TSan, assertions, timeouts), findings are triaged by stack-hash deduplication and reduced by delta debugging, structure-aware and stateful fuzzing handle checksums, protocols and APIs, and fuzzing in the large (OSS-Fuzz's thousands of bugs, continuous fuzzing in CI, corpus minimization) treats it as infrastructure; when to stop is a species-discovery problem (Böhme's STADS: the probability of discovering a new path after n runs estimated by Good–Turing from singletons); fuzzing complements symbolic execution (which solves the branches fuzzing can't guess, e.g. magic numbers, at far higher cost per input) and property-based testing (fuzzing with a specification as oracle).
---
# Fuzzing

**In one sentence.** Generate inputs faster than a human could think of them, let the
program's own checks (crashes, sanitizers, assertions) be the oracle, and — since AFL —
keep whatever input reaches new code, so that random search becomes an evolutionary
search over coverage.

## Random inputs and what they find (Miller 1990; Fuzzing Book "Fuzzing: Breaking Things with Random Inputs" — read)
Miller et al. piped random characters into ~90 Unix utilities during a thunderstorm-
corrupted modem session and crashed 25–33 % of them; repeated in 1995 (still ~25 %),
2000 (Windows), 2006 (macOS), 2020 (still crashes). The book's architecture: a `Fuzzer`
with `fuzz()` producing a string (`RandomFuzzer(min_length, max_length, char_start,
char_range)`), a `Runner` with `run(input) → (result, outcome ∈ {PASS, FAIL, UNRESOLVED})`,
`ProgramRunner` for external programs via files/stdin, and `runs(runner, trials)`. **Bugs
fuzzers find**: **buffer overflows** (C `gets()`, the classic — the book's `crash_if_too_long`),
**missing error checks** (an input the developer never imagined → unhandled exception,
NULL deref), **rogue numbers** (integer overflow/underflow, huge allocation sizes, negative
lengths — the book's `collapse_if_too_large`), hangs and resource exhaustion. **Catching
errors**: generic checkers — memory checkers (Valgrind, **AddressSanitizer**: shadow memory
detecting out-of-bounds and use-after-free at ~2× slowdown; MSan uninitialized reads;
**UBSan** signed overflow, misaligned access, null; **TSan** data races), the language
runtime (Python's exceptions, Rust's panics/overflow checks); program-specific checkers
— assertions and invariants ([[design-by-contract]]), e.g. a heap's `assert_is_sane()`; static
checkers as complements ([[static-and-dynamic-analysis-tools]]). Fuzz targets
must be written so failures are *detectable*: turn on sanitizers, assert invariants, fail
loudly, avoid swallowing exceptions.

## Mutation-based fuzzing ("Mutation-Based Fuzzing")
Random bytes rarely pass a parser; instead start from valid **seeds** (a URL, a PNG, a
protocol message) and apply small **mutations**: delete/insert/flip a random character or
bit, arithmetic on bytes, replace with "interesting" values (0, −1, MAX_INT, 2ⁿ ± 1),
insert dictionary tokens (keywords, magic bytes), **splice** two inputs (first half of one,
second half of another). Mutants stay mostly valid, so they reach deep code; the
`MutationFuzzer` picks a seed, applies `min_mutations..max_mutations`, and the
`MutationCoverageFuzzer` keeps mutants that increase coverage — the bridge to greybox.

## Coverage-guided greybox fuzzing: how does AFL work? ("Greybox Fuzzing" — read; Zalewski)
**Blackbox** = no program knowledge; **whitebox** = heavy analysis/solving
([[symbolic-execution-and-concolic-testing]]); **greybox** = lightweight instrumentation.
AFL compiles the target with a **trampoline** after every conditional jump: `cur_location
= random_id; shared_mem[cur_location ^ prev_location]++; prev_location = cur_location >> 1`
— i.e. it counts **edges** (branch transitions, the shift breaks symmetry of A→B vs B→A)
in a 64 KB **bitmap**, with hit counts bucketed (1, 2, 3, 4–7, 8–15, …). An input whose
bitmap has a new edge or a new bucket is **interesting** → added to the seed **corpus**.
Loop: pick a seed (by a **power schedule** assigning **energy** = number of mutants to
generate; favouring small, fast, recently found seeds), mutate (**deterministic** stage:
walking bit/byte flips, arithmetic, interesting values, dictionary; then **havoc**: random
stacked mutations; then **splicing**), run via a **fork server** (fork after initialization
to avoid exec cost; persistent mode runs the target function in-process, ~10⁴–10⁵
execs/s), record coverage, keep interesting mutants; **corpus culling/minimization** keeps
the smallest set covering all seen edges. The book's `GreyboxFuzzer(seeds, mutator,
schedule)` + `FunctionCoverageRunner` demonstrates a URL parser's corpus degrading into
`http2Ot/*gv-VRgogec:om/rearc h=fu~i g` while coverage climbs. **AFLFast** (Böhme et al.
2016): view fuzzing as a Markov chain over paths; most energy is wasted on high-frequency
paths; assign energy ∝ 1/(frequency of the seed's path) (with an exponential schedule) —
found bugs ~7× faster. **AFLGo** (directed greybox fuzzing, Böhme et al. 2017): compute
each basic block's distance to target locations (e.g. a patched line, a suspicious
function) via call graph + CFG; schedule energy by (annealed) distance so the population
converges on the target — the book's maze example. Successors: AFL++, libFuzzer
(in-process, LLVM, `LLVMFuzzerTestOneInput`), honggfuzz; comparative-evaluation
methodology is its own paper (Klees et al. 2018: use many seeds, ≥24 h, ≥30 trials,
measure bugs not crashes).

## Generation-based / grammar fuzzing ("Fuzzing with Grammars", "Grammar Coverage")
When inputs have structure (JSON, C, SQL, network packets), define a **grammar** (or a
**generator** — [[property-based-testing]]) and expand nonterminals randomly to produce
valid inputs; control length via cost-based expansion (choose min-cost expansions once a
depth limit is hit); **grammar coverage** (each production at least once, then pairs);
**probabilistic grammars** (weights learned from samples or set to reach rare
productions); **greybox + grammars** (mutate derivation trees, not bytes — structure-aware
mutation, as in Nautilus/Superion); **mining input grammars** from parsers dynamically.
Compiler fuzzing (Csmith generates C programs avoiding UB and differential-tests GCC vs
Clang — 300+ bugs; YARPGen; EMI); protocol/stateful fuzzing (AFLNet, state machines
inferred from responses); API fuzzing (sequences of calls with generated arguments —
Randoop/EvoSuite; carving unit tests from system tests); checksums/magic numbers handled
by patching the check, using dictionaries, or by concolic help.

## Triage, reduction, and fuzzing in the large ("Fuzzing in the Large", "When to Stop")
Thousands of crashes → **deduplicate** by stack-trace hash (top N frames) or by coverage
signature; **reduce** each input with delta debugging (`afl-tmin`, `creduce`, the book's
`DeltaDebugger` — [[delta-debugging-and-fault-localization]]); classify severity
(exploitability: write vs read, controlled address); file with reproducer, sanitizer
report, and regression test. **OSS-Fuzz** (2016–): continuous fuzzing of ~1000 open-source
projects on Google infrastructure, >10 000 vulnerabilities and >36 000 bugs by 2023;
ClusterFuzz orchestration, fuzz targets checked into repos, crash bisection, auto-filed
issues with 90-day disclosure; **continuous fuzzing in CI** (CIFuzz: short fuzz on each
PR against the accumulated corpus); corpus sharing. **When to stop** (Böhme's STADS,
2018): treat each distinct path/edge as a species; the number of undiscovered species
and the probability that the next input finds one are estimated à la Good–Turing from
the count of singletons (species seen exactly once) — **residual risk** ≈ f₁/n; stop when
the discovery curve has flattened *and* residual risk is below tolerance; note that
absence of new coverage ≠ absence of bugs.

## How fuzzing relates to the other techniques
Fuzzing is cheap per input and blind to conditions like `if (x == 0xDEADBEEF)`;
**symbolic/concolic execution** solves such conditions but explores paths slowly —
hybrid fuzzers (Driller, QSYM) hand stuck seeds to a solver
([[symbolic-execution-and-concolic-testing]]). **Property-based testing** = fuzzing with a
specification as the oracle and typed generators ([[property-based-testing]]).
**Mutation analysis** mutates the *program* to evaluate the *tests*; fuzzing mutates the
*input* to find bugs ([[software-testing-fundamentals]]). Static analysis finds bug
*patterns* without inputs ([[static-and-dynamic-analysis-tools]]).
Memory-safe languages ([[type-systems]], Rust) remove the bug class ASan finds; fuzzing
still finds logic bugs, panics, and DoS. Fuzzing belongs in the security toolkit:
[[web-security]] and [[security-principles]] (§8) — most CVEs in parsers were found this way.

## Pitfalls
- Fuzzing without sanitizers or assertions (silent memory corruption passes).
- Bad or single seeds; no dictionary; ignoring the parser's structure (all inputs die
  at the lexer).
- Non-deterministic targets (coverage feedback becomes noise); global state in
  persistent mode.
- Counting crashes instead of unique bugs; comparing fuzzers on one short run.
- Stopping at "no new coverage for an hour" without reasoning about residual risk.

## Related
- [[software-testing-fundamentals]], [[property-based-testing]],
  [[symbolic-execution-and-concolic-testing]], [[delta-debugging-and-fault-localization]],
  [[static-and-dynamic-analysis-tools]], [[design-by-contract]], [[debugging]],
  [[type-systems]] (memory safety), [[randomized-algorithms]], [[web-security]],
  [[security-principles]], [[continuous-integration-and-delivery]].

## Sources
Zeller et al., Fuzzing Book: "Fuzzing: Breaking Things with Random Inputs" (read), "Greybox Fuzzing" (read), ToC (read), "Mutation-Based Fuzzing", "Fuzzing with Grammars", "Fuzzing in the Large", "When To Stop Fuzzing"; Miller, Fredriksen & So 1990; Zalewski, AFL technical whitepaper 2013; Böhme, Pham & Roychoudhury 2016 (AFLFast); Böhme et al. 2017 (AFLGo); Böhme 2018 (STADS); Serebryany et al. 2012 (ASan); Yang et al. 2011 (Csmith); Klees et al. 2018; Serebryany 2017 (OSS-Fuzz).

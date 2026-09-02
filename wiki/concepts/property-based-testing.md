---
title: Property-based testing — QuickCheck's idea (properties as executable specifications, random generation with tester-controlled distributions, Arbitrary instances, conditional properties, observing test-case distribution), shrinking to minimal counterexamples, Hypothesis and modern PBT (integrated shrinking, example database, stateful/model-based testing), finding good properties (round-trip, invariants, idempotence, commutativity, oracle/model comparison, metamorphic relations), generator design and the vacuous-property trap, and PBT vs fuzzing vs example tests
type: concept
section: "7.2"
level: 300
tags: [property-based-testing, pbt, quickcheck, claessen, hughes, properties, executable-specification, random-testing, generators, arbitrary, distribution, classify, collect, conditional-properties, vacuous, shrinking, minimal-counterexample, integrated-shrinking, hypothesis, maciver, example-database, stateful-testing, model-based-testing, state-machine-testing, round-trip, inverse, invariants, idempotence, commutativity, oracle, model, metamorphic, generator-design, hedgehog, proptest, fast-check, jqwik, fscheck, scalacheck, erlang-quickcheck, quviq, haskell]
sources: [testing-and-program-analysis-texts-courses-and-seminal-papers]
summary: Property-based testing, introduced by QuickCheck (Claessen & Hughes 2000), replaces hand-written examples with properties — executable specifications like "reverse (reverse xs) == xs" or "decode (encode x) == x" written as ordinary functions — that the tool checks on hundreds of randomly generated inputs, using a generator DSL (Arbitrary instances, combinators like choose/oneof/frequency/sized) that puts the distribution under the tester's control because random testing is meaningless without a distribution, tools to observe that distribution (classify, collect) so that conditional properties (precondition ==> claim) aren't vacuously passing on trivial data, and, since QuickCheck 2 and Hypothesis, shrinking that reduces a failing input to a minimal counterexample (Hypothesis shrinks the underlying byte stream so shrinking composes automatically through any generator, remembers failures in an example database, and supports stateful model-based testing of APIs against a simplified model); the skill is finding properties — round-trip/inverse pairs, invariants preserved by operations, idempotence, commutativity/associativity, comparison against a reference oracle or model, metamorphic relations, "hard to compute, easy to verify" — and designing generators that hit edge cases (empty, huge, duplicates, unicode) with reasonable frequency; PBT sits between example tests (which document specific behaviour and are cheap to read) and fuzzing (which uses implicit crash oracles and coverage feedback on raw bytes), and it shines on pure functions, serializers, parsers, data structures, concurrency schedules and anything with an algebraic law.
---
# Property-based testing

**In one sentence.** State what should be true of *all* inputs, let the tool generate the
inputs and shrink the failures, and you get tests that find the cases you didn't think
of — provided you control the input distribution and check that your properties aren't
vacuous.

## QuickCheck (Claessen & Hughes 2000 — read)
Testing is "up to 50 % of the cost of software development"; functional programs suit
automatic testing because pure functions can be tested at fine grain. QuickCheck's three
decisions: (1) the oracle is a **formal specification** — a DSL of testable properties
embedded in Haskell via the class system, written next to the code as checkable
documentation (`prop_RevRev xs = reverse (reverse xs) == xs`); (2) test data is
**random** ("competes surprisingly favourably with systematic methods in practice") but
"it is meaningless to talk about random testing without discussing the distribution of
test data" — for reusable units the real distribution is unknown and a uniform one
over infinite sets isn't even defined, so **distribution is put under the tester's
control** via a generator language (`Gen`, `Arbitrary` class, `choose`, `oneof`,
`frequency`, `sized`, `elements`, `vectorOf`) and made observable (`classify`, `collect`,
`cover` print the distribution of cases actually tested); (3) it is **lightweight** — one
~300-line Haskell 98 module. **Conditional properties** `pre ==> prop` discard cases
failing the precondition — the paper's pitfall: an insertion-into-sorted-list property
whose generated lists were almost never sorted beyond length 2, so the property was
"tested" on trivial data (**vacuous properties**); fix by a custom generator of sorted
lists. Also: properties over functions (via `CoArbitrary`), the `Testable` class making
`Bool`, `Gen`, and functions all properties, and case studies (a queue, a pretty-printer,
Edison, a formal-methods tool) where PBT found bugs in code believed correct. Later:
QuickCheck 2's **shrinking**; Quviq's commercial Erlang QuickCheck with **state-machine
models** (Hughes: bugs in Volvo's AUTOSAR, Klarna, Dropbox, LevelDB); "Testing the hard
stuff and staying sane" (2014).

## Shrinking and modern tools (Hypothesis — MacIver; Hedgehog; proptest; fast-check)
A random counterexample is large and noisy; **shrinking** searches for a smaller input
that still fails (delete elements, halve numbers, simplify structure —
[[delta-debugging-and-fault-localization]] is the same idea on arbitrary inputs).
QuickCheck's `shrink :: a → [a]` is type-directed and must be written per type;
**Hypothesis** (Python) shrinks the underlying **byte stream** that drove the generator
("internal shrinking"), so every derived generator shrinks for free and shrinks respect
invariants (`filter`/`map`/`flatmap` compose); it keeps an **example database** of past
failures to replay, targets **coverage** of branches when available, supports
`@given(strategies)`, `assume()` (with health checks that fail the test if too many
cases are filtered — the vacuity trap made visible), `note()`, `settings(max_examples,
deadline)`, and **stateful testing** (`RuleBasedStateMachine`: rules with preconditions
run in random sequences against a **model** — e.g. a dict as the model of a key-value
store — shrinking to a minimal operation sequence). Hedgehog and jqwik use integrated
shrinking too; proptest (Rust), fast-check (JS/TS), FsCheck, ScalaCheck, PropEr (Erlang),
Kotest; Rust's `cargo fuzz` and Go's native fuzzing blur into [[fuzzing]].

## What properties should I write? (Hughes; Wlaschin "Choosing properties")
- **Round-trip / inverse**: `parse(print(x)) == x`, `decode(encode(x)) == x`,
  `decompress(compress(x)) == x` — the most bug-dense category (serializers, parsers,
  codecs — [[source-coding-and-compression]]).
- **Invariants** the operation must preserve: a sorted output is sorted and a permutation
  of the input; a tree stays balanced; a set's size changes by ≤ 1
  ([[abstract-data-types-and-rep-invariants]] — the rep invariant *is* a property).
- **Idempotence** (`normalize(normalize(x)) == normalize(x)`), **commutativity /
  associativity** (merge, union, CRDT ops), distributive
  laws.
- **Oracle / model**: compare against a slow reference implementation (`fastSort == naiveSort`),
  a previous version, or a simple model (a list as the model of a queue; a dict as the
  model of a database — stateful PBT).
- **Metamorphic relations** when there's no oracle: filtering never increases count; adding
  a document never decreases a search hit's score ([[software-testing-fundamentals]]).
- **Hard to solve, easy to check**: solutions from a solver satisfy the constraints
  ([[p-vs-np]] intuition); a path returned is a valid path of the claimed
  length.
- **"No crash"** with typed generators — the weakest useful property, close to fuzzing.

## Generator design
Generators decide what gets tested: bias toward **edge cases** (empty, singleton, max
size, duplicates, zero/negative, NaN, unicode, boundaries at 2ⁿ), use `sized` so
structures grow with the test index, build **domain generators** (valid emails, well-typed
programs, consistent transactions) rather than filtering (filters shrink the effective
sample; >90 % rejection is a broken test — Hypothesis fails it); recursive generators need
size limits; **check the distribution** with `classify`/`collect`/`statistics` before
trusting a green run; seed for reproducibility and replay failures from the database.
Trade-off: a generator that only produces valid inputs never tests the error path — keep
a separate property for invalid inputs.

## PBT vs example tests vs fuzzing
Example tests ([[unit-testing]]) document specific behaviour, are readable, and pin
regressions; PBT states the *law* and explores; fuzzing ([[fuzzing]]) uses raw bytes,
implicit oracles and coverage feedback for security bugs at scale. Use all three:
examples for the spec you can name, properties for the algebra, fuzzing for the parser
boundary. PBT's cost: harder to write (finding properties is design work — it often
reveals that the spec was never stated), slower runs, flaky if generators are
unbounded, and shrunk counterexamples that still need [[debugging]].

## Pitfalls
- Vacuous properties (filters/preconditions discarding almost everything) — always
  inspect the distribution.
- Properties that restate the implementation (`f(x) == f(x)`); tautologies.
- Unbounded generators (huge inputs, deep recursion) → timeouts mistaken for bugs.
- Not seeding/recording failures; no shrinking (drowning in a 10 000-element list).
- Treating "100 cases passed" as proof — it's a sample; raise `max_examples` for
  critical code and combine with [[program-verification]] where it matters.

## Related
- [[software-testing-fundamentals]], [[unit-testing]], [[fuzzing]],
  [[delta-debugging-and-fault-localization]], [[design-by-contract]],
  [[abstract-data-types-and-rep-invariants]], [[program-verification]],
  [[randomized-algorithms]], [[higher-order-functions]] (properties over functions),
  [[source-coding-and-compression]].

## Sources
Claessen & Hughes 2000 (read: abstract, §1–2); Hughes 2007 ("QuickCheck testing for fun and profit"), 2016 ("Experiences with QuickCheck"); Arts, Hughes et al. 2006 (Erlang QuickCheck); MacIver & Hatfield-Dodds 2019/2020 (Hypothesis); Wlaschin 2014; Zeller et al., Fuzzing Book "Fuzzing with Generators".

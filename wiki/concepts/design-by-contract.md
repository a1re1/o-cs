---
title: Design by contract — preconditions, postconditions and class/loop invariants as executable specifications (Meyer, Eiffel), assertions as the cheapest debugging and testing tool (fail fast, detect infections near the defect), the Liskov substitution rule for contracts under inheritance (weaker pre, stronger post), defensive programming vs contracts (who is responsible for checking), old-value and frame conditions, assertion policy in production, contracts as oracles for fuzzing and property-based testing, and the road from runtime contracts to static verification (JML, Dafny, SPARK, Hoare logic)
type: concept
section: "7.2"
level: 300
tags: [design-by-contract, dbc, contracts, preconditions, postconditions, invariants, class-invariant, loop-invariant, meyer, eiffel, assertions, assert, fail-fast, infections, defects, hoare-triples, liskov, behavioral-subtyping, weaken-precondition, strengthen-postcondition, defensive-programming, responsibility, blame, old-values, frame-conditions, side-effects, assertion-policy, production-assertions, ndebug, oracles, fuzzing-oracles, property-based, jml, dafny, spark, ada, code-contracts, icontract, deal, rust-debug-assert, python-assert, runtime-verification, specification, executable-specification, asserting-expectations, debugging-book]
sources: [testing-and-program-analysis-texts-courses-and-seminal-papers]
summary: Design by contract (Meyer, Eiffel, 1986) treats every routine as a contract between caller and callee — the precondition is what the caller must guarantee, the postcondition what the callee then promises (often relative to old values), and the class invariant what holds of every object between calls — written as executable assertions so that a violated precondition blames the caller and a violated postcondition blames the callee, which converts a silent wrong state into a failure at the earliest possible moment near the defect (the Debugging Book's "Asserting Expectations": assertions catch infections before they spread; a heap's assert_is_sane, a memory allocator's redzone checks, are contracts for data structures); under inheritance a subclass may weaken preconditions and strengthen postconditions but never the reverse (Liskov's behavioural subtyping, the rule SOLID's L abbreviates); contracts differ from defensive programming in assigning responsibility — check each condition once, at the boundary that owns it, rather than everywhere — and from error handling in that a contract violation is a bug, not a condition to recover from; practical policy keeps cheap assertions on in production (crash reports beat corrupted data), gates expensive ones (full invariant checks) behind debug builds, and never puts side effects in assertions; contracts are the oracle that makes fuzzing and property-based testing find logic bugs rather than only crashes; and because a contract is a Hoare triple, the same annotations feed static verifiers — JML/OpenJML, Dafny, SPARK/Ada, Frama-C ACSL, Code Contracts — that prove them for all inputs instead of checking them on some.
---
# Design by contract

**In one sentence.** Say, in code, what each routine requires and ensures and what each
object always satisfies; then every run checks the specification for you, blame is
assigned automatically, bugs surface where they happen instead of where they hurt, and
the same statements become the oracle for fuzzers and the proof obligations for
verifiers.

## Contracts (Meyer 1986/1997; Hoare 1969)
For routine `r`: **precondition** `require` — obligations on the caller (arguments, object
state), **postcondition** `ensure` — obligations on the callee, stated over the result and
the state change, using **`old` values** (`count = old count + 1`); **class invariant** —
holds after construction and before/after every public call (may be broken *during* a
call); **loop invariant** and **variant** (a decreasing natural number — termination) for
loops. Eiffel example:
```
push (x: G)
  require not_full: count < capacity
  do ... ensure pushed: item = x; one_more: count = old count + 1 end
invariant 0 <= count and count <= capacity
```
A contract is a **Hoare triple** {P} r {Q} ([[program-verification]] (Hoare logic)); runtime checking evaluates P
on entry (failure ⇒ **the caller is wrong**) and Q + invariant on exit (failure ⇒ **the
callee is wrong**). This **assignment of blame** is the point — a stack trace at a
precondition failure names the culprit; without contracts a bad argument becomes a
corrupted structure discovered three modules later. Contracts also *are* the
documentation: what a client may assume is exactly what is ensured — the interface of
[[modularity-and-information-hiding]] made checkable, and the **rep invariant** /
**abstraction function** discipline of [[abstract-data-types-and-rep-invariants]] is the
class-invariant idea for implementers.

## Assertions catch infections early (Debugging Book "Asserting Expectations"; Zeller)
Defect → infection (wrong state) → failure: the further the infection travels, the harder
the debugging ([[delta-debugging-and-fault-localization]]). An **assertion** turns an
infection into a failure at the point of the assertion; the book's examples: a **heap
memory checker** (redzones + `assert_is_sane`, the idea behind AddressSanitizer —
[[static-and-dynamic-analysis-tools]]), a **red-black tree's** `assert invariant` after every
operation, `assert` on function entry/exit via decorators (`@precondition`,
`@postcondition`), and **system invariants** (checksums, referential integrity — assert in
the DB layer). Assertions are the **cheapest testing tool**: one `assert` runs on every
test and every fuzz input ([[fuzzing]] with contracts finds *logic* bugs, not just
crashes; [[property-based-testing]] properties are contracts stated over generated
inputs); KLEE turns each assertion into a reachability query
([[symbolic-execution-and-concolic-testing]]). Rules: an assertion must have **no side
effects** (it may be compiled out — C's `NDEBUG`, Python's `-O`, Rust's `debug_assert!`),
must check *the program's* assumptions not *the user's* input (invalid input is an
expected condition handled by validation and errors),
and should be as strong as you can make cheaply.

## Inheritance: behavioural subtyping (Liskov & Wing 1994; Meyer)
A subclass routine that redefines `r` may **weaken the precondition** (accept more) and
**strengthen the postcondition** (promise more) — never the reverse — and must preserve the
parent's invariant; then any client written against the parent contract works with the
child ([[liskov-substitution]], [[solid-principles]]). Eiffel enforces it by `require else` /
`ensure then`. Violations are the classic square/rectangle and "read-only collection
subclass throws" bugs; contract-checking tools (and property tests over the interface)
detect them. History constraints (the state may only evolve in certain ways) extend the
idea to protocols/typestate.

## Contracts vs defensive programming vs error handling
**Defensive programming** checks everything everywhere ("just in case"), duplicating
checks and hiding who is responsible; contracts assign each check to **one** side: the
**non-redundancy principle** — a routine with a precondition does not also test for it
inside (the caller must). Trade-off at **trust boundaries**: input from users, files,
networks, and other services is *validated* (an expected condition → error return /
exception — [[security-principles]]: never trust input), while calls within a module obey
contracts (a violation → bug → assertion failure, fail fast). **Fail fast** (Shore 2004):
crashing at the violation with a clear message is better than limping on with corrupted
state; in services, pair with supervision/restart ([[site-reliability-engineering]],
Erlang's "let it crash"). **Production assertions**: keep cheap ones on (Google, Microsoft,
SQLite all ship with assertions or their equivalents; a crash report is diagnosable, a
corrupted database isn't); make expensive invariant checks (O(n) tree walks) debug-only
or sampled; log-and-continue only for non-critical, well-understood checks.

## From runtime checks to proofs
Contracts in languages/tools: Eiffel (native), **JML** (Java Modeling League annotations —
runtime checking with OpenJML, static with ESC/Java2, KeY), **.NET Code Contracts**, **D**
(`in`/`out`/`invariant`), **Kotlin** `require/check`, Python (`icontract`, `deal`,
`assert`), Rust (`assert!`, `debug_assert!`, `contracts` crate; `unsafe` preconditions as
docs — [[type-systems]]), Clojure `:pre/:post`, C++ contracts (C++26). **Static verification**
proves the triples for all inputs: **Dafny** (pre/post/invariants discharged by Z3 —
[[sat-and-smt-solvers]]), **SPARK/Ada** (industrial: proves absence of runtime errors and
functional contracts; used in avionics), **Frama-C/ACSL** (C), **Why3**, **Viper**;
[[program-verification]] covers the logic and [[program-verification]] (Hoare logic) the calculus. **Runtime
verification** monitors temporal contracts (protocols, ordering) on traces. Contracts
also feed **specification mining** — Daikon infers likely invariants from passing runs
(the Debugging Book's "Mining Function Specifications"), which you then confirm or
refute and adopt as contracts. The gradient: assertions → property tests → contracts
checked by fuzzing → static verification, each rung buying certainty with effort.

## Pitfalls
- Side effects or expensive computation inside assertions.
- Using assertions to validate external input (compiled out → security hole).
- Subclasses that strengthen preconditions (LSP violations).
- Redundant defensive checks that obscure responsibility; swallowing contract
  violations as errors.
- Disabling all assertions in production and shipping silent corruption.

## Related
- [[program-verification]] (Hoare logic), [[program-verification]], [[abstract-data-types-and-rep-invariants]],
  [[modularity-and-information-hiding]], [[liskov-substitution]], [[solid-principles]],
  [[software-testing-fundamentals]], [[property-based-testing]], [[fuzzing]],
  [[symbolic-execution-and-concolic-testing]], [[static-and-dynamic-analysis-tools]],
  [[delta-debugging-and-fault-localization]], [[debugging]],
  [[security-principles]], [[type-systems]],
  [[sat-and-smt-solvers]].

## Sources
Meyer 1992 ("Applying Design by Contract", IEEE Computer), *Object-Oriented Software Construction* 1997 ch. 11; Hoare 1969; Liskov & Wing 1994; Zeller, Debugging Book "Asserting Expectations", "Mining Function Specifications" (ToC read); Shore 2004 (fail fast); Leavens et al. 2006 (JML); Leino 2010 (Dafny); Ernst et al. 2007 (Daikon); Hunt & Thomas 1999 ch. 4.

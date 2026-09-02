---
title: Unit testing — partitions, boundaries, black-box vs glass-box, coverage, test-first
type: concept
section: "2.2"
level: 200
tags: [unit-testing, test-first, partitioning, boundary-values, black-box-testing, glass-box-testing, coverage, regression-tests, test-doubles, assertions, testing-strategy, flaky-tests]
sources: [mit-6-102-software-construction, ousterhout-philosophy-of-software-design, htdp]
summary: Exhaustive testing is impossible, so choose inputs systematically — partition the input space by the spec, include boundaries, cover each partition with a small test — write tests first against the spec (black-box), then add glass-box tests for implementation branches, measure coverage as a gap-finder not a goal, and keep tests as a regression suite; testing shows bugs, never their absence.
---
# Unit testing

**In one sentence.** A good test suite is a *designed* sample of the input space: each spec clause
and boundary gets a test, tests are written before or alongside the code, and every bug fixed becomes
a regression test.

## Choosing inputs (6.102 reading 02)
1. **Partition** the input (and output) space from the *spec*: e.g. `max(a, b)`: a < b, a = b, a > b;
   signs; magnitudes. For collections: empty, one element, many; duplicates; sorted/unsorted.
2. Add **boundary values**: 0, ±1, min/max, empty string, first/last index, `null`/`None`, off-by-one
   neighbours — bugs cluster at boundaries.
3. Cover each partition with at least one test; combine partitions of several inputs sparingly
   (full Cartesian product explodes; cover each value of each dimension).
4. **Black-box** tests come from the spec only (they survive re-implementation); **glass-box** tests add
   cases for implementation branches (each `if`, each loop 0/1/many). Neither should depend on the rep.
5. **Coverage** (statement/branch): use it to find *untested* code, not as a target; 100% coverage with
   weak assertions proves nothing.

## Discipline
- **Test-first**: spec → tests → implementation. Writing tests first clarifies the spec and stops you
  from unconsciously writing tests that match your code.
- Small, independent, fast, deterministic tests; one concept per test; descriptive names that state the
  expected behaviour.
- Assertions should check outputs *and* important side effects; testing exceptions is part of the spec.
- **Regression tests**: reproduce each bug as a failing test before fixing ([[debugging]]).
- Flaky tests (time, randomness, order, network) get fixed or quarantined; a suite people ignore is
  worse than none.
- Ousterhout's caveat: TDD taken literally produces tactical code; write tests first for the
  *interface* you designed, not one increment at a time.

## Beyond examples
Property-based testing (generate inputs, check invariants), mutation testing (does the suite catch
injected bugs?), fuzzing — §7.2 ([[property-based-testing]]). Integration/system tests, test doubles
(stubs, mocks, fakes) for dependencies — use fakes at architectural boundaries, not mocks of every class.

## Pitfalls
- Tests that restate the implementation (assert the loop runs n times) instead of the spec.
- Only "happy path" tests; no boundaries; no error paths.
- Shared mutable fixtures leaking between tests (order-dependent failures).
- Asserting on floating-point equality ([[floating-point]]) or on dict/set ordering.

## Related
- [[specifications-and-invariants]], [[design-recipe]], [[debugging]], [[code-review]],
  [[property-based-testing]], [[abstract-data-types-and-rep-invariants]].

## Sources
6.102 reading 02 (Testing); HtDP design recipe step 3/6; Ousterhout ch. 19.

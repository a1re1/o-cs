---
title: Specifications — preconditions, postconditions, and designing specs
type: concept
section: "2.2"
level: 200
tags: [specifications, preconditions, postconditions, requires-effects, contracts, behavioral-equivalence, deterministic, underdetermined, declarative, spec-strength, exceptions, fail-fast, design-by-contract]
sources: [mit-6-102-software-construction, ousterhout-philosophy-of-software-design, effective-java]
summary: A spec is a contract — requires (the client's obligation) and effects (the implementer's) — that defines when two implementations are substitutable; good specs are declarative, deterministic where it matters, and as weak in precondition / strong in postcondition as you can afford; exceptions belong in the postcondition and "fail fast" versus "define errors out of existence" is a layer decision.
---
# Specifications

**In one sentence.** Behavioural equivalence "is in the eye of the client", so write down what clients
may rely on — the spec — before anyone depends on the implementation; then any implementation
satisfying the spec is a legal replacement.

## Anatomy (6.102 reading 04)
```
find(arr: Array<number>, val: number): number
  requires: val occurs exactly once in arr
  effects:  returns index i such that arr[i] = val
```
- **requires** (precondition): obligations on the *caller*; if violated, the implementation may do
  anything ("garbage in"). Behaviour outside the precondition is not part of the contract, so the
  spec above never mentions the `return -1` both implementations contain.
- **effects** (postcondition): obligations on the *implementer* when called legally — return value,
  mutations (say explicitly which arguments are mutated; default assumption: none), exceptions thrown.
- Order of work that is safest from bugs: **spec, tests, implementation, clients, re-implementation**.
- The spec is a firewall: clients can't depend on the rep; implementers can be replaced (6.102's
  forward-search vs two-ended `find`).

## Designing specs (reading 05) — three dimensions
| Dimension | Options | Guidance |
|---|---|---|
| Deterministic vs **underdetermined** | one legal output vs a set ("returns *an* index i with arr[i] = val") | underdetermined specs leave freedom to implementers (any index, any order) — but clients then can't rely on it; not the same as *nondeterministic* code |
| **Declarative** vs operational | *what* the result is vs *how* it's computed | prefer declarative; operational details in a spec become accidental promises |
| Strength | stronger = weaker precondition and/or stronger postcondition | a stronger spec can replace a weaker one anywhere (this is [[liskov-substitution]]); pick the weakest precondition you can check cheaply, and put checks in the implementation (fail fast) rather than trusting callers when the check is cheap |

Preconditions are appropriate when checking is expensive (a sorted-array precondition for binary
search) or when the function is private/internal; otherwise convert them to a postcondition that
throws (`IllegalArgumentException`) — an exception *is* part of the contract.

## Exceptions in specs
Use exceptions for **special results** (not found, invalid input) that the caller must handle, and
checked/unchecked according to the language; avoid special return values (−1, null) that are easy to
ignore. Failure atomicity (Bloch): on exception leave the object as it was.
> **Contradiction (resolved by layer):** 6.102 says *fail fast* — detect a violated assumption as early
> as possible and throw. Ousterhout says *define errors out of existence* — design interfaces so the
> error case is a normal case (deleting a nonexistent file succeeds; substring clamps indices). Both are
> right: eliminate error cases at the *interface design* level when a sensible default exists; for the
> cases that remain, fail fast rather than limping on with corrupted state.

## Testing against a spec
Partition the input space by the spec's clauses (each requires/effects boundary), test each partition
and boundary values, and test exceptional paths — black-box testing needs no knowledge of the code
([[unit-testing]]).

## Related
- [[abstract-data-types-and-rep-invariants]], [[liskov-substitution]], [[unit-testing]], [[design-recipe]],
  [[managing-complexity-in-software-design]], [[invariant-principle]].

## Sources
6.102 readings 04 (Specifications), 05 (Designing Specifications); Ousterhout ch. 10; Effective Java items 49, 69–76.

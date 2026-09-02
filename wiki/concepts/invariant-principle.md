---
title: Invariant principle (state machines, loop invariants, termination)
type: concept
section: "1.1"
level: 200
tags: [invariants, state-machines, loop-invariant, termination, induction, program-correctness, floyd]
sources: [mcs-lehman-leighton-meyer]
summary: Floyd's Invariant Principle — a property true at the start and preserved by every transition holds in every reachable state — is the induction behind loop invariants, safety arguments, and termination proofs via a strictly decreasing derived variable.
---
# Invariant principle

**In one sentence.** If a predicate holds in the start state and every transition preserves it,
it holds in every reachable state — so to prove a program never does X, find a preserved invariant that
excludes X.

## Why it matters
This is the single most useful proof pattern for programmers: loop invariants, data-structure
representation invariants, type-soundness ("preservation + progress"), consensus safety proofs, and
security "the attacker can never reach state S" arguments all instantiate it. It converts an infinite
question (all executions) into two finite checks (start, one step).

## How it works
A **state machine** is a set of states, a start state, and a transition relation q → r. An **execution**
is a sequence of states starting at the start state where consecutive states are related by →. A state is
**reachable** if some execution ends in it. A predicate P is a **preserved invariant** if
P(q) ∧ q → r ⇒ P(r).

**Invariant Principle.** If P holds in the start state and P is a preserved invariant, then P holds in
every reachable state. *Proof:* induction on the length of the execution ([[induction]]).

Recipe:
1. Model the loop/protocol as states (the tuple of variables) and transitions (one iteration / one message).
2. Guess P: usually "the relationship between the variables that the loop is maintaining".
3. Check P at initialization; check P is preserved by one step (this is where you use the loop guard).
4. At exit, P ∧ ¬guard ⇒ the postcondition.

**Termination** is separate: exhibit a *derived variable* f(state) taking values in a well-ordered set
(usually N) that strictly decreases on every transition; then executions are finite. If f only weakly
decreases, no conclusion.

## Worked examples
- **Diagonal robot** (MCS 5.4): from (0,0), each move is (±1, ±1). Invariant: x + y is even (preserved
  since the sum changes by −2, 0, +2). Hence (1, 0) is unreachable. Note the invariant is *stronger*
  than "not at (1,0)" — you almost always need to strengthen.
- **Fast exponentiation** computing a^b: variables (x, y, z) with invariant z · x^y = a^b; each step
  either halves y (squaring x) or decrements y (multiplying z); y decreases, so it terminates; at y = 0,
  z = a^b.
- **Euclid's gcd**: invariant gcd(x, y) = gcd(a, b); derived variable x + y decreases; at y = 0, x is the gcd
  ([[number-theory-basics]]).
- **Die Hard jugs** (3 and 5 gallon): invariant "both amounts are multiples of gcd" shows why 4 gallons is
  reachable with (3,5) but not with (3,6).

## Pitfalls & gotchas
- An invariant that is true but *not preserved by every transition* proves nothing — the check is
  "P(q) and q → r ⇒ P(r)" for *all* q satisfying P, including unreachable ones. If that fails, strengthen P.
- Forgetting to prove the start state satisfies P.
- Using the invariant to conclude termination — it never does; you need the decreasing measure.
- In concurrent code, the "transition" is any single thread step; invariants must survive interleavings.

## Related
- [[induction]] — the underlying principle.
- [[dags-and-partial-orders]] — well-founded orders generalise "strictly decreasing natural number".
- [[proof-techniques]].

## Sources
MCS ch. 5.4 (State Machines, Invariant Principle, derived variables, termination), problems on Die Hard and fast exponentiation.

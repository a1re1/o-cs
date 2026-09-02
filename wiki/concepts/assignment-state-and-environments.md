---
title: Assignment, local state, identity vs equality, and the costs of mutation
type: concept
section: "2.1"
level: 100
tags: [assignment, mutable-state, side-effects, referential-transparency, identity-vs-equality, aliasing, sameness, imperative-programming, functional-programming, environment-model]
sources: [sicp, composing-programs]
summary: Introducing assignment buys objects with local state (a withdraw procedure with a balance) at the price of the substitution model — the same expression no longer has the same value, "same" splits into identity and equality, aliasing makes order of evaluation matter, and programs become harder to reason about — which is the argument for isolating mutation.
---
# Assignment and state

**In one sentence.** `set!`/`=` lets a procedure remember, which models real objects nicely but
destroys the property that an expression means the same thing every time it is evaluated.

## What you gain (SICP 3.1.1)
`make-withdraw` returns a procedure with a private `balance`; each call changes it. Local state gives
modular models of the world: bank accounts, random number generators (a hidden seed makes `rand`
usable by callers that need not manage the state), queues, tables, simulators. The environment model
explains the mechanism ([[substitution-and-environment-models]]).

## What you pay (SICP 3.1.3)
- The substitution model fails: substituting 25 for `balance` in `make-simplified-withdraw` produces
  nonsense because `balance` is now a *place*, not a value.
- **Referential transparency** is lost: `(W 20)` returns 5 then −5. Equational reasoning, memoization,
  reordering, and parallelization all rely on it.
- **Sameness**: two `make-decrementer 25` are interchangeable; two `make-simplified-withdraw 25` are
  distinct objects with separate histories. So we need both `equal?`/`==` (same value) and `eq?`/`is`
  (same object). Python: `a == b` vs `a is b`; Java `equals` vs `==`; Rust makes the distinction in the
  type system (ownership).
- **Aliasing**: two names for one mutable object; mutating through one surprises code holding the other
  (mutable default arguments in Python, shared lists, callers keeping references to internal state).
- Order of evaluation now matters (`(+ (f) (g))` with side effects); concurrency turns this into races
  ([[synchronization-primitives]]).

## Design consequences
- Keep the functional core pure and push state to the edges (SICP's stream chapter shows a bank
  account as a function of a stream of requests — state as time, not mutation —
  [[streams-and-lazy-evaluation]]).
- Prefer immutable data by default; copy-on-write and persistent data structures make this cheap
  ([[persistent-data-structures]]).
- Make identity explicit when it matters (entities with IDs) and value semantics otherwise.
- Document which operations mutate; return new values rather than mutating arguments (6.102's "safe
  from bugs, easy to understand, ready for change" — [[specifications-and-invariants]]).

## Pitfalls
- Python default arguments evaluated once: `def f(x, acc=[])` shares one list across calls.
- Mutating a collection while iterating over it.
- Caching a value that later changes (stale state), or memoizing an impure function.

## Related
- [[substitution-and-environment-models]], [[data-abstraction]], [[streams-and-lazy-evaluation]],
  [[functional-programming-principles]], [[objects-and-classes]].

## Sources
SICP 3.1 (assignment and local state, benefits, costs), 3.3 (mutable data); Composing Programs 2.4.

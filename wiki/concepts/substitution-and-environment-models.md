---
title: Substitution model and environment model of evaluation
type: concept
section: "2.1"
level: 100
tags: [substitution-model, environment-model, evaluation, scoping, lexical-scope, closures, frames, environment-diagrams, applicative-order, normal-order]
sources: [sicp, composing-programs]
summary: Two mental models for "what does this expression do" — substitute arguments into the body (valid without assignment) and the environment model (frames of bindings with parent pointers, needed once state exists) — plus the parent-pointer rule that explains closures, lexical scope, and most scoping bugs.
---
# Substitution model and environment model

**In one sentence.** Without assignment, a call is just "replace parameters with arguments and
evaluate the body"; with assignment you must track *where* names live, which is the environment model
of frames and parent pointers.

## Substitution model (SICP 1.1.5)
To evaluate a combination: evaluate the operator and operands, then apply. Applying a compound
procedure = evaluate its body with each formal parameter replaced by the corresponding argument.
**Applicative order** (evaluate arguments first — Scheme, Python, most languages) vs **normal order**
(substitute unevaluated expressions and evaluate only when needed — lazy languages, `if`, short-circuit
`and`/`or`, macros). They agree on values for pure terminating programs; normal order can terminate
where applicative order loops (arguments that are never used) and can duplicate work
([[streams-and-lazy-evaluation]]).

## Environment model (SICP 3.2, Composing Programs environment diagrams)
- An **environment** is a sequence of **frames**; each frame maps names to values and has a parent
  (except the global frame).
- A user-defined function value is a pair: (code, defining environment). **Parent-pointer rule**: a
  function's parent is the frame in which the function was *defined* (lexical scoping), not where it is
  called (dynamic scoping).
- Calling a function creates a new frame whose parent is the function's defining environment, binds
  parameters, evaluates the body there. Name lookup walks parent pointers; assignment updates the
  nearest binding found (Python: assignment creates a *local* binding unless `nonlocal`/`global`).
- **Closures** fall out: a returned function keeps its defining frame alive (`make_adder(3)`,
  counters, memoized functions). Loops that create closures over a loop variable capture the *variable*,
  not its value — the classic JavaScript/Python late-binding surprise.

## Why the models matter
- They are exactly what an interpreter implements ([[interpreters-eval-apply]]): substitution ↔ term
  rewriting, environments ↔ frames on a stack or heap.
- Understanding "parent = defining frame" resolves 90% of scope questions: shadowing, `nonlocal`,
  closures in loops, decorators, callbacks holding stale state.
- The substitution model is what makes equational reasoning and refactoring safe; assignment breaks
  it ([[assignment-state-and-environments]]).

## Worked example
```python
def make_counter():
    n = 0
    def inc():
        nonlocal n        # without this, n = n + 1 creates a new local n -> UnboundLocalError
        n += 1
        return n
    return inc
c = make_counter(); c(); c()   # 2 — frame of make_counter survives because inc points to it
```

## Related
- [[recursion-and-iteration]], [[higher-order-functions]], [[assignment-state-and-environments]],
  [[interpreters-eval-apply]].

## Sources
SICP 1.1.5, 3.2; Composing Programs 1.3–1.6 (environment diagrams), 2.4.

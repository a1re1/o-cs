---
title: Higher-order functions, closures, map/filter/reduce, and sequences as conventional interfaces
type: concept
section: "2.1"
level: 100
tags: [higher-order-functions, first-class-functions, closures, lambda, map, filter, reduce, fold, currying, decorators, function-composition, pipelines, fixed-points]
sources: [sicp, composing-programs, htdp]
summary: Treating functions as values lets you name patterns of computation instead of instances — sum-over-a-range, fixed-point iteration, map/filter/accumulate pipelines — so structurally different programs (sum odd squares of a tree, list even Fibonaccis) become one enumerate→map→filter→accumulate plan; closures, currying, and decorators are the everyday forms.
---
# Higher-order functions

**In one sentence.** When functions are first-class, common *patterns* (loop over a range, apply to
each, keep those that…, combine with…) become library functions, and programs become compositions of
them.

## The moves (SICP 1.3)
- **Functions as arguments**: `sum(term, a, next, b)` abstracts Σ; `fixed_point(f, guess)` iterates
  f until |f(x) − x| < tol — √x is the fixed point of y ↦ x/y with average damping; Newton's method is
  the fixed point of x − g(x)/g′(x). One general method, many instances.
- **Functions as return values**: `make_adder(n)`, `compose(f, g)`, `derivative(g)` — closures capture
  their defining environment ([[substitution-and-environment-models]]).
- **lambda** for anonymous functions; `let` as sugar for lambda application.
- **Currying / partial application**: turn f(a, b) into f(a)(b) (`functools.partial`).
- **Decorators** (Python): `@memo`, `@trace` — a function that takes a function and returns a wrapped one.
- **Rights and privileges of first-class elements** (SICP): named, passed, returned, stored in data structures.

## Sequences as conventional interfaces (SICP 2.2.3)
Two programs — "sum the squares of odd leaves of a tree" and "list the even Fibonacci numbers ≤ n" —
are the *same* signal-flow plan: **enumerate** (leaves / integers) → **map** (square / fib) →
**filter** (odd? / even?) → **accumulate** (+ from 0 / cons from nil). Writing programs against this
interface (lists as the signal) lets stages be mixed and matched: nested mappings (`flatmap`) express
searches like "pairs (i, j) with i + j prime" and the eight-queens problem. Modern forms: Python
comprehensions/generators, Java streams, Rust iterators, LINQ, SQL, MapReduce ([[mapreduce-and-dataflow]]).

```
accumulate(op, initial, seq)   # foldr: op(x1, op(x2, ... op(xn, initial)))
reduce(op, seq)                # foldl in most libraries — check associativity/order for non-commutative op
```

## Why it matters
- Removes duplicated control structure; the remaining code states *what*, not *how*.
- Testable pieces: each stage is pure and small.
- The foundation of functional programming ([[functional-programming-principles]]), of callbacks and
  event handlers, and of parallel data processing (map and reduce distribute trivially).

## Pitfalls
- Deeply nested lambdas hurt readability; name intermediate functions.
- Laziness matters for performance: `map` over a huge list materializes it eagerly in some languages
  (Python 2 list vs Python 3 iterator; use generators — [[streams-and-lazy-evaluation]]).
- Closures over mutable variables capture the variable, not the value (late binding in loops).
- fold-left vs fold-right differ for non-associative operations and for stack use.

## Related
- [[substitution-and-environment-models]], [[recursion-and-iteration]], [[data-abstraction]],
  [[streams-and-lazy-evaluation]], [[functional-programming-principles]].

## Sources
SICP 1.3, 2.2.3; Composing Programs 1.6; HtDP Part III.

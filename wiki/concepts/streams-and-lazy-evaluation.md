---
title: Streams, delayed evaluation, iterators, and generators
type: concept
section: "2.1"
level: 200
tags: [streams, lazy-evaluation, delayed-evaluation, iterators, generators, yield, infinite-sequences, memoization, thunks, normal-order, pipelines]
sources: [sicp, composing-programs]
summary: A stream is a pair whose rest is delayed — a memoized thunk — so infinite sequences (integers, primes by sieve, power series) can be defined recursively and consumed lazily; Python generators/iterators are the same idea, and the pattern turns state-over-time into a pure function of a stream.
---
# Streams and lazy evaluation

**In one sentence.** `(cons-stream a b)` evaluates `a` now and wraps `b` in a memoized thunk;
`stream-cdr` forces it — so a stream is computed one element at a time, only as far as needed.

## Mechanism (SICP 3.5)
- `delay` creates a thunk; `force` runs it; `memo-proc` caches the result so forcing twice costs once.
  Without memoization, recursive stream definitions do exponential work.
- Infinite streams: `integers = cons-stream 1 (map (+1) integers)`; Eratosthenes sieve as a stream
  filter; Fibonacci as `fibgen`; power series arithmetic; `sqrt-stream` of successive approximations
  and sequence accelerators (Euler transform) as stream transformers.
- Streams as **signals**: `integral` of a stream with feedback loops; a bank account whose balance is
  the running fold of a request stream — "time" modelled as the sequence, not as mutation
  ([[assignment-state-and-environments]]).
- Normal-order evaluation everywhere (the lazy evaluator, SICP 4.2) makes every list a stream but
  complicates reasoning about when side effects happen; Haskell takes this route
  ([[functional-programming-principles]]).

## In mainstream languages
- **Iterators**: an object with `next()` (Python `__iter__`/`__next__`, Java `Iterator`, Rust
  `Iterator` trait). Lazy by construction; `map`/`filter`/`zip` return iterators in Python 3.
- **Generators**: functions with `yield` — the runtime saves the frame between calls; a generator *is*
  a stream with the thunk being "resume the function". `yield from` for delegation; generator
  expressions `(f(x) for x in xs)`.
- Rust iterators compile lazy pipelines to loops with zero overhead; Java streams add parallelism.
- Reactive streams / async iterators for events over time (`async for`).

## When to use
- Data larger than memory or unbounded (log tailing, network responses): process incrementally.
- Pipelines where early termination is common (`first match`, `take(10)`) — avoid materializing.
- Decoupling producers from consumers; defining sequences recursively/self-referentially.

## Pitfalls
- A generator can be consumed once; iterating twice silently yields nothing the second time.
- Laziness hides *when* work happens: exceptions surface at `next()`, resources (files) may stay open,
  and side effects inside a lazy `map` may never run.
- Space leaks: holding the head of a long stream keeps every memoized element alive.
- Debugging lazily evaluated code is harder (stack traces point at forcing sites).

## Related
- [[higher-order-functions]], [[assignment-state-and-environments]], [[substitution-and-environment-models]]
  (normal vs applicative order), [[functional-programming-principles]].

## Sources
SICP 3.5 (streams), 4.2 (lazy evaluation); Composing Programs 4.2 (implicit sequences, generators).

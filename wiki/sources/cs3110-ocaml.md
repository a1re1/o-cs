---
title: OCaml Programming: Correct + Efficient + Beautiful (Cornell CS 3110)
type: source
section: "2.4"
level: 200
tags: [ocaml, functional-programming, variants, pattern-matching, higher-order-functions, fold, modules, functors, monads, mutability, interpreters, type-inference, red-black-trees, persistent-arrays]
sources: []
authors: [Michael R. Clarkson et al.]
year: 2024
institution: Cornell
url: https://cs3110.github.io/textbook/
license: CC-BY-NC-ND
format: html
summary: Cornell's free OCaml textbook with videos — basics, data and types (lists, variants, records, pattern matching, options), higher-order programming (map, filter, fold, pipelining), modules and functors, modular programming with data structures, correctness (specs, testing, proofs by induction), mutability, monads, and language implementation (interpreters, substitution/environment models, type checking and inference) — with a Curry–Howard lagniappe.
---
# OCaml Programming (CS 3110)

## What it is
Level 200 (after CS 2110). Parts: **Introduction** (1 better programming through OCaml; 2 basics —
expressions, functions, let, scope, type annotations); **Data and Types** (3 lists, variants, unit
testing, records/tuples, ADTs, options, association lists, algebraic data types, exceptions; 4
higher-order programming — map, filter, fold, beyond lists, pipelining, currying); **Modules** (5
modules, signatures, encapsulation, functional data structures, compilation units, functors,
includes); 6 modular programming with data structures; **Correctness** (7 specifications, testing,
proofs about programs — induction on naturals, lists and trees, structural induction); 8
mutability; 9 data structures (hash tables, amortized analysis, red-black trees, sequences,
memoization, persistent arrays, 2-3 trees); 10 interpreters (calculator, parsing, substitution model,
environment model, type checking, type inference); lagniappe: Curry–Howard.

## Key ideas → pages
- Variants + pattern matching with exhaustiveness checking — [[algebraic-data-types]].
- The **Abstraction Principle** ("factor out recurring patterns"): map/filter/fold derived by
  parameterizing sum and concat — [[higher-order-functions]], [[fold-and-structural-recursion]].
- Modules as ADTs: signatures hide representation; functors are functions from modules to modules
  (not inheritance: the output can be anything) — [[ml-modules-and-functors]], [[data-abstraction]].
- Monads (Maybe, Writer, State) as a design pattern with laws — [[monads]].
- Persistent (functional) data structures, amortized analysis via banker's method —
  [[persistent-data-structures]], [[amortized-analysis]].
- Specifications, unit tests and proofs by induction as one continuum — [[specifications-and-invariants]],
  [[induction]]; interpreters and type inference — [[interpreters-eval-apply]], [[type-systems]].

## What it adds
The most complete free FP course; pairs the ideas from [[hughes-why-fp-matters]] and
[[wadler-monads]] with a typed, strict language and a real module system (vs Scheme in [[sicp]]).

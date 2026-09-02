---
title: Structure and Interpretation of Computer Programs (Abelson, Sussman & Sussman)
type: source
section: "2.1"
level: 100
tags: [sicp, scheme, abstraction, higher-order-functions, data-abstraction, state, streams, interpreters, metacircular-evaluator, register-machines, lisp]
sources: []
authors: [Harold Abelson, Gerald Jay Sussman, Julie Sussman]
year: 1996
institution: MIT
url: https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html
license: CC-BY-SA
format: html
summary: The "wizard book" (2nd ed., free, CC-BY-SA; JavaScript edition 2022) — five chapters that build up from procedures and the substitution model, through data abstraction and higher-order sequence operations, to assignment/state/streams, a metacircular Scheme interpreter with lazy, nondeterministic and logic-programming variants, and finally a register-machine compiler — the canonical statement that programs are about managing complexity through abstraction.
---
# Structure and Interpretation of Computer Programs (SICP)

## What it is
MIT's 6.001 text (1985–2007), Scheme throughout; free HTML/PDF; *SICP in JavaScript* (2022) is an
official port. Chapters: **1 Building abstractions with procedures** (expressions, naming, the
substitution model, conditionals, Newton's square root, procedures as black boxes; linear recursion vs
iteration, tree recursion, orders of growth, exponentiation, gcd, primality; higher-order procedures,
lambda, procedures as general methods — fixed points — and as returned values). **2 Building
abstractions with data** (rational numbers, abstraction barriers, "what is meant by data" — data as
closures; sequences, hierarchical data, the closure property, sequences as conventional interfaces, the
picture language; symbolic data: differentiation, sets, Huffman trees; multiple representations, tagged
data, data-directed and message-passing styles; generic arithmetic with coercion). **3 Modularity,
objects, and state** (assignment and local state, the costs of assignment, environment model, mutable
data, queues and tables, digital circuit simulator, constraint propagation; concurrency and
serializers; streams and delayed evaluation). **4 Metalinguistic abstraction** (the metacircular
evaluator eval/apply, lazy evaluator, `amb` nondeterministic evaluator, logic programming/query
language). **5 Computing with register machines** (register-machine simulator, storage allocation and
garbage collection, a compiler for Scheme).

## Key ideas → pages
- Three mechanisms of every language: primitives, means of combination, means of abstraction.
- Substitution model, then the environment model once assignment appears —
  [[substitution-and-environment-models]].
- A recursive *procedure* can generate an iterative *process* (tail calls); tree recursion and
  exponential blow-up; memoization — [[recursion-and-iteration]].
- Procedures as arguments/results; fixed points, average damping, Newton as a higher-order method;
  lambda and let — [[higher-order-functions]].
- Data abstraction: constructors/selectors, **abstraction barriers**, "data is defined by the
  conditions the selectors and constructor satisfy" (pairs implemented as procedures) —
  [[data-abstraction]].
- **Sequences as conventional interfaces**: enumerate → map → filter → accumulate; the signal-flow view
  that makes structurally different programs share code — [[higher-order-functions]].
- Tagged data, data-directed dispatch tables vs message passing — the two ways to add operations/types
  (the expression problem) — [[data-abstraction]].
- Assignment breaks the substitution model and referential transparency; identity vs equality; the
  environment model — [[assignment-state-and-environments]].
- Streams = delayed evaluation; infinite sequences; "time" as a stream — [[streams-and-lazy-evaluation]].
- The metacircular evaluator: eval dispatches on expression type, apply on procedure type; the
  environment is the interpreter's central data structure — [[interpreters-eval-apply]].

## Notable claims & quotes
- "Programs must be written for people to read, and only incidentally for machines to execute."
- On assignment: "no simple model with 'nice' mathematical properties can be an adequate framework for
  dealing with objects and assignment."
- "The evaluator, which determines the meaning of expressions in a programming language, is just another program."

## What it adds
The foundational framing for §2 (abstraction as the tool against complexity), §2.4 (functional
programming, laziness), §4.3 (interpreters), §5.4 (evaluation models). [[composing-programs]] is its
Python adaptation; [[htdp]] is its methodological rival.

---
title: Composing Programs (DeNero) and Berkeley CS61A
type: source
section: "2.1"
level: 100
tags: [python, cs61a, environment-diagrams, higher-order-functions, recursion, oop, iterators, generators, scheme-interpreter, sql, declarative-programming]
sources: []
authors: [John DeNero]
year: 2024
institution: UC Berkeley
url: https://www.composingprograms.com/
license: CC-BY-NC-SA
format: html
summary: The free Python adaptation of SICP used by Berkeley CS61A — functions and environment diagrams, higher-order functions and recursion, data abstraction, mutability, OOP and inheritance, iterators/generators, then interpreters (a Scheme interpreter project) and declarative programming with SQL — with a 3rd edition (2025) adding guidance on using AI tools after learning the foundations.
---
# Composing Programs / Berkeley CS61A

## What it is
CS61A "Structure and Interpretation of Computer Programs" in Python (plus Scheme and SQL), ~1,500
students/term, fully open (lectures, labs, homework, projects: Hog, Cats, Ants, Scheme interpreter).
Text chapters: **1 Functions** (elements of programming, defining functions, designing functions —
docstrings, assertions, the "functions should do one thing" rule — control, higher-order functions,
recursion); **2 Data** (native types, data abstraction, sequences, mutable data, object-oriented
programming, implementing classes and objects, composition, generic operations, efficiency,
recursive objects: linked lists and trees); **3 Interpreting computer programs** (functional
programming, exceptions, interpreters for languages with combination and abstraction — a
calculator, then Scheme); **4 Data processing** (implicit sequences: iterators, generators, streams;
declarative programming: SQL, recursive select; unification/logic programming; distributed and
parallel computing). The 3rd edition (in progress, 2025) rewrites chapter 1 with the thesis "understand
how languages represent information and manage complexity first, *then* use AI tools".

## Key ideas → pages
- **Environment diagrams** (frames, bindings, the parent pointer rule: a function's parent is the frame
  in which it was defined) as the mental model for scoping and closures —
  [[substitution-and-environment-models]], [[assignment-state-and-environments]].
- Recursion taught with "the recursive leap of faith" and tree recursion (counting partitions) —
  [[recursion-and-iteration]].
- Higher-order functions: functions as arguments, as returned values (make_adder), currying,
  decorators — [[higher-order-functions]].
- Data abstraction with "abstraction barrier violations" called out explicitly — [[data-abstraction]].
- Mutable data and identity vs equality (`is` vs `==`), the object system built from dispatch
  dictionaries, inheritance and multiple inheritance — [[data-abstraction]], [[objects-and-classes]].
- Iterators, generators, `yield`, lazy sequences — [[streams-and-lazy-evaluation]].
- Interpreters: read-eval-print loop, calculator language, the Scheme project — [[interpreters-eval-apply]].

## What it adds
The same ideas as [[sicp]] with Python's syntax, environment diagrams as a first-class teaching tool,
and SQL/declarative programming; the best on-ramp for someone who already codes in Python.

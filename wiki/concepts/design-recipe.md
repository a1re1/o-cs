---
title: The design recipe — data definitions, signatures, examples, templates, tests
type: concept
section: "2.1"
level: 100
tags: [design-recipe, data-definitions, signatures, purpose-statements, examples-first, templates, structural-recursion, unit-tests, incremental-development, docstrings, wishful-thinking]
sources: [htdp, composing-programs, think-python]
summary: HtDP's six-step method for writing any function — data definition, signature + purpose, examples as tests, a template derived from the data's shape, code, tests — with Composing Programs' and Think Python's companions (docstrings, assertions, incremental development, wishful thinking) — the beginner's version of spec-first, test-first design.
---
# The design recipe

**In one sentence.** Before writing the body of a function, write what it consumes and produces,
what it is for, and examples of it working; the code then largely writes itself from the shape of the data.

## The steps (HtDP)
1. **Data definition** — name the kind of data and its shape; for compound or self-referential data
   spell out the variants (`; A Shape is one of: (make-circle r) | (make-rect w h)`).
2. **Signature and purpose statement** — `; area : Shape -> Number  ; computes the area of s`.
   In Python: type hints + a one-line docstring saying *what*, not *how*.
3. **Functional examples** — concrete inputs and expected outputs; edge cases (empty list, zero, one
   element). They become the tests.
4. **Template** — the skeleton dictated by step 1: a `cond` with one clause per variant; selectors for
   each field; a recursive call for each self-reference. (This is [[recursion-and-iteration]]'s
   structural recursion and [[induction]] made mechanical.)
5. **Definition** — fill in the template; combine the pieces with wishful thinking ("assume the recursive
   call works").
6. **Test** — run the examples; when one fails, fix and re-run; keep them as regression tests.
Then: if two functions share a template, abstract the difference into a parameter
([[higher-order-functions]]).

## Companion habits
- **Incremental development** (Think Python): add a few lines, run, print intermediates, remove
  scaffolding; never write 100 lines before running once.
- **Wishful thinking** (SICP): write the top-level function using helpers you have not written yet,
  with their signatures decided; then write them.
- **Assertions/docstrings** (Composing Programs): `assert` preconditions; `doctest` examples in
  docstrings are steps 2–3 in one place.
- Function guidelines: one job per function, no repetition (DRY), general enough to be reused, good
  names (verbs for functions, nouns for values), and short.

## Why it works
Most beginner bugs are *design* bugs: unclear inputs, missing cases, no examples. Steps 1–3 force the
thinking before typing; step 4 guarantees every case is handled; step 6 makes correctness checkable.
The same discipline scales up as specifications, representation invariants, and test-first development
([[specifications-and-invariants]], [[unit-testing]]).

## Pitfalls
- Skipping examples ("it's obvious") — the edge cases hide there.
- Templates for generative recursion don't follow the data; those need a termination argument.
- Tests that restate the code rather than the intent.

## Related
- [[recursion-and-iteration]], [[higher-order-functions]], [[debugging]], [[specifications-and-invariants]],
  [[unit-testing]].

## Sources
HtDP Prologue and Parts I–III (the design recipe); Composing Programs 1.4 (designing functions); Think Python ch. 4, 6.

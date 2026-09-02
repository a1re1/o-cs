---
title: A Philosophy of Software Design (Ousterhout)
type: source
section: "2.2"
level: 300
tags: [software-design, complexity, deep-modules, information-hiding, interfaces, abstraction, comments, strategic-programming, design-it-twice, exceptions]
sources: []
authors: [John Ousterhout]
year: 2021
institution: Stanford
url: https://web.stanford.edu/~ouster/cgi-bin/book.php
license: proprietary-open-access
format: pdf
summary: The Stanford CS190 book (2nd ed. 2021; free lecture videos) that defines complexity as "anything that makes software hard to understand or modify" (symptoms: change amplification, cognitive load, unknown unknowns; causes: dependencies and obscurity) and argues for deep modules, information hiding, general-purpose interfaces, pulling complexity downward, defining errors out of existence, strategic (not tactical) programming, and comments that say what code cannot.
---
# A Philosophy of Software Design (Ousterhout, 2nd ed.)

## What it is
Short (~190 pages), opinionated, distilled from teaching CS190 where students build and review large
programs. Chapters: the nature of complexity; working code isn't enough (strategic vs tactical
programming); modules should be deep; information hiding and leakage; general-purpose modules are
deeper; different layer, different abstraction; pull complexity downwards; better together or better
apart; define errors out of existence; design it twice; why write comments; comments should describe
things that aren't obvious from the code; choosing names; write the comments first; modifying existing
code; consistency; code should be obvious; software trends (agile, unit tests, TDD, design patterns,
getters/setters); designing for performance; decide what matters; conclusion.

## Key ideas → pages
- **Complexity** = dependencies + obscurity; symptoms are change amplification, cognitive load, and
  unknown unknowns; it accumulates incrementally — "zero tolerance" — [[managing-complexity-in-software-design]].
- **Deep modules**: large functionality behind a small interface (Unix file I/O: five calls); shallow
  modules (a class per tiny thing, "classitis") add interface cost without hiding anything —
  [[managing-complexity-in-software-design]], [[modularity-and-information-hiding]].
- **Information hiding vs leakage**; temporal decomposition is a classic leak (splitting by *when*
  things happen rather than by *what knowledge* they need) — [[modularity-and-information-hiding]].
- **Define errors out of existence** (e.g. `unset` of a missing variable is a no-op; substring with
  out-of-range indices clamps) and mask exceptions at low levels; exceptions are a major source of
  complexity — [[specifications-and-invariants]] (contrast with 6.102's "fail fast").
- **Strategic programming**: invest 10–20% of effort in design; **design it twice**; comments should
  capture what the code cannot (interface comments describe abstraction, implementation comments
  describe *why*); write comments first as a design tool — [[code-review]].
- Skeptical of TDD (leads to tactical code) and of getters/setters; supportive of unit tests as enablers
  of refactoring — [[unit-testing]].

## Notable claims & quotes
- "Complexity is anything related to the structure of a software system that makes it hard to
  understand and modify the system."
- "The best modules are those that provide powerful functionality yet have simple interfaces."
- "Working code isn't enough."

## What it adds
A vocabulary for *design quality* (depth, leakage, cognitive load) that [[mit-6-102-software-construction]]
lacks, and a counterweight: where 6.102 says "fail fast", Ousterhout says "define errors out of existence" —
both are right at different layers (see contradiction note in [[specifications-and-invariants]]).

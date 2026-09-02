---
title: How to Design Programs (Felleisen, Findler, Flatt, Krishnamurthi)
type: source
section: "2.1"
level: 100
tags: [htdp, design-recipe, racket, data-definitions, structural-recursion, generative-recursion, accumulators, testing, teaching-languages]
sources: []
authors: [Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi]
year: 2018
institution: Northeastern / Brown / Utah / Northwestern
url: https://htdp.org/
license: CC-BY-NC-ND
format: html
summary: The free 2nd edition (2018, updated 2024) that teaches programming as *systematic design* — the design recipe (data definition → signature/purpose → examples/tests → template from the data's shape → code → test) across fixed-size data, arbitrarily large data, abstraction, intertwined data, generative recursion, and accumulators, using Racket's teaching languages.
---
# How to Design Programs (HtDP, 2nd ed.)

## What it is
Prologue "How to Program"; **I Fixed-size data** (structures, enumerations, intervals, itemizations;
the design recipe); **II Arbitrarily large data** (lists, natural numbers, self-referential data
definitions, structural recursion, larger designs: worlds/games); **III Abstraction** (similarities in
functions, abstracting from templates, using abstractions — map/filter/foldr — lambda); **IV Intertwined
data** (trees, S-expressions, mutually recursive data, projects); **V Generative recursion**
(algorithms whose recursion is not dictated by the data's shape: quicksort, gcd, backtracking;
termination arguments); **VI Accumulators** (when structural recursion loses context: accumulator-style
functions; a "graph traversal with visited set" example). Intermezzos cover the teaching languages,
quote/quasiquote, scope, numbers, and the cost of computation.

## The design recipe (the book's contribution)
1. **Data definition**: describe the data with a comment/type and, for compound/self-referential data,
   an explicit shape (`; A List-of-numbers is either '() or (cons Number List-of-numbers)`).
2. **Signature, purpose statement, header**: `; sum : List-of-numbers -> Number`.
3. **Functional examples** that become tests (`check-expect`).
4. **Template**: the skeleton follows the data definition — one `cond` clause per variant, one selector
   call per field, a recursive call for each self-reference.
5. **Code**: fill in the template.
6. **Test**, and refine. Abstraction step: when two functions share a template, abstract to a
   higher-order function.

## Key ideas → pages
- Structural recursion follows the data's shape; the template *is* the proof-by-induction skeleton —
  [[recursion-and-iteration]], [[design-recipe]].
- Generative recursion needs a separate termination argument (the [[invariant-principle]] measure).
- Accumulators as the transition to loops and to tail recursion — [[recursion-and-iteration]].
- Tests first, from examples — [[design-recipe]].

## What it adds
A *method* rather than a tour: [[sicp]] shows what abstraction can do; HtDP tells a beginner what to
write next. Its data-definition-driven templates are algebraic data types and pattern matching in
disguise (§2.4), and the design recipe is the ancestor of "write the spec and tests first" in §2.2.

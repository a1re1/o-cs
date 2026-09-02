---
title: Refactoring: Improving the Design of Existing Code (Fowler, 2nd ed. 2018) and Object-Oriented Software Construction (Meyer)
type: source
section: "2.5"
level: 300
tags: [refactoring, code-smells, extract-function, rename, move, inline, replace-conditional-with-polymorphism, tests, design-by-contract, meyer, open-closed, command-query-separation]
sources: []
authors: [Martin Fowler, Kent Beck, Bertrand Meyer]
year: 2018
institution: ThoughtWorks / ETH Zürich
url: https://refactoring.com/catalog/
license: proprietary
format: book
summary: Fowler defines refactoring as behavior-preserving restructuring in small steps under a test safety net, catalogues code smells (duplicated code, long function, feature envy, data clumps, primitive obsession, shotgun surgery, …) and ~60 named refactorings (Extract Function, Inline, Rename, Move, Replace Temp with Query, Replace Conditional with Polymorphism, Introduce Parameter Object, …); Meyer's OOSC contributes design by contract, command–query separation and the open–closed principle.
---
# Refactoring (Fowler) / Object-Oriented Software Construction (Meyer)

## What it is
Fowler: ch. 1 a worked example (theatrical billing → extract, split loops, move to polymorphism);
ch. 2 principles — definition ("a change made to the internal structure … without changing its
observable behavior"), the two hats (adding function vs refactoring), when (rule of three,
preparatory, comprehension, litter-pickup), when not (rewrite), the relationship with performance
and with tests; ch. 3 **bad smells in code** (mysterious name, duplicated code, long function, long
parameter list, global data, mutable data, divergent change, shotgun surgery, feature envy, data
clumps, primitive obsession, repeated switches, loops, lazy element, speculative generality,
temporary field, message chains, middle man, insider trading, large class, alternative classes with
different interfaces, data class, refused bequest, comments); ch. 4 building tests; ch. 6–12 the
catalogue: first set (Extract/Inline Function, Extract/Inline Variable, Change Function Declaration,
Encapsulate Variable, Rename, Introduce Parameter Object, Combine Functions into Class/Transform,
Split Phase), encapsulation, moving features, organizing data, simplifying conditional logic
(Decompose Conditional, Consolidate, Replace Nested Conditional with Guard Clauses, Replace
Conditional with Polymorphism, Introduce Special Case, Introduce Assertion), refactoring APIs
(Separate Query from Modifier, Parameterize Function, Replace Parameter with Query, Replace Error
Code with Exception, Replace Exception with Precheck), dealing with inheritance (Pull Up/Push Down,
Replace Subclass with Delegate, Replace Superclass with Delegate).
Meyer OOSC: design by contract (preconditions, postconditions, class invariants; "the contract"
metaphor), command–query separation, the open–closed principle, uniform access, genericity vs
inheritance.

## What it adds
[[refactoring]] and the smells → refactorings map; contracts feed [[specifications-and-invariants]]
and [[liskov-substitution]]; open–closed is a pillar of [[solid-principles]].

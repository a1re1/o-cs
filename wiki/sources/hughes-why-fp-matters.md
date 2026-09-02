---
title: Why Functional Programming Matters (Hughes, 1990)
type: source
section: "2.4"
level: 200
tags: [functional-programming, higher-order-functions, fold, lazy-evaluation, modularity, glue, streams, newton-raphson, alpha-beta, miranda]
sources: []
authors: [John Hughes]
year: 1990
institution: Chalmers
url: https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf
license: open-access
format: pdf
summary: The classic argument that FP's value is not the absence of assignment but two new kinds of glue — higher-order functions (foldr generalizes to trees, map is a fold) and lazy evaluation (generators like repeat/within/relative and infinite game trees for alpha-beta) — which let programs be decomposed into smaller, reusable, independently improvable parts.
---
# Why Functional Programming Matters

## What it is
A 20-page essay in Miranda. §1: the "no assignment, no side effects" characterization is a list of
what FP lacks; the real question is what it enables. §2: the case for modularity — one must be able
to *glue* solutions to subproblems together, and the kinds of glue a language provides bound the
modularity achievable. §3 gluing functions together: `foldr`, `map = foldr (Cons . f) Nil`,
`summatrix = sum . map sum`, `foldtree`, and *the same trick on any recursive datatype*. §4 gluing
programs together: lazy evaluation lets a producer (`repeat (next n) a0` — infinite Newton–Raphson
approximations) be composed with independent consumers (`within eps`, `relative eps`); numerical
differentiation and integration with `elimerror`/`order`/`improve` (Richardson extrapolation as a
stream transformer); alpha-beta search as `maximize . maptree static . prune 5 . gametree`, where
the infinite game tree is pruned lazily and `maximize'` returns lists of numbers so the minimum of
a maximum can be short-cut. §5: conclusion — modularity is the key to successful programming, and
FP's glue is what makes small, general, reusable parts possible.

## Notable claims
- "Lazy evaluation is perhaps the most powerful tool for modularization in the functional
  programmer's repertoire" — it decouples termination conditions from generators.
- Small modules reuse: `within` and `relative` serve square roots, derivatives and integrals.
- The alpha-beta example shows a "whole program" being simplified by lazy composition of parts,
  each of which is a one-liner.

## What it adds
The rationale for [[higher-order-functions]] and [[streams-and-lazy-evaluation]] as *modularity
mechanisms* rather than tricks; the fold-on-any-datatype idea in [[fold-and-structural-recursion]];
Rust iterators, Python generators and Unix pipes are the same glue in other clothes.

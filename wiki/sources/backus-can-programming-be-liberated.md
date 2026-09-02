---
title: Can Programming Be Liberated from the von Neumann Style? (Backus, 1978 Turing lecture)
type: source
section: "2.4"
level: 300
tags: [functional-programming, fp-language, von-neumann-bottleneck, combining-forms, algebra-of-programs, applicative, history]
sources: []
authors: [John Backus]
year: 1978
institution: IBM
url: https://dl.acm.org/doi/10.1145/359576.359579
license: ACM-open
format: pdf
summary: Backus's Turing lecture attacks "von Neumann languages" — word-at-a-time programming through the CPU–memory bottleneck, with assignment as the bottleneck's intellectual mirror — and proposes FP, a variable-free language of functions combined by fixed combining forms (composition, construction, insert/reduce, apply-to-all) with an algebra of programs enabling equational reasoning.
---
# Can Programming Be Liberated from the von Neumann Style?

## What it is
Sections: the von Neumann computer and its bottleneck (a tube through which words pass one at a
time); von Neumann languages inherit it — assignment statements, "word-at-a-time" thinking, huge
languages with weak mathematical properties; comparison of an inner-product program in a
conventional language vs FP (`Def IP ≡ (Insert +) ∘ (ApplyToAll ×) ∘ Transpose`); the FP system —
objects, functions, functional forms (composition `f∘g`, construction `[f,g]`, condition `p→f;g`,
constant, insert `/f`, apply-to-all `αf`), definitions; the algebra of programs (laws such as
`αf ∘ [g,h] = [f∘g, f∘h]`) used to prove program equivalences and optimize; applicative state
transition systems for the state-bearing parts.

## Notable claims
- "Programming languages appear to be in trouble" — growth in size without growth in expressive
  power; the fix is to build languages around combining forms with clean algebraic laws.
- Programs written without variables can be reasoned about algebraically, like arithmetic.

## What it adds
The historical case for point-free style and combinator libraries; the "algebra of programs" is
what fold fusion, [[higher-order-functions]] laws and [[monads]] laws deliver in practice; the
bottleneck argument foreshadows the [[caches-and-memory-hierarchy]] and data-parallel
[[mapreduce-and-dataflow]] framings.

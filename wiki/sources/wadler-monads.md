---
title: Monads for Functional Programming (Wadler, 1995)
type: source
section: "2.4"
level: 300
tags: [monads, functional-programming, effects, state-monad, exception-monad, writer-monad, parser-combinators, monad-laws, haskell]
sources: []
authors: [Philip Wadler]
year: 1995
institution: University of Glasgow
url: https://homepages.inf.ed.ac.uk/wadler/papers/marktoberdorf/baastad.pdf
license: open-access
format: pdf
summary: The tutorial that made monads usable: a simple evaluator is extended three ways (exceptions, a division counter, an execution trace), each requiring the program to be rewritten; a monad (type M a, unit, bind ⋆) factors the plumbing so each extension is a local change, with the three laws (left unit, right unit, associativity) and applications to state (arrays), parsers, and I/O.
---
# Monads for Functional Programming

## What it is
§2 Evaluating monads: `eval :: Term → Int` for `Con`/`Div`; variation one — exceptions (`M a = Raise
Exception | Return a`), two — state (`M a = State → (a, State)` counting divisions), three — output
(`M a = (Output, a)`). Each pure rewrite threads a different thing through every case: "straightforward
but tedious". §2.5 a monadic evaluator: define `unit :: a → M a` and `⋆ :: M a → (a → M b) → M b` once;
`eval (Div t u) = eval t ⋆ λa. eval u ⋆ λb. unit (a ÷ b)`; each variation is now a local change
(replace `unit (a÷b)` by `raise` / `tick ⋆ λ(). …` / `out … ⋆ λ(). …`). Reversing trace order is a
one-token change in `⋆` — harder in an impure language. §3 the monad laws. §4 state monads: array
update, an interpreter with an array as state, `unit`/`bind` hide the threading. §5 parsers: a monad
of `String → [(a, String)]`, alternation, `item`, sequencing; efficiency and error reporting.
§6 I/O.

## Key claims
- A monad is a type constructor `M` with `unit` and `⋆` obeying: left unit `unit a ⋆ λb.n = n[a/b]`;
  right unit `m ⋆ λa.unit a = m`; associativity `(m ⋆ λa.n) ⋆ λb.o = m ⋆ (λa. n ⋆ λb.o)` — exactly
  what makes `do`-notation/sequencing well-behaved.
- "The type M explicitly indicates what sort of effect may occur": effects become visible in types.
- In a lazy language the pure output monad still prints incrementally.

## What it adds
The reference for [[monads]]; the state monad reappears in [[interpreters-eval-apply]]; parser
combinators in [[lexing-and-parsing]]; the effect-in-the-type idea is the ancestor of `Result`/`?` in
[[rust-traits-generics-lifetimes]] and of effect systems in [[type-systems]].

---
title: Monads — sequencing computations with effects in types
type: concept
section: "2.4"
level: 300
tags: [monads, bind, unit, return, flatmap, maybe-monad, option, result, state-monad, writer-monad, list-monad, parser-combinators, io-monad, monad-laws, functor, applicative, do-notation, effects]
sources: [wadler-monads, cs3110-ocaml, rust-book]
summary: A monad is a type constructor M with `return : a → M a` and `bind : M a → (a → M b) → M b` satisfying left/right identity and associativity; it factors the plumbing of an effect (failure, state, logging, nondeterminism, parsing, I/O) out of the code that uses it, so extending a program with a new effect is a local change — Option/Result chaining, promises, and iterator flatMap are all instances.
---
# Monads

**In one sentence.** A monad packages "a computation that produces an `a` plus some effect" so that
you can chain such computations with `bind` without hand-threading the effect through every step.

## Wadler's demonstration
An evaluator for `Con | Div` needs, in turn, error handling, a division counter, and a trace. Each
pure version rewrites every case to pass the exception/state/output along. Define instead
`unit :: a → M a`, `(⋆) :: M a → (a → M b) → M b`, and write once
`eval (Div t u) = eval t ⋆ λa. eval u ⋆ λb. unit (a ÷ b)`; the three variants become one-line changes
at the site of the effect (`raise`, `tick`, `out`). The type `M` documents which effect may occur.

## The instances you already use
| Monad | `M a` | effect | `bind` does | seen as |
|---|---|---|---|---|
| Maybe/Option | `None \| Some a` | failure | short-circuit on None | `?` in Rust, `and_then`, optional chaining `?.` |
| Either/Result | `Err e \| Ok a` | failure with reason | propagate first Err | `?`, `Result::and_then`, exceptions in types |
| List | `[a]` | nondeterminism | flatMap | list comprehensions, `SelectMany` |
| State | `s → (a, s)` | mutable state | thread the state | interpreters, random generators, parsers |
| Writer | `(w, a)` | logging/output | append logs | trace collection |
| Reader | `r → a` | environment/config | pass env along | dependency injection |
| Parser | `String → [(a, String)]` | consume input | sequence parsers | parser combinators ([[parsing]]) |
| IO / Promise / Future | world → (a, world) | I/O, async | run then continue | `async/await`, `.then` |

## Laws (what makes `do`/`let*`/`?` behave)
Left identity `return a >>= f = f a`; right identity `m >>= return = m`; associativity
`(m >>= f) >>= g = m >>= (λx. f x >>= g)`. They say sequencing has no hidden extra effect and that
bracketing does not matter — so syntax sugar (`do` in Haskell, `let*` in OCaml, `for` in Scala,
`?` in Rust) can flatten nesting.

## Around the monad
`Functor` (`map`), `Applicative` (`pure`, `<*>`: independent effects, no data dependency — enables
parallel validation that collects *all* errors, which a monad cannot), `Monad` (dependent
sequencing). Monad transformers / effect systems compose effects; "monads don't compose" is the
practical complaint.

## When to use the idea (even without the word)
- Chaining fallible operations: prefer `Option`/`Result` combinators or `?` over nested ifs.
- Threading state through recursive code: a `State`-style signature `s -> (a, s)` avoids globals and
  keeps functions pure and testable ([[unit-testing]]).
- Designing DSLs/interpreters: the monadic evaluator lets you add effects late
  ([[interpreters-eval-apply]]).

## Pitfalls
- Confusing the container with the sequencing: `List` is a monad because of flatMap, not because it
  holds things.
- Over-abstracting in languages without typeclasses/HKTs — a plain `and_then` API is often enough.
- Assuming laws hold: a "monad" whose bind reorders effects breaks refactoring.

## Related
- [[higher-order-functions]], [[algebraic-data-types]], [[rust-traits-generics-lifetimes]],
  [[interpreters-eval-apply]], [[parsing]], [[type-systems]].

## Sources
Wadler 1995 §2–5; CS3110 ch. 8.7 (monads); Rust Book ch. 9.

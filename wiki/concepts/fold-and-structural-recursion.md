---
title: Fold, structural recursion, and the Abstraction Principle
type: concept
section: "2.4"
level: 200
tags: [fold, foldr, foldl, reduce, map, filter, structural-recursion, catamorphism, abstraction-principle, tail-recursion, fusion, higher-order-functions]
sources: [hughes-why-fp-matters, cs3110-ocaml, sicp]
summary: Every recursive datatype has a fold that replaces its constructors with functions (foldr replaces Cons by f and Nil by z); sum, product, length, map, filter, append and reverse are all folds, foldl is the tail-recursive accumulator version, the same construction gives foldtree for trees and an eval for expression types, and factoring a recurring recursion pattern into a higher-order function is the Abstraction Principle in action.
---
# Fold and structural recursion

**In one sentence.** `foldr f z [a,b,c] = f a (f b (f c z))` — "replace every Cons with f and Nil
with z" — and once you see that, most list functions are one-liners and the same idea works for
any [[algebraic-data-types]] type.

## Deriving it (Hughes §3, CS3110 4.3)
`sum [] = 0; sum (h::t) = h + sum t` and `concat [] = ""; concat (h::t) = h ^ concat t` differ only in
the base value and the combining operator → factor both out:
`foldr f z [] = z; foldr f z (h::t) = f h (foldr f z t)`. Then
`sum = foldr (+) 0`, `product = foldr (*) 1`, `anytrue = foldr (||) false`, `length = foldr (fun _ n
-> n+1) 0`, `map f = foldr (fun x acc -> f x :: acc) []`, `filter p = foldr (fun x acc -> if p x then
x :: acc else acc) []`, `append xs ys = foldr cons ys xs`, `foldr cons [] = id`.

## foldr vs foldl
- `foldr` is right-associative, matches the list's structure, works on infinite lists with a lazy
  `f` (e.g. `any`) — but uses O(n) stack in strict languages.
- `foldl f z [a,b,c] = f (f (f z a) b) c` — tail-recursive, constant stack, natural for accumulators
  (reverse, sums); Haskell needs the strict `foldl'` to avoid thunk build-up. `reduce` in
  Python/JS/Rust `fold` are left folds. For associative `f` with identity `z` the two agree, which is
  what lets [[mapreduce-and-dataflow]] parallelize a reduce.
- OCaml argument orders differ (`List.fold_left f init l` vs `List.fold_right f l init`) — a
  classic source of bugs.

## Beyond lists
Trees: `foldtree f g z (Node label subtrees)` replaces Node with `f` and the subtree list's
Cons/Nil with `g`/`z` (Hughes), or `fold_tree leaf node`. Expressions: `eval` is the fold whose
`f`'s are the operators. In general the fold of a type is its **catamorphism**: one function per
constructor, arity matching the fields, recursive fields already folded. Writing a function by
following the type's constructors is **structural recursion**, and it terminates because arguments
shrink — the computational twin of structural [[induction]] and the [[design-recipe]]'s template step.

## Laws and performance
`map f . map g = map (f . g)` and fold/build fusion let compilers eliminate intermediate lists
(Backus's algebra of programs — [[backus-can-programming-be-liberated]]); iterator chains in Rust and
generator pipelines in Python get the same effect by laziness ([[streams-and-lazy-evaluation]]).

## Pitfalls
- Using `foldr` on huge lists in a strict language (stack overflow); use `foldl`/tail recursion.
- Non-associative operators with the wrong fold direction (subtraction, list building with `@`
  giving O(n²)).
- Reaching for an explicit loop with mutable state where a fold names the pattern ("If you're
  writing the same recursion twice, abstract it" — CS3110's Abstraction Principle).

## Related
- [[higher-order-functions]], [[algebraic-data-types]], [[recursion-and-iteration]], [[induction]],
  [[streams-and-lazy-evaluation]], [[mapreduce-and-dataflow]].

## Sources
Hughes §3; CS3110 4.3–4.4; SICP 2.2.3 (accumulate).

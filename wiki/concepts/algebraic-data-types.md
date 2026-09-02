---
title: Algebraic data types and pattern matching
type: concept
section: "2.4"
level: 200
tags: [algebraic-data-types, adt, sum-types, product-types, variants, records, pattern-matching, exhaustiveness, option, result, tagged-union, ocaml, rust, haskell, make-illegal-states-unrepresentable]
sources: [cs3110-ocaml, rust-book, hughes-why-fp-matters]
summary: An algebraic data type is built from products (records/tuples: this AND that) and sums (variants: this OR that, each tagged), possibly recursive (lists, trees, expressions); pattern matching destructures values by shape with compiler-checked exhaustiveness, so adding a case is caught everywhere, and the design rule "make illegal states unrepresentable" follows directly.
---
# Algebraic data types (ADTs) and pattern matching

**In one sentence.** Model data as sums of products — `type shape = Circle of float | Rect of float *
float` — and let `match` take it apart; the compiler tells you when you forgot a case.

## Why "algebraic"
Product `A × B` has |A|·|B| values; sum `A + B` has |A| + |B|; `unit` is 1, `bool` is 2, `option a` is
`1 + a`, `list a = 1 + a × list a` (a recursive equation). Counting states makes design errors
visible: a record `{loading: bool; data: option; error: option}` has 8 states but 3 are meaningful;
`Loading | Loaded of data | Failed of error` has exactly 3 — the "make illegal states
unrepresentable" rule (Yaron Minsky).

## Language forms
| | OCaml | Rust | Haskell | TypeScript/Java |
|---|---|---|---|---|
| sum | `type t = A \| B of int` | `enum T { A, B(i32) }` | `data T = A \| B Int` | tagged unions / sealed interfaces + records |
| product | tuples, records | structs, tuples | records, tuples | classes |
| match | `match x with \| A -> … \| B n -> …` | `match x { A => …, B(n) => … }` | `case`/equations | `switch` on `kind` / pattern matching (Java 21) |
The "expression problem": ADTs make adding *operations* easy (one new function) and adding *cases*
hard (edit every match); objects are the mirror image ([[data-abstraction]], [[objects-and-classes]]).

## Pattern matching
Patterns nest (`Some (x :: rest)`), bind variables, use wildcards `_`, guards (`when`), or-patterns,
literals; matching is a **total function by construction** when exhaustive (warning/error otherwise)
— which is why refactoring by adding a variant is safe. Recursive functions follow the type's shape
([[fold-and-structural-recursion]], [[induction]] for proofs about them). `Option`/`Result` are the
everyday ADTs that replace null and exceptions ([[rust-traits-generics-lifetimes]]).

## Idioms
- Expression trees: `type expr = Num of int | Add of expr * expr | …` with `eval` by match — the
  entry point to [[interpreters-eval-apply]].
- State machines as variants carrying only the data valid in that state.
- Newtypes/opaque single-constructor types for units and validated values
  ([[abstract-data-types-and-rep-invariants]]).
- Zippers, finger trees, and other structures are ADTs plus invariants ([[persistent-data-structures]]).

## Pitfalls
- Catch-all `_` arms defeat exhaustiveness checking — avoid them when you'll add variants.
- Deeply nested matches: introduce helper functions per constructor; use records for many fields.
- Boolean blindness (`bool * bool`) where a sum type would name the cases.

## Related
- [[fold-and-structural-recursion]], [[data-abstraction]], [[type-systems]], [[interpreters-eval-apply]],
  [[rust-traits-generics-lifetimes]], [[sets-relations-functions]] (the counting).

## Sources
CS3110 ch. 3 (variants, options, ADTs); Rust Book ch. 6; Hughes §3 (`treeof`).

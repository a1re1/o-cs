---
title: The lambda calculus — syntax, β-reduction, Church encodings, fixed-point combinators, evaluation strategies, confluence, and why it is the core of every functional language
type: concept
section: "5.4"
level: 400
tags: [lambda-calculus, untyped-lambda-calculus, abstraction, application, beta-reduction, alpha-conversion, eta, free-variables, substitution, capture-avoiding, de-bruijn-indices, church-numerals, church-booleans, church-encoding, pairs, y-combinator, fixed-point-combinator, recursion, normal-form, call-by-name, call-by-value, call-by-need, evaluation-strategy, confluence, church-rosser, normalization, combinators, ski, turing-complete, simply-typed-lambda-calculus, strong-normalization]
sources: [pierce-tapl-and-pl-theory-texts, pl-theory-seminal-papers]
summary: Church's λ-calculus has three forms — variables, abstraction λx.M, application M N — and one rule, β-reduction ((λx.M) N → M[x := N] with capture-avoiding substitution, α-renaming bound variables, de Bruijn indices to avoid names entirely), yet it is Turing-complete: Church encodings represent booleans, numerals, pairs and lists as functions, and fixed-point combinators (Y, Z) give recursion without naming; evaluation strategy matters — call-by-name/normal order finds a normal form whenever one exists, call-by-value is what most languages implement, call-by-need shares work (lazy languages) — and the Church–Rosser theorem guarantees confluence (any two reduction paths reconverge, so normal forms are unique); the simply typed version is strongly normalizing (every program terminates, so it is not Turing-complete, which is the trade every type system makes), and the whole thing is the kernel that Landin, Scheme, ML, Haskell and every compiler's intermediate representation refine.
---
# The lambda calculus

**In one sentence.** Functions, and nothing else: with variables, abstraction and
application you can build numbers, data, control and recursion, which is why the
λ-calculus is both the smallest programming language and the semantics of all the others.

## Syntax and reduction (TAPL ch. 5; PFPL ch. 21)
Terms t ::= x | λx.t | t t. **Free variables** FV; **α-conversion** renames bound variables
(λx.x ≡ λy.y); **substitution** t[x := s] must be **capture-avoiding** (rename bound variables
that clash — the source of most bugs in interpreters; **de Bruijn indices** replace names with
binder distances, TAPL ch. 6; locally nameless and HOAS are the other fixes). **β-reduction**:
(λx.t) s → t[x := s]; **η**: λx.(f x) ≡ f (extensionality). A term with no β-redexes is in
**normal form**; some terms have none: Ω = (λx.x x)(λx.x x) → Ω. Currying: multi-argument
functions as nested abstractions (λx.λy.t), application left-associative.

## Programming in it (TAPL 5.2)
- **Booleans**: tru = λt.λf.t, fls = λt.λf.f; test = λl.λm.λn. l m n; and = λb.λc. b c fls.
- **Pairs**: pair = λf.λs.λb. b f s; fst = λp. p tru.
- **Church numerals**: c₀ = λs.λz.z, c₁ = λs.λz.s z, cₙ = n-fold application; succ = λn.λs.λz.
  s (n s z); plus = λm.λn.λs.λz. m s (n s z); times = λm.λn.λs. m (n s); iszero = λm. m (λx.fls)
  tru; predecessor is the famous puzzle (pairs trick — Kleene). Lists as folds (Scott/Church
  encodings — [[fold-and-structural-recursion]]).
- **Recursion** without names: the **Y combinator** Y = λf.(λx.f (x x))(λx.f (x x)) satisfies
  Y f = f (Y f) (works under call-by-name); the **Z combinator** λf.(λx.f (λv. x x v))(λx.f
  (λv. x x v)) for call-by-value. Factorial = Z (λfct.λn. if n=0 then 1 else n × fct (n−1)).
  Fixed points are the semantics of `letrec` and of recursive types
  ([[operational-and-denotational-semantics]]).
- Data + recursion + conditionals ⇒ **Turing complete** ([[turing-machines]]); combinatory
  logic (S, K — SKI) needs no variables at all; Church numerals are exponentially slower than
  binary, which is why real languages add primitives.

## Evaluation strategies (TAPL 5.1; PLAI)
Which redex next? **Full β**: any. **Normal order**: leftmost-outermost — reaches a normal
form if one exists (standardization theorem). **Call-by-name**: outermost, never inside
abstractions, arguments unevaluated (may duplicate work). **Call-by-value**: arguments to
values first (ML, Scheme, most languages; Ω as an argument diverges even if unused).
**Call-by-need**: call-by-name with sharing (thunks memoized — Haskell;
[[streams-and-lazy-evaluation]]). The choice changes which programs terminate (λx.c₁) Ω:
CBN gives c₁, CBV loops), and the equational theory (CBV needs "values" in the β rule);
Plotkin 1975 relates CBN and CBV via CPS translation ([[closures-and-environment-model]]).

## Metatheory
**Church–Rosser / confluence**: if t →* t₁ and t →* t₂ then some t₃ with t₁ →* t₃ and t₂ →* t₃
— so normal forms are unique and evaluation order can't change *which* answer, only whether
you get one. **Böhm's theorem**: distinct normal forms are observationally separable.
Reduction is undecidable to predict (halting — [[decidability-and-reductions]]); β-equivalence
is undecidable. **Simply typed λ-calculus** (Church 1940; TAPL ch. 9): types T ::= base | T → T;
every well-typed term **strongly normalizes** (Tait's method — [[type-systems]]), so it is not
Turing-complete; general recursion must be added back (fix, PCF) — the price of a
consistent logic ([[curry-howard-correspondence]]). System F adds type abstraction
([[polymorphism-and-type-inference]]).

## Why it matters in practice
Scheme/Racket, ML/OCaml, Haskell are λ-calculi with data, effects and types; compilers
use λ-calculus cores (GHC Core = System F_C; CPS and ANF — [[intermediate-representations-and-ssa]]);
closures are how λ is implemented ([[closures-and-environment-model]]); interpreters are
best written as λ evaluators (PLAI, SICP's metacircular evaluator — [[sicp]]); proof
assistants are typed λ-calculi ([[curry-howard-correspondence]]); and "lambda" in Python/Java/
C++ is the anonymous-function fragment.

## Pitfalls
- Substitution without capture avoidance (the classic interpreter bug).
- Expecting the Y combinator to work under call-by-value (use Z or letrec).
- Confusing normal form (no redexes) with weak head normal form (what lazy evaluators stop at).
- Reading "Turing complete" as "practical": Church numerals are unary.

## Related
- [[type-systems]], [[polymorphism-and-type-inference]], [[curry-howard-correspondence]],
  [[closures-and-environment-model]], [[operational-and-denotational-semantics]],
  [[turing-machines]], [[fold-and-structural-recursion]], [[streams-and-lazy-evaluation]], [[sicp]].

## Sources
Church 1936; Barendregt, *The Lambda Calculus* (1984); TAPL ch. 5–7, 9, 12; PFPL ch. 21; PLAI ch. on functions and recursion; Rojas "A Tutorial Introduction to the Lambda Calculus".

---
title: Polymorphism and type inference — System F, Hindley–Milner and Algorithm W, let-polymorphism and the value restriction, parametricity and free theorems, existential types and abstract data types, type classes and higher kinds
type: concept
section: "5.4"
level: 400
tags: [polymorphism, parametric-polymorphism, system-f, universal-types, type-abstraction, type-application, impredicative, hindley-milner, algorithm-w, unification, constraint-based-typing, principal-types, let-polymorphism, generalization, instantiation, value-restriction, parametricity, abstraction-theorem, reynolds, free-theorems, wadler, existential-types, abstract-data-types, modules, type-classes, dictionary-passing, higher-kinded-types, f-omega, rank-n, bidirectional-typing, local-type-inference, ad-hoc-polymorphism, subtype-polymorphism, generics, java-generics, rust-traits, monomorphization, erasure]
sources: [pierce-tapl-and-pl-theory-texts, pl-theory-seminal-papers]
summary: Parametric polymorphism lets one definition work at all types — System F (Girard/Reynolds) adds type abstraction ΛX.t and application t [T] with ∀X.T types, is strongly normalizing, and encodes all data types — but full System F type inference is undecidable, so ML restricts to prenex (let-) polymorphism where Hindley–Milner's Algorithm W infers principal types by unification with no annotations at all (generalize at let, instantiate at use; the value restriction keeps references sound); Reynolds' parametricity says polymorphic functions cannot inspect their type argument, so a type alone yields Wadler's "free theorems" (any r : ∀a.[a]→[a] commutes with map) and justifies representation independence; existential types ∃X.T are abstract data types and the theory of modules; type classes (Haskell) and traits (Rust) add principled ad-hoc polymorphism by dictionary passing or monomorphization, higher-kinded types (F-omega) abstract over type constructors (Functor, Monad), and modern languages blend these with subtyping via local/bidirectional inference (Scala, TypeScript, Rust) — which is why Java erases generics, Rust monomorphizes, and OCaml infers everything.
---
# Polymorphism and type inference

**In one sentence.** Write `reverse` once for every element type, let the compiler figure
out the types, and get theorems for free because the code never looked at the type.

## System F (TAPL ch. 23; PFPL ch. 16)
Terms add ΛX.t (type abstraction) and t [T] (type application); types add ∀X.T. `id = ΛX.λx:X.x
: ∀X. X → X`. **Impredicative**: X may range over all types including ∀-types. Strongly
normalizing (Girard — needs a stronger logical relation), so consistent as a logic
([[curry-howard-correspondence]]: ∀ = second-order propositional quantification). Encodes
booleans, numerals (∀X.(X→X)→X→X), products, sums, lists (Church/Böhm–Berarducci) —
inductive types without primitives ([[lambda-calculus]]). **Erasure**: types can be erased
before running (Java erases generics; but ML's `eq` and Rust's `sizeof` need them —
monomorphization). Type inference for full System F is **undecidable** (Wells 1994) —
hence annotations for rank-n types (GHC) and the restriction below. **Existential types**
∃X.T = {*S, t} — an implementation type hidden behind an interface; elimination `let {X, x} =
p in …` cannot leak X: this is the **abstract data type** / module signature
([[modularity-and-information-hiding]], [[ml-modules-and-functors]]); ∃ is encodable as
∀Y.(∀X.T→Y)→Y. **F-ω** adds type operators and kinds (* → *), giving higher-kinded
abstraction (`Functor f`, `Monad m` — [[monads]]).

## Hindley–Milner inference (Milner 1978; TAPL ch. 22)
Restrict ∀ to the outside (**prenex** polymorphism; type schemes σ = ∀ᾱ.T) and to `let`-bound
names. **Algorithm W**: walk the term generating fresh type variables and equations;
**unification** (Robinson; with occurs check — `α = α → β` fails, rejecting Ω) solves them,
yielding the **principal type** (most general; every other typing is an instance) — the
Damas–Milner theorem. `let x = e₁ in e₂`: infer e₁, **generalize** free variables not in Γ,
**instantiate** fresh at each use of x; λ-bound variables are monomorphic (why `λf. (f 1, f
true)` fails but the `let` version works). Constraint-based formulation (TAPL 22.3) separates
generation from solving; union-find makes it near-linear ([[union-find]]); nested lets can
make it exponential in pathological cases. **The value restriction** (Wright 1995): generalize
only syntactic values, else `let r = ref [] in r := [1]; head !r : bool` breaks preservation
(references + polymorphism). Extensions: **let should not be generalized** (GHC's choice with
GADTs), local assumptions, OutsideIn(X); row polymorphism for records (OCaml objects, Elm);
**bidirectional / local type inference** (Pierce & Turner) for languages with subtyping and
higher-rank types (Scala, TypeScript, Rust's inference within function bodies with mandatory
signatures at boundaries — a deliberate engineering trade for error messages and modularity).

## Parametricity (Reynolds 1983; Wadler 1989)
Polymorphic code is **uniform**: it cannot branch on the type, so it preserves all relations
between instantiations. **Abstraction theorem**: for f : ∀X.T and any relation R between
types A and B, f[A] and f[B] are related by the relational interpretation of T. **Free
theorems**: from r : ∀a. [a] → [a] alone, map g (r xs) = r (map g xs) for all g; a function
∀a. a → a must be the identity (or diverge); ∀a. a → a → a has two total inhabitants;
∀a. (a → Bool) → [a] → [a] commutes with map for fusion (the basis of deforestation and
`foldr/build` rewrite rules — [[compiler-optimizations]]). Consequences: **representation
independence** (clients of an existential can't tell two implementations apart — the formal
Parnas principle, [[modularity-and-information-hiding]]), theorems about `fold`
([[fold-and-structural-recursion]]), and the reason Haskell's `unsafeCoerce`, Java's reflection
and instanceof, and `seq` weaken the guarantee. Proved by **logical relations**, the same tool
as normalization ([[operational-and-denotational-semantics]]).

## Ad-hoc polymorphism done right: type classes and traits
`Eq a`, `Show a`, `Monad m` — overloading resolved by types (Wadler & Blott 1989): a constraint
`Eq a ⇒ a → a → Bool` compiles to **dictionary passing** (a record of methods as an implicit
argument), coherently (one instance per type); Rust **traits** are the same with
monomorphization (zero cost, code bloat) and `dyn Trait` for dictionaries at run time; Scala
implicits/givens, Swift protocols with witness tables, C++ concepts. Higher-kinded classes
(Functor/Applicative/Monad) need F-ω-style kinds — absent in Rust/Java, present in Haskell,
Scala, OCaml (via modules). Associated types, functional dependencies, and multi-parameter
classes push toward type-level programming; GADTs and type families give dependent-type
flavour ([[curry-howard-correspondence]]). Contrast **subtype polymorphism** ([[type-systems]],
[[polymorphism-and-dispatch]]) — the OO route, and the two interact badly (variance, F-bounded
quantification for `Comparable<T extends Comparable<T>>`).

## Pitfalls
- Expecting inference where subtyping or higher-rank types are involved (write signatures).
- `let`-generalizing mutable references (value restriction); monomorphism restriction
  surprises in Haskell.
- Reaching for reflection/instanceof and losing parametricity guarantees.
- Java erasure gotchas (`new T[]`, `instanceof List<String>`); Rust monomorphization bloat in
  hot generic code.

## Related
- [[type-systems]], [[lambda-calculus]], [[curry-howard-correspondence]],
  [[ml-modules-and-functors]], [[rust-traits-generics-lifetimes]], [[monads]],
  [[fold-and-structural-recursion]], [[modularity-and-information-hiding]], [[union-find]],
  [[polymorphism-and-dispatch]].

## Sources
Milner 1978; Damas & Milner 1982; Girard 1972; Reynolds 1974, 1983; Wadler 1989; Wadler & Blott 1989; Wright 1995; Pierce & Turner 2000; TAPL ch. 22–24, 26, 29–30; PFPL ch. 16–17, 48.

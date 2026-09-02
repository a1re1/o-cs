---
title: Type systems — simply typed lambda calculus, type soundness by progress and preservation, products/sums/records/references/exceptions, subtyping, recursive types, substructural and effect types, gradual typing, and what types buy in practice
type: concept
section: "5.4"
level: 400
tags: [type-systems, static-typing, dynamic-typing, simply-typed-lambda-calculus, typing-judgment, typing-rules, type-soundness, safety, progress, preservation, wright-felleisen, stuck-terms, well-typed-programs-cannot-go-wrong, product-types, sum-types, records, variants, unit, references, exceptions, recursive-types, iso-recursive, equi-recursive, subtyping, structural-subtyping, nominal, covariance, contravariance, width-depth-subtyping, top-bottom, featherweight-java, substructural-types, linear-types, affine-types, ownership, rust-borrow-checker, effect-types, effect-systems, gradual-typing, soundness-vs-completeness, type-checking-vs-inference, typescript, refinement-types, session-types, strong-normalization]
sources: [pierce-tapl-and-pl-theory-texts, pl-theory-seminal-papers]
summary: A type system is a syntactic method for proving the absence of certain behaviours by classifying phrases (Pierce), and its central theorem is soundness — Wright & Felleisen's recipe proves that well-typed programs do not get stuck by progress (a well-typed term is a value or can step) and preservation (stepping preserves the type) over a small-step semantics — starting from the simply typed λ-calculus and adding base types, products and sums (the algebraic data types), records, references (the store typing), exceptions, general recursion (fix) and recursive types (iso- vs equi-recursive, lists and trees), then subtyping (structural width/depth/function subtyping with contravariant arguments; nominal in Java; the source of covariance bugs in arrays), substructural types (linear/affine — use exactly/at most once — the theory behind Rust's ownership and borrow checker), effect types (checked exceptions, algebraic effects, Koka), and gradual typing (TypeScript, Python type hints — sound or not); the engineering trade is soundness versus completeness (every checker rejects some correct programs), and the payoff is documentation, early errors, abstraction, optimization, and the ability to state and mechanize what "cannot go wrong" means.
---
# Type systems

**In one sentence.** A type system is a tractable, syntactic proof method that certain bad
things cannot happen at run time — and the theorem that says so is proved the same way for
every language: progress plus preservation.

## The simply typed λ-calculus (TAPL ch. 8–9; PFPL ch. 4–5)
Types T ::= Bool | Nat | T₁ → T₂; typing judgment Γ ⊢ t : T with rules T-Var, T-Abs (Γ, x:T₁ ⊢
t : T₂ ⇒ Γ ⊢ λx:T₁.t : T₁ → T₂), T-App, T-If … Inversion, uniqueness of types, and
**canonical forms** (a value of type T₁ → T₂ is a λ). **Type safety = progress +
preservation** (Wright & Felleisen 1994): *progress* — a closed well-typed term is a value or
steps; *preservation* — if t : T and t → t' then t' : T; together, evaluation never reaches a
**stuck** term (the formal content of "well-typed programs cannot go wrong", Milner 1978).
Proofs by induction on typing derivations and the substitution lemma. Erasure: types don't
affect evaluation (Curry vs Church style). STLC is strongly normalizing (logical relations,
TAPL ch. 12) — so real languages add `fix` (T-Fix: (T → T) → T) and become Turing-complete
([[lambda-calculus]]).

## Extending the language (TAPL ch. 11, 13–14, 20)
| Feature | Types | Notes |
|---|---|---|
| Unit, sequencing, ascription, let | derived forms | `let` as sugar for application |
| **Products, tuples, records** | T₁ × T₂, {lᵢ : Tᵢ} | projections; structural |
| **Sums, variants** | T₁ + T₂, ⟨lᵢ : Tᵢ⟩ | case with exhaustiveness — [[algebraic-data-types]]; null as an option type |
| **Lists, general recursion** | List T; fix | |
| **References** | Ref T; store typing Σ | preservation needs Σ ⊆ Σ'; aliasing makes reasoning harder; Ref is invariant under subtyping |
| **Exceptions** | error : T; try | progress restated: value, step, or `error` |
| **Recursive types** | μX.T (lists, trees, streams) | iso-recursive (fold/unfold, ML/Haskell data) vs equi-recursive (needs coinductive subtyping); untyped λ-calculus embeds via D = μX. X → X — [[fold-and-structural-recursion]] |
| Type operators / kinds | F-ω | type-level functions; higher-kinded types (Functor, Monad — [[monads]]) |
Polymorphism (System F, HM inference) and existentials/modules are in
[[polymorphism-and-type-inference]]; dependent types in [[curry-howard-correspondence]].

## Subtyping (TAPL ch. 15–19)
S <: T — "an S can be used where a T is expected"; T-Sub (subsumption). **Structural**: record
width ({a, b} <: {a}), depth (covariant fields), permutation; **functions** are contravariant
in arguments, covariant in results (S₁ → S₂ <: T₁ → T₂ iff T₁ <: S₁ and S₂ <: T₂ — the rule
people get wrong); Top and Bottom; **references are invariant** (Java's covariant arrays are
unsound and throw ArrayStoreException at run time; variance annotations in Scala/Kotlin/C#,
`in`/`out`). **Nominal** subtyping (Java, C#: declared `extends`) vs structural (TypeScript,
Go interfaces, OCaml objects). Algorithmic subtyping needs minimal types; joins/meets for
conditionals; intersection/union types. Featherweight Java (TAPL ch. 19) is the standard
tiny model of a class-based language with soundness proved; [[liskov-substitution]] is the
behavioural version of the same idea; coercion semantics for numeric subtyping.

## Substructural and ownership types (ATTAPL ch. 1; Rust)
Ordinary contexts allow weakening, contraction, exchange; drop **contraction** and variables
are used at most once (**affine**), drop weakening too and exactly once (**linear** — Girard's
linear logic, Wadler "Linear types can change the world"). Uses: resource protocols (files
must be closed, sessions typed — **session types**), safe in-place update, and **Rust**:
ownership (affine — moved values can't be reused), borrowing (shared `&T` xor unique `&mut T`
— a lifetime-indexed capability discipline proved sound by RustBelt in Iris),
[[ownership-and-borrowing]]. Uniqueness types (Clean), regions (Tofte–Talpin, the ancestor of
lifetimes), capabilities.

## Effects, gradual and refinement types
**Effect systems** track what a computation *does* (Java checked exceptions; Koka/Eff's
algebraic effects and handlers; Haskell's IO and monads as effect types — [[monads]];
async/await as an effect — [[async-and-event-driven-concurrency]]). **Gradual typing** (Siek &
Taha 2006): a dynamic type `?` with casts at the boundary; TypeScript and Flow are
deliberately *unsound* (no runtime casts, for performance and adoption), Typed Racket is
sound with blame; mypy/Python hints are advisory; the "gradual guarantee" and the cost of
boundary checks. **Refinement types** (Liquid Haskell, F*): {v : Int | v > 0} checked by SMT
([[sat-and-smt-solvers]]) — a step toward [[program-verification]]. Type-based analyses
(nullability, ownership in C++ static analyzers, taint types — [[security-principles]]).

## In practice
Types buy: early error detection, documentation that cannot rot, **abstraction** (existential
types / module signatures hide representations — [[modularity-and-information-hiding]]),
refactoring safety, IDE tooling, and performance (unboxed representations, no dynamic checks,
[[compiler-optimizations]]). Costs: annotation burden (mitigated by inference), rejecting
correct programs (Rice — every sound static check is incomplete, [[decidability-and-reductions]]),
and complexity of advanced features. Dynamic languages implement types as run-time tags and
check late ([[bytecode-vms-and-jit]] specialize on them). The design questions: what is
checked, how expressive, how inferred, how sound — and which invariants matter for *your*
program.

## Pitfalls
- Believing "compiles ⇒ correct": types prove the absence of *specific* errors only.
- Covariant mutable containers; reference types under subtyping; `any`/casts escaping the
  guarantees.
- Adding features (subtyping + inference, references + polymorphism — the value restriction)
  without re-proving soundness.
- Confusing static typing with strong typing, or dynamic with untyped.

## Related
- [[lambda-calculus]], [[operational-and-denotational-semantics]], [[polymorphism-and-type-inference]],
  [[curry-howard-correspondence]], [[algebraic-data-types]], [[ownership-and-borrowing]],
  [[rust-traits-generics-lifetimes]], [[liskov-substitution]], [[monads]], [[program-verification]],
  [[compilers-overview]].

## Sources
TAPL ch. 8–20 (esp. 8.3, 9.3, 13, 15, 20); Wright & Felleisen 1994; PFPL ch. 4–6, 10, 20, 24–25, 34–35; SF Types/Stlc/StlcProp/Sub/References; ATTAPL ch. 1 (substructural); Siek & Taha 2006; Jung et al. "RustBelt" 2018.

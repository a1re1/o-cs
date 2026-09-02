---
title: Context-free grammars and pushdown automata — derivations and parse trees, ambiguity, Chomsky normal form, CFG ↔ PDA, the CF pumping lemma, closure and decidability, and the Chomsky hierarchy
type: concept
section: "5.1"
level: 300
tags: [context-free-grammars, cfg, productions, derivations, parse-trees, leftmost-derivation, ambiguity, inherently-ambiguous, chomsky-normal-form, pushdown-automata, pda, stack, nondeterministic-pda, deterministic-pda, cf-pumping-lemma, closure-properties, cyk, membership, emptiness, undecidable-equivalence, chomsky-hierarchy, context-sensitive, unrestricted-grammars, dyck-language, nested-structure]
sources: [sipser-and-theory-of-computation-courses, theory-of-computation-seminal-papers]
summary: Context-free grammars generate strings by rewriting variables with productions (S → aSb | ε), which captures nested, recursive structure — balanced brackets, arithmetic expressions, the syntax of programming languages — that finite automata cannot; a grammar's parse trees are the meaning-carrying structure and a grammar is ambiguous when some string has two of them (fix by rewriting precedence into the grammar, or the language is inherently ambiguous); every CFG converts to Chomsky normal form (enabling the O(n³) CYK membership algorithm), and CFGs are exactly equivalent to nondeterministic pushdown automata (a finite control plus one stack — nondeterminism matters here: deterministic PDAs recognize strictly fewer languages, the DCFLs that LR parsers handle in linear time); the CF pumping lemma (two pumpable pieces around a nested core) shows {aⁿbⁿcⁿ} is not context-free, CFLs are closed under union, concatenation and star but not intersection or complement, membership and emptiness are decidable but equivalence, ambiguity and universality are undecidable, and the whole story sits in the Chomsky hierarchy between regular and context-sensitive/Turing-recognizable languages.
---
# Context-free grammars and pushdown automata

**In one sentence.** Add one stack to a finite automaton and you can match nested things — the
brackets, blocks and expressions of every programming language — but you lose the ability to
compare two counts or to decide whether two grammars agree.

## Grammars (Sipser 2.1)
G = (V, Σ, R, S): variables, terminals, productions A → w, start symbol. **Derivation**: rewrite
step by step; **leftmost** derivations correspond one-to-one with **parse trees**; the language
is all terminal strings derivable from S. Examples: S → aSb | ε for {aⁿbⁿ}; palindromes; the
Dyck language of balanced brackets; expressions E → E + T | T, T → T × F | F, F → (E) | id
(precedence and associativity encoded by the layering). **Ambiguity**: a string with two parse
trees (E → E + E | E × E | id gives two trees for id + id × id) — a problem for compilers
because the tree is the meaning; resolved by rewriting the grammar or by precedence
declarations; some languages are **inherently ambiguous** ({aⁱbʲcᵏ : i = j or j = k}), and
ambiguity is undecidable in general. **Chomsky normal form** (A → BC | a, plus S → ε):
every CFG converts; gives the **CYK** dynamic-programming membership test in O(n³·|G|)
([[dynamic-programming]]) and bounded-depth parse trees for the pumping lemma.

## Pushdown automata (Sipser 2.2)
An NFA with a stack: transitions read an input symbol (or ε), pop a stack symbol (or ε), push a
string. Accept by final state (or empty stack — equivalent for nondeterministic PDAs).
**Theorem**: L is context-free iff some PDA recognizes it (grammar → PDA simulates leftmost
derivations on the stack; PDA → grammar with variables A_pq for "go from p to q, stack
unchanged"). Nondeterminism *matters*: **deterministic PDAs** recognize the DCFLs, a strict
subset (palindromes are CF but not DCF — you must guess the middle); DCFLs are closed under
complement, have unambiguous grammars, and are exactly what **LR(k) parsers** handle in linear
time ([[lexing-and-parsing]]) — the reason language designers keep syntax deterministic.

## Non-context-free languages (Sipser 2.3)
**CF pumping lemma**: for p (from CNF tree depth), any s ∈ L with |s| ≥ p splits as uvxyz with
|vxy| ≤ p, |vy| ≥ 1, and uvⁱxyⁱz ∈ L for all i — a long derivation repeats a variable, and
that subtree can be pumped in *two* places at once. Hence {aⁿbⁿcⁿ}, {ww}, {aⁱbʲcᵏ : i ≤ j ≤ k}
are not context-free — one stack can match one pair of counts, not two. Ogden's lemma
strengthens it. Practical consequence: type checking, declared-before-use, and matching
`#ifdef`s are not syntax — they live in semantic analysis ([[compilers-overview]]).

## Closure and decidability
Closed under union, concatenation, star, reversal, homomorphism, substitution, and
intersection with a *regular* language (product with a DFA — useful for proofs); **not**
closed under intersection ({aⁿbⁿcᵐ} ∩ {aᵐbⁿcⁿ}) or complement. Decidable: membership (CYK),
emptiness (mark generating variables), finiteness. **Undecidable**: equivalence, universality
(L = Σ*?), ambiguity, whether L is regular, intersection emptiness (all by reduction from the
Post correspondence problem — [[decidability-and-reductions]]). This gap between DFAs
(everything decidable) and CFGs is a first taste of how quickly questions become undecidable.

## The Chomsky hierarchy
| Type | Grammar | Machine | Example |
|---|---|---|---|
| 3 regular | A → aB, A → a | finite automaton | aⁿ |
| 2 context-free | A → w | (nondeterministic) PDA | aⁿbⁿ |
| 1 context-sensitive | αAβ → αγβ (non-contracting) | linear-bounded automaton | aⁿbⁿcⁿ |
| 0 unrestricted | α → β | Turing machine | any recognizable language |
Each level is strictly larger; context-sensitive languages already have a PSPACE-complete
membership problem ([[complexity-classes]]), and type 0 reaches undecidability
([[turing-machines]]). Programming languages are described by a CFG for syntax plus non-CF
constraints checked separately — and natural language, arguably, needs mildly context-
sensitive grammars.

## Pitfalls
- Writing a grammar that is ambiguous and letting the parser generator "resolve" it silently.
- Expecting a CFG (or a parser) to enforce declaration-before-use or matched type counts.
- Treating PDAs as deterministic when the language needs guessing.
- Trying to decide grammar equivalence by testing.

## Related
- [[finite-automata-and-regular-languages]], [[lexing-and-parsing]], [[turing-machines]],
  [[decidability-and-reductions]], [[complexity-classes]], [[dynamic-programming]],
  [[compilers-overview]].

## Sources
Sipser ch. 2 (18.404 L3–5); Barak ch. 10; Hopcroft, Motwani & Ullman ch. 5–7; Chomsky 1956/1959; Knuth "On the translation of languages from left to right" 1965.

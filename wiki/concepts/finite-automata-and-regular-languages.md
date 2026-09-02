---
title: Finite automata and regular languages — DFAs, NFAs, subset construction, regular expressions, closure properties, the pumping lemma, and minimization
type: concept
section: "5.1"
level: 300
tags: [finite-automata, dfa, nfa, epsilon-transitions, subset-construction, powerset-construction, regular-languages, regular-expressions, kleene-theorem, closure-properties, pumping-lemma, myhill-nerode, dfa-minimization, state-machines, lexers, pattern-matching, regular-grammars, right-linear, decision-problems, equivalence, emptiness]
sources: [sipser-and-theory-of-computation-courses, theory-of-computation-seminal-papers]
summary: A deterministic finite automaton reads input one symbol at a time with a fixed finite memory (its state) and accepts or rejects; nondeterministic automata (guessing, ε-moves) recognize exactly the same class because the subset construction converts any NFA to a DFA (with up to 2ⁿ states), and Kleene's theorem shows that class — the regular languages — is exactly what regular expressions (union, concatenation, star) describe; regular languages are closed under union, intersection, complement, reversal, homomorphism, and their decision problems (emptiness, equivalence, membership) are all decidable; the pumping lemma (any long enough string in a regular language has a middle piece that can be repeated) proves languages like {0ⁿ1ⁿ} non-regular, and Myhill–Nerode characterizes regularity by finitely many distinguishable prefixes, giving a unique minimal DFA — which is why lexers, `grep`, network protocol parsers, and hardware controllers are finite automata.
---
# Finite automata and regular languages

**In one sentence.** A machine with a fixed, finite amount of memory can recognize exactly
the patterns you can write with union, concatenation and star — no more, no counting.

## Deterministic finite automata (Sipser 1.1)
M = (Q, Σ, δ, q₀, F): finite states, alphabet, transition function δ: Q×Σ → Q, start state,
accept states. Run: apply δ per symbol; accept iff the final state ∈ F. The language L(M) is
the set of accepted strings; a language is **regular** if some DFA recognizes it. Examples:
strings with an even number of 1s (2 states); binary numbers divisible by 3 (3 states —
remainder as state); contains substring "abab" (KMP failure automaton —
[[string-algorithms]]). Design heuristic: the state is "what you must remember about the
prefix so far" — finitely many things. The same model is the hardware state machine
([[digital-logic-and-the-alu]]) and the embedded controller
([[cyber-physical-systems-and-models-of-computation]]).

## Nondeterminism and the subset construction (Sipser 1.2)
**NFA**: δ: Q×(Σ∪{ε}) → P(Q); accept if *some* computation path accepts — "guess and
verify", or equivalently the machine is in a set of states at once. **Theorem**: every NFA has
an equivalent DFA whose states are subsets of the NFA's states (**powerset construction**);
exponential blowup is sometimes unavoidable (the language "n-th symbol from the end is 1"
needs 2ⁿ DFA states, n+1 NFA states). Nondeterminism adds nothing to *power* here — unlike
for pushdown automata ([[context-free-grammars]]) and, apparently, for polynomial time
([[p-vs-np]]).

## Regular expressions and Kleene's theorem (Sipser 1.3)
Atoms a, ε, ∅; operations R₁∪R₂, R₁R₂, R*. RE → NFA by Thompson's construction (one
fragment per operator, ε-edges glue); NFA → RE by state elimination (generalized NFA) —
together **Kleene's theorem**: regular expressions = finite automata. Practical regex engines
add counted repetition, classes, anchors (still regular) and **backreferences** (not regular —
matching becomes NP-hard; backtracking engines go exponential — ReDoS; RE2/Rust regex use
automata to guarantee linear time — [[text-processing-and-regex]]). Lexers compile token
regexes into one DFA ([[lexing-and-parsing]]).

## Closure and decision properties
Regular languages are closed under union, intersection (product construction), complement
(swap accept states of a *DFA*), concatenation, star, reversal, homomorphism and inverse
homomorphism. Decidable: membership (run it), emptiness (reachability to an accept state —
[[graph-search]]), equivalence (symmetric difference empty; or minimize both), finiteness.
This is why model checkers and protocol analyzers love automata ([[model-checking]]).

## Proving non-regularity: the pumping lemma (Sipser 1.4)
If L is regular there is p (the number of states) such that every s ∈ L with |s| ≥ p splits
as s = xyz with |xy| ≤ p, |y| ≥ 1, and xyⁱz ∈ L for all i ≥ 0 (a long string must revisit a
state — pigeonhole). Contrapositive use: for {0ⁿ1ⁿ}, take s = 0ᵖ1ᵖ, y is all 0s, pumping
breaks the balance. Also non-regular: palindromes, {ww}, primes in unary, balanced parentheses
(hence parsers need a stack). The lemma is necessary, not sufficient; **Myhill–Nerode** is the
exact characterization: L is regular iff the relation "x ≡ y when for all z, xz ∈ L ⇔ yz ∈ L"
has finitely many classes — and the classes *are* the states of the minimal DFA.

## Minimization
Merge indistinguishable states: partition refinement (Moore/Hopcroft O(n log n)) from
{accepting, non-accepting} splitting on transitions; Brzozowski's reverse–determinize–
reverse–determinize. The minimal DFA is unique up to renaming — canonical form for
equivalence checking and for lexer tables.

## Beyond: what finite memory buys
Regular languages are the bottom of the Chomsky hierarchy (type 3; right-linear grammars).
Weighted/probabilistic automata (Markov chains, HMMs — [[markov-chains]]), Büchi automata on
infinite words (LTL model checking), tree automata (XML schemas), transducers (Mealy/Moore
machines — [[digital-logic-and-the-alu]]), and streaming algorithms as "automata with a little
more memory" ([[streaming-and-sketching]]).

## Pitfalls
- Using the pumping lemma to prove regularity (it can't); pumping in the wrong place.
- Complementing an NFA by swapping accept states (only valid for a complete DFA).
- Regexes with backreferences or nested quantifiers on untrusted input (ReDoS).
- Trying to count with a DFA (0ⁿ1ⁿ, balanced brackets — needs a stack).

## Related
- [[context-free-grammars]], [[turing-machines]], [[lexing-and-parsing]],
  [[text-processing-and-regex]], [[string-algorithms]], [[digital-logic-and-the-alu]],
  [[model-checking]], [[cyber-physical-systems-and-models-of-computation]].

## Sources
Sipser ch. 1 (18.404 L1–3); Barak ch. 6; Hopcroft, Motwani & Ullman ch. 2–4; Kleene 1956; Rabin & Scott 1959; Thompson 1968.

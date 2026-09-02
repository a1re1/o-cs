---
title: Induction (ordinary, strong, structural, well ordering)
type: concept
section: "1.1"
level: 200
tags: [induction, strong-induction, structural-induction, well-ordering, recursion, proofs]
sources: [mcs-lehman-leighton-meyer, hammack-book-of-proof, levin-dmoi, berkeley-cs70]
summary: Mathematical induction in its three interchangeable formats (ordinary, strong, well-ordering) plus structural induction over recursive data; how to pick the hypothesis, common mistakes, and why every recursive program is an induction proof waiting to be written.
---
# Induction

**In one sentence.** To prove P(n) for every natural number n, prove P(0) and prove that P(n) implies
P(n+1); every recursive definition (lists, trees, expressions) comes with its own induction principle.

## Why it matters
Recursion and iteration are proved correct by induction; the [[invariant-principle]] is induction
on the number of steps a program has taken. Complexity bounds for recursive algorithms
([[recurrences]]) are typically proved by "guess and verify by induction".

## The three formats are one method
| Format | Hypothesis available at step n | When it reads best |
|---|---|---|
| Ordinary induction | P(n) | when case n+1 reduces directly to case n |
| Strong induction | P(0), …, P(n) | when case n+1 uses arbitrary smaller cases (e.g. n = ab factoring, Fibonacci) |
| Well-ordering principle | "a smallest counterexample exists" | when a minimal-counterexample contradiction is natural |

MCS 5.3: any strong-induction proof can be *mechanically* rewritten as ordinary induction (strengthen
the hypothesis to ∀k ≤ n P(k)) or as a well-ordering proof. Choose the format that signals to the reader
which smaller cases you need. Structural induction is the same idea over a recursively defined set:
prove P for the base constructors and show each constructor preserves P.

## How to write one
1. State the predicate P(n) *precisely*, including its variable. ("P(n) := the sum of the first n odd
   numbers is n²", not "the formula holds").
2. Base case(s): as many as the inductive step reaches back (a step using n−1 and n−2 needs two base cases).
3. Inductive step: assume P(n) (or P(k) for all k ≤ n), prove P(n+1). Say where the hypothesis is used.
4. Conclude by the induction principle.

## Pitfalls & gotchas
- **Wrong predicate**: proving something true but not the statement wanted; or a predicate that is not
  strong enough to push through the step. Fix: *strengthen the hypothesis* (prove more so you can assume more).
  Classic: proving a sum ≤ 2 by first proving it ≤ 2 − 1/n.
- **Missing base case** for a step that reaches back several values ("all horses are the same colour"
  fails because the n = 1 → 2 step is invalid).
- **Off-by-one in the range**: P must be proved for all n ≥ b where b is the smallest value claimed.
- Structural induction over trees must cover *every* constructor; over strings, the empty string.

## Worked example (structural induction)
Define matched-bracket strings: ε is matched; if s, t matched then [s]t matched. Claim: every matched
string has equal numbers of `[` and `]`. Base: ε has 0 and 0. Step: [s]t has (1 + #[s + #[t) opens and
(1 + #]s + #]t) closes, equal by hypothesis on s and t. ∎ — this is exactly how a parser's correctness
is argued.

## Related
- [[invariant-principle]] — induction on execution steps of a state machine.
- [[recurrences]] — induction proves closed forms and asymptotic bounds.
- [[proof-techniques]] — the surrounding toolkit.
- [[sets-relations-functions]] — well ordering of N is the property that makes "smallest counterexample" work.

## Sources
MCS ch. 2 (well ordering), 5 (induction, state machines), 6 (recursive data types); Book of Proof ch. 10; Levin §2.5; CS70 Note 3.

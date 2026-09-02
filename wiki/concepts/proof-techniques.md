---
title: Proof techniques
type: concept
section: "1.1"
level: 200
tags: [proofs, logic, contrapositive, contradiction, cases, iff, counterexample]
sources: [mcs-lehman-leighton-meyer, hammack-book-of-proof, berkeley-cs70]
summary: The standard toolkit for proving a claim — direct, contrapositive, contradiction, cases, iff, existence/uniqueness, counterexample — with templates, when to reach for each, and the MCS rules for writing proofs that readers can follow.
---
# Proof techniques

**In one sentence.** A proof is a chain of implications from accepted facts to the claim, and each
technique is a *template* for arranging that chain; picking the right template is most of the work.

## Why it matters
Correctness arguments for programs (loop invariants, termination, reductions, security proofs) are
ordinary proofs wearing different clothes. The same templates appear in [[induction]], the
[[invariant-principle]], NP-completeness reductions, and amortized analysis.

## The templates
| Goal | Technique | Template |
|---|---|---|
| P ⇒ Q | **Direct** | Assume P. Derive Q. |
| P ⇒ Q | **Contrapositive** | Assume ¬Q. Derive ¬P. (Same truth table as P ⇒ Q; often far easier when Q is a negative statement like "n is odd".) |
| any P | **Contradiction** | Assume ¬P. Derive something false. Conclude P. (√2 irrational: assume n/d in lowest terms, both turn out even.) |
| P ⇔ Q | **Two implications** | Prove P ⇒ Q and Q ⇒ P separately; or chain P ⇔ R ⇔ Q. |
| P for all x | **Cases** | Partition the domain (n even/odd; x ≥ 0 / x < 0); prove each case. Say why the cases are exhaustive. |
| ∃x P(x) | **Construction** or non-constructive | Exhibit x; or show a counting/probabilistic argument forces one to exist ([[pigeonhole-principle]]). |
| ∃! x P(x) | **Existence + uniqueness** | Exhibit one; assume two, show they are equal. |
| ∀n ≥ b P(n) | **Induction** | See [[induction]]. |
| ¬∀x P(x) | **Counterexample** | One explicit x with ¬P(x) suffices; check it against the *exact* statement. |

## Rules for writing proofs (MCS ch. 1.9)
1. **State your game plan** first ("we argue by contradiction", "induction on n").
2. **Keep a linear flow**; a proof is an essay, not a calculation — use complete sentences and words over symbols.
3. **Introduce notation thoughtfully**, and define it before using it.
4. **Structure long proofs** as lemmas, exactly as long programs are broken into procedures; a repeated
   argument becomes one general lemma cited several times.
5. **Be wary of "obviously"** — never use it to bully the reader, and be suspicious when others do.
6. **Finish**: state how the established facts yield the claim; don't leave the last step implicit.

## Pitfalls & gotchas
- *Assuming what you want to prove* (circular reasoning) — usually hides in an "obviously".
- *Proving the converse* (Q ⇒ P) instead of P ⇒ Q.
- In case analysis, forgetting a case (e.g. n = 0 in "positive or negative").
- Contradiction proofs that never actually use the negated assumption are really direct proofs in
  disguise; rewrite them.
- "For all" statements are disproved by one counterexample but never proved by examples.

## Worked example (contrapositive)
Claim: if n² is even then n is even. Contrapositive: if n is odd then n² is odd. n = 2k+1 ⇒
n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, odd. ∎ (Direct proof would need to argue about factors of n²,
which is harder.)

## Related
- [[induction]] — the technique for ∀n claims and recursive structures.
- [[invariant-principle]] — induction specialised to programs/state machines.
- [[propositional-logic]] — the truth-table justification for contrapositive and contradiction.
- [[sets-relations-functions]] — proving set equalities by double inclusion.

## Sources
MCS ch. 1 (Good Proofs in Practice); Book of Proof parts II–III; CS70 Notes 1–2.

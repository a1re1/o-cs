---
title: Propositional logic and predicates
type: concept
section: "1.1"
level: 200
tags: [propositional-logic, predicates, quantifiers, truth-tables, implication, sat, boolean-algebra, cnf, dnf]
sources: [mcs-lehman-leighton-meyer, levin-dmoi, hammack-book-of-proof]
summary: Connectives, truth tables, the semantics of implication, quantifiers and their negation, equivalence laws (De Morgan, distributivity), normal forms, and why deciding satisfiability (SAT) is the central hard problem of CS.
---
# Propositional logic and predicates

**In one sentence.** Propositions are true/false; connectives (∧ ∨ ¬ ⇒ ⇔) combine them by truth
table; predicates add variables and quantifiers (∀, ∃); every proof technique is a valid pattern of
these connectives.

## Core facts to have at hand
- **Implication** P ⇒ Q is false *only* when P is true and Q false. It equals ¬P ∨ Q, its
  contrapositive ¬Q ⇒ ¬P, and is *not* its converse Q ⇒ P. Vacuous truth: false ⇒ anything.
- **Equivalence laws**: De Morgan ¬(P ∧ Q) ≡ ¬P ∨ ¬Q; ¬(P ∨ Q) ≡ ¬P ∧ ¬Q; distributivity of ∧ over ∨
  and vice versa; P ⇒ Q ≡ ¬P ∨ Q; P ⇔ Q ≡ (P ⇒ Q) ∧ (Q ⇒ P).
- **Validity vs satisfiability**: valid (tautology) = true under every assignment; satisfiable = true under
  some. ¬P is valid iff P is unsatisfiable, so validity checking and SAT are the same problem.
- **Normal forms**: every formula has an equivalent DNF (OR of ANDs) and CNF (AND of ORs); converting
  can blow up exponentially unless you introduce fresh variables (Tseitin), which preserves
  satisfiability but not equivalence.
- **Quantifier negation**: ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x). Order matters: ∀x∃y P(x,y)
  ("everyone has a mother") differs from ∃y∀x P(x,y) ("someone is everyone's mother").
- In programs, `&&`/`||` short-circuit, so `x != 0 && y/x > 1` is not commutative — logic identities
  need care with side effects and undefined values (MCS 3.2).

## SAT
Deciding whether a CNF formula is satisfiable is NP-complete (Cook–Levin, §5.1); yet modern solvers
(CDCL) handle millions of clauses, powering verification, planning and package resolution (§5.5).
Any polynomial SAT algorithm would break RSA and most of cryptography (MCS 8.12).

## Pitfalls
- Reading "P only if Q" as Q ⇒ P (it means P ⇒ Q). "P if Q" means Q ⇒ P.
- Treating ⇒ as causation; it is a truth-function.
- Dropping the domain of a quantifier: "∀x, x² ≥ 0" is true over R, false over C.

## Related
- [[proof-techniques]] — contrapositive/contradiction are these equivalences in use.
- [[sets-relations-functions]] — set-builder notation is predicates applied to sets.
- [[induction]] — the induction axiom is a second-order statement over predicates.

## Sources
MCS ch. 3; Levin ch. 3; Book of Proof ch. 2; CS70 Note 1.

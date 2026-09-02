---
title: Description Logics and Reasoning
type: concept
section: "10.4"
level: 400
tags: [description-logics, owl, reasoning, subsumption, tableau, decidability, open-world]
sources: [knowledge-representation-texts-and-papers]
summary: The decidable fragments of first-order logic underlying OWL — concepts, roles, TBox/ABox, the reasoning tasks (subsumption, consistency, instance checking), and the expressiveness/tractability trade-off.
---

# Description Logics and Reasoning
**In one sentence.** Description logics (DLs) are carefully chosen **decidable**
fragments of [[first-order-logic]] for describing classes of things and their
relationships, giving the formal semantics of OWL and enabling automated reasoning over
ontologies.

## Why it matters
DLs are the sweet spot between expressiveness and computability: rich enough to model
ontologies (biomedical SNOMED CT, gene ontologies), restricted enough that reasoning
*terminates* with guarantees full first-order logic can't offer (FOL validity is
undecidable). They are what lets a [[knowledge-graphs-and-ontologies]] reasoner infer
and check facts automatically.

## How it works
**Building blocks:**
- **Concepts** (classes/unary predicates): `Person`, `Parent`.
- **Roles** (binary relations): `hasChild`, `marriedTo`.
- **Individuals** (constants): `alice`.

**Constructors** build complex concepts: intersection (`Parent ⊓ Female`), union,
negation, and **restrictions** on roles — existential `∃hasChild.Person` ("has some
child who is a Person") and universal `∀hasChild.Female` ("all children are Female"),
plus number restrictions (`≥2 hasChild`). The naming (e.g. **ALC**, **SHOIN**,
**SROIQ** = OWL 2 DL) encodes exactly which constructors are allowed.

**Knowledge base = TBox + ABox:**
- **TBox** (terminology) — general axioms about concepts: `Mother ≡ Woman ⊓ ∃hasChild.⊤`,
  `Parent ⊑ Person` (subsumption / subclass).
- **ABox** (assertions) — facts about individuals: `Woman(alice)`, `hasChild(alice, bob)`.

**Reasoning tasks:**
- **Subsumption** — is concept A necessarily a subclass of B? (builds the classified
  hierarchy).
- **Consistency** — is the knowledge base satisfiable (no contradictions)?
- **Instance checking** — is individual x a member of concept C?
- **Classification** — compute the full subsumption hierarchy.

The standard algorithm is the **tableau** method: try to build a model; if every attempt
leads to a contradiction (a **clash**), the concept is unsatisfiable. Modern reasoners
(HermiT, Pellet, ELK) implement optimized tableaux or consequence-based methods.

**Open-world assumption.** DLs reason open-world: what is not stated is *unknown*, not
false — so a reasoner won't conclude `alice` has no other children just because none are
listed. This is the opposite of databases' closed-world negation-as-failure.

## Complexity & trade-offs
- Expressiveness trades directly against **reasoning complexity**: ALC is
  ExpTime-complete; OWL 2 DL (SROIQ) is N2ExpTime-complete in the worst case.
- The **EL** family (OWL 2 EL) restricts constructors so subsumption is **polynomial**
  — which is why huge medical ontologies (SNOMED CT) use it and classify in seconds.
  Choose the least expressive DL that models your domain.

## Pitfalls & gotchas
- **Open-world surprises** — expecting database-style "not found = false" gives wrong
  inferences; OWL won't derive negatives you didn't state.
- **No unique-name assumption** — two individuals may be inferred equal unless declared
  distinct, silently changing cardinality reasoning.
- **Expressiveness creep** — one powerful axiom can push an EL ontology into an
  intractable DL, making reasoning blow up.
- **Confusing OWL Full with OWL DL** — OWL Full is undecidable; stay in OWL 2 DL for
  guaranteed reasoning.

## Worked example
TBox: `Parent ≡ Person ⊓ ∃hasChild.Person`. ABox: `Person(alice)`,
`hasChild(alice, bob)`, `Person(bob)`. A reasoner infers `Parent(alice)` by instance
checking — a fact never asserted directly. Add `Parent ⊑ ¬Childless` and assert
`Childless(alice)`, and consistency checking reports a clash: the KB is unsatisfiable.

## Related
- [[knowledge-graphs-and-ontologies]] — DLs give OWL its semantics and inference.
- [[first-order-logic]] — DLs are decidable fragments of FOL.
- [[propositional-logic]] — the proof-theoretic backdrop.
- [[computability-and-halting-problem]] — why decidability matters (FOL is undecidable).

## Sources
Distilled from [[knowledge-representation-texts-and-papers]] (Brachman & Levesque;
Baader et al. *DL Handbook*; W3C OWL 2).

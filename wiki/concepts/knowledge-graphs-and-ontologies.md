---
title: Knowledge Graphs and Ontologies
type: concept
section: "10.4"
level: 400
tags: [knowledge-graphs, ontologies, rdf, sparql, triples, entity-linking, transe]
sources: [knowledge-representation-texts-and-papers]
summary: Representing facts as a graph of entities and relations — RDF triples, ontologies and RDFS/OWL schemas, SPARQL querying, entity linking, and knowledge-graph embeddings like TransE.
---

# Knowledge Graphs and Ontologies
**In one sentence.** A knowledge graph stores facts as a graph of **entities** connected
by typed **relations** (subject–predicate–object triples), and an **ontology** is the
schema defining the classes, relations, and constraints that give those facts meaning.

## Why it matters
Knowledge graphs back web search knowledge panels, question answering, recommendation,
biomedical databases, and increasingly the grounding for LLMs (retrieval and fact
checking). They integrate messy data from many sources under a shared vocabulary in a
way rigid relational tables struggle with. This is the applied face of
[[knowledge-representation-texts-and-papers]].

## How it works
**RDF triples.** The atomic unit is a **(subject, predicate, object)** triple, e.g.
`(Ada_Lovelace, bornIn, London)`. A set of triples is a directed labeled graph.
Entities and predicates are named by **IRIs** (global URIs) so different datasets can
refer to the same thing (**linked data**). Objects can be entities or literal values.

**Ontology / schema (RDFS, OWL).** Defines the vocabulary and its logic:
- **Classes** and **subclass** hierarchies (`Person subClassOf Agent`).
- **Properties** with **domain/range** (`bornIn` domain Person, range Place).
- **Constraints** — functional properties, disjointness, cardinality — expressed in
  **OWL**, whose formal basis is [[description-logics-and-reasoning]]. A **reasoner**
  can then *infer* new triples (if `bornIn` range is Place and X bornIn Y, then Y is a
  Place) and detect inconsistencies.

**SPARQL.** The query language for RDF: **graph-pattern matching**. You write triple
patterns with variables and the engine finds all bindings — the graph analogue of SQL:

```sparql
SELECT ?city WHERE {
  ?person  rdf:type       :Scientist .
  ?person  :bornIn        ?city .
  ?city    :country       :UK .
}
```

**Building knowledge graphs.**
- **Entity linking / resolution** — map text mentions or duplicate records to the same
  canonical entity ("NYC" = "New York City").
- **Relation/information extraction** — pull triples from text (or LLMs).
- **Knowledge-graph embeddings** — learn vectors for entities and relations to predict
  missing links. **TransE (2013)** models a relation as a translation: `h + r ≈ t`, so
  `Paris + capitalOf ≈ France`. Used for **link prediction** / KG completion; related to
  [[graph-neural-networks]].

## Complexity & trade-offs
- Triple stores are **schema-flexible** (add new relation types without migrations) and
  natural for sparse, heterogeneous, interlinked data — but SPARQL joins over billions
  of triples are costly, and they lack the maturity/optimizers of relational engines.
- Vs the [[relational-model]]: relational is best for dense, regular, transactional
  data; knowledge graphs for sparse, evolving, multi-source facts and reasoning.
- OWL reasoning is expressive but can be computationally expensive (see the DL page).

## Pitfalls & gotchas
- **Open-world assumption** — in RDF/OWL, a missing triple means *unknown*, not false
  (unlike a database's closed world). Absence of "X marriedTo Y" does not assert they
  aren't.
- **Identity/`sameAs` errors** — wrongly equating two entities corrupts inferences
  transitively.
- **Ontology sprawl** — over-modeling produces unusable, inconsistent schemas; model
  what queries need.
- **No unique-name assumption** — two IRIs may denote the same entity unless stated.

## Worked example
Combine a movies dataset and an actors dataset by aligning entities via `owl:sameAs`,
then a SPARQL query walks `?film :directedBy ?d . ?d :bornIn ?c . ?c :inContinent
:Europe` to list films by European-born directors — a join across two sources that
required no shared table schema, only shared IRIs and a small ontology.

## Related
- [[description-logics-and-reasoning]] — the logic under OWL that powers inference.
- [[relational-model]] — the database alternative; SPARQL vs SQL.
- [[graph-neural-networks]] — learning over knowledge-graph structure.
- [[large-language-models]] — KGs ground LLMs (RAG, fact checking).
- [[first-order-logic]] — the logical roots of KR.

## Sources
Distilled from [[knowledge-representation-texts-and-papers]] (W3C RDF/SPARQL/OWL;
Semantic Web for the Working Ontologist; Berners-Lee 2001; Wikidata; TransE 2013).

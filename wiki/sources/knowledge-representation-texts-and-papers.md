---
title: Knowledge Representation & Semantic Web — Texts and Papers
type: source
section: "10.4"
level: 400
tags: [knowledge-representation, semantic-web, ontologies, rdf, description-logics]
authors: Brachman & Levesque; Berners-Lee et al.; Hitzler et al.
year: 2004
institution: various; W3C
url: https://www.w3.org/standards/semanticweb/
license: mixed
format: texts+specs+papers
sources: []
summary: The knowledge-representation and semantic-web canon — Brachman & Levesque on KR&R, the W3C RDF/OWL/SPARQL specs, Semantic Web for the Working Ontologist, and the seminal papers from Berners-Lee's Semantic Web to Freebase, Wikidata, and TransE.
---

# Knowledge Representation & Semantic Web — Texts and Papers

## What it is
The field of representing facts about the world in a form machines can store, query,
and *reason* over — from logic-based knowledge representation to web-scale knowledge
graphs. It answers "how do we encode what we know so a computer can draw conclusions?"

## Key ideas
- **Knowledge graphs & ontologies** — entities, relations, and schemas as graphs
  (RDF triples); querying with SPARQL. See [[knowledge-graphs-and-ontologies]].
- **Description logics & reasoning** — the decidable logic under OWL; inference and
  consistency checking. See [[description-logics-and-reasoning]].
- **Knowledge-graph embeddings** — learning vector representations of entities and
  relations (TransE). See [[knowledge-graphs-and-ontologies]].

## Chapter / lecture map
- **Brachman & Levesque, *Knowledge Representation and Reasoning*** — the KR&R
  foundation: logic, frames, semantic networks, description logics, tractability.
- **Allemang & Hendler, *Semantic Web for the Working Ontologist*** — RDF, RDFS, OWL,
  and modeling in practice.
- **Hitzler et al., *Foundations of Semantic Web Technologies*** — the formal theory.
- **W3C specs (free): RDF, RDFS, OWL, SPARQL** — the normative standards.

## Notable claims & quotes
- **Berners-Lee, Hendler & Lassila, "The Semantic Web" (2001)** — a vision of web data
  with machine-readable meaning, enabling agents to combine information across sites.
- The **knowledge acquisition bottleneck**: hand-building large knowledge bases is the
  historic limiter, which large-scale extraction (Freebase, Wikidata) and LLMs attack.

## Seminal papers
- **Berners-Lee et al. (2001)** — the Semantic Web vision; linked data.
- **Bollacker et al., Freebase (2008)** — a large collaborative knowledge base
  (became part of Google's Knowledge Graph).
- **Vrandečić & Krötzsch, Wikidata (2014)** — the open, collaborative knowledge graph.
- **Bordes et al., TransE (2013)** — knowledge-graph embeddings by modeling relations
  as vector translations `h + r ≈ t`.

## What it adds
The symbolic, reasoning-first counterpart to statistical ML: explicit facts and logical
inference rather than learned patterns. Connects to [[first-order-logic]] and
[[propositional-logic]] (its formal basis), [[graph-neural-networks]] (learning on the
same graphs), [[large-language-models]] (RAG grounding and the "neuro-symbolic"
frontier), and [[relational-model]] (databases vs triple stores).

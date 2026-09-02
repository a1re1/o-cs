---
title: Software architecture & system design — Garlan & Shaw's "An Introduction to Software Architecture" (1994), Fielding's REST dissertation ch. 5 (2000), Lewis & Fowler's "Microservices" (2014), the system-design-primer, The Architecture of Open Source Applications (AOSA) and 500 Lines or Less, Designing Data-Intensive Applications, Bass/Clements/Kazman's Software Architecture in Practice, Richards & Ford's Fundamentals of Software Architecture, Martin's Clean Architecture, Evans' Domain-Driven Design, Hohpe & Woolf's Enterprise Integration Patterns, Kruchten's 4+1 views, Helland's "Life beyond distributed transactions"; CMU 17-655
type: source
section: "7.3"
level: 400
tags: [garlan-shaw, software-architecture, architectural-styles, fielding, rest, dissertation, lewis-fowler, microservices, system-design-primer, donnemartin, aosa, architecture-of-open-source-applications, 500-lines, ddia, kleppmann, bass-clements-kazman, software-architecture-in-practice, richards-ford, fundamentals-of-software-architecture, clean-architecture, uncle-bob, evans, domain-driven-design, ddd, hohpe-woolf, enterprise-integration-patterns, kruchten, 4-plus-1, helland, life-beyond-distributed-transactions, 17-655, cs169, atam, quality-attributes]
sources: []
authors: [David Garlan, Mary Shaw, Roy Fielding, James Lewis, Martin Fowler, Donne Martin, Amy Brown, Greg Wilson, Martin Kleppmann, Len Bass, Paul Clements, Rick Kazman, Mark Richards, Neal Ford, Robert Martin, Eric Evans, Gregor Hohpe, Bobby Woolf, Philippe Kruchten, Pat Helland]
year: 2000
institution: CMU / UC Irvine / Thoughtworks
url: https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
license: mixed (Garlan & Shaw TR, Fielding, Fowler, primer, AOSA open; books commercial)
format: html
summary: Garlan & Shaw (CMU-CS-94-166; read: abstract, contents, introduction) define the architecture level of design — "gross organization and global control structure; protocols for communication, synchronization, and data access; assignment of functionality to design elements; physical distribution; composition; scaling and performance; selection among alternatives" — catalogue the common styles (pipes and filters, data abstraction/object-oriented, event-based implicit invocation, layered systems, repositories/blackboards, table-driven interpreters, plus process control, client-server, distributed, main-program-and-subroutine, state-transition) and show through six case studies (Parnas' KWIC in four styles with a comparison table, oscilloscope instrumentation software as objects/layers/pipes, compilers as pipeline vs shared-symbol-table repository, a layered process-control system, a rule-based interpreter, Hearsay-II blackboard recast as interpreter) that choosing and mixing styles is the design decision; Fielding's chapter 5 (read: §5.1 in full — deriving REST by adding constraints to the null style: client–server for separation of concerns and independent evolution, stateless so every request carries all context (visibility, reliability, scalability at the cost of repeated data and less server control), cache with explicitly labelled cacheability (efficiency vs staleness), the uniform interface — identification of resources, manipulation through representations, self-descriptive messages, hypermedia as the engine of application state — which trades efficiency for simplicity, visibility and independent evolvability, layered system bounding what any component can see, and optional code-on-demand) is the origin of REST as an architectural style rather than an API convention; Lewis & Fowler (read: definition and the monolith contrast) characterize microservices by componentization via independently deployable services, organization around business capabilities (Conway), products not projects, smart endpoints and dumb pipes, decentralized governance and data, infrastructure automation, design for failure, evolutionary design, with the sidebars on size, SOA, and "synchronous calls considered harmful"; the system-design-primer (read: headings) is the open study guide — scalability lecture, performance vs scalability, latency vs throughput, availability vs consistency (CAP), consistency and availability patterns, DNS, CDN, load balancer, reverse proxy, application layer/microservices/service discovery, database (RDBMS, replication, federation, sharding, denormalization, SQL tuning, NoSQL key-value/document/wide-column/graph, SQL vs NoSQL), cache (client/CDN/web-server/database/application; cache-aside, write-through, write-behind, refresh-ahead), asynchronism (queues, task queues, back pressure), communication (TCP/UDP/RPC/REST), security, latency numbers every programmer should know, powers of two, and worked interview designs; AOSA (read: contents) has practitioners explain the architecture of Asterisk, Bash, Berkeley DB, CMake, Eclipse, HDFS, LLVM, Mercurial, NoSQL, Riak/OTP, Selenium, Sendmail, VTK and forty more, and 500 Lines or Less builds small versions of a web server, a template engine, a CI system, a flow-based programmer, a static analyzer, a database, and an OCR; the books supply the vocabulary — DDIA for data systems (reliability/scalability/maintainability, data models, storage engines, encoding, replication, partitioning, transactions, distributed-systems trouble, consistency and consensus, batch and stream processing, the future of data systems), Bass et al. for quality attributes, tactics and ATAM, Richards & Ford for style trade-offs and architecture characteristics ("everything is a trade-off"; "why is more important than how"), Clean Architecture for the dependency rule and hexagonal/ports-and-adapters, Evans' DDD for ubiquitous language, bounded contexts, aggregates and context maps, Hohpe & Woolf for messaging patterns, Kruchten for the 4+1 views, and Helland for why scale forces you to give up distributed transactions in favour of entities and idempotent messages.
---
# Software architecture & system design: sources

## What they are
- **Garlan & Shaw 1994** (read: abstract, ToC, §1): from programming languages to ADTs
  to architecture; styles §3.1–3.8; case studies §4.1–4.6 (KWIC four ways — the
  companion to [[parnas-1972-criteria]]); open problems §5. Shaw & Garlan's book
  *Software Architecture: Perspectives on an Emerging Discipline* (1996) expands it.
- **Fielding 2000, ch. 5** (read §5.1): null style → client–server → stateless → cache →
  uniform interface → layered → code-on-demand; §5.2 elements (resources and resource
  identifiers, representations, connectors, components), §5.3 views, §5.4 related work.
  Ch. 3 catalogues network-based styles (data-flow, replication, hierarchical, mobile
  code, peer-to-peer) and rates each on performance, scalability, simplicity,
  evolvability, extensibility, customizability, configurability, reusability,
  visibility, portability, reliability — the evaluation matrix that architecture
  decisions should be made with.
- **Lewis & Fowler 2014** (read: opening + characteristics list): microservices defined;
  sidebars — how big (two-pizza teams; Amazon's "you build it, you run it"), vs SOA,
  polyglot, "battle-tested vs enforced standards", circuit breaker, synchronous calls
  considered harmful. Fowler's later "MonolithFirst", "Microservice Premium",
  "Strangler Fig", "Modular Monolith" essays are the correctives.
- **system-design-primer** (read: headings): open study guide with Anki decks, the
  scalability lecture (Harvard CS75), the Anatomy of a System Design Interview, and
  solutions for Pastebin, Twitter timeline, web crawler, Mint, Amazon sales rank, AWS
  scaling, and key-value cache.
- **AOSA** (2011–12, two volumes; read: contents) and **500 Lines or Less** (2016) —
  architecture by example; *Software Design by Example* (Wilson) as the successor.
- **DDIA** (Kleppmann 2017; source page [[database-textbooks]]; §4 distributed/DB pages carry its content:
  [[distributed-systems-basics]], [[replication-and-partitioning]], [[consistency-models]],
  [[consistent-hashing]]); **Software Architecture in Practice** (Bass, Clements & Kazman
  4e 2021: quality attributes — availability, deployability, energy, integrability,
  modifiability, performance, safety, security, testability, usability — each with
  tactics; ATAM evaluation; documenting views); **Fundamentals of Software Architecture**
  (Richards & Ford 2020: architecture characteristics, component-based thinking, styles
  — layered, pipeline, microkernel, service-based, event-driven, space-based, SOA,
  microservices — each rated on ~12 characteristics; fitness functions; ADRs);
  **Clean Architecture** (Martin 2017: the dependency rule — source dependencies point
  inward toward policy; entities/use-cases/adapters/frameworks; screaming architecture);
  **Domain-Driven Design** (Evans 2003: ubiquitous language, entities/value objects/
  aggregates/repositories, bounded contexts, context maps, anti-corruption layer; Vernon's
  *Implementing DDD*); **Enterprise Integration Patterns** (Hohpe & Woolf 2003: message
  channel, pipes-and-filters, router, translator, endpoint; publish–subscribe, competing
  consumers, dead-letter channel, idempotent receiver); **Kruchten 1995** (4+1: logical,
  process, development, physical views + scenarios); **Helland 2007** ("Life beyond
  distributed transactions: an apostate's opinion" — at scale, entities are the unit of
  atomicity, messages between them are idempotent and at-least-once, and "almost-infinite
  scaling" forbids cross-entity transactions — the design basis of DynamoDB-style
  systems). Course: CMU 17-655 (Garlan; architectural styles, ADLs, analysis).

## Key ideas → pages
[[software-architecture-and-system-design]], [[api-design]],
[[microservices-and-resilience-patterns]], [[scalable-system-design]]; existing:
[[distributed-systems-basics]], [[replication-and-partitioning]], [[consistency-models]],
[[consistent-hashing]], [[modularity-and-information-hiding]], [[site-reliability-engineering]].

## What they add
Garlan & Shaw give the vocabulary of styles and the KWIC-four-ways proof that style
choice is a real decision; Fielding shows an architecture derived from constraints and
the properties each induces — and, read carefully, that most "REST APIs" satisfy two of
his six constraints; Lewis & Fowler define the style everyone argues about; the primer
is the interview canon; AOSA is the case-study literature every other engineering field
has and software mostly lacks.

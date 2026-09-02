---
title: Software architecture — what the architecture level of design is (Garlan & Shaw), architectural styles (pipes-and-filters, layered, object/ADT, event-based implicit invocation, repository/blackboard, interpreter, client–server, microkernel, service-based, microservices, event-driven, space-based) and their trade-offs, KWIC in four styles, quality attributes and tactics (availability, modifiability, performance, security, testability, deployability), views (4+1, C4) and architecture decision records, evaluating architecture (ATAM, fitness functions), the dependency rule and hexagonal/clean architecture, domain-driven design (ubiquitous language, bounded contexts, aggregates), monolith vs modular monolith vs microservices, and how to make architecture decisions ("everything is a trade-off")
type: concept
section: "7.3"
level: 400
tags: [software-architecture, architecture-level, garlan-shaw, architectural-styles, pipes-and-filters, layered, layered-architecture, object-oriented-organization, implicit-invocation, event-based, publish-subscribe, repository, blackboard, interpreter, client-server, microkernel, plugin-architecture, service-based, microservices, event-driven-architecture, space-based, kwic, quality-attributes, non-functional-requirements, tactics, availability, modifiability, performance, security, testability, deployability, views, 4-plus-1, kruchten, c4-model, adr, architecture-decision-records, atam, fitness-functions, evolutionary-architecture, dependency-rule, clean-architecture, hexagonal, ports-and-adapters, onion, domain-driven-design, ddd, ubiquitous-language, bounded-context, aggregates, context-map, anti-corruption-layer, monolith, modular-monolith, monolith-first, trade-offs, richards-ford, bass-clements-kazman, architect-role, conways-law]
sources: [software-architecture-texts-courses-and-seminal-papers]
summary: Software architecture is the level of design above algorithms and data structures — Garlan & Shaw's "gross organization and global control structure, protocols for communication, synchronization and data access, assignment of functionality to elements, physical distribution, composition, scaling and performance, and selection among alternatives" — and its vocabulary is architectural styles, each a set of component/connector types plus constraints that induce properties: pipes-and-filters (composable, streaming, no shared state, but batch-ish and poor for interaction), layered (each layer sees only the one below — portability and substitutability at the cost of crossing overhead and leaks), object/ADT organization (hides representations; objects must know each other's identities), event-based implicit invocation (announcers don't know who reacts — extensibility, but no control over ordering or completion), repository/blackboard (shared data store as the integration point), interpreter (a virtual machine for a domain), client–server, microkernel/plugins, service-based, event-driven, space-based and microservices — and Garlan & Shaw's KWIC example built four ways (shared data, ADTs, implicit invocation, pipes) is the demonstration that the same functionality has different change, performance, and reuse profiles under each style; architecture decisions are driven by quality attributes (availability, modifiability, performance, security, testability, deployability, usability), each with tactics catalogued by Bass, Clements & Kazman, are evaluated by scenario-based methods (ATAM) or continuously by fitness functions, are documented as views (Kruchten's 4+1: logical, process, development, physical plus scenarios; the C4 model's context/container/component/code diagrams) and as architecture decision records that capture the why; structural rules that keep an architecture from eroding include the dependency rule (dependencies point inward toward domain policy — clean/hexagonal/onion/ports-and-adapters) and domain-driven design's bounded contexts with a ubiquitous language, aggregates as consistency boundaries, and context maps with anti-corruption layers; and the perennial deployment question — monolith, modular monolith, or microservices — is answered by trade-off (start with a well-modularized monolith, extract services when team scale, independent deployability, or heterogeneous scaling needs justify the distributed-systems premium), because in architecture, as Richards & Ford put it, everything is a trade-off and the why matters more than the how.
---
# Software architecture and system design

**In one sentence.** Architecture is the set of decisions that are expensive to change —
which components exist, how they talk, where state lives, what each may know about the
others — chosen by trading quality attributes against each other under a named style,
documented as views and decision records, and defended against erosion by dependency
rules and bounded contexts.

## The architecture level of design (Garlan & Shaw 1994 — read)
"As the size of software systems increases, the algorithms and data structures of the
computation no longer constitute the major design problems." Structural issues: gross
organization and global control structure; protocols for communication, synchronization,
and data access; assignment of functionality to design elements; physical distribution;
composition of design elements; scaling and performance; selection among design
alternatives. Historically: high-level languages abstracted machine code, ADTs
([[abstract-data-types-and-rep-invariants]]) abstracted data, architecture abstracts
system organization — described with **components** (computation/data), **connectors**
(interaction), and **configurations** (their topology), constrained by a **style**. An
architecture is *what* is hard to change (Fowler: "the important stuff, whatever that
is"; Ford: "the decisions you wish you could get right early").

## Architectural styles and what each buys (Garlan & Shaw §3; Richards & Ford)
| Style | Components / connectors | Buys | Costs |
|---|---|---|---|
| **Pipes and filters** (Unix shell, compilers, ETL, streaming) | filters transform streams; pipes | composability, reuse, concurrency, easy analysis of throughput | lowest-common-denominator data format, parsing overhead, poor for interactive/stateful |
| **Layered** (OS, network stacks, n-tier apps) | layers using only the one below | portability, substitution, incremental understanding | performance of crossing layers, leaky abstractions, "sinkhole" pass-throughs |
| **Data abstraction / OO** | objects with hidden representation; method calls | information hiding, locality of change | each object must know its collaborators' identities; identity coupling |
| **Event-based / implicit invocation** (GUI frameworks, pub/sub, event buses) | announcers, subscribers; broadcast | extensibility (new listeners without changing announcers), loose coupling | announcer can't know who reacts, in what order, or when done; hard to reason about global behaviour; debugging |
| **Repository / blackboard** (databases + apps, IDEs, Hearsay-II) | central data store; knowledge sources | integration through shared data; opportunistic control | store is a bottleneck and coupling point |
| **Interpreter / virtual machine** (rule engines, DSLs) | interpretation engine, program, state | flexibility, portability | performance, extra level of indirection |
| **Client–server / n-tier** | clients, servers, request–reply | separation of concerns, independent evolution | server as bottleneck; network |
| **Microkernel / plugin** (Eclipse, browsers, VS Code) | core + plugins via extension points | extensibility, isolation | contract design, versioning of plugin APIs |
| **Service-based / microservices** | independently deployable services; network APIs, messaging | independent deployment, scaling, team autonomy | distributed-systems complexity, data consistency, ops premium ([[microservices-and-resilience-patterns]]) |
| **Event-driven** (brokers/topics, CQRS, event sourcing) | producers, brokers, consumers | decoupling, elasticity, audit log | eventual consistency, ordering, replay semantics |
| **Space-based** (in-memory data grids) | processing units + replicated in-memory data | extreme scalability for spiky loads | consistency, cost |

Real systems are **heterogeneous**: a layered system whose layers use different styles;
a pipeline whose filters are OO. **KWIC four ways** (Garlan & Shaw §4.1, after Parnas —
[[parnas-1972-criteria]], [[modularity-and-information-hiding]]): shared data (efficient,
but format change touches everything), ADTs (hides formats; adding functions — e.g. a
new "delete line" — is hard), implicit invocation (easy to add features that react to
changes; harder to control order/performance), pipes-and-filters (reuse and
concurrency; poor for interactive/incremental use) — their comparison table ranks each
on change in algorithm, change in data representation, change in function, performance,
and reuse. Fielding's ch. 3 does the same for network styles ([[api-design]] for REST).

## Quality attributes, tactics, and evaluation (Bass, Clements & Kazman; Richards & Ford)
Architecture exists to achieve **quality attributes** ("-ilities", non-functional
requirements): **availability** (tactics: detect faults — ping/heartbeat/exception;
recover — active/passive redundancy, rollback, retry, degradation; prevent — removal
from service, transactions), **modifiability** (reduce coupling: encapsulate, use an
intermediary, restrict dependencies, abstract common services; defer binding), **performance**
(manage demand: sampling, prioritizing, bounding; manage resources: concurrency,
caching, replication, scheduling — [[scalable-system-design]]), **security** (detect, resist
— authenticate/authorize/encrypt/limit exposure, react, recover — [[security-principles]]),
**testability** (control and observe state, limit complexity), **deployability**
(pipelines, feature toggles, blue/green — [[continuous-integration-and-delivery]]),
**usability**, **interoperability**, **safety**, **energy**. Attributes conflict (security vs
performance vs usability; modifiability vs performance) — the architect's job is
prioritizing. Specify them as **scenarios** (stimulus, source, environment, artefact,
response, measure: "under peak load, 99 % of searches return in < 200 ms"). **ATAM**
(architecture trade-off analysis method): stakeholders generate a utility tree of
scenarios, analyse the architecture's approach to each, surface **sensitivity points**,
**trade-off points**, and **risks**. **Fitness functions** (Ford, Parsons & Kua, *Building
Evolutionary Architectures*): automated checks of architecture characteristics in CI —
dependency rules (ArchUnit), latency budgets, coupling metrics, cyclic-dependency checks
— so the architecture is guarded continuously rather than reviewed once.

## Documenting: views and decision records (Kruchten 1995; C4; Nygard 2011)
No single diagram shows an architecture: **4+1** — **logical** (functionality:
classes/components), **process** (concurrency, communication, performance),
**development** (module organization in the repo), **physical** (deployment onto
hardware/nodes) + **scenarios** (use cases tying them together). **C4** (Brown): **context**
(system among users and other systems) → **containers** (deployable units: services, DBs,
SPAs) → **components** → **code**; each a zoom level with a consistent notation. Views
matter because different stakeholders ask different questions (ops: physical; devs:
development; product: context). **Architecture decision records** (ADRs): one short file
per decision — context, decision, status, consequences — kept in the repo; the
antidote to "why is it like this?" ([[technical-debt-and-maintenance]]). Design docs
before large changes ([[modularity-and-information-hiding]]).

## Keeping structure honest: the dependency rule and DDD (Martin 2017; Evans 2003)
**Dependency rule**: source-code dependencies point *inward* — frameworks/drivers → interface
adapters (controllers, gateways, presenters) → application use cases → enterprise
entities; the domain knows nothing of the web, the DB, or the UI. **Hexagonal / ports and
adapters** (Cockburn) and **onion** are the same idea: the application core exposes
**ports** (interfaces); **adapters** (HTTP, CLI, Postgres, in-memory fake) plug in — which
is what makes the core testable without infrastructure ([[unit-testing]] test doubles,
[[software-testing-fundamentals]]). "Screaming architecture": the top-level structure
should reveal the domain, not the framework. **Domain-driven design**: a **ubiquitous
language** shared by developers and domain experts and used in code; building blocks —
**entities** (identity), **value objects** (immutable, by value), **aggregates** (a cluster with
a root that enforces invariants; the unit of transactional consistency —
Helland's "entity" and the natural service boundary), **repositories**, **domain events**,
**services**; strategic design — **bounded contexts** (a model is valid within a boundary;
"customer" means different things to billing and to shipping), **context maps** with
relationships (shared kernel, customer–supplier, conformist, **anti-corruption layer**
translating a legacy model, open host service, published language). Bounded contexts are
the principled way to draw service boundaries and to apply Conway's law deliberately
([[software-engineering-fundamentals]] — team topologies).

## Monolith, modular monolith, or microservices? (Fowler; Richards & Ford; Newman)
A **monolith** (one deployable) is simplest to build, test, debug, and run; it fails when
teams contend on one release train, when parts need different scaling or technology, or
when its internal modularity has rotted. A **modular monolith** enforces module
boundaries in-process (packages with explicit APIs, no cross-module DB access,
ArchUnit-style checks) — most of the modularity benefit without the network.
**Microservices** buy independent deployability, team autonomy, per-service scaling and
technology, and failure isolation, at the **microservice premium**: network calls
(latency, partial failure — [[distributed-systems-basics]]), data split across services
(no joins, no cross-service transactions — sagas, eventual consistency —
[[microservices-and-resilience-patterns]]), observability and platform needs
([[site-reliability-engineering]]), versioned APIs ([[api-design]]), and the risk of a
**distributed monolith** (services that must deploy together). **Monolith first**: start
with a monolith whose module boundaries follow bounded contexts, extract services when a
boundary is stable and a concrete pressure (team scale, load, isolation) justifies it,
using the strangler fig ([[technical-debt-and-maintenance]]). The primer's interview
framing — requirements → estimates → high-level design → components → scaling — is in
[[scalable-system-design]].

## Making architecture decisions
Richards & Ford's laws: "everything in software architecture is a trade-off" (if you
think something isn't, you haven't identified the trade-off yet) and "why is more
important than how." Practice: state the quality-attribute scenarios, list two or three
candidate styles, analyse each against the scenarios (ATAM-lite), prototype the risky
part (Brooks' "plan to throw one away", the spiral's risk-driven cycle —
[[software-engineering-fundamentals]]), decide, record (ADR), and add a fitness function.
Architects stay hands-on (code, reviews), keep decisions **reversible** where possible
(interfaces, feature flags), and prefer boring technology for the parts that aren't the
product's differentiator.

## Pitfalls
- Choosing a style by fashion (microservices for a five-person team) rather than by
  quality-attribute scenarios.
- No views/ADRs — architecture that lives in one head; or diagrams without a notation
  that anyone can read.
- Layers that pass through (architecture sinkholes); dependency rule violated by "just
  this once" imports; DB shared across services.
- Ignoring Conway: an architecture the org can't own.
- Big-bang rewrites in the name of "the new architecture".

## Related
- [[api-design]], [[microservices-and-resilience-patterns]], [[scalable-system-design]],
  [[modularity-and-information-hiding]], [[parnas-1972-criteria]],
  [[software-engineering-fundamentals]], [[technical-debt-and-maintenance]],
  [[design-patterns-catalog]], [[distributed-systems-basics]], [[consistency-models]],
  [[site-reliability-engineering]], [[continuous-integration-and-delivery]],
  [[security-principles]], [[unit-testing]], [[software-testing-fundamentals]],
  [[internet-architecture-and-layering]] (the canonical layered system).

## Sources
Garlan & Shaw 1994 (read: abstract, §1, ToC); Shaw & Garlan 1996; Bass, Clements & Kazman 2021; Richards & Ford 2020; Ford, Parsons & Kua 2017; Kruchten 1995; Brown (C4); Nygard 2011 (ADRs); Martin 2017; Cockburn 2005 (hexagonal); Evans 2003; Vernon 2013; Lewis & Fowler 2014 (read); Fowler 2015 ("MonolithFirst", "Microservice Premium"); Newman 2015/2019; Helland 2007; AOSA (read: ToC).

---
title: Microservices and resilience patterns — Lewis & Fowler's characteristics (componentization via services, business capabilities, products not projects, smart endpoints and dumb pipes, decentralized governance and data, infrastructure automation, design for failure, evolutionary design), service boundaries and data ownership, synchronous vs asynchronous communication, resilience patterns (timeouts, retries with exponential backoff and jitter, circuit breaker, bulkhead, load shedding, backpressure, idempotent receivers, fallbacks), distributed data (database per service, sagas, outbox pattern, CQRS, event sourcing), messaging and enterprise integration patterns, API gateway, service discovery and service mesh, observability (tracing, correlation ids), and when not to use microservices
type: concept
section: "7.3"
level: 400
tags: [microservices, lewis-fowler, service-oriented, soa, componentization, business-capabilities, conways-law, two-pizza-teams, products-not-projects, smart-endpoints-dumb-pipes, decentralized-governance, decentralized-data, polyglot-persistence, infrastructure-automation, design-for-failure, evolutionary-design, service-boundaries, bounded-context, data-ownership, database-per-service, synchronous, asynchronous, messaging, message-queues, kafka, rabbitmq, pub-sub, resilience, timeouts, retries, exponential-backoff, jitter, retry-storms, circuit-breaker, bulkhead, load-shedding, backpressure, rate-limiting, idempotent-receiver, fallback, graceful-degradation, sagas, compensating-transactions, outbox-pattern, transactional-outbox, cqrs, event-sourcing, event-driven, enterprise-integration-patterns, hohpe-woolf, dead-letter-queue, api-gateway, backend-for-frontend, service-discovery, service-mesh, istio, envoy, sidecar, distributed-tracing, correlation-id, distributed-monolith, microservice-premium, nygard, release-it]
sources: [software-architecture-texts-courses-and-seminal-papers]
summary: Lewis & Fowler (2014) define the microservice style as building one application as a suite of small services, each in its own process, communicating by lightweight mechanisms (usually HTTP or messaging), built around business capabilities, independently deployable by automated machinery, with minimal centralized management and freedom of language and datastore — and characterize it by componentization via services (a component is independently replaceable and upgradeable; services enforce boundaries that in-process libraries let you erode), organization around business capabilities (Conway's law used deliberately: cross-functional teams own a capability end to end — "you build it, you run it"), products not projects, smart endpoints and dumb pipes (logic in services, not in an ESB; REST or a lightweight message bus), decentralized governance and data management (polyglot, one database per service, eventual consistency accepted), infrastructure automation, design for failure and evolutionary design; the price is that every call is now a network call that can fail, be slow, or be duplicated, so production-ready services apply the resilience patterns catalogued by Nygard's Release It!: timeouts on every call, retries with exponential backoff and jitter only for idempotent operations (else retry storms amplify outages), circuit breakers that fail fast when a dependency is unhealthy, bulkheads that isolate resource pools so one slow dependency can't exhaust the threads, load shedding and backpressure to protect capacity, idempotent receivers for at-least-once delivery, and fallbacks/graceful degradation; data split across services replaces distributed transactions with sagas (a sequence of local transactions with compensating actions), the transactional outbox (write the event in the same local transaction as the state change, relay it to the broker) to avoid dual-write inconsistency, CQRS (separate write model and read projections) and event sourcing (the event log is the source of truth) where audit and replay justify their complexity, all on top of the messaging vocabulary of Enterprise Integration Patterns (channels, routers, translators, dead-letter queues, competing consumers); the platform pieces are an API gateway or backend-for-frontend at the edge, service discovery, and a service mesh (Envoy sidecars, Istio) that moves timeouts, retries, mTLS and telemetry out of application code, plus distributed tracing with correlation ids because no single log tells the story; and the counsel is monolith-first — microservices pay off for organizations with many teams, independent deployment needs and heterogeneous scaling, and produce a distributed monolith everywhere else.
---
# Microservices and resilience patterns

**In one sentence.** Split an application into independently deployable services owned by
capability-aligned teams and you buy autonomy and scale at the price of turning every
function call into a network call and every transaction into a saga — so the style is
only as good as its resilience patterns, its data-ownership discipline, and its platform.

## The characteristics (Lewis & Fowler 2014 — read)
"An approach to developing a single application as a suite of small services, each
running in its own process and communicating with lightweight mechanisms, often an HTTP
resource API. These services are built around business capabilities and independently
deployable by fully automated deployment machinery." Contrast with the **monolith** (UI +
DB + one server-side executable; changes require a full rebuild/redeploy; modular
structure hard to keep; scales only as a whole). Characteristics:
- **Componentization via services** — a *component* is "independently replaceable and
  upgradeable"; **libraries** are in-process components, **services** out-of-process ones.
  Services make boundaries explicit and enforceable (you can't reach across a process
  as you can across a package — [[modularity-and-information-hiding]]); cost: remote calls
  are expensive and coarse-grained interfaces are harder to design.
- **Organized around business capabilities** — cross-functional teams (UI, storage,
  project management) per capability, invoking Conway's law deliberately; vs the
  siloed UI/middleware/DBA teams that produce layered architectures.
- **Products not projects** — the team owns the service for its lifetime ("you build
  it, you run it" — Amazon), which ties builders to users and operations
  ([[site-reliability-engineering]]).
- **Smart endpoints and dumb pipes** — logic in the services; communication via REST-ish
  HTTP or a lightweight message bus (RabbitMQ/ZeroMQ, now Kafka), not an ESB with routing,
  transformation and business rules inside the pipe (the SOA anti-pattern).
- **Decentralized governance** — polyglot languages, "battle-tested standards" (HTTP,
  protobuf) over enforced ones; tooling that makes the right thing easy.
- **Decentralized data management** — each service owns its data store (**database per
  service**), possibly different technologies (**polyglot persistence**); cross-service
  consistency is eventual and handled by compensation, not distributed transactions
  (Helland).
- **Infrastructure automation** — CI/CD, automated tests, deployment pipelines
  ([[continuous-integration-and-delivery]]) are prerequisites, not options.
- **Design for failure** — any call can fail; monitor, degrade, and test failure
  (circuit breakers; Netflix's chaos engineering).
- **Evolutionary design** — services as the unit of replacement; expect to merge and
  split them.
Sidebars: "how big?" (a team; two-pizza); microservices vs SOA (SOA's ESB-heavy,
vendor-driven history); "synchronous calls considered harmful" — chains of sync calls
multiply latency and failure probability; prefer async where possible.

## Service boundaries and data ownership
Boundaries follow **bounded contexts** and **aggregates** (DDD —
[[software-architecture-and-system-design]]): a service should own a cohesive capability,
its data, and its invariants; **nouns that change together stay together**. Signs of a
wrong cut: two services always deployed together, chatty synchronous chains, shared
database tables (the **distributed monolith** — all the costs, none of the benefits),
distributed transactions. Prefer fewer, larger services early (macro-services), split
by evidence. Each service exposes an API ([[api-design]]) and publishes **events** about
state changes; other services keep their own **read replicas/projections** of the data
they need rather than querying at request time (data duplication is the price of
autonomy — [[replication-and-partitioning]]).

## Resilience patterns (Nygard, *Release It!*; Netflix Hystrix; SRE)
Every remote call can fail, hang, or succeed twice. **Timeouts** on every call (connect
and request), propagated as **deadlines** down the call chain (gRPC deadlines) so work
is abandoned when the caller has given up. **Retries** only for **idempotent** operations
or with **idempotency keys**; **exponential backoff with jitter** (`sleep = rand(0, base·2ⁿ)`
— jitter spreads the thundering herd) and a **retry budget** (≤10 % extra load) — naive
retries at every layer turn a blip into a **retry storm** that keeps a recovering
dependency down. **Circuit breaker**: count failures per dependency; when a threshold is
crossed, **open** the circuit and fail fast (or fall back) without calling; after a
cooldown, **half-open** with trial requests; **closed** again on success — protects both
the caller's threads and the struggling dependency. **Bulkhead**: separate thread pools /
connection pools / instances per dependency or tenant so one slow dependency can't
exhaust shared resources (the ship-compartment metaphor). **Load shedding** and
**admission control**: reject excess work early (429/503) at the edge, by priority,
rather than degrading everything; **backpressure**: consumers signal producers to slow
(bounded queues, reactive streams, TCP-style flow control) instead of buffering to
death; **rate limiting** per client (token bucket). **Fallbacks / graceful degradation**:
cached/stale data, defaults, feature disabled, "reduced mode". **Idempotent receivers** +
**deduplication** for at-least-once delivery. **Health checks** (liveness vs readiness),
**fail fast** on startup misconfiguration, **steady state** (bounded logs, caches, queues),
**decoupling middleware** (async messaging breaks sync chains). Test them: fault
injection, chaos engineering (Netflix Chaos Monkey; game days —
[[site-reliability-engineering]]); a pattern you haven't exercised in production doesn't
exist. Service meshes implement timeouts/retries/breakers/mTLS uniformly (below).

## Distributed data: sagas, outbox, CQRS, event sourcing
No cross-service ACID ([[distributed-databases-and-nosql]] is available but couples
availability and is avoided at scale — Helland). **Saga**: a business transaction as a
sequence of local transactions, each publishing an event/command that triggers the
next; on failure, run **compensating transactions** in reverse (cancel reservation,
refund); **choreography** (services react to events; simple, hard to see the whole) vs
**orchestration** (a coordinator drives steps; explicit, single point of logic —
Temporal/Cadence, Step Functions); sagas are not isolated (others see intermediate
states) — design **semantic locks** and idempotent, commutative steps. **Dual-write
problem**: updating the DB then publishing to the broker can fail in between; fix with
the **transactional outbox** (insert the event into an outbox table in the same local
transaction; a relay/CDC — Debezium — publishes it; consumers deduplicate) or
**change data capture** from the DB log ([[database-recovery-and-logging]]). **CQRS**:
separate the write model (commands, aggregates, invariants) from **read models**
(denormalized projections built from events; per-screen, per-consumer); adopt only
when read/write shapes diverge — it doubles the models. **Event sourcing**: persist the
sequence of domain events as the source of truth; state = fold(events); gives audit,
temporal queries, replay into new projections; costs: event schema evolution
(upcasters), snapshots for long streams, eventual consistency of projections, and a
mental model most teams underestimate. Messaging vocabulary (**Enterprise Integration
Patterns**): message channel (point-to-point vs publish–subscribe), message router,
translator, content-based router, splitter/aggregator, **competing consumers**, **dead-letter
channel** (poison messages), message store, idempotent receiver, guaranteed delivery,
correlation identifier; brokers — Kafka (partitioned log, consumer groups, ordering
per partition, replay), RabbitMQ/AMQP (queues, routing, acks), cloud Pub/Sub, SQS —
[[mapreduce-and-dataflow]] for the processing side. Delivery semantics: at-most-once,
at-least-once (default; needs idempotency), effectively-once via dedup/transactions.

## Platform: gateway, discovery, mesh, observability
**API gateway** at the edge (auth, rate limiting, routing, TLS termination, aggregation)
and **backend-for-frontend** per client type; **service discovery** (DNS/Consul/etcd, or
the orchestrator's — Kubernetes services; client-side vs server-side load balancing —
[[scalable-system-design]]); **service mesh** (Envoy sidecar per pod + control plane
Istio/Linkerd): uniform mTLS, retries, timeouts, circuit breaking, traffic splitting
(canaries), and telemetry without touching application code — at the cost of another
layer to operate; containers and orchestration ([[containers-and-kubernetes]]).
**Observability**: **distributed tracing** (OpenTelemetry; a trace id propagated in headers
through every hop; spans show where latency and errors live), **structured logs** with
**correlation ids**, RED/USE metrics per service, SLOs per user journey
([[site-reliability-engineering]]) — the debugging of microservices *is* observability
([[debugging]]). Testing: consumer-driven contract tests, per-service tests with fakes,
few E2E ([[software-testing-fundamentals]]); **deployment**: independent pipelines,
canary/blue-green, feature flags, backward-compatible APIs and schemas (expand–migrate–
contract) because services deploy at different times.

## When not to (Fowler "Microservice Premium"; Newman)
Small team, unclear domain boundaries, no CI/CD or observability, no platform team:
the premium (network, data, ops, testing) exceeds the benefit. **Monolith first** with
enforced modules; extract when teams collide on deploys, a component needs independent
scaling or a different runtime, or failure isolation is worth the cost. Watch for the
distributed monolith, the shared database, nano-services (dozens of one-endpoint
services), and synchronous call chains > 3 deep. Some organizations (Amazon Prime
Video's 2023 case, Shopify's modular monolith) have merged services back.

## Pitfalls
- Retries without idempotency or budgets (retry storms); timeouts absent or infinite.
- Shared database across services; distributed transactions; sync chains.
- Event sourcing/CQRS adopted for fashion; event schemas without evolution plans.
- No tracing → outages debugged by guesswork across 40 services.
- Splitting before boundaries are understood; nano-services.

## Related
- [[software-architecture-and-system-design]], [[api-design]], [[scalable-system-design]],
  [[distributed-systems-basics]], [[consistency-models]], [[replication-and-partitioning]],
  [[distributed-databases-and-nosql]], [[database-recovery-and-logging]],
  [[mapreduce-and-dataflow]], [[site-reliability-engineering]], [[containers-and-kubernetes]],
  [[continuous-integration-and-delivery]], [[software-testing-fundamentals]],
  [[modularity-and-information-hiding]], [[technical-debt-and-maintenance]], [[debugging]].

## Sources
Lewis & Fowler 2014 (read); Fowler 2015 ("MonolithFirst", "Microservice Premium"); Newman 2015/2019 (*Building Microservices*, *Monolith to Microservices*); Nygard 2007/2018 (*Release It!*); Hohpe & Woolf 2003; Richardson 2018 (*Microservices Patterns*: sagas, outbox, CQRS); Helland 2007; Garcia-Molina & Salem 1987 (sagas); Vernon 2013; Basiri et al. 2016 (chaos engineering); Beyer et al. 2016 (SRE ch. 21–22, cascading failures); AWS Architecture Blog (backoff and jitter, 2015).

---
title: API design and REST — Fielding's REST constraints (client–server, stateless, cacheable, uniform interface — resource identification, representations, self-descriptive messages, HATEOAS — layered, code-on-demand) and the properties each induces, resources vs RPC, HTTP semantics (methods, safety and idempotency, status codes, caching headers, content negotiation, ETags and conditional requests), REST vs gRPC/protobuf vs GraphQL vs async/event APIs, API design rules (naming, pagination, filtering, errors, idempotency keys, rate limits), versioning and backward compatibility (Hyrum's law, additive change, deprecation), API specifications (OpenAPI, protobuf IDL, contract tests), and library API design (Bloch)
type: concept
section: "7.3"
level: 400
tags: [api-design, rest, fielding, architectural-constraints, client-server, stateless, cacheable, uniform-interface, resources, representations, self-descriptive, hateoas, hypermedia, layered-system, code-on-demand, richardson-maturity-model, rpc, grpc, protobuf, protocol-buffers, graphql, json, http-semantics, http-methods, get, post, put, patch, delete, safe-methods, idempotent, status-codes, caching-headers, cache-control, etag, conditional-requests, content-negotiation, pagination, cursor-pagination, filtering, error-format, problem-details, idempotency-keys, rate-limiting, versioning, backward-compatibility, hyrums-law, deprecation, openapi, swagger, idl, contract-testing, consumer-driven-contracts, webhooks, async-api, streaming, websockets, library-api-design, bloch, least-astonishment]
sources: [software-architecture-texts-courses-and-seminal-papers]
summary: Fielding derived REST (2000) not as an API format but as an architectural style for the Web: starting from the null style he adds constraints and names the property each induces — client–server (separation of concerns, independent evolution across organizations), stateless interaction where every request carries all context (visibility, reliability, scalability; costs repeated data and less server control over clients), explicit cacheability of responses (efficiency; costs staleness), the uniform interface (identification of resources by URI, manipulation through representations, self-descriptive messages, hypermedia as the engine of application state — simplicity, visibility and decoupled evolution at the cost of efficiency for non-hypermedia uses), layered systems in which no component sees past its neighbour (bounded complexity, intermediaries for caching, load balancing and security; costs latency), and optional code-on-demand; HTTP is REST's reference implementation, so an "API that is RESTful" means resources with stable URIs, methods with the standard semantics (GET safe and idempotent, PUT/DELETE idempotent, POST neither, PATCH partial), correct status codes, caching and conditional-request headers (ETag/If-None-Match, Cache-Control), and content negotiation — most real "REST" APIs stop at the Richardson maturity model's level 2 and skip hypermedia; the alternatives are RPC-style interfaces (gRPC over HTTP/2 with protobuf IDL, binary encoding, streaming and generated clients — best for internal service-to-service calls), GraphQL (client-specified queries over a typed schema, solving over/under-fetching for UIs at the cost of caching and server complexity), and asynchronous/event APIs (webhooks, message topics, server-sent events, WebSockets); good API design in any style means consistent naming, pagination by cursor, filtering and sorting conventions, a uniform error shape, idempotency keys for retried non-idempotent operations, rate limits with headers, and — because Hyrum's law says every observable behaviour will be depended on — versioning by additive change, explicit deprecation with timelines, and a specification (OpenAPI, protobuf) that drives documentation, generated clients, and consumer-driven contract tests; library APIs follow the same rules in miniature (Bloch: easy to use correctly, hard to use incorrectly, minimal, consistent, fail fast, documentation is part of the API).
---
# API design and REST

**In one sentence.** An API is a contract that will outlive every implementation behind
it and be depended on in every detail, so design it from constraints that induce the
properties you want (Fielding's method), follow the protocol's semantics exactly,
keep it small and consistent, and plan its evolution before the first client ships.

## REST as derived constraints (Fielding 2000 ch. 5 — read)
Design by **adding constraints** to the null style and observing the induced properties:
1. **Client–server** — separation of UI from data concerns; components evolve
   independently across organizational domains.
2. **Stateless** — "each request from client to server must contain all of the
   information necessary to understand the request, and cannot take advantage of any
   stored context on the server. Session state is therefore kept entirely on the
   client." Induces **visibility** (a monitor understands a request from the request
   alone), **reliability** (easier recovery from partial failures), **scalability** (servers
   free resources between requests); costs per-request overhead and server control over
   consistent client behaviour.
3. **Cache** — responses labelled cacheable or not; caches may reuse equivalent responses;
   improves efficiency, scalability, perceived performance; risks staleness.
4. **Uniform interface** — the defining constraint: **identification of resources** (URIs
   name resources — conceptual mappings, not files), **manipulation through
   representations** (clients hold representations plus metadata, not the resource),
   **self-descriptive messages** (each message carries enough — method, media type,
   cache directives — for any intermediary to process it), **hypermedia as the engine
   of application state** (HATEOAS — the client moves through the application by
   following links in representations, not by out-of-band knowledge of URI templates).
   Trades **efficiency** (standardized forms) for simplicity, visibility, decoupled
   evolvability; "optimizing for the common case of the Web".
5. **Layered system** — a component cannot see beyond the immediate layer; bounds
   complexity, allows intermediaries (shared caches at organizational boundaries, load
   balancers, firewalls, legacy encapsulation); costs latency. With the uniform interface
   it behaves like a uniform pipe-and-filter: intermediaries can transform content
   because messages are self-descriptive.
6. **Code-on-demand** (optional) — clients extend themselves by downloading scripts;
   simplifies clients, improves extensibility, reduces visibility — optional so the style
   works whether or not a realm supports it.
Data elements: resources, resource identifiers, representations, metadata, control data;
connectors: client, server, cache, resolver, tunnel; components: origin server, gateway,
proxy, user agent. The insight that HTTP/1.1 (which Fielding co-authored) embodies REST
is why it scaled to the planet ([[dns-http-and-the-web-stack]], [[internet-architecture-and-layering]]).

## HTTP semantics for "REST APIs" (RFC 9110; Richardson maturity model)
Level 0 = one URI, POST everything (RPC over HTTP); level 1 = **resources** with URIs
(`/orders/42`, nouns, hierarchical, plural collections); level 2 = **HTTP verbs and status
codes** with their semantics — **GET** (safe: no side effects; idempotent; cacheable),
**HEAD**, **PUT** (replace; idempotent), **DELETE** (idempotent), **POST** (create/process; neither),
**PATCH** (partial update; use JSON Merge Patch or JSON Patch); status: 200/201 (Created +
Location)/202 (Accepted, async)/204; 301/304 (Not Modified); 400 (malformed)/401
(unauthenticated)/403 (forbidden)/404/405/409 (conflict — version mismatch)/412
(precondition failed)/422 (semantic)/429 (Too Many Requests + Retry-After); 500/502/503
(+ Retry-After)/504; **caching**: `Cache-Control: max-age, private, no-store`, `ETag` +
`If-None-Match` (304 saves bandwidth), `Last-Modified`/`If-Modified-Since`, `Vary`;
**optimistic concurrency**: `If-Match: "etag"` on PUT → 412 on stale
([[transactions-and-concurrency-control]]); **content negotiation** (`Accept`,
`Content-Type`, versioned media types); level 3 = **hypermedia** (links in responses: HAL,
JSON:API, Siren) — rarely implemented; its value is decoupling clients from URI
structure. Idempotency of retries depends on this: clients and proxies may safely retry
GET/PUT/DELETE, not POST — hence **idempotency keys** (`Idempotency-Key` header stored
server-side with the first response) for payments and other POSTs
([[microservices-and-resilience-patterns]]).

## Choosing the style: REST vs gRPC vs GraphQL vs events
- **Resource/REST over JSON**: public and browser-facing APIs; cacheable, tool-friendly,
  human-readable; weak typing, chattiness for aggregated views, no streaming.
- **gRPC** (HTTP/2, **protobuf** IDL): internal
  service-to-service; binary, compact, strongly typed, generated clients in every
  language, unary/server/client/bidirectional **streaming**, deadlines and cancellation
  propagate; poor browser support (grpc-web), opaque to caches/proxies.
- **GraphQL**: one endpoint, typed schema, client specifies the shape → fixes
  over/under-fetching for UIs aggregating many resources; costs: HTTP caching lost
  (POST), N+1 resolution (DataLoader batching), query cost/depth limits, authorization
  per field; best as a **backend-for-frontend** layer over services.
- **Async / event APIs**: **webhooks** (server → client callbacks; sign payloads, retry with
  backoff, idempotent receivers), **message topics** (Kafka/Pub-Sub — schema registry;
  [[microservices-and-resilience-patterns]]), **SSE**/**WebSockets** for push
  ([[dns-http-and-the-web-stack]]); AsyncAPI spec. Long-running operations: 202 + operation
  resource to poll, or a callback.
- **Batch endpoints**, **bulk** and **field selection** (`?fields=`) as REST's answers to
  chattiness. Mixed architectures are normal: gRPC inside, REST/GraphQL at the edge via
  an API gateway.

## Design rules that survive every style
**Naming**: consistent casing, nouns for resources, no verbs in paths except for
actions modelled as sub-resources (`/orders/42/cancellation`); consistent
singular/plural; ISO 8601 timestamps in UTC; explicit units in field names
(`timeout_ms`). **Pagination**: cursor-based (`?cursor=…&limit=`; opaque, stable under
inserts, index-friendly) over offset (`?page=`; skips/duplicates under churn, O(n) in the
DB); return `next_cursor`. **Filtering/sorting**: `?status=open&sort=-created_at`;
document allowed fields. **Errors**: one machine-readable shape (RFC 9457 Problem Details:
`type`, `title`, `status`, `detail`, `instance`, plus a stable error `code`); never leak
stack traces; correlate with a request id. **Idempotency keys** for unsafe retries;
**rate limits** (429, `RateLimit-*` headers, token buckets per key — [[scalable-system-design]]);
**timeouts and deadlines** in the contract; **security**: TLS everywhere, OAuth 2/OIDC
or signed tokens, scopes, least privilege, input validation, no secrets in URLs
([[web-security]], [[security-principles]]); **observability**: request ids, structured
logs ([[site-reliability-engineering]]). **Least astonishment** and consistency beat
cleverness: an API is learned once and used a thousand times.

## Versioning, compatibility, and evolution (Hyrum's law)
Every observable behaviour — field order, error text, latency, undocumented fields —
will be depended on ([[modularity-and-information-hiding]]). Therefore: **additive change
only** (new optional fields, new endpoints; never rename, retype, or change semantics),
**tolerant readers** (ignore unknown fields — protobuf's unknown-field preservation,
JSON clients that don't fail on extras), **explicit versioning** when a break is
unavoidable (`/v2/`, `Accept: application/vnd.x.v2+json`, or a date-based version header
as Stripe does — with server-side transforms between versions), **deprecation**
(`Deprecation`/`Sunset` headers, timelines, usage metrics per consumer, migration
guides) — [[technical-debt-and-maintenance]]. **Specification first**: **OpenAPI** for HTTP
(schemas, examples, generated docs/clients/servers, request validation), **protobuf/IDL**
for gRPC (field numbers are the contract — never reuse), GraphQL SDL; **contract tests**
— consumer-driven contracts (Pact) verify that a provider still satisfies each consumer's
recorded expectations; schema linting (Spectral) and breaking-change detection (buf
breaking) in CI ([[continuous-integration-and-delivery]]). For **library APIs** (Bloch
2006): easy to use correctly and hard to use incorrectly; as small as possible (you can
add, never remove); names and parameter orders consistent; fail fast; minimize
mutability; don't expose implementation types; document every exported symbol —
"public APIs, like diamonds, are forever."

## Pitfalls
- Calling an RPC-over-POST interface "REST"; ignoring GET safety (a GET that mutates
  gets prefetched/cached into disaster).
- Offset pagination on large, changing collections; unbounded list endpoints.
- Breaking changes without a version; reusing protobuf field numbers; error formats
  that differ per endpoint.
- No idempotency for retried POSTs → duplicate charges; no timeouts in the contract.
- Chatty resource models that force N calls per screen (add aggregate endpoints or a
  BFF/GraphQL layer rather than bloating every resource).

## Related
- [[software-architecture-and-system-design]], [[microservices-and-resilience-patterns]],
  [[scalable-system-design]], [[dns-http-and-the-web-stack]], [[internet-architecture-and-layering]],
   [[modularity-and-information-hiding]],
  [[technical-debt-and-maintenance]], [[web-security]], [[security-principles]],
  [[transactions-and-concurrency-control]], [[continuous-integration-and-delivery]],
  [[site-reliability-engineering]], [[design-by-contract]].

## Sources
Fielding 2000 ch. 5 (read §5.1–5.2.1), ch. 3; Fielding & Reschke, RFC 9110 (HTTP semantics) 2022; Richardson & Ruby 2007; Fowler 2010 (Richardson maturity model); Nottingham & Wilde, RFC 9457; Google API Design Guide (AIPs); Stripe API versioning (2017 blog); Bloch 2006 ("How to design a good API and why it matters"); Winters et al. 2020 ch. 1 (Hyrum's law).

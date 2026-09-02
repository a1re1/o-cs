---
title: Web backends, sessions and authentication — the request lifecycle (router, middleware, handler, response; frameworks Express/Fastify, Django/Flask/FastAPI, Rails, Spring, Go net/http), stateless HTTP and where state lives (cookies, sessions, tokens), cookie attributes (HttpOnly, Secure, SameSite, Domain/Path), session-based vs token-based (JWT) auth and their trade-offs, password storage (bcrypt/scrypt/Argon2, salts, rate limits), OAuth 2.0 and OpenID Connect flows (authorization code + PKCE), authorization (RBAC/ABAC, per-resource checks), CSRF and CORS in one paragraph, talking to databases (ORMs, N+1, migrations, connection pools), caching and background jobs, and the full-stack shape of a typical app
type: concept
section: "7.5"
level: 300
tags: [backend, web-backend, request-lifecycle, router, middleware, handlers, controllers, express, fastify, django, flask, fastapi, rails, spring, go-net-http, mvc, stateless, cookies, set-cookie, httponly, secure, samesite, domain, path, sessions, session-store, session-id, tokens, jwt, json-web-token, bearer-token, access-token, refresh-token, token-revocation, session-vs-token, passwords, password-hashing, bcrypt, scrypt, argon2, salt, pepper, rate-limiting, mfa, totp, passkeys, webauthn, oauth2, openid-connect, oidc, authorization-code, pkce, client-credentials, implicit-flow, scopes, id-token, authorization, rbac, abac, idor, csrf, cors, same-origin-policy, orm, active-record, data-mapper, n-plus-one, migrations, connection-pool, transactions, caching, redis, background-jobs, queues, websockets, server-sent-events, file-uploads, logging, twelve-factor, full-stack]
sources: [web-development-texts-courses-and-seminal-papers]
summary: A web backend receives an HTTP request, runs it through a router and a middleware chain (logging, body parsing, auth, rate limits) to a handler that touches a database or other services and returns a response — Express, Fastify, Django, FastAPI, Rails, Spring and Go's net/http all embody this shape — and since HTTP is stateless, "who is this?" must be re-established on every request from something the client sends: a cookie (with HttpOnly so scripts can't read it, Secure so it only travels over TLS, SameSite=Lax/Strict against cross-site requests, and a tight Domain/Path) carrying a random session id that keys server-side session state — simple, instantly revocable, but requiring a session store — or a bearer token such as a JWT, a signed (not encrypted by default) JSON claim set the server verifies statelessly, which scales across services and works for non-browser clients but cannot be revoked before expiry (hence short-lived access tokens plus refresh tokens with rotation, and never storing them where XSS can read them); passwords are stored only as salted slow hashes (Argon2id, scrypt, bcrypt — never SHA-256 alone) with rate limiting, breach-list checks and MFA (TOTP, passkeys/WebAuthn as the phishing-resistant successor); delegated login and API access use OAuth 2.0 — the authorization-code flow with PKCE for browsers and mobile apps (the implicit flow is deprecated), client credentials for machine-to-machine, scopes for least privilege — and OpenID Connect adds an ID token so OAuth can also authenticate; authorization is checked per request and per resource (roles/attributes, ownership — the missing check is IDOR, the most common web vulnerability class); CSRF is why cookies need SameSite and anti-forgery tokens and CORS is how the browser's same-origin policy is deliberately relaxed for cross-origin API calls; data access goes through an ORM or query builder with awareness of N+1 queries, transactions, connection pools and versioned migrations; slow or unreliable work goes to background jobs via a queue, hot reads to a cache; and the resulting full-stack shape — static/SSR frontend, JSON or GraphQL API, auth service or library, relational DB, cache, queue, object storage — is what the courses build end to end.
---
# Web backends, sessions and authentication

**In one sentence.** Every request arrives anonymous; the backend's job is to route it,
re-establish who is asking from a cookie or token without trusting anything else, check
what they may do to this specific resource, do the work through a database and a few
services, and answer — with the auth machinery (hashing, sessions, OAuth, cookies
flags) done the boring standard way because that is the only way it is safe.

## Request lifecycle and framework shape (Full Stack Open part 3; Express/Django/Rails docs)
Listener accepts a connection → parse request → **router** matches method + path
(`GET /users/:id`) → **middleware** chain (each sees request/response and calls next:
logging/request id, body parsing (JSON, forms, multipart uploads), compression, CORS,
authentication, rate limiting, CSRF, validation) → **handler/controller** (validate
input, call services/domain logic, query DB, return status + body) → error middleware
(map exceptions to status codes; never leak stack traces) → response. Frameworks:
**Express**/Fastify/Hono/NestJS (Node — [[javascript-and-the-event-loop]]), **Django**
(batteries: ORM, admin, auth, migrations), Flask/**FastAPI** (Python; Pydantic validation,
OpenAPI for free), **Rails** (convention over configuration, Active Record), Spring Boot
(Java), Go `net/http` + chi/Gin, ASP.NET, Phoenix (Elixir). MVC/MVT: models (data +
rules), views/templates (or JSON serializers), controllers (glue). Concurrency model
matters: Node/asyncio single-threaded event loop (I/O-bound; never block), Go goroutine
per request, Java/Rails thread per request (pool sizing; async where needed)
([[processes-and-threads]]). Configuration and secrets from the environment,
logs to stdout, stateless processes so you can run N behind a load balancer
([[containers-and-kubernetes]] Twelve-Factor, [[scalable-system-design]]). Return
correct status codes and a uniform error shape ([[api-design]]).

## Where state lives: cookies (RFC 6265bis; MDN "Using HTTP cookies")
HTTP is stateless; the browser stores **cookies** the server sets (`Set-Cookie: sid=…;
HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=…`) and sends them automatically on
matching requests — which is both the mechanism of sessions and the source of CSRF.
Attributes: **HttpOnly** (invisible to `document.cookie` — protects against XSS
exfiltration), **Secure** (HTTPS only), **SameSite** (`Strict`: never sent cross-site;
`Lax` (default): sent on top-level GET navigations only; `None; Secure`: sent cross-site —
needed for third-party embeds), `Domain` (subdomains — keep narrow), `Path`, `Max-Age`/
`Expires` (session cookie if absent), `__Host-` prefix (locks Secure + no Domain + Path=/).
Cookie size ≤ 4 KB; sent on every request (keep small); third-party cookies being phased
out affects tracking, not first-party auth. Alternatives for client-held state:
`localStorage`/`sessionStorage` (readable by any script on the origin — never for
tokens), IndexedDB (app data).

## Sessions vs tokens (OWASP Session Management; JWT RFC 7519)
**Server-side sessions**: on login, create a random ≥128-bit session id, store `{id →
user, expiry, data}` in a store (in-memory for one process; **Redis**/DB for many),
set it in an HttpOnly cookie; each request looks it up. Pros: instant revocation
(logout everywhere, ban), small cookie, server controls lifetime; cons: a store to
scale and replicate, sticky or shared state across instances. Regenerate the id on
login (session fixation), idle + absolute timeouts, bind to nothing brittle.
**Token-based (JWT)**: the server issues `header.payload.signature` (base64url JSON,
signed with HMAC or RSA/ECDSA — **signed, not encrypted**: anyone can read claims), the
client sends `Authorization: Bearer <jwt>`, the server verifies the signature and claims
(`exp`, `iss`, `aud`) statelessly. Pros: no store, works across services and for mobile/
CLI clients, carries claims; cons: **cannot be revoked** before `exp` (mitigate: short-
lived **access tokens** (5–15 min) + **refresh tokens** stored server-side with rotation
and reuse detection; or a denylist — at which point you have sessions again), payload
bloat, algorithm confusion attacks (`alg: none`, RS→HS key confusion — pin the
algorithm), where to store on the web (HttpOnly cookie again; not localStorage).
Rule of thumb: browser app + one backend → cookie sessions (or cookie-carried JWT);
public API/mobile/microservices → tokens issued by an auth server, validated at the
gateway ([[microservices-and-resilience-patterns]]). Both need TLS everywhere
([[dns-http-and-the-web-stack]]).

## Passwords and MFA (OWASP Password Storage; NIST 800-63B)
Never store or log plaintext; never reversible encryption; never fast hashes (MD5/SHA-1/
SHA-256 — GPUs try billions/s). Use a **slow, salted, memory-hard KDF**: **Argon2id**
(preferred), **scrypt**, or **bcrypt** (cost ≥ 10–12); the library generates a per-user
**salt** (defeats rainbow tables and cross-user comparison); optional server-side
**pepper** in a secret store; tune cost to ~100–500 ms; upgrade hashes on login when
parameters change; constant-time comparison ([[hash-functions-cryptographic]]). Policy
(NIST): length ≥ 8 (allow 64+), no composition rules or forced rotation, check against
**breach lists** (Have I Been Pwned k-anonymity), rate-limit and lock/slow after failures,
generic "invalid credentials" (no user enumeration), password reset via single-use,
expiring tokens sent out of band. **MFA**: TOTP (RFC 6238, shared secret + time — phishable
in real time), SMS (weakest — SIM swap), push, hardware keys/**passkeys** (WebAuthn/FIDO2:
public-key challenge–response bound to the origin — phishing-resistant, no shared
secret; the direction the platforms are pushing — [[public-key-cryptography]]). Or
**don't run auth yourself**: delegate to an identity provider (Auth0/Cognito/Keycloak/
Firebase Auth) via OIDC.

## OAuth 2.0 and OpenID Connect (RFC 6749, 7636, 8252; OIDC Core)
**OAuth 2.0** is *delegated authorization*: a **resource owner** (user) lets a **client** (your
app) access a **resource server** (their Google Drive) with limited **scopes**, via an
**authorization server** that issues tokens — without sharing the password. **Authorization-
code flow with PKCE** (all public clients — SPAs, mobile — and confidential ones):
client redirects to the AS with `client_id, redirect_uri, scope, state (CSRF), code_challenge
= S256(verifier)`; user authenticates and consents; AS redirects back with a short-lived
`code`; client exchanges `code` + `code_verifier` (+ `client_secret` if confidential) at
the token endpoint for an **access token** (+ refresh token); PKCE binds the code to the
client that started the flow (defeats code interception); the **implicit flow** (token
in the URL fragment) is deprecated; **client credentials** for service-to-service;
device flow for TVs/CLIs. Validate `state`, exact `redirect_uri` matching, `aud` on
tokens; access tokens are opaque to the client (don't parse them for identity).
**OpenID Connect** layers authentication on OAuth: the `openid` scope returns an
**ID token** (a JWT with `sub`, `iss`, `aud`, `exp`, `nonce`, profile claims) that the
client verifies to learn *who* logged in ("Sign in with Google/GitHub"), plus a
`userinfo` endpoint and discovery document; SAML is the older enterprise equivalent.
Then create *your own* session for the user — OIDC ends at "this is user X".

## Authorization, CSRF, CORS (OWASP Top 10; MDN CORS)
**Authorization** is separate from authentication and must be checked on every request
for the specific resource: role-based (RBAC: `admin`, `editor`), attribute/relationship-
based (owner of the document, member of the org — ReBAC/Zanzibar), policy engines
(OPA, Casbin) or framework guards; deny by default; check **object-level** access —
`GET /invoices/123` must verify the caller may see invoice 123 (**IDOR** / broken object-
level authorization is the top API vulnerability); enforce on the server, never only
in the UI; audit-log sensitive actions. **CSRF**: because cookies auto-attach, a malicious
site can make the victim's browser POST to your app; defences — `SameSite=Lax/Strict`
cookies, **anti-CSRF tokens** (synchronizer token in forms/headers, double-submit cookie),
checking `Origin`/`Sec-Fetch-Site` headers, and never mutating state on GET. **CORS**:
the browser's **same-origin policy** blocks scripts from reading cross-origin responses;
a server opts in with `Access-Control-Allow-Origin` (specific origins, not `*` with
credentials), `-Methods`, `-Headers`, `-Credentials`; **preflight** `OPTIONS` for non-simple
requests; CORS protects users' browsers, not your API — auth still required. Full
treatment (XSS, injection, headers like CSP/HSTS) in [[web-security]] and
[[security-principles]]; input validation at the boundary always
([[design-by-contract]] distinguishes bugs from bad input).

## Data, caching, jobs, real-time (Full Stack Open parts 3–4, 13; Rails/Django guides)
**Database access**: ORMs (Active Record — Rails/Django: model = table row; Data Mapper —
Hibernate/SQLAlchemy/Prisma/Drizzle) or query builders (Knex, jOOQ) or raw parameterized
SQL (**never** string-concatenate user input — injection); the **N+1** problem (a list of
posts then a query per author — eager-load/join/batch; DataLoader for GraphQL);
**transactions** for multi-row invariants ([[transactions-and-concurrency-control]]);
indexes for every query in the hot path ([[storage-engines-and-indexes]]); **connection
pools** sized to the DB (PgBouncer; serverless functions exhaust connections);
**migrations** as versioned, reversible files run by CI, backward-compatible with running
code ([[continuous-integration-and-delivery]] expand–contract); read replicas and caching
when reads dominate ([[scalable-system-design]]). **Caching**: HTTP caching headers for
public GETs, application cache (Redis) for expensive computations/sessions/rate limits
with explicit TTL and invalidation. **Background jobs**: anything slow, retryable, or
external (email, image processing, webhooks, reports) → a queue + workers (Sidekiq,
Celery, BullMQ, SQS), idempotent, with retries and dead-letter handling; scheduled jobs
(cron). **Real-time**: **WebSockets** (bidirectional; sticky routing or a pub/sub backplane
like Redis across instances), **Server-Sent Events** (server → client stream over plain
HTTP; simpler, auto-reconnect), long polling as a fallback; push notifications via
service workers. **Files**: stream uploads to object storage (S3) with presigned URLs; never
serve user uploads from your origin without content-type/size checks. **Observability**:
request ids, structured logs, metrics, tracing ([[observability-monitoring-and-incident-response]]).
Typical full stack: CDN/static or SSR frontend ([[frontend-frameworks-and-state-management]])
→ API (REST/GraphQL — [[api-design]]) → auth (OIDC provider or framework auth) → Postgres
→ Redis → queue/workers → object storage; deployed via containers or a PaaS
([[cloud-and-serverless]]).

## Pitfalls
- Tokens in `localStorage`; cookies without HttpOnly/Secure/SameSite; JWTs as sessions
  with no revocation story; `alg` not pinned.
- Fast hashes or homemade crypto for passwords; password rules from 2005; no rate limits.
- OAuth without `state`/PKCE; wildcard redirect URIs; treating an access token as proof
  of identity.
- Authorization only in the UI; missing object-level checks (IDOR); mutating state on GET.
- String-built SQL; N+1 in every list endpoint; migrations that lock large tables;
  blocking the event loop with CPU work; synchronous email sending in the request.

## Related
- [[api-design]], [[dns-http-and-the-web-stack]], [[web-security]], [[security-principles]],
  [[javascript-and-the-event-loop]], [[frontend-frameworks-and-state-management]],
  [[hash-functions-cryptographic]], [[public-key-cryptography]],
  [[transactions-and-concurrency-control]], [[storage-engines-and-indexes]],
  [[scalable-system-design]], [[microservices-and-resilience-patterns]],
  [[continuous-integration-and-delivery]], [[containers-and-kubernetes]],
  [[cloud-and-serverless]], [[processes-and-threads]], [[design-by-contract]],
  [[observability-monitoring-and-incident-response]].

## Sources
Full Stack Open parts 3–4, 13 (read: outline); MDN: "Using HTTP cookies", "CORS", "HTTP authentication"; OWASP Cheat Sheets (Session Management, Password Storage, Authentication, CSRF, Authorization); NIST SP 800-63B (2017/2024); RFC 6265bis (cookies), RFC 7519 (JWT), RFC 8725 (JWT best practices), RFC 6749/6750 (OAuth 2.0), RFC 7636 (PKCE), RFC 8252 (native apps), OAuth 2.1 draft; OpenID Connect Core 1.0; WebAuthn L3; Express, Django, Rails, FastAPI documentation; CS50 Web (Django, users); Hoffman 2020 (*Web Application Security*).

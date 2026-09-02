---
title: DNS, HTTP/1.1–2–3, TLS, and the web stack — what happens when you load a page
type: concept
section: "4.4"
level: 300
tags: [dns, resolvers, recursive-resolution, authoritative-servers, ttl, caching, http, http-1-1, keep-alive, http-2, multiplexing, hpack, http-3, quic, tls, tls-1-3, handshake, certificates, pki, sni, cdn, caching-headers, cookies, rest, websockets, latency, head-of-line-blocking]
sources: [networking-textbooks, networking-seminal-papers]
summary: Loading a page is DNS (a hierarchical, cached, UDP-based lookup from stub resolver to recursive resolver to root, TLD and authoritative servers, with TTLs and record types A/AAAA/CNAME/MX/NS), a TCP handshake (or QUIC), a TLS 1.3 handshake (key exchange, certificate chain validated against trusted roots, SNI, 1-RTT or 0-RTT resumption), then HTTP — text request/response with headers, methods, status codes and caching (1.1 keep-alive but head-of-line blocked; HTTP/2 multiplexes binary streams with HPACK header compression over one TCP connection; HTTP/3 runs those streams over QUIC to remove TCP-level HOL blocking and speed handshakes) — usually via a CDN that terminates TLS near the user; latency, not bandwidth, is the constraint, so round trips are what engineers count.
---
# DNS, HTTP and the web stack

**In one sentence.** Every page load is a chain of round trips — name lookup, transport
handshake, crypto handshake, requests — and every protocol revision since 2010 has been about
removing round trips and head-of-line blocking.

## DNS (K&R 2.4; RFC 1034/1035)
Hierarchical namespace (`www.example.com.`); **authoritative** servers per zone; **root** (13
anycast identities) → **TLD** (`.com`) → domain's servers. A host's stub resolver asks a
**recursive resolver** (ISP, 8.8.8.8, 1.1.1.1) which iterates: root → TLD → authoritative, caching
each answer for its **TTL**. Records: A/AAAA (addresses), CNAME (alias), MX (mail), NS
(delegation), TXT (policy, verification), SRV, PTR (reverse). UDP port 53 (TCP for large/zone
transfers); DNSSEC signs records; DoH/DoT encrypt queries; DNS is the universal indirection for
load balancing, failover, CDNs (geo/anycast answers) and also a frequent outage cause.

## Transport and TLS
TCP three-way handshake (1 RTT) then **TLS 1.3** (RFC 8446): ClientHello with key shares and
**SNI** → ServerHello, certificate chain, Finished — 1 RTT (0-RTT resumption for repeat
visits, replayable); ECDHE for forward secrecy; the certificate binds the name to a public key,
signed by a CA the client trusts (PKI, Let's Encrypt/ACME automation, certificate transparency
logs); revocation via OCSP stapling; ALPN negotiates HTTP/2. QUIC folds TLS into its own 1-RTT
handshake. ([[cryptography-basics]], [[security-principles]].)

## HTTP (RFC 9110–9114)
- Request line (`GET /path HTTP/1.1`), headers, body; response status (2xx ok, 3xx redirect,
  4xx client error, 5xx server); methods with semantics (GET safe/idempotent, PUT idempotent,
  POST neither); **caching** (`Cache-Control: max-age`, `ETag`/`If-None-Match`, `Last-Modified`,
  `Vary`) — the web's biggest performance lever; cookies for state; content negotiation;
  compression (`gzip`/`br`); ranges; `Host` header for virtual hosting.
- **HTTP/1.1**: persistent connections and pipelining (rarely used); one request at a time per
  connection ⇒ browsers open 6 connections per host; **head-of-line blocking** at the
  application level.
- **HTTP/2** (2015): binary framing, many concurrent **streams** over one TCP connection,
  **HPACK** header compression, prioritization, server push (deprecated). Removes HTTP HOL
  blocking but a lost TCP segment still stalls every stream (transport HOL).
- **HTTP/3** (2022): HTTP/2's streams over **QUIC**: independent stream loss recovery, 0/1-RTT
  setup, connection migration; QPACK; now most of Google/Cloudflare traffic
  ([[tcp-reliability-and-congestion-control]]).
- REST as an architectural style (resources, representations, statelessness — Fielding);
  WebSockets for bidirectional messaging; gRPC over HTTP/2; server-sent events.

## The page load (HPBN)
DNS → TCP/QUIC → TLS → HTML → parse → discover resources → more requests (preconnect,
preload, resource hints) → render. Latency dominates: a 100 ms RTT with 3 handshakes and 20
sequential requests is seconds; hence CDNs (TLS termination and caching at the edge — anycast
and geo-DNS, [[consistent-hashing]]), connection reuse, HTTP/3, bundling/HTTP/2 push debates,
early hints, and measuring Time to First Byte and Largest Contentful Paint.

## Pitfalls
- Long DNS TTLs during migrations; negative caching; relying on DNS round-robin as a load
  balancer.
- Mis-set caching headers (either never cached or stale forever); cookies on static assets.
- Terminating TLS in the wrong place (plaintext behind the CDN); expired certificates.
- Assuming HTTP/2 fixes everything on lossy networks (it can be slower than 1.1 without QUIC).

## Related
- [[tcp-reliability-and-congestion-control]], [[internet-architecture-and-layering]],
  [[sockets-programming]], [[cryptography-basics]], [[security-principles]], [[consistent-hashing]],
  [[web-application-architecture]].

## Sources
K&R ch. 2, 8; HPBN parts I–IV; RFC 1034/1035, 9110–9114, 8446, 9000; Langley et al. 2017.

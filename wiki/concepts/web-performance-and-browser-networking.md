---
title: Web performance and browser networking — latency vs bandwidth and why latency dominates (speed of light, last mile, round trips), TCP handshake/slow start/head-of-line blocking and TLS handshake costs, HTTP/1.1 vs HTTP/2 (multiplexing, header compression, prioritization) vs HTTP/3 (QUIC), what the browser does to load a page (DNS, connect, request, parse, critical rendering path, preload scanner), the metrics that matter (Core Web Vitals: LCP, INP, CLS; TTFB, FCP), and the optimization playbook (fewer bytes and round trips, caching and CDNs, resource hints, critical CSS, defer/async and code splitting, image and font strategies, service workers and offline, measuring in the field with RUM vs lab)
type: concept
section: "7.5"
level: 300
tags: [web-performance, browser-networking, hpbn, latency, bandwidth, speed-of-light, propagation-delay, last-mile, round-trips, rtt, tcp-handshake, slow-start, congestion-window, initial-cwnd, bandwidth-delay-product, head-of-line-blocking, tls-handshake, tls-1-3, session-resumption, 0-rtt, ocsp-stapling, hsts, http1, keep-alive, domain-sharding, http2, multiplexing, streams, hpack, server-push, prioritization, http3, quic, connection-migration, page-load, dns-lookup, preconnect, dns-prefetch, preload, prefetch, priority-hints, critical-rendering-path, render-blocking, parser-blocking, preload-scanner, defer, async, modules, core-web-vitals, lcp, inp, cls, fid, ttfb, fcp, tti, tbt, lighthouse, rum, real-user-monitoring, lab-vs-field, caching, cache-control, immutable, etag, cdn, edge, compression, gzip, brotli, minification, bundling, code-splitting, tree-shaking, lazy-loading, images, avif, webp, srcset, lazy-loading-images, fonts, font-display, subsetting, service-workers, pwa, offline, cache-api, performance-budget, third-party-scripts, resource-hints]
sources: [web-development-texts-courses-and-seminal-papers]
summary: Web performance is mostly a latency problem, not a bandwidth one — the speed of light puts a floor of tens of milliseconds on a round trip, the last mile adds more, and above ~5 Mbps extra bandwidth barely improves page load while every extra round trip (DNS, TCP's three-way handshake, TLS's handshake, then slow start ramping the congestion window from ~10 packets) costs a full RTT — so the playbook is fewer round trips and fewer bytes on the critical path; HTTP/1.1 could only pipeline poorly, so browsers opened six connections per host and developers sharded domains and concatenated files, HTTP/2 fixed this with multiplexed streams over one connection, HPACK header compression and prioritization (and made those old hacks harmful) but still suffers TCP head-of-line blocking when a packet is lost, and HTTP/3 over QUIC (UDP, TLS 1.3 built in, independent streams, 0-RTT resumption, connection migration) removes that too; loading a page means DNS → connect → TLS → request → HTML streams in → the preload scanner discovers resources while the parser builds the DOM → CSS blocks rendering and synchronous scripts block parsing → render tree, layout, paint → hydration and interaction, and the user-centric measures of this are the Core Web Vitals: Largest Contentful Paint (loading, ≤2.5 s), Interaction to Next Paint (responsiveness, ≤200 ms, replacing First Input Delay) and Cumulative Layout Shift (stability, ≤0.1), plus TTFB and FCP as diagnostics; the techniques are caching with long max-age and hashed immutable filenames and a CDN at the edge, Brotli compression and minification, resource hints (preconnect, preload, prefetch, priority hints), inlined critical CSS and non-blocking loading of the rest, defer/async/module scripts with code splitting and tree shaking so the initial bundle is small, responsive modern-format images with explicit dimensions and lazy loading below the fold, font subsetting with font-display, keeping the main thread free of long tasks and third-party scripts on a budget, and service workers for offline and instant repeat visits — all verified by measuring in the field (RUM, CrUX) because lab tools (Lighthouse, WebPageTest) only predict.
---
# Web performance and browser networking

**In one sentence.** Pages are slow because of round trips and main-thread work, not
megabytes: cut the round trips (connections, redirects, chained requests), cut the bytes
on the critical path, cache everything that can be cached at the edge, keep the main
thread free, and measure what real users see.

## Why is my site slow on mobile but fine on my laptop? Latency, bandwidth, and why latency wins (HPBN ch. 1 — ToC read)
"Speed is a feature": +100 ms latency costs Amazon ~1 % sales; 400 ms delay cut Google
searches 0.6 %. **Latency** components: propagation (speed of light in fibre ≈ 200 000
km/s → NY–London ≈ 28 ms one way, ≥ 56 ms RTT; a transatlantic RTT can't go below that),
transmission (bytes / link rate), processing (routers), queuing (buffers, bufferbloat);
**last mile** (DSL/cable/wireless access) often adds 10–40 ms; mobile radio (RRC state
transitions, HPBN ch. 7) adds hundreds of ms after idle. **Bandwidth** helps only up
to a point: Belshe's experiment — going from 5 to 10 Mbps improves page load ~5 %, while
halving RTT improves it nearly linearly, because a page load is a series of dependent
round trips. Hence: count RTTs on the critical path, not kilobytes
([[tail-latency-at-scale]] for server-side tails).

## TCP, TLS, and the connection cost (HPBN ch. 2, 4)
**TCP** three-way handshake: 1 RTT before data; **slow start**: congestion window begins
at ~10 segments (~14 KB) and doubles per RTT — a 100 KB response needs ~4 RTTs of
ramp-up on a fresh connection, so **reuse connections** (keep-alive) and keep the
first response small; **flow control** (receive window), **congestion control**
(CUBIC/BBR — [[tcp-reliability-and-congestion-control]]); **bandwidth-delay product**
limits throughput per connection; **head-of-line blocking**: a lost packet stalls
everything behind it on that connection. Tuning: larger initial cwnd, window scaling,
TCP Fast Open, no slow-start-after-idle. **TLS** ([[cryptography-basics]]): TLS 1.2 adds
2 RTTs, **TLS 1.3** 1 RTT, **0-RTT** on resumption (replay caveats); costs: certificate
chain size (send only intermediates, use ECDSA), **OCSP stapling** (avoid a client-side
revocation lookup), **session resumption** (tickets), **ALPN** to negotiate h2/h3 in the
handshake, **SNI**; **HSTS** to skip the HTTP→HTTPS redirect (a whole RTT + insecure
request); certificate automation (ACME/Let's Encrypt). On a mobile network a cold
HTTPS request can cost 4–6 RTTs ≈ 300–600 ms before the first byte of HTML.

## HTTP/1.1 → HTTP/2 → HTTP/3 (HPBN ch. 9–12; RFC 9113/9114)
**HTTP/1.1**: one request in flight per connection (pipelining unusable in practice);
browsers open **6 connections per host**; workarounds — domain sharding, sprite sheets,
concatenated bundles, inlining — each with costs. **HTTP/2** (2015, from SPDY): binary
framing, **multiplexing** many streams over one TCP connection (no more 6-connection
limit or bundling for concurrency), **HPACK** header compression (cookies/headers repeated
per request were a real cost), stream **prioritization** (dependencies/weights, replaced
by simpler priority hints in practice), server push (deprecated — use preload/103 Early
Hints); requires TLS in browsers; the old hacks become anti-patterns (sharding defeats
one connection; giant bundles hurt caching). Remaining problem: TCP-level head-of-line
blocking — one lost packet stalls all streams. **HTTP/3** (2022) over **QUIC** (UDP; TLS 1.3
integrated → 1-RTT or 0-RTT setup; streams independently retransmitted; **connection
migration** across IP changes — WiFi to cellular; user-space congestion control;
QPACK); ~30 % of web traffic; enable via `Alt-Svc`/HTTPS DNS records. WebSocket (single
long-lived bidirectional connection; HPBN ch. 17), Server-Sent Events, WebRTC (P2P
UDP media/data; STUN/TURN/ICE for NAT traversal — HPBN ch. 3, 18);
[[dns-http-and-the-web-stack]] for the protocol details.

## What happens when a page loads (MDN "Critical rendering path" — read; HPBN ch. 10)
DNS lookup (cached, or ~20–120 ms) → TCP + TLS → request → **TTFB** (server think time +
1 RTT) → HTML streams in; the parser builds the DOM incrementally while the **preload
scanner** races ahead to discover `<link>`, `<script>`, `<img>` and start fetches;
**CSS is render-blocking** (CSSOM must be complete to compute styles — but not
parser-blocking), **synchronous `<script>` is parser-blocking** and waits for pending CSS;
`defer` (execute after parse, in order) / `async` (execute when loaded) / `type=module`
(deferred by default) unblock the parser; DOM + CSSOM → render tree → **layout** → **paint**
→ composite ([[html-css-and-the-dom]]); then JS runs, frameworks **hydrate**
([[frontend-frameworks-and-state-management]]), data fetches fire (waterfalls when
discovered late), fonts swap in, images decode. Critical path = the chain of resources
needed for first render: minimize their **number**, **bytes**, and **length** (depth of
dependent requests). **Metrics**: **Core Web Vitals** — **LCP** (largest contentful paint ≤
2.5 s at p75: hero image/text render time), **INP** (interaction to next paint ≤ 200 ms:
worst-case input responsiveness across the visit; replaced **FID** in 2024), **CLS**
(cumulative layout shift ≤ 0.1: unexpected movement — images without dimensions, late
fonts/ads/injected banners); diagnostics — **TTFB** (≤ 800 ms), **FCP**, **TBT** (total
blocking time: long tasks > 50 ms on the main thread), TTI; **Lab vs field**: Lighthouse/
WebPageTest simulate a device and network (reproducible, diagnostic); **RUM** (web-vitals
library, CrUX, analytics) measures real users (what ranking and users actually
experience — p75 across devices, geographies) — optimize the field numbers, debug in the
lab. Set a **performance budget** (e.g., ≤ 170 kB compressed JS on the critical path,
LCP ≤ 2 s on a mid-range Android over 4G) and enforce in CI
([[continuous-integration-and-delivery]]).

## The optimization playbook (HPBN ch. 13; web.dev)
- **Cache**: `Cache-Control: max-age=31536000, immutable` on hashed static assets;
  short/`no-cache` + `ETag` on HTML/API; `stale-while-revalidate`; a **CDN** at the edge
  for static and cacheable dynamic responses (cuts RTT to tens of ms, terminates TLS
  near the user) — [[scalable-system-design]]; avoid redirects (each is an RTT, and
  `http://` → `https://` → `www` chains are common).
- **Bytes**: **Brotli**/gzip for text; minify; **tree-shake** and **code-split** by route/
  component (dynamic `import()`), ship modern syntax to modern browsers (`module/nomodule`
  or browserslist), audit bundle (source-map-explorer), replace heavy dependencies
  (moment → date-fns/Intl; lodash → per-method); defer non-critical JS; keep third-party
  scripts (tags, chat, ads) on a budget and load them late/async — they are the usual LCP/
  INP killers.
- **Round trips and discovery**: `<link rel=preconnect>` to critical third-party origins,
  `dns-prefetch`, **`preload`** for late-discovered critical resources (hero image, fonts,
  CSS-referenced assets), `fetchpriority=high` on the LCP image, `prefetch` for likely
  next-page resources, 103 Early Hints; avoid request waterfalls (fetch data in parallel;
  SSR the first data; don't chain `@import` in CSS).
- **CSS/JS placement**: inline **critical CSS** for above-the-fold, load the rest non-
  blocking (`media=print onload` trick or `rel=preload as=style`); scripts at the end or
  `defer`; avoid layout-affecting JS before first paint; **font-display: swap/optional**,
  self-host and **subset** fonts (WOFF2), preload the one critical font, `size-adjust` to
  limit CLS.
- **Images/media**: modern formats (**AVIF**/WebP), responsive `srcset`/`sizes`, explicit
  `width/height` or `aspect-ratio` (CLS), `loading=lazy` below the fold (never on the LCP
  image), `decoding=async`, compress (quality ~75–80), image CDN transforms, video with
  `preload=metadata` and posters.
- **Main thread**: break long tasks (`scheduler.yield`, `requestIdleCallback`), move CPU
  work to workers, debounce input handlers, virtualize long lists, avoid layout
  thrashing, minimize hydration (islands/RSC) — INP is a main-thread problem
  ([[javascript-and-the-event-loop]]).
- **Offline and repeat visits**: **service worker** with the Cache API (precache the app
  shell, runtime-cache with strategies: cache-first for assets, network-first/stale-
  while-revalidate for data), background sync, push; a **PWA** manifest for install;
  beware stale-cache bugs and update flows (Workbox).
- **Server**: TTFB — fast backends, edge rendering, streaming HTML (flush the head early),
  HTTP/2/3 enabled, TLS 1.3, OCSP stapling, HSTS, Early Hints, compression at the CDN.
- **Mobile** (HPBN ch. 8): batch network activity, avoid periodic polling (radio wake-ups
  drain battery), design for variable and intermittent connectivity
  ([[mobile-development-and-cross-platform]]).

## Pitfalls
- Optimizing bandwidth-side (bigger images "look fine on WiFi") while ignoring RTTs and
  redirects; testing only on a MacBook on fibre.
- HTTP/1.1 hacks under HTTP/2 (sharding, mega-bundles); disabling caching "to be safe";
  cache-busting via query strings without immutable headers.
- Lazy-loading the hero image; fonts that block text for 3 s; images without dimensions.
- One giant JS bundle hydrating a static page; third-party tags loaded synchronously in
  `<head>`.
- Trusting a Lighthouse score over field p75; no performance budget in CI.

## Related
- [[dns-http-and-the-web-stack]], [[tcp-reliability-and-congestion-control]],
  [[html-css-and-the-dom]], [[javascript-and-the-event-loop]],
  [[frontend-frameworks-and-state-management]], [[scalable-system-design]] (CDN, caching),
  [[tail-latency-at-scale]], [[cryptography-basics]] (TLS), [[caches-and-memory-hierarchy]]
  (the same principle one level down), [[continuous-integration-and-delivery]],
  [[mobile-development-and-cross-platform]], [[profiling-and-performance]].

## Sources
Grigorik 2013, *High Performance Browser Networking* (ToC read) ch. 1–4, 7–13, 15–18; MDN "Critical rendering path" (read), "HTTP caching", "Resource hints"; web.dev Core Web Vitals (Walton 2020; INP 2024); RFC 9110–9114, RFC 9000 (QUIC); Belshe 2010 ("More bandwidth doesn't matter (much)"); Osmani 2018–23 (cost of JavaScript); Souders 2007 (*High Performance Web Sites*); Google, "Speed matters" 2009; Full Stack Open part 0 (read: outline).

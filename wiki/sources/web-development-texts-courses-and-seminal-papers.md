---
title: Web development & full-stack — MDN Web Docs (free; HTTP overview and critical rendering path read), Haverbeke's Eloquent JavaScript (4e 2024, free), Simpson's You Don't Know JS, Grigorik's High Performance Browser Networking (free; ToC read), Full Stack Open (Helsinki, free; parts read), Harvard CS50 Web, The Odin Project, freeCodeCamp, MIT Web.lab; Berners-Lee's "Information Management: A Proposal" (1989), Fielding's REST (2000), Garrett's "Ajax" (2005), Crockford's JSON, React's architecture (2013–), the WHATWG/W3C HTML, DOM, CSS and Fetch specs
type: source
section: "7.5"
level: 200
tags: [mdn, mdn-web-docs, eloquent-javascript, haverbeke, you-dont-know-js, simpson, hpbn, high-performance-browser-networking, grigorik, full-stack-open, helsinki, luukkainen, cs50-web, odin-project, freecodecamp, web-lab, berners-lee, information-management, www, fielding, rest, garrett, ajax, crockford, json, react, facebook, whatwg, w3c, html-living-standard, dom-spec, css-spec, fetch-spec, web-platform]
sources: []
authors: [Marijn Haverbeke, Kyle Simpson, Ilya Grigorik, Matti Luukkainen, Tim Berners-Lee, Roy Fielding, Jesse James Garrett, Douglas Crockford, Jordan Walke]
year: 2024
institution: Mozilla / University of Helsinki / O'Reilly / CERN
url: https://developer.mozilla.org/
license: CC BY-SA (MDN); CC BY-NC (Eloquent JS, HPBN, FSO)
format: html
summary: MDN Web Docs is the reference for the web platform (HTML elements and attributes, CSS properties/selectors/layout, JavaScript language and built-ins, Web APIs — DOM, Fetch, service workers, workers, storage — plus HTTP, accessibility, performance, security and privacy guides and the "Learn web development" curriculum; the HTTP overview read here: client–server, user agents, proxies, stateless-but-not-sessionless via cookies, extensible headers, what HTTP controls — caching, origin relaxation via CORS, authentication, proxies, sessions — the request/response flow and message anatomy; the critical-rendering-path guide read here: bytes → tokens → DOM, CSSOM, render tree, layout, paint, render-blocking CSS and parser-blocking scripts, measure with Performance APIs, optimize by minimizing critical resources, bytes and path length); Eloquent JavaScript (contents read: values/types, program structure, functions, objects and arrays, higher-order functions, the secret life of objects, bugs and errors, regular expressions, modules, asynchronous programming, a programming-language project; the browser part — DOM, events, canvas, HTTP and forms; Node.js) teaches the language as a language; You Don't Know JS goes deep on scope/closures, `this`/prototypes, types/coercion, async; High Performance Browser Networking (ToC read: latency and bandwidth primer — speed of light, last mile; TCP — handshake, slow start, congestion, bandwidth-delay product, head-of-line blocking, tuning; UDP and NAT traversal (STUN/TURN/ICE); TLS — handshake, forward secrecy, ALPN/SNI, resumption, chain of trust, OCSP stapling, optimization checklist incl. HSTS; wireless/WiFi/mobile networks and the RRC state machine; then HTTP/1.x, HTTP/2, browser networking and APIs — XHR, SSE, WebSocket, WebRTC) is the networking-for-web-developers text; Full Stack Open (parts read: fundamentals of web apps, React, communicating with server, Node/Express, testing, React Router, advanced state management, custom hooks, GraphQL, TypeScript, React Native, CI/CD, containers, relational databases, Next.js) is the free full course; and the seminal items are Berners-Lee's 1989 proposal (hypertext over the internet, the URL/HTTP/HTML trio), Fielding's REST, Garrett's naming of Ajax (asynchronous XMLHttpRequest updates making the page an application), Crockford's JSON (a JavaScript-literal subset as the lingua franca that displaced XML), React's declarative components and virtual-DOM reconciliation, and the living standards that define the platform.
---
# Web development: sources

## What they are
- **MDN Web Docs** (Mozilla, now Open Web Docs; CC BY-SA): references for HTML, CSS,
  JavaScript, Web APIs, HTTP; guides (box model, flexbox/grid, responsive images,
  animations, performance, accessibility, security, PWAs); "Learn web development"
  modules and the MDN Curriculum. Read: *Overview of HTTP*, *Critical rendering path*.
- **Eloquent JavaScript** (Haverbeke, 4e 2024; contents read): Part 1 Language (ch. 1–12:
  values, program structure, functions, data structures, higher-order functions, objects,
  a robot project, bugs and errors, regular expressions, modules, asynchronous
  programming, a programming-language project), Part 2 Browser (ch. 13–19: JS and the
  browser, DOM, events, a platform game, canvas, HTTP and forms, a pixel-art editor),
  Part 3 Node (ch. 20–21: Node.js, a skill-sharing website). Interactive sandbox.
- **You Don't Know JS (Yet)** (Simpson; free on GitHub): Get Started; Scope & Closures;
  Objects & Classes (`this`, prototypes); Types & Grammar (coercion); Sync & Async; ES.Next.
- **High Performance Browser Networking** (Grigorik 2013; free; ToC read): Networking
  101 (latency/bandwidth, TCP, UDP, TLS); wireless (WiFi, mobile, RRC); HTTP (history,
  HTTP/1.x, HTTP/2, optimizing delivery); browser APIs (primer on browser networking,
  XHR, SSE, WebSocket, WebRTC). Complement: the HTTP/3 & QUIC material in
  [[dns-http-and-the-web-stack]].
- **Full Stack Open** (Helsinki; CC BY-NC-SA; parts read): React SPA + Node/Express REST
  + MongoDB, then testing, state management, GraphQL, TypeScript, React Native, CI/CD,
  containers, relational DBs, Next.js — a full curriculum with exercises.
- **Courses**: CS50 Web (Django, JS, React, testing, scalability, security); The Odin
  Project (foundations → full-stack JS/Ruby); freeCodeCamp certifications; MIT Web.lab
  (6.148, IAP).
- **Seminal**: Berners-Lee 1989 ("Information Management: A Proposal" — the "vague but
  exciting" memo; linked information system for CERN; 1990–91 WorldWideWeb, HTTP, HTML,
  URLs); Fielding 2000 ([[api-design]]); Garrett 2005 ("Ajax: A New Approach to Web
  Applications" — standards-based presentation, DOM, XML/XSLT, XMLHttpRequest, JS
  binding it; Gmail/Maps as exemplars); Crockford 2001–06 (JSON, RFC 8259; "the
  fat-free alternative to XML"); React (Walke 2013; Facebook's declarative UI, virtual
  DOM diffing, unidirectional data flow — later hooks 2019, concurrent rendering, server
  components); WHATWG HTML Living Standard, DOM Standard, Fetch Standard; W3C CSS specs
  and WAI-ARIA/WCAG.

## Key ideas → pages
[[html-css-and-the-dom]], [[javascript-and-the-event-loop]],
[[frontend-frameworks-and-state-management]], [[web-backends-sessions-and-authentication]],
[[web-performance-and-browser-networking]]; existing: [[dns-http-and-the-web-stack]],
[[api-design]], [[higher-order-functions]].

## What they add
MDN is the ground truth for the platform; Eloquent JS is the best free language text in
any language; HPBN explains why the page is slow at every layer below JavaScript; Full
Stack Open is the free path from zero to deployed full-stack app; the seminal items
show the Web as a series of deliberately simple decisions (URL/HTTP/HTML, REST, JSON,
Ajax, declarative components) each of which won by being the least clever option.

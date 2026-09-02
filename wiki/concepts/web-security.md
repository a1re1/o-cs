---
title: Web security — the browser security model (origins, the same-origin policy and what it does and doesn't cover, CORS as controlled relaxation), injection attacks (SQL injection and parameterized queries, command/LDAP/NoSQL injection, SSRF), cross-site scripting (stored/reflected/DOM XSS, output encoding by context, Content Security Policy, trusted types), cross-site request forgery (SameSite cookies, tokens, the confused-deputy framing), clickjacking and UI redressing, authentication and session attacks (fixation, hijacking, credential stuffing), access-control flaws (IDOR/BOLA, path traversal), TLS in practice and mixed content, security headers (CSP, HSTS, X-Frame-Options, referrer/permissions policy), the OWASP Top 10, and secure defaults for building web apps
type: concept
section: "8.1"
level: 300
tags: [web-security, browser-security-model, origin, same-origin-policy, sop, cors, cross-origin, injection, sql-injection, sqli, parameterized-queries, prepared-statements, command-injection, ldap-injection, nosql-injection, ssrf, server-side-request-forgery, xss, cross-site-scripting, stored-xss, reflected-xss, dom-xss, output-encoding, contextual-encoding, content-security-policy, csp, trusted-types, csrf, cross-site-request-forgery, samesite, csrf-token, double-submit, confused-deputy, clickjacking, ui-redressing, x-frame-options, frame-ancestors, session-fixation, session-hijacking, credential-stuffing, mfa, idor, bola, broken-access-control, path-traversal, directory-traversal, open-redirect, tls, https, hsts, mixed-content, secure-cookies, httponly, security-headers, referrer-policy, permissions-policy, subresource-integrity, sri, owasp-top-10, secure-defaults, portswigger]
sources: [computer-security-texts-courses-and-seminal-papers]
summary: Web security starts from the browser's model: content is grouped by origin (scheme + host + port), and the same-origin policy stops a script on one origin from reading another origin's responses, cookies, or DOM — while deliberately allowing cross-origin writes (form posts, image/script loads), which is exactly why the two archetypal web attacks exist; CORS relaxes reading with server opt-in headers. Injection (OWASP A03) happens whenever untrusted input is interpreted as code: SQL injection is fixed not by escaping but by parameterized queries/prepared statements that keep data out of the query's structure (plus least-privilege DB accounts and ORMs used safely), and the same discipline covers command, LDAP, XPath and NoSQL injection and template injection; SSRF (A10) tricks the server into making requests to internal targets (cloud metadata endpoints), mitigated by allowlists and blocking link-local addresses. Cross-site scripting injects attacker script into a page so it runs with the victim's origin — stored, reflected, and DOM-based — and is stopped by contextual output encoding (HTML, attribute, JS, URL contexts each need their own), a strict Content Security Policy (nonces/hashes, no unsafe-inline) and Trusted Types for the DOM sinks, plus HttpOnly cookies so stolen script can't read the session. Cross-site request forgery abuses the browser's automatic cookie attachment to make the victim's browser perform state-changing requests (the confused deputy), defeated by SameSite=Lax/Strict cookies, anti-CSRF tokens, and checking Origin. Beyond these: clickjacking (framed UI — frame-ancestors/X-Frame-Options), broken access control and IDOR/BOLA (the top risk — enforce object-level authorization server-side on every request), path traversal and open redirects, authentication and session flaws (fixation, hijacking, credential stuffing — regenerate ids, HttpOnly+Secure cookies, MFA), and transport (TLS everywhere, HSTS, no mixed content, SRI for third-party scripts). The OWASP Top 10 is the shared checklist and PortSwigger's Web Security Academy the hands-on canon; the winning move is secure-by-default frameworks (auto-escaping templates, ORM parameterization, CSRF tokens, secure cookie flags) plus defense in depth.
---
# Web security

**In one sentence.** The browser lets any site cause your browser to *send* requests to
any other but not to *read* the responses (the same-origin policy), and almost every web
vulnerability is either that asymmetry abused (CSRF, clickjacking), untrusted input
interpreted as code (injection, XSS), or an authorization check the server forgot
(IDOR) — so the fixes are structural: keep data out of code, encode by context, lock the
policy down, and check every access.

## The browser security model (CS161 ch. 18–19; 6.858 L13 — read)
The web runs untrusted code (any page's JS) in your browser next to your logged-in
sessions, so isolation is everything. **Origin** = (scheme, host, port); the **same-origin
policy (SOP)** is the baseline: script from origin A may **not read** origin B's DOM,
responses (fetch/XHR), cookies, or storage; it **may**, however, cause cross-origin
**writes/sends** — navigate to B, submit a form to B, load `<img>/<script>/<link>` from B,
and those requests **carry B's cookies**. That "send but not read" split is deliberate
(embedding, links) and is the root of CSRF and clickjacking. What SOP does *not* isolate
by default: it's per-origin, not per-site, and Spectre showed in-process origin
separation is insufficient → **site isolation** puts sites in separate processes
([[access-control-and-isolation]]). **CORS** relaxes cross-origin *reading* with server
opt-in: the browser sends `Origin`, the server answers `Access-Control-Allow-Origin`
(specific origin, not `*` with credentials), `-Methods`, `-Headers`, `-Credentials`;
non-simple requests get a **preflight** `OPTIONS`. CORS protects the *user's* data in
their browser; it is not server-side access control ([[web-backends-sessions-and-authentication]]).
Cookies have their own scoping (domain/path, not port) and flags (HttpOnly, Secure,
SameSite). `postMessage`, `iframe` sandboxing, and COOP/COEP/CORP (cross-origin
isolation for SharedArrayBuffer) round out the model.

## Injection: keep data out of code (OWASP A03; CS161 ch. 17)
Any time untrusted input is concatenated into something an interpreter parses, the input
can change the *structure*, not just the data. **SQL injection**: `"SELECT * FROM users
WHERE name='" + input + "'"` with input `' OR '1'='1' --` returns everything; `'; DROP
TABLE...` destroys. The fix is **not escaping** but **parameterized queries / prepared
statements**: the query structure is fixed and the input is bound as a value the parser
never treats as SQL (`db.query("... WHERE name = ?", [input])`); ORMs do this by default
(but raw fragments and dynamic column/table names reintroduce it — allowlist those);
plus **least-privilege DB accounts** (the OKWS lesson — [[access-control-and-isolation]])
and stored-procedure care. Same pattern for **command injection** (never build shell
strings — use `execve`-style arg arrays, no shell), **LDAP/XPath/NoSQL injection**
(Mongo `$where`, operator injection), **template injection** (SSTI → RCE), **XML external
entities** (disable DTDs), **header/CRLF injection**, and log injection. **SSRF** (A10):
the attacker supplies a URL the *server* fetches, reaching internal services or the
cloud **metadata endpoint** (`169.254.169.254` → credentials — the Capital One breach);
defend with strict allowlists of destinations, blocking link-local/private/loopback and
redirects, requiring IMDSv2, and network egress control. General rule: validate/allowlist
input at the boundary ([[design-by-contract]]) *and* use structural APIs — validation
alone is not a substitute for parameterization.

## Cross-site scripting (XSS) (OWASP; CS161 ch. 22; 6.858 L13)
XSS runs attacker JavaScript **in the victim's origin**, so it can read the DOM, exfiltrate
cookies/tokens, make authenticated requests, and rewrite the page. Types: **stored**
(payload saved server-side — a comment, profile — and served to every viewer; worst),
**reflected** (payload in the request echoed into the response — a search term in an
error page; delivered via a crafted link), **DOM-based** (client-side JS writes untrusted
data into a dangerous sink — `innerHTML`, `document.write`, `eval`, `location` — without
the server involved). **Defenses**, layered: **contextual output encoding** — encode data
for the context it lands in (HTML body → entity-encode `< > & " '`; HTML attribute →
attribute-encode + quote; JavaScript string → JS-encode/JSON; URL → percent-encode; CSS
→ CSS-encode); frameworks that **auto-escape** by default (React's `{}`, Angular,
templating engines) prevent most XSS — the holes are `dangerouslySetInnerHTML`,
`v-html`, bypassing the framework, and `href="javascript:"`; **sanitize** rich HTML with
a vetted library (DOMPurify), never regex. **Content Security Policy (CSP)**: a response
header restricting where scripts may come from — a strict policy uses **nonces** or
**hashes** and drops `unsafe-inline`/`unsafe-eval` (`script-src 'nonce-…' 'strict-dynamic'`),
turning "inject a `<script>`" into a no-op; report-only mode to roll out. **Trusted
Types** force DOM sinks to accept only vetted objects, killing DOM XSS at the sink.
**HttpOnly** cookies mean a successful XSS still can't read the session cookie (raising
the bar). Defense in depth: encode + framework + CSP + Trusted Types + HttpOnly.

## Cross-site request forgery, clickjacking (OWASP; CS161 ch. 20–21, 23)
**CSRF**: because the browser **auto-attaches cookies** to cross-origin requests, a
malicious page can make *your* browser POST to `bank.com/transfer` while you're logged
in — the server sees a valid session and acts; a **confused deputy**
([[access-control-and-isolation]]) where the deputy is your browser. Defenses:
**SameSite cookies** (`Lax` default blocks cookies on cross-site POSTs and top-level
GETs' subrequests; `Strict` for sensitive apps), **anti-CSRF tokens** (a per-session/
per-request unpredictable token in a hidden field or header that the attacker can't
read due to SOP — synchronizer token, or double-submit cookie), checking the **`Origin`**/
`Sec-Fetch-Site` headers, and never performing state changes on **GET** (SOP allows
cross-origin GET freely). **Clickjacking / UI redressing**: the attacker frames your site
invisibly over their bait so the victim's clicks land on your UI ("delete account");
defend with **`X-Frame-Options: DENY`** / CSP **`frame-ancestors 'none'|self`** to forbid
framing, and framebusting as a fallback. **Login CSRF**, **CORS misconfig** (reflecting
`Origin` with credentials), **postMessage** without origin checks, and **tabnabbing**
(`target=_blank` without `rel=noopener`) are related.

## Access control, auth, transport, and the rest (OWASP A01, A02, A07; CS161)
**Broken access control (A01 — the #1 risk)**: **IDOR/BOLA** — `GET /api/orders/123`
served without checking the caller owns order 123; **missing function-level checks** (an
admin endpoint reachable by a normal user), **path traversal** (`../../etc/passwd` — the
web form of the same "data used as structure" bug; canonicalize and confine), **mass
assignment** (binding request fields to privileged model attributes like `isAdmin`), and
**open redirects** (`?next=//evil.com`). Enforce authorization **server-side, per object,
on every request**, deny by default, and never trust the client or hidden fields
([[web-backends-sessions-and-authentication]]). **Authentication/session (A07)**:
**session fixation** (regenerate the session id on login), **hijacking** (HttpOnly+Secure+
SameSite cookies; short lifetimes; bind cautiously), **credential stuffing/brute force**
(rate limit, MFA, breached-password checks, generic errors — [[web-backends-sessions-and-authentication]],
[[security-principles]]), JWT pitfalls (`alg:none`, no revocation). **Cryptographic
failures (A02)**: plaintext or weak-hashed passwords, missing TLS, weak ciphers, secrets
in code ([[cryptography-basics]]). **Transport**: **TLS everywhere** (LetsEncrypt),
**HSTS** (`Strict-Transport-Security` with preload — skip the downgradeable first HTTP
hop), no **mixed content**, **SRI** (`integrity=` hashes on third-party `<script>`/`<link>`
so a compromised CDN can't swap them — the polyfill.io lesson,
[[software-supply-chain-security]]). **Security headers**: CSP, HSTS, `X-Content-Type-Options:
nosniff`, `Referrer-Policy`, `Permissions-Policy`, COOP/COEP; cookie prefixes (`__Host-`).
**Other A0x**: security misconfiguration (defaults, verbose errors, open buckets),
vulnerable components (dependency scanning — [[dependency-management-and-packaging]]),
insecure design (threat-model the feature — [[security-principles]]), logging/monitoring
failures ([[observability-monitoring-and-incident-response]]).

## How do I protect my web app from common attacks? Building securely: secure defaults + defense in depth
Use frameworks that are **secure by default** (auto-escaping templates, ORM
parameterization, CSRF tokens, secure session cookies, security headers middleware) and
don't opt out; validate input, encode output, parameterize queries, authorize every
request server-side; set the header suite (CSP with nonces, HSTS, frame-ancestors,
nosniff); HttpOnly+Secure+SameSite cookies; secrets in a vault; scan dependencies and
containers; pen-test and fuzz ([[fuzzing]]); learn attacks hands-on (PortSwigger Web
Security Academy, DVWA, OWASP Juice Shop). Treat the OWASP Top 10 and ASVS as the
minimum checklist, not the ceiling.

## Pitfalls
- Escaping SQL by hand instead of parameterizing; blocklisting XSS instead of contextual
  encoding + CSP; regex "sanitizers".
- Relying on CORS or SOP for server-side authorization; state changes on GET.
- Authorization in the UI only; forgetting object-level checks (IDOR).
- CSP with `unsafe-inline`; cookies without HttpOnly/Secure/SameSite; JWTs you can't
  revoke.
- No HSTS (SSL-strip); third-party scripts without SRI; verbose stack traces in prod.

## Related
- [[security-principles]], [[web-backends-sessions-and-authentication]],
  [[access-control-and-isolation]], [[dns-http-and-the-web-stack]],
  [[html-css-and-the-dom]], [[cryptography-basics]], [[network-security-attacks-and-defenses]],
  [[software-supply-chain-security]], [[dependency-management-and-packaging]],
  [[fuzzing]], [[design-by-contract]], [[api-design]],
  [[observability-monitoring-and-incident-response]],
  [[technology-law-privacy-and-intellectual-property]].

## Sources
CS161 textbook ch. 17–24 (read: ToC); OWASP Top 10:2021 (read) and Cheat Sheet Series (XSS Prevention, SQL Injection Prevention, CSRF, CORS, Session Management, Access Control); 6.858 L13–14 (read: schedule; web security model, OWASP); PortSwigger Web Security Academy; Stuttard & Pinto 2011; Zalewski 2011 (*The Tangled Web*); Barth, Jackson & Mitchell 2008 (CSRF); Weichselbaum et al. 2016 (CSP is dead, long live CSP); Anderson 2020 ch. 21.

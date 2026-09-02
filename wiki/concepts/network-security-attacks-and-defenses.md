---
title: Network security — why the Internet's protocols were designed for a trusted network and what breaks (Bellovin), attacks by layer (ARP spoofing and DHCP attacks on the LAN, IP spoofing, TCP sequence prediction and RST injection, BGP hijacking and route leaks, DNS cache poisoning and Kaminsky, DNS spoofing), on-path vs off-path attackers and machine-in-the-middle, denial of service (volumetric, amplification/reflection, SYN floods, application-layer, DDoS and botnets) and defenses, TLS in practice (what it does and doesn't protect, certificates and the CA/PKI trust model, certificate transparency, HSTS, downgrade/SSL-strip), securing the infrastructure (DNSSEC, RPKI/BGPsec, WPA for WiFi, VPNs and IPsec/WireGuard), and perimeter and detection (firewalls, network segmentation, IDS/IPS and their evasion, zero trust)
type: concept
section: "8.1"
level: 400
tags: [network-security, trusted-network-assumption, bellovin, tcp-ip-security, arp-spoofing, arp-poisoning, dhcp-attacks, ip-spoofing, tcp-sequence-prediction, rst-injection, off-path, on-path, machine-in-the-middle, mitm, bgp-hijacking, route-leak, prefix-hijack, dns, dns-cache-poisoning, kaminsky, dns-spoofing, denial-of-service, dos, ddos, amplification, reflection, dns-amplification, ntp-amplification, syn-flood, syn-cookies, application-layer-dos, botnet, mirai, tls, ssl, handshake, cipher-suite, forward-secrecy, certificates, ca, pki, certificate-authority, chain-of-trust, certificate-transparency, ct-logs, hsts, ssl-strip, downgrade-attack, sslstrip, dnssec, rpki, bgpsec, roa, wpa, wpa2, wpa3, wifi-security, vpn, ipsec, wireguard, firewall, stateful-firewall, network-segmentation, ids, ips, intrusion-detection, signature-based, anomaly-based, ids-evasion, ptacek-newsham, zero-trust, beyondcorp, defense-in-depth]
sources: [computer-security-texts-courses-and-seminal-papers]
summary: The Internet's core protocols were designed for a small, mutually trusting research network, so most have no authentication — and network security is largely the story of retrofitting it (Bellovin 1989). Attacks follow the layers: on a LAN, ARP has no authentication so an attacker answers ARP queries to redirect traffic (ARP spoofing → machine-in-the-middle) and rogue DHCP hands out a malicious gateway/DNS; IP source addresses are unauthenticated (spoofing), classic TCP used predictable initial sequence numbers (connection spoofing, and an on-path or well-timed off-path attacker can inject RST or data); BGP trusts route announcements, so a network can announce someone else's prefix (hijack — YouTube/Pakistan 2008, the 2018 Amazon Route 53 theft) or leak routes; DNS resolvers accepted forged answers (cache poisoning, made devastatingly practical by Kaminsky 2008), redirecting names to attacker servers. The attacker's power depends on position: an on-path (machine-in-the-middle) attacker reads and modifies, an off-path one must guess or race. Denial of service ranges from SYN floods (answered by SYN cookies) to volumetric and reflection/amplification attacks (spoof the victim's address to a DNS/NTP/memcached server that replies far larger) and application-layer floods, delivered by botnets (Mirai's IoT devices) and absorbed by overprovisioning, scrubbing/anycast CDNs, and rate limiting. TLS is the workhorse defense: it gives confidentiality, integrity and server authentication over TCP via a handshake that agrees a cipher suite and keys (with forward secrecy in TLS 1.3), but it depends on the CA/PKI trust model — browsers trust a set of certificate authorities to vouch for domains, which fails when a CA is compromised or mis-issues (DigiNotar), so Certificate Transparency logs make every issued certificate publicly auditable; TLS protects content, not metadata, and is undone by SSL-strip downgrades unless HSTS forces HTTPS. Infrastructure defenses add authentication where protocols lacked it — DNSSEC signs DNS records, RPKI/BGPsec authorize route origins, WPA2/3 secure WiFi, IPsec/WireGuard build encrypted tunnels/VPNs — while perimeters (stateful firewalls, segmentation), detection (signature- and anomaly-based IDS/IPS, which attackers evade by ambiguity — Ptacek & Newsham), and the modern zero-trust model (authenticate and authorize every request regardless of network location — Google BeyondCorp) round out defense in depth.
---
# Network security

**In one sentence.** Almost every core Internet protocol assumed the other end was
honest, so attacks are about forging what isn't authenticated (ARP, IP, TCP sequence
numbers, BGP routes, DNS answers) and the defenses are about adding cryptographic
authentication on top (TLS, DNSSEC, RPKI, WPA, IPsec) plus perimeter, detection, and
"trust nothing by network location."

## The original sin: a trusted network (Bellovin 1989; CS161 ch. 25; 6.858 L15 — read)
The ARPANET/early Internet connected cooperating academics, so protocols optimized for
simplicity and openness over authentication. Bellovin's "Security Problems in the TCP/IP
Protocol Suite" catalogued the consequences that still bite: unauthenticated addresses,
predictable sequence numbers, trusting routing and naming. Layered defense-in-depth
(and the OSI layering itself — [[internet-architecture-and-layering]], [[ip-routing-and-forwarding]])
frames the attacks below.

## Attacks by layer (CS161 ch. 26–34)
- **Link/LAN — ARP spoofing**: ARP maps IP→MAC with no authentication; an attacker on the
  segment replies to (or gratuitously announces) ARP for the gateway's IP with its own
  MAC → traffic flows through the attacker (**machine-in-the-middle**); **DHCP attacks**:
  a rogue DHCP server hands victims a malicious default gateway and DNS resolver; **MAC
  flooding** to turn a switch into a hub. Defends: dynamic ARP inspection, DHCP snooping,
  802.1X port authentication.
- **Network — IP spoofing**: source addresses are unauthenticated → forge them (enables
  reflection DoS and blind attacks); ingress filtering (BCP 38) at ISPs limits it but is
  under-deployed.
- **Transport — TCP**: classic stacks used **predictable initial sequence numbers**, letting
  an off-path attacker guess a valid sequence and **spoof a connection** or inject data
  (Mitnick attack); **RST injection** tears down connections (censorship/GFW), **data
  injection** if the attacker can guess/observe sequence numbers; an **on-path** attacker
  does all this trivially. Defends: randomized ISNs, and ultimately TLS for
  authenticity ([[tcp-reliability-and-congestion-control]]).
- **Routing — BGP hijacking**: BGP accepts route announcements on trust; an AS can
  announce a prefix it doesn't own → traffic for those IPs is drawn to it (**prefix
  hijack**: Pakistan Telecom blackholed YouTube globally in 2008; the 2018 hijack that
  stole Amazon Route 53 traffic to steal cryptocurrency), or **route leaks** propagate
  routes that shouldn't be. Defends: **RPKI** route-origin authorization, prefix filters,
  BGPsec (below).
- **Naming — DNS cache poisoning**: a resolver accepts a forged response (matching query
  name, type, and the 16-bit transaction id + source port) and caches it, sending every
  user of that resolver to the attacker's IP; **Kaminsky (2008)** made this practical by
  spraying answers for many subdomains with glue records for the parent, beating the
  cache and the small ID space. Mitigations: source-port randomization (raises entropy),
  0x20 encoding, and properly **DNSSEC** (below); **DNS spoofing** on-path is simpler
  ([[dns-http-and-the-web-stack]]).

## Attacker position, and machine-in-the-middle
Power scales with position: **off-path** (can only send packets; must guess ids/sequence,
race the real party, or exploit spoofing) < **on-path**/**MITM** (reads, modifies, drops,
injects — a malicious WiFi AP, a compromised router, ARP/DNS/BGP redirection) < endpoint
compromise. A MITM defeats confidentiality and integrity unless the endpoints
authenticate each other cryptographically — which is exactly what TLS provides, and why
TLS without certificate validation is worthless.

## Denial of service (CS161 ch. 34; Anderson ch. 21)
Goal: exhaust a resource. **SYN flood** (send SYNs, never complete the handshake → fill the
half-open connection table) answered by **SYN cookies** (encode state in the sequence
number, keep none until ACK). **Volumetric**: saturate the link; **reflection/
amplification**: spoof the victim's source address to servers that reply much larger
(DNS ANY, NTP monlist ×550, memcached ×50 000, SSDP) so the victim is flooded by third
parties — Tbps-scale. **Application-layer**: expensive requests (search, login, GraphQL
depth) at low volume (Slowloris holds connections open). **DDoS** via **botnets**
(compromised IoT — **Mirai** 2016 took down Dyn's DNS and much of the US east-coast web).
Defenses: overprovisioning and **anycast scrubbing** networks/CDNs (Cloudflare,
Akamai) that absorb and filter near the source, rate limiting and challenge (CAPTCHA/
proof-of-work — [[scalable-system-design]] load shedding), SYN cookies, disabling
amplifiers (close open resolvers), upstream filtering, BCP 38. Ransom DDoS and DDoS as
cover for other attacks.

## TLS in practice and the PKI trust model (CS161 ch. 31, 13; 6.858 L16–17 — read)
**TLS** (over TCP; QUIC embeds it — [[dns-http-and-the-web-stack]]) provides
**confidentiality**, **integrity**, and **server authentication** (optionally mutual): the
**handshake** negotiates a cipher suite, authenticates the server via its **certificate**,
and establishes session keys; **TLS 1.3** uses (EC)DHE for **forward secrecy** (a later key
compromise doesn't decrypt past traffic), removes legacy ciphers, and cuts setup to 1-RTT
(0-RTT with replay caveats). What TLS protects: the content of the connection against
on/off-path attackers. What it does **not**: metadata (destination IP, SNI mostly — ECH
helps, timing, sizes), the endpoints themselves, or anything if certificate validation
is skipped. **PKI / chain of trust**: your browser/OS ships a **root store** of trusted
**Certificate Authorities**; a CA signs a certificate binding a domain to a public key
after **domain validation** (ACME/Let's Encrypt: prove control via HTTP/DNS challenge);
the server presents a chain root→intermediate→leaf; the client verifies signatures,
validity, hostname, and revocation. **Failure modes**: a compromised or coerced CA can
mis-issue for any domain (**DigiNotar** 2011 issued a wildcard *.google.com used to spy
on Iranians → DigiNotar destroyed; Symantec distrusted for sloppy issuance) — the trust
is only as strong as the *weakest* of hundreds of CAs. **Certificate Transparency**:
every issued certificate must be logged in public append-only **CT logs** (Merkle trees —
[[hash-functions-cryptographic]]) that browsers check, so mis-issuance is detectable
after the fact (domain owners monitor logs); revocation (CRL/OCSP, OCSP stapling,
short-lived certs) remains weak. **Downgrade / SSL-strip** (Marlinspike): a MITM keeps
the user on HTTP and proxies HTTPS to the server → the user never gets TLS; defeated by
**HSTS** (server declares "HTTPS only" so the browser refuses HTTP; preload lists ship it
in the browser) and HTTPS-everywhere defaults. TLS misuse (not validating certs in apps/
IoT, accepting any cert) is a top real-world failure ([[cryptography-basics]],
[[public-key-cryptography]]).

## Adding authentication to the infrastructure
- **DNSSEC**: signs DNS records with a chain of trust from the root's key, so resolvers
  verify answers weren't forged (defeats cache poisoning) — deployment is partial and it
  authenticates records, not confidentiality; DoH/DoT encrypt the resolver query for
  privacy ([[dns-http-and-the-web-stack]]).
- **RPKI / BGPsec**: **RPKI** lets address holders publish **ROAs** (which AS may originate
  their prefix) so routers reject invalid origins (Route Origin Validation — now widely
  deployed, cutting hijacks); **BGPsec** would sign the whole AS path (little deployment).
- **WiFi — WPA2/WPA3**: WEP was broken (RC4 key reuse); **WPA2** (AES-CCMP, 4-way handshake)
  is standard but the PSK is offline-crackable and KRACK reinstalls keys; **WPA3** adds
  SAE (dragonfly) for forward secrecy and offline-attack resistance, plus Enterprise
  (802.1X/EAP with a RADIUS server) for per-user keys.
- **VPNs / tunnels**: **IPsec** (AH/ESP, IKE) and **WireGuard** (modern, small,
  Curve25519/ChaCha20) build encrypted authenticated tunnels — for remote access and
  site-to-site; a VPN moves trust to the VPN provider/endpoint, it is not anonymity
  ([[privacy-enhancing-technologies]] for Tor).

## Perimeter, detection, and zero trust (CS161 ch. 35–37; 6.858)
**Firewalls**: **stateful** packet filters at the boundary (allow established, default-deny
inbound), application/next-gen firewalls (L7 inspection), WAFs for web apps; **network
segmentation** and micro-segmentation limit lateral movement after a breach (defense in
depth — [[security-principles]]). **IDS/IPS**: **signature-based** (Snort/Suricata rules
match known attacks — precise, blind to novelty) vs **anomaly-based** (flag deviations —
catches novel, noisy with false positives); **evasion** (Ptacek & Newsham 1998): because
the IDS and the endpoint may interpret ambiguous packets differently (TTL tricks,
overlapping fragments, differing TCP reassembly), an attacker crafts traffic the IDS
reads as benign and the target reads as the attack — normalization and endpoint agreement
are required. **Zero trust / BeyondCorp** (Google): abandon the "inside the perimeter =
trusted" model (which fails once one host is compromised — the flat-network breach);
instead authenticate and authorize **every request** based on device and user identity
and posture, regardless of network location, with strong auth (mTLS, device certs, MFA)
and least-privilege access ([[access-control-and-isolation]], [[security-principles]]).
Monitoring, NetFlow, EDR/XDR, honeypots, and incident response detect and contain what
gets through ([[observability-monitoring-and-incident-response]]).

## Pitfalls
- Trusting the LAN ("internal" traffic) — ARP/DHCP/rogue-AP MITM; flat networks.
- TLS without certificate/hostname validation (apps, IoT, internal services); no HSTS
  (SSL-strip); trusting a private CA carelessly.
- Running open resolvers/NTP (amplifiers); no ingress filtering; no DDoS plan.
- IDS signatures as the only defense; ignoring evasion and encrypted-traffic blind spots.
- Perimeter-only security ("crunchy outside, soft inside") instead of zero trust +
  segmentation.

## Related
- [[security-principles]], [[dns-http-and-the-web-stack]],
  [[ip-routing-and-forwarding]], [[tcp-reliability-and-congestion-control]],
  [[internet-architecture-and-layering]], [[cryptography-basics]],
  [[public-key-cryptography]], [[hash-functions-cryptographic]], [[web-security]],
  [[access-control-and-isolation]], [[scalable-system-design]],
  [[observability-monitoring-and-incident-response]], [[privacy-enhancing-technologies]].

## Sources
CS161 textbook ch. 25–39 (read: ToC); Bellovin 1989; 6.858 L15–17 (read: schedule; TCP/IP problems, SSL 3.0 analysis, certificates); Kaminsky 2008 (DNS); Ptacek & Newsham 1998 (IDS evasion); Marlinspike 2009 (sslstrip); Antonakakis et al. 2017 (Mirai); Durumeric et al. 2013 (CT/HTTPS ecosystem); RFC 8446 (TLS 1.3), RFC 4033 (DNSSEC), RFC 6480 (RPKI); Ward & Beyer 2014 (BeyondCorp); Anderson 2020 ch. 21.

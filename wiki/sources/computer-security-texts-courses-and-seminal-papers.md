---
title: Computer security — the Berkeley CS161 textbook (Wagner, Weaver, Kao et al.; free; ToC and ch. 1 "Security Principles" read), MIT 6.858/6.5660 (Zeldovich; 2023 schedule read), Stanford CS155, Anderson's Security Engineering (3e 2020; chapter list read), Bishop's Computer Security: Art and Science, The Web Application Hacker's Handbook, Erickson's Hacking: The Art of Exploitation, OWASP Top 10:2021 (read) and Cheat Sheets; Saltzer & Schroeder's "The Protection of Information in Computer Systems" (1975; abstract and glossary read), Thompson's "Reflections on Trusting Trust" (1984), Aleph One's "Smashing the Stack for Fun and Profit" (1996), Lampson's "A Note on the Confinement Problem" (1973), Spectre/Meltdown (2018)
type: source
section: "8.1"
level: 300
tags: [cs161, berkeley, wagner, weaver, kao, computer-security-textbook, 6-858, 6-5660, mit, zeldovich, cs155, stanford, boneh, anderson, security-engineering, bishop, art-and-science, web-application-hackers-handbook, erickson, hacking-art-of-exploitation, owasp, owasp-top-10, cheat-sheets, saltzer-schroeder, protection-of-information, thompson, trusting-trust, aleph-one, smashing-the-stack, lampson, confinement, spectre, meltdown, threat-models, pwn-college]
sources: []
authors: [David Wagner, Nicholas Weaver, Peyrin Kao, Nickolai Zeldovich, Dan Boneh, Ross Anderson, Matt Bishop, Jerome Saltzer, Michael Schroeder, Ken Thompson, Aleph One, Butler Lampson, Paul Kocher, Moritz Lipp]
year: 2024
institution: UC Berkeley / MIT / Stanford / Cambridge
url: https://textbook.cs161.org/
license: CC BY-SA 4.0 (CS161); Anderson 3e free chapters; papers open
format: html
summary: The CS161 textbook (read: ToC; ch. 1 in full) is a compact free survey — Security Principles (1.1 know your threat model with its six attacker assumptions — unnoticed interaction, general knowledge of the system, persistent and lucky, resourced, able to coordinate across systems, every device a target (the casino fish-tank thermometer); 1.2 consider human factors; 1.3 security is economics; 1.4 detect if you can't prevent; 1.5 defense in depth; 1.6 least privilege; 1.7 separation of responsibility; 1.8 ensure complete mediation; 1.9 Shannon's maxim / Kerckhoffs; 1.10 fail-safe defaults; 1.11 design security in from the start; 1.12 the trusted computing base; 1.13 TOCTTOU), Memory Safety (x86 and the call stack, vulnerabilities, mitigations), Cryptography (ch. 5–16: symmetric, hashes, MACs, PRNGs, Diffie–Hellman, public-key, signatures, certificates, passwords, case studies, Bitcoin), Web Security (SQL injection, the web, same-origin policy, cookies and sessions, CSRF, XSS, UI attacks, CAPTCHAs), Network Security (ARP, DHCP, WPA, BGP, TCP/UDP, TLS, DNS, DNSSEC, DoS, firewalls, intrusion detection and abusing it, malware, anonymity and Tor); MIT 6.858 (read: 2023 schedule) is paper-driven — threat models, Google infrastructure security, baggy bounds checking, OKWS privilege separation, containers and VMs, software fault isolation via WebAssembly, KSplit library sandboxing, iOS and Android security models, transient-execution attacks, EXE symbolic execution, Knox verification, the web security model and OWASP, TCP/IP security problems, SSL 3.0 analysis, certificates, U2F, secure messaging, supply chain/SBOM, Tor circuit fingerprinting, SUNDR untrusted storage, secure processors and controlled-channel attacks, Zoom E2E — with labs on buffer overflows, privilege separation, symbolic execution, browser security, ACME + WebAuthn; Anderson's Security Engineering (read: 3e chapter list — what is security engineering, who is the opponent, psychology and usability, protocols, cryptography, access control, distributed systems, economics, multilevel security, boundaries, inference control, banking, physical protection, monitoring and metering, nuclear command and control, security printing, biometrics, tamper resistance, side channels, advanced cryptographic engineering, network attack and defence, phones, electronic warfare, copyright and DRM, surveillance or privacy, secure systems development, assurance and sustainability) is the encyclopedic systems view; OWASP Top 10:2021 (read) ranks broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable and outdated components, identification and authentication failures, software and data integrity failures, logging and monitoring failures, SSRF; and Saltzer & Schroeder (read: abstract, glossary) define the vocabulary — principal, authenticate/authorize, access control list vs capability (ticket-oriented vs list-oriented), domain, confinement, complete isolation, protected subsystem, discretionary vs nondiscretionary, revoke, TCB — and the eight design principles (economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability) that every later list restates.
---
# Computer security: sources

## What they are
- **CS161 textbook** (Berkeley; read: ToC, ch. 1): 39 chapters in five parts — principles;
  memory safety (2–4); cryptography (5–16); web security (17–24); network security
  (25–39). Course adds projects (a binary-exploitation project, a crypto project, a web
  project, a network project). Free, maintained, CC BY-SA.
- **MIT 6.858 / 6.5660** (Zeldovich & Devadas; read: Spring 2023 calendar): 24 lectures
  with a paper each (listed in the summary), five labs (buffer overflows on a web
  server, privilege separation, symbolic execution, browser security, ACME + WebAuthn).
  The 2014 OCW version has full videos.
- **Stanford CS155** (Boneh & Mitchell): control hijacking, sandboxing, web security,
  network security, mobile, crypto in practice; projects on exploits and web attacks.
- **Anderson, *Security Engineering*** (3e 2020; free chapters; read: chapter list) —
  systems, people, economics, and the domains (banking, nuclear C2, biometrics, DRM,
  phones) where security is really engineered; 15 lecture videos.
- **Bishop, *Computer Security: Art and Science*** (2e 2018): formal foundations — access
  control matrix, HRU undecidability, Bell–LaPadula, Biba, Clark–Wilson, Chinese Wall,
  information flow, assurance. **Web Application Hacker's Handbook** (Stuttard & Pinto
  2011; superseded in practice by PortSwigger's Web Security Academy). **Erickson,
  *Hacking: The Art of Exploitation*** (2e 2008): C, assembly, stack/heap/format-string
  exploitation, shellcode, networking attacks, crypto — hands-on. **OWASP** Top 10:2021
  (read), ASVS, Cheat Sheet Series, Testing Guide, Dependency-Check.
- **Seminal**: **Saltzer & Schroeder 1975** (read: abstract, glossary; §I.A.3 principles
  from memory) — the tutorial that fixed the vocabulary and the eight principles;
  **Thompson 1984** (trusting trust — a self-reproducing compiler backdoor;
  [[software-supply-chain-security]]); **Aleph One 1996** (Phrack 49: the stack buffer
  overflow tutorial that made exploitation public knowledge; [[software-exploitation-and-mitigations]]);
  **Lampson 1973** (confinement: a borrowed program must not leak its caller's data —
  covert channels; [[access-control-and-isolation]]); Bell & LaPadula 1973; Denning 1976
  (lattice model of information flow); Anderson 1972 (reference monitor); Shacham 2007
  (return-oriented programming); Kocher et al. 2018 (Spectre) and Lipp et al. 2018
  (Meltdown); Bellovin 1989 (security problems in TCP/IP); Ptacek & Newsham 1998
  (IDS evasion); Kerckhoffs 1883.

## Key ideas → pages
[[security-principles]], [[access-control-and-isolation]],
[[software-exploitation-and-mitigations]], [[web-security]],
[[network-security-attacks-and-defenses]]; existing: [[memory-safety-and-buffer-overflows]],
[[undefined-behavior]], [[cryptography-basics]], [[symmetric-encryption-and-authenticated-encryption]],
[[public-key-cryptography]], [[hash-functions-cryptographic]],
[[cryptographic-protocols-and-zero-knowledge]], [[web-backends-sessions-and-authentication]],
[[software-supply-chain-security]], [[dns-http-and-the-web-stack]], [[differential-privacy]].

## What they add
CS161 ch. 1 is the best one-chapter statement of how to think like a defender; 6.858's
reading list is the graduate canon; Anderson insists security is about people, money and
institutions as much as code; Saltzer & Schroeder is where the words come from.

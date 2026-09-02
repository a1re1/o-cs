---
title: Security principles — thinking like a defender: threat models (who is the attacker, what can they do, what do you protect — and the standard attacker assumptions), security as economics and risk management, the CIA triad and beyond (confidentiality, integrity, availability, authenticity, non-repudiation), Saltzer & Schroeder's eight design principles (economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability) and CS161's modern list (defense in depth, detect if you can't prevent, Shannon's maxim, design security in, minimize the TCB, beware TOCTTOU), the trusted computing base, human factors and usable security, attack surface, and the vocabulary (principal, authentication vs authorization, vulnerability vs exploit vs threat, zero-day, security through obscurity)
type: concept
section: "8.1"
level: 300
tags: [security-principles, threat-model, threat-modeling, attacker-model, adversary, assets, attacker-assumptions, security-is-economics, risk, cost-benefit, cia-triad, confidentiality, integrity, availability, authenticity, non-repudiation, saltzer-schroeder, economy-of-mechanism, fail-safe-defaults, fail-closed, complete-mediation, reference-monitor, open-design, kerckhoffs, shannons-maxim, separation-of-privilege, two-person-rule, least-privilege, least-common-mechanism, psychological-acceptability, usable-security, human-factors, defense-in-depth, detect-if-you-cant-prevent, design-security-in, tcb, trusted-computing-base, tocttou, race-condition, attack-surface, principal, authentication, authorization, vulnerability, exploit, threat, zero-day, security-through-obscurity, stride, cs161, anderson, secure-by-default]
sources: [computer-security-texts-courses-and-seminal-papers]
summary: Security is not a property you add but a set of reasoning habits — start from a threat model (which attacker, with what resources and access, against which assets, and what you are willing to spend), assuming with CS161 that the attacker interacts unnoticed, knows your system's general design, is persistent and lucky ("if an attack succeeds 1 in a million times, they will try a million times"), is resourced, coordinates across systems, and treats every device as a target (the casino breached through a fish-tank thermometer); treat security as economics — defenders spend to raise the attacker's cost above the asset's value to them, not to reach "secure", so ranking risks and accepting some is the job; state goals in terms of confidentiality, integrity and availability (plus authenticity, non-repudiation, privacy) so you can say what "secure" means for this system; and apply the design principles that Saltzer and Schroeder wrote down in 1975 and every later list restates — economy of mechanism (small, simple, auditable), fail-safe defaults (deny unless permitted; fail closed), complete mediation (check every access, every time, through a reference monitor that cannot be bypassed — the principle TOCTTOU races violate), open design (security must not depend on secrecy of the design — Kerckhoffs/Shannon's maxim "the enemy knows the system"; only keys are secret), separation of privilege (two keys, two people, two factors), least privilege (every component gets the minimum access for its job, so a compromise stays small), least common mechanism (don't share state between users you don't need to), and psychological acceptability (if the secure path is hard, people will route around it) — to which modern practice adds defense in depth (layers so one failure isn't total), detect if you can't prevent (logging, monitoring, tamper-evidence), design security in from the start, and minimize the trusted computing base (everything whose failure breaks the guarantee — keep it small enough to reason about); with the shared vocabulary of principals, authentication (who) vs authorization (what), vulnerability vs exploit vs threat, attack surface, and zero-days.
---
# Security principles

**In one sentence.** Decide who you are defending against and what it would cost them,
then build so that every access is checked, every default denies, every component has
only the privilege it needs, the design survives being published, the trusted core is
small, humans can follow the secure path, and you find out when something got through
anyway.

## Threat models: who is the attacker? (CS161 §1.1 — read; Anderson ch. 2)
"A threat model is a model of who your attacker is and what resources they have."
Motives: money (criminals, ransomware), politics/intelligence (states), fun/status
(teenagers, researchers), personal (intimate partners, insiders — often the most
dangerous because they are already inside). Standard **assumptions** about the attacker
(CS161): (1) can interact with your system **without being noticed**; (2) has **general
knowledge** of the system (OS, software versions, likely vulnerabilities); (3) is
**persistent and lucky** — "if an attack is successful 1/1 000 000 times, the attacker will
try 1 000 000 times"; (4) will **devote time and resources** (up to what the target is
worth); (5) can **coordinate** complex attacks across systems and chain them; (6) **every
system is a potential target** — the casino breached via a fish-tank thermometer on the
network. Old code deserves suspicion: its assumptions (a trusted academic Internet)
no longer hold. **Assets** and **goals**: what must be protected, from what (read,
modify, deny), for how long, and what a breach costs; **capabilities**: network position
(remote, on-path, in the LAN, physical access), code execution (none, unprivileged,
root), knowledge (black/grey/white box), budget. Structured methods: **STRIDE** (spoofing,
tampering, repudiation, information disclosure, denial of service, elevation of
privilege) per data flow; attack trees; "what would I do if I were them". Write it
down — a design without a threat model is secure against nothing in particular.

## Security is economics; goals (CS161 §1.3; Anderson ch. 8)
No system is secure against an unbounded attacker; defenders raise the attacker's cost
(time, money, risk of detection) above the value of the asset *to the attacker* — a
$10 lock on a $5 bike is rational. So: **rank risks** (likelihood × impact), spend on the
top ones, and **accept** the rest explicitly (risk register); the weakest link determines
the outcome ("a chain is as strong as its weakest link"); attackers optimize too
(phishing beats cryptanalysis). Incentives matter (Anderson: whoever bears the loss
should control the risk — liability design; externalities explain why patching lags).
**Goals** (the CIA triad): **confidentiality** (no unauthorized reading — encryption,
access control), **integrity** (no unauthorized modification — MACs, signatures,
permissions, audit), **availability** (the system works when needed — redundancy,
rate limits, DoS defence); also **authenticity** (of origin), **non-repudiation**
(cannot deny having acted — signatures, logs), **accountability**, **privacy**. A
security *policy* states which principals may do what to which objects; a *mechanism*
enforces it; a *model* lets you reason about it ([[access-control-and-isolation]]).

## The design principles (Saltzer & Schroeder 1975; CS161 §1.4–1.13 — read)
1. **Economy of mechanism**: keep the security mechanism small and simple — it must be
   inspected and tested line by line; complexity hides bugs (OpenSSL's Heartbleed lived
   in a rarely-used extension).
2. **Fail-safe defaults** (CS161 §1.10): base access on permission, not exclusion; the
   default is deny; on error, **fail closed** (a firewall that crashes should block, a
   payment check that times out should not approve) — but note availability trade-offs.
3. **Complete mediation** (§1.8): every access to every object is checked for authority,
   every time; the checker (**reference monitor**: always invoked, tamper-proof, small
   enough to verify — Anderson 1972) cannot be bypassed; caching decisions is where this
   breaks. **TOCTTOU** (§1.13): check then use with a window in between (`access()` then
   `open()` on a path the attacker swaps via symlink; a file's permissions changing
   after the check) — a *race* that violates complete mediation; fix by making check and
   use atomic (`openat` + `O_NOFOLLOW`, operate on the opened descriptor, capabilities).
4. **Open design** (§1.9, **Shannon's maxim** / **Kerckhoffs's principle**): "the enemy knows
   the system" — security must not depend on the secrecy of the design or the code,
   only on secrets that are small, changeable, and replaceable (keys, passwords).
   **Security through obscurity** is not a mechanism; it can be a *layer* (unusual port
   numbers reduce noise) but never the only one ([[cryptography-basics]]).
5. **Separation of privilege** (§1.7 "separation of responsibility"): require two
   independent conditions for a sensitive action — two keys for the safe, two-person
   rule for launches and deploys, **two-factor** authentication, code review plus CI —
   so one compromised person/credential isn't enough.
6. **Least privilege** (§1.6): every program and user operates with the smallest set of
   privileges needed for its task, for the shortest time — so a compromised component
   yields little (a web server that doesn't run as root; a token scoped to one bucket;
   [[access-control-and-isolation]] privilege separation, [[infrastructure-as-code-and-devops]]
   short-lived credentials). Corollary: **minimize the attack surface** — fewer exposed
   interfaces, features off by default, remove what you don't need.
7. **Least common mechanism**: minimize mechanisms shared between users — shared state
   is a channel (side channels, covert channels) and a single point of compromise
   (one kernel bug affects all tenants — hence VMs over containers for hostile tenants).
8. **Psychological acceptability** (§1.2 human factors): the secure way must be the
   easy way; users route around unusable security (postponed updates, password
   reuse, "remind me later"); design for humans as they are (the NSA key-shaped
   crypto token that any 18-year-old soldier can use); social engineering targets
   people, so training and defaults matter more than exhortation
   ([[human-computer-interaction]]).
Modern additions: **defense in depth** (§1.5): multiple independent layers (network
segmentation + host hardening + app auth + encryption + monitoring) so a single failure
isn't a breach — layers must be independent to count; **detect if you can't prevent**
(§1.4): logging, integrity checks, alerts, tamper-evident audit trails, honeypots; know
you've been breached and how ([[observability-monitoring-and-incident-response]]);
**design security in from the start** (§1.11): retrofitting is expensive and leaky (the
Internet's protocols, [[network-security-attacks-and-defenses]]); **the trusted computing
base** (§1.12): the set of hardware/software whose correctness the security depends on —
keep it small, isolate it, verify it (a bug outside the TCB can't violate the policy; a
bug inside can); **secure by default** and **secure by design** (CISA 2023) as vendor
obligations; **assume breach**/zero trust — no implicit trust from network location.

## Vocabulary
**Principal**: the entity to which authorizations are granted — the unit of accountability
(user, service account, role). **Authentication**: verifying a claimed identity (something
you know/have/are); **authorization**: deciding what an authenticated principal may do;
**audit**: recording what they did. **Vulnerability**: a weakness (bug, misconfiguration);
**exploit**: code/technique that uses it; **threat**: a potential cause of harm (an actor +
capability); **attack**: the realized attempt; **zero-day**: a vulnerability unknown to the
defender/vendor (no patch); **n-day**: known and patched, still exploited (most
breaches). **Attack surface**: all points where an attacker can interact. **Trust** vs
**trustworthy**: you trust what can hurt you; aim to trust only what is trustworthy.
**Security policy** vs **mechanism**; **assurance**: the evidence that a mechanism enforces
the policy (testing, review, formal verification — [[program-verification]]).

## How do I think about securing a new system, and where do I start? A checklist for a design review
Threat model written? Assets and goals named? Every entry point authenticated and
authorized (complete mediation), including internal APIs? Defaults deny; errors fail
closed? Components run with least privilege, in separate processes/containers, with
scoped, short-lived credentials? Secrets small and rotatable; design publishable? Two
independent controls on the dangerous actions? Attack surface minimized (features off,
ports closed, dependencies few — [[software-supply-chain-security]])? Input validated at
the boundary ([[design-by-contract]]); memory-safe languages or mitigations
([[software-exploitation-and-mitigations]])? Logging and alerting to detect what gets
through? Users able to do the right thing without training? TCB identified and small?
Recovery plan (backups, rotation, incident response) exists?

## Pitfalls
- Designing for "an attacker" instead of *your* attackers; defending the front door
  while the fish tank is on the network.
- Secrecy of design as the mechanism; a hidden admin URL as "authentication".
- Check-then-act races; caching an authorization decision past its validity.
- Root/admin everywhere "for now"; long-lived broad credentials.
- Security that users must fight — they will win.
- No detection: breaches discovered by a journalist months later.

## Related
- [[access-control-and-isolation]], [[software-exploitation-and-mitigations]],
  [[web-security]], [[network-security-attacks-and-defenses]], [[cryptography-basics]],
  [[memory-safety-and-buffer-overflows]], [[software-supply-chain-security]],
  [[web-backends-sessions-and-authentication]], [[infrastructure-as-code-and-devops]],
  [[observability-monitoring-and-incident-response]], [[design-by-contract]],
  [[program-verification]], [[human-computer-interaction]],
  [[computing-ethics-and-professional-responsibility]] (ACM 2.8, 2.9),
  [[technology-law-privacy-and-intellectual-property]].

## Sources
Wagner, Weaver, Kao et al., CS161 textbook ch. 1 (read); Saltzer & Schroeder 1975 (read: abstract, glossary; §I.A.3); Anderson 2020 ch. 1–3, 8; Anderson 1972 (reference monitor); Kerckhoffs 1883; Shannon 1949; Shostack 2014 (*Threat Modeling*); Microsoft STRIDE (Kohnfelder & Garg 1999); CISA "Secure by Design" 2023; Lampson 2004 ("Computer security in the real world").

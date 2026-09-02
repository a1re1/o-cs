---
title: Technology law for engineers — privacy and data protection (fair information practices, GDPR's lawful bases/rights/DPIAs/breach notification, CCPA/CPRA, HIPAA/COPPA/FERPA sectoral laws, contextual integrity, privacy by design and data minimization, de-identification limits), intellectual property (copyright and fair use, software patents, trade secrets, trademarks, licenses and DMCA anti-circumvention, API copyrightability after Oracle v. Google, AI training-data and output questions), computer crime law (CFAA "unauthorized access", Van Buren, security research safe harbors and responsible disclosure), platform liability and speech (Section 230, DSA/DMA), accessibility law (ADA, Section 508, EAA, WCAG as the standard), export controls and encryption, contracts and liability (EULAs, warranties, SLAs), and how to work with counsel
type: concept
section: "7.8"
level: 200
tags: [technology-law, privacy-law, data-protection, fair-information-practices, fipps, gdpr, lawful-basis, consent, legitimate-interest, data-subject-rights, right-to-erasure, data-portability, dpia, breach-notification, dpo, ccpa, cpra, state-privacy-laws, hipaa, coppa, ferpa, glba, contextual-integrity, nissenbaum, privacy-by-design, data-minimization, purpose-limitation, retention, de-identification, re-identification, anonymization, pseudonymization, intellectual-property, copyright, fair-use, software-patents, alice, trade-secrets, trademarks, dmca, anti-circumvention, section-1201, oracle-v-google, api-copyright, ai-training-data, ai-copyright, cfaa, unauthorized-access, van-buren, hiqa-v-linkedin, security-research, safe-harbor, responsible-disclosure, section-230, platform-liability, dsa, dma, accessibility-law, ada, section-508, european-accessibility-act, wcag, export-controls, encryption-law, ear, crypto-wars, contracts, eula, warranty, sla, liability, product-liability, ai-act, regulation, counsel]
sources: [computing-ethics-texts-courses-and-codes]
summary: Engineers don't need to be lawyers but must recognize when law binds a design — most often in five areas: privacy and data protection, where the fair information practice principles (notice, choice, access, security, purpose limitation, minimization, accountability) became binding in the GDPR (a lawful basis for every processing purpose — consent, contract, legal obligation, vital interest, public task, legitimate interest — data-subject rights to access, rectification, erasure, portability and objection, data-protection impact assessments for risky processing, 72-hour breach notification, data-protection officers, and fines up to 4 % of global revenue), in California's CCPA/CPRA and the growing set of US state laws, and in sectoral US statutes (HIPAA for health data, COPPA for under-13s, FERPA for education, GLBA for finance), with Nissenbaum's contextual integrity (information flows are appropriate relative to the norms of the context they came from) as the theory that explains why "it was public data" is not a defense and privacy by design (minimize, limit purpose, set retention, pseudonymize, and remember that de-identification is fragile — Sweeney's 87 % re-identification from zip/birthdate/sex, the Netflix Prize, and differential privacy as the rigorous alternative) as the engineering response; intellectual property, where copyright protects expression not ideas (with fair use's four factors, and Oracle v. Google holding Google's reimplementation of the Java API declarations fair use without deciding API copyrightability), patents protect inventions but software claims must clear Alice's abstract-idea bar, trade secrets protect what you keep secret (NDAs, the DTSA), trademarks protect source identity, licenses govern use (open source obligations are copyright conditions), the DMCA both provides notice-and-takedown safe harbor and criminalizes circumventing technical protection measures (with security-research exemptions), and generative-AI training and outputs are being litigated (NYT v. OpenAI, Getty v. Stability, the Copyright Office's human-authorship requirement); computer crime, where the CFAA's "unauthorized access" was narrowed by Van Buren to gates, not purposes, hiQ v. LinkedIn treated public scraping as not "without authorization", and security research is protected by DOJ policy and vendor safe harbors but still requires authorization and coordinated disclosure; platform and speech law (Section 230's immunity for third-party content, the EU's Digital Services and Digital Markets Acts); accessibility law (ADA and Section 508 in the US, the European Accessibility Act, with WCAG as the de facto standard and lawsuits over inaccessible sites common); plus export controls on encryption, contracts (EULAs, warranties, SLAs, limitation of liability) and emerging AI regulation (EU AI Act's risk tiers) — with the working rule that engineers flag the trigger (personal data, copying, access, accessibility, cross-border) and bring counsel in early rather than after launch.
---
# Technology law, privacy and intellectual property

**In one sentence.** Law reaches into design at predictable points — whenever you collect
data about people, copy or reimplement someone's work, access a system you don't own,
host others' speech, ship an interface the public must use, or cross a border with
cryptography — and the engineer's job is to recognize those points, know the shape of
the rule, and involve counsel before the architecture hardens.

## Privacy and data protection (GDPR; CCPA/CPRA; FIPPs; Nissenbaum)
**Fair Information Practice Principles** (HEW 1973 → OECD 1980): notice/transparency,
choice/consent, purpose specification and limitation, data minimization, use
limitation, access and correction, security, retention limits, accountability. **GDPR**
(EU 2018; extraterritorial — applies to anyone processing EU residents' data): personal
data = anything relating to an identifiable person (IP addresses, device ids, pseudonyms
count); special categories (health, biometrics, religion, sexual orientation…) need
extra bases; every processing purpose needs a **lawful basis** — consent (freely given,
specific, informed, unambiguous, withdrawable; not for anything you could do anyway),
contract, legal obligation, vital interests, public task, **legitimate interests**
(balancing test); **data-subject rights**: access (a copy within a month), rectification,
**erasure** ("right to be forgotten" — design for deletion across backups and
downstream systems), restriction, **portability** (machine-readable export), objection
(incl. to profiling/direct marketing), rights around automated decisions (Art. 22 —
human review); **controllers** vs **processors** (contracts required); **DPIA** for high-risk
processing (new tech, large-scale profiling, sensitive data); **breach notification** to
the regulator within 72 h; **DPO** for large-scale monitoring; **privacy by design and by
default** (Art. 25); international transfers (adequacy, SCCs, the Schrems litigation
over US surveillance); fines up to €20 M / 4 % global turnover (Meta €1.2 B, Amazon
€746 M). **US**: no general federal law; **CCPA/CPRA** (California: notice, right to know/
delete/correct/opt out of sale or *sharing*, limit sensitive data, non-discrimination;
"Do Not Sell" and Global Privacy Control signals) and ~20 state laws (Virginia,
Colorado, Texas…); sectoral: **HIPAA** (covered entities and business associates; PHI;
security rule), **COPPA** (under-13: verifiable parental consent — the reason for "must
be 13"), **FERPA** (education records), **GLBA** (financial), **BIPA** (Illinois biometrics —
private right of action; Facebook $650 M), FTC Act §5 (unfair/deceptive practices —
the de facto US privacy regulator: broken promises, dark patterns, security failures);
plus ECPA/Wiretap Act (interception, consent for recording), CAN-SPAM/TCPA (marketing
messages), the SEC's cyber-disclosure rules. Elsewhere: Brazil LGPD, China PIPL, India
DPDP, Canada PIPEDA, Japan APPI — GDPR-like patterns dominate.
**Theory**: **contextual integrity** (Nissenbaum): privacy is the appropriateness of
information *flows* relative to the norms of the context in which information was
shared — medical data flowing to an insurer violates norms even if "the user agreed"
in a 40-page policy; "publicly available" is not a license for any use (Cambridge
Analytica; scraping for face recognition — Clearview fined across the EU). **Engineering**:
data map/inventory (what, why, where, who, how long), **minimization** (don't collect
what you can't justify), **purpose limitation** (new use → new basis), retention and
deletion pipelines, pseudonymization, access controls and logging, encryption
([[security-principles]]), consent UX that isn't a dark pattern, privacy reviews in
design ([[computing-ethics-and-professional-responsibility]]), and honesty about
**de-identification**: Sweeney (2000) re-identified 87 % of Americans from zip + birth
date + sex; the Netflix Prize (Narayanan & Shmatikov 2008) and AOL search logs (2006)
were de-anonymized by linkage; k-anonymity/l-diversity are weak; **differential privacy**
is the rigorous tool ([[differential-privacy]]); aggregate and synthetic data still leak
([[fairness-in-machine-learning]] for the discrimination side).

## Intellectual property (Copyright Act; Patent Act; DMCA; Oracle v. Google)
- **Copyright**: automatic on original *expression* (code, docs, UI art, datasets'
  selection/arrangement) — not ideas, methods, facts, or functional elements (idea/
  expression merger); author or employer (work for hire — check your contract and
  moonlighting/IP-assignment clauses; state laws limit them); term life+70 / 95 years;
  exclusive rights to copy, distribute, make derivatives, perform; **fair use** (17
  U.S.C. §107) balances four factors — purpose and character (transformative? commercial?),
  nature of the work, amount used, market effect; **Oracle v. Google** (2021): Google's
  copying of 11 500 lines of Java API declarations was fair use (reimplementation for a
  new platform, functional nature of declaring code) — the Court assumed but did not
  decide that APIs are copyrightable, so clean-room reimplementation remains prudent
  practice ([[api-design]]); **licenses** are conditions on copyright permissions
  ([[software-licensing]]); open source violations are copyright infringement (SFC v.
  Vizio, Hellwig v. VMware); **DMCA §512** notice-and-takedown safe harbor for hosts
  (and abuse via bogus takedowns), **§1201 anti-circumvention** (breaking DRM/TPMs is
  illegal even for lawful uses, with triennial exemptions — security research, repair,
  accessibility — and the chilling effect on researchers); **generative AI**: training on
  copyrighted works (fair use? — NYT v. OpenAI, Authors Guild, Getty v. Stability;
  Thomson Reuters v. Ross 2025 found no fair use for a competing non-generative use),
  outputs (the US Copyright Office requires human authorship; AI-only images
  unprotectable; memorized/regurgitated content infringes), code models and license
  compliance (GitHub Copilot litigation; attribution of copyleft snippets) —
  [[large-language-models]], [[ai-safety-and-alignment]].
- **Patents**: 20-year monopoly on novel, non-obvious, useful inventions in exchange for
  disclosure; software claims must survive **Alice v. CLS Bank** (2014): abstract ideas
  implemented on a generic computer are unpatentable, an "inventive concept" is
  required — most pure-software patents issued before 2014 are now vulnerable; trolls
  (non-practicing entities), defensive portfolios, patent grants in Apache-2.0/GPLv3,
  OIN and LOT networks; prior-art searches before "inventing"; standards-essential
  patents and FRAND (codecs — the H.264/AV1 story).
- **Trade secrets**: information with economic value from being secret, protected by
  reasonable measures (NDAs, access control) — the DTSA (2016) and UTSA; Waymo v. Uber;
  the reason source code stays private and why leaving with a USB stick is a crime;
  vs patents: no term limit, no disclosure, but no protection against independent
  invention or reverse engineering (which is lawful absent contract/§1201).
- **Trademarks**: source identifiers (names, logos); distinct from code licenses; forks
  must rename ([[open-source-practice-and-governance]]); domain disputes (UDRP).

## Computer crime and security research (CFAA; Van Buren; disclosure norms)
**CFAA** (1986): crimes for accessing a computer "without authorization" or "exceeding
authorized access"; long stretched to cover ToS violations and scraping (Aaron Swartz,
2011–13); **Van Buren v. US** (2021): "exceeds authorized access" means accessing areas
(files, folders, databases) off-limits to you — a **gates-up-or-down** test — not
misusing access you have for an improper purpose; **hiQ v. LinkedIn** (2022): scraping
publicly available pages is not access "without authorization" (though contract/
copyright claims may remain); DOJ 2022 policy: good-faith security research is not to be
prosecuted; EU: Computer Misuse Act (UK), NIS2/Cyber Resilience Act obligations for
vendors. For practitioners: **authorization in writing** (scope, systems, dates, rules of
engagement) before any testing; bug bounties and **safe harbor** statements (disclose.io);
**coordinated disclosure** (report privately, agree a timeline — 90 days is customary,
CVE, publish after fix); wiretap and stored-communications laws constrain traffic
capture; anti-circumvention (§1201) constrains DRM research even with authorization —
[[security-principles]], [[web-security]]. ACM Code 2.8 mirrors this.

## Platforms, speech, accessibility, and everything else
- **Section 230** (US 1996): interactive services aren't treated as the publisher of
  third-party content and may moderate in good faith — the legal foundation of user-
  generated-content platforms; exceptions (federal crimes, IP, FOSTA); live debate on
  algorithmic amplification; EU **Digital Services Act** (notice-and-action, transparency,
  systemic-risk audits for very large platforms) and **Digital Markets Act** (gatekeeper
  interoperability, self-preferencing bans); the UK Online Safety Act; the First
  Amendment limits government mandates in the US (NetChoice cases).
- **Accessibility**: **ADA** Title III (public accommodations — courts and DOJ apply it
  to websites/apps; thousands of suits per year; DOJ's 2024 Title II rule adopts WCAG
  2.1 AA for state/local government), **Section 508** (federal procurement), the **European
  Accessibility Act** (2025, private-sector products and services), EN 301 549; **WCAG
  2.x AA** is the standard everywhere ([[html-css-and-the-dom]]) — accessibility is both
  a legal exposure and a design duty.
- **Export controls and encryption**: EAR/Wassenaar classify strong crypto and some
  security tools; open-source publication is largely exempt (post-"crypto wars", Bernstein
  v. DOJ) but distribution to embargoed countries and certain intrusion software are
  controlled; lawful-access/backdoor mandates recur (Apple v. FBI 2016, UK Investigatory
  Powers Act, EU "chat control") — [[cryptography-basics]].
- **Contracts and liability**: **EULAs/ToS** (enforceable when assented; unconscionable
  terms fail), open source disclaimers of warranty, **SLAs** with credits
  ([[site-reliability-engineering]]), limitation-of-liability clauses, indemnities in B2B
  deals, IP assignment and non-compete clauses in employment (FTC's 2024 non-compete
  ban was blocked; state law varies), product liability for software in physical
  products (cars, medical devices — FDA SaMD, Therac-25's legacy), the EU **Product
  Liability Directive** (2024) explicitly covering software and AI, and negligence
  standards ("reasonable security" — FTC, state AGs, the SEC's SolarWinds action).
- **AI regulation**: EU **AI Act** (2024): risk tiers — prohibited (social scoring,
  manipulative systems), high-risk (employment, credit, education, law enforcement:
  conformity assessment, documentation, human oversight, logging), transparency
  duties (chatbots, deepfakes), obligations for general-purpose models; US executive
  orders and state laws (Colorado AI Act), NIST AI RMF; sectoral rules (FDA, EEOC,
  CFPB adverse-action notices for algorithmic credit decisions) —
  [[ai-safety-and-alignment]], [[fairness-in-machine-learning]].

## Working with counsel
Flag the **triggers** early: personal data (esp. children, health, biometrics, location),
cross-border flows, copying/reimplementing/training on others' work, scraping or
accessing third-party systems, hosting user content, public-facing interfaces
(accessibility), cryptography distribution, safety-relevant products, automated
decisions about people. Bring the **facts** lawyers need: data flow diagrams, what is
stored where and how long, who can access, what the model was trained on, what the
user was told. Prefer designs that reduce legal surface (minimize data, don't store
what you don't need, log access, make deletion possible, keep provenance of training
data, clean-room reimplementations, written authorization) — the cheapest legal advice
is architecture. Don't rely on "everyone does it"; do rely on documented reasoning
(DPIAs, ADRs) — regulators and courts reward demonstrated diligence.

## Pitfalls
- Consent banners as a substitute for a lawful basis and minimization; collecting
  "just in case".
- "It's public" (scraping, face data) or "it's anonymized" as blanket defenses.
- Copying API/SDK code without a license; assuming Oracle v. Google settled API
  copyrightability; ignoring open source obligations in shipped products.
- Testing a system you weren't authorized to test; publishing a vulnerability without
  disclosure; DRM research without checking §1201 exemptions.
- Shipping an inaccessible interface; treating WCAG as optional polish.
- Discovering the legal trigger at launch review instead of at design.

## Related
- [[computing-ethics-and-professional-responsibility]], [[software-licensing]],
  [[differential-privacy]], [[fairness-in-machine-learning]], [[security-principles]],
  [[web-security]], [[cryptography-basics]], [[html-css-and-the-dom]] (accessibility),
  [[api-design]], [[large-language-models]], [[ai-safety-and-alignment]],
  [[open-source-practice-and-governance]], [[site-reliability-engineering]].

## Sources
GDPR (Reg. 2016/679) and EDPB guidelines; CCPA/CPRA; HIPAA, COPPA, FERPA, BIPA; FTC Act §5 enforcement; Nissenbaum 2004/2010 (contextual integrity); Sweeney 2000; Narayanan & Shmatikov 2008; 17 U.S.C. §§102, 107, 512, 1201; *Google LLC v. Oracle America* (2021); *Alice Corp. v. CLS Bank* (2014); Defend Trade Secrets Act 2016; *Van Buren v. United States* (2021); *hiQ Labs v. LinkedIn* (9th Cir. 2022); DOJ CFAA charging policy 2022; 47 U.S.C. §230; EU DSA/DMA (2022), AI Act (2024), Product Liability Directive (2024), European Accessibility Act; DOJ ADA Title II rule 2024; Quinn 2022 ch. 4–8; MIT 6.805 / *Blown to Bits* (Abelson, Ledeen & Lewis 2008/2021); Stanford CS181 (read: syllabus units); Samuelson 2021 (on Oracle v. Google).

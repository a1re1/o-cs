---
title: Software licensing — copyright as the default (all rights reserved; a license is permission), the Open Source Definition and the four freedoms, the license spectrum from permissive (MIT, BSD, Apache 2.0 with its patent grant) through weak copyleft (LGPL, MPL 2.0) to strong (GPLv3) and network copyleft (AGPLv3), what each requires (notices, disclose source, same license, state changes) and forbids (liability, warranty, trademark), compatibility and combining licenses, how licenses attach (LICENSE file, headers, SPDX identifiers, NOTICE), contributor agreements (CLA vs DCO), patents and trademarks, non-open "source-available" licenses (BSL, SSPL, Elastic) and relicensing, Creative Commons for content, public domain/Unlicense/CC0, and practical compliance (SBOM license scans, attribution, GPL obligations when distributing)
type: concept
section: "7.7"
level: 200
tags: [licensing, copyright, all-rights-reserved, license-grant, open-source-definition, osi, four-freedoms, fsf, permissive, mit, bsd, isc, apache-2, patent-grant, copyleft, weak-copyleft, strong-copyleft, network-copyleft, lgpl, mpl, gpl, gplv2, gplv3, agpl, tivoization, conditions, disclose-source, same-license, state-changes, notices, limitations, liability, warranty, trademark, license-compatibility, combining-licenses, spdx, license-file, headers, notice-file, cla, dco, sign-off, patents, trademarks, source-available, bsl, sspl, elastic-license, relicensing, dual-licensing, creative-commons, cc-by, cc-by-sa, cc0, public-domain, unlicense, compliance, license-scanning, attribution, distribution, saas-loophole, choosealicense]
sources: [open-source-practice-texts-and-seminal-papers]
summary: Software is copyrighted the moment it is written, so without a license nobody may legally copy, modify or redistribute it — a license is the grant of permission, and open source licenses (per the OSI definition and the FSF's four freedoms) grant everyone permission to use, modify and share for any purpose subject to conditions; choosealicense.com orders them by conditions: the Unlicense/CC0 (none — public domain dedication), MIT/BSD/ISC (keep the copyright and license notice), Apache 2.0 (notices, state changes, and an explicit patent grant with termination on patent litigation — why companies prefer it), MPL 2.0 (weak, file-level copyleft: modified files stay MPL, the larger work may be proprietary), LGPL (library copyleft: the library and its modifications stay open, programs linking through its interfaces need not), GPLv3 (strong copyleft: any distributed work containing GPL code must be distributed with complete source under the GPL — plus patent grant and anti-tivoization) and AGPLv3 (adds that offering the software as a network service counts as distribution, closing the SaaS loophole), all of which disclaim warranty and liability; compatibility follows the conditions (permissive code can go into copyleft projects, not the reverse; GPLv2-only and Apache 2.0 conflict, GPLv3 fixed it), and a project applies a license with a LICENSE file, SPDX identifiers in headers and a NOTICE file, decides whether contributors sign a CLA (grants the project rights to relicense — enabling later moves to source-available licenses, as Elastic, HashiCorp and Redis did, each provoking forks) or merely a DCO sign-off; patents (Apache/GPLv3 grants; MIT is silent), trademarks (separately protected — the name is not the code), and "source-available" licenses (BSL with a change date, SSPL, Elastic License, fair-source) that restrict competing services and are not open source by the OSI definition; content uses Creative Commons (BY, BY-SA, NC and ND variants, CC0); and compliance in practice means scanning dependencies' licenses (SBOMs), shipping attributions, honouring copyleft obligations when you distribute (binaries, containers, firmware — AGPL for services), and asking a lawyer before combining or changing licenses.
---
# Software licensing

**In one sentence.** Copyright means "no" by default; a license is the "yes" with
conditions — pick permissive when you want maximal adoption, copyleft when you want
derivatives to stay open, know that AGPL is the only one that reaches services, and
apply, combine and comply with licenses deliberately because the conditions are legal
obligations, not etiquette.

## Copyright, the definition, and the spectrum (OSI; FSF; choosealicense — read)
Code is a literary work: **copyright** attaches automatically to the author (or the
employer for work made for hire — check your employment agreement before publishing);
"all rights reserved" is the default; a **license** grants specified permissions under
**conditions** with **limitations** of liability. **Open Source Definition** (OSI, from
Debian's guidelines): free redistribution; source code available; derived works
allowed; integrity of the author's source (may require patches/renaming); no
discrimination against persons or fields of endeavour (so "no military use" or "no
commercial use" licenses are *not* open source); license not specific to a product or
restricting other software; technology-neutral. **Four freedoms** (FSF): run, study and
change, redistribute, distribute modified versions. Sorted by number of conditions
(choosealicense.com):

| License | Type | Conditions | Notes |
|---|---|---|---|
| Unlicense / CC0 / 0BSD | public-domain-like | none | some jurisdictions don't allow dedication; 0BSD is a safe zero-condition license |
| **MIT** / ISC / BSD-2/3 | permissive | keep copyright + license notice (BSD-3: no endorsement) | shortest; no patent language |
| **Apache 2.0** | permissive | notices, **state changes**, NOTICE file, **explicit patent grant** (terminates if you sue over patents) | preferred by companies; GPLv2-incompatible, GPLv3-compatible |
| **MPL 2.0** | weak copyleft (file) | modified *files* stay MPL and source disclosed; larger work may be proprietary | Firefox; "compatible" secondary licenses |
| **LGPL v3** | weak copyleft (library) | library + modifications stay LGPL; apps using it via its interfaces may be proprietary (dynamic linking or relinkable) | glibc uses LGPL v2.1 |
| **GPL v3** (v2) | strong copyleft | distribute complete corresponding source of the whole work under GPL; state changes; v3 adds patent grant, anti-**tivoization** (must be able to install modified versions on consumer devices), compatibility with Apache | Linux is GPLv2-only |
| **AGPL v3** | network copyleft | GPLv3 + **network use is distribution**: users interacting over a network must be able to get the source | closes the "SaaS loophole"; many companies ban AGPL dependencies |

All disclaim **warranty** and **liability**; Apache/MPL also deny **trademark** rights.
"Do anything" licenses (Fogel) vs the GPL is the first decision a project makes:
permissive maximizes adoption (and lets others close it — BSD → macOS); copyleft
guarantees downstream freedom (and deters some corporate use). Most new projects choose
MIT/Apache-2.0 (often dual "MIT OR Apache-2.0" in Rust for patent coverage + simplicity);
infrastructure with commercial pressure increasingly chooses AGPL or leaves open source.

## Compatibility and combining
You may combine works only if you can satisfy *all* their conditions on the combined
work: permissive → into anything; MPL files inside a GPL project (MPL 2.0 allows);
LGPL library linked by proprietary app (with relinking); **GPL is viral by design** — a
work containing GPL code that is *distributed* must be GPL as a whole (the FSF's view of
linking; static vs dynamic linking arguments are unsettled; separate processes over
pipes/network are generally separate works). **Incompatibilities**: GPLv2-only with Apache
2.0 (patent termination clause is an added restriction under v2 — Linux can't take
Apache code), GPL with CDDL (why ZFS isn't in mainline Linux), any copyleft with
proprietary distribution. Compatibility tables: FSF's license list, OSI, and SPDX
expressions (`MIT OR Apache-2.0`, `GPL-2.0-only WITH Classpath-exception-2.0`).
Distribution triggers obligations; **internal use** and **SaaS** do not (except AGPL) —
which is why the cloud era created AGPL and the source-available licenses.

## Applying a license; CLAs and the DCO; patents and trademarks (Fogel ch. 2, 9)
Put a `LICENSE` (exact text) at the root; `SPDX-License-Identifier: Apache-2.0` in file
headers (machine-readable — [[software-supply-chain-security]] SBOM tooling reads them);
a `NOTICE` for Apache attributions; `COPYING` for GPL; declare in package metadata
(`license` in package.json/pyproject/Cargo.toml). **Copyright holders**: individual
contributors keep copyright under inbound=outbound (the default: contributions under
the project license) unless a **CLA** (contributor license agreement — grants the
project/company broad rights, sometimes assignment) is required; CLAs enable
**relicensing** and dual licensing and are why Elastic (2021, to SSPL/Elastic License),
HashiCorp (2023, BSL → OpenTofu fork), and Redis (2024, RSALv2/SSPL → Valkey fork)
could change terms; the **DCO** (Developer Certificate of Origin — `Signed-off-by:`,
Linux kernel) is the lightweight alternative asserting you have the right to
contribute. **Patents**: MIT/BSD say nothing (implied license arguments only); Apache 2.0
and GPLv3 grant contributors' patents and terminate on litigation; patent trolls and
standards-essential patents are a separate risk. **Trademarks**: the name/logo is
protected independently of the code (Firefox/Iceweasel; Rust and Python trademark
policies); forks must rename; the license doesn't grant trademark use.

## Source-available, dual licensing, and the commercial edge
Not open source by the OSI definition but common: **BSL/BUSL** (MariaDB; production use
restricted for N years, then converts to an open license — "change date"), **SSPL**
(MongoDB; AGPL plus "release the entire service stack" — rejected by OSI), **Elastic
License 2.0**, **Functional Source License**, "fair-source", Commons Clause (added
non-compete restriction). **Dual licensing** (GPL + commercial — MySQL, Qt): copyleft
for the community, paid license for those who won't open their code. **Open core**: open
base, proprietary features/plugins. Trade-offs: source-available protects against
cloud providers reselling your work but forfeits the open-source label, distro
packaging, some contributors, and invites forks ([[open-source-practice-and-governance]]).
Reading a license summary is not reading the license; company policies (allow-lists,
AGPL bans) exist because obligations are real.

## Content, data, and models
**Creative Commons**: CC BY (attribution), BY-SA (share-alike — Wikipedia, this-style
wikis), BY-NC (non-commercial — *not* free-culture), BY-ND (no derivatives), CC0 (public
domain); not recommended for code. Data: ODbL, CDLA; models: "open weights" under
custom terms (Llama, RAIL) vs truly open (Apache-2.0 weights) — [[large-language-models]]
licensing debates; documentation often CC BY-SA or the code's license.

## Compliance in practice
Inventory dependencies and their licenses (SBOM tools: Syft, FOSSA, ScanCode; SPDX/
CycloneDX — [[dependency-management-and-packaging]]); policy: allow permissive, review
weak copyleft, restrict strong copyleft in distributed products, AGPL needs legal
sign-off; ship **attribution** (third-party notices in about pages/binaries — required by
MIT/BSD/Apache); when distributing GPL code (binaries, Docker images, embedded
firmware), provide source or a written offer and installation info (GPLv3); don't strip
headers; record license changes in the changelog; for your own project, choose early
(retrofitting requires every contributor's consent without a CLA). Ask counsel for
combinations, acquisitions (license audit), and anything involving patents.

## Pitfalls
- "No license" on GitHub ≠ free to use — it is all rights reserved.
- Copying MIT code without keeping the notice; removing headers.
- Believing SaaS avoids all copyleft (AGPL) or that dynamic linking always avoids GPL.
- Signing a CLA without reading it; relicensing "our" project without contributors'
  consent when there is no CLA.
- Using a NC or "ethical" license and calling it open source; picking a license by
  vibe rather than by intended freedoms.

## Related
- [[open-source-practice-and-governance]], [[dependency-management-and-packaging]],
  [[software-supply-chain-security]], [[computing-ethics-and-professional-responsibility]]
  (IP and professional duties), [[large-language-models]] (model licenses).

## Sources
choosealicense.com (read); Open Source Initiative, "The Open Source Definition"; FSF, "What is free software?" and license list; Fogel 2023 ch. 2, 9 (ToC read); Rosen 2004 (*Open Source Licensing*); GNU GPLv3/AGPLv3/LGPLv3 texts and FAQ; Apache License 2.0; MPL 2.0 FAQ; SPDX specification; Developer Certificate of Origin 1.1; OSI on SSPL (2021); Kuhn & Sandler, *Copyleft and the GNU GPL: A Comprehensive Tutorial*.

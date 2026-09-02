---
title: Open source practice & software ecosystems — Fogel's Producing Open Source Software (2e 2023, free; ToC read), Raymond's The Cathedral and the Bazaar (1997–99, free; "Release Early, Release Often" read), Eghbal's Working in Public (2020), OSI's Open Source Definition and choosealicense.com (read), the SLSA specification (read: levels), OpenSSF guides, Reproducible Builds (read: definition), SPDX and CycloneDX SBOM standards, Semantic Versioning 2.0.0, and Fowler/Preston-Werner on versioning
type: source
section: "7.7"
level: 300
tags: [fogel, producing-open-source-software, producingoss, raymond, cathedral-and-the-bazaar, catb, release-early-release-often, linus-law, eghbal, working-in-public, osi, open-source-definition, choosealicense, licenses, gpl, mit, apache, slsa, openssf, supply-chain, reproducible-builds, sbom, spdx, cyclonedx, semver, semantic-versioning, preston-werner, governance, community, maintainers]
sources: []
authors: [Karl Fogel, Eric Raymond, Nadia Eghbal, Open Source Initiative, OpenSSF, Reproducible Builds project, Tom Preston-Werner]
year: 2023
institution: Open Tech Strategies / OSI / OpenSSF / Linux Foundation
url: https://producingoss.com/
license: CC BY-SA (Fogel); OPL (Raymond); open specs
format: html
summary: Fogel's Producing Open Source Software (read: full table of contents) is the operating manual for running a free-software project — history and "free vs open source"; getting started (name, mission statement, license choice — "do anything" licenses vs the GPL, hosting, version control and bug tracker, communications, developer guidelines, documentation, setting the tone: avoid private discussions, nip rudeness in the bud, practice conspicuous code review, be open from day one); technical infrastructure (mailing lists/forums, version control vocabulary and pull requests, bug tracker hygiene, chat, wikis, translation); social and political infrastructure (forkability, benevolent dictators, consensus-based democracy, voting, adding maintainers, writing it all down, non-profits); organizations and money (corporate involvement, governments, contracting, transparency, funding non-programming work, open source quality assurance, "don't surprise your lawyers"); and later chapters on communications, packaging/releasing/daily development, managing participants, and licenses/copyrights/patents; Raymond's essay (read: "Release Early, Release Often" — Linus treating users as co-developers, kernel releases more than once a day in 1991, "given enough eyeballs, all bugs are shallow", the bazaar vs cathedral models, and the 19 lessons) is the founding text of the bazaar model; Eghbal's Working in Public documents how GitHub-era open source became a few maintainers serving many passive users ("stadiums" not "bazaars") and the resulting maintainer burnout and funding problem; the OSI definition and choosealicense.com (read: the license spectrum from AGPLv3 through GPLv3, LGPLv3, MPL 2.0, Apache 2.0, MIT/BSD to the Unlicense, with permissions/conditions/limitations per license) settle what "open source" and each license mean; SLSA (read: Build track levels L0–L3 — provenance exists, signed provenance from a hosted build platform, hardened builds) and the OpenSSF guides (Scorecard, Sigstore, best-practices badge) define supply-chain security, Reproducible Builds (read: definition — same source, build environment and instructions yield bit-for-bit identical output, enabling independent verification) the verification foundation, SPDX/CycloneDX the SBOM formats, and SemVer 2.0.0 the versioning contract.
---
# Open source practice & software ecosystems: sources

## What they are
- **Producing Open Source Software** (Fogel; read: ToC): 1 Introduction (history, free vs
  open source); 2 Getting Started (name, mission, license — "the 'do anything'
  licenses" and the GPL, hosting, VCS/bug tracker, guidelines, docs, **setting the tone**,
  be open from day one, announcing); 3 Technical Infrastructure (web site, canned hosting,
  forums/mailing lists, version control — vocabulary, branches, PRs/MRs, commit
  notifications; bug tracker; chat; wikis; translation; social networks); 4 Social and
  Political Infrastructure (forkability, benevolent dictators, consensus-based
  democracy, voting, vetoes, adding maintainers, non-profits); 5 Organizations and Money
  (corporate goals, governments, hiring from the community, contracting transparency,
  OSQA, legal); 6 Communications; 7 Packaging, Releasing, and Daily Development (release
  numbering, branches, stabilization, testing/release managers); 8 Managing
  Participants (delegation, praise/criticism, territoriality, difficult people,
  forks); 9 Legal Matters (licenses, copyright assignment/CLAs, patents, trademarks).
- **The Cathedral and the Bazaar** (Raymond 1997/99; read: §4): the fetchmail case
  study; lessons incl. "every good work of software starts by scratching a developer's
  personal itch", "good programmers know what to write; great ones know what to rewrite
  (and reuse)", "plan to throw one away", "treating your users as co-developers is your
  least-hassle route to rapid code improvement", **"release early, release often, and
  listen to your customers"**, **Linus's law** ("given a large enough beta-tester and
  co-developer base, almost every problem will be characterized quickly and the fix
  obvious to someone" — "given enough eyeballs, all bugs are shallow"), "smart data
  structures and dumb code works better", "the next best thing to having good ideas is
  recognizing good ideas from your users", "perfection is achieved when there is nothing
  more to take away". Companion essays: *Homesteading the Noosphere* (gift culture,
  ownership customs), *The Magic Cauldron* (economics).
- **Working in Public** (Eghbal 2020): a taxonomy — federations (Rust, Node), clubs
  (Astropy), toys, **stadiums** (one maintainer, huge audience — most popular npm
  packages); the shift from producing to maintaining; attention as the scarce resource;
  funding models (GitHub Sponsors, Open Collective, Tidelift, foundations).
- **Licensing**: OSI's Open Source Definition (10 criteria: free redistribution, source
  code, derived works, no discrimination, license not product-specific, technology-
  neutral…); choosealicense.com (read); Rosen's *Open Source Licensing*; the FSF's
  four freedoms; Creative Commons for non-code; "source-available"/BSL/SSPL as
  non-OSI.
- **Supply chain**: SLSA v1.0 (read: levels), OpenSSF Scorecard/Sigstore/best-practices,
  *Software Supply Chain Security* (Chainguard/OpenSSF free book), Reproducible Builds
  (read: definition), SPDX/CycloneDX (SBOM), CISA SBOM minimum elements, NIST SSDF;
  incidents: event-stream (2018), SolarWinds (2020), Log4Shell (2021), xz-utils (2024),
  polyfill.io (2024), ua-parser-js/colors/faker protestware.
- **Versioning/dependencies**: SemVer 2.0.0 (Preston-Werner); Hyrum's law
  ([[modularity-and-information-hiding]]); lockfiles; Go's minimal version selection
  (Cox 2018); the "left-pad" incident (2016).

## Key ideas → pages
[[open-source-practice-and-governance]], [[software-licensing]],
[[dependency-management-and-packaging]], [[software-supply-chain-security]]; existing:
[[git-data-model]], [[code-review]], [[continuous-integration-and-delivery]].

## What they add
Fogel is the practical how-to; Raymond the (contested) theory and the phrases everyone
quotes; Eghbal the corrective about who actually maintains the commons; the license
spectrum and SLSA levels are reference tables an agent should be able to cite exactly.

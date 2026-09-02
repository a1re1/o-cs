---
title: Open source practice and governance — free software vs open source, the bazaar model (release early and often, users as co-developers, Linus's law), starting and running a project (mission, license, hosting, communication channels, contribution workflow, code of conduct, setting the tone in public), governance models (benevolent dictator, consensus/lazy consensus, voting, steering committees, foundations), forkability as the ultimate check, maintainers and sustainability (Eghbal's stadiums, burnout, funding), corporate participation and open-core, contributing to others' projects (issues, PRs, etiquette), and releasing (versioning, branches, release managers)
type: concept
section: "7.7"
level: 300
tags: [open-source, free-software, four-freedoms, osi-definition, bazaar, cathedral, release-early-release-often, users-as-co-developers, linus-law, eyeballs, fogel, producing-oss, mission-statement, hosting, github, mailing-lists, contribution-workflow, contributing-md, pull-requests, issues, triage, code-of-conduct, setting-the-tone, public-discussion, conspicuous-code-review, be-open-from-day-one, governance, benevolent-dictator, bdfl, consensus, lazy-consensus, voting, steering-committee, tsc, foundations, apache-way, cncf, forkability, forks, maintainers, sustainability, burnout, funding, sponsors, open-collective, tidelift, eghbal, stadiums, federations, clubs, corporate-open-source, open-core, inner-source, relicensing, cla, dco, contributing, etiquette, releases, release-manager, stabilization-branch, lts, changelog, semver]
sources: [open-source-practice-texts-and-seminal-papers]
summary: Open source is both a licensing condition (the OSI definition: anyone may use, modify and redistribute the source for any purpose) and a development model — Raymond's bazaar, where releasing early and often and treating users as co-developers makes "all bugs shallow" given enough eyeballs, versus the cathedral of infrequent, polished releases — and Fogel's Producing Open Source Software turns it into practice: start with a clear mission statement, a license and a name you can own, a public repository with issue tracker and discussion channels, a CONTRIBUTING guide and a code of conduct, and set the tone by keeping technical discussion public, doing code review conspicuously, nipping rudeness early and being open from day one because waiting only creates an exposure event; governance decides who can merge and who decides when people disagree — a benevolent dictator (who governs by earned trust and can be forked), consensus with lazy-consensus defaults and votes as a last resort, elected steering committees, or a foundation (Apache, Linux Foundation/CNCF, Python SF) that holds trademarks and money — and forkability is the constitutional check that keeps every model honest; the sustainability problem (Eghbal's stadiums: one or two maintainers serving millions of passive users, drowning in issues and security reports) is addressed by triage discipline, saying no, growing maintainers deliberately, funding (sponsors, Open Collective, Tidelift, foundations, corporate employment) and by companies contributing upstream rather than forking, with open-core, relicensing to source-available licenses and CLAs as the recurring flashpoints; contributing well means reading the guidelines, filing reproducible issues, small focused PRs with tests, patience and courtesy; and releases follow a numbering scheme (SemVer), stabilization branches, release managers and changelogs so downstream users can depend on the project.
---
# Open source practice and governance

**In one sentence.** Open source works when a project is legally open (the license),
socially open (public discussion, conspicuous review, a way in for newcomers) and
constitutionally open (a governance model everyone can read, backed by the right to
fork) — and it fails, usually quietly, when a few unpaid maintainers carry a stadium
of users.

## Free software, open source, the bazaar (Fogel ch. 1; Raymond — read)
**Free software** (Stallman, FSF 1985): the four freedoms — run, study/modify, redistribute,
distribute modified versions — an ethical position; **open source** (OSI 1998): the same
licenses framed as a superior development method (the Open Source Definition's ten
criteria — [[software-licensing]]). Fogel: the split is about rhetoric more than
practice; today "the situation" is that open source underlies nearly all software, but
most projects are small and most users never contribute. **The bazaar** (Raymond 1997):
Linux showed that a loosely coordinated crowd releasing constantly could out-develop
the cathedral; the lessons that survived scrutiny — **release early, release often** (Linus
released kernels "more than once a day" in 1991; users as co-developers get "constant
stimulation and reward"); **Linus's law** ("given enough eyeballs, all bugs are shallow" —
true for *characterizing* bugs, overclaimed for *finding* them: Heartbleed and xz-utils
lived in heavily used code for years; eyeballs need incentives and tooling —
[[software-supply-chain-security]]); scratch your own itch; reuse and rewrite; smart
data structures, dumb code; recognize users' good ideas. Critiques: Bezroukov, and
Eghbal's data — most projects are not bazaars.

## Starting a project (Fogel ch. 2 — ToC read)
- **Name** you can own in the important namespaces (domain, package registry, repo,
  social); **mission statement** (one paragraph: what, for whom, why); state clearly that
  it is free/open source; features and requirements; **development status** that reflects
  reality; downloads/releases; **license** applied correctly (LICENSE file, headers,
  SPDX id — [[software-licensing]]).
- **Infrastructure** (ch. 3): a hosted forge (GitHub/GitLab/Codeberg — "canned hosting")
  with issues, PRs, CI, discussions; a mailing list or forum for design discussion (chat
  for real time, but decisions land in durable, searchable places); wiki/docs site;
  version control ([[git-data-model]]) — "version everything", use branches to avoid
  bottlenecks, singularity of information (one place per fact); bug tracker hygiene
  (templates, triage labels, pre-filtering); commit notifications; translation
  infrastructure.
- **Documentation**: README (what/why/quick start), user docs, **developer docs** (build,
  test, architecture — [[software-architecture-and-system-design]] design docs),
  **CONTRIBUTING.md** (workflow, style, DCO/CLA, review expectations), demos/screenshots.
- **Setting the tone**: avoid private discussions (decisions made in private must be
  re-made in public); **nip rudeness in the bud** (once, publicly, calmly); **practice
  conspicuous code review** (review in public, including your own core team's changes —
  it teaches norms and shows newcomers what to expect — [[code-review]]); a **code of
  conduct** (Contributor Covenant) with an enforcement path; **be open from day one** —
  "waiting just creates an exposure event" (a closed-then-opened project carries
  accumulated private context, hacks and embarrassments; opening a formerly closed
  project needs cleanup, license audit, and expectation setting); announce when there is
  something to try.

## Governance: who decides? (Fogel ch. 4; Apache; CNCF)
- **Benevolent dictator** (BD/BDFL — Linux, Python until 2018): final say rests with a
  founder whose authority is earned and *renewed* by good judgment; works when the BD
  delegates, listens, and rarely overrides; fails at succession (Python moved to a
  steering council).
- **Consensus-based democracy**: decisions by rough consensus among committers; **lazy
  consensus** ("silence is assent after N days") keeps velocity; **vote** only when
  consensus fails (define who votes — committers/PMC — and on what; polls vs binding
  votes; vetoes for code changes in Apache's model — a −1 with technical justification
  blocks); **write it all down** (governance doc, decision records — who can commit,
  release, add maintainers, and how).
- **Adding maintainers**: by demonstrated sustained contribution and judgment, nominated
  and confirmed; "not all maintainers are coders" (docs, triage, community); emeritus
  status; the bus factor ([[software-engineering-fundamentals]]).
- **Foundations** (Apache Software Foundation — "the Apache Way": community over code,
  PMCs, meritocracy; Linux Foundation/CNCF — technical steering committees, graduation
  levels, corporate members; Eclipse, Python SF, OpenJS, Rust Foundation): hold
  trademarks, money, legal protection, neutral ground for competitors; cost: process.
- **Forkability** is the constitutional backstop — anyone can take the code and the
  community elsewhere (LibreOffice from OpenOffice, MariaDB from MySQL, Valkey from
  Redis, OpenTofu from Terraform after relicensing); the *threat* of forking keeps
  leaders accountable; hostile forks are costly and rare, friendly forks (experiments,
  downstreams) are normal.

## Sustainability: maintainers, money, corporations (Eghbal; Fogel ch. 5, 8)
Eghbal's taxonomy by contributor/user growth: **federations** (many contributors, many
users — Rust, Kubernetes), **clubs** (many contributors, few users — niche communities),
**toys**, **stadiums** (few contributors, huge audience — most of npm/PyPI's most-depended-
on packages); GitHub lowered the cost of *using* and *asking* far more than of
*maintaining*, so the maintainer's scarce resource is attention — issue floods,
entitlement, security-report deadlines, CI bills. Practices: **triage** (templates,
bots, "needs-repro", close politely, `SECURITY.md`), **say no** (scope, roadmap), grow
co-maintainers, automate (CI, release bots, dependabot), set expectations (response
times; "maintained by volunteers"), take breaks, hand off or archive honestly. **Funding**:
GitHub Sponsors, Open Collective, Tidelift/Thanks.dev, foundations and grants (Sovereign
Tech Fund), paid support/consulting, corporate employment of maintainers (most large
projects are effectively company-staffed), dual licensing/open-core. **Corporate
participation** (Fogel ch. 5): state motives openly, "appear as many, not as one",
hire from the community and for the long term, contract transparently, contribute
upstream instead of carrying private forks ([[technical-debt-and-maintenance]] —
a private fork is debt with compound interest), fund non-programming work (docs, UX,
QA, legal). **Flashpoints**: **CLAs** (copyright assignment/licence grants enabling
relicensing — vs the lightweight **DCO** sign-off), **relicensing** to source-available
(Elastic 2021, HashiCorp 2023, Redis 2024 → forks), **open-core** boundaries, protestware
(colors/faker 2022), trademark policy. **Inner source**: applying these practices inside
a company (public-within-the-firm repos, contribution across team boundaries).

## Contributing to others' projects
Read CONTRIBUTING/CoC and recent PRs to learn norms; search before filing; file
**reproducible** issues (versions, minimal steps, expected vs actual —
[[delta-debugging-and-fault-localization]]); ask before large work (an issue proposing
the change); **small, focused PRs** with tests and a clear description; follow style and
commit conventions; respond to review promptly and without defensiveness; be patient
(maintainers are volunteers; "bump" is not a contribution); good first issues and docs
fixes are real contributions; security issues go through the private channel, not a
public issue. Maintainers, symmetrically: respond kindly, explain "no", give credit,
merge or close — don't leave PRs to rot.

## Releases (Fogel ch. 7)
**Version numbers** communicate compatibility — SemVer (`MAJOR.MINOR.PATCH`; breaking/
feature/fix — [[dependency-management-and-packaging]]) or CalVer; **release branches**
(stabilize `1.x` while `main` moves on; backport fixes; LTS lines); a **release manager**
role rotates; feature freeze → RC → release; changelog (Keep a Changelog; generated
from conventional commits), signed tags and artifacts ([[software-supply-chain-security]]),
reproducible builds, packaging for distros/registries, deprecation policy
([[api-design]]), and announcing. Daily development: pre-commit checks, CI on every PR
([[continuous-integration-and-delivery]]), "trunk is always releasable".

## Pitfalls
- Deciding in private and announcing in public; tolerating the brilliant jerk.
- No governance doc until the first real conflict; BDFL with no succession plan.
- Measuring health by stars; treating users' demands as obligations; maintainer
  burnout unnoticed until the archive notice.
- Corporate "open source" with no outside committers, a CLA that enables relicensing,
  and a surprise license change.
- PRs without an issue, tests, or a description; issues without reproductions.

## Related
- [[software-licensing]], [[dependency-management-and-packaging]],
  [[software-supply-chain-security]], [[git-data-model]], [[code-review]],
  [[continuous-integration-and-delivery]], [[software-engineering-fundamentals]],
  [[technical-debt-and-maintenance]], [[api-design]],
  [[delta-debugging-and-fault-localization]], [[software-architecture-and-system-design]],
  [[computing-ethics-and-professional-responsibility]].

## Sources
Fogel 2005/2023 (read: ToC) ch. 1–5, 7–9; Raymond 1997/1999 (read: "Release Early, Release Often"; lessons 1–19); Eghbal 2020; Apache Software Foundation, "The Apache Way"; CNCF governance templates; Python PEP 8016 (steering council); Contributor Covenant; Open Source Guides (opensource.guide, GitHub); Bezroukov 1999 (critique); Hoffmann, Nagle & Zhou 2024 (the value of open source, HBS).

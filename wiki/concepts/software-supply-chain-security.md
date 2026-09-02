---
title: Software supply chain security — the threat model (compromised source, build, dependencies, registry, distribution, and the humans in between; SolarWinds, event-stream, Log4Shell, xz-utils, polyfill.io, typosquatting and dependency confusion), SLSA levels and provenance (L1 provenance exists, L2 signed provenance from a hosted build, L3 hardened builds), Sigstore signing (cosign, Fulcio, Rekor) and attestations (in-toto), SBOMs (SPDX, CycloneDX) and vulnerability matching (CVE/OSV, VEX), reproducible builds (bit-for-bit identical artifacts from the same source, environment and instructions) and diverse double-compiling against trusting-trust attacks, dependency hygiene (lockfiles, pinning by digest, scanning, minimal dependencies, install-script caution), CI/CD hardening (least-privilege tokens, OIDC trusted publishing, pinned actions), OpenSSF Scorecard, and the maintainer side (2FA, security policy, coordinated disclosure)
type: concept
section: "7.7"
level: 400
tags: [supply-chain-security, supply-chain-attacks, threat-model, solarwinds, sunburst, event-stream, log4shell, log4j, xz-utils, xz-backdoor, polyfill-io, codecov, ua-parser-js, typosquatting, dependency-confusion, protestware, malicious-packages, slsa, provenance, build-provenance, slsa-levels, hosted-build, hardened-build, sigstore, cosign, fulcio, rekor, keyless-signing, transparency-log, attestations, in-toto, sbom, spdx, cyclonedx, cve, osv, vulnerability-scanning, vex, reproducible-builds, bit-for-bit, source-date-epoch, diverse-double-compiling, trusting-trust, thompson, dependency-hygiene, lockfiles, pin-by-digest, minimal-dependencies, install-scripts, ci-hardening, least-privilege-tokens, oidc, trusted-publishing, pinned-actions, github-actions-security, openssf, scorecard, best-practices-badge, 2fa, security-md, coordinated-disclosure, cvss, nist-ssdf, executive-order-14028]
sources: [open-source-practice-texts-and-seminal-papers]
summary: Supply-chain attacks compromise software before it reaches you — by injecting code into a dependency (event-stream 2018: a maintainer handed a popular npm package to a stranger who added a bitcoin-wallet stealer; ua-parser-js and colors/faker; polyfill.io 2024, a CDN domain bought and weaponized), into the build system (SolarWinds 2020: the build server inserted SUNBURST into signed Orion updates shipped to 18 000 customers; Codecov 2021: a modified uploader script exfiltrated CI secrets), into source via social engineering (xz-utils 2024: a multi-year persona became co-maintainer and hid an SSH backdoor in test files and build scripts, caught by a Postgres developer noticing 500 ms of latency), through registry tricks (typosquatting, dependency confusion where an internal package name is claimed publicly with a higher version), or by a vulnerability in a ubiquitous dependency (Log4Shell 2021) — so defenses must cover source, build, dependencies, distribution and people: SLSA's build track grades what you can prove about how an artifact was built (L1 provenance exists, L2 signed provenance from a hosted build platform that prevents tampering after the build, L3 hardened builds that prevent tampering during it), Sigstore makes signing routine (cosign signs artifacts with short-lived keys issued by Fulcio against an OIDC identity and records them in the Rekor transparency log, so verification checks "built by this workflow from this repo" without managing keys) and in-toto attestations carry the provenance, SBOMs (SPDX or CycloneDX) list what is inside an artifact so vulnerability databases (CVE, OSV) can be matched and VEX statements can say which findings actually apply, reproducible builds let independent parties rebuild and compare bit for bit (defeating a compromised builder, and diverse double-compiling defeats Thompson's trusting-trust compiler backdoor), dependency hygiene (lockfiles with hashes, pin by digest, minimal and vetted dependencies, no install scripts from strangers, scanners in CI, private registry scoping to block confusion) shrinks the attack surface, CI hardening (least-privilege short-lived tokens, OIDC trusted publishing instead of long-lived registry tokens, pinned third-party actions, no secrets in pull-request builds from forks) protects the build, and maintainers protect their side with 2FA, a SECURITY.md and coordinated disclosure, while OpenSSF Scorecard measures all of this automatically.
---
# Software supply chain security

**In one sentence.** Your software is everything you ship plus everything you pulled in
and every machine that touched it on the way; securing it means being able to prove
where each artifact came from (provenance, signatures, reproducibility), knowing what's
inside it (SBOM), pulling in as little as possible from people you can verify, and
locking down the build that assembles it.

## Threat model, by the incidents that defined it
- **Dependency compromise**: **event-stream** (npm, 2018; maintainer transfer → malicious
  `flatmap-stream` targeting a bitcoin wallet — 2 M weekly downloads); **ua-parser-js**,
  **coa**/**rc** (hijacked maintainer accounts, 2021); **colors/faker** protestware (2022);
  PyPI/npm malware waves (credential stealers in install scripts); **xz-utils** (2024;
  CVE-2024-3094: a persona ("Jia Tan") earned co-maintainership over two years, hid a
  backdoor in binary test files unpacked by the build, targeting `sshd` via
  systemd/liblzma linkage; found by Andres Freund investigating a 500 ms ssh login and
  valgrind noise days before it reached stable distros) — the social-engineering-of-
  maintainers threat ([[open-source-practice-and-governance]] sustainability).
- **Registry/naming**: **typosquatting** (`requets`), **dependency confusion** (Birsan 2021:
  publish `internal-lib` publicly at version 99 → resolvers prefer it), namespace
  takeovers (expired maintainer emails, deleted GitHub usernames), **polyfill.io**
  (2024: domain sold, CDN began serving malware to 100 k+ sites — third-party script
  inclusion — [[web-security]]).
- **Build compromise**: **SolarWinds** (2020; SUNSPOT implant on the build server
  swapped source during compilation → signed Orion updates with SUNBURST → US agencies,
  Microsoft, FireEye); **Codecov** (2021; Docker image credential leak → altered bash
  uploader exfiltrated CI env vars for months); **CircleCI** (2023) secrets breach;
  compromised GitHub Actions (tj-actions/changed-files 2025 — tags moved to malicious
  commits).
- **Vulnerable ubiquitous component**: **Log4Shell** (2021; JNDI lookup in log messages →
  RCE in an estimated 10 % of assets; the "who uses log4j?" scramble that made SBOMs
  policy), Heartbleed (2014, OpenSSL — two unpaid maintainers), Struts/Equifax (2017 —
  unpatched known CVE).
- **Trusting trust** (Thompson 1984): a compiler that inserts a backdoor when compiling
  the login program *and* when compiling itself — invisible in source; countered by
  **diverse double-compiling** (Wheeler 2009) and reproducible bootstraps
  ([[compilers-overview]]).
Assets to protect: source (repo, review), build (platform, dependencies fetched at
build time), artifact (registry, distribution channel), consumers' installs (scripts,
post-install), and credentials/people at each hop.

## SLSA: what can you prove about the build? (slsa.dev v1.0 — read)
**Provenance** = an attestation of "what entity built the artifact, what process they
used, what the inputs were". **Build track**: **L0** nothing; **L1 provenance exists** —
generated by the build process (prevents mistakes; forgeable); **L2 hosted build platform**
— provenance signed by a hosted platform (GitHub Actions, GitLab, Google Cloud Build)
so it can't be tampered with *after* the build; **L3 hardened builds** — the platform
prevents tampering *during* the build (isolated, ephemeral runners; secrets not
accessible to user-defined steps; provenance generated outside the user's control —
e.g., the `slsa-github-generator` reusable workflow). Consumers **define expectations**
(this package must come from repo X, workflow Y) and verify each artifact's provenance
against them; higher levels defeat more threats (tampered build, forged provenance,
modified artifact). Related: NIST SSDF, US EO 14028 (SBOMs for federal purchases),
OpenSSF **Scorecard** (automated checks: branch protection, pinned deps, signed
releases, fuzzing, SAST, token permissions, maintained), best-practices badge.

## Signing, attestations, transparency (Sigstore; in-toto)
**Sigstore**: **cosign** signs container images/blobs; **keyless** — a short-lived signing
certificate from **Fulcio** bound to an OIDC identity (a GitHub workflow, an email); the
signature and certificate are logged in **Rekor**, an append-only **transparency log**
(Merkle tree — [[hash-functions-cryptographic]]), so anyone can audit what was signed
when and revocation of long-lived keys is unnecessary; verification policy: "signed by
identity `https://github.com/org/repo/.github/workflows/release.yml@refs/tags/v*`".
npm and PyPI **provenance attestations** and **trusted publishing** (the registry accepts
uploads from a specific CI workflow via OIDC — no long-lived API tokens to leak).
**in-toto** attestations (statement + predicate: SLSA provenance, SBOM, vulnerability
scan, test results) chain the steps of a pipeline; **TUF** (The Update Framework)
secures update/registry metadata against rollback and key compromise (used by Rekor,
Docker Content Trust, PyPI plans). Package managers verify hashes from lockfiles
(`go.sum` + the Go checksum database — a transparency log of module hashes;
[[dependency-management-and-packaging]]).

## SBOMs, vulnerabilities, reproducibility — how do we find out fast whether a vulnerable library is deployed anywhere? (SPDX/CycloneDX; OSV; reproducible-builds.org — read)
**SBOM**: a machine-readable inventory of components (name, version, supplier, hashes,
dependency relationships, license) in **SPDX** (ISO 5962) or **CycloneDX** formats;
generated at build time (Syft, Trivy, cdxgen, `cargo sbom`) and shipped/attested with
the artifact; consumers match it against vulnerability databases — **CVE**/NVD, **OSV**
(open-source, precise version ranges), GitHub Advisories — with scanners (Grype, Trivy,
Dependabot, `npm audit`, `cargo audit`, `pip-audit`); **VEX** (vulnerability
exploitability exchange) lets producers say "affected / not affected because the
vulnerable function isn't reachable" to cut the noise (reachability analysis —
[[static-and-dynamic-analysis-tools]]); severity via CVSS, exploit likelihood via EPSS/
KEV; SLAs by severity. **Reproducible builds**: "given the same source code, build
environment and build instructions, any party can recreate bit-by-bit identical copies
of all specified artifacts" — requires eliminating variance (timestamps →
`SOURCE_DATE_EPOCH`, build paths, locales, archive metadata ordering, randomness,
parallelism order) and recording the environment; verified by hash comparison; enables
independent rebuilders (Debian ~95 % reproducible, Arch, F-Droid, NixOS, Go's
reproducible toolchain) so a single compromised builder is caught; **bootstrappable
builds** (build the toolchain from a tiny auditable seed) address trusting trust.
Hermetic build systems ([[build-systems-and-make]], Bazel, Nix) make reproducibility
the default.

## Dependency and CI hygiene (OpenSSF guides; GitHub Actions security hardening)
- **Dependencies**: lockfiles with integrity hashes committed and enforced in CI; pin
  base images and third-party actions **by digest/SHA**, not tag; minimal dependencies
  (audit transitive count; prefer stdlib); review new dependencies (maintainers,
  activity, 2FA, Scorecard) and diffs on updates (Socket, deps.dev); disable or sandbox
  **install scripts** (`npm ci --ignore-scripts`, pnpm's default block); private registry
  with **scoped names** and blocked public fallback to stop dependency confusion;
  automated upgrades with CI gates ([[continuous-integration-and-delivery]]); scan
  continuously; vendor only with a process.
- **CI/CD**: **least-privilege, short-lived tokens** (`permissions:` minimal per job;
  OIDC federation to clouds/registries — [[infrastructure-as-code-and-devops]]); never
  expose secrets to builds of pull requests from forks (`pull_request` vs
  `pull_request_target` footguns); ephemeral, isolated runners; protected branches with
  required review and signed commits; separate the build from the release/signing step;
  attest and sign every artifact; audit logs; secrets scanning (pre-commit, push
  protection) and rotation on leak.
- **Maintainers**: 2FA/hardware keys on registry and forge accounts; release from CI
  only (trusted publishing); `SECURITY.md` with a private reporting channel and a
  **coordinated disclosure** policy (embargo, CVE assignment via GitHub/MITRE, advisory,
  fixed versions, credit); vet new co-maintainers slowly (xz); sign tags; keep the bus
  factor > 1. **Consumers**: know your inventory (SBOMs for what you deploy), patch SLAs,
  and an incident playbook for "is log4j in anything we run?" that takes minutes, not
  weeks ([[observability-monitoring-and-incident-response]]).

## Pitfalls
- Trusting a green checkmark: a signature proves *who*, not *safe*; provenance without
  expectations verifies nothing.
- SBOMs generated once and never matched; scanners producing thousands of unreachable
  findings that get muted (use VEX/reachability).
- Long-lived registry tokens in CI; actions pinned to `@main`; secrets in fork PR builds.
- Pulling third-party scripts from CDNs at runtime (polyfill.io) without SRI.
- Treating the maintainer as the threat only — and not funding or vetting maintainers.

## Related
- [[dependency-management-and-packaging]], [[open-source-practice-and-governance]],
  [[software-licensing]], [[continuous-integration-and-delivery]],
  [[infrastructure-as-code-and-devops]], [[containers-and-kubernetes]],
  [[build-systems-and-make]], [[hash-functions-cryptographic]], [[public-key-cryptography]],
  [[security-principles]], [[web-security]], [[static-and-dynamic-analysis-tools]],
  [[compilers-overview]] (trusting trust), [[observability-monitoring-and-incident-response]].

## Sources
SLSA specification v1.0 (read: Security levels); Reproducible Builds project (read: Definitions); OpenSSF, *Software Supply Chain Security* (Chainguard, 2023), Scorecard, npm/PyPI best-practices guides; Sigstore documentation (cosign, Fulcio, Rekor); in-toto specification; SPDX 3.0 and CycloneDX 1.6; NIST SP 800-218 (SSDF); Thompson 1984 ("Reflections on Trusting Trust"); Wheeler 2009 (diverse double-compiling); Birsan 2021 (dependency confusion); Freund 2024 (xz backdoor disclosure); Ohm et al. 2020 (backstabber's knife collection — malicious package taxonomy); Ladisa et al. 2023 (supply-chain attack taxonomy, S&P); CISA SBOM minimum elements (2021).

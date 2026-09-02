---
title: Dependency management and packaging — what a package manager does (resolution, fetching, installing, building), semantic versioning and version constraints (caret/tilde/ranges), lockfiles and reproducible installs, dependency resolution (NP-hard in general, SAT/PubGrub solvers, Go's minimal version selection, npm's nested vs pnpm's content-addressed store, Python's pip/uv), the diamond dependency problem and one-version rules, transitive dependencies and the dependency graph, vendoring vs registries vs monorepos, updating dependencies (Dependabot/Renovate, upgrade cadence, breaking changes), publishing a package (metadata, entry points, ABI/API stability, deprecation), language ecosystems compared (npm, PyPI, crates.io, Maven, Go modules, Cargo, NuGet, apt/brew), and the left-pad lesson
type: concept
section: "7.7"
level: 300
tags: [dependency-management, package-manager, packaging, npm, pnpm, yarn, pip, uv, poetry, pypi, cargo, crates-io, maven, gradle, go-modules, nuget, apt, homebrew, nix, semver, semantic-versioning, caret, tilde, version-ranges, pinning, lockfile, package-lock, reproducible-installs, resolution, dependency-resolution, np-hard, sat-solver, pubgrub, minimal-version-selection, mvs, nested-node-modules, hoisting, content-addressed-store, diamond-dependency, one-version-rule, transitive-dependencies, dependency-graph, dependency-bloat, vendoring, registries, monorepo, updating-dependencies, dependabot, renovate, upgrade-cadence, breaking-changes, changelogs, publishing, package-metadata, entry-points, api-stability, abi, deprecation, yanking, left-pad, unpublish, phantom-dependencies, peer-dependencies, optional-dependencies, dev-dependencies, workspaces, lockfile-drift, hyrums-law]
sources: [open-source-practice-texts-and-seminal-papers]
summary: A package manager resolves the transitive dependency graph of a project to a concrete set of versions satisfying every constraint, fetches and verifies them from a registry, installs them into a layout the language's loader understands, and records the exact result in a lockfile so every machine installs the same thing — and each of those steps has a design space: versions follow semantic versioning (MAJOR for breaking, MINOR for compatible features, PATCH for fixes; `^1.2.3` accepts 1.x ≥ 1.2.3, `~1.2.3` accepts 1.2.x, `0.x` is unstable) which is a promise authors keep imperfectly (Hyrum's law) so lockfiles, not ranges, define reproducibility; resolution with ranges is NP-hard in general and modern tools use SAT-style or PubGrub solvers with good error messages (Cargo, uv, Dart), while Go's minimal version selection sidesteps it by picking the lowest version satisfying all requirements (deterministic, no lockfile solver, high-fidelity builds) and npm allows multiple versions of one package by nesting them in node_modules (avoiding diamond conflicts at the cost of duplication and phantom dependencies — pnpm's strict content-addressed store fixes both) whereas Maven and Go enforce one version per package; the diamond problem (A needs C v1, B needs C v2) is solved by nesting, by a one-version rule with coordinated upgrades (monorepos), or by breaking-change discipline; dependencies must be updated continuously in small steps (Dependabot/Renovate, CI on every bump, reading changelogs, upgrade before the version is EOL) because the cost of an upgrade grows with how long you waited; publishing a package means stable metadata, explicit entry points/exports, a compatibility policy and deprecation path, signed/provenance-attested releases, and never breaking consumers by unpublishing — the 2016 left-pad incident, where removing an 11-line package broke builds worldwide, taught registries immutability and taught consumers to weigh every dependency's maintenance, size and trust cost; vendoring or a monorepo trades registry convenience for control, and Nix-style content-addressed, hermetic builds are the end state of the reproducibility idea.
---
# Dependency management and packaging

**In one sentence.** Declare what you need loosely (ranges), resolve it once into an
exact, locked graph, install that identically everywhere, verify what you fetched, and
keep the whole graph moving forward in small, frequent, tested steps — while being
stingy about what you depend on at all.

## What a package manager does
1. **Resolve**: from the manifest's direct dependencies and constraints, find versions for
   the whole **transitive graph** that satisfy every constraint (below).
2. **Fetch** from a **registry** (npm, PyPI, crates.io, Maven Central, Go proxy, NuGet) or
   VCS/URL; **verify** integrity (hash in the lockfile; signatures/provenance —
   [[software-supply-chain-security]]).
3. **Install/link** into the layout the loader expects (`node_modules` tree, site-packages/
   virtualenv, `~/.cargo/registry` + compiled artifacts, Maven local repo, Go module
   cache); possibly **build** native extensions ([[build-systems-and-make]]).
4. **Record** the exact result in a **lockfile** (`package-lock.json`/`pnpm-lock.yaml`,
   `uv.lock`/`poetry.lock`, `Cargo.lock`, `go.sum`+`go.mod`, Gradle lockfiles) — commit
   it for applications; for libraries, commit it for CI reproducibility but consumers
   resolve their own.
Manifest vocabulary: dependencies vs **devDependencies** (build/test only), **peer
dependencies** (host must provide — plugins), optional deps, **workspaces** (monorepo
packages resolved locally), scripts/hooks (a supply-chain vector — `npm install` runs
arbitrary code), engines/python-requires.

## Semantic versioning and constraints (SemVer 2.0.0; Preston-Werner)
`MAJOR.MINOR.PATCH[-prerelease][+build]`: **MAJOR** for incompatible API changes, **MINOR**
for backward-compatible additions, **PATCH** for backward-compatible fixes; `0.y.z` means
anything may change (Cargo treats `0.y` as the major); pre-releases sort before the
release. Constraints: exact `=1.2.3`, **caret** `^1.2.3` (≥1.2.3 <2.0.0 — npm/Cargo
default), **tilde** `~1.2.3` (≥1.2.3 <1.3.0), ranges `>=1.2,<2`, wildcards, Python's
compatible-release `~=1.2`; Go modules require ≥ a version and use the *major* in the
import path (`/v2`) so majors are different packages. SemVer is a promise, and
**Hyrum's law** ([[modularity-and-information-hiding]]) says every observable behaviour
is depended on, so a "patch" can still break someone — which is why applications pin via
lockfiles and test upgrades, and libraries state ranges to allow deduplication. CalVer
(`2024.06`) for things where compatibility isn't the point (Ubuntu, pip). Authors:
document a compatibility policy, keep changelogs (Keep a Changelog; conventional
commits → automated release notes), and treat removing/renaming anything public as a
major ([[api-design]]).

## Resolution: solvers, MVS, nesting (Cox 2018; PubGrub; npm/pnpm docs)
With ranges and transitive constraints, finding a satisfying assignment is **NP-hard**
(reduction from 3-SAT — [[np-completeness-and-reductions]]); in practice graphs are
benign and solvers are fast but need good **conflict explanations**: **PubGrub** (Dart's
pub; adopted by uv, Cargo's resolver improvements, Poetry) does CDCL-style learning
with human-readable derivations ("A 1.0 depends on B ^2, but C needs B ^1"); apt/Conda
use SAT/SMT ([[sat-and-smt-solvers]]); pip's backtracking resolver (2020) replaced
"first wins". **Minimal version selection** (Go): each module lists minimum required
versions; the build uses, for each dependency, the *maximum of the minimums* across the
graph — no ranges, no solver, deterministic and reproducible without a lockfile solver
(`go.sum` only verifies hashes), upgrades are explicit (`go get -u`), and builds don't
silently change when a new version is published (high-fidelity builds); costs — you
don't get the newest patch automatically, and the ecosystem must keep majors as
separate paths. **Multiple versions vs one version**: npm nests conflicting versions
(`node_modules/a/node_modules/c`) and **hoists** compatible ones to the top — flexible,
but duplicates code (bundle bloat), permits **phantom dependencies** (importing something
you never declared because hoisting exposed it), and lets two copies of a singleton
coexist (React "invalid hook call"); **pnpm** stores each version once in a content-
addressed store and links a strict tree (no phantoms; Yarn Berry's PnP similar); Cargo
allows multiple *semver-incompatible* versions of a crate (types don't unify); Maven,
Go, Python allow **one version per package** — the **diamond problem** (A→C v1, B→C v2)
must be resolved by picking one (Maven's nearest-wins is order-dependent — dangerous),
by MVS, or by upgrading A/B. Google's/Bazel monorepo **one-version rule**: exactly one
version of every third-party package in the repo, upgraded atomically for everyone —
no diamonds, at the cost of coordinated upgrades ([[technical-debt-and-maintenance]] LSCs).

## Living with dependencies
- **Choosing**: every dependency is code you run and must maintain the relationship with —
  weigh maintenance activity, bus factor, size (transitive count!), license
  ([[software-licensing]]), security history, and whether 30 lines of your own code would
  do (the **left-pad** lesson: an 11-line package's removal in 2016 broke thousands of
  builds; `is-odd` exists). `npm ls`, `cargo tree`, `pipdeptree` to see the graph;
  bundle analyzers for size ([[web-performance-and-browser-networking]]).
- **Updating**: continuous small upgrades (Dependabot/Renovate PRs grouped by cadence,
  CI green before merge — [[continuous-integration-and-delivery]]) beat annual big-bang
  upgrades whose cost compounds; read changelogs for majors; keep runtimes within
  support windows; pin actions/base images by digest; **lockfile drift** (lockfile not
  matching manifest) fails CI (`npm ci`, `uv sync --locked`, `cargo --locked`).
- **Vendoring** (copying sources into the repo — Go's `vendor/`, Chromium, many
  monorepos): reproducibility and offline builds, visible diffs, no registry
  dependency; costs repo size and manual updates; **private registries/proxies** (Artifactory,
  Nexus, Go proxy) cache and control what enters the org. **Monorepo** workspaces make
  internal dependencies just paths and enforce one version.
- **Environments**: virtualenvs/`uv`/`nvm`/`asdf`/`mise` per project; Docker for full
  reproducibility ([[containers-and-kubernetes]]); **Nix**/Guix: every package built in a
  hermetic sandbox from a hash of *all* inputs — reproducible, multiple versions
  coexisting, rollbacks ([[software-supply-chain-security]] reproducible builds).
- **Publishing**: stable name (own it early — [[open-source-practice-and-governance]]),
  metadata (license, repository, description, keywords), **entry points/exports** map
  (ESM/CJS dual packages; `exports` field restricts deep imports = smaller public
  surface), types shipped, minimal files in the tarball, semver discipline, deprecate
  before removing (`npm deprecate`, `cargo yank` — yanking hides but doesn't delete;
  registries now forbid unpublishing after 72 h/if depended upon), 2FA/trusted
  publishing (OIDC from CI) and provenance attestations, changelog and migration guide
  per major; **ABI stability** for compiled libraries (symbol versioning, soname) — a
  separate, harder promise than API stability.

## Ecosystems at a glance
npm/pnpm/yarn (JS: nested versions, scripts, huge graphs); pip + venv/**uv**/Poetry/
PDM (Python: wheels vs sdists, `pyproject.toml`, one version per env, PEP 440/508
specifiers, uv's PubGrub and lockfile); **Cargo** (Rust: `Cargo.toml/lock`, crates.io
immutable, features, semver-aware multi-version, `cargo audit`); **Go modules** (MVS,
proxy + checksum DB, `go.sum`, major in path); Maven/Gradle (JVM: coordinates
`group:artifact:version`, nearest-wins vs Gradle conflict resolution, BOMs, Maven
Central immutable + signed); NuGet (.NET, lockfile optional, central package
management); system packages — apt/dnf (distro-curated, SAT resolution, security
backports), Homebrew (formulae, bottles); Conda (binary science stack, SAT/libmamba);
Nix (hermetic). Shared trends: lockfiles everywhere, immutable registries, provenance,
workspaces, and faster Rust-written tools (uv, pnpm's successors, Bun).

## Pitfalls
- No lockfile in an application; `npm install` in CI instead of `npm ci`; floating
  `latest` tags.
- Phantom dependencies; two React copies; nearest-wins surprises in Maven.
- Waiting years to upgrade; ignoring deprecation warnings until removal.
- Depending on trivial packages; ignoring transitive count and install scripts.
- Publishing without `exports`/a compatibility policy; unpublishing; reusing a version
  number with different contents.

## Related
- [[software-supply-chain-security]], [[software-licensing]],
  [[open-source-practice-and-governance]], [[build-systems-and-make]],
  [[modularity-and-information-hiding]] (Hyrum's law), [[api-design]],
  [[technical-debt-and-maintenance]], [[continuous-integration-and-delivery]],
  [[containers-and-kubernetes]], [[np-completeness-and-reductions]], [[sat-and-smt-solvers]],
  [[web-performance-and-browser-networking]].

## Sources
Preston-Werner, SemVer 2.0.0; Cox 2018 ("Version SAT", "Minimal Version Selection", Go & Versioning series); PubGrub (Dart, 2018) and uv's resolver docs; npm, pnpm, Cargo, pip/PEP 440/508/517/518/621, Go modules, Maven documentation; Abate et al. 2012 (dependency solving is NP-complete; OPIUM/MANCOOSI); the left-pad incident (2016, Koçulu/npm); Winters et al. 2020 ch. 21 (dependency management; one-version rule); Fogel 2023 ch. 7 (ToC read); Dolstra 2006 (Nix).

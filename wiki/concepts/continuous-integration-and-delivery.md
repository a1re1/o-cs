---
title: Continuous integration and continuous delivery — trunk-based development and small batches, the deployment pipeline (commit stage, automated acceptance, capacity, production), build once and promote the same artifact, fast feedback and the ten-minute build, keeping the main branch green (pre-submit checks, merge queues, flaky-test quarantine), deployment strategies (blue-green, canary and progressive rollout, rolling, feature flags and dark launches, rollback), release vs deploy, database migrations (expand–contract), the DORA metrics and why speed and stability are not a trade-off, and CI at scale (hermetic builds, caching, test selection, monorepo pipelines)
type: concept
section: "7.4"
level: 300
tags: [continuous-integration, continuous-delivery, continuous-deployment, ci, cd, ci-cd, trunk-based-development, small-batches, batch-size, deployment-pipeline, commit-stage, acceptance-tests, build-once, artifact-promotion, immutable-artifacts, fast-feedback, ten-minute-build, green-main, pre-submit, presubmit, merge-queue, flaky-tests, quarantine, blue-green, canary, progressive-rollout, rolling-update, feature-flags, feature-toggles, dark-launch, rollback, roll-forward, release-vs-deploy, decouple-deploy-release, database-migrations, expand-contract, backward-compatible-schema, dora-metrics, lead-time, deployment-frequency, change-fail-rate, recovery-time, humble-farley, if-it-hurts-do-it-more-often, hermetic-builds, build-caching, test-selection, monorepo, pipelines-as-code, github-actions, gitlab-ci, jenkins, bazel, semantic-versioning, release-engineering]
sources: [devops-cicd-and-sre-texts-courses-and-seminal-papers]
summary: Continuous integration means every change is merged to the shared main branch at least daily and verified by an automated build and test run within minutes, so integration problems surface in small, attributable increments instead of in a "merge hell" phase; continuous delivery (Humble & Farley) extends that to keeping the software always in a deployable state through a deployment pipeline — a commit stage (compile, unit tests, static checks, ~10 minutes), automated acceptance tests, capacity and exploratory stages, and production — through which one immutable artifact, built once, is promoted with only configuration varying per environment, so that releases become routine, low-risk, on-demand events ("if it hurts, do it more often") rather than code-freeze-and-hardening rituals; the supporting practices are trunk-based development with short-lived branches, pre-submit checks and merge queues that keep main green, aggressive treatment of flaky tests, hermetic and cached builds, and test selection so pipelines stay fast at scale; deployment strategies separate deploying code from releasing features — blue-green (two environments, switch traffic, instant rollback), rolling updates, canary and progressive rollouts (a small percentage of traffic, compared against baseline on SLO metrics, then widened — the SRE Workbook's canarying), feature flags and dark launches (code in production but off, per-cohort enablement, kill switches) — with rollback or roll-forward planned before every deploy and database changes made backward-compatible via expand–migrate–contract so that old and new code coexist; and the payoff is measured by DORA's metrics (change lead time, deployment frequency, failed-deployment recovery time, change fail rate, rework rate), on which the research consistently finds that high performers deploy more often and fail less — speed and stability are not opposed, because small batches are both faster and safer.
---
# Continuous integration and delivery

**In one sentence.** Merge small changes to main many times a day, verify each in
minutes with an automated pipeline, build one artifact and promote it unchanged
through environments, and release by shifting traffic or flipping flags — so that
deploying becomes boring, rollback trivial, and the batch size small enough that when
something breaks you know exactly what.

## Why: small batches, and the research (continuousdelivery.com — read; Accelerate)
"Continuous delivery is the ability to get changes of all types — new features,
configuration changes, bug fixes and experiments — into production, or into the hands of
users, safely and quickly in a sustainable way" by ensuring the code is "always in a
deployable state, even in the face of teams of thousands of developers making changes
on a daily basis", eliminating "the integration, testing and hardening phases that
traditionally followed 'dev complete', as well as code freezes." Benefits: low-risk
releases (blue-green, zero downtime), faster time to market (no weeks-long
integrate/test/fix phase), higher quality (regressions found in minutes, humans freed
for exploratory/usability/performance/security testing), lower costs (fixed release
costs automated away), better products (small batches → feedback → A/B tests; "the 2/3
of features we build that deliver zero or negative value"), happier teams (less
burnout, more contact with users). The **batch-size** argument (Reinertsen): smaller
batches reduce cycle time, variability, risk, and the cost of diagnosing failures
(a failed deploy of one change is self-explanatory). **DORA** (Forsgren, Humble & Kim;
metrics guide read): throughput — **change lead time** (commit → production), **deployment
frequency**, **failed-deployment recovery time**; instability — **change fail rate**,
**deployment rework rate**; elite performers deploy on demand, lead time < 1 h, recover in
< 1 h, fail rate ~5 %; "speed and stability are not tradeoffs … the metrics are
correlated" — [[software-engineering-fundamentals]] for measuring productivity.

## Continuous integration: keeping main green (Fowler 2006; SWE at Google ch. 23)
Practices: single shared **main/trunk**; everyone integrates at least daily
(**trunk-based development**; branches live hours to a day or two; long-lived feature
branches are the anti-pattern — [[git-data-model]]); every commit triggers an automated
build + tests on a clean agent; fix a broken build immediately (nobody merges onto a red
main); the **ten-minute build** (split into commit-stage fast tests and later slow
tests); test in a production-like environment; everyone can see results; automate
deployment. Mechanics at scale: **pre-submit/pre-merge** checks (build, unit tests,
linters, static analysis — [[static-and-dynamic-analysis-tools]] — on the proposed merge
commit, not the branch tip), **merge queues** (serialize merges, test each against the
true future main, batch and bisect — GitHub merge queue, Bors, Zuul), **post-submit**
continuous builds with automatic culprit finding (bisect the batch —
[[delta-debugging-and-fault-localization]]); **hermetic builds** (pinned toolchains and
dependencies; [[build-systems-and-make]]) with **remote caching** and **test selection**
(run only tests affected by the change — Bazel's dependency graph; TAP at Google), test
**sharding**; **flaky tests** quarantined and fixed, never retried into green
([[software-testing-fundamentals]]); **pipelines as code** (YAML in the repo — GitHub
Actions, GitLab CI, Buildkite, Jenkinsfile, Tekton/Argo), ephemeral, containerized
agents ([[containers-and-kubernetes]]). Security in CI: least-privilege tokens, pinned
actions, no secrets in logs, provenance/SBOM (supply chain — [[security-principles]]).

## The deployment pipeline (Humble & Farley ch. 5)
```
commit stage (≤10 min)      → automated acceptance tests → capacity/perf tests → manual/exploratory (optional) → production
compile, unit, lint, SA;      end-to-end on prod-like env;   load, soak;                 UAT, security review;         deploy on demand
produce ONE versioned artifact ────────────── same artifact promoted, only config changes per environment ──────────────▶
```
Principles: **build once** — the binary/container image tested in staging is byte-for-
byte what ships (immutable artifacts in a registry, tagged with the commit); **deploy
the same way everywhere** (one scripted mechanism for dev, test, prod — drift between
environments is the classic "works in staging"); **configuration** externalized
(environment variables, config service; Twelve-Factor) and versioned; **smoke tests**
after every deploy; **everything in version control** — code, tests, pipeline, infra
([[infrastructure-as-code-and-devops]]), schema migrations; the pipeline is the only
route to production. **Continuous deployment** = every green commit auto-deploys;
**continuous delivery** = every commit *could* be deployed, a human/business decision
triggers it. **Release engineering** (SRE ch. 8): self-service releases, high velocity,
hermetic builds, policy enforcement (signed, auditable), reproducible versions.

## Deploy ≠ release: strategies (SRE Workbook ch. 16; Humble & Farley ch. 10)
- **Rolling update**: replace instances gradually (Kubernetes Deployments —
  `maxSurge`/`maxUnavailable`); needs N and N+1 to coexist.
- **Blue-green**: two full environments; deploy to idle one, run smoke tests, switch the
  router; rollback = switch back; costs double capacity; database shared → schema
  compatibility required.
- **Canary** and **progressive delivery**: route 1 % → 5 % → 25 % → 100 % of traffic
  (or one region/cell) to the new version; compare **canary vs baseline** (same size,
  same age, same traffic — the Workbook's methodology) on SLO indicators (error rate,
  latency percentiles, CPU) with statistical care ([[hypothesis-testing-and-confidence-intervals]]);
  automated analysis (Kayenta/Spinnaker, Argo Rollouts, Flagger); abort automatically
  on regression. Choosing canary population and duration: enough traffic to detect the
  regression sizes you care about; long enough to cover periodic behaviour.
- **Feature flags / toggles**: deploy dark, enable per user cohort, percentage, region;
  **kill switches** for instant disable without deploy; separate *release* toggles
  (short-lived — remove them, [[technical-debt-and-maintenance]]), *experiment* toggles
  (A/B), *ops* toggles (circuit breakers, load shedding — [[microservices-and-resilience-patterns]]),
  *permission* toggles; flags multiply test configurations — test the on/off combos that
  ship.
- **Dark launches / shadow traffic**: new path receives copies of production traffic,
  results discarded and compared.
- **Rollback vs roll-forward**: rollback must be tested and fast (previous artifact +
  compatible schema); roll-forward with a fix when rollback would lose data. **Data
  migrations**: **expand–migrate–contract** — add the new column/table (compatible with old
  code), deploy code that writes both/reads new, backfill, then remove the old — never a
  single-step breaking migration; migrations versioned and run by the pipeline; large
  tables online (`pt-online-schema-change`, gh-ost).
- **Launch coordination** (SRE ch. 27): checklists, capacity, dependencies,
  gradual ramps, rollback plans, comms.

## Pitfalls
- Long-lived branches merged in big bangs; broken main tolerated; CI that takes an hour.
- Different artifacts per environment (rebuild for prod); config baked into images;
  secrets in the repo.
- Canaries without a baseline (comparing new 1 % against 99 % old at different ages/
  loads); canaries too small/short to detect anything.
- Feature flags never removed; untested flag combinations; migrations that break the
  previous version (so rollback is impossible).
- Measuring deploys per day without change-fail rate — or vice versa.

## Related
- [[infrastructure-as-code-and-devops]], [[containers-and-kubernetes]],
  [[observability-monitoring-and-incident-response]], [[site-reliability-engineering]],
  [[chaos-engineering-and-reliability-testing]], [[software-testing-fundamentals]],
  [[unit-testing]], [[build-systems-and-make]], [[git-data-model]],
  [[static-and-dynamic-analysis-tools]], [[microservices-and-resilience-patterns]],
  [[technical-debt-and-maintenance]], [[software-engineering-fundamentals]],
  [[delta-debugging-and-fault-localization]], [[hypothesis-testing-and-confidence-intervals]].

## Sources
Humble & Farley 2010 (ch. 3–5, 10, 12); continuousdelivery.com (read); Forsgren, Humble & Kim 2018; DORA metrics guide (read); Fowler 2006 ("Continuous Integration"), 2010 ("Feature Toggles" — Hodgson 2017), 2010 ("BlueGreenDeployment"); Beyer et al. 2016 ch. 8, 27 (ToC read); Beyer et al. 2018 (Workbook) ch. 16 (ToC read); Winters et al. 2020 ch. 23–24; Reinertsen 2009; Wiggins 2011 (Twelve-Factor).

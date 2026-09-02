---
title: Technical debt and software maintenance — Cunningham's metaphor and its abuse, kinds of debt (deliberate/inadvertent, prudent/reckless — Fowler's quadrant), interest and principal, Lehman's laws and why systems rot, maintenance categories (corrective, adaptive, perfective, preventive) and their share of cost, legacy code and characterization tests (Feathers), refactoring vs rewriting (the second-system trap, strangler fig), dependency and version upgrades (Hyrum's law, large-scale changes), deprecation, documentation debt, measuring debt (hotspots, churn × complexity), and paying it down as a budgeted practice
type: concept
section: "7.1"
level: 300
tags: [technical-debt, cunningham, debt-metaphor, interest, principal, deliberate-debt, inadvertent-debt, prudent-reckless, fowler-quadrant, maintenance, software-evolution, lehmans-laws, software-rot, bit-rot, corrective, adaptive, perfective, preventive, maintenance-cost, legacy-code, feathers, characterization-tests, seams, refactoring, rewrite, big-rewrite, second-system, strangler-fig, incremental-migration, dependency-upgrades, hyrums-law, large-scale-changes, lsc, deprecation, dead-code, documentation-debt, code-hotspots, churn, complexity-metrics, cyclomatic, code-ownership, boy-scout-rule, tech-debt-budget, architecture-erosion, feature-flags, toil]
sources: [software-engineering-texts-courses-and-seminal-papers]
summary: Technical debt (Cunningham 1992) is the metaphor for the cost of choosing an expedient design now — the "principal" is the work to fix it, the "interest" the extra effort every subsequent change pays until it's fixed — and Fowler's quadrant separates prudent-deliberate debt (ship now, fix next quarter — a legitimate financing decision) from reckless debt ("we don't have time for design") and from inadvertent debt (we didn't know better then; the design we'd choose now, having learned) which is unavoidable and healthy if paid; the underlying dynamics are Lehman's laws — a system in use must keep changing, and its complexity grows unless deliberate work reduces it — which is why maintenance is 60–80 % of lifetime cost, split into corrective (bugs), adaptive (new platforms, dependencies, regulations), perfective (new features, performance) and preventive (refactoring, upgrades) work; legacy code is code without tests (Feathers), attacked by finding seams, writing characterization tests that pin current behaviour, and then refactoring in small steps; rewrites are the tempting trap (Brooks' second-system effect, Netscape) and the strangler-fig pattern — route traffic to new components one at a time behind the old interface — is the survivable alternative; dependency upgrades are maintenance's largest recurring bill because Hyrum's law guarantees every upgrade breaks someone, so large organizations invest in large-scale-change tooling, one-version policies and deprecation as a first-class process with owners, timelines and migration tools; debt is measured where it hurts — hotspots of high churn × high complexity, long lead times, flaky tests, on-call toil — and paid down as an explicit budget (a fraction of every sprint, the boy-scout rule, dedicated fixit weeks) rather than as an apology.
---
# Technical debt and maintenance

**In one sentence.** Every shortcut and every decision that the world has since
invalidated charges interest on each future change; maintenance is the majority of
software's cost because Lehman's laws guarantee the changes keep coming, so the craft is
to take debt deliberately, keep it visible, and pay it down on a budget — with tests,
seams, incremental migration, and tooling for the upgrades that never stop.

## The metaphor and its quadrant (Cunningham 1992; Fowler 2009; McConnell)
Cunningham: "Shipping first-time code is like going into debt. A little debt speeds
development so long as it is paid back promptly with a rewrite … The danger occurs when
the debt is not repaid. Every minute spent on not-quite-right code counts as interest."
**Principal** = cost to fix; **interest** = extra cost on every change made while it stands
(and the bugs it breeds). Fowler's quadrant: **deliberate–prudent** ("we must ship now and
deal with consequences" — a financing decision, recorded), **deliberate–reckless** ("we don't
have time for design"), **inadvertent–reckless** ("what's layering?"), **inadvertent–prudent**
("now we know how we should have done it" — unavoidable; the sign of a team learning).
Abuses: calling all bad code "debt" (some is just bad), using the metaphor to excuse never
paying, or to demand a rewrite. Debt lives in code, tests (missing/flaky), architecture
(erosion), dependencies (outdated), documentation, infrastructure, and data models;
**intentional** debt should be tracked like a loan (a ticket with the interest rate: what
it slows down).

## Why systems rot: Lehman and maintenance economics (Lehman 1980; Sommerville ch. 9)
**Lehman's laws** ([[software-engineering-fundamentals]]): E-type systems must change to
stay useful (I) and grow in complexity unless work is done to reduce it (II); growth is
steady (VI) and quality declines unless adapted (VII). Maintenance therefore dominates:
60–80 % of lifetime cost in most studies; categories — **corrective** (bug fixes, ~20 %),
**adaptive** (new OS/platform/dependency/regulation, ~25 %), **perfective** (features,
performance, ~50 %), **preventive** (refactoring, upgrades, cleanup — the one that's cut
first and costs most when skipped). **Software rot / bit rot**: nothing changes in the code
and it stops working — because dependencies, platforms, certificates, data formats, and
assumptions changed around it ([[dependency-management-and-packaging]]); **architecture
erosion**: the implemented structure drifts from the intended one (cyclic dependencies,
layer violations) until "the architecture" is a slide nobody's code matches. Feedback
that keeps rot in check: tests, CI ([[continuous-integration-and-delivery]]), static analysis,
code ownership, and someone whose job includes preventive work
([[site-reliability-engineering]] treats operational **toil** the same way).

## Legacy code: tests first, then change (Feathers 2004)
"Legacy code is code without tests." Changing it safely: identify the **change point**;
find **seams** (places where behaviour can be altered without editing the code —
parameters, virtual methods, link-time substitution, preprocessor) to break dependencies
so the unit can be instantiated in a test harness (the "sprout method/class" and "wrap
method" moves to add new code without touching old); write **characterization tests** —
pin the *current* behaviour, including the bugs, as the regression net (golden files,
approval tests, snapshot tests); then refactor in small verified steps ([[refactoring]],
[[unit-testing]]); use the compiler/type system as a lever (lean on types to find all call
sites — [[type-systems]]); scratch refactoring to learn, then revert. Understanding comes
before changing: read the tests, the version history ([[git-data-model]] — `git blame`/`log
-S`), and the hotspots; write the missing docs as you learn.

## Refactor vs rewrite (Brooks; Spolsky 2000; Fowler)
"The single worst strategic mistake … is to decide to rewrite the code from scratch"
(Spolsky on Netscape 6): old code is ugly because it has absorbed years of bug fixes and
edge cases that a rewrite must rediscover; the **second-system effect** loads the rewrite
with every deferred wish; feature freeze during the rewrite hands the market to
competitors. **Refactoring** (behaviour-preserving, test-backed, continuous — [[refactoring]])
([[fowler-refactoring]]) is the default; when the architecture truly must change, migrate **incrementally**: the
**strangler fig** (put a facade in front, route one capability at a time to the new
implementation, retire the old when nothing routes to it), **branch by abstraction**
(introduce an abstraction over the old component, implement the new one behind it, flip),
**parallel run** (new and old both compute; compare), **feature flags** for staged rollout
([[continuous-integration-and-delivery]]), and **expand–migrate–contract** for schema changes
([[database-schema-evolution]]). Rewrites are justified when the runtime/language is
dead, the old system cannot be tested at all, or scale requires a different architecture —
and even then, incrementally.

## Upgrades, deprecation, and large-scale change (SWE at Google ch. 15, 21–22)
Dependencies are the biggest recurring maintenance bill: security patches, EOL runtimes,
breaking API changes; **Hyrum's law** means every upgrade breaks some consumer, so the
cost is proportional to how long you waited (the compiler-upgrade lesson: upgrade often,
in small steps, with tests that catch behavioural changes). Practices: pin versions but
update continuously (Dependabot/Renovate), **one-version rule** in monorepos (no diamonds),
vendoring vs package managers, semantic versioning as a promise, tests at the boundary.
**Deprecation** as a process: advisory (warnings, docs) → compulsory (deadline, owners
migrate or are migrated); deprecating without a migration path just creates two supported
versions; the deprecating team pays for migration tooling. **Large-scale changes (LSCs)**:
automated refactors across millions of lines (codemods, Rosie/Refaster, clang-tidy
fixits), split into per-owner shards, reviewed by tooling plus local approval — the
mechanism that makes API evolution in a 2-billion-line monorepo possible. **Dead code**
deletion is maintenance's highest-return activity (no tests to run, no bugs to fix).
**Documentation debt**: stale docs are worse than none; docs live with code, have owners,
and are reviewed ([[code-review]]).

## Measuring and budgeting (Tornhill; Accelerate; Sculley et al. 2015)
Find debt where it hurts: **hotspots** = files with high **churn** (commits) × high
**complexity** (indentation/cyclomatic — a proxy that works); lead time for changes in a
module; defect density; test flakiness and CI time; on-call toil hours; "how long does a
new engineer take to make a change here"; architecture-conformance checks (dependency
rules in CI). ML systems have their own debts (entanglement, data dependencies, glue
code — [[mlops-and-ml-systems]]). Pay-down as a **budget**: 10–20 % of each iteration for
preventive work, the **boy-scout rule** (leave the code cleaner than you found it — small,
continuous), dedicated fix-it weeks for cross-cutting debt, and debt items prioritized by
interest paid (hotspots first), with the business case stated in lead time and risk, not
aesthetics. Governance: code ownership (someone accountable per module), review standards
([[code-review]]), architecture decision records so future maintainers know *why*
([[modularity-and-information-hiding]] design docs).

## Pitfalls
- Calling every ugly line "debt" and every rewrite "paying it down".
- Taking debt without recording it (invisible interest); never scheduling repayment.
- The big rewrite; feature freeze; rediscovering old bug fixes.
- Refactoring legacy code without characterization tests; "cleaning up" behaviour that
  users depend on (Hyrum).
- Deferring upgrades until they are impossible; deprecations with no owner or tooling.
- Measuring debt by opinion instead of churn/complexity/lead time.

## Related
- [[software-engineering-fundamentals]], [[modularity-and-information-hiding]],
  [[refactoring]], [[unit-testing]], [[code-review]], [[git-data-model]],
  [[continuous-integration-and-delivery]], [[dependency-management-and-packaging]],
  [[database-schema-evolution]], [[developer-tooling-and-workflow]],
  [[site-reliability-engineering]], [[mlops-and-ml-systems]], [[type-systems]],
  [[design-patterns-catalog]].

## Sources
Cunningham 1992 (OOPSLA experience report); Fowler 2009 ("Technical Debt Quadrant"); McConnell 2007; Lehman 1980; Feathers 2004 (*Working Effectively with Legacy Code*); Spolsky 2000 ("Things You Should Never Do"); Fowler 2004 (strangler fig), 2018 (*Refactoring* 2e); Winters, Manshreck & Wright 2020 ch. 15, 21–22 (ToC read); Tornhill 2015 (*Your Code as a Crime Scene*); Forsgren et al. 2018; Sommerville 10e ch. 9; Sculley et al. 2015.

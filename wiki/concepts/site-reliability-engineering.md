---
title: Site reliability engineering — SLIs/SLOs and error budgets, toil, monitoring and alerting, on-call and incident response, postmortems, release engineering, load balancing and overload, cascading failures
type: concept
section: "4.8"
level: 400
tags: [sre, site-reliability-engineering, sli, slo, sla, error-budget, availability, nines, toil, automation, monitoring, four-golden-signals, alerting, on-call, incident-management, incident-command, postmortems, blameless, release-engineering, canary, rollback, feature-flags, capacity-planning, load-balancing, overload, load-shedding, retries, backpressure, cascading-failures, chaos-engineering, disaster-recovery, data-integrity, runbooks, change-management]
sources: [datacenter-and-sre-books]
summary: SRE is Google's answer to running warehouse-scale services — software engineers own reliability with an explicit contract: service level indicators measured against objectives (e.g. 99.9 % of requests under 300 ms), an error budget (1 − SLO) that is spent on launches and change velocity and, when exhausted, freezes releases; toil (manual, repetitive, automatable work) capped at 50 % of time; monitoring on the four golden signals (latency, traffic, errors, saturation) with alerts on symptoms that need a human now; on-call with bounded load, runbooks, and a structured incident command; blameless postmortems that turn every outage into action items; release engineering with hermetic builds, canaries, staged rollouts and fast rollback; capacity planning and load balancing (DNS/anycast at the front, weighted round-robin and least-loaded in the datacenter with subsetting); and defenses against overload and cascading failure — per-client quotas, criticality, adaptive throttling, retry budgets, load shedding, and never retrying into a saturated backend.
---
# Site reliability engineering

**In one sentence.** Decide how reliable the service must be, measure it, spend the gap on
change, and make every outage cheaper than the last.

## The contract: SLIs, SLOs, error budgets (SRE ch. 3–4)
**SLI**: a measured quantity (fraction of successful requests, fraction under a latency
threshold, freshness, durability). **SLO**: a target on an SLI over a window (99.9 % of
requests succeed per 30 days ≈ 43 minutes of full outage). **SLA**: the business contract with
consequences. 100 % is the wrong target (users can't tell past the next weakest link; each nine
costs ~10×). **Error budget** = 1 − SLO: product and SRE agree that the budget funds risk —
launches, experiments, planned maintenance; when it's spent, releases slow until it recovers.
This aligns developers (velocity) and operators (stability) with one number. Measure at the
user (black-box probes) and inside (white-box metrics); percentiles not means
([[tail-latency-at-scale]]).

## Toil and automation (ch. 5, 7)
**Toil**: manual, repetitive, automatable, tactical, no enduring value, scales with service
size. Cap at 50 % of SRE time; the rest is engineering that removes toil (automation,
self-healing, better tooling). Automation ladder: none → externally maintained scripts →
service-owned tooling → autonomous systems; automate the *system*, not the *task*.

## Monitoring and alerting (ch. 6, 10)
**Four golden signals**: latency (successful and failed separately), traffic, errors,
saturation (how full — plus prediction). Alerts (page now) vs tickets (act soon) vs logs
(diagnose later); page on symptoms tied to SLOs (burn rate — "budget will be gone in N hours"),
not on causes; every page must be actionable and novel; dashboards for the rest
([[cluster-scheduling-and-observability]]).

## On-call, incidents, postmortems (ch. 11–15)
On-call: bounded (≤ 25 % time, ≤ 2 events per shift), runbooks, escalation, compensation;
**incident management**: roles (incident commander, operations lead, communications lead,
planning), a live document, hand-offs, declare early; **troubleshooting**: hypothesize/test/
treat, look at recent changes first (most outages follow a change). **Blameless postmortem**:
timeline, impact, root causes and triggers, what went well/badly, action items with owners,
published widely — errors are systemic, blame hides information (Allspaw). Practise with
DiRT/game days, chaos engineering (Netflix), fault injection ([[distributed-systems-basics]]).

## Change: releases and capacity (ch. 8, 18, 27)
Hermetic, reproducible builds ([[build-systems-and-make]]); config as code and reviewed;
**canary** a small fraction, watch SLIs, staged rollout, **fast rollback** (rollback is a
feature — always available, always tested); feature flags decouple deploy from release;
launch checklists. Capacity planning: organic growth + launches + redundancy (N+2), regular
load tests, ordering lead times; demand forecasting.

## Load balancing, overload, cascading failure (ch. 19–22)
Front end: DNS with geo/anycast, then L4/L7 balancers (Maglev, consistent hashing —
[[consistent-hashing]], [[dns-http-and-the-web-stack]]); in the datacenter: **subsetting**
(each client talks to a deterministic subset of backends), weighted round robin by
backend-reported load, least-loaded; health checking with lame-duck states. **Overload**: cap
per-client quotas, classify request **criticality**, **adaptive throttling** on the client
(reject locally when the backend's rejection rate rises), **load shedding** (serve degraded
results, drop low-criticality), keep serving *some* of the traffic well rather than all of it
badly; retries with budgets (≤ 10 % of requests), jittered backoff, per-request retry limits,
and *never* retry into a backend already rejecting for overload. **Cascading failures**: one
overloaded server dies, its load lands on the others, they die — causes: resource exhaustion
(CPU, memory, threads, file descriptors), slow dependencies, retries; prevention: load tests
to failure, queue limits, timeouts shorter than the caller's, circuit breakers, graceful
degradation, capacity headroom; recovery: reduce load (drop traffic), then add capacity,
restart in waves ([[queueing-theory]]).

## Data integrity (ch. 26)
Backups are not the goal; **restores** are; defense in depth — soft deletion, backups plus
replication (they protect against different failures), out-of-band validation; test restores
regularly ([[raid-and-erasure-coding]], [[distributed-file-and-object-storage]]).

## Pitfalls
- Alerting on every anomaly (pager fatigue); SLOs set without user data; 100 % availability
  goals.
- Postmortems that blame or that produce no action items; runbooks that rot.
- Retry storms and thundering herds after an outage; rollback that has never been exercised.
- Toil accepted as the job; heroics rewarded instead of automation.

## Related
- [[cluster-scheduling-and-observability]], [[tail-latency-at-scale]], [[warehouse-scale-computing]],
  [[distributed-systems-basics]], [[queueing-theory]], [[cloud-and-serverless]],
  [[consistent-hashing]], [[build-systems-and-make]], [[debugging]].

## Sources
Beyer et al., Site Reliability Engineering (2016) ch. 3–8, 10–15, 18–22, 26; The Site Reliability Workbook (2018); Building Secure and Reliable Systems (2020); Allspaw "Blameless PostMortems"; Nygard, Release It!.

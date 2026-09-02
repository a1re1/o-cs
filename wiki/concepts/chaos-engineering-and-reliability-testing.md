---
title: Chaos engineering and testing for reliability — the Principles of Chaos (steady-state hypothesis, real-world event variables, disproving the hypothesis, run in production, automate, minimize blast radius), Netflix's Chaos Monkey/Kong/FIT/ChAP, Google DiRT and game days, fault injection (latency, errors, resource exhaustion, dependency failure, region loss), the reliability testing hierarchy (SRE ch. 17: unit → integration → system → production/canary/disaster testing), load and capacity testing, canary analysis, disaster-recovery testing (restore drills, failover exercises), resilience patterns as the fixes, and how to start safely
type: concept
section: "7.4"
level: 400
tags: [chaos-engineering, principles-of-chaos, steady-state, hypothesis, real-world-events, run-in-production, automate-experiments, blast-radius, chaos-monkey, chaos-kong, simian-army, fit, chap, netflix, basiri, rosenthal, dirt, disaster-recovery-testing, game-days, fault-injection, latency-injection, error-injection, resource-exhaustion, dependency-failure, region-failure, az-failure, kill-instances, network-partition, clock-skew, gremlin, litmus, chaos-mesh, aws-fis, toxiproxy, testing-for-reliability, sre-ch17, production-testing, canary, load-testing, stress-testing, soak-testing, capacity-testing, performance-regression, dr-drills, backup-restore, failover-exercise, rpo-rto, resilience-patterns, circuit-breaker, fallbacks, retries, timeouts, cascading-failures, confidence]
sources: [devops-cicd-and-sre-texts-courses-and-seminal-papers]
summary: Chaos engineering is "the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production" — because even when every service works, their interactions plus rare real-world events (crashed servers, failed disks, severed networks, retry storms from mistuned timeouts, overloaded dependencies, cascading failures from a single point of failure) make distributed systems chaotic — and it proceeds as an experiment: define steady state as a measurable system output (throughput, error rate, latency percentiles — not internal attributes), hypothesize it will hold in both a control and an experimental group, introduce variables that reflect real-world events prioritized by impact or frequency, and try to disprove the hypothesis by looking for a steady-state difference; the advanced principles are to build hypotheses around steady-state behaviour, vary real-world events, run experiments in production (the only environment with real traffic and real dependencies), automate them to run continuously, and minimize blast radius (small cohorts, kill switches, business-hours runs); Netflix's Chaos Monkey (randomly terminating instances so teams design for it), Chaos Kong (evacuating a region), FIT (fault injection at the request level: latency and failures for chosen services and user cohorts) and ChAP (automated experiments comparing a canary cluster with injected faults to a baseline on business metrics, aborting on deviation), and Google's DiRT (company-wide disaster and recovery testing exercises) are the reference practices; the broader reliability-testing hierarchy (SRE ch. 17) runs from unit and integration tests through system, performance/load/soak/capacity tests, canary releases and production testing to disaster-recovery drills — restoring from backups, failing over regions, exercising RPO/RTO — plus game days that rehearse the humans; what chaos finds gets fixed with the resilience patterns (timeouts, retries with backoff, circuit breakers, bulkheads, fallbacks, load shedding, redundancy across failure domains), and the way to start is small: one service, one hypothesis, staging first, then production with a tiny blast radius and an abort button.
---
# Chaos engineering and testing for reliability

**In one sentence.** You don't know your system is resilient until you have broken it
on purpose and watched the steady state hold — so inject the failures the world will
inject anyway, in production, with a small blast radius and a hypothesis, and fix what
falls over before a customer finds it.

## The principles (principlesofchaos.org — read; Basiri et al. 2016)
Definition: "the discipline of experimenting on a system in order to build confidence in
the system's capability to withstand turbulent conditions in production." Motivation:
"even when all of the individual services in a distributed system are functioning
properly, the interactions between those services can cause unpredictable outcomes";
systemic weaknesses — "improper fallback settings when a service is unavailable; retry
storms from improperly tuned timeouts; outages when a downstream dependency receives
too much traffic; cascading failures when a single point of failure crashes."
**The experiment**: (1) define **steady state** as a measurable output that indicates
normal behaviour; (2) hypothesize it continues in both control and experimental group;
(3) introduce **variables reflecting real-world events** (servers crash, disks fail,
network severed); (4) try to **disprove** the hypothesis by a difference in steady state.
"The harder it is to disrupt the steady state, the more confidence we have."
**Advanced principles**: **build a hypothesis around steady-state behaviour** (system
output — throughput, error rate, latency percentiles — not internals; "verifies that the
system does work, rather than trying to validate how it works"); **vary real-world
events** (prioritize by potential impact or estimated frequency: hardware failures,
software failures like malformed responses, non-failure events like traffic spikes and
scaling; any event capable of disrupting steady state is a candidate); **run experiments
in production** (systems behave differently with real traffic and dependencies; the
only way to build confidence in the system that matters); **automate experiments to run
continuously** (manual experiments don't scale; automate orchestration and analysis);
**minimize blast radius** (experiments can hurt — contain and limit fallout while still
learning). Chaos is not random breakage: it is controlled, hypothesis-driven, measured.

## Reference practices (Netflix; Google DiRT)
**Chaos Monkey** (2011): randomly terminates production instances during business
hours so every service is designed to survive instance loss (autoscaling groups,
stateless, no pets); the **Simian Army** added Latency Monkey (injected delays — retired:
too coarse), Conformity/Security/Janitor monkeys, **Chaos Gorilla** (AZ failure) and
**Chaos Kong** (evacuate an AWS region — exercised regularly; Netflix survived real
region outages). **FIT** (Failure Injection Testing, 2014): inject latency or failure into
specific service calls for a chosen cohort (device, user id, percentage) via request
headers propagated through the stack — precise, scoped experiments; **ChAP** (Chaos
Automation Platform, 2017): for a target dependency, spin up a **canary** cluster with
injected failure and a **baseline** cluster, route a small slice of traffic to each,
compare on the key business metric (streams-per-second) with automated statistical
analysis, **abort** on deviation, run continuously — chaos as a CI stage. **Google DiRT**
(Disaster Recovery Testing, 2006–): annual multi-day company-wide exercises — simulated
data-centre loss, network partitions, "the on-call is unreachable", fictional
scenarios — testing technical failover *and* human processes (who has the keys? does
the runbook exist? — [[observability-monitoring-and-incident-response]]); ~90 % of
issues are process/communication. **Game days** (Amazon; Allspaw): scheduled,
announced failure exercises with the team in a room; blameless review after. Tools:
Gremlin, AWS Fault Injection Simulator, Chaos Mesh / LitmusChaos (Kubernetes —
[[containers-and-kubernetes]] pod kill, network delay/loss, CPU/memory stress, DNS
failure, clock skew), Toxiproxy (TCP-level latency/failure for local tests), Istio fault
injection (HTTP delays/aborts by route), `tc netem`.

## What to inject (the failure catalogue)
Infrastructure: instance/pod termination, AZ/region loss, disk full/slow, memory
pressure/OOM, CPU steal, clock skew ([[distributed-systems-basics]] — time is a
dependency), certificate expiry; network: added latency (the most revealing — exposes
missing timeouts), packet loss, partition, DNS failure, bandwidth caps; dependencies:
5xx/timeouts/malformed responses from a specific downstream, slow database, cache
eviction/flush (thundering herd — [[scalable-system-design]]), message broker lag or
duplication (at-least-once — idempotency), third-party API outage; load: traffic spikes,
hot keys, retry storms (does load shedding hold?); process: config push errors, a bad
deploy (does the canary catch it? — [[continuous-integration-and-delivery]]), on-call
unavailable. Prioritize by frequency × impact and by what your **resilience patterns**
claim to handle ([[microservices-and-resilience-patterns]]: does the circuit breaker
actually open? does the fallback serve? do timeouts fire before the caller's deadline?
does the bulkhead prevent thread exhaustion? — a pattern never exercised is a
hypothesis, not a defence). Cascading failures (SRE ch. 22): a failed instance shifts
load to others, which fail — test that load shedding and graceful degradation kick in.

## Testing for reliability: the wider hierarchy (SRE ch. 17; Workbook ch. 16)
Traditional tests ([[software-testing-fundamentals]]): unit → integration → system
(smoke, performance, regression). Production tests: **canary** (roll to a small slice,
compare against baseline, promote — the reliable way to test in prod), **configuration
tests** (config files validated and tested like code), **stress/load** (find the knee and
the failure mode — does it degrade or collapse?), **soak** (hours/days — leaks, slow
growth), **capacity** tests (N+2 planning: can you lose a region and a machine and still
serve at peak? — [[site-reliability-engineering]]), **performance regression** in CI
([[profiling-and-performance]]); **disaster recovery drills**: restore from backup
regularly (a backup never restored is a hypothesis — SRE ch. 26 data integrity),
failover to the secondary region on a schedule (and fail *back*), measure achieved
**RPO/RTO** against targets, rotate the people who do it; **fuzzing** for
robustness of parsers and APIs ([[fuzzing]]); **fault-injection tests** at the unit level
(mock dependencies that time out/throw — the cheapest chaos). Statistical care in
comparing canary/baseline ([[hypothesis-testing-and-confidence-intervals]]): equal-sized,
same-age cohorts, enough traffic, pre-registered metrics.

## How to start, safely
1. Pick a service with an SLO and good telemetry (you need a steady-state metric —
   [[observability-monitoring-and-incident-response]]). 2. Write the hypothesis ("if the
   recommendations service returns 500s, the home page still renders with the fallback
   row and p99 stays < 400 ms"). 3. Run in staging first, then production during business
   hours with the team watching, a **tiny blast radius** (1 % of traffic, one instance, one
   AZ), an **abort/kill switch**, and stakeholders informed. 4. Observe; if the hypothesis
   is disproved, you found a bug — fix it (add timeout, fallback, redundancy); if not,
   widen the radius next time. 5. Automate the ones that matter into a scheduled/CI
   experiment; add new event types from every postmortem ("could we have found this with
   an experiment?"). Culture: blameless, opt-in first, then organization-wide expectations
   (e.g., "every tier-1 service survives instance and AZ loss, verified monthly").

## Pitfalls
- Random breakage without a hypothesis or steady-state metric ("chaos" without
  engineering).
- Only in staging — dependencies, traffic and data differ; or in production without a
  kill switch/blast-radius limit.
- Injecting outright failure only; latency and partial degradation find more bugs.
- Never testing restores/failover; DR plans that exist only on paper.
- Treating a surviving experiment as proof; treating a disproved one as someone's fault.

## Related
- [[site-reliability-engineering]], [[microservices-and-resilience-patterns]],
  [[observability-monitoring-and-incident-response]], [[continuous-integration-and-delivery]],
  [[containers-and-kubernetes]], [[infrastructure-as-code-and-devops]],
  [[software-testing-fundamentals]], [[fuzzing]], [[distributed-systems-basics]],
  [[scalable-system-design]], [[profiling-and-performance]],
  [[hypothesis-testing-and-confidence-intervals]].

## Sources
Principles of Chaos Engineering (2019 revision; read); Basiri, Behnam, de Rooij, Hochstein, Kosewski, Reynolds & Rosenthal 2016 (IEEE Software); Rosenthal & Jones 2020 (*Chaos Engineering*, O'Reilly); Netflix Tech Blog (Chaos Monkey 2011, FIT 2014, ChAP 2017); Krishnan 2012 ("Weathering the unexpected", CACM — DiRT); Beyer et al. 2016 ch. 17, 22, 26 (ToC read); Beyer et al. 2018 (Workbook) ch. 16 (ToC read); Allspaw 2012 (game days); Gremlin documentation.

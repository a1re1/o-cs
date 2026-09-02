---
title: Observability, monitoring & incident response — metrics/logs/traces and what "observability" adds (high-cardinality, arbitrary questions), the four golden signals and RED/USE, Prometheus-style metrics (counters, gauges, histograms, labels, cardinality), structured logging and sampling, distributed tracing and OpenTelemetry, dashboards and SLO burn-rate alerting (alert on symptoms, page only on user-visible urgent problems), on-call design, incident management (incident command, roles, comms, severity), troubleshooting method, blameless postmortems and action items, runbooks, and the observability cost problem
type: concept
section: "7.4"
level: 400
tags: [observability, monitoring, telemetry, metrics, logs, traces, three-pillars, high-cardinality, wide-events, four-golden-signals, latency, traffic, errors, saturation, red-method, use-method, prometheus, counters, gauges, histograms, summaries, labels, cardinality-explosion, percentiles, structured-logging, log-levels, log-sampling, distributed-tracing, spans, trace-context, opentelemetry, otel, jaeger, dapper, dashboards, grafana, alerting, symptom-based-alerting, cause-based, alert-fatigue, slo-alerting, burn-rate, multi-window, paging, tickets, on-call, on-call-rotation, incident-management, incident-command, incident-commander, roles, severity-levels, status-page, communication, troubleshooting, hypothesis-driven, postmortem, blameless, action-items, runbooks, playbooks, mttr, mttd, observability-cost, sampling, retention, profiling-continuous]
sources: [devops-cicd-and-sre-texts-courses-and-seminal-papers]
summary: Monitoring tells you whether the system is healthy against known failure modes; observability (borrowed from control theory) is the property of being able to ask arbitrary new questions of the system from its externally emitted telemetry without shipping new code — in practice metrics (cheap, aggregated time series: counters, gauges, histograms with labels, mind the cardinality), logs (discrete structured events, sampled at volume), and traces (a request's path across services as a tree of spans propagated by trace context — Dapper's idea, standardized by OpenTelemetry), increasingly unified as wide, high-cardinality events; the SRE book's four golden signals (latency, traffic, errors, saturation) and the RED (rate, errors, duration per service) and USE (utilization, saturation, errors per resource) methods say what to measure, dashboards show it, and alerting follows the rules that pages go only for urgent, user-visible, actionable symptoms (alert on SLO burn rate with multi-window thresholds, not on every cause), everything else becomes a ticket, and alert fatigue is a system failure to be fixed; on-call is engineered (bounded shifts, page volume caps, compensation, escalation, handoffs) and incidents are run with an explicit command structure (incident commander, operations lead, communications lead; severity levels; a live document; status page updates; declared early and handed off cleanly), troubleshooting proceeds hypothesis-driven from symptoms to a bisected cause with mitigation before diagnosis ("stop the bleeding"), and every significant incident gets a blameless postmortem — timeline, impact, root causes and triggers, what went well and badly, action items with owners — because the point is the system that let the mistake become an outage, not the person; the practical constraints are cost (telemetry volume grows faster than traffic — sample traces, aggregate metrics, tier retention) and the discipline of runbooks that turn 3 a.m. pages into procedures.
---
# Observability, monitoring & incident response

**In one sentence.** Emit enough structured telemetry that you can answer questions you
didn't anticipate, alert only on user-visible symptoms measured against SLOs, run
incidents with roles and a timeline, and turn every outage into a blameless postmortem
whose action items change the system.

## Monitoring vs observability; the three pillars (SRE ch. 6; Majors et al.)
**Monitoring**: collecting, processing, aggregating and displaying real-time quantitative
data — for known unknowns (is the error rate high? disk full?). **Observability**: can
you understand any internal state from external outputs — for unknown unknowns ("why is
this one customer's checkout slow since Tuesday?") — which needs **high-cardinality**
(user id, build id, endpoint, region…), **high-dimensionality** data you can slice
arbitrarily. Signals: **metrics** — numeric time series, cheap to store and query, pre-
aggregated, good for alerting and dashboards, bad for cardinality (a label with 10⁶
values × 10 other labels explodes); **logs** — discrete events with context, expensive
at volume, best when **structured** (JSON with fields, request id, severity), sampled or
tail-sampled for errors, retained in tiers; **traces** — one request's causal tree of
**spans** (name, start/duration, attributes, parent) across services, propagated by
trace-context headers; sampled (head-based 1 %, or tail-based keep-the-slow-and-failed);
**profiles** (continuous profiling — [[profiling-and-performance]]) as a fourth. The
modern synthesis: emit one **wide event** per request per service with all fields, derive
metrics and traces from it. **OpenTelemetry** (OTel): vendor-neutral SDKs, auto-
instrumentation, the Collector (receive → process → export), semantic conventions;
backends Prometheus/Grafana (metrics), Loki/ELK (logs), Jaeger/Tempo (traces),
Honeycomb/Datadog (unified). Dapper (2010) is the ancestor
([[cluster-scheduling-and-observability]]).

## What to measure: golden signals, RED, USE (SRE ch. 6; Wilkie; Gregg)
**Four golden signals** per service: **latency** (distinguish successful from failed
requests — fast 500s pollute the average; use percentiles p50/p95/p99 —
[[tail-latency-at-scale]]), **traffic** (requests/s, sessions, bytes), **errors** (explicit
5xx, implicit wrong content, policy — "> 1 s counts as an error"), **saturation** (how
full: CPU, memory, queue depth, connection pool; leading indicator — predict the fill).
**RED** for request-driven services (rate, errors, duration); **USE** for resources
(utilization, saturation, errors — per CPU, disk, NIC, memory) — Gregg's checklist for
performance triage. Prometheus model: `counter` (monotonic; `rate()` it), `gauge`,
`histogram` (buckets; `histogram_quantile` — choose buckets to match SLO thresholds;
aggregatable across instances, unlike summaries), labels as dimensions; scrape-based
pull, service discovery, PromQL; recording rules for expensive queries; **cardinality**
budget (no user ids or URLs with ids as labels). Instrument at boundaries (server
handlers, client calls, queues, DB) and business-level (orders placed, signups) — the
SLI must reflect the user ([[site-reliability-engineering]] SLIs). **Dashboards**: one per
service following a template — SLOs first, golden signals, then resources; dashboards
are for humans exploring, not for detecting (alerts do that); avoid wall-of-graphs.

## Alerting: symptoms, SLO burn rates, and pages vs tickets (SRE ch. 10; Workbook ch. 5)
Rules: a **page** must be **urgent**, **actionable**, **user-visible**, and **novel** (not a
duplicate); everything else is a ticket or a dashboard. Alert on **symptoms** ("user-
facing error rate above SLO") not **causes** ("CPU > 80 %", "disk 90 %") — causes are
many, change, and often harmless; the exception is imminent-cause alerts (disk full in
4 h) as tickets. **SLO-based alerting**: page when the **error-budget burn rate** threatens
the SLO — burn rate = (observed error ratio) / (1 − SLO); with a 30-day 99.9 % SLO, a burn
rate of 14.4 over 1 h consumes 2 % of the monthly budget → page; 6 over 6 h → page; 1
over 3 days → ticket; use **multi-window** (long window for significance, short window
for reset when the problem stops) and **multi-burn-rate** rules — precise, few, tied to
what matters. **Alert fatigue** is an engineering failure: track pages per shift (SRE's
rule: ≤ 2 per 12 h shift), delete or fix noisy alerts, every page needs a runbook link;
"an alert that is always ignored should not exist." Use inhibition/grouping
(Alertmanager), maintenance silences, and escalation policies (PagerDuty/Opsgenie).

## On-call and incident management (SRE ch. 11, 13–14; Workbook ch. 8–9)
**On-call** design: rotations sized so each engineer is on-call ≤ 25 % of time (shifts of
12–24 h; ≥ 8 people for 24/7 across two sites), a **primary** and **secondary**, response-time
expectations (5 min for user-facing), compensation/time off, page volume caps that
trigger reduction work, clean **handoffs**; new engineers shadow before going solo;
"operational underload" is also a problem (skills decay; run game days —
[[chaos-engineering-and-reliability-testing]]). **Incident management** (from ICS):
declare early (a clear threshold: user impact, needs > 1 person, or unclear); roles —
**incident commander** (coordinates, decides, delegates — does *not* debug), **operations
lead** (hands-on mitigation), **communications lead** (stakeholders, status page,
scheduled updates), scribe; a **live incident document** (timeline, hypotheses, actions,
owners); clear handoffs ("you are now IC"); **severity** levels with defined response
(SEV1: all hands, exec comms; SEV3: business hours); **mitigate first, diagnose later** —
rollback, drain traffic, disable feature, add capacity, fail over ("stop the bleeding");
declare resolved with follow-ups. **Troubleshooting** method (SRE ch. 12): triage →
examine (telemetry, logs, traces; what changed? — deploys, config, traffic, dependencies)
→ diagnose (simplify and reduce; "what, where, why"; bisect the system half by half;
correlate with recent changes) → test hypotheses (one at a time, cheapest first) → cure;
avoid tunnel vision and the "last change was fine" trap; the debugging discipline of
[[debugging]] and [[delta-debugging-and-fault-localization]] applied to systems.

## Postmortems and learning (SRE ch. 15; Workbook ch. 10)
Write one for every user-visible outage, data loss, on-call intervention beyond
threshold, or near miss; **blameless**: assume everyone acted with the best intentions on
the information they had; name systems and processes, not people ("the deploy tool
allowed a config push without validation", not "X pushed bad config") — because blame
hides information and the next incident needs it. Template: title/owners; impact
(users, duration, revenue, SLO budget spent); **timeline** with timestamps (detection,
escalation, mitigation, resolution — compute time to detect, to mitigate); **root
causes** (plural; the five whys but stop at systemic factors) vs **trigger**; what went
well / what went wrong / where we got lucky; **action items** — specific, owned, ticketed,
prioritized (fix the class, not the instance: add validation, add alert, add test, add
runbook), tracked to completion; reviewed by peers, shared widely (Google's postmortem
collection, reading clubs). Metrics: MTTD, MTTR — with care (a few big incidents
dominate; DORA now uses failed-deployment recovery time). **Runbooks/playbooks**: per alert,
what to check, common causes, safe mitigations, escalation — the automation backlog in
prose ([[infrastructure-as-code-and-devops]] toil).

## Cost and scale
Telemetry can cost more than compute: metrics cardinality limits, trace sampling (head
1–10 %, tail-based for errors/slow), log sampling and level discipline (debug off in
prod, sample info, keep errors), tiered retention (hot 7–14 days, cold 90+ days), roll-
ups, and cost per signal reviewed like any budget. Correlation across signals (trace id
in logs, exemplars linking histogram buckets to traces) is where value lies — invest in
propagation before in more dashboards.

## Pitfalls
- Paging on causes; hundreds of alerts nobody reads; no runbooks.
- Averages instead of percentiles; latency including failed requests; unbounded label
  cardinality.
- Incidents with no commander (everyone debugging, nobody communicating); no timeline.
- Postmortems that blame, or produce no action items, or action items never done.
- Logging everything at debug in production; no trace propagation across queues.

## Related
- [[site-reliability-engineering]], [[cluster-scheduling-and-observability]],
  [[continuous-integration-and-delivery]], [[chaos-engineering-and-reliability-testing]],
  [[infrastructure-as-code-and-devops]], [[containers-and-kubernetes]],
  [[microservices-and-resilience-patterns]], [[tail-latency-at-scale]],
  [[profiling-and-performance]], [[debugging]], [[delta-debugging-and-fault-localization]],
  [[scalable-system-design]].

## Sources
Beyer et al. 2016 ch. 6, 10–15 (ToC read; ch. 4 read); Beyer et al. 2018 (Workbook) ch. 4–5, 8–10 (ToC read); Majors, Fong-Jones & Miranda 2022 (*Observability Engineering*); Sigelman et al. 2010 (Dapper); Wilkie 2015 (RED); Gregg 2012 (USE); Prometheus documentation; OpenTelemetry specification; Allspaw 2012 (blameless postmortems); Google Cloud, "Incident management" (PagerDuty incident response docs); Ewaschuk & Beyer, "My philosophy on alerting" (2013).

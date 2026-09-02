---
title: DevOps, CI/CD, SRE & infrastructure — Google's Site Reliability Engineering (2016) and The Site Reliability Workbook (2018) (free), Humble & Farley's Continuous Delivery (2010) and continuousdelivery.com, Forsgren, Humble & Kim's Accelerate (2018) and the DORA State of DevOps reports and metrics, Kim et al.'s The DevOps Handbook and The Phoenix Project, Basiri et al.'s "Chaos Engineering" (2016) and the Principles of Chaos, Dean's "Designs, Lessons and Advice from Building Large Distributed Systems" (2009), the Kubernetes documentation, Terraform/HashiCorp docs, Verma et al.'s Borg (2015)
type: source
section: "7.4"
level: 400
tags: [sre-book, site-reliability-engineering, beyer, jones, petoff, murphy, sre-workbook, humble, farley, continuous-delivery, continuousdelivery-com, forsgren, kim, accelerate, dora, state-of-devops, four-keys, five-metrics, devops-handbook, phoenix-project, three-ways, basiri, chaos-engineering, principles-of-chaos, chaos-monkey, netflix, dean, designs-lessons-advice, numbers-every-programmer, kubernetes-docs, terraform, hashicorp, infrastructure-as-code, borg, verma, deployment-pipeline, canarying, slo, error-budget, toil, postmortem]
sources: []
authors: [Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, Jez Humble, David Farley, Nicole Forsgren, Gene Kim, Ali Basiri, Nora Jones, Casey Rosenthal, Jeff Dean, Abhishek Verma]
year: 2016
institution: Google / Thoughtworks / DORA / Netflix
url: https://sre.google/sre-book/table-of-contents/
license: CC BY-NC-ND 4.0 (SRE books); web pages open; books commercial
format: html
summary: The SRE book (read: table of contents; ch. 4 "Service Level Objectives" in full — SLIs as carefully defined quantitative measures such as request latency, error rate, throughput, availability/yield and durability, SLOs as target values or ranges for an SLI, SLAs as the consequences, the Shakespeare example, "you don't always get to choose" (QPS is set by users), latency and QPS being coupled, why 100 % is the wrong target, and the workbook's follow-ups on implementing SLOs, alerting on SLOs and canarying) organizes Google's production discipline as Principles (embracing risk, SLOs, eliminating toil, monitoring distributed systems, automation, release engineering, simplicity), Practices (practical alerting, on-call, troubleshooting, emergency response, managing incidents, postmortem culture, tracking outages, testing for reliability, load balancing at the frontend and in the datacenter, handling overload, cascading failures, distributed consensus, cron, data-processing pipelines, data integrity, launches) and Management, with the 2018 Workbook adding "how SRE relates to DevOps", SLO case studies, managing load, non-abstract large system design, configuration design, and canarying releases; continuousdelivery.com (read) defines CD as the ability to get changes of all types into production safely, quickly and sustainably by keeping the code always deployable, eliminating integration/hardening phases and code freezes, and lists its benefits (low-risk releases via blue-green, faster time to market, higher quality from fast regression feedback, lower costs, better products through small batches and A/B tests — "the 2/3 of features that deliver zero or negative value", happier teams) backed by the peer-reviewed research that speed and stability are not a trade-off; DORA (read: the metrics guide) measures software delivery with throughput (change lead time, deployment frequency, failed-deployment recovery time) and instability (change fail rate, deployment rework rate) — the five-metric evolution of the four keys — and finds top performers do well on all of them; the Principles of Chaos (read) define chaos engineering as experimenting on a system to build confidence in its ability to withstand turbulent production conditions via steady-state hypotheses, real-world event variables, disproving the hypothesis, and the advanced principles (build a hypothesis around steady state, vary real-world events, run in production, automate experiments, minimize blast radius); the Kubernetes docs (read: concepts index — cluster architecture, controllers, pods and probes, Deployments/StatefulSets/DaemonSets/Jobs, autoscaling, Services/Ingress/Gateway, volumes and storage classes, ConfigMaps/Secrets, security and RBAC, scheduling, resource management) describe the orchestrator descended from Borg; and Accelerate, The DevOps Handbook (the Three Ways: flow, feedback, continual learning), The Phoenix Project, Dean's talk (the numbers every engineer should know; design for failure at scale; back-of-envelope reasoning) and the Terraform docs (declarative infrastructure as code, state, plan/apply, modules) supply the rest.
---
# DevOps, CI/CD, SRE & infrastructure: sources

## What they are
- **SRE book** (Beyer, Jones, Petoff & Murphy 2016; read: ToC + ch. 4): I Introduction
  (ch. 1–2: SRE = software engineers doing operations; 50 % cap on ops work; the
  production environment); II Principles (3 Embracing Risk — error budgets; 4 SLOs; 5
  Eliminating Toil; 6 Monitoring Distributed Systems — four golden signals; 7 Evolution
  of Automation; 8 Release Engineering; 9 Simplicity); III Practices (10 Practical
  Alerting — Borgmon; 11 Being On-Call; 12 Effective Troubleshooting; 13 Emergency
  Response; 14 Managing Incidents; 15 Postmortem Culture; 16 Tracking Outages; 17 Testing
  for Reliability; 18 Software Engineering in SRE; 19–20 Load Balancing; 21 Handling
  Overload; 22 Cascading Failures; 23 Distributed Consensus; 24 Cron; 25 Data Processing
  Pipelines; 26 Data Integrity; 27 Reliable Product Launches); IV Management (28–32);
  V Conclusions; appendices (availability table, best practices, incident state doc,
  example postmortem, launch checklist). The §4.8 page [[site-reliability-engineering]]
  distils ch. 3–8, 10–15, 18–22, 26–27.
- **SRE Workbook** (2018; read: ToC): 1 How SRE relates to DevOps ("class SRE implements
  DevOps"); I Foundations (2 Implementing SLOs; 3 SLO case studies; 4 Monitoring; 5
  Alerting on SLOs — burn-rate alerts; 6 Toil; 7 Simplicity); II Practices (8 On-Call; 9
  Incident Response; 10 Postmortem Culture; 11 Managing Load; 12 Non-Abstract Large
  System Design; 13 Data Processing Pipelines; 14–15 Configuration Design and Specifics;
  16 Canarying Releases); III Processes (17 Overload; 18–21 engagement model, reaching
  beyond your walls, team lifecycles, organizational change); appendices (example SLO
  document, error-budget policy, postmortem analysis).
- **Continuous Delivery** (Humble & Farley 2010; site read): the deployment pipeline
  (commit stage → automated acceptance → capacity/manual → release), configuration
  management, continuous integration, testing strategy, deploying and releasing
  (blue-green, canary), infrastructure and environments, data migration, component and
  branch management; "if it hurts, do it more often."
- **Accelerate / DORA** (Forsgren, Humble & Kim 2018; metrics guide read): 24 capabilities
  (CD, architecture, product/process, lean management, culture — Westrum generative
  culture) that statistically predict software delivery performance and organizational
  performance; the four keys → five metrics (change lead time, deployment frequency,
  failed-deployment recovery time; change fail rate, deployment rework rate); annual
  State of DevOps reports (2014–).
- **The DevOps Handbook / The Phoenix Project** (Kim et al. 2016; Kim, Behr & Spafford
  2013): the Three Ways — flow (small batches, WIP limits, reduce handoffs), feedback
  (telemetry, fast detection, andon cord), continual learning and experimentation
  (blameless postmortems, game days); the novel's IT-as-manufacturing lessons (Brent the
  bottleneck, four types of work: business projects, internal projects, changes,
  unplanned work).
- **Chaos engineering** (Basiri et al., IEEE Software 2016; Principles of Chaos, 2019
  revision, read): the four-step experiment and five advanced principles; Netflix's
  Chaos Monkey (2011), Chaos Kong (region failure), FIT and ChAP (automated platform);
  Google DiRT; Gremlin; AWS Fault Injection Simulator; *Chaos Engineering* (Rosenthal &
  Jones 2020).
- **Dean 2009/2013** ("Designs, Lessons and Advice from Building Large Distributed
  Systems"; "The Tail at Scale"): numbers every engineer should know; the rule of
  thumb designs (GFS, MapReduce, Bigtable); design for failure (a cluster of 10 000
  machines sees ~1 000 individual failures a year, disks, network, power, sharks);
  back-of-envelope; hedged requests — [[tail-latency-at-scale]], [[scalable-system-design]].
- **Kubernetes docs** (read: concepts index) and **Borg** (Verma et al., EuroSys 2015 —
  [[cluster-scheduling-and-observability]]); **Terraform** docs (providers, resources,
  state, plan/apply, modules, workspaces); Docker docs; the Twelve-Factor App (Wiggins
  2011); *Infrastructure as Code* (Morris 2016/2020); *Observability Engineering*
  (Majors, Fong-Jones & Miranda 2022); *Release It!* (Nygard).

## Key ideas → pages
[[continuous-integration-and-delivery]], [[containers-and-kubernetes]],
[[infrastructure-as-code-and-devops]], [[observability-monitoring-and-incident-response]],
[[chaos-engineering-and-reliability-testing]]; existing: [[site-reliability-engineering]],
[[cluster-scheduling-and-observability]], [[cloud-and-serverless]].

## What they add
The SRE books are the free, complete statement of how a planet-scale operator thinks
(risk as a budget, toil as a cap, alerts as symptoms); CD and DORA are the evidence that
shipping faster makes systems *more* stable; chaos engineering makes resilience an
experimental science; the Kubernetes docs are where the Borg ideas became the industry's
operating system.

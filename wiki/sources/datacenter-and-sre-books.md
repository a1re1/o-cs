---
title: The Datacenter as a Computer (Barroso, Hölzle, Ranganathan — free), Site Reliability Engineering and Building Secure and Reliable Systems (Google — free), with Stanford CS349D and Berkeley CS262A reading lists
type: source
section: "4.8"
level: 400
tags: [datacenter-as-a-computer, warehouse-scale-computing, barroso, holzle, sre-book, site-reliability-engineering, building-secure-and-reliable-systems, google, cs349d, cs262a, cloud-computing-course]
sources: []
authors: [Luiz André Barroso, Urs Hölzle, Parthasarathy Ranganathan, Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Murphy, Heather Adkins]
year: 2018
institution: Google
url: https://sre.google/books/
license: free online (Morgan & Claypool synthesis lecture; O'Reilly books free from Google)
format: html
summary: The Datacenter as a Computer (3rd ed.) treats a warehouse-scale computer as one machine — workloads and software infrastructure, hardware building blocks (servers, storage, networking, accelerators), datacenter basics (power distribution, cooling, PUE), energy and power efficiency, modeling cost (TCO), dealing with failures and repairs (hardware fails constantly, so software provides availability), and the "tail at scale"; the SRE book codifies Google's operations discipline — SLOs and error budgets, eliminating toil, monitoring (four golden signals), release engineering, simplicity, alerting, on-call, incident management, blameless postmortems, load balancing, overload handling, cascading failures, distributed consensus in practice, cron, data-processing pipelines, data integrity; Building Secure and Reliable Systems extends it to security (design for least privilege, understandability, resilience and recovery, crisis management); CS349D (cloud computing technology) and CS262A (advanced systems, Berkeley) provide paper lists.
---
# Datacenter and SRE books

## What they are
- **The Datacenter as a Computer** (WSC): 1 introduction (WSCs vs datacenters; cost efficiency
  at scale; the architecture of a Google WSC); 2 workloads and software infrastructure
  (platform-level, cluster-level — resource management, storage, monitoring; application-
  level — internet services, e.g. web search; monitoring; buy vs build; tail tolerance); 3
  hardware building blocks (cost-efficient server hardware, DRAM/flash/disk hierarchy, WSC
  memory hierarchy — latencies and bandwidths from local DRAM to remote disk, interconnects,
  accelerators — TPUs); 4 datacenter basics (tiers, power systems — UPS, PDUs; cooling —
  CRAC, free cooling; **PUE**; example designs); 5 energy and power efficiency (energy
  proportionality, power provisioning and capping, dynamic voltage/frequency scaling); 6
  modeling costs (capital vs operational expense, case studies — the cost of a server-year);
  7 dealing with failures and repairs (fault-tolerant software as the enabler of cheap
  hardware; categorizing faults; machine-level failures; repairs); 8 closing remarks
  (hardware trends, software trends, economic factors).
- **SRE**: I introduction (Google's approach; 50 % cap on ops work); II principles —
  embracing risk (availability targets, error budgets), **SLOs** (SLIs, choosing targets),
  eliminating **toil**, monitoring distributed systems (latency, traffic, errors, saturation),
  automation, release engineering, simplicity; III practices — alerting on SLOs, being
  on-call, effective troubleshooting, emergency response, incident management, **postmortem**
  culture, tracking outages, testing for reliability, capacity planning, load balancing at the
  front end and in the datacenter, handling overload (per-customer quotas, retries, criticality),
  addressing cascading failures, managing critical state with distributed consensus, cron,
  data-processing pipelines, data integrity, reliable product launches; IV management.
  The Workbook (2018) adds worked examples. **Building Secure and Reliable Systems** (2020):
  security and reliability tradeoffs, design (least privilege, understandability, adaptability,
  resilience, recovery), implementation (testing, deploying, investigating), maintaining
  (crisis management, recovery, culture).
- **CS349D / CS262A**: reading lists across cloud infrastructure (VMs, containers, serverless,
  storage, scheduling, ML systems) and classic systems papers.

## Key ideas → pages
[[warehouse-scale-computing]], [[site-reliability-engineering]], [[cloud-and-serverless]],
[[distributed-file-and-object-storage]], [[tail-latency-at-scale]], [[cluster-scheduling-and-observability]].

## What they add
WSC explains the economics that make everything in §4.6–4.8 necessary; SRE turns distributed-
systems theory into an operating discipline with numbers (SLOs, error budgets) that
organizations can actually run on.

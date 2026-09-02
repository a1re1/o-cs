---
title: Cluster scheduling and observability — Borg and Kubernetes, serverless, distributed tracing (Dapper), and blast-radius thinking
type: concept
section: "4.6"
level: 400
tags: [cluster-scheduling, borg, kubernetes, containers, pods, bin-packing, resource-quotas, priority, preemption, autoscaling, service-discovery, load-balancing, serverless, aws-lambda, firecracker, cold-starts, observability, distributed-tracing, dapper, opentelemetry, spans, sampling, metrics, logs, slos, blast-radius, cell-architecture, physalia, memcached-at-facebook, cache-invalidation, thundering-herd]
sources: [mit-6-824, distributed-systems-seminal-papers]
summary: Running many services on shared machines needs a cluster manager — Borg (Google 2015) schedules jobs of tasks into cells, bin-packs by requested CPU/memory with priorities, quotas and preemption, restarts failed tasks, and exposes naming and monitoring, lessons that Kubernetes carried forward as pods, labels, declarative desired state reconciled by controllers, services with load balancing, and etcd-backed control — with serverless platforms (AWS Lambda on Firecracker microVMs) pushing scheduling to per-invocation granularity; understanding such systems in production needs observability — Dapper's distributed tracing (trace and span ids propagated through every RPC, sampled, aggregated — now OpenTelemetry) alongside metrics and structured logs against SLOs — and designing them needs blast-radius thinking: cells, shuffle sharding, Physalia's per-volume consensus cells, and cache-tier lessons from Facebook's Memcached (leases against thundering herds and stale sets, regional invalidation streams).
---
# Cluster scheduling and observability

**In one sentence.** A datacenter is one computer whose operating system is the cluster
manager, and whose debugger is tracing.

## Borg and Kubernetes (Verma et al. 2015)
**Borg**: a **cell** (~10k machines) run by a replicated **Borgmaster** (Paxos-based store, an
elected leader — [[consensus-paxos-raft]]) and per-machine **Borglets**; users submit **jobs**
of identical **tasks** with resource requests, priority (monitoring > production > batch >
best-effort) and **quota**; the scheduler does feasibility checking then scoring (bin-packing
vs spreading, avoiding stranded resources), **preempts** lower-priority tasks, and packs prod
and batch together for utilization (the paper's key economic claim: segregating them would
need 20–30 % more machines). Also: resource reclamation (usage < request), naming (BNS) and
load balancing, monitoring, Chubby-based config. Lessons that shaped **Kubernetes**: pods (co-
scheduled containers) instead of tasks, **labels** instead of job names, one IP per pod,
**declarative desired state** with controllers reconciling ([[invariant-principle]]),
etcd + API server, deployments/replica sets, services + kube-proxy/ingress, horizontal
autoscaling, namespaces/quotas; multi-cluster and cell-per-region layouts. Alternatives:
Mesos/Omega (two-level and shared-state scheduling), YARN, Nomad.

## Serverless (Brooker, 6.824 L17)
AWS Lambda: functions invoked per event; **Firecracker** microVMs (KVM, ~125 ms boot, strong
isolation — [[os-kernels-and-virtualization]]) with snapshot restore for cold starts; a
placement service bin-packs by predicted memory/CPU; worker fleets, multi-tenant with cell-
based isolation; the economics of paying for milliseconds; state lives elsewhere (S3, DynamoDB)
— design implications: idempotent handlers, retries, concurrency limits.

## Observability (Dapper 2010)
**Distributed tracing**: each request gets a trace id; every RPC creates a **span** (parent
id, timestamps, annotations) propagated in headers through all services; sampled (1/1024 at
Google) to bound overhead; collected out-of-band and indexed for latency debugging, dependency
maps, and outlier analysis. **OpenTelemetry** standardizes traces + **metrics** (counters,
gauges, histograms — Prometheus; RED/USE methods) + **logs** (structured, correlated by trace
id). SLIs/SLOs and error budgets (SRE); percentiles not averages ([[profiling-and-performance]]);
alerting on symptoms; cardinality costs.

## Caches at scale (Memcached at Facebook 2013; 6.824 L16)
Look-aside cache in front of MySQL; **leases** to stop thundering herds and stale sets; regional
pools and replication; cross-region invalidation via the DB replication stream (mcsqueal);
gutter pools for failed servers; consistency is eventual and deliberately so — reads-your-
writes handled by per-user routing. Cache invalidation is a distributed-systems problem
([[caches-and-memory-hierarchy]], [[consistency-models]]).

## Blast radius (Physalia 2020; AWS cell architecture)
Failures correlate (deploys, config, power, software bugs); limit what one failure can take
down: **cells** (independent copies of the whole stack sized to a bounded fraction of
customers), **shuffle sharding** (each customer mapped to a random subset of nodes so
overlap between any two customers is tiny), static stability (data plane keeps working when
the control plane is down), per-volume consensus cells placed near their clients (Physalia).
Gradual deploys, canaries, and load shedding ([[queueing-theory]]).

## Pitfalls
- Overcommitting without priorities or without measuring actual usage.
- Stateful services scheduled like stateless ones; no pod disruption budgets.
- Unsampled tracing that becomes the load; metrics with unbounded label cardinality.
- One control plane whose failure is the outage; correlated failure through shared config.

## Related
- [[consensus-paxos-raft]], [[replication-and-partitioning]], [[os-kernels-and-virtualization]],
  [[processes-and-threads]], [[profiling-and-performance]], [[queueing-theory]],
  [[consistency-models]], [[mapreduce-and-dataflow]].

## Sources
Verma et al. 2015; Burns et al. "Borg, Omega, and Kubernetes" 2016; Sigelman et al. 2010; Nishtala et al. 2013; Brooker et al. 2020; Agache et al. "Firecracker" 2020; 6.824 L16–17.

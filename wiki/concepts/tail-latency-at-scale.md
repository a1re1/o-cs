---
title: The tail at scale — why p99 latency dominates fan-out services and the techniques that tame it (hedged and tied requests, micro-partitions, selective replication, load shedding)
type: concept
section: "4.7"
level: 400
tags: [tail-latency, p99, percentiles, fan-out, latency-amplification, variability, hedged-requests, tied-requests, backup-requests, micro-partitions, selective-replication, latency-induced-probation, canary-requests, good-enough-results, garbage-collection-pauses, queueing, load-shedding, timeouts, retries, sla, slo, coordinated-omission, dean-barroso]
sources: [parallel-computing-seminal-papers, stanford-cs149-and-cmu-15-418]
summary: Dean & Barroso (2013) observed that in a service fanning a request out to many servers the slowest reply sets the latency, so rare slowness becomes common — if 1 in 100 requests is slow, 63% of 100-way fan-outs are — and catalogued both the causes of variability (shared resources, background daemons, GC and compaction, queueing, power throttling, head-of-line blocking, hardware aging) and the cures: reduce component variability (service classes, breaking large requests into small ones, managing background work), and tolerate it — hedged requests (send a second copy after the p95 delay and take the first answer), tied requests (send to two queues with cross-cancellation), micro-partitions that can be moved and replicated for load balance, selective replication of hot items, latency-induced probation of slow servers, and for information-retrieval good-enough results and canary requests; the same tail thinking governs timeouts, retry budgets and load shedding, and measuring it honestly requires percentiles (never averages) and avoiding coordinated omission.
---
# The tail at scale

**In one sentence.** In a system that waits for the slowest of many, the 99th percentile is
the median — so engineer for variability, not for the average.

## The arithmetic (Dean & Barroso 2013)
If each server answers within its p99 with probability 0.99, a request touching 100 servers
finishes within that bound with probability 0.99¹⁰⁰ ≈ 0.37. Fan-out is intrinsic to search,
recommendations, storage (sharded reads), microservices — hence tail latency, not throughput,
is the user-visible metric; it also compounds along dependency chains. Amdahl for latency:
the slowest leg is the serial fraction ([[parallel-programming-models]]).

## Sources of variability
Shared resources (CPU, cache, memory bandwidth, network switches — noisy neighbours),
background daemons and log compaction ([[storage-engines-and-indexes]]), **garbage
collection** pauses ([[garbage-collection]]), queueing at every layer ([[queueing-theory]]),
maintenance and re-replication, energy management (frequency scaling, idle states), head-of-
line blocking in single queues, hardware variability and aging, interrupt/NUMA effects, and
**coordinated omission** in your own load generator hiding the truth.

## Reducing component variability
Differentiated service classes and priority queues; breaking large requests into smaller
interleaved pieces; managing background activity (throttle, schedule at low load, synchronize
across a fleet so the disruption hits once); reducing head-of-line blocking; bounded work per
request; warm caches; pre-allocation and GC tuning; avoiding synchronous disk/`fsync`
([[file-systems]]) on the request path.

## Living with variability (within-request short-term adaptations)
- **Hedged requests**: send the request to one replica; if no reply by the p95 latency, send it
  to another; take the first answer, cancel the rest — cuts p99.9 by 10× for ~2 % extra load.
- **Tied requests**: enqueue on two servers at once, each tagged with the other's identity; the
  first to start cancels the twin — avoids duplicate work while removing queueing tails.
- Probe first, or send to the server with the shorter queue (join-shortest-queue, power of two
  choices — [[randomized-algorithms]]).
Cross-request long-term adaptations: **micro-partitions** (many more partitions than machines
so load can be rebalanced finely — [[replication-and-partitioning]]), **selective replication**
of hot partitions/items, **latency-induced probation** (temporarily stop sending to a slow
server while still probing it). Large information-retrieval systems: **good-enough** results
(return when enough shards answered), **canary requests** (send novel queries to one or two
leaves first to catch pathological queries before fanning out).

## Related engineering
Timeouts and **retry budgets** (retries amplify overload; hedges must be bounded); **load
shedding** and admission control ahead of queues; circuit breakers; deadlines propagated
through RPCs (gRPC); backpressure. Measurement: histograms with percentiles (HdrHistogram),
per-dependency latency budgets, SLOs on p99/p99.9 ([[cluster-scheduling-and-observability]]);
CS149-style profiling of where the tail comes from ([[profiling-and-performance]]).

## Pitfalls
- Averages and even medians as the SLI; percentiles computed by averaging percentiles.
- Hedging every request (doubling load) or hedging non-idempotent operations.
- Retries without budgets during an outage (retry storm); timeouts longer than the SLO.
- Ignoring GC and compaction pauses in "the network is slow" diagnoses.

## Related
- [[queueing-theory]], [[replication-and-partitioning]], [[cluster-scheduling-and-observability]],
  [[distributed-systems-basics]], [[profiling-and-performance]], [[garbage-collection]],
  [[randomized-algorithms]].

## Sources
Dean & Barroso, "The Tail at Scale", CACM 2013; Tene "How NOT to measure latency"; SRE book ch. 21–22; Mitzenmacher "The power of two choices" 2001.

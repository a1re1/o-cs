---
title: Distributed systems basics — system models, partial failure, RPC, the FLP impossibility, failure detectors, and the fallacies
type: concept
section: "4.6"
level: 400
tags: [distributed-systems, system-model, asynchronous, synchronous, partially-synchronous, crash-stop, crash-recovery, byzantine, partial-failure, network-partition, rpc, at-least-once, at-most-once, exactly-once, idempotency, timeouts, retries, flp, impossibility, failure-detectors, heartbeats, leases, fallacies-of-distributed-computing, two-generals, split-brain, fencing-tokens]
sources: [mit-6-824, distributed-systems-textbooks, distributed-systems-seminal-papers]
summary: A distributed system is one where message delay is not negligible (Lamport), so the defining problem is partial failure — a node cannot tell a crashed peer from a slow network — and everything follows from the model you assume: network (reliable/fair-loss/arbitrary), nodes (crash-stop, crash-recovery, Byzantine), timing (synchronous with bounded delays, asynchronous with none, or partially synchronous — eventually bounded, the realistic choice); RPC hides messaging but not its failure semantics (at-least-once needs idempotency, at-most-once needs deduplication, exactly-once is at-least-once plus idempotent or transactional application of effects); the two-generals problem shows no finite protocol guarantees agreement over a lossy link, and FLP proves no deterministic asynchronous consensus protocol always terminates with even one crash — so practical systems escape through timeouts (partial synchrony), randomization, or failure detectors (Chandra & Toueg: eventually-accurate suspicion via heartbeats suffices), and defend against wrong suspicions with leases, quorums and fencing tokens.
---
# Distributed systems basics

**In one sentence.** You cannot distinguish a dead node from a slow one, so every guarantee
must survive being wrong about who is alive.

## Why and what (6.824 L1; van Steen ch. 1)
Reasons: scale/performance, fault tolerance, physical separation of data, isolation. Costs:
concurrency, **partial failure** (some parts fail while others continue — unlike a single
machine that stops entirely), unpredictable performance, the impossibility of global state.
The fallacies (Deutsch): the network is reliable, latency is zero, bandwidth is infinite, the
network is secure, topology doesn't change, one administrator, transport cost is zero, the
network is homogeneous. Transparency goals (access, location, replication, failure) are
never fully achieved — Waldo et al. "A Note on Distributed Computing": latency, memory access,
partial failure and concurrency make remote objects fundamentally different from local ones.

## System models (Kleppmann lecture 2; Cachin ch. 2)
| Dimension | Options |
|---|---|
| Network | reliable (delivered eventually) / fair-loss (retry enough and it arrives) / arbitrary (adversary); partitions |
| Nodes | crash-stop / crash-recovery (stable storage survives) / Byzantine (arbitrary, malicious) |
| Timing | synchronous (bounded delay and processing, clocks accurate) / asynchronous (no bounds — proofs of impossibility live here) / **partially synchronous** (bounds hold eventually or after an unknown GST — the model real systems design for) |
Fault tolerance thresholds: crash faults need majority quorums (2f+1 to tolerate f);
Byzantine needs 3f+1 ([[byzantine-fault-tolerance-and-blockchains]]). Safety ("nothing bad
happens" — provable in any model) vs liveness ("something good eventually happens" — needs
timing assumptions).

## RPC and failure semantics (6.824 L2)
Stubs marshal arguments, send a request, wait for a reply ([[sockets-programming]]; gRPC/
Thrift/Protobuf IDLs). If no reply: the request was lost, the server crashed before or after
executing, or the reply was lost — indistinguishable. **At-least-once** (retry) requires
**idempotent** operations; **at-most-once** requires server-side duplicate detection (unique
request ids, per-client sequence numbers — 6.824 lab 2/4); "**exactly-once**" = at-least-once
delivery + idempotent/transactional effects (dedup tables, idempotency keys, outbox pattern).
Timeouts must be chosen (too short: false suspicion, retry storms; too long: slow recovery);
exponential backoff with jitter; circuit breakers; retries amplify overload (retry budgets).

## Impossibility results
- **Two generals**: over a lossy channel no finite message exchange lets both parties know the
  other will act — acknowledgements regress; hence commit protocols only bound, never
  eliminate, uncertainty ([[distributed-databases-and-nosql]] 2PC).
- **FLP** (1985): in the asynchronous crash model, no deterministic consensus protocol
  guarantees termination with one faulty process — there is always an execution where messages
  are delayed just so that the system stays undecided. Not a statement about probability;
  practical escape hatches: partial synchrony (timeouts — Paxos/Raft are safe always, live
  when the network behaves), randomization (Ben-Or), failure detectors.
- **Failure detectors** (Chandra & Toueg 1996): heartbeats and timeouts implement an
  eventually perfect detector ◇P (eventually every crashed node is suspected and no live node
  is); ◇W (eventually some correct process is never suspected by anyone) is the weakest to solve
  consensus with a majority. Leader election Ω is a failure detector.

## Living with wrong suspicions
**Split brain**: two nodes each believe they lead. Defences: majority **quorums** (only one
side of a partition can have a majority — [[consensus-paxos-raft]]), **leases** (time-bounded
authority that expires without renewal — needs bounded clock drift, [[time-clocks-and-ordering]]),
**fencing tokens** (monotonic epoch numbers checked by the resource so a stale leader's
writes are rejected — Kleppmann's lock-service example), STONITH. Design for retries,
duplicates and reordering at every boundary; test with fault injection (Jepsen, chaos
engineering, deterministic simulation as in FoundationDB).

## Pitfalls
- Treating a timeout as proof of death; treating RPC like a local call.
- Non-idempotent handlers retried; missing request ids.
- Assuming clocks agree or that "eventually" comes quickly.
- Reasoning about liveness in the asynchronous model ("it must terminate").

## Related
- [[time-clocks-and-ordering]], [[consistency-models]], [[consensus-paxos-raft]],
  [[replication-and-partitioning]], [[distributed-databases-and-nosql]], [[sockets-programming]],
  [[internet-architecture-and-layering]], [[byzantine-fault-tolerance-and-blockchains]].

## Sources
6.824 L1–2; Kleppmann lectures 1–3; van Steen & Tanenbaum ch. 1, 4, 8; Cachin et al. ch. 2; FLP 1985; Chandra & Toueg 1996; DDIA ch. 8.

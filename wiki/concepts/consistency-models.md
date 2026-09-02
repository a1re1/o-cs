---
title: Consistency models — linearizability, sequential and causal consistency, eventual consistency and session guarantees, CAP/PACELC, and CRDTs
type: concept
section: "4.6"
level: 400
tags: [consistency-models, linearizability, sequential-consistency, causal-consistency, eventual-consistency, strong-eventual-consistency, read-your-writes, monotonic-reads, session-guarantees, cap, pacelc, quorums, crdts, conflict-resolution, last-writer-wins, jepsen, anomalies, stale-reads, coordination-avoidance, external-consistency, strict-serializability]
sources: [mit-6-824, distributed-systems-textbooks, distributed-systems-seminal-papers]
summary: A consistency model is the contract between a replicated store and its clients about which histories are allowed: linearizability (each operation appears to take effect atomically at some instant between its invocation and response — the strongest single-object guarantee, what CAP calls C, checkable per Herlihy–Wing and Jepsen), sequential consistency (a total order consistent with each client's program order but not real time), causal consistency (respects happens-before, the strongest model achievable while staying available under partition), and eventual consistency (replicas converge if updates stop — meaningful only with session guarantees such as read-your-writes and monotonic reads), with strict serializability = linearizability for multi-object transactions; CAP says linearizability and availability are incompatible during a partition and PACELC adds the latency cost even without one, quorum reads/writes (W+R>N) give a middle ground that is still not linearizable without care, and CRDTs let replicas accept writes independently and merge deterministically (strong eventual consistency) for counters, sets, maps and collaborative text.
---
# Consistency models

**In one sentence.** Pick the weakest model your application can survive, because every
notch of strength costs a round trip, a partition-time outage, or both.

## The models (6.824 L8; Kleppmann lecture 7)
| Model | Guarantee | Cost / where |
|---|---|---|
| **Linearizability** (atomic) | one total order of operations consistent with real time; reads see the latest completed write | consensus or single leader with synchronous replication; unavailable under partition; Herlihy & Wing 1990 |
| Strict serializability | linearizability for multi-object transactions (serializable + real-time) | Spanner, CockroachDB, FaunaDB |
| **Sequential consistency** | one total order consistent with each process's order, not real time | processor-local ordering; cheaper reads (ZooKeeper reads are sequentially consistent, writes linearizable) |
| **Causal consistency** (+ read-your-writes = causal+) | writes related by happens-before seen in that order everywhere; concurrent writes may differ | strongest available-under-partition model (Mahajan/Attiya); COPS, Antidote; vector timestamps |
| Session guarantees (Terry 1994; Vogels 2009) | read-your-writes, monotonic reads, monotonic writes, writes-follow-reads | sticky sessions or version tokens on top of eventual stores |
| **Eventual consistency** | replicas converge if updates cease; no guarantee on what a read returns meanwhile | Dynamo, DNS, Cassandra; must define conflict resolution |
Anomalies to name: stale reads, non-monotonic reads (time going backwards), lost updates,
causality violations (a reply visible before the question). Verification: Jepsen/Knossos
(linearizability checking is NP-complete in general), Elle for transactional anomalies.

## Achieving linearizability
Single leader with synchronous replication (reads served by the leader, or with lease-based
leader reads / read index in Raft); consensus per operation; or a leaderless quorum with
**read repair before returning** and synchronous read-repair on writes (still subtle — Dynamo-
style W+R>N quorums are not linearizable under sloppy quorums or concurrent writes).
Linearizable reads are the expensive part: leases (clock assumptions), quorum reads, or
follower reads at a safe timestamp (Spanner).

## CAP and PACELC
Gilbert & Lynch: in an asynchronous network, a linearizable register cannot answer every
request at every non-failing node during a partition. Kleppmann: C = linearizability, A = every
node answers, model = single register; so most systems are neither CP nor AP. **PACELC**
(Abadi): if Partition then A vs C; Else Latency vs Consistency — the everyday trade is latency.
Coordination-avoidance (Bailis): invariant confluence decides which application invariants
can be maintained without coordination.

## CRDTs (Shapiro et al. 2011)
Data types whose replicas can be updated independently and **merged** deterministically:
**state-based** (states form a join-semilattice; merge = least upper bound; gossip states) —
G-counter, PN-counter, G-set, **OR-set** (add-wins with unique tags), LWW-register, MV-
register; **op-based** (operations commute; require causal delivery). Sequences for
collaborative editing (RGA, Yjs, Automerge; vs operational transformation). Guarantees
**strong eventual consistency** (converge as soon as the same updates are seen) but not
application invariants (a CRDT counter can go negative); tombstones and metadata growth.

## Choosing
Money and uniqueness need linearizability (or an escrow/coordination-free design); social
feeds tolerate causal; caches tolerate eventual with TTLs. Read-your-writes is the minimum
users notice. Document the model at every API boundary.

## Pitfalls
- Calling an eventually consistent store "consistent because it converges".
- Assuming quorums imply linearizability; reading from followers without a safe timestamp.
- LWW discarding concurrent writes silently.
- Confusing ACID consistency (invariants) with CAP consistency (linearizability).

## Related
- [[time-clocks-and-ordering]], [[consensus-paxos-raft]], [[replication-and-partitioning]],
  [[distributed-systems-basics]], [[distributed-databases-and-nosql]],
  [[transactions-and-concurrency-control]], [[cache-coherence-and-memory-consistency]].

## Sources
6.824 L8–9; Kleppmann lectures 5–8; DDIA ch. 5, 9; Herlihy & Wing 1990; Gilbert & Lynch 2002; Vogels 2009; Shapiro et al. 2011; Bailis et al. 2014; Kleppmann 2015.

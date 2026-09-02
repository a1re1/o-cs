---
title: Consensus and state-machine replication — Paxos, Raft, ZooKeeper/Chubby coordination services, and practical concerns (leases, reconfiguration, snapshots, blast radius)
type: concept
section: "4.6"
level: 400
tags: [consensus, state-machine-replication, replicated-log, paxos, single-decree-paxos, multi-paxos, proposers, acceptors, ballots, raft, leader-election, terms, randomized-timeouts, log-replication, log-matching, leader-completeness, commit-index, joint-consensus, membership-change, log-compaction, snapshots, zab, zookeeper, chubby, etcd, coordination-service, leases, linearizable-reads, read-index, quorum, majority, viewstamped-replication, epaxos, physalia]
sources: [mit-6-824, distributed-systems-textbooks, distributed-systems-seminal-papers]
summary: Consensus lets a majority of crash-prone servers agree on one value — and, as a replicated log driving deterministic state machines (Schneider), on an ordered sequence of commands, making a fault-tolerant service that survives f failures with 2f+1 nodes; Paxos does it with proposers and acceptors exchanging numbered prepare/promise and accept/accepted messages, choosing any value already accepted by a quorum (safety) and using a stable leader to skip phase 1 (multi-Paxos); Raft decomposes the same thing into leader election by randomized timeouts and terms, log replication by AppendEntries with the log-matching invariant, and a safety rule (only candidates with up-to-date logs win; a leader commits only entries from its own term) that yields leader completeness and state-machine safety, plus joint-consensus membership changes and snapshot-based compaction — and coordination services (Chubby, ZooKeeper with Zab, etcd) package a consensus-replicated small store with watches, ephemeral nodes and leases so everyone else can do leader election, locks and configuration without reimplementing Paxos.
---
# Consensus: Paxos and Raft

**In one sentence.** Get a majority to agree on each log entry in order, and any majority
overlaps every previous one — that overlap is the whole trick; the rest is making it
understandable and fast.

## State-machine replication (Schneider 1990; 6.824 L6)
Deterministic state machine + agreed input order ⇒ identical replicas. Requirements: agreement
(all correct replicas receive the same commands) and order. Consensus per log slot;
**safety** always (no two servers decide differently), **liveness** only when the network is
eventually timely (FLP — [[distributed-systems-basics]]). Tolerates f crash failures with 2f+1
servers because any two majorities intersect. Applications: configuration stores, lock
services, metadata (Chubby for GFS/Bigtable), replicated databases (Spanner Paxos groups,
CockroachDB Raft ranges), Kafka's KRaft, TiKV, etcd for Kubernetes.

## Paxos (Lamport 1998/2001; 6.824 L4)
Roles: proposers, acceptors, learners. **Single-decree**: phase 1 — proposer picks ballot n,
sends *prepare(n)*; acceptors promise not to accept lower ballots and report the highest-
ballot value they accepted; phase 2 — proposer sends *accept(n, v)* where v is the highest-
ballot accepted value reported, or its own if none; acceptors accept unless they promised a
higher ballot; a value accepted by a majority is chosen. Invariant: once a value is chosen,
every higher-ballot proposal carries it. Duelling proposers can livelock ⇒ elect a
distinguished leader. **Multi-Paxos**: leader runs phase 1 once for all future slots, then
phase 2 per command; holes, reconfiguration, and log compaction are left "as exercises" — the
source of Raft's complaint and of many divergent implementations (Chubby, Spanner). Variants:
Flexible Paxos (phase quorums need only intersect), EPaxos (leaderless, commutativity),
Viewstamped Replication (1988, Raft's closest relative).

## Raft (Ongaro & Ousterhout 2014; 6.824 L6–7)
Servers are follower, candidate, or leader; time divided into **terms** (monotonic, one leader
max per term). 
- **Leader election**: followers time out (randomized 150–300 ms) → become candidate,
  increment term, RequestVote; a majority elects; heartbeats (empty AppendEntries) suppress
  elections. Election restriction: vote only for candidates whose last log entry is at least as
  up-to-date (term, then index).
- **Log replication**: leader appends entry, sends AppendEntries with (prevLogIndex,
  prevLogTerm); followers reject on mismatch; leader decrements nextIndex and retries
  (**log matching**: same index+term ⇒ identical prefix). An entry is **committed** once stored
  on a majority *and* from the leader's current term (figure 8 subtlety: earlier-term entries
  commit indirectly). Committed entries applied in order; clients get results after commit.
- **Safety properties**: election safety, leader append-only, log matching, **leader
  completeness** (a committed entry is in every future leader's log), **state machine safety**.
- **Membership changes**: joint consensus (C_old,new) requiring majorities of both; or the
  single-server-change simplification. **Log compaction**: snapshots with last included
  index/term, InstallSnapshot RPC (lab 3D). **Client interaction**: at-most-once via client
  ids + sequence numbers (lab 4); linearizable reads via leader lease or **ReadIndex** (confirm
  leadership with a heartbeat round); follower reads with safe indexes.
- Performance: one round trip to a majority per batch; pipelining; the leader is the
  bottleneck ⇒ shard into many Raft groups (CockroachDB ranges, [[replication-and-partitioning]]).

## Coordination services (6.824 L9; Chubby 2006; ZooKeeper 2010)
Small replicated hierarchical store (znodes) with **watches**, **ephemeral** nodes (die with the
session), **sequential** nodes; ZooKeeper: linearizable writes via **Zab**, reads served locally
(FIFO client order + `sync` for freshness) for scalability; recipes — leader election (lowest
sequential ephemeral node), locks (watch predecessor to avoid herd effects), group membership,
configuration, barriers. Chubby's lessons: developers misuse locks, need caching with
invalidation, sessions/leases, and the service becomes the availability root — hence
**Physalia** (2020): many tiny Paxos cells near their clients to limit blast radius and
correlated failure.

## Pitfalls
- Implementing consensus yourself instead of using etcd/ZooKeeper/Raft libraries.
- Serving reads from the leader without lease or ReadIndex (stale after a partition).
- Committing prior-term entries by counting replicas (Raft figure 8).
- Membership changes with disjoint majorities; forgetting to persist currentTerm/votedFor/log
  before replying.
- One giant consensus group; putting hot data paths through the coordination service.

## Related
- [[distributed-systems-basics]], [[time-clocks-and-ordering]], [[consistency-models]],
  [[replication-and-partitioning]], [[distributed-databases-and-nosql]],
  [[database-recovery-and-logging]] (the log again), [[byzantine-fault-tolerance-and-blockchains]].

## Sources
Lamport 1998/2001; Ongaro & Ousterhout 2014 (esp. figs. 2, 8); Schneider 1990; Burrows 2006; Hunt et al. 2010; 6.824 L4, 6–7, 9 and labs 3–4; Brooker et al. 2020.

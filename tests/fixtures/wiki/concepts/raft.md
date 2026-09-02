---
title: Raft Consensus
type: concept
section: "4.6"
level: 400
tags: [consensus, Raft, replication, fault-tolerance, Paxos, linearizability]
sources: [raft-paper, mit-6.5840]
summary: Raft is consensus for replicated logs: a leader is elected, replicates log entries, and commits them once a majority stores them.
---

# Raft Consensus

**In one sentence.** Raft is a consensus algorithm for **replicated logs** that
solves leader election and log replication with an explicit, understandable
state machine.

## How it works

- Servers are **leaders**, **followers**, or **candidates**. Everything happens
  in **terms** (epochs); each term has at most one leader.
- **Leader election:** followers that hear no heartbeat become candidates,
  increment the term, and request votes; a majority of votes makes leader.
- **Log replication:** the leader appends client commands to its log and sends
  AppendEntries RPCs; an entry is **committed** once stored on a majority, then
  applied to the state machine.
- **Safety invariant:** if any log contains an entry at index i with term t,
  leaders of later terms also carry that entry — two-phase-commit-flavored
  majority quorums make conflicting entries impossible. A candidate with an
  out-of-date log loses the election (voters compare last log index + term).
- **Log matching property:** AppendEntries carries (prevLogIndex, prevTerm);
  if the follower disagrees it rejects, forcing a consistent-prefix repair.

## Why it matters over Paxos

Paxos proves agreement first and elapses the log problem to reconfiguration
paperwork; Raft bakes the log into the core state machine so leader election,
membership changes, and snapshotting are explicit. Both guarantee safety under
the same crash-recovery, non-Byzantine model with majority quorums.

## Pitfalls & gotchas

- Split votes and stale candidates: term check on every RPC.
- Committed ≠ applied; a crashed leader must not double-apply on restart.
- Reads: ReadIndex or leases — naive reads are not linearizable.

## Related

[[bm25]] — a search service fronted by BM25 ranking can store its index on Raft-replicated shards.
[[induction]] — Raft's safety proof is an induction over log indices and terms.

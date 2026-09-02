---
title: Replication and partitioning — leader-based, multi-leader and leaderless replication, chain replication, sharding and rebalancing, and geo-distribution
type: concept
section: "4.6"
level: 400
tags: [replication, partitioning, sharding, leader-based, primary-backup, synchronous-replication, asynchronous-replication, replication-lag, failover, multi-leader, conflict-resolution, leaderless, quorum, sloppy-quorum, hinted-handoff, read-repair, anti-entropy, gossip, merkle-trees, chain-replication, craq, hash-partitioning, range-partitioning, consistent-hashing, rebalancing, hot-spots, secondary-indexes, routing, geo-replication, primary-backup, vm-ft, gfs]
sources: [mit-6-824, distributed-systems-textbooks, distributed-systems-seminal-papers]
summary: Replication keeps copies of data on several nodes for fault tolerance, read scaling and locality — leader-based (all writes through one node, followers apply its log synchronously for durability or asynchronously for latency, with lag anomalies and failover hazards like split brain and lost writes), multi-leader (writes accepted in several datacenters, conflicts resolved by last-writer-wins, merges or CRDTs), leaderless (Dynamo: any replica accepts, W+R>N quorums, sloppy quorums with hinted handoff, read repair and Merkle-tree anti-entropy), and chain replication (writes down a chain, reads at the tail — strong consistency with high throughput; CRAQ lets any node serve clean reads); partitioning splits data across nodes by key range (ordered scans, hot spots) or hash (uniform, consistent hashing or fixed virtual partitions for rebalancing), with global or local secondary indexes, request routing (client, proxy, or coordination service), and rebalancing that moves whole partitions rather than rehashing everything.
---
# Replication and partitioning

**In one sentence.** Replication answers "what if this node dies" and partitioning answers
"what if this node isn't big enough"; the hard part of both is what happens while the copies
disagree or the shards move.

## Replication (DDIA ch. 5; Kleppmann lecture 6)
- **Leader-based (primary-backup)**: leader orders writes, ships its log (statement, WAL,
  logical/row-based, or trigger-based); followers read-only. **Synchronous** (leader waits for
  k followers — durability, latency) vs **asynchronous** (lag; a failed leader may lose
  acknowledged writes); semi-synchronous. Failover: detect (timeout), choose new leader
  (consensus or manual), reroute; hazards — lost writes, **split brain** (two leaders;
  fencing), inconsistent secondary systems (GitHub's autoincrement incident). Replication-lag
  anomalies → session guarantees ([[consistency-models]]). **VM-FT** (6.824): replicate a
  whole VM by shipping nondeterministic events in a log channel. **GFS**: primary per chunk
  orders mutations; record append at-least-once.
- **Multi-leader**: per-datacenter leaders, offline clients, collaborative editing; conflicts
  are inherent — avoid (route a record to one home), LWW (lossy), merge functions, keep all
  versions for the app, CRDTs; topologies (ring, star, all-to-all) and causality problems.
- **Leaderless** (Dynamo, Cassandra, Riak): client or coordinator writes to N replicas, waits
  for W acks; reads R replicas, takes newest by version; W+R>N ensures overlap (yet not
  linearizability under sloppy quorums, concurrent writes, or partial write failures);
  **hinted handoff**, **read repair**, **anti-entropy** with **Merkle trees**, gossip
  membership, version vectors for concurrent versions.
- **Chain replication** (van Renesse & Schneider 2004; CRAQ 2009): head accepts writes,
  propagates down the chain, tail acks and serves reads ⇒ linearizable with reads off the
  leader path; CRAQ lets every node serve reads when clean (dirty objects query the tail);
  a master (consensus service) reconfigures chains on failure. Used in Azure Storage,
  HDFS pipeline, Delta/log stores.
- **Consensus-replicated** (Raft groups per shard) — the modern NewSQL default
  ([[consensus-paxos-raft]]).

## Partitioning (DDIA ch. 6; 6.824 lab 5)
Goal: spread data and load evenly; avoid **hot spots** (celebrity keys — add random suffixes,
split hot partitions). **Key-range** partitioning (Bigtable/HBase tablets, CockroachDB ranges):
ordered scans, adaptive splits, but sequential-key hot spots (timestamps). **Hash**
partitioning: uniform; loses ranges (Cassandra: hash the partition key, range within);
**consistent hashing**/virtual nodes ([[consistent-hashing]]) or fixed number of partitions
assigned to nodes (Riak, Elasticsearch: choose many partitions up front) — never mod N.
**Secondary indexes**: document-partitioned (local — scatter/gather reads) vs term-
partitioned (global — consistent writes are harder). **Rebalancing**: move whole partitions,
throttle, avoid rehash storms; automatic rebalancing plus automatic failure detection is a
cascading-failure recipe (Cassandra manual by default). **Request routing**: any node forwards
(gossip), routing tier (ZooKeeper-backed — HBase, Kafka), or partition-aware clients; shard
controller with configuration epochs (6.824 lab 5 — reconfiguration must be linearizable and
moves must complete or roll back).

## Geo-distribution
Latency vs consistency: async cross-region followers (read locally, write far away), multi-
leader with conflict handling, or consensus groups spanning regions with leaseholders near
writers (Spanner/CockroachDB placement policies); data residency constraints; disaster
recovery RPO/RTO.

## Pitfalls
- Async replication with the belief that acknowledged = durable.
- Failover automation that promotes a lagging follower or creates two leaders.
- Hash mod N; rehashing everything on scale-out; hot keys ignored.
- Cross-partition transactions and global indexes treated as free.

## Related
- [[consistency-models]], [[consensus-paxos-raft]], [[distributed-databases-and-nosql]],
  [[consistent-hashing]], [[distributed-systems-basics]], [[database-recovery-and-logging]],
  [[cluster-scheduling-and-observability]].

## Sources
DDIA ch. 5–6; Kleppmann lecture 6; Dynamo 2007; GFS 2003; van Renesse & Schneider 2004; Terrace & Freedman (CRAQ) 2009; 6.824 L3, 13 and lab 5; Petrov part II.

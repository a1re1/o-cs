---
title: Distributed databases and NoSQL — partitioning and replication, two-phase commit, Bigtable/Dynamo/Spanner, CAP and its critique, column stores and OLAP, NewSQL, and vector databases
type: concept
section: "4.5"
level: 400
tags: [distributed-databases, sharding, partitioning, replication, two-phase-commit, 2pc, paxos-commit, distributed-transactions, nosql, key-value-store, document-store, wide-column, graph-database, bigtable, dynamo, cassandra, hbase, spanner, truetime, external-consistency, cap-theorem, linearizability, eventual-consistency, quorums, vector-clocks, newsql, cockroachdb, olap, data-warehouse, column-store, star-schema, mpp, snowflake, htap, vector-database, hnsw, one-size-fits-all, polyglot-persistence]
sources: [cmu-15-445, database-textbooks, database-seminal-papers]
summary: Scaling a database beyond one machine means partitioning data (by hash or range; naive vs consistent hashing; hot spots and rebalancing) and replicating it (leader-based with synchronous/asynchronous followers, multi-leader with conflict resolution, or leaderless Dynamo-style quorums with vector clocks and anti-entropy), then choosing how much coordination transactions get: two-phase commit for atomic multi-partition commit (blocking if the coordinator dies — Paxos/Raft-replicated coordinators fix it), Spanner's TrueTime-timestamped serializable transactions at the strong end, Dynamo/Cassandra's eventual consistency at the available end; the CAP theorem only says a linearizable single register cannot also answer every request during a partition (Kleppmann: too narrow to label systems CP or AP), so real designs are judged on isolation, latency and failure behaviour; NoSQL families (key-value, document, wide-column, graph) relax schema and joins for scale and flexibility, NewSQL restores SQL and transactions over sharded Raft groups, analytic warehouses use column stores with MPP execution and star schemas (Stonebraker's "one size fits all" is over), and vector databases add approximate-nearest-neighbour indexes for embeddings.
---
# Distributed databases and NoSQL

**In one sentence.** Once data spans machines every guarantee costs a round trip, so each
system picks which guarantees to keep — and the honest way to compare them is by isolation
level and failure behaviour, not by a two-letter CAP label.

## Architecture (15-445 L22)
Shared-memory / shared-disk (Aurora, Snowflake: storage decoupled from compute) / **shared-
nothing** (each node owns a partition). Homogeneous vs heterogeneous nodes; transparency —
the application sees one database. **Partitioning/sharding** ([[replication-and-partitioning]]):
range (ordered scans, hot spots) or hash (uniform, no ranges; consistent hashing for
rebalancing — [[consistent-hashing]]); secondary indexes local or global; co-locating
related rows (Spanner interleaving) to avoid cross-partition transactions.
**Replication**: leader-based (sync = durability, async = lag and lost writes on failover),
multi-leader (cross-datacenter; conflict resolution — last-writer-wins, CRDTs), leaderless
(Dynamo: N replicas, W+R>N quorums, sloppy quorums, hinted handoff, read repair, Merkle-tree
anti-entropy, vector clocks for concurrent versions).

## Distributed transactions (L23; DDIA ch. 9)
**Two-phase commit**: coordinator sends PREPARE, participants force their logs and vote,
coordinator logs COMMIT and sends it; correct but **blocking** if the coordinator dies after
participants prepared (they hold locks). Presumed abort/commit optimizations; **Paxos Commit**
and replicated coordinators (Spanner, CockroachDB) remove the blocking window
([[distributed-systems-basics]]). Concurrency control across partitions: distributed 2PL with
deadlock detection, T/O with hybrid logical clocks, deterministic ordering (Calvin). **Spanner**:
data in Paxos groups; read-write transactions use 2PL + 2PC; **TrueTime** gives timestamps with
bounded uncertainty ε so commit waits out ε and transactions are **externally consistent**
(linearizable order matches real time); lock-free snapshot reads at a timestamp. Consistency
words: linearizability (single-object real-time order), serializability (multi-object),
strict serializability (both), causal, eventual.

## CAP and its critique (Kleppmann 2015)
The theorem: for a single read/write register over an asynchronous network, you cannot have
**linearizability** and **availability** (every non-failing node answers every request) during a
partition. It says nothing about multi-object transactions, latency, or other faults; ACID C
≠ CAP C; "AP" systems may be arbitrarily slow and still "available". So: ask which consistency
model a system offers, how it behaves under partition, and what its latency/coordination cost
is (PACELC); test with Jepsen. HAT (Bailis 2013) enumerates what is achievable without
coordination.

## System families
| Family | Model | Examples | Origin |
|---|---|---|---|
| Key-value | opaque values, get/put, sometimes ranges | Dynamo, Riak, Redis, RocksDB (embedded) | Dynamo 2007 |
| Wide-column | sparse sorted map (row, column family, column, timestamp) | Bigtable, HBase, Cassandra | Bigtable 2006 |
| Document | JSON documents, secondary indexes, no/limited joins | MongoDB, CouchDB, DynamoDB (both) | web apps |
| Graph | nodes/edges, traversal queries (Cypher, Gremlin, SPARQL) | Neo4j, Neptune | RDF/property graphs |
| NewSQL | SQL + serializable transactions over sharded Raft/Paxos groups | Spanner, CockroachDB, TiDB, YugabyteDB, Aurora (different: shared storage) | Spanner 2012 |
| OLAP / warehouse (L24) | column stores, MPP execution, separation of storage and compute, star/snowflake schemas, push-based vectorized engines | Vertica (C-Store), Redshift, BigQuery (Dremel), Snowflake, ClickHouse, DuckDB | C-Store 2005 |
| Lakehouse / dataflow | files (Parquet) + table formats (Iceberg/Delta) + engines (Spark, Trino) | [[mapreduce-and-dataflow]] | MapReduce 2004 |
| Vector | embeddings with ANN indexes (HNSW, IVF-PQ) + filters | pgvector, Milvus, Pinecone, FAISS | [[similarity-search-and-lsh]] |
| Stream / time-series | append-heavy, windowed queries | Kafka/ksql, Flink, InfluxDB, TimescaleDB | [[mapreduce-and-dataflow]] |
"One size fits all" (Stonebraker 2005): OLTP row stores, OLAP column stores, streams and
text engines each win by 10–100× in their niche; HTAP systems (TiDB, SingleStore, Unistore)
try to recombine them; polyglot persistence vs operational simplicity.

## Pitfalls
- Choosing NoSQL for "scale" you don't have and losing joins and transactions you did need.
- Eventual consistency surprising users (read-your-writes needs session guarantees).
- Cross-shard transactions and hot partitions (celebrity keys); resharding without consistent
  hashing.
- Trusting vendor CAP claims and isolation defaults; not running Jepsen-style tests.

## Related
- [[replication-and-partitioning]], [[distributed-systems-basics]], [[consistent-hashing]],
  [[transactions-and-concurrency-control]], [[storage-engines-and-indexes]],
  [[mapreduce-and-dataflow]], [[similarity-search-and-lsh]], [[query-optimization]].

## Sources
15-445 L22–24; DDIA ch. 5–6, 9; Bigtable 2006; Dynamo 2007; Spanner 2012; C-Store 2005; Stonebraker 2005; Bailis et al. 2013; Kleppmann 2015.

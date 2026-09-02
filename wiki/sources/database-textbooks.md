---
title: Database texts — Silberschatz's Database System Concepts, Ramakrishnan & Gehrke, the Red Book (Readings in Database Systems), Kleppmann's Designing Data-Intensive Applications, Hellerstein et al. Architecture of a Database System, Gray & Reuter Transaction Processing, and Use The Index, Luke
type: source
section: "4.5"
level: 300
tags: [database-textbook, silberschatz, ramakrishnan-gehrke, cow-book, red-book, ddia, kleppmann, hellerstein, architecture-of-a-database-system, gray-reuter, transaction-processing, use-the-index-luke, sql-performance]
sources: []
authors: [Abraham Silberschatz, Henry Korth, S. Sudarshan, Raghu Ramakrishnan, Johannes Gehrke, Peter Bailis, Joseph Hellerstein, Michael Stonebraker, Martin Kleppmann, Jim Gray, Andreas Reuter, Markus Winand]
year: 2017
institution: various
url: http://www.redbook.io/
license: mixed (Red Book, Hellerstein, Use The Index Luke free)
format: html
summary: Silberschatz and Ramakrishnan & Gehrke are the standard courses in a book (relational model, SQL, design/normalization, storage and indexing, query processing and optimization, transactions, concurrency, recovery, distributed and parallel databases); the Red Book (5th ed., free) curates the seminal papers with editorial essays by Bailis, Hellerstein and Stonebraker; Hellerstein, Stonebraker & Hamilton's Architecture of a Database System (free) describes a real DBMS's components — process model, parallel architecture, storage manager, transactions (locking, latching, logging, buffer pool), query processor (parser, rewriter, optimizer, executor, access methods), shared services; Kleppmann's DDIA bridges databases and distributed systems (data models, storage engines, encoding, replication, partitioning, transactions, consistency and consensus, batch and stream processing); Gray & Reuter is the transaction-processing bible; and Use The Index, Luke (free) teaches developers how B-tree indexes make SQL fast.
---
# Database textbooks

## What they are
- **Silberschatz, Korth & Sudarshan** (7th ed.): I introduction and relational model/SQL;
  II database design (E-R, normalization — functional dependencies, BCNF/3NF, multivalued
  dependencies); III application design; IV big data analytics; V storage management and
  indexing (disks/SSDs, file organization, buffers, B+trees, hashing, bitmap/spatial indexes);
  VI query processing and optimization (algorithms, cost estimation, equivalence rules, join
  ordering); VII transaction management (concurrency control — locking, timestamps,
  validation, MVCC, snapshot isolation; recovery — ARIES); VIII parallel and distributed
  databases; IX advanced topics.
- **Ramakrishnan & Gehrke** (the "cow book"): same territory, stronger on internals and query
  optimization; used by CS186.
- **Red Book** (Bailis, Hellerstein, Stonebraker): chapters on background, traditional RDBMS
  systems (System R, POSTGRES), techniques everyone should know (access path selection,
  ARIES, Gray's granularity of locks, Kung & Robinson OCC), new DBMS architectures (C-Store,
  H-Store), large-scale dataflow (MapReduce and critiques, Spark), weak isolation and
  distribution (Berenson et al. isolation critique, HAT, Dynamo), query optimization
  (Volcano/Cascades, eddies), interactive analytics (online aggregation, cubes), languages
  (Datalog), web data.
- **Architecture of a Database System** (Hellerstein, Stonebraker, Hamilton 2007): five main
  components — client communications manager; process manager (process-per-worker, thread-
  per-worker, process pool; admission control); relational query processor (parsing/
  authorization, query rewrite, optimizer — Selinger and Cascades descendants, executor —
  iterator model, access methods, data warehousing extensions); transactional storage manager
  (ACID, serializability via 2PL, latches vs locks, isolation levels, log manager with ARIES,
  buffer pool with steal/no-force); shared components (catalog, memory allocator, replication,
  administration/monitoring). Also parallel architectures (shared memory / shared disk /
  shared nothing) and the case for and against threads.
- **DDIA** (Kleppmann 2017): I foundations — reliability/scalability/maintainability, data
  models (relational vs document vs graph), storage and retrieval (LSM vs B-tree, column
  stores), encoding (JSON/Protobuf/Avro, schema evolution); II distributed data — replication
  (leader, multi-leader, leaderless), partitioning, transactions (weak isolation, serializable
  via SSI/2PL/actual serial), the trouble with distributed systems (clocks, faults, partial
  failure), consistency and consensus (linearizability, ordering, 2PC, Raft/Paxos); III
  derived data — batch (MapReduce), stream processing, the future (unbundling).
- **Gray & Reuter** (1993): fault tolerance, transaction models, locking theory, logging and
  recovery, TP monitors — the authoritative source on ACID mechanics.
- **Use The Index, Luke** (Winand): B-tree anatomy, index-only scans, function-based indexes,
  `LIKE` and range predicates, join order, sorting via index, pagination (keyset vs offset) —
  the developer's guide to `EXPLAIN`.

## Key ideas → pages
[[relational-model]], [[storage-engines-and-indexes]], [[query-optimization]],
[[transactions-and-concurrency-control]], [[database-recovery-and-logging]],
[[distributed-databases-and-nosql]], [[replication-and-partitioning]].

## What they add
Hellerstein's survey is the map; Silberschatz/R&G the syllabus; the Red Book the primary
literature; DDIA the modern synthesis; Winand the everyday practice.

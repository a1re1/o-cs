---
title: Database seminal papers — Codd (1970), Bayer & McCreight B-trees (1972), Gray granularity of locks (1976), Selinger System R optimizer (1979), Bernstein & Goodman (1981), POSTGRES (1986), ARIES (1992), Berenson isolation critique (1995), LSM-tree (1996), MapReduce (2004), C-Store and One Size Fits All (2005), Bigtable (2006), Dynamo (2007), Spanner (2012), Spark (2012), HAT (2013), Kleppmann on CAP (2015)
type: source
section: "4.5"
level: 500
tags: [codd, relational-model, b-tree, bayer-mccreight, granularity-of-locks, gray, selinger, system-r, query-optimization, bernstein-goodman, postgres, stonebraker, aries, mohan, lsm-tree, oneil, mapreduce, c-store, column-store, one-size-fits-all, bigtable, dynamo, spanner, spark, hat, bailis, cap, kleppmann, isolation-levels, berenson]
sources: []
authors: [Edgar Codd, Rudolf Bayer, Edward McCreight, Jim Gray, Patricia Selinger, Philip Bernstein, Nathan Goodman, Michael Stonebraker, C. Mohan, Hal Berenson, Patrick O'Neil, Jeffrey Dean, Sanjay Ghemawat, Daniel Abadi, Fay Chang, Giuseppe DeCandia, James Corbett, Matei Zaharia, Peter Bailis, Martin Kleppmann]
year: 1970
institution: various
url: http://www.redbook.io/
license: various
format: pdf
summary: Codd introduced relations, normal form and data independence (freedom from ordering, indexing and access-path dependence) so programs survive representation changes; B-trees gave the balanced, disk-block-sized index; Gray's granularity of locks introduced intention locks and the hierarchy of lock modes (and, with Gray's degrees of consistency, isolation levels); Selinger's System R optimizer introduced cost-based access-path selection with dynamic programming over left-deep join orders and "interesting orders"; Bernstein & Goodman surveyed concurrency control (2PL, timestamp ordering, validation) as serializability theory; POSTGRES added extensible types, rules and no-overwrite storage; ARIES made write-ahead logging with steal/no-force practical via repeating history, per-page LSNs, compensation log records and fuzzy checkpoints; Berenson et al. showed the ANSI isolation levels were ambiguous and defined snapshot isolation and its write skew; the LSM-tree traded read cost for sequential-write throughput; MapReduce, Bigtable, Dynamo and Spanner defined Google/Amazon-scale storage (respectively batch dataflow, sorted wide-column store on GFS, eventually consistent Dynamo-style key-value with consistent hashing and vector clocks, and globally serializable transactions with TrueTime); C-Store and "One Size Fits All" argued for column stores and specialized engines; Spark added in-memory resilient distributed datasets; HAT catalogued which isolation guarantees are achievable highly available; and Kleppmann argued CAP's definitions are too narrow to classify real databases.
---
# Database seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Codd, "A Relational Model of Data for Large Shared Data Banks" (1970) | Users "must be protected from having to know how the data is organized in the machine"; three dependencies to remove — **ordering, indexing, access path**; n-ary relations, normal form (no repeating groups), a universal data sublanguage based on predicate calculus; derivability, redundancy, consistency; the "connection trap" | [[relational-model]] |
| Bayer & McCreight, "Organization and Maintenance of Large Ordered Indices" (1972) | The B-tree: high-fanout balanced tree of disk pages, logarithmic search/insert/delete with splits and merges | [[balanced-search-trees]], [[storage-engines-and-indexes]] |
| Gray, Lorie, Putzolu, Traiger, "Granularity of Locks and Degrees of Consistency" (1976) | Lock hierarchy (database → file → page → record) with **intention locks** (IS/IX/SIX); degrees of consistency 0–3 → isolation levels | [[transactions-and-concurrency-control]] |
| Selinger et al., "Access Path Selection in a Relational DBMS" (System R, 1979) | Cost-based optimization: statistics, selectivity estimates, cost = I/O + CPU, dynamic programming over left-deep join orders, interesting orders | [[query-optimization]] |
| Bernstein & Goodman, "Concurrency Control in Distributed Database Systems" (1981) | Serializability theory and the taxonomy of 2PL, timestamp ordering, and their combinations | [[transactions-and-concurrency-control]] |
| Stonebraker & Rowe, "The Design of POSTGRES" (1986) | Abstract data types, rules/triggers, no-overwrite (versioned) storage, procedures — the extensible DBMS; became PostgreSQL | [[storage-engines-and-indexes]] |
| Mohan et al., "ARIES" (1992) | WAL with steal/no-force buffer management; **repeating history** on restart (analysis, redo everything, undo losers); page LSNs; compensation log records chained via prevLSN for bounded logging under repeated crashes; fuzzy checkpoints; fine-grained locking and partial rollback | [[database-recovery-and-logging]] |
| Berenson et al., "A Critique of ANSI SQL Isolation Levels" (1995) | Anomalies (dirty write/read, fuzzy read, phantom, lost update, read/write skew); defines snapshot isolation and shows it is not serializable | [[transactions-and-concurrency-control]] |
| O'Neil et al., "The Log-Structured Merge-Tree" (1996) | Buffer writes in memory, flush sorted runs, merge levels — sequential I/O for writes; RocksDB, LevelDB, Cassandra | [[storage-engines-and-indexes]] |
| Dean & Ghemawat, "MapReduce" (2004) | Map/shuffle/reduce with fault tolerance by re-execution; critiqued by DeWitt & Stonebraker for ignoring DB lessons (indexes, schemas) | [[mapreduce-and-dataflow]] |
| Stonebraker et al., "C-Store" (2005); Stonebraker & Çetintemel, "One Size Fits All: An Idea Whose Time Has Come and Gone" (2005) | Column storage with compression and projections for analytics; specialized engines (OLTP, OLAP, streams, text) beat one general DBMS | [[storage-engines-and-indexes]], [[distributed-databases-and-nosql]] |
| Chang et al., "Bigtable" (2006) | Sparse sorted multidimensional map, tablets on GFS, SSTables + memtable (an LSM), Chubby for coordination; HBase | [[distributed-databases-and-nosql]] |
| DeCandia et al., "Dynamo" (2007) | Always-writeable key-value store: consistent hashing, vector clocks, sloppy quorums, hinted handoff, anti-entropy via Merkle trees; Cassandra, Riak | [[distributed-databases-and-nosql]], [[consistent-hashing]] |
| Corbett et al., "Spanner" (2012) | Globally distributed, externally consistent transactions via Paxos groups, 2PL + 2PC, and **TrueTime** bounded clock uncertainty | [[distributed-databases-and-nosql]] |
| Zaharia et al., "Resilient Distributed Datasets" (Spark, 2012) | In-memory dataflow with lineage-based fault tolerance | [[mapreduce-and-dataflow]] |
| Bailis et al., "Highly Available Transactions" (2013) | Which isolation levels can be provided without coordination (read committed, monotonic atomic view) vs which cannot (serializability, snapshot isolation) | [[transactions-and-concurrency-control]], [[distributed-systems-basics]] |
| Kleppmann, "Please Stop Calling Databases CP or AP" (2015) | CAP's C is linearizability, A is every non-failing node answers, the model is a single register; real systems need finer vocabulary (linearizable vs not, availability vs latency) | [[distributed-databases-and-nosql]], [[distributed-systems-basics]] |

## Why read them
Codd for the abstraction, Selinger and ARIES for how the two hardest subsystems actually
work, Berenson for why "isolation level" is a trap, Dynamo/Spanner for the two poles of
distributed data, Kleppmann for clear thinking.

---
title: MapReduce, GFS/HDFS, Spark and dataflow — batch and stream processing at scale
type: concept
section: "4.6"
level: 400
tags: [mapreduce, gfs, hdfs, batch-processing, shuffle, combiners, stragglers, speculative-execution, fault-tolerance-by-reexecution, spark, rdd, lineage, dag-scheduler, dataframes, dataflow, stream-processing, flink, kafka, event-time, processing-time, watermarks, windows, exactly-once, checkpointing, dryad, flumejava, beam, lambda-architecture, kappa-architecture, dewitt-stonebraker-critique]
sources: [mit-6-824, database-seminal-papers, distributed-systems-seminal-papers]
summary: MapReduce (Dean & Ghemawat 2004) let non-experts run computations over petabytes on thousands of unreliable machines by restricting programs to a map phase (key/value in, intermediate key/value out), a shuffle that groups by key, and a reduce phase, with a master scheduling tasks near their GFS/HDFS data, re-executing failed tasks (deterministic, idempotent), and speculatively duplicating stragglers; database people (DeWitt & Stonebraker) objected that it rediscovered parallel DBMS techniques without indexes or schemas, and the answer was higher-level dataflow — Spark's resilient distributed datasets (immutable partitioned collections with lineage for recovery, a DAG scheduler, in-memory caching for iterative jobs, DataFrames with an optimizer), Dryad/FlumeJava/Beam pipelines — and stream processing (Kafka logs as the substrate; Flink/Beam with event time vs processing time, watermarks, windows, checkpointed state for exactly-once semantics), which unify with batch as processing of bounded vs unbounded data.
---
# MapReduce and dataflow

**In one sentence.** Constrain the programming model enough (pure map, group-by-key, reduce
over an immutable input) and fault tolerance, parallelism and locality become the runtime's
problem instead of the programmer's.

## GFS (2003; 6.824 L3)
Assumptions: component failure is normal; huge files; mostly appends and large sequential
reads. Single **master** holds metadata in memory (namespace, chunk → chunkservers) with an
operation log replicated for recovery; **chunks** of 64 MB replicated 3×; clients get chunk
locations then talk to chunkservers directly; a lease designates a **primary** replica that
orders mutations; **record append** at-least-once (duplicates and padding possible — clients
handle) — a deliberately relaxed consistency model. HDFS copies it (NameNode/DataNode).
Lessons: single master limits scale (Colossus shards metadata); relaxed semantics push
complexity to applications.

## MapReduce (2004; 6.824 lab 1)
`map(k1, v1) → list(k2, v2)`; shuffle groups by k2 (partition by hash(k2) mod R, sorted);
`reduce(k2, list(v2)) → list(v3)`. Master assigns M map tasks (reading local GFS chunks) and R
reduce tasks; intermediate files on map workers' disks; reducers fetch, sort, reduce.
**Fault tolerance**: worker failure ⇒ re-execute its tasks (map outputs lost with the disk);
master failure ⇒ restart the job (later: checkpoint); deterministic functions make re-execution
safe; atomic renames of reduce outputs. **Stragglers** ⇒ backup tasks near the end. Combiners
(local pre-reduce), counters, custom partitioners (total order via sampling — TeraSort).
Examples: grep, URL count, inverted index, reverse links, sort. Hadoop as the open-source
implementation; Hive/Pig as SQL/scripting on top. **The critique** (DeWitt & Stonebraker 2008):
no schema, no indexes, brute-force full scans, materializing intermediates — parallel DBMSs
were faster; MapReduce's reply: fault tolerance at scale, semistructured data, ease. Both
were right; the field converged on engines with optimizers *and* elastic fault tolerance.

## Spark and DAG dataflow (Zaharia 2012)
**RDDs**: immutable, partitioned collections built by deterministic transformations (map,
filter, join, groupByKey) from stable storage or other RDDs; recovery by recomputing lost
partitions from **lineage** (no replication of intermediates); persist in memory for iterative
algorithms (PageRank, ML — 10–100× over Hadoop); narrow vs wide dependencies determine stages;
a **DAG scheduler** pipelines narrow ops and shuffles at wide ones. Actions trigger lazy
evaluation ([[streams-and-lazy-evaluation]]). DataFrames/Datasets + Catalyst optimizer
([[query-optimization]]) + Tungsten code generation; SQL, MLlib, GraphX, Structured Streaming.
Predecessors: Dryad (arbitrary DAGs), FlumeJava (pipelines with deferred evaluation); Beam
unifies batch/stream over Flink/Dataflow. Ray (6.824 L18) generalizes to dynamic task graphs
and actors for ML.

## Stream processing (DDIA ch. 11)
Events in append-only **logs** (Kafka: partitioned, replicated, consumer offsets — the
distributed [[database-recovery-and-logging]] log as a product); processing: **event time** vs
**processing time**; **windows** (tumbling, hopping, sliding, session); **watermarks** for
lateness; stateful operators with **checkpointed state** (Chandy–Lamport barriers in Flink —
[[time-clocks-and-ordering]]) for **exactly-once** *effects* (at-least-once + idempotent/
transactional sinks); joins (stream-stream, stream-table); change data capture makes
databases into streams (Debezium); materialized views maintained incrementally
(Materialize/differential dataflow). Architectures: lambda (batch + speed layers) → kappa
(reprocess the log).

## Pitfalls
- Non-deterministic or side-effecting map/reduce functions (re-execution duplicates effects).
- Data skew (one hot key on one reducer); tiny files; shuffles of everything.
- Treating Spark caching as free; collecting to the driver.
- Processing-time windows for event-time questions; unbounded state without TTL.

## Related
- [[replication-and-partitioning]], [[distributed-databases-and-nosql]], [[query-optimization]],
  [[streams-and-lazy-evaluation]], [[time-clocks-and-ordering]], [[cluster-scheduling-and-observability]],
  [[parallel-architectures-simd-gpu]].

## Sources
Ghemawat et al. 2003; Dean & Ghemawat 2004; Zaharia et al. 2012; DeWitt & Stonebraker 2008; DDIA ch. 10–11; 6.824 L1, 3, 18 and lab 1; Akidau et al. "The Dataflow Model" 2015.

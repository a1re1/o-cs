---
title: Query processing and optimization — execution models, join and sort algorithms, rewriting, cost-based planning, and cardinality estimation
type: concept
section: "4.5"
level: 400
tags: [query-processing, query-execution, iterator-model, volcano, materialization-model, vectorized-execution, compiled-queries, access-methods, sequential-scan, index-scan, external-merge-sort, hashing, aggregation, nested-loop-join, block-nested-loop, index-nested-loop, sort-merge-join, hash-join, grace-hash-join, query-optimization, query-rewrite, predicate-pushdown, projection-pushdown, join-ordering, selinger, dynamic-programming, left-deep, cost-model, statistics, histograms, selectivity, cardinality-estimation, cascades, explain, query-plans, parallel-query]
sources: [cmu-15-445, database-textbooks, database-seminal-papers]
summary: A query is parsed into a relational-algebra tree, rewritten with equivalence rules (push selections and projections down, unnest subqueries, eliminate redundant joins), then a cost-based optimizer (Selinger's System R: statistics and histograms → selectivity estimates → I/O+CPU cost, dynamic programming over join orders, left-deep trees, interesting orders; Volcano/Cascades generalize with transformation rules and memoization) picks a physical plan of access methods (sequential vs index scan), joins (nested-loop, index nested-loop, sort-merge, hash/Grace hash — hash join wins for equi-joins that fit partitions in memory) and external sorts/hash aggregation; the executor runs the plan under the iterator (Volcano, tuple-at-a-time), materialization, or vectorized (batch-at-a-time, SIMD-friendly) model — or compiles it to machine code — and cardinality estimation errors, which compound exponentially through joins, are why plans go wrong and why `EXPLAIN ANALYZE` exists.
---
# Query processing and optimization

**In one sentence.** Declarative SQL is only fast because the system searches a space of
equivalent plans with a cost model — and the cost model is only as good as its guesses about
how many rows come out of each operator.

## Pipeline
SQL → parser → binder (catalog: names, types) → logical plan (relational algebra tree) →
rewriter (rule-based) → optimizer (cost-based physical plan) → executor. Prepared statements
cache plans (parameter sniffing hazards). `EXPLAIN` shows the plan; `EXPLAIN ANALYZE` shows
estimated vs actual rows — the first thing to read when a query is slow.

## Execution (15-445 L11–14; Hellerstein §4)
- **Processing models**: **iterator/Volcano** — every operator implements `open/next/close`,
  pulling one tuple at a time (simple, pipelined, function-call overhead); **materialization**
  — each operator produces its whole output (fine for OLTP point queries); **vectorized** —
  batches of ~1k tuples with tight loops over columns (MonetDB/X100, DuckDB, ClickHouse;
  SIMD-friendly — [[parallel-architectures-simd-gpu]]); **compiled** (HyPer, Umbra) —
  generate LLVM/machine code per query, data-centric pipelines. Pipeline breakers: sort, hash
  build, aggregation.
- **Access methods**: sequential scan (with zone maps, buffer pool bypass), index scan, index-
  only scan, bitmap scan (multiple indexes ANDed), predicate pushdown into scans.
- **Sorting**: external merge sort (runs of memory size, k-way merge; B buffers ⇒ ⌈log_{B−1}(N/B)⌉
  passes); top-N via heap. **Aggregation**: sort-based or hash-based (partition when too big).
- **Joins** (L12): nested loop O(N·M) pages, block nested loop (buffer as much of outer as
  fits), index nested loop (probe an index per outer tuple — good for small outer/selective),
  **sort-merge** (sort both, merge; ideal when inputs are sorted or output must be), **hash
  join** (build hash table on the smaller input, probe with the larger; **Grace/hybrid hash**
  partitions both to disk when they don't fit; Bloom filters on the build side; the default for
  equi-joins). Non-equi joins fall back to nested loops.
- **Parallelism**: intra-operator (partition data across threads — exchange operators), inter-
  operator (pipelines), inter-query; NUMA awareness; morsel-driven scheduling.

## Optimization (L15; Selinger 1979)
- **Rewrite rules**: predicate pushdown, projection pruning, constant folding, subquery
  unnesting/decorrelation (turn correlated subqueries into joins), view merging, join
  elimination, `OR` → `UNION`, redundant sort removal.
- **Cost-based search**: enumerate join orders — n! bushy trees; System R restricts to
  left-deep, uses **dynamic programming** on subsets (optimal subplans compose), keeps plans with
  **interesting orders** (sorted output useful later); heuristics/genetic search beyond ~12
  tables (Postgres GEQO). **Cascades/Volcano** (SQL Server, CockroachDB, Calcite): top-down,
  rule-driven, memoized groups of equivalent expressions.
- **Cost model**: I/O (sequential vs random page reads), CPU per tuple, memory, network for
  distributed; **statistics**: row counts, distinct values, min/max, **histograms** (equi-
  width/depth), sketches (HyperLogLog, [[streaming-and-sketching]]), sampling; **selectivity**
  under uniformity and independence assumptions — both wrong for correlated columns, so
  estimates degrade multiplicatively across joins ("How good are query optimizers, really?" —
  Leis 2015: cardinality errors dominate, cost models matter less). Fixes: multi-column stats,
  adaptive query execution, learned estimators, eddies.

## Pitfalls
- Stale statistics (`ANALYZE`); non-sargable predicates (`WHERE f(col) = …`); implicit casts.
- N+1 query patterns from ORMs; `SELECT *` defeating index-only scans.
- Assuming the optimizer sees through views/CTEs (optimization fences in some engines).
- Hash joins spilling because of underestimated build sides; nested loops chosen on wrong
  estimates — check estimated vs actual rows.

## Related
- [[relational-model]], [[storage-engines-and-indexes]], [[sorting]], [[hash-tables]],
  [[dynamic-programming]], [[streaming-and-sketching]], [[distributed-databases-and-nosql]].

## Sources
15-445 L11–15; Selinger et al. 1979; Graefe "Volcano"/"Cascades"; Hellerstein et al. §4; Silberschatz ch. 15–16; Leis et al. 2015.

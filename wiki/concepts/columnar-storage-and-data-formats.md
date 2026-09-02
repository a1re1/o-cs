---
title: Columnar Storage and Data Formats
type: concept
section: "10.2"
level: 400
tags: [columnar-storage, parquet, arrow, data-lake, lakehouse, olap, vectorized-execution]
sources: [big-data-mining-texts-and-papers]
summary: Why analytical systems store data by column, not row — compression, scan efficiency, and vectorized execution — plus Parquet, Arrow, and the data-lake/lakehouse architecture.
---

# Columnar Storage and Data Formats
**In one sentence.** Analytical (OLAP) systems store each column's values contiguously
rather than each row's, so a query that touches a few columns reads only those, and
runs of similar values compress far better — the foundation of Parquet, Arrow, and
modern data warehouses.

## Why it matters
Analytics scans huge tables but usually needs only a handful of columns and aggregates
them. Row storage forces reading whole rows; columnar storage reads 10–100× less data
and enables vectorized, cache-friendly execution. It is why Parquet/Arrow, column
stores, and lakehouses dominate data engineering. Contrast with row-oriented
[[storage-engines-and-indexes]] built for OLTP point lookups.

## How it works
**Row vs column layout.** Row stores (`OLTP`, [[storage-engines-and-indexes]]) keep a
record's fields together — great for "fetch/update this row." Column stores keep all
values of one column together — great for "sum this column over a billion rows."

**Why columnar wins for analytics:**
- **Projection** — read only the columns the query references, skipping the rest on disk.
- **Compression** — a column is homogeneous (all the same type, often low cardinality),
  so run-length, dictionary, and bit-packing encodings shrink it dramatically; less data
  = less I/O.
- **Vectorized execution** — process a column in tight SIMD loops over contiguous arrays
  instead of interpreting one row at a time; see [[parallel-architectures-simd-gpu]].
- **Predicate pushdown & statistics** — per-block min/max and zone maps let the reader
  skip blocks that can't match a filter.

**Parquet** — the on-disk columnar file format: row groups split into column chunks and
pages, with per-column encoding, compression, and statistics. **Arrow** — the in-memory
columnar standard: a language-agnostic layout that lets systems share data with
**zero-copy** (no serialization) across pandas, Spark, DuckDB, etc.

**Data lake → lakehouse.** A **data lake** is cheap object storage (S3) holding raw
files (often Parquet). It lacks transactions and schema enforcement, so **table formats**
— Delta Lake, Apache Iceberg, Hudi — add ACID transactions, schema evolution, and time
travel over those files, giving the **lakehouse**: warehouse semantics on lake storage.

## Complexity & trade-offs
- Columnar is **write-once/append, read-many**: excellent for scans and aggregates,
  poor for row-level updates and point lookups (which OLTP row stores handle).
- Reconstructing whole rows requires stitching many columns — costly, so avoid
  `SELECT *` on wide columnar tables.
- More compression saves I/O but costs CPU to decode; the balance favors compression
  because analytics is usually I/O-bound.

## Pitfalls & gotchas
- **Small-files problem** — many tiny Parquet files kill scan performance; compact them.
- **`SELECT *`** defeats the projection advantage — name the columns you need.
- **Schema evolution** without a table format (adding/renaming columns across files)
  breaks readers; use Iceberg/Delta.
- **Row-level updates** on a lake are expensive rewrites; batch them or use a table
  format's merge.

## Worked example
A 1 TB event table with 50 columns. Query: average latency by day. Row storage reads
all 1 TB. Parquet reads only the `day` and `latency` columns — say 40 GB — skips row
groups whose min/max `day` excludes the range, decodes them into Arrow arrays, and sums
them with vectorized SIMD, finishing orders of magnitude faster.

## Related
- [[storage-engines-and-indexes]] — row-oriented OLTP storage, the contrast.
- [[mapreduce-and-dataflow]] — engines (Spark) read Parquet/Arrow columnar data.
- [[parallel-architectures-simd-gpu]] — vectorized execution over columns.
- [[data-wrangling-and-tidy-data]] — Arrow backs fast dataframes.

## Sources
Distilled from [[big-data-mining-texts-and-papers]] (MMDS; Parquet/Arrow docs; lakehouse literature).

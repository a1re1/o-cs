---
title: Storage engines and indexes — pages, buffer pools, heap files, B+trees, hash indexes, LSM-trees, column stores, and compression
type: concept
section: "4.5"
level: 400
tags: [storage-engine, disk-oriented, pages, slotted-pages, heap-file, tuples, buffer-pool, replacement-policy, lru-k, clock, mmap, b-plus-tree, clustered-index, secondary-index, covering-index, hash-index, extendible-hashing, lsm-tree, memtable, sstable, compaction, write-amplification, read-amplification, bloom-filter, column-store, row-store, pax, compression, dictionary-encoding, run-length, index-organized, latch-crabbing, use-the-index-luke]
sources: [cmu-15-445, database-textbooks, database-seminal-papers]
summary: A disk-oriented storage engine keeps data in fixed-size pages (slotted pages of variable-length tuples in heap files, or index-organized), moves them through a buffer pool that it manages itself (page table, pins, dirty bits, LRU-K/CLOCK eviction — not mmap, because the DBMS needs control of write ordering for recovery), and reaches tuples through indexes: B+trees (high fanout, sorted, range scans; clustered vs secondary; covering indexes; concurrent via latch crabbing), hash indexes (equality only), and Bloom filters; write-heavy engines use LSM-trees (in-memory memtable → sorted immutable SSTables merged by leveled or tiered compaction, trading read and space amplification for sequential writes); analytics engines store columns (compression via dictionary/RLE/bit-packing, only needed columns read, vectorized scans) while OLTP stores rows — and PAX/hybrid layouts sit between.
---
# Storage engines and indexes

**In one sentence.** The engine's whole job is to make the disk look like memory without
losing control of when bytes reach it — and an index is a second copy of the data in an order
the query wants.

## Pages and files (15-445 L03–05)
Storage hierarchy: the DBMS assumes data lives on non-volatile storage and copies pages
(4–16 KB) into memory; sequential I/O ≫ random on disks, less so on SSDs; NVM blurs it.
**Heap files** of unordered pages tracked by a directory/free-space map; **slotted pages** —
header, slot array growing forward, tuples growing backward; tuple = header (nulls, visibility
bits for MVCC) + attributes, fixed-length first; large values via overflow pages/TOAST;
record ids (page, slot). Alternatives: **log-structured** (append records, index to latest,
compact) and **index-organized** (tuples stored in the B+tree leaves — MySQL InnoDB, SQLite).
**Storage models**: NSM (row store — OLTP: whole tuple in one place, fast point writes), DSM
(column store — OLAP: only needed columns read, great compression, vectorization), PAX/hybrid
(row groups with columns inside — Parquet, ORC). Compression: dictionary (most important,
allows predicates on codes), RLE, bit-packing, delta, null suppression; late materialization.

## Buffer pool (L06)
Frames + page table (page id → frame) with **pin counts** and **dirty flags**; replacement
**LRU-K**/CLOCK/2Q resistant to sequential flooding; prefetching, scan sharing, buffer pool
bypass. Why not `mmap`: transactional safety (the OS may flush dirty pages any time,
breaking WAL ordering), I/O stalls, error handling, TLB shootdowns ("Are You Sure You Want to
Use MMAP in Your DBMS?"). The pool is the OS's page cache reimplemented with the knowledge the
OS lacks ([[caches-and-memory-hierarchy]], [[virtual-memory]]).

## Indexes (L07–10)
- **B+tree**: all values in leaves (linked for range scans), internal nodes route; fanout in the
  hundreds ⇒ 3–4 levels for billions of keys; splits/merges keep balance; key compression,
  suffix truncation; **clustered** (heap ordered by the key — one per table) vs **secondary**
  (leaf holds record ids or primary keys — extra lookup); **covering index** (all needed columns
  in the index — index-only scan); composite keys and the leftmost-prefix rule; function/
  partial indexes. Concurrency: **latch crabbing** (hold parent latch until the child is safe),
  optimistic descent, B-link trees. Winand: an index helps `WHERE`, `JOIN`, `ORDER BY`,
  `LIMIT`; `LIKE '%x'` and functions on columns defeat it; keyset pagination over `OFFSET`.
  ([[balanced-search-trees]])
- **Hash indexes**: static (linear probing, cuckoo) or dynamic (extendible, linear hashing);
  O(1) equality, no ranges. **Bloom filters** to skip lookups. Skip lists, radix/ART tries and
  learned indexes in memory-optimized engines ([[tries]], [[hash-tables]]).
- Bitmap indexes and zone maps for analytics; inverted indexes for text
  ([[search-engines-and-ranking]]); R-trees/spatial; vector indexes (HNSW) in vector DBs.

## LSM-trees (O'Neil 1996; DDIA ch. 3)
Writes go to a WAL and an in-memory sorted **memtable**; when full, flush as an immutable sorted
**SSTable**; reads check memtable then SSTables newest-first (Bloom filters per file);
background **compaction** merges files — **leveled** (RocksDB: each level 10× larger, low space
amplification) or **tiered** (Cassandra: fewer merges, more space). Trade-offs: write
amplification (compaction rewrites), read amplification (multiple files), space amplification —
the RUM conjecture: you can optimize two of read, update, memory. Versus B+trees: LSM wins
sequential write throughput and compression; B+tree wins read latency and predictability.
Lineage: [[file-systems]] (LFS) → flash FTLs → LSM.

## Pitfalls
- Indexing every column (write cost, planner confusion); missing composite-index prefix order.
- Relying on `mmap` or the OS cache for durability guarantees.
- Ignoring write amplification on SSDs; compaction stalls; tombstones in LSMs.
- Row stores for scans of wide tables; column stores for point updates.

## Related
- [[relational-model]], [[query-optimization]], [[database-recovery-and-logging]],
  [[transactions-and-concurrency-control]], [[balanced-search-trees]], [[hash-tables]],
  [[file-systems]], [[caches-and-memory-hierarchy]], [[distributed-databases-and-nosql]].

## Sources
15-445 L03–10; Silberschatz ch. 12–14; DDIA ch. 3; Bayer & McCreight 1972; O'Neil et al. 1996; Use The Index, Luke; Hellerstein et al. §5.

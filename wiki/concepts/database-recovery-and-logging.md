---
title: Database logging and recovery — write-ahead logging, steal/no-force, checkpoints, and ARIES (analysis, redo by repeating history, undo with compensation log records)
type: concept
section: "4.5"
level: 400
tags: [recovery, logging, write-ahead-logging, wal, steal, no-force, force, no-steal, undo, redo, log-sequence-number, lsn, page-lsn, compensation-log-records, clr, checkpoints, fuzzy-checkpoint, dirty-page-table, active-transaction-table, aries, repeating-history, shadow-paging, group-commit, fsync, durability, media-recovery, physiological-logging, crash-consistency]
sources: [cmu-15-445, database-textbooks, database-seminal-papers]
summary: Durability and atomicity across crashes come from the log — the DBMS writes a log record describing each change (with a monotonically increasing LSN) to stable storage before the corresponding data page can be written (write-ahead logging) and before commit is acknowledged (force the log, not the data), which lets the buffer pool use the fast steal/no-force policy (evict dirty pages of uncommitted transactions; don't flush at commit) at the cost of needing both undo and redo; ARIES restarts in three passes — analysis (rebuild the dirty page table and active transaction table from the last fuzzy checkpoint), redo (repeat history: reapply every logged update whose LSN exceeds the page's stored LSN, even those of losers), undo (roll back losers newest-first, writing compensation log records chained by prevLSN so that rollbacks are themselves logged and a crash during recovery does bounded extra work) — and the same design underlies journaling file systems and replication logs.
---
# Database logging and recovery

**In one sentence.** Write what you are about to do to an append-only log before you do it;
after a crash, replay the log forward to where you were, then undo whoever hadn't committed.

## The problem (15-445 L20)
Failures: transaction (abort, deadlock), system (power loss, kernel panic — memory lost, disk
intact), media (disk lost — needs backups + archived log). Volatile buffer pool means at crash
time committed changes may not be on disk and uncommitted ones may be. Buffer policies:
**steal** (may write an uncommitted transaction's dirty page — needs undo) vs no-steal;
**force** (all of a transaction's pages written at commit — no redo needed, slow) vs
**no-force**. Steal + no-force is fastest and requires both undo and redo ⇒ WAL. **Shadow
paging** (System R, LMDB, SQLite's rollback journal is the inverse) copies pages and swaps a
root pointer atomically — simple, but fragments and doesn't scale to fine-grained locking.

## Write-ahead logging
Each update appends a record ⟨LSN, txn, page, offset, before-image, after-image⟩ (physical),
or logical (`INSERT INTO …`, compact but hard to redo idempotently), or **physiological**
(physical to a page, logical within it — ARIES's choice, survives slot reorganization).
Rules: (1) a page can be flushed only after log records up to its **pageLSN** are on disk
(flushedLSN ≥ pageLSN); (2) commit returns only after the commit record is durable
(`fsync` — [[file-systems]] crash-consistency caveats about drive caches apply). **Group
commit** batches log flushes; log on separate device; log buffer. LSNs: flushedLSN,
pageLSN (in each page header), recLSN (first record that dirtied the page), lastLSN per
transaction, MasterRecord (last checkpoint).

## ARIES (Mohan et al. 1992; L21)
Data structures carried in **fuzzy checkpoints** (no quiescing — record the **active
transaction table** ATT with lastLSN/status and the **dirty page table** DPT with recLSN;
begin/end checkpoint records):
1. **Analysis**: scan forward from the last checkpoint to rebuild ATT and DPT, learning which
   transactions were active (losers) and which pages might be dirty.
2. **Redo — repeat history**: start at the smallest recLSN in the DPT; for every update or CLR
   record, if the page's pageLSN < record LSN, reapply (redo is idempotent because pageLSN says
   whether it already happened). *All* updates are redone, including losers' — restoring the
   exact pre-crash state so undo has a consistent picture and fine-grained locking works.
3. **Undo**: process losers' records newest-first following prevLSN chains; for each undone
   update write a **compensation log record** (CLR) whose undoNextLSN points past it — CLRs are
   redo-only, never undone, so a crash mid-undo resumes where it left off with bounded work
   (no infinite undo of undos). Write end records; abort of a single transaction in normal
   operation uses the same undo path (partial rollbacks to savepoints too).
Also: nested top actions (structure modifications like B+tree splits that must not be undone
logically), logical undo for index operations, media recovery from backup + log, parallel
redo. ARIES lives on in DB2, SQL Server, Postgres (redo-only variant with MVCC providing
undo), InnoDB (redo log + undo tablespaces).

## Beyond one machine
The same log is the replication stream (log shipping, logical decoding/CDC) and the state-
machine-replication input ([[replication-and-partitioning]], [[distributed-systems-basics]]);
journaling file systems are metadata-only ARIES ([[file-systems]]); LSM engines make the log
the primary structure ([[storage-engines-and-indexes]]).

## Pitfalls
- Disabling `fsync`/`synchronous_commit` without knowing you traded durability for latency.
- Log on the same failure domain as data; unbounded log growth without checkpoints/archiving.
- Non-idempotent redo (logical logging) or forgetting pageLSN checks.
- Believing a "committed" reply means data is on disk when a middle layer buffers.

## Related
- [[transactions-and-concurrency-control]], [[storage-engines-and-indexes]], [[file-systems]],
  [[replication-and-partitioning]], [[distributed-systems-basics]].

## Sources
Mohan et al. 1992; 15-445 L20–21; Silberschatz ch. 19; Gray & Reuter ch. 9–10; Hellerstein et al. §5.4.

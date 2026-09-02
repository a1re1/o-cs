---
title: Transactions and concurrency control — ACID, serializability, two-phase locking, timestamp ordering, optimistic and multi-version concurrency control, isolation levels and their anomalies
type: concept
section: "4.5"
level: 400
tags: [transactions, acid, atomicity, isolation, durability, serializability, conflict-serializability, precedence-graph, schedules, two-phase-locking, strict-2pl, deadlock-detection, deadlock-prevention, wait-die, wound-wait, lock-granularity, intention-locks, latches-vs-locks, timestamp-ordering, optimistic-concurrency-control, occ, validation, mvcc, snapshot-isolation, write-skew, serializable-snapshot-isolation, ssi, isolation-levels, read-uncommitted, read-committed, repeatable-read, phantoms, dirty-read, lost-update, predicate-locks, index-locking]
sources: [cmu-15-445, database-textbooks, database-seminal-papers]
summary: A transaction is a unit of work that is atomic (all or nothing), consistent (preserves invariants), isolated (as if alone) and durable; isolation is defined by serializability — the interleaved schedule must be equivalent to some serial order, checked via conflict pairs and an acyclic precedence graph — and enforced pessimistically by two-phase locking (grow then shrink; strict 2PL holds until commit to avoid cascading aborts; deadlocks detected by waits-for cycles or prevented by wait-die/wound-wait; hierarchical intention locks from Gray 1976), by timestamp ordering, or optimistically by validation at commit (OCC), while multi-version concurrency control lets readers see a consistent snapshot without blocking writers (snapshot isolation, which permits write skew; serializable SI adds rw-dependency tracking); the ANSI isolation levels (read uncommitted, read committed, repeatable read, serializable) are defined by which anomalies (dirty reads, non-repeatable reads, phantoms, lost updates, write skew) they forbid, and most databases default to something weaker than serializable.
---
# Transactions and concurrency control

**In one sentence.** Interleave transactions for throughput but make the result
indistinguishable from running them one at a time — or admit exactly which anomalies you are
willing to see.

## ACID and serializability (15-445 L16; Gray & Reuter)
**Atomicity** and **durability** come from logging and recovery
([[database-recovery-and-logging]]); **consistency** is the application's invariants plus
constraints; **isolation** is the scheduler's job. A **schedule** is serializable if
equivalent to some serial schedule. **Conflict serializability**: two operations conflict if
from different transactions, on the same object, and at least one is a write (RW, WR, WW);
the schedule is conflict-serializable iff the **precedence graph** (edges Ti→Tj for each
conflict with Ti first) is acyclic ([[graph-search]]). View serializability is broader but
NP-complete to check. **Recoverable** schedules commit a transaction only after those it read
from; strictness avoids cascading aborts.

## Pessimistic: two-phase locking (L17)
Shared (S) and exclusive (X) locks on objects; **2PL**: a transaction acquires all its locks
before releasing any (growing then shrinking phase) ⇒ conflict-serializable schedules; **strict
2PL** (rigorous) releases only at commit ⇒ strict/cascadeless. Costs: blocking, **deadlocks** —
detect via the waits-for graph and abort a victim, or prevent by timestamp priority (**wait-
die**: older waits for younger, younger dies; **wound-wait**: older wounds younger). **Lock
granularity** (Gray et al. 1976): hierarchy table → page → tuple with **intention locks**
(IS, IX, SIX) so a table-level X and a tuple-level S conflict correctly; lock escalation.
**Latches** protect in-memory structures for microseconds (no deadlock detection, no
transaction scope); **locks** protect logical database content for the transaction's life.
Phantoms: a predicate query re-run sees new rows — need predicate/index-range/next-key locks
(InnoDB gap locks) or MVCC.

## Timestamp ordering and OCC (L18)
**T/O**: each transaction gets a timestamp; reads/writes checked against per-object read/write
timestamps; violations abort (Thomas write rule ignores obsolete writes). **Optimistic
concurrency control** (Kung & Robinson 1981): read phase in a private workspace, **validation**
(backward/forward against concurrent transactions), write phase — wins when conflicts are
rare (short transactions, partitioned data), loses on hot spots (wasted work). Partition-based
T/O (H-Store/VoltDB): single-threaded execution per partition, no locks at all.

## Multi-version concurrency control (L19; DDIA ch. 7)
Keep multiple versions of each tuple with begin/end timestamps; readers use a **snapshot** and
never block writers; writers create new versions (first-committer/first-updater-wins detects
WW conflicts). Variants: append-only (Postgres — old versions in the heap, `VACUUM`), time-
travel (SQL Server), delta/undo storage (MySQL InnoDB rollback segments, Oracle). Garbage
collection of dead versions; index handling. **Snapshot isolation** avoids dirty, non-repeatable
and phantom reads but allows **write skew** (two transactions each read the other's write set
and update disjoint rows — the on-call doctors example) — it is *not* serializable; **SSI**
(Cahill 2008; Postgres `SERIALIZABLE`) tracks rw-antidependencies and aborts dangerous
structures. MVCC + 2PL (InnoDB), MVCC + T/O, MVCC + OCC (Hekaton) are all deployed.

## Isolation levels (Berenson et al. 1995)
| Level | Forbids | Permits | Typical default |
|---|---|---|---|
| Read uncommitted | — | dirty reads | — |
| Read committed | dirty reads | non-repeatable reads, phantoms, lost updates | Postgres, Oracle |
| Repeatable read / snapshot | non-repeatable reads (+phantoms under SI) | write skew, (phantoms in lock-based RR) | MySQL InnoDB |
| Serializable | everything | — | rarely default |
Anomalies: dirty write/read, lost update (read-modify-write races — fix with `SELECT … FOR
UPDATE`, atomic updates, or CAS), read skew, write skew, phantoms. Application code must know
its level: Jepsen tests repeatedly find databases violating the level they claim. Highly
available transactions (Bailis 2013): read committed and causal-like guarantees can be
coordination-free; serializability and SI cannot.

## Pitfalls
- Assuming the default level is serializable; read-modify-write without locking.
- Long transactions (bloat, lock waits, replication lag); holding locks across user input.
- Retrying only some errors (serialization failures must be retried in a loop).
- Confusing latches with locks; confusing ACID C with CAP C ([[distributed-databases-and-nosql]]).

## Related
- [[database-recovery-and-logging]], [[storage-engines-and-indexes]], [[synchronization-primitives]],
  [[cache-coherence-and-memory-consistency]] (same conflict logic at hardware scale),
  [[distributed-databases-and-nosql]], [[distributed-systems-basics]], [[graph-search]].

## Sources
15-445 L16–19; Gray et al. 1976; Bernstein & Goodman 1981; Kung & Robinson 1981; Berenson et al. 1995; Cahill et al. 2008; Bailis et al. 2013; DDIA ch. 7; Gray & Reuter.

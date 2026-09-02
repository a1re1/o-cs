---
title: Lock-free and wait-free programming — linearizability, compare-and-swap and the consensus hierarchy, ABA and memory reclamation, lock-free stacks/queues/lists, RCU, and transactional memory
type: concept
section: "4.7"
level: 500
tags: [lock-free, wait-free, obstruction-free, non-blocking, linearizability, linearization-points, compare-and-swap, cas, load-linked-store-conditional, fetch-and-add, consensus-number, consensus-hierarchy, universal-construction, aba-problem, tagged-pointers, memory-reclamation, hazard-pointers, epoch-based-reclamation, rcu, treiber-stack, michael-scott-queue, harris-list, elimination, backoff, spin-locks, ttas, mcs-lock, clh-lock, ticket-lock, seqlock, transactional-memory, htm, stm, memory-ordering, acquire-release, atomics]
sources: [stanford-cs149-and-cmu-15-418, parallel-programming-texts, parallel-computing-seminal-papers]
summary: Non-blocking data structures replace critical sections with atomic read-modify-write instructions so that a delayed or dead thread cannot block others: lock-free means some thread always makes progress, wait-free means every thread finishes in bounded steps, and correctness is linearizability (Herlihy & Wing — every operation appears atomic at a linearization point between its call and return); Herlihy's consensus hierarchy shows why compare-and-swap (or LL/SC) is the essential primitive — registers can't even solve two-thread consensus, test-and-set and fetch-and-add solve it for two, CAS for any number, hence universal — and the classic structures (Treiber stack, Michael–Scott queue, Harris's linked list with marked pointers, lock-free hash tables and skip lists) are CAS loops that retry on interference, with the ABA problem solved by tagged pointers or by safe memory reclamation (hazard pointers, epoch-based reclamation, RCU's grace periods which give readers zero-cost access in the Linux kernel); good lock implementations (TTAS with backoff, ticket, MCS/CLH queue locks) matter just as much under contention, and transactional memory (HTM in hardware, STM in software) offers optimistic critical sections when composition of lock-free pieces gets too hard.
---
# Lock-free programming

**In one sentence.** Replace "take the lock, mutate, release" with "read, compute, compare-
and-swap, retry" — and then discover that the hard problems are correctness definitions,
memory ordering, and freeing memory somebody may still be reading.

## Progress guarantees and correctness (Herlihy & Shavit ch. 3; Herlihy & Wing 1990)
Blocking (locks): a preempted holder stalls everyone; priority inversion; not fault-tolerant.
**Obstruction-free**: a thread running alone finishes; **lock-free**: some thread finishes in
bounded steps (system-wide progress; starvation possible); **wait-free**: every thread finishes
in bounded steps. **Linearizability**: each operation takes effect atomically at a
**linearization point** between invocation and response; the resulting sequential history must
be legal; it is **compositional** (linearizable objects compose into a linearizable system —
unlike serializability, [[transactions-and-concurrency-control]]) and nonblocking as a
property. Proving: identify the linearization point (often the successful CAS); tools check
histories ([[consistency-models]] uses the same definition across a network).

## Primitives and the consensus hierarchy (Herlihy 1991; CS149 L15)
Atomics: load/store, **test-and-set**, **fetch-and-add**, **compare-and-swap** (`CAS(addr,
expected, new)` — x86 `lock cmpxchg`), **LL/SC** (ARM/RISC-V, immune to ABA within the
reservation), double-width CAS. **Consensus number** = max threads that can reach wait-free
consensus using the primitive: registers 1 (so no wait-free queue from reads/writes alone);
TAS, FAA, swap, queues/stacks 2; CAS, LL/SC, memory-to-memory move ∞ — **universal**: any
sequential object has a wait-free implementation from CAS (universal construction; slow but
proves the point). Memory ordering: atomics carry acquire/release/seq_cst semantics; the
data-race-free contract and fences ([[cache-coherence-and-memory-consistency]]); relaxed
atomics for counters.

## Locks done well (Herlihy & Shavit ch. 7; CS149 L15)
TAS spins hammer the coherence bus; **TTAS** (test then TAS) spins on the cache; exponential
**backoff**; **ticket locks** (FAA to take a number — fair, but all spin on one word);
**MCS/CLH queue locks** — each waiter spins on its own cache line, O(1) coherence traffic per
handoff, used in Linux (qspinlock) and JVMs; reader-writer locks; **seqlocks** (writers
increment a sequence; readers retry if it changed — reads never block); futexes to sleep
([[synchronization-primitives]]). Fine-grained locking (hand-over-hand on lists), optimistic
validation, lazy deletion (mark then unlink) as steps toward lock-free.

## Classic lock-free structures
- **Treiber stack**: push/pop = CAS on the head; **elimination** backoff (a push and a pop meet
  in an array and cancel) for scalability.
- **Michael–Scott queue**: head and tail pointers, enqueue CASes the last node's next then
  swings tail (helping: any thread may finish another's tail swing); dequeue CASes head; dummy
  node.
- **Harris linked list**: logical deletion by marking the low bit of `next`, physical unlink by
  CAS; basis for lock-free skip lists and hash sets (split-ordered lists).
- Counters (FAA), bounded queues (Vyukov MPMC with per-slot sequence numbers), work-stealing
  deques ([[work-stealing-and-fork-join]]), lock-free allocators.

## ABA and memory reclamation (McKenney ch. 9)
**ABA**: thread reads A, is delayed, the value changes A→B→A, its CAS succeeds wrongly (e.g. a
popped node reused). Fixes: **tagged/versioned pointers** (double-width CAS), LL/SC, or never
reusing memory while a reader may hold it — which is the reclamation problem: **hazard
pointers** (readers publish what they're reading; freers scan before freeing), **epoch-based
reclamation** (readers enter an epoch; free after all readers advance — crossbeam), **RCU**
(Linux: readers have zero-cost critical sections, writers copy-update and wait a **grace
period** until all pre-existing readers finish — ideal for read-mostly data; `synchronize_rcu`,
`call_rcu`), reference counting (expensive, cyclic), garbage collection (the JVM's quiet
advantage). Rust's `Arc`/crossbeam and Java's `java.util.concurrent` package these.

## Transactional memory (CS149 L17–18; Herlihy & Shavit ch. 18)
`atomic { … }` executed speculatively: track read/write sets, detect conflicts, commit or
abort/retry. **HTM** (Intel TSX/RTM, IBM POWER, Arm TME): cache-based, bounded, aborts on
capacity/interrupts — needs a fallback lock; **STM**: software versioning (eager/lazy), often
slow; lock elision as the practical win. Composability is the point (two lock-free structures
don't compose; two transactions do); I/O and nesting are the problems.

## Pitfalls
- Assuming lock-free = faster; under low contention a good lock often wins, and CAS loops
  can livelock under high contention.
- Forgetting memory ordering (a "lock-free" structure that's only correct on x86 TSO).
- ABA via memory reuse; freeing nodes readers still hold.
- Complex lock-free code without a model checker (loom, TLA+, litmus tests — [[model-checking]]).

## Related
- [[synchronization-primitives]], [[cache-coherence-and-memory-consistency]],
  [[work-stealing-and-fork-join]], [[consistency-models]], [[parallel-programming-models]],
  [[garbage-collection]], [[ownership-and-borrowing]] (Rust's Send/Sync).

## Sources
Herlihy 1991; Herlihy & Wing 1990; Herlihy & Shavit ch. 3, 5–7, 9–11, 18; McKenney perfbook ch. 7, 9, 15; Michael & Scott 1996; Harris 2001; Treiber 1986; CS149 L15–18; Adve & Gharachorloo 1996.

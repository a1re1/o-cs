---
title: Synchronization — locks, condition variables, semaphores, atomics, and concurrency bugs (races, deadlock)
type: concept
section: "4.2"
level: 300
tags: [synchronization, locks, mutex, spinlock, test-and-set, compare-and-swap, ticket-lock, futex, condition-variables, monitors, semaphores, producer-consumer, readers-writers, atomics, lock-free, deadlock, deadlock-conditions, lock-ordering, atomicity-violation, order-violation, priority-inversion, rwlock, channels]
sources: [ostep, xv6-and-6-1810, os-seminal-papers, cache-coherence-and-memory-consistency]
summary: Shared mutable state needs atomicity and ordering — locks (built on hardware test-and-set/compare-and-swap/LL-SC; spin vs block via futexes; evaluated by mutual exclusion, fairness, and performance) provide critical sections, condition variables (always wait in a while loop, hold the lock, signal/broadcast) let threads wait for state changes, semaphores generalize both, and higher-level tools (channels, monitors, RCU, lock-free structures) trade complexity for scalability; the recurring bugs are atomicity violations, order violations, and deadlock (mutual exclusion + hold-and-wait + no preemption + circular wait), prevented by lock ordering, trylock/backoff, or avoiding shared state.
---
# Synchronization primitives and concurrency bugs

**In one sentence.** A race is two threads touching shared state with at least one write and no
ordering; the fix is always the same — establish an order — and the primitives differ in how
much they cost and how easy they are to misuse.

## Locks (OSTEP ch. 28)
- Goal: **mutual exclusion** for a critical section; evaluate by correctness, **fairness**
  (starvation?), **performance** (uncontended cost, contention scaling).
- Building blocks: disabling interrupts (uniprocessor kernels only); loads/stores alone fail
  (Peterson works but needs SC memory); hardware atomics — **test-and-set**, **compare-and-swap**,
  **load-linked/store-conditional** (RISC-V `lr/sc`, ARM), **fetch-and-add** (ticket locks: FIFO
  fair). Spinlocks waste CPU while waiting (fine for short kernel sections with interrupts off —
  xv6 `acquire`); user-space mutexes **spin briefly then block** via **futex** (Linux) so the
  uncontended path is one atomic op and the contended path sleeps. MCS/queue locks scale on many
  cores by spinning on local flags ([[cache-coherence-and-memory-consistency]]). Reader-writer locks
  when reads dominate (beware writer starvation); RCU for read-mostly kernel data.
- Lock-based data structures (OSTEP 29): coarse vs fine-grained (hand-over-hand list locking),
  per-core approximate counters (sloppy counters) — scalability through less sharing.

## Condition variables and semaphores (OSTEP ch. 30–31)
- **CV**: `wait(cv, lock)` atomically releases the lock and sleeps; `signal` wakes one, `broadcast`
  all. Rules: always hold the lock when calling wait/signal; **always re-check the predicate in
  a `while` loop** (Mesa semantics — spurious/lost wakeups; xv6's `sleep`/`wakeup` solves the
  lost-wakeup race by passing the lock). Producer/consumer with a bounded buffer needs two CVs
  (empty/fill) and the loop.
- **Semaphore** (Dijkstra, THE): integer with `wait` (P: decrement, block if < 0) and `post` (V:
  increment, wake one). Binary semaphore = lock; counting semaphore = resource pool; ordering
  (child signals parent) = CV without the loop. Readers–writers via semaphores; the dining
  philosophers (break symmetry).
- **Monitors** (Hoare/Mesa; Java `synchronized` + `wait/notify`) package lock + CVs with data.

## Beyond locks
Atomics with explicit memory orderings ([[cache-coherence-and-memory-consistency]]); **lock-free**
queues/stacks with CAS (ABA problem → tagged pointers or hazard pointers/epochs); **channels**
and message passing ("share memory by communicating" — Go, Rust `mpsc`); transactional memory
(niche); immutability and ownership so there is nothing to race on ([[ownership-and-borrowing]],
[[purity-and-referential-transparency]]); event loops that avoid threads
([[async-and-event-driven-concurrency]]).

## Concurrency bugs (OSTEP ch. 32, Lu et al. 2008)
- **Non-deadlock (97%)**: **atomicity violation** (check-then-act without a lock — `if (p) use(p)`
  while another thread nulls p) → lock around the whole assumption; **order violation** (thread B
  assumes A ran first) → CV/semaphore/join.
- **Deadlock** requires all four: mutual exclusion, hold-and-wait, no preemption, circular wait.
  Prevention: **global lock ordering** (by address if needed), acquire all at once, trylock with
  backoff, lock-free; avoidance (Banker's algorithm, static scheduling); detection and recovery
  (databases abort a transaction — [[transactions-and-concurrency-control]]). Tools: lockdep,
  TSan, deadlock detectors, model checking (TLA+, loom).
- **Priority inversion** → inheritance ([[cpu-scheduling]]).

## Pitfalls
- `if` instead of `while` around `wait`; signalling without holding the lock; forgetting to
  signal on every state change.
- Holding locks across blocking I/O or callbacks; nested locks in inconsistent order.
- "Double-checked locking" without atomics/fences; volatile as a synchronization tool.
- Fine-grained locking that costs more in cache-line traffic than the parallelism it buys — measure.

## Related
- [[processes-and-threads]], [[cache-coherence-and-memory-consistency]], [[cpu-scheduling]],
  [[ownership-and-borrowing]], [[async-and-event-driven-concurrency]], [[transactions-and-concurrency-control]],
  [[undefined-behavior]].

## Sources
OSTEP ch. 28–32; xv6 book ch. 6–7; Dijkstra 1968; Lu et al. "Learning from Mistakes" 2008.

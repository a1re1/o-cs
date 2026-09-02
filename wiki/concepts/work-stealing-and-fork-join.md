---
title: Fork-join parallelism and work stealing — work/span analysis, greedy scheduling, Cilk, task graphs, and race detection
type: concept
section: "4.7"
level: 400
tags: [fork-join, cilk, spawn, sync, work, span, critical-path, parallelism, greedy-scheduler, brent, work-stealing, blumofe-leiserson, continuation-stealing, child-stealing, deque, task-parallelism, task-graph, tbb, rayon, java-fork-join, openmp-tasks, race-detection, determinacy-race, reducers, parallel-loops, divide-and-conquer, cilkscan]
sources: [stanford-cs149-and-cmu-15-418, parallel-programming-texts, parallel-computing-seminal-papers]
summary: Fork-join (Cilk's spawn/sync, TBB, Rayon, Java's ForkJoinPool, OpenMP tasks) expresses parallelism as a DAG of strands whose performance is captured by two numbers — work T₁ (total operations) and span T∞ (longest dependency path) — giving parallelism T₁/T∞ and the greedy-scheduler bound T_P ≤ T₁/P + T∞ (Brent/Graham), so a divide-and-conquer algorithm with logarithmic span scales as long as its parallelism far exceeds the core count; randomized work stealing (Blumofe & Leiserson 1999) achieves that bound in expectation with each worker running its own deque (push/pop at the bottom, thieves steal from the top — old, big tasks), touching other workers only when idle, keeping serial semantics and bounded space; and because the model is deterministic apart from races, tools like Cilksan detect determinacy races exactly and reducers/hyperobjects turn shared accumulators into per-worker views.
---
# Fork-join and work stealing

**In one sentence.** Express all the parallelism you have as a DAG, let a runtime with
per-core deques schedule it, and predict the speedup from work and span.

## The model (6.172 L6–8; CS149 L5)
`spawn f(); g(); sync;` — the callee may run in parallel with the continuation; a `sync` waits
for all spawned children. `parallel_for` = recursive halving with spawns (grain size to bound
overhead). Parallelism is *permitted*, not mandated: the same program is a correct serial
program when spawns are ignored (**serial semantics** — Cilk's "serial elision"), which makes
debugging and testing tractable. Implemented as Cilk/OpenCilk (C/C++), Intel TBB, Rayon
(Rust — `join`, `par_iter`), Java ForkJoinPool, OpenMP `task`/`taskwait`, .NET TPL, Go's
scheduler (goroutines on P-local run queues with stealing).

## Work and span
Computation DAG of strands. **Work** T₁ = total instructions; **span** (critical path,
depth) T∞ = longest path; **parallelism** T₁/T∞ = max useful processors. Lower bounds: T_P ≥
T₁/P (work law), T_P ≥ T∞ (span law). **Greedy scheduler** (never idles when work is ready):
T_P ≤ T₁/P + T∞ (Graham/Brent) — within 2× of optimal, and near-perfect linear speedup when
T₁/T∞ ≫ P (**parallel slackness**). Examples: parallel merge sort with parallel merge — work
Θ(n log n), span Θ(log³ n) (Θ(log² n) with better merge); matrix multiply divide-and-conquer —
work Θ(n³), span Θ(log² n); reductions Θ(log n); a naive parallel loop that spawns each
iteration from a serial loop has span Θ(n) — recursive spawning fixes it. Amdahl is the
special case of the span law ([[divide-and-conquer]], [[divide-and-conquer]]).

## Work stealing (Blumofe & Leiserson 1999)
Each worker keeps a **deque** of ready tasks; it pushes and pops at the bottom (LIFO — keeps the
cache-hot continuation local); when empty it becomes a **thief** and steals from the **top** of a
random victim's deque (FIFO — the oldest task, likely the largest chunk of remaining work, so
steals are rare: O(P·T∞) expected). Theorem: expected time T₁/P + O(T∞), space ≤ S₁·P,
communication O(P·T∞·S_max). Design choices: **continuation stealing** (Cilk: the spawner's
continuation is stolen; the child runs on the spawning worker — "work-first", preserves serial
execution order) vs **child stealing** (TBB, Java: children go on the deque, the parent
continues — simpler, deeper stacks); cactus stacks; the THE protocol for the deque (Dijkstra-
style, lock-free in the common case — [[lock-free-programming]]). Hierarchical/NUMA-aware and
locality-aware stealing; task graphs with explicit dependencies (CS149 assignment 2: schedule
a DAG of bulk tasks with a thread pool and dependency counting — the same problem as
[[build-systems-and-make]] and [[cpu-scheduling]] with a DAG).

## Races and reducers (6.172 L7)
**Determinacy race**: two logically parallel strands access the same location, one a write —
results depend on scheduling; distinct from data races under locks (which can be intended).
Cilksan (Nondeterminator) finds them precisely by SP-bags/SP-order in one run; race-free
Cilk programs are deterministic. **Reducers/hyperobjects**: each worker gets a private view
(`sum += x` on its own copy) merged with an associative operation at joins — parallel
accumulation without locks (also TBB `parallel_reduce`, OpenMP `reduction`). Parallel prefix
sums, list ranking, and other span-reducing tricks ([[parallel-programming-models]]).

## Pitfalls
- Spawning tiny tasks (overhead ~ a few hundred cycles per spawn — coarsen at the leaves).
- Serial spawning loops (linear span); global barriers instead of nested joins.
- Locks inside parallel code creating hidden dependencies; blocking inside a task (deadlocks
  a worker — use async I/O or dedicated threads — [[async-and-event-driven-concurrency]]).
- Measuring parallelism on a laptop and extrapolating; ignoring memory bandwidth
  ([[roofline-model]]).

## Related
- [[parallel-programming-models]], [[lock-free-programming]], [[divide-and-conquer]],
  [[amortized-analysis]], [[cpu-scheduling]], [[async-and-event-driven-concurrency]],
  [[processes-and-threads]], [[build-systems-and-make]].

## Sources
Blumofe & Leiserson 1999; Frigo, Leiserson & Randall "The Implementation of the Cilk-5 Multithreaded Language" 1998; 6.172 L6–8; CS149 L5 and assignment 2; CLRS ch. 26 (multithreaded algorithms); Herlihy & Shavit ch. 16.

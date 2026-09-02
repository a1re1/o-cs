---
title: CPU scheduling — FIFO, SJF/STCF, round robin, MLFQ, lottery/stride, CFS, and multiprocessor scheduling
type: concept
section: "4.2"
level: 300
tags: [cpu-scheduling, fifo, sjf, stcf, round-robin, turnaround-time, response-time, mlfq, priority-boost, lottery-scheduling, stride-scheduling, proportional-share, cfs, vruntime, multiprocessor-scheduling, cache-affinity, load-balancing, real-time, edf, priority-inversion]
sources: [ostep, xv6-and-6-1810]
summary: Scheduling policies trade turnaround time (favoring shortest-job-first and its preemptive form STCF) against response time (favoring round robin with short time slices) under unknown job lengths; MLFQ learns job behaviour by demoting CPU-bound jobs and periodically boosting everyone to avoid starvation and gaming, proportional-share schedulers (lottery, stride, Linux CFS with a red-black tree of virtual runtime and nice weights) divide the CPU by shares, and multiprocessor schedulers balance load while keeping cache affinity; real-time systems use rate-monotonic or EDF with priority inheritance to avoid priority inversion.
---
# CPU scheduling

**In one sentence.** Two metrics pull opposite ways — turnaround (finish jobs fast) wants
shortest-first, response (react fast) wants round robin — and every real scheduler is a way of
guessing job lengths and blending the two.

## Basics (OSTEP ch. 7)
Workload assumptions relaxed one at a time. Metrics: **turnaround** = completion − arrival;
**response** = first run − arrival; fairness; throughput. Policies:
- **FIFO**: convoy effect (a long job delays short ones).
- **SJF**: optimal average turnaround if all arrive together; non-preemptive.
- **STCF / PSJF**: preempt for a shorter remaining job — optimal turnaround with arrivals, but
  needs job lengths (unknown) and hurts response.
- **Round robin**: time slice q; great response, poor turnaround; q must amortize the context
  switch (~ms) but stay small for interactivity. Overlap I/O: a job that blocks gives up the
  CPU; treat each CPU burst as a job.

## MLFQ (OSTEP ch. 8)
Multiple priority queues; rules: higher priority runs first; equal priority → RR; new jobs start
at the top; a job that uses its whole *allotment* at a level is demoted (regardless of how many
times it yields — defeats gaming by frequent I/O); periodically **boost** all jobs to the top (no
starvation; adapts to phase changes). Approximates SJF without knowing lengths by learning from
history. Solaris TS, BSD, and Windows are MLFQ variants with tunable tables.

## Proportional share (OSTEP ch. 9)
**Lottery**: each job holds tickets; pick a random winner each slice — probabilistically fair,
trivially handles ticket transfer/inflation. **Stride**: deterministic — advance each job's pass
by stride = C/tickets; run the lowest pass. **Linux CFS**: track **vruntime** per task (weighted
by `nice` via a weight table so nice −20 gets ~88× nice +19); always run the smallest vruntime
(red-black tree keyed by vruntime, O(log n) — [[balanced-search-trees]]); slice = sched_latency
/ n with a minimum granularity; sleeping tasks' vruntime is set to max(own, min − latency) so
I/O-bound tasks get quick response without starving others; cgroups give hierarchical shares
(containers). EEVDF (2023) replaces CFS with lag-based deadlines.

## Multiprocessor scheduling (OSTEP ch. 10)
Issues: **cache affinity** (moving a thread loses its warm cache and TLB —
[[caches-and-memory-hierarchy]]), synchronization of a single queue (lock contention) vs
**per-CPU queues** with periodic **load balancing**/work stealing (migrate from busy to idle);
NUMA awareness; gang scheduling for parallel jobs; hyperthreads share a core. Linux: per-CPU
runqueues, scheduling domains, `sched_setaffinity`.

## Real-time and priorities
Hard real-time: rate-monotonic (static priority ∝ 1/period; schedulable if utilization ≤ n(2^{1/n}
− 1)) and **EDF** (earliest deadline first; optimal up to 100% utilization). **Priority
inversion** (a low-priority holder blocks a high-priority waiter while a medium job runs — Mars
Pathfinder) → priority inheritance/ceiling protocols ([[synchronization-primitives]]).
Linux SCHED_FIFO/RR/DEADLINE classes precede CFS.

## Pitfalls
- Tuning time slices without measuring context-switch and cache costs.
- Starvation in pure priority schemes (need aging/boost).
- Assuming fairness across processes when the scheduler is per-thread (a 100-thread process
  gets 100 shares unless grouped).
- Latency-sensitive services on a loaded box: use isolation (cgroups, cpusets), not nice alone.

## Related
- [[processes-and-threads]], [[limited-direct-execution-and-syscalls]], [[synchronization-primitives]],
  [[caches-and-memory-hierarchy]], [[balanced-search-trees]], [[probabilistic-analysis-of-algorithms]]
  (lottery fairness), [[queueing-theory]].

## Sources
OSTEP ch. 7–10; xv6 book ch. 7; Linux CFS/EEVDF documentation.

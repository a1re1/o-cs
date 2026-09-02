---
title: Real-time scheduling — periodic task model, rate-monotonic and earliest-deadline-first, utilization bounds and response-time analysis, priority inversion and inheritance/ceiling protocols, WCET
type: concept
section: "4.9"
level: 400
tags: [real-time, hard-real-time, soft-real-time, periodic-tasks, deadlines, jitter, rate-monotonic, rms, deadline-monotonic, earliest-deadline-first, edf, utilization-bound, liu-layland, schedulability, response-time-analysis, critical-instant, priority-inversion, mars-pathfinder, priority-inheritance, priority-ceiling, wcet, worst-case-execution-time, aperiodic-servers, time-triggered, cyclic-executive, rtos, preemption, multiprocessor-scheduling]
sources: [embedded-systems-texts-and-courses]
summary: Real-time correctness means meeting deadlines, not running fast: the classic model has periodic tasks with period T, worst-case execution time C and deadline D, and the question is schedulability — Liu & Layland (1973) showed that among fixed-priority schemes rate-monotonic (shorter period → higher priority) is optimal and guarantees deadlines whenever total utilization ≤ n(2^{1/n} − 1) → 69.3 % (the exact test is response-time analysis at the critical instant when all tasks release together), while dynamic-priority earliest-deadline-first is optimal on one processor and schedules any task set with utilization ≤ 1 at the cost of unpredictable overload behaviour; shared resources cause priority inversion (a high-priority task blocked by a low one that a medium one preempts — the Mars Pathfinder reset), fixed by priority inheritance or the priority ceiling protocol, which also bounds blocking and prevents deadlock; the whole analysis rests on WCET bounds that caches, pipelines and branch predictors make hard, so hard real-time systems favour simple, time-predictable hardware, cyclic executives or time-triggered schedules, and RTOSes with bounded-latency primitives.
---
# Real-time scheduling

**In one sentence.** A late right answer is a wrong answer, so the scheduler must be
provable: give me the periods and worst-case times and I will tell you whether every deadline
holds — forever.

## The model (Liu ch. 3; Lee & Seshia ch. 12)
Tasks τᵢ release jobs periodically (or sporadically with a minimum inter-arrival) with period
Tᵢ, worst-case execution time Cᵢ, relative deadline Dᵢ (often = Tᵢ), utilization Uᵢ = Cᵢ/Tᵢ.
**Hard** real time: a missed deadline is a failure (flight control, ABS); **soft**: value
degrades (video); **firm**: late results worthless but harmless. Jitter, phase, precedence
constraints, resources. Contrast with throughput-oriented [[cpu-scheduling]] (CFS, MLFQ) and
with latency SLOs ([[tail-latency-at-scale]]) — here the guarantee is per job, worst case.

## Fixed priority: rate-monotonic (Liu & Layland 1973)
Assign priorities by period (shortest first); **deadline-monotonic** when Dᵢ < Tᵢ. Optimal among
fixed-priority assignments (if any fixed-priority assignment works, RM does). **Utilization
bound**: U = ΣCᵢ/Tᵢ ≤ n(2^{1/n} − 1) is sufficient (n=2: 0.828; n→∞: ln 2 ≈ 0.693); harmonic
periods allow up to 1. Exact test: **response-time analysis** — the **critical instant** is
when all higher-priority tasks release simultaneously; Rᵢ = Cᵢ + Σ_{j∈hp(i)} ⌈Rᵢ/Tⱼ⌉·Cⱼ,
iterate to a fixed point, schedulable iff Rᵢ ≤ Dᵢ for all i. Overload behaviour is predictable:
the lowest-priority tasks miss first. Standard in RTOSes (FreeRTOS, VxWorks, QNX, Zephyr,
RTEMS) and automotive OSEK/AUTOSAR.

## Dynamic priority: EDF
Highest priority to the job with the earliest absolute deadline. **Optimal** on a uniprocessor:
any feasible set is EDF-schedulable; schedulability iff U ≤ 1 (D = T); processor-demand
tests otherwise. Costs: deadline bookkeeping, and under overload a **domino effect** (every
task misses); less common in safety-critical practice, common in multimedia and Linux
`SCHED_DEADLINE` (with constant-bandwidth servers). Least-laxity-first is also optimal but
thrashes. **Aperiodic/sporadic** work is served by bandwidth-preserving servers (sporadic
server, deferrable server, CBS) so that periodic guarantees survive.

## Resources: priority inversion (Lee & Seshia 12.5; Sha, Rajkumar & Lehoczky 1990)
A high-priority task waits on a mutex held by a low-priority task, which is preempted by
medium-priority tasks — unbounded blocking; **Mars Pathfinder (1997)** rebooted repeatedly until
JPL enabled priority inheritance remotely. **Priority inheritance**: the holder runs at the
priority of the highest waiter (bounded but chainable blocking; deadlock still possible).
**Priority ceiling protocol**: each resource has a ceiling = highest priority of any task
using it; a task may lock only if its priority exceeds all ceilings of currently locked
resources → blocked at most once per job, no deadlock, no chained blocking; immediate
priority ceiling (stack resource policy) implements it cheaply. Non-preemptive critical
sections and lock-free buffers as alternatives ([[synchronization-primitives]],
[[lock-free-programming]]).

## WCET and predictability (Lee & Seshia ch. 16; Lee 2008)
The analysis is only as good as Cᵢ. Static WCET analysis (aiT, OTAWA): control-flow graph,
loop bounds, abstract interpretation of cache and pipeline state ([[abstract-interpretation]]);
measurement-based approaches risk missing the worst path; **timing anomalies** (a cache hit
that makes things slower) on out-of-order cores; multi-core interference (shared caches,
buses, DRAM) — hence partitioning, cache locking, and time-predictable architectures (PRET),
and Lee's argument that mainstream abstractions (ISAs, threads, languages) discard time and
CPS needs timing as a first-class semantic property (synchronous languages Esterel/Lustre/
SCADE, time-triggered architecture, LET — logical execution time).

## Alternatives and practice
**Cyclic executive/time-triggered** schedules: a precomputed table over the hyperperiod —
fully deterministic, trivial to verify, rigid; **RTOS** with preemptive priorities and bounded
interrupt latency (tickless kernels, priority-aware interrupt controllers); mixed-criticality
systems (Vestal) run high- and low-criticality tasks with different assurance; multiprocessor:
partitioned (bin-pack tasks to cores, then uniprocessor tests) vs global (Pfair/LLREF optimal
but impractical; global EDF bounds); Linux PREEMPT_RT for soft/firm real time
([[cpu-scheduling]]).

## Pitfalls
- Using average execution times; ignoring interrupt and scheduler overhead and blocking terms.
- Mutexes without inheritance/ceiling in a priority-scheduled system.
- Caches, DMA and other cores silently breaking WCET assumptions.
- EDF without overload management; RM with non-harmonic periods near the bound.

## Related
- [[cpu-scheduling]], [[microcontrollers-and-embedded-programming]],
  [[cyber-physical-systems-and-models-of-computation]], [[synchronization-primitives]],
  [[abstract-interpretation]], [[caches-and-memory-hierarchy]], [[model-checking]].

## Sources
Liu & Layland 1973; Liu, Real-Time Systems ch. 4–8; Lee & Seshia ch. 12, 16; Sha, Rajkumar & Lehoczky 1990; Buttazzo, Hard Real-Time Computing Systems; Reeves, "What really happened on Mars" (1997).

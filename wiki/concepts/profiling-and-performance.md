---
title: Profiling and performance measurement — timing, sampling vs tracing, flame graphs, resource monitors
type: concept
section: "2.6"
level: 200
tags: [profiling, performance, benchmarking, wall-clock, cpu-time, user-time, sys-time, sampling-profiler, tracing-profiler, perf, flame-graph, cprofile, valgrind, memory-profiler, htop, iotop, lsof, hot-spots, amdahl]
sources: [missing-semester, csapp-15-213]
summary: Measure before optimizing: `time` splits real/user/sys; tracing profilers instrument every call (exact, slow, distorting) while sampling profilers interrupt periodically (cheap, statistical) — visualize with flame graphs or call graphs; memory profilers find leaks and churn; system monitors (htop, iotop, ss, lsof, du) locate CPU/IO/network/disk bottlenecks; then apply Amdahl's law — only the hot 10% matters — and re-measure with a proper benchmark that controls warm-up, variance and input size.
---
# Profiling and performance

**In one sentence.** Guesses about where time goes are usually wrong; a profiler shows the truth, and
Amdahl's law says fix the biggest fraction first.

## Timing
`time cmd` → **real** (wall clock), **user** (CPU in user space), **sys** (CPU in kernel).
real ≫ user+sys ⇒ waiting on I/O, network or other processes; user+sys > real ⇒ parallelism.
Micro-benchmarks need repetition, warm-up (JIT, caches), fixed CPU frequency, and reporting of
distributions, not one run (`hyperfine`, `criterion`, `pytest-benchmark`, `timeit`).

## CPU profilers
- **Tracing/instrumenting**: record every call (Python `cProfile`, `line_profiler`; `valgrind
  --tool=callgrind`); exact counts but high overhead that distorts timing; great for call counts.
- **Sampling**: interrupt N times/second and record the stack (`perf record` + `perf report`,
  `py-spy`, `pprof`, Instruments, `async-profiler`); ~1–5% overhead, statistical; the default for
  production.
- Visualize: **flame graphs** (x = share of samples, y = stack depth; wide plateaus are hot),
  call graphs (`gprof2dot`), per-line views. Look for the top of the flame first, then the callers
  that make it hot.
- Distinguish self time (in the function) from total time (including callees).

## Memory and other resources
Memory profilers (`memory_profiler`, `valgrind --tool=massif`, heaptrack, `tracemalloc`) for leaks
and allocation churn ([[dynamic-memory-allocation]]); cache misses and branch mispredictions via
`perf stat` counters ([[caches-and-memory-hierarchy]]); I/O with `iotop`, `strace -c`, `dtrace`;
network with `ss`/`iftop`/`tcpdump`; disk with `df`, `du`, `ncdu`; open files with `lsof`; system
overview with `htop`/`glances`. Load-test servers with `ab`/`wrk`/`k6`.

## Turning measurements into speedups
- **Amdahl**: speeding a fraction p by factor s gives 1 / ((1 − p) + p/s) — a 2× win on 10% of
  runtime is 5%. Find p first.
- Order of attack: algorithmic complexity ([[asymptotic-notation]]) → data structure and memory
  layout ([[caches-and-memory-hierarchy]]) → I/O and syscalls batching → compiler flags/
  [[compiler-optimizations]] → parallelism → micro-optimizations last.
- Keep the benchmark and the profile in the PR; re-run after the change; watch for regressions in
  CI ([[build-systems-and-make]]).

## Pitfalls
- Optimizing without a baseline; benchmarking debug builds; measuring one run.
- Profiler overhead changing what is hot (tracing); sampling missing short-lived processes.
- Confusing throughput and latency; ignoring tail latency (p99) in services.
- Premature optimization that destroys clarity ([[refactoring]]: clarity first, then measured wins).

## Related
- [[debugging]], [[asymptotic-notation]], [[caches-and-memory-hierarchy]], [[dynamic-memory-allocation]],
  [[compiler-optimizations]], [[refactoring]].

## Sources
Missing Semester lecture 7; CSAPP ch. 5 (optimizing program performance).

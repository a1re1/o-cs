---
title: The Roofline model — arithmetic intensity, bandwidth vs compute bound, and the ceilings that tell you which optimization to try
type: concept
section: "4.7"
level: 400
tags: [roofline, arithmetic-intensity, operational-intensity, flops-per-byte, memory-bound, compute-bound, peak-flops, peak-bandwidth, ridge-point, ceilings, simd, ilp, prefetching, numa, cache-blocking, performance-model, gpu-roofline, hbm, stream-benchmark, kernel-optimization, bottleneck-analysis]
sources: [stanford-cs149-and-cmu-15-418, parallel-computing-seminal-papers]
summary: Roofline (Williams, Waterman & Patterson 2009) plots attainable performance against a kernel's arithmetic (operational) intensity — flops per byte moved from DRAM — on log-log axes: performance is bounded by min(peak compute, peak bandwidth × intensity), so kernels left of the ridge point (where the two lines meet) are memory-bound and only more reuse (blocking, fusion, compression) helps, kernels to the right are compute-bound and only more throughput (SIMD, ILP, balanced multiply-add, more cores/tensor cores) helps; additional ceilings below the roof — no SIMD, no ILP, no prefetching, unbalanced NUMA — order the optimizations to attempt and show how far a measured kernel is from its bound, and the same chart works for L1/L2 rooflines, GPUs with HBM, and accelerators, which is why it is the first thing profilers like Nsight and Intel Advisor draw.
---
# The Roofline model

**In one sentence.** Measure how many operations you do per byte you fetch; the machine's
bandwidth and peak throughput then tell you the best you could possibly do and which wall
you are hitting.

## The model (Williams et al. 2009)
- **Arithmetic intensity** I = operations / bytes from memory (FLOP/byte; for a given kernel
  and cache behaviour). Examples: SpMV ~0.25 (memory-bound forever), stencils 0.5–2, FFT
  ~1–2 (grows with log n), dense matmul O(n) with blocking (compute-bound), DNN inference
  varies by batch — attention is bandwidth-bound at small batch.
- **Roofline**: attainable GFLOP/s = min(peak FLOP/s, peak GB/s × I). Log-log: a sloped
  bandwidth line meeting a flat compute line at the **ridge point** I* = peak FLOP/s ÷ peak
  GB/s (e.g. CPU: 1 TFLOP/s ÷ 100 GB/s = 10 FLOP/byte; H100: ~1000 TFLOP/s (tensor) ÷ 3.35 TB/s
  ≈ 300 FLOP/byte — GPUs need enormous reuse to be compute-bound).
- Measure peaks with microbenchmarks (STREAM for bandwidth, a FMA loop for compute) rather
  than datasheets; measure a kernel's I with hardware counters (DRAM bytes) or by counting.

## Ceilings
Below the roof, draw the performance you get **without** each optimization: compute ceilings
— no SIMD (÷ vector width), no FMA balance (÷2), no ILP/dependency chains, no multithreading;
bandwidth ceilings — no software prefetching, no NUMA affinity, non-unit-stride/uncoalesced
access ([[gpu-programming-cuda]]). A kernel's measured point relative to the ceilings says what
to do next: memory-bound left of the ridge → increase I (cache **blocking/tiling**, loop
fusion, smaller data types, recompute instead of store, compression) or raise achieved
bandwidth (prefetch, layout, NUMA, coalescing); compute-bound → vectorize, unroll for ILP,
balance mul/add, use tensor cores, more cores. Hierarchical rooflines use L1/L2/LLC bandwidths
to locate which level bounds you ([[caches-and-memory-hierarchy]]). Cache-oblivious layouts
raise I at every level at once ([[cache-oblivious-algorithms]]).

## Using it
1. Get peak compute and bandwidth for the node/GPU. 2. Count or measure a kernel's flops and
DRAM bytes → I. 3. Plot; compare achieved to bound. 4. If far from the roof, check the
ceilings in order (cheapest first); if at the roof and still too slow, change the algorithm
(higher I) or the hardware. Tools: Intel Advisor, NVIDIA Nsight Compute (roofline section),
Empirical Roofline Toolkit, `perf` counters, likwid. Related models: the balance equation
(machine balance vs algorithm balance), Little's law for memory-level parallelism
([[queueing-theory]]), the Amdahl view for serial fractions ([[performance-equation-and-amdahl]]).

## Pitfalls
- Using datasheet peaks; ignoring that intensity depends on cache behaviour and problem size.
- Counting flops and bytes at the wrong level (L2 traffic vs DRAM).
- Treating the roofline as a predictor rather than an upper bound (latency, instruction
  overhead, imbalance sit below it).
- Optimizing compute in a memory-bound kernel (the classic wasted week).

## Related
- [[performance-equation-and-amdahl]], [[caches-and-memory-hierarchy]], [[gpu-programming-cuda]],
  [[parallel-programming-models]], [[cache-oblivious-algorithms]], [[profiling-and-performance]],
  [[parallel-architectures-simd-gpu]].

## Sources
Williams, Waterman & Patterson, CACM 2009; CS267 lecture on roofline; 6.172; Ofenbeck et al. "Applying the roofline model" 2014; NVIDIA Nsight docs.

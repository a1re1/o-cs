---
title: Parallel architectures — SIMD/vector, multicore, GPUs, and domain-specific accelerators
type: concept
section: "4.1"
level: 300
tags: [parallel-architectures, flynn-taxonomy, simd, vector-processors, avx, sve, multicore, shared-memory, gpu, cuda, warps, simt, memory-coalescing, tpu, systolic-array, accelerators, domain-specific-architectures, heterogeneous, roofline, dlp, tlp]
sources: [patterson-hennessy-cod, architecture-seminal-papers]
summary: Flynn's taxonomy sorts hardware parallelism into SIMD (one instruction, many data — vector units like AVX-512/SVE, GPUs' SIMT warps) and MIMD (multicore, clusters); GPUs are throughput machines — thousands of simple lanes, massive multithreading to hide memory latency, coalesced memory access, and a programming model (CUDA/OpenCL) of kernels over thread blocks — while domain-specific accelerators (TPU's systolic array for matrix multiply) trade generality for 10–100× perf/W; the roofline model says which kernels benefit, and the shift to these designs follows from the end of Dennard scaling.
---
# Parallel architectures: SIMD, multicore, GPUs, accelerators

**In one sentence.** When one core can't get faster, get more lanes (SIMD), more cores (MIMD),
or a machine shaped like your problem (DSA) — and rewrite the software to expose the parallelism.

## Flynn's taxonomy (COD ch. 6)
SISD (classic core), **SIMD** (data-level parallelism: one instruction on a vector), MISD (rare),
**MIMD** (multiple independent instruction streams: multicore, clusters). Modern CPUs are MIMD of
cores each with SIMD units and SMT; GPUs are SIMT (single instruction, multiple threads).

## SIMD / vector
- x86 SSE/AVX/AVX-512 (128/256/512-bit registers: 16 floats per op), ARM NEON/SVE (scalable
  vector length), RISC-V V. Compilers auto-vectorize simple loops (stride-1, no aliasing — use
  `restrict`, no loop-carried dependences); intrinsics or libraries (Eigen, NumPy) otherwise.
- Vector processors (Cray, RISC-V V): vector length register, strip-mining, masking for
  conditionals, gather/scatter; lanes and chaining; memory bandwidth is the bottleneck.
- Subword parallelism for images/audio; SoA layout enables it ([[caches-and-memory-hierarchy]]).

## Multicore and shared memory
Cores share L3 and memory; private L1/L2 need [[cache-coherence-and-memory-consistency]]; programs
use threads with locks/atomics ([[synchronization-primitives]]). NUMA on multi-socket: memory
attached to another socket is slower — place data near the threads using it. Scaling is bounded
by Amdahl's serial fraction and by contention ([[performance-equation-and-amdahl]]).

## GPUs (COD 6.6, CA:AQA 4.4)
- Hardware: tens of streaming multiprocessors (SMs), each with many lanes, huge register files,
  and warp schedulers; threads run in **warps** of 32 in lockstep (SIMT) — divergent branches
  serialize; **latency hiding** by switching among thousands of resident threads instead of
  caches/OoO; high-bandwidth memory (HBM ~TB/s) but high latency; small caches + shared memory
  (scratchpad) per SM; tensor cores for matrix multiply.
- Programming model (CUDA/OpenCL/HIP): a **kernel** runs over a grid of thread blocks; threads in
  a block share scratchpad and synchronize with barriers; **memory coalescing** (adjacent threads
  read adjacent addresses) is the key performance rule; host↔device copies over PCIe/NVLink are
  expensive — keep data on device.
- Good for: dense linear algebra, stencils, image/signal processing, deep learning training and
  inference ([[gradient-descent]]), simulation; bad for: pointer-heavy, branchy, latency-bound
  code.

## Domain-specific architectures (Hennessy–Patterson 2019)
TPU: a 256×256 **systolic array** of MACs streams weights/activations so each value is fetched
once and reused hundreds of times; 8-bit integer inference; 30–80× perf/W vs CPUs/GPUs of its
generation. DSA design rules: dedicated memories, drop unneeded features (caches, OoO), the
simplest parallelism that fits (SIMD/systolic), reduced precision, a domain-specific language to
target it (TensorFlow/XLA, Halide). FPGAs for reconfigurable pipelines (Microsoft Catapult);
video/crypto/network offload engines; Apple's heterogeneous SoCs.

## Deciding what to use
Roofline: compute arithmetic intensity (FLOPs per byte); below the ridge point you are memory-
bound and no amount of ALUs helps — improve locality first. Vectorize inner loops; multithread
across independent work; move to GPU when the working set fits device memory and the kernel is
regular; DSAs when the workload is stable and enormous.

## Related
- [[cache-coherence-and-memory-consistency]], [[synchronization-primitives]], [[performance-equation-and-amdahl]],
  [[caches-and-memory-hierarchy]], [[pipelining-and-hazards]], [[gradient-descent]], [[mapreduce-and-dataflow]].

## Sources
COD ch. 6 and appendix on GPUs; CA:AQA ch. 4–5, 7; Jouppi et al. TPU 2017; Hennessy & Patterson 2019.

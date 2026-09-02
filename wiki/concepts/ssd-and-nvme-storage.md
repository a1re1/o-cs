---
title: SSDs and NVMe — NAND flash, the flash translation layer, write amplification and wear, what field studies show, and the fast-storage software stack
type: concept
section: "4.8"
level: 400
tags: [ssd, nand-flash, slc, mlc, tlc, qlc, pages, blocks, erase-before-write, flash-translation-layer, ftl, wear-leveling, garbage-collection, write-amplification, over-provisioning, trim, nvme, pcie, queues, io-latency, iops, zoned-namespaces, zns, open-channel, persistent-memory, optane, cxl, flash-reliability, raw-bit-error-rate, uncorrectable-errors, endurance, dwpd, io_uring, spdk, fsync]
sources: [storage-and-cloud-seminal-papers, datacenter-and-sre-books, ostep]
summary: NAND flash reads pages (4–16 KB) fast and randomly, writes pages only into erased blocks (MBs), and wears out after thousands (TLC) to tens of thousands (SLC) of program/erase cycles, so an SSD's flash translation layer remaps logical to physical pages log-structured-style, garbage-collects blocks (copying live pages — write amplification, reduced by over-provisioning and TRIM), wear-levels, and hides bit errors with ECC; NVMe exposes the parallelism over PCIe with deep multi-queue submission/completion rings, giving ~100 μs latency and millions of IOPS that the traditional block layer and blocking syscalls cannot keep up with (hence io_uring, SPDK, zoned namespaces that move the FTL's placement into the host), while Google's field study (Schroeder 2016) found raw bit errors grow slowly with wear and don't predict uncorrectable errors, SLC is not more reliable than MLC in practice, age matters more than use, and SSDs are replaced less often than disks but return uncorrectable errors more often — so software must checksum and replicate regardless.
---
# SSDs and NVMe storage

**In one sentence.** Flash is fast, parallel, and refuses to overwrite in place — so a small
log-structured file system lives inside every drive, and the rest of the stack has spent
fifteen years catching up to its speed.

## The device (OSTEP ch. 44)
Cells store 1 (SLC), 2 (MLC), 3 (TLC), 4 (QLC) bits — more bits: cheaper, slower, fewer P/E
cycles (~100k → ~1k). Organization: planes/dies → **blocks** (MBs) → **pages** (4–16 KB).
Operations: read a page (~25–100 μs), program a page (~200 μs–ms, only into an erased block,
pages in order), **erase a block** (ms). Raw bit errors rise with wear, retention time and
read disturb; on-drive ECC (BCH/LDPC) corrects most. Disks vs flash: no seeks, random reads
≈ sequential, but writes need the FTL and wear is finite (endurance rated in drive-writes-
per-day — DWPD).

## The FTL
Maps logical block addresses → physical pages with a **log-structured** policy (write anywhere
free, update the map — the LFS idea reborn, [[file-systems]] → LSM lineage in
[[storage-engines-and-indexes]]); page-level maps need DRAM (1 GB per TB) or hybrid block/page
mapping; **garbage collection** picks blocks with few live pages, copies live pages, erases —
**write amplification** (WA = flash writes / host writes; 2–10× for random small writes);
**over-provisioning** (extra hidden capacity) and **TRIM/discard** (host says which blocks are
free) cut WA; **wear leveling** moves static data so blocks age evenly; power-loss protection
(capacitors) for the map; on-drive compression/dedup in some. Performance cliffs: a fresh
drive is fast until GC starts (steady-state benchmarking needs preconditioning); mixed
read/write workloads suffer tail latency from GC ([[tail-latency-at-scale]]).

## NVMe and the host stack
SATA/AHCI (one queue, 32 commands) → **NVMe** over PCIe: up to 64k queues × 64k commands,
MSI-X interrupts per queue per core, ~10 μs protocol overhead; 4–8 GB/s and 1M+ IOPS per drive.
The software stack becomes the bottleneck: interrupt cost, block layer locking (fixed by blk-mq),
syscall overhead (fixed by **io_uring** — shared submission/completion rings, batching, polling;
[[sockets-programming]]), kernel bypass (**SPDK** user-space polled drivers). **NVMe-oF**
(TCP/RDMA) disaggregates storage over the network. **Zoned namespaces (ZNS)** and open-channel
SSDs expose append-only zones so the host (e.g. an LSM engine) does placement and GC once
instead of twice. **Persistent memory** (Optane DC PM, byte-addressable, ~300 ns; discontinued
2022) and **CXL**-attached memory continue the blurring of memory and storage
([[caches-and-memory-hierarchy]], [[virtual-memory]]).

## What the field says (Schroeder, Lagisetty & Merchant 2016)
Millions of drive-days, 10 models, SLC/eMLC/MLC over six years at Google: RBER grows
**linearly**, not exponentially, with P/E cycles; RBER is **not predictive** of uncorrectable
errors; the UBER metric is meaningless (no correlation between reads and uncorrectable
errors); SLC drives are **not** more reliable than MLC within typical lifetimes; drive **age**
(independent of P/E cycles) matters; 20–63 % of drives see at least one uncorrectable error;
SSDs have lower replacement rates than disks but higher uncorrectable-error rates. Consequence:
plan for uncorrectable reads (checksums, replication, erasure coding —
[[raid-and-erasure-coding]]) rather than trusting endurance ratings; monitor bad-block growth.

## Using SSDs well
Align writes to pages; large sequential writes; batch and coalesce; leave over-provisioning
(don't fill to 100 %); enable discard; understand `fsync` cost (drive write cache — FUA/flush;
consumer drives lie); prefer append-only structures (LSM, WAL) for write-heavy loads; use
direct I/O + io_uring for latency-critical paths; in the cloud, know local NVMe (ephemeral,
fast) vs network block storage (durable, slower, IOPS-provisioned).

## Pitfalls
- Random small overwrites in place (WA and wear); filling the drive; disabling TRIM.
- Benchmarks on fresh drives; comparing IOPS at different queue depths.
- Assuming SSD = no corruption; skipping checksums.
- Blocking I/O threads per request when the device wants deep queues.

## Related
- [[file-systems]], [[storage-engines-and-indexes]], [[raid-and-erasure-coding]],
  [[io-and-device-drivers]], [[caches-and-memory-hierarchy]], [[tail-latency-at-scale]],
  [[distributed-file-and-object-storage]].

## Sources
OSTEP ch. 44; Schroeder et al. FAST 2016; Agrawal et al. "Design Tradeoffs for SSD Performance" 2008; NVMe specification; Axboe io_uring docs; Bjørling et al. "ZNS" 2021.

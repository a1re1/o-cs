---
title: RAID and erasure coding — mirroring, striping, parity, Reed–Solomon, durability arithmetic, and rebuild
type: concept
section: "4.8"
level: 400
tags: [raid, raid-0, raid-1, raid-5, raid-6, raid-10, mirroring, striping, parity, small-write-problem, write-hole, rebuild, mttf, mttr, durability, annual-failure-rate, erasure-coding, reed-solomon, local-reconstruction-codes, failure-domains, availability-zones, replication-factor, bit-rot, scrubbing, checksums, silent-data-corruption]
sources: [storage-and-cloud-seminal-papers, datacenter-and-sre-books]
summary: RAID (Patterson, Gibson & Katz 1988) combines cheap disks for throughput (striping, RAID 0), reliability (mirroring, RAID 1; parity, RAID 5 with rotated parity and RAID 6 with two parities), and both (RAID 10), at the cost of the small-write problem (a parity update costs two reads and two writes), the write hole (power loss between data and parity writes — fixed by journaling or copy-on-write as in ZFS), and long rebuilds during which a second failure is likely on large disks; distributed systems generalize the idea as erasure coding — Reed–Solomon (k data + m parity fragments tolerate any m losses at (k+m)/k storage overhead instead of 3× replication) and local reconstruction codes that cut rebuild traffic — placed across failure domains (racks, availability zones), with durability computed from failure rates, repair times and correlated failures, and defended against silent corruption by end-to-end checksums and background scrubbing.
---
# RAID and erasure coding

**In one sentence.** Redundancy converts many unreliable cheap devices into one reliable
fast one; the arithmetic of how much redundancy, where, and how fast you repair decides
whether you lose data.

## RAID (Patterson, Gibson & Katz 1988)
Motivation: CPUs and memory improved 40 %/year, single large expensive disks did not
(Amdahl's balance again — [[performance-equation-and-amdahl]]); arrays of PC disks give
parallel bandwidth, but MTTF of 100 disks is 1/100 of one — so add redundancy.
| Level | Scheme | Capacity | Tolerates | Notes |
|---|---|---|---|---|
| 0 | striping only | N | 0 | throughput; reliability worse than one disk |
| 1 | mirroring | N/2 | 1 per pair | fast reads, 2× writes |
| 2/3/4 | bit/byte/block striping with Hamming or dedicated parity | N−1 | 1 | parity disk is a write bottleneck (4) |
| **5** | block striping, rotated parity | N−1 | 1 | **small-write problem**: read old data + old parity, write new data + new parity (4 I/Os); stripe writes are cheap |
| **6** | two parities (P + Q, Reed–Solomon) | N−2 | 2 | needed once rebuild takes days |
| 10 (1+0) | mirrored stripes | N/2 | 1 per mirror | databases, fast rebuild |
Implementation: hardware controllers with battery-backed cache vs software (Linux md, ZFS
RAID-Z, Windows Storage Spaces). **Write hole**: crash between data and parity updates leaves
an inconsistent stripe — ZFS/btrfs avoid it with copy-on-write full-stripe writes and
checksums ([[file-systems]]). **Rebuild**: reading every surviving disk for hours/days with
elevated load and correlated failures (same batch, same age); unrecoverable read errors during
rebuild (~1 in 10^14–10^15 bits) make RAID 5 on multi-TB disks statistically unsafe — hence
RAID 6, triple mirrors, and declustered RAID (spread rebuild across all disks).

## Durability arithmetic
Annual failure rate (AFR) in fleets 1–4 % for disks (Schroeder & Gibson 2007; Backblaze),
lower replacement but more uncorrectable errors for SSDs ([[ssd-and-nvme-storage]]).
Mean time to data loss for mirrored pairs ≈ MTTF² / (2·MTTR): shorter repair matters as
much as better disks — fast detection and rebuild dominates. Correlated failures (power,
firmware, rack, AZ, software bugs, operator error) break independence assumptions — spread
copies across **failure domains**; count the durability in nines per year (S3 claims 11)
with explicit models (Markov chains of failure/repair states — [[markov-chains]]).

## Erasure coding at scale
**Replication** (3× in GFS/HDFS): simple, fast reads, 200 % overhead. **Reed–Solomon (k, m)**
over a Galois field: k data fragments + m parity; any k of k+m reconstruct; overhead m/k
(e.g. RS(10,4) = 1.4× tolerating 4 losses — used by Colossus, HDFS-EC, Azure, Ceph, S3
tiers); costs — encoding CPU (Intel ISA-L, SIMD — [[parallel-architectures-simd-gpu]]),
reads must gather k fragments (latency), and **repair traffic** of k fragments to rebuild one.
**Local reconstruction codes** (Azure LRC, Facebook HDFS-Xorbas) add local parities so
single-fragment repair reads a few fragments; regenerating codes minimize repair bandwidth.
Hot data replicated, cold data erasure-coded; hybrid tiers.
([[channel-capacity-and-error-correction]] for the coding theory; [[fft]] for fast RS.)

## Integrity
Disks and buses return wrong data silently (bit rot, misdirected writes, firmware bugs —
CERN found ~1 in 10^7 files); RAID parity alone doesn't detect which copy is wrong.
**End-to-end checksums** (ZFS, Ceph BlueStore, GFS chunk checksums, S3 MD5/CRC32C on
put/get) locate corruption; **scrubbing** reads and verifies in the background; the end-to-end
argument for storage ([[internet-architecture-and-layering]]).

## Pitfalls
- RAID as backup (it doesn't protect against deletion, ransomware, or correlated loss).
- RAID 5 on large disks; rebuild windows without monitoring; hot spares that never get tested.
- Copies in the same failure domain (same rack, same AZ, same cloud account).
- Erasure coding hot, small objects (latency and repair cost); ignoring the CPU cost.
- No scrubbing or checksums: corruption discovered only at restore time.

## Related
- [[file-systems]], [[distributed-file-and-object-storage]], [[ssd-and-nvme-storage]],
  [[replication-and-partitioning]], [[channel-capacity-and-error-correction]],
  [[warehouse-scale-computing]], [[markov-chains]].

## Sources
Patterson, Gibson & Katz 1988; Chen et al. "RAID: High-Performance, Reliable Secondary Storage" 1994; Schroeder & Gibson 2007; Huang et al. "Erasure Coding in Windows Azure Storage" 2012; Sathiamoorthy et al. "XORing Elephants" 2013; OSTEP ch. 38.

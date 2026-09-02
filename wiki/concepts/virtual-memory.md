---
title: Virtual memory — address spaces, paging, page tables, TLBs, page faults, swapping and replacement
type: concept
section: "4.2"
level: 300
tags: [virtual-memory, address-space, address-translation, base-and-bounds, segmentation, paging, page-table, pte, multi-level-page-tables, tlb, tlb-miss, asid, page-fault, demand-paging, copy-on-write, swapping, page-replacement, lru, clock, thrashing, mmap, huge-pages, memory-protection]
sources: [ostep, xv6-and-6-1810, patterson-hennessy-cod, csapp-15-213]
summary: Each process sees a private, contiguous address space that the OS and MMU map onto scattered physical frames in fixed-size pages via per-process page tables (multi-level to stay sparse: Sv39/x86-64 use 3–5 levels of 4 KB pages), cached by the TLB (a miss costs a page-table walk; ASIDs avoid flushes on context switch); a page-table entry's present/protection bits turn accesses into page faults that the kernel uses for demand paging, lazy allocation, copy-on-write fork, memory-mapped files and swapping to disk with replacement policies (LRU approximated by clock; thrashing when working sets exceed RAM) — delivering transparency, efficiency and protection at once.
---
# Virtual memory

**In one sentence.** Every address a program uses is a lie the MMU translates, and the page
table is the dictionary — which lets the OS relocate, share, protect, and over-commit memory
without the program knowing.

## Goals and the translation idea (OSTEP ch. 13–16)
Address space: code, heap (grows up), stack (grows down), mapped libraries
([[memory-layout-stack-heap]]). Goals: **transparency**, **efficiency** (hardware translation),
**protection** (isolation). Early schemes: base-and-bounds (contiguous, external fragmentation),
**segmentation** (base/bounds per segment; sparse address spaces; still variable-size chunks →
fragmentation, compaction).

## Paging (OSTEP ch. 18–20)
- Fixed-size **pages** (4 KB; 2 MB/1 GB huge pages) map to physical **frames**. Virtual address
  = VPN | offset; the **page table** maps VPN → PFN; **PTE** bits: valid/present, R/W/X,
  user, dirty, accessed, cache-disable. A linear table for 2⁴⁸ bytes is impossible, so tables
  are **multi-level** (radix trees: x86-64 4–5 levels of 512 entries, RISC-V Sv39 3 levels)
  and only populated where the address space is used; inverted/hashed tables are the
  alternative.
- **TLB**: a small fully-associative cache of translations (64–2048 entries); hit → 1 cycle
  extra; miss → hardware page walker (x86, RISC-V) or software trap (MIPS) costing 10s–100s of
  cycles; **ASIDs** tag entries so context switches need no flush; TLB reach (entries × page
  size) is why huge pages matter for big working sets ([[caches-and-memory-hierarchy]]). Caches
  are typically virtually indexed, physically tagged to overlap lookup.
- Page table pages themselves are cached; a TLB miss on a 4-level table can take 4 memory
  accesses — the reason for paging-structure caches.

## Page faults as a mechanism (xv6 ch. 4, OSTEP ch. 21)
Accessing a non-present or protected page traps to the kernel
([[limited-direct-execution-and-syscalls]]), which can: allocate on first touch (**lazy
allocation** of heap/stack), load from the executable/file on demand (**demand paging**, `mmap`),
**copy-on-write** (fork shares pages read-only; the first write copies — makes fork cheap),
fetch from swap, grow the stack, implement guard pages, user-level VM tricks (GC barriers,
persistent memory). Everything is a fault handler plus PTE bits.

## Swapping and replacement (OSTEP ch. 21–22)
When RAM is over-committed, evict pages to a **swap** device; the **present bit** marks
swapped-out pages. Policies: optimal (Belady's MIN — evict the page used furthest in future;
the lower bound), FIFO (Belady's anomaly: more frames can mean more misses), random, **LRU**
(good, expensive) approximated by **clock** (accessed bit, second chance) with dirty-bit
preference; page daemons keep a free pool (high/low watermarks); prefetching, clustering writes.
**Thrashing**: the sum of working sets exceeds memory → admission control or kill (OOM killer).
Modern: NVMe swap, zswap compression, memory tiering, cgroup limits.

## APIs and practice
`mmap` (file-backed or anonymous; shared vs private), `mprotect`, `madvise`, `mlock`; huge
pages (`madvise(MADV_HUGEPAGE)`); measure with `perf stat -e dTLB-load-misses`, `/proc/pid/smaps`,
RSS vs virtual size. Memory-mapped I/O for databases ([[storage-engines-and-indexes]]),
[[garbage-collection]] interactions, and ASLR for security ([[memory-safety-and-buffer-overflows]]).

## Pitfalls
- Confusing virtual size with resident memory; over-committing and meeting the OOM killer.
- Ignoring TLB effects for large arrays (random access over GBs → TLB-miss bound; use huge pages).
- Sharing memory across processes without considering copy-on-write costs after fork (Redis
  snapshots).

## Related
- [[caches-and-memory-hierarchy]], [[limited-direct-execution-and-syscalls]], [[processes-and-threads]],
  [[memory-layout-stack-heap]], [[dynamic-memory-allocation]], [[file-systems]], [[os-kernels-and-virtualization]].

## Sources
OSTEP ch. 13–23; xv6 book ch. 3–4; COD 5.7; CSAPP ch. 9.

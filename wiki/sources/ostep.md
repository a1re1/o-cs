---
title: Operating Systems: Three Easy Pieces (Arpaci-Dusseau) and Wisconsin CS537
type: source
section: "4.2"
level: 300
tags: [ostep, operating-systems, virtualization, concurrency, persistence, processes, scheduling, virtual-memory, paging, tlb, threads, locks, condition-variables, semaphores, deadlock, file-systems, ffs, journaling, lfs, raid, ssd, distributed]
sources: []
authors: [Remzi Arpaci-Dusseau, Andrea Arpaci-Dusseau]
year: 2023
institution: University of Wisconsin–Madison
url: https://pages.cs.wisc.edu/~remzi/OSTEP/
license: free-online
format: pdf
summary: The free OS text organized around three pieces — virtualization (the process abstraction, limited direct execution, scheduling from FIFO to MLFQ and CFS, address spaces, segmentation, paging, TLBs, multi-level page tables, swapping and replacement policies), concurrency (threads, locks and how to build them, condition variables, semaphores, common concurrency bugs and deadlock, event-based concurrency), and persistence (I/O devices, disks, RAID, files and directories, file system implementation, FFS, crash consistency with journaling, LFS, flash SSDs, data integrity, distributed systems, NFS, AFS) — each chapter framed by a "crux of the problem" and homework simulators.
---
# Operating Systems: Three Easy Pieces

## What it is
Ch. 2 introduction: a running program just executes instructions (von Neumann); the OS
**virtualizes** resources (CPU, memory, disk) into easier virtual forms, exposes system calls (a
"standard library"), and acts as a resource manager; goals: abstraction, performance, protection,
reliability, energy. **Virtualization**: 4 the process (registers, address space, open files;
API — create, destroy, wait, misc control, status; creation: load, allocate stack/heap, init I/O),
5 process API (fork/exec/wait and why the separation lets the shell redirect), 6 **limited direct
execution** (user/kernel mode, trap table, system calls via trap, timer interrupts, context
switch), 7 scheduling (turnaround/response time; FIFO, SJF, STCF, round robin, I/O overlap), 8
MLFQ (learn from history, priority boost, gaming prevention), 9 lottery/stride, 10 multiprocessor
scheduling (cache affinity, per-CPU queues, CFS), 13 address spaces (code/heap/stack; goals:
transparency, efficiency, protection), 14 memory API, 15 address translation (base and bounds),
16 segmentation (external fragmentation), 17 free-space management (splitting/coalescing, best/
first/next fit, segregated lists, buddy), 18 **paging** (fixed-size pages avoid fragmentation;
page tables map VPN → PFN; overhead), 19 TLBs (hardware- vs OS-managed, ASIDs, locality), 20
smaller tables (multi-level page tables), 21–22 swapping (present bit, page faults, replacement
— FIFO, random, LRU, clock, Belady's anomaly, thrashing), 23 VAX/VMS case study, 24 summary.
**Concurrency**: 26 threads (one process, multiple PCs and stacks; the uncontrolled scheduling
problem; atomicity), 27 thread API, 28 locks (evaluate: mutual exclusion, fairness, performance;
building them — disable interrupts, test-and-set, compare-and-swap, LL/SC, fetch-and-add ticket
locks; spinning vs yielding vs queues/futexes), 29 lock-based data structures, 30 condition
variables (wait/signal, always use while, producer/consumer), 31 semaphores, 32 concurrency
bugs (atomicity violation, order violation, deadlock — four conditions and prevention/avoidance/
detection), 33 event-based concurrency. **Persistence**: 36 I/O devices (polling vs interrupts,
DMA, drivers), 37 hard disks (seek/rotate/transfer, scheduling), 38 RAID, 39 files and
directories (open/read/write/lseek, fsync, rename, links, mounts), 40 file system implementation
(inodes, bitmaps, indirect blocks, directories, access paths), 41 FFS (cylinder groups, locality),
42 crash consistency (fsck, journaling — data vs metadata, checksums), 43 LFS, 44 flash-based SSDs
(FTL, wear leveling), 45 data integrity, 47–49 distributed systems, NFS, AFS.

## Key ideas → pages
[[processes-and-threads]], [[limited-direct-execution-and-syscalls]], [[cpu-scheduling]],
[[virtual-memory]], [[synchronization-primitives]], [[file-systems]], [[os-kernels-and-virtualization]].

## What it adds
The most readable OS text; [[xv6-and-6-1810]] is the code, the seminal papers
([[os-seminal-papers]]) are the primary sources OSTEP summarizes.

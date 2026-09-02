---
title: OS seminal papers — UNIX (1974), THE (1968), Lampson's Hints (1983), FFS (1984), LFS (1992), Exokernel (1995), L4 µ-kernel (1995), Disco (1997), Xen (2003), Multics, Mach, Plan 9
type: source
section: "4.2"
level: 500
tags: [unix, ritchie-thompson, dijkstra-the, layered-design, semaphores, lampson-hints, ffs, lfs, log-structured, exokernel, microkernel, l4, liedtke, disco, xen, paravirtualization, multics, mach, plan9, history]
sources: []
authors: [Dennis Ritchie, Ken Thompson, Edsger Dijkstra, Butler Lampson, Marshall McKusick, Mendel Rosenblum, John Ousterhout, Dawson Engler, Jochen Liedtke, Edouard Bugnion, Paul Barham]
year: 1974
institution: various
url: https://dl.acm.org/doi/10.1145/361011.361061
license: various
format: pdf
summary: The primary sources behind OS design — UNIX's small set of orthogonal ideas (files as byte streams, everything-is-a-file, fork/exec, pipes, the shell as an ordinary program); Dijkstra's THE with layered structure and semaphores; Lampson's hints ("keep it simple", "make it fast", "use a good idea again", "handle normal and worst cases separately", "safety first", "end-to-end", "log updates", "make actions atomic") with the observation that interface design is the hardest part; FFS's cylinder groups and larger blocks for locality; LFS's write-everything-sequentially log with cleaning; Exokernel's "separate protection from management"; Liedtke's case that microkernels are slow only when badly built (IPC in ~100 cycles); Disco's VMM for commodity OSes on NUMA hardware and Xen's paravirtualization — and Multics, Mach, and Plan 9 as the ancestors and alternatives.
---
# OS seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Ritchie & Thompson, "The UNIX Time-Sharing System" (CACM 1974) | Files as unstructured byte streams; directories as files; devices as files; the file descriptor; fork/exec/wait; pipes and the shell as glue; "the most important achievement is to demonstrate that a powerful OS for interactive use need not be expensive" | [[processes-and-threads]], [[file-systems]], [[shell-and-unix-tools]] |
| Dijkstra, "The Structure of the THE Multiprogramming System" (1968) | Strict layering (each layer a virtual machine for the next: processor allocation, segment controller, console, I/O, user programs); semaphores as the synchronization primitive; a priori proof of correctness as design method | [[synchronization-primitives]], [[os-kernels-and-virtualization]] |
| Lampson, "Hints for Computer System Design" (SOSP 1983) | Functionality: separate normal and worst case, keep interfaces simple/complete/fast, don't generalize, get it right, plan to throw one away, keep secrets, use a good idea again, divide and conquer; Speed: split resources, use static analysis, cache answers, use hints, when in doubt use brute force, compute in background, batch processing; Fault-tolerance: end-to-end, log updates, make actions atomic | [[managing-complexity-in-software-design]], [[file-systems]] |
| McKusick et al., "A Fast File System for UNIX" (1984) | Cylinder groups placing inodes near data, 4 KB blocks with fragments, rotational awareness, long file names, file locking, symbolic links — 10× throughput over the original FS | [[file-systems]] |
| Rosenblum & Ousterhout, "The Design and Implementation of a Log-Structured File System" (1992) | Buffer all writes and write them sequentially as a log; inode map; segment cleaning with cost-benefit policy; fast crash recovery via checkpoints — the ancestor of SSD FTLs, LSM trees, and copy-on-write file systems | [[file-systems]], [[storage-engines-and-indexes]] |
| Engler, Kaashoek & O'Toole, "Exokernel" (SOSP 1995) | Separate protection from management: the kernel securely multiplexes hardware, library OSes implement abstractions; secure bindings, visible revocation, abort protocol | [[os-kernels-and-virtualization]] |
| Liedtke, "On µ-Kernel Construction" (SOSP 1995) | Microkernel slowness came from poor implementation, not the concept; minimal primitives (address spaces, threads, IPC), IPC in ~100 cycles, the L4 family (seL4 later formally verified) | [[os-kernels-and-virtualization]] |
| Bugnion et al., "Disco" (SOSP 1997); Barham et al., "Xen and the Art of Virtualization" (SOSP 2003) | Run commodity OSes on a VMM: Disco on NUMA multiprocessors with copy-on-write sharing; Xen's paravirtualized interface (hypercalls, shadow page tables) with near-native performance and 100 VMs per host — the cloud's foundation | [[os-kernels-and-virtualization]] |
| Corbató et al. (Multics), Accetta et al. (Mach, 1986), Pike et al. (Plan 9, 1995) | Multics: segmentation, rings, hierarchical FS, dynamic linking; Mach: microkernel with ports and external pagers (macOS's XNU descends from it); Plan 9: everything is a file *server*, 9P, per-process namespaces (containers' ancestor) | [[os-kernels-and-virtualization]] |

## Why read them
They are short, argued, and specific about trade-offs; OSTEP ([[ostep]]) is the tour, these are
the buildings.

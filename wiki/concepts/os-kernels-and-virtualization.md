---
title: Kernel architectures and virtualization — monolithic, microkernel, exokernel, unikernels; hypervisors, paravirtualization, containers
type: concept
section: "4.2"
level: 400
tags: [kernel-architecture, monolithic-kernel, microkernel, l4, sel4, exokernel, library-os, unikernel, plan9, virtualization, hypervisor, vmm, trap-and-emulate, paravirtualization, xen, disco, hardware-virtualization, vt-x, nested-page-tables, containers, namespaces, cgroups, kvm, firecracker]
sources: [os-seminal-papers, ostep, xv6-and-6-1810]
summary: Where to draw the kernel boundary is the recurring OS design question — monolithic kernels (Linux, xv6) put everything in one privileged address space for speed and simplicity of interfaces, microkernels (Mach, L4/seL4) keep only address spaces, threads and IPC in the kernel and were made fast by Liedtke's careful IPC design, exokernels/library OSes separate protection from management, unikernels compile app + libOS into one image — while virtualization stacks a hypervisor beneath whole OSes (trap-and-emulate, Disco's and Xen's paravirtualization, then hardware support like VT-x and nested page tables) and containers virtualize the kernel's namespaces and cgroups instead, the basis of cloud infrastructure.
---
# Kernel architectures and virtualization

**In one sentence.** Every layer that is "the OS" is a choice about which mechanisms need
privilege; virtual machines add a layer beneath, containers add one inside.

## Kernel structures
- **Monolithic** (Unix, Linux, xv6): one kernel address space with scheduler, VM, FS, drivers,
  network; procedure calls between subsystems; loadable modules. Fast; a driver bug is a kernel
  bug. Dijkstra's **THE** showed strict layering inside a monolith (each layer a virtual machine
  for the next).
- **Microkernel** (Mach, L3/L4, QNX, MINIX 3, Fuchsia's Zircon): kernel provides address spaces,
  threads, **IPC**; file systems, drivers, network run as user servers. Early ones were slow
  (Mach IPC ~100 µs); Liedtke's L4 showed IPC in ~100 cycles with careful design (small kernel
  that fits in cache, register-based message passing, no policy). **seL4**: formally verified
  functional correctness. Cost is still the extra context switches per operation; benefit is
  isolation and restartable servers.
- **Exokernel** (Engler et al. 1995): "separate protection from management" — the kernel securely
  multiplexes raw hardware (secure bindings, visible revocation), and **library operating
  systems** implement abstractions per application (a database can manage its own pages and
  disk layout). Unikernels (MirageOS, OSv) and Firecracker-style microVMs are the descendants;
  DPDK/SPDK bypass the kernel for the same reason.
- **Plan 9**: everything is a file *server* spoken to via 9P; per-process **namespaces** — the
  idea Linux borrowed for containers. Hybrid kernels (XNU: Mach + BSD; Windows NT) mix models.
- Where Linux is today: monolithic core, user-space drivers where latency allows (FUSE, VFIO),
  eBPF for safe in-kernel extension, io_uring for batched syscalls.

## Virtual machines (Disco 1997, Xen 2003, OSTEP appendix)
- A **VMM/hypervisor** runs guest OSes: Type 1 on bare metal (Xen, ESXi, Hyper-V), Type 2 hosted
  (VirtualBox); KVM turns Linux into a Type 1.
- **Trap-and-emulate** (Popek–Goldberg): run the guest kernel in user mode; privileged
  instructions trap to the VMM, which emulates them. x86 had non-trapping sensitive instructions
  → binary translation (VMware) or **paravirtualization** (Xen: modify the guest to make
  hypercalls; shadow page tables; near-native performance, ~100 guests).
- **Hardware virtualization** (VT-x/AMD-V, 2006+): a guest mode with its own privilege levels;
  **nested/extended page tables** translate guest-virtual → guest-physical → host-physical (a TLB
  miss can walk both tables: up to 24 memory accesses — [[virtual-memory]]); I/O via emulated
  devices, paravirtual drivers (virtio), or direct assignment (SR-IOV/IOMMU).
- **Disco** anticipated all of this: commodity OSes on NUMA machines with transparent page
  sharing and memory migration.
- Uses: server consolidation, isolation for multi-tenant clouds, live migration, snapshots,
  testing kernels; costs: memory duplication, I/O overhead, noisy neighbours.

## Containers
Not virtual machines: **namespaces** (pid, mount, net, user, uts, ipc) give each container its
own view of the kernel's resources; **cgroups** limit and account CPU, memory, I/O; capabilities,
seccomp, and LSMs restrict syscalls; layered image file systems (overlayfs). One kernel shared →
lightweight (ms startup) but a kernel exploit escapes; gVisor (user-space kernel) and Firecracker
(minimal VMs) trade back toward VM isolation ([[security-principles]]).

## Pitfalls
- Assuming containers isolate like VMs; running untrusted code without a VM or sandbox layer.
- Nested virtualization and TLB cost for memory-heavy guests (use huge pages).
- Microkernel "purity" that ignores the syscall/IPC budget of real workloads — measure.

## Related
- [[limited-direct-execution-and-syscalls]], [[virtual-memory]], [[processes-and-threads]],
  [[file-systems]], [[security-principles]], [[distributed-systems-basics]], [[io-and-device-drivers]].

## Sources
Dijkstra 1968; Engler et al. 1995; Liedtke 1995; Bugnion et al. 1997; Barham et al. 2003; OSTEP appendix (VMMs); Pike et al. Plan 9.

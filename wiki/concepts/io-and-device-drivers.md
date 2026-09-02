---
title: I/O and device drivers — memory-mapped registers, polling vs interrupts, DMA, the block and network stacks, and driver structure
type: concept
section: "4.2"
level: 300
tags: [io, device-drivers, memory-mapped-io, port-io, device-registers, polling, interrupts, interrupt-handlers, top-half, bottom-half, dma, scatter-gather, iommu, pci, pcie, block-layer, request-queue, io-scheduler, blk-mq, network-stack, napi, interrupt-coalescing, driver-model, kernel-modules, user-space-drivers, vfio, virtio, io_uring, asynchronous-io]
sources: [ostep, xv6-and-6-1810, storage-and-cloud-seminal-papers]
summary: A device is a set of registers (status, command, data) reached by memory-mapped or port I/O; the OS talks to it by polling (spin until ready — low latency, wastes CPU) or by letting it raise an interrupt (efficient when slow, livelock-prone when fast — so drivers coalesce and switch to polling under load, as Linux NAPI does), and moves bulk data by DMA (the device reads/writes memory directly, with scatter-gather lists and an IOMMU for protection); drivers hide device specifics behind class interfaces (block, character, network) so the rest of the kernel is device-independent — the block layer queues, merges and schedules requests (multi-queue blk-mq for NVMe), the network stack hands packets to sockets — and interrupt work is split into a fast top half and deferred bottom half; drivers are most of any kernel's code and most of its bugs, motivating user-space drivers (VFIO, DPDK, SPDK), paravirtual devices (virtio), and asynchronous interfaces (io_uring) that let one thread keep deep device queues full.
---
# I/O and device drivers

**In one sentence.** The OS's job at the bottom is to turn "wait for a register bit" into a
uniform, asynchronous, protected service — and to survive the fact that device code is the
buggiest code it runs.

## Talking to a device (OSTEP ch. 36; xv6 uart/virtio_disk)
A device presents **registers** — status, command, data — either at I/O port addresses (x86
`in`/`out`) or **memory-mapped** (loads/stores to special physical addresses; must be marked
uncacheable and accessed with volatile/barriers — [[cache-coherence-and-memory-consistency]]).
Canonical protocol: wait until not busy → write data → write command → wait until done.
**Polling** wastes CPU while waiting; **interrupts** let the CPU run something else and the
device signal completion via the interrupt controller (PIC/APIC, MSI-X vectors per queue) →
handler ([[limited-direct-execution-and-syscalls]]). Interrupts cost context switches and can
**livelock** a system under a flood (10 Gb NICs), so real drivers use **interrupt coalescing**
and hybrid polling (Linux **NAPI**: interrupt once, then poll while packets keep coming).
**DMA**: the CPU programs the device with buffer addresses and the device transfers data
itself; **scatter-gather** lists for non-contiguous buffers; the **IOMMU** translates and
restricts device addresses (protection from buggy/malicious devices, needed for VFIO and
virtualization); cache coherence with DMA (bounce buffers, `dma_sync`).

## Driver structure
Kernels organize devices by class: **character** (byte streams — terminals, serial), **block**
(fixed-size sectors, random access — disks; go through the buffer cache), **network** (packets).
Above the driver: a device-independent layer (VFS, block layer, socket layer); below: bus
drivers (PCI/PCIe enumeration, USB, I²C/SPI in embedded — [[microcontrollers-and-embedded-programming]]).
Interrupt handling is split: **top half** (acknowledge, grab data, schedule) and **bottom
half** (softirq/tasklet/workqueue/threaded IRQ — the real work, preemptible). Drivers as
loadable kernel modules; the driver model (device tree on ARM, ACPI on x86) for discovery.
Device drivers are ~70 % of Linux source and historically 3–7× the bug rate of the rest
(Chou et al. 2001) — hence isolation efforts: user-space drivers (**VFIO**, DPDK/SPDK
with polling for line-rate I/O), microkernel driver servers ([[os-kernels-and-virtualization]]),
Rust for Linux, driver synthesis.

## The block layer (OSTEP ch. 37, 44; Linux blk-mq)
Requests carry (device, sector, length, buffer); the layer merges adjacent requests, sorts them
(**I/O schedulers**: elevator/deadline/CFQ for disks, none/mq-deadline/BFQ for SSDs), applies
fairness, and dispatches; **blk-mq** gives per-CPU software queues mapped to hardware queues
(NVMe) to avoid lock contention ([[ssd-and-nvme-storage]]). Disk geometry basics: seek +
rotation + transfer; SSTF/SCAN scheduling; why sequential wins ([[file-systems]]). Completion
via interrupt → bio callback → wake the waiting process. **Asynchronous I/O**: `aio`,
**io_uring** (submission/completion rings shared with the kernel; no syscall per I/O; also
covers sockets and files) — the interface that keeps NVMe queues full from one thread
([[async-and-event-driven-concurrency]]).

## The network path
NIC DMA ring buffers → interrupt/NAPI poll → driver → protocol stack (IP, TCP —
[[tcp-reliability-and-congestion-control]]) → socket receive queue → `recv`. Offloads (checksum,
segmentation — TSO/GSO/LRO, RSS to spread flows across queues/cores), zero-copy (`sendfile`,
`MSG_ZEROCOPY`), XDP/eBPF for early packet processing, kernel bypass (DPDK) for millions of
packets per second ([[sockets-programming]]).

## Virtual devices
Trap-and-emulate real devices (slow), **virtio** paravirtual drivers (shared ring queues —
virtqueues — between guest driver and host), SR-IOV/passthrough with the IOMMU (near-native),
vhost/user-space backends; the same virtqueue idea in Firecracker, gVisor, WSL
([[os-kernels-and-virtualization]]).

## Pitfalls
- Sleeping in interrupt context; long handlers; missing barriers on MMIO.
- DMA into pageable/cached memory without sync; buffer overruns from device-supplied lengths
  (security — devices are untrusted inputs).
- Polling everywhere (CPU burn) or interrupts everywhere (livelock).
- Assuming a completed write is durable (device write caches; flush/FUA — [[file-systems]]).

## Related
- [[limited-direct-execution-and-syscalls]], [[file-systems]], [[ssd-and-nvme-storage]],
  [[os-kernels-and-virtualization]], [[sockets-programming]], [[async-and-event-driven-concurrency]],
  [[microcontrollers-and-embedded-programming]], [[virtual-memory]].

## Sources
OSTEP ch. 36–37, 44; xv6 book ch. 5 (interrupts and device drivers); Linux Device Drivers (Corbet, Rubini, Kroah-Hartman); Mogul & Ramakrishnan "Eliminating receive livelock" 1997; Chou et al. "An Empirical Study of Operating Systems Errors" 2001.

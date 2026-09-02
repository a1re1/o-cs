---
title: Processes and threads — the process abstraction, fork/exec/wait, context switches, and threads
type: concept
section: "4.2"
level: 300
tags: [processes, threads, process-abstraction, address-space, pcb, fork, exec, wait, exit, context-switch, file-descriptors, pipes, signals, zombies, thread-control-block, user-threads, kernel-threads, green-threads, pthreads]
sources: [ostep, xv6-and-6-1810, os-seminal-papers, csapp-15-213]
summary: A process is a running program — its address space, registers/PC, open file descriptors, and kernel bookkeeping (PID, state, parent) — that the OS creates by loading code, allocating stack and heap and setting up I/O; Unix creates processes with fork (clone) and exec (replace the image) plus wait, a separation that lets the shell redirect and pipe; a context switch saves one process's registers and restores another's; threads are multiple execution contexts (PC, registers, stack) sharing one address space, cheaper to switch and able to share data — which is exactly why they need synchronization.
---
# Processes and threads

**In one sentence.** The OS turns one CPU into many virtual CPUs by time-slicing processes;
threads are lighter virtual CPUs inside one address space.

## The process (OSTEP ch. 4–5)
- **Machine state**: address space (code, data, heap, stack — [[memory-layout-stack-heap]]),
  registers incl. PC and SP, I/O state (open file descriptors — 0/1/2 by default), plus kernel
  metadata in the **PCB** (`struct proc` in xv6: state, pid, parent, kernel stack, page table,
  trapframe, context, open files, cwd).
- **States**: running, ready, blocked (waiting on I/O or a lock); transitions by the scheduler
  and by events ([[cpu-scheduling]]).
- **Creation**: load the executable (ELF) into the address space (eagerly or lazily via paging),
  allocate the stack (with argc/argv) and heap, set up stdin/stdout/stderr, jump to `main`.
- **API (Unix)**: `fork()` clones the caller (child gets a copy of the address space — copy-on-
  write — and returns 0; parent gets the child's PID), `exec()` replaces the image with a new
  program (keeping open descriptors), `wait()` blocks for a child and collects its exit status
  (otherwise it becomes a **zombie**; orphans are reparented to init), `exit()`, `kill`/signals
  (SIGINT, SIGTERM, SIGKILL, SIGCHLD; handlers run asynchronously — reentrancy hazards), `getpid`.
  Why fork/exec are separate: the shell can alter the child's environment *between* them —
  redirect (`close(1); open(file)` → fd 1), set up pipes (`pipe()`, `dup2`), change cwd/limits —
  without any special API (Ritchie & Thompson). `posix_spawn`/`vfork`/`clone` are the modern
  optimizations. Windows `CreateProcess` bundles the two.
- **Context switch** (OSTEP 6): on a timer interrupt or syscall the kernel saves user registers
  to the trapframe, the scheduler saves callee-saved registers/SP of the current kernel thread
  (`swtch` in xv6) and restores another's; switching processes also switches the page table
  (TLB flush unless ASIDs). Cost: ~1–5 µs direct plus cache/TLB pollution.

## Threads (OSTEP ch. 26–27)
- Multiple **PCs and stacks** in one address space; per-thread TCB; shared heap and globals.
  Creation `pthread_create`, `join`; thread-local storage.
- Why: parallelism on multicore; overlap I/O with computation; simpler structure for servers
  (thread per connection) vs event loops ([[async-and-event-driven-concurrency]]).
- Cost: the danger — uncontrolled interleaving on shared data (the counter `x++` race: load,
  add, store interleaved) → **race conditions**, **indeterminate** results; needs
  [[synchronization-primitives]]. Thread stacks are small (MBs) — deep recursion overflows.
- **Kernel threads** (1:1, Linux NPTL, scheduled by the OS, can block independently) vs **user
  threads** (N:1 or M:N — green threads, goroutines, Rust async tasks: cheap creation and
  switching, cooperative or runtime-scheduled, a blocking syscall stalls the carrier unless the
  runtime intercepts it). Fibers/coroutines are the language-level form.
- Processes vs threads: isolation (a crash or leak is contained; separate address spaces) vs
  sharing (cheap communication, cheap creation); IPC (pipes, sockets, shared memory, message
  queues, signals) bridges processes.

## Pitfalls
- Forgetting `wait` (zombies) or calling non-async-signal-safe functions in handlers.
- fork in a multithreaded program (only the calling thread survives in the child; locks held by
  others stay locked — use `exec` immediately or `posix_spawn`).
- Assuming thread scheduling order; sharing data without synchronization ([[undefined-behavior]]
  data races).
- Thread-per-request without limits (thousands of stacks; use pools or async).

## Related
- [[limited-direct-execution-and-syscalls]], [[cpu-scheduling]], [[virtual-memory]],
  [[synchronization-primitives]], [[shell-and-unix-tools]], [[memory-layout-stack-heap]],
  [[async-and-event-driven-concurrency]].

## Sources
OSTEP ch. 4–6, 26–27; xv6 book ch. 1, 7; Ritchie & Thompson 1974; CSAPP ch. 8.

---
title: Limited direct execution — user/kernel mode, traps, system calls, interrupts, and exceptions
type: concept
section: "4.2"
level: 300
tags: [limited-direct-execution, user-mode, kernel-mode, privilege-levels, trap, trap-table, system-calls, syscall, interrupts, timer-interrupt, exceptions, page-fault, trapframe, exceptional-control-flow, vdso, io_uring, syscall-cost]
sources: [ostep, xv6-and-6-1810, csapp-15-213]
summary: The OS runs programs directly on the CPU for speed but limits them with hardware privilege modes — user code cannot touch devices, page tables or interrupts, so it asks via a system call that traps into the kernel through a trap table set up at boot (saving registers to a trapframe, switching to a kernel stack, dispatching on the syscall number, returning with a privileged return-from-trap); timer interrupts give the kernel control back for scheduling, and exceptions (page faults, illegal instructions, divide by zero) use the same path, which is how demand paging, copy-on-write, signals and debuggers work — and why syscalls cost ~100s of ns and are batched by fast paths like vDSO and io_uring.
---
# Limited direct execution and system calls

**In one sentence.** Run the program on the bare CPU, but arrange that anything dangerous or
any long-running stretch of time lands in the kernel through a trap.

## The two problems (OSTEP ch. 6)
1. **Restricted operations**: user mode (RISC-V U, x86 ring 3) cannot execute privileged
   instructions (I/O, page-table writes, interrupt masking). To do I/O the program executes a
   **system call** instruction (`ecall`, `syscall`) which raises the privilege level and jumps to
   a kernel entry point fixed by the **trap table** (`stvec`; IDT on x86) registered at boot — the
   program cannot choose where it lands. The kernel saves user registers (**trapframe**), switches
   to the process's kernel stack, dispatches on the syscall number in a register (`a7`/`rax`),
   validates arguments (copy in/out from user memory — never trust user pointers), does the work,
   and returns with `sret`/`sysret`, restoring user mode. xv6: `uservec` → `usertrap` → `syscall`
   → `usertrapret` → `userret`, via a **trampoline** page mapped in every address space.
2. **Switching between processes**: a cooperative OS waits for syscalls/yields (a buggy program
   hangs the machine); a **timer interrupt** (every ~1–10 ms) forces entry into the kernel, whose
   handler may run the scheduler and **context switch** ([[processes-and-threads]],
   [[cpu-scheduling]]). Interrupts must be disabled during the switch; nested interrupts and
   re-entrancy need care.

## Exceptional control flow (CSAPP ch. 8)
| Kind | Cause | Async? | Return to |
|---|---|---|---|
| Interrupt | device signal (timer, disk, NIC, keyboard) | yes | next instruction |
| Trap | intentional (`syscall`, breakpoint) | no | next instruction |
| Fault | recoverable error (page fault, protection fault) | no | *same* instruction after fixing (demand paging, copy-on-write, lazy allocation — [[virtual-memory]]) |
| Abort | unrecoverable (machine check) | no | terminate |
The kernel turns faults into **signals** for the process (SIGSEGV on bad access, SIGFPE), which
is how debuggers (breakpoints via `int3`/trap), profilers (timer signals), and garbage collectors
(write barriers via protection faults) work. Interrupt handlers run with interrupts off, do
minimal work, and defer the rest (bottom halves, softirqs, threaded IRQs) ([[io-and-device-drivers]]).

## Cost and fast paths
A syscall is a mode switch plus register save/restore and cache/TLB effects: ~50–300 ns (more
with Spectre/Meltdown mitigations like KPTI). Programs batch (`writev`, `readv`), buffer
(stdio), use **vDSO** for `gettimeofday`, memory-map files ([[virtual-memory]]), and use
**io_uring**/`epoll` to submit many I/Os per switch ([[async-and-event-driven-concurrency]]).
The kernel/user boundary is also the security boundary: every syscall is attack surface
(seccomp filters, sandboxes) ([[security-principles]]).

## Pitfalls
- Kernel code trusting user pointers or lengths (TOCTOU races on copy-in).
- Forgetting that signal handlers interrupt arbitrary code (use async-signal-safe functions,
  `sigaction` with SA_RESTART, or signalfd).
- Assuming syscalls are cheap in hot loops (strace -c to count them —
  [[profiling-and-performance]]).

## Related
- [[processes-and-threads]], [[cpu-scheduling]], [[virtual-memory]], [[calling-conventions-and-the-stack]],
  [[io-and-device-drivers]], [[security-principles]], [[pipelining-and-hazards]] (precise exceptions).

## Sources
OSTEP ch. 6; xv6 book ch. 4–5; CSAPP ch. 8.

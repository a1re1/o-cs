---
title: Memory safety — buffer overflows, stack smashing, and their defences
type: concept
section: "2.3"
level: 300
tags: [memory-safety, buffer-overflow, stack-smashing, use-after-free, dangling-pointer, double-free, stack-canary, aslr, nx-bit, dep, rop, return-oriented-programming, cfi, attacklab, sanitizers, bounds-checking]
sources: [csapp-15-213, rust-book, stanford-cs107]
summary: A memory-safety bug lets a program read or write memory it should not (out of bounds, after free, uninitialized, through a wrong type); a buffer overflow on the stack overwrites the return address to hijack control; defences stack up — canaries, non-executable stacks, ASLR, control-flow integrity, sanitizers, bounds-checked libraries — and memory-safe languages remove the class entirely, which is why ~70% of serious CVEs in C/C++ codebases were memory-safety bugs.
---
# Memory safety and buffer overflows

**In one sentence.** Memory safety = every access is to a valid, live, correctly typed object; C and
C++ leave it to the programmer, attackers exploit the gap, and defences are layers that raise the cost
rather than closing it.

## The bug classes
Spatial: out-of-bounds read/write (buffer overflow/underflow, off-by-one).
Temporal: use-after-free, double free, dangling stack pointers, uninitialized reads.
Type: strict-aliasing violations, wrong-type function pointers. Concurrency: data races.
All are [[undefined-behavior]]; the "usually works" cases hide the ones that don't.

## Stack smashing (CSAPP 3.10, attacklab)
`gets(buf)` into a 32-byte local: input longer than the buffer walks up the frame over saved
registers and the **return address** ([[calling-conventions-and-the-stack]]). Classic exploit: inject
shellcode into the buffer and point the return address at it; modern exploit: **return-oriented
programming** (ROP) chains addresses of existing code fragments ending in `ret` so no injected code
executes. Heap variants corrupt allocator metadata or adjacent objects
([[dynamic-memory-allocation]]); format-string bugs (`printf(user)`) read/write arbitrary stack slots;
integer overflow in a size computation leads to an undersized buffer ([[integer-representation-and-bits]]).

## Defences (each defeats one previous attack)
| Defence | Stops | Bypass |
|---|---|---|
| Bounds-checked APIs (`fgets`, `snprintf`, `strlcpy`), compiler `_FORTIFY_SOURCE` | the obvious overflow | logic bugs in size math |
| **Stack canary** (random value before the return address, checked at `ret`) | naive return-address overwrite | leaking the canary, non-stack targets |
| **NX/DEP** (non-executable stack) | injected shellcode | ROP |
| **ASLR** (randomize stack/heap/library bases) | hard-coded addresses in ROP chains | info leaks, brute force on 32-bit |
| **CFI / shadow stacks / CET** | ROP by validating indirect branches/returns | data-only attacks |
| Sanitizers (ASan/UBSan/MSan/TSan) in test; fuzzing ([[fuzzing]]) | find bugs before ship | coverage gaps |
| Memory-safe languages (Rust, Go, Java, Swift) | the whole class | `unsafe`, FFI, logic bugs |

## The Rust answer
Bounds checks on slices, no null, ownership + borrowing (no dangling, no double free, no data races)
— [[ownership-and-borrowing]]. Microsoft and Google both reported ~70% of their security bugs were
memory-safety issues, which drove Rust into Android, Windows and Linux kernels.

## Related
- [[undefined-behavior]], [[calling-conventions-and-the-stack]], [[pointers-and-memory]],
  [[dynamic-memory-allocation]], [[ownership-and-borrowing]], [[fuzzing]], [[security-principles]].

## Sources
CSAPP 3.10 and attacklab; CS107 "Banking on Security"; CS110L lecture 2; Rust Book ch. 4, 19.

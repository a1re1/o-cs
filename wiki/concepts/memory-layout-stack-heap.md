---
title: Process memory layout — stack, heap, static data, and object lifetimes
type: concept
section: "2.3"
level: 200
tags: [memory-layout, stack, heap, static-storage, text-segment, bss, storage-duration, lifetimes, stack-frames, dangling-pointers, stack-overflow, address-space]
sources: [csapp-15-213, stanford-cs107, rust-book, modern-c-gustedt]
summary: A process's address space has code, read-only data, initialized/uninitialized static data, a growing heap, shared libraries, and a downward-growing stack of frames; every object has a storage duration (automatic, static, allocated, thread) that fixes when it dies — and most memory bugs are a pointer outliving the storage it points to.
---
# Memory layout: stack, heap, static

**In one sentence.** Know which region an object lives in and you know its lifetime, its cost, and
who must free it.

## The picture (x86-64 Linux, low → high)
```
text (code, read-only) → rodata (literals) → data (initialized globals) → bss (zeroed globals)
→ heap (brk/mmap; grows up) → … → mmap region (shared libs, large mallocs) → stack (grows down) → kernel
```
Virtual addresses; the OS maps pages on demand ([[virtual-memory]]). ASLR randomizes stack/heap/lib
bases per run.

## Storage durations (Modern C)
| Duration | Where | Lifetime | Created by |
|---|---|---|---|
| automatic | stack frame (or registers) | until the block exits | locals, parameters |
| static | data/bss | whole program | globals, `static` locals, string literals |
| allocated | heap | until `free` | `malloc`/`calloc`/`realloc` |
| thread | per-thread static | thread lifetime | `_Thread_local` |

## Stack
- Each call pushes a **frame**: return address, saved registers, locals, spill space
  ([[calling-conventions-and-the-stack]]). Push/pop is one instruction; allocation is free; size is
  fixed at compile time (VLAs/`alloca` aside).
- Default limits ~8 MB (Linux main thread), often 1–2 MB for spawned threads: deep recursion or large
  local arrays ⇒ **stack overflow** (segfault) ([[recursion-and-iteration]]).
- A pointer to a local becomes **dangling** when the function returns; the memory is reused by the
  next call — bugs appear "randomly" ([[memory-safety-and-buffer-overflows]]).
- Rust: fixed-size values live on the stack; `String`/`Vec` are stack structs (ptr, len, cap) owning a
  heap buffer ([[ownership-and-borrowing]]).

## Heap
- Explicitly sized, arbitrary lifetime, slower (allocator search + pointer chasing, cache misses).
- Ownership discipline: exactly one `free` per `malloc`, no use after free, no double free
  ([[dynamic-memory-allocation]]). Growing containers `realloc` (may move — old pointers dangle).
- Fragmentation and allocator overhead: many small objects are expensive; arenas/pools batch them.

## Static
- Zero-initialized (bss) by default; globals are shared across threads (races) and make code hard to
  test ([[code-review]]). String literals are read-only: writing to `"abc"` segfaults.

## Rules of thumb
- Prefer stack for small, short-lived data; heap for large, variable-size, or escaping data.
- Never return pointers to automatic storage; either return by value, use static (non-reentrant), or
  malloc and document that the caller frees.
- In C++/Rust, RAII/Drop ties allocated-storage lifetime to a stack object — the best of both.

## Related
- [[pointers-and-memory]], [[dynamic-memory-allocation]], [[calling-conventions-and-the-stack]],
  [[virtual-memory]], [[ownership-and-borrowing]], [[memory-safety-and-buffer-overflows]].

## Sources
CSAPP 3.7, 9.9; CS107 lecture 7; Rust Book 4.1 (stack and heap); Modern C level 2 (storage).

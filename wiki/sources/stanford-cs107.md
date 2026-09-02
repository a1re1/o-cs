---
title: Stanford CS107 Computer Organization and Systems
type: source
section: "2.3"
level: 200
tags: [c, unix, bits, c-strings, pointers, arrays, stack, heap, void-pointers, function-pointers, x86-64, assembly, heap-allocator]
sources: []
institution: Stanford
year: 2026
url: https://web.stanford.edu/class/cs107/
license: unknown
format: html
summary: Stanford's C-and-systems course (open lectures, labs with solutions, assignments) — Unix and C, integers/bits/bytes, chars and C-strings, pointers and arrays, stack and heap, generic `void*` operations, function pointers, x86-64 assembly, condition codes and control flow, the runtime stack, alignment and optimization, managing the heap, sockets — culminating in writing a heap allocator.
---
# Stanford CS107

## What it is
Level 200 (after CS106B). Seven weeks: 1 welcome, Unix and C, integers/bits/bytes; 2 chars and
C-strings, pointers and arrays; 3 pointers and arrays, stack and heap, generic operations with
`void *`; 4 function pointers, intro to assembly; 5 arithmetic/logic ops, x86-64 condition codes and
control flow; 6 the runtime stack, alignment/optimization/basic architecture, managing the heap;
7 sockets, review. Assignments: bit manipulation ("A Bit of Fun"), C strings, "A Heap of Fun" (stack vs
heap), "Into the void*" (generics via `void*` and function pointers), "Banking on Security" (assembly and
security), heap allocator. Labs with solutions; a testing-strategies guide.

## Key ideas → pages
- C strings are `char` arrays terminated by `\0`; `strlen` vs `sizeof`; off-by-one and missing
  terminators are the source of most CS107 bugs — [[pointers-and-memory]].
- Generic C: `void *`, `memcpy`, function pointers for comparators (`qsort`) — the pre-generics way to
  write reusable code — [[function-pointers-and-generic-c]].
- Stack vs heap lifetimes; returning pointers to locals; `malloc`/`realloc`/`free` discipline —
  [[memory-layout-stack-heap]], [[dynamic-memory-allocation]].
- Reading x86-64 to understand what the compiler did with your code —
  [[calling-conventions-and-the-stack]].

## What it adds
More hands-on C than [[csapp-15-213]] (which moves faster to architecture and OS topics); the `void*`
assignment is the best explanation of why languages grew generics ([[type-systems]]).

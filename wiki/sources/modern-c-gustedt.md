---
title: Modern C (Gustedt) and The C Programming Language (Kernighan & Ritchie)
type: source
section: "2.3"
level: 200
tags: [c, c23, k-and-r, undefined-behavior, integers, pointers, arrays, const, restrict, atomics, threads, standard-library]
sources: []
authors: [Jens Gustedt, Brian Kernighan, Dennis Ritchie]
year: 2024
institution: INRIA / Bell Labs
url: https://gustedt.gitlabpages.inria.fr/modern-c/
license: CC-BY-NC-ND
format: pdf
summary: Modern C (free, C23 edition) teaches C as it is today in five levels — encounter, acquaintance (control, arithmetic, aggregates, pointers as opaque, functions, style), cognition (pointers, the C memory model, storage, malloc, error handling, generic programming with _Generic), experience (performance, functions pointers, atomics, threads), ambition — while K&R (1988) remains the concise classic that defined the idiom.
---
# Modern C (Gustedt) / The C Programming Language (K&R)

## What it is
Modern C levels: **0 Encounter** (getting started, the principal structure of a program); **1
Acquaintance** (everything is about control; expressing computations; basic values and data — integer
types, `size_t`, unsigned wraparound, signed overflow is UB; derived data types — arrays, pointers as
opaque types, structs, unions; functions; C library; style); **2 Cognition** (pointers; the C memory
model — object representation, alignment, effective types; storage — `static`, `malloc`/`free`,
lifetimes; more control — sequence points, `setjmp`, signals; error handling; generic programming
with `_Generic`); **3 Experience** (performance — `inline`, `restrict`; function-like macros; variadic
functions; type-generic macros; atomic access and memory consistency; threads with `<threads.h>`);
**4 Ambition**. C23 additions: `_BitInt(N)`, `<stdckdint.h>` checked arithmetic, `<stdbit.h>`,
`nullptr`, attributes, `constexpr`, `auto`.
K&R (2nd ed., ANSI C): tutorial, types/operators, control flow, functions and program structure,
pointers and arrays (pointer arithmetic, `char *` strings, pointer arrays, `argv`, function pointers,
complicated declarations), structures, input/output, the Unix system interface (file descriptors, a
storage allocator).

## Key ideas → pages
- Integer rules: promotions, `size_t` for sizes, unsigned wraps, signed overflow undefined —
  [[integer-representation-and-bits]], [[undefined-behavior]].
- The C memory model: objects, effective types, alignment, strict aliasing; `restrict` —
  [[pointers-and-memory]], [[undefined-behavior]].
- Storage durations (automatic/static/allocated/thread), lifetimes, and the malloc contract —
  [[memory-layout-stack-heap]], [[dynamic-memory-allocation]].
- Error handling in C (return codes, `errno`, cleanup with `goto`), `_Generic` for type-generic macros
  — [[error-handling-strategies]], [[function-pointers-and-generic-c]].
- K&R's storage allocator (ch. 8.7) is the simplest working free-list malloc — [[dynamic-memory-allocation]].

## What it adds
Modern C corrects what K&R-era teaching gets wrong today (implicit int, `gets`, ignoring UB) and is
the reference for C23; K&R remains the clearest exposition of pointers and arrays.

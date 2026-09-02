---
title: Function pointers, void*, and generic programming in C
type: concept
section: "2.3"
level: 200
tags: [function-pointers, void-pointer, generics, qsort, bsearch, callbacks, comparator, memcpy, _Generic, macros, vtable, dispatch, opaque-types]
sources: [stanford-cs107, modern-c-gustedt, csapp-15-213]
summary: C achieves reuse without templates by passing `void *` plus a byte size (memcpy-based generic swap/sort/search), by passing function pointers as callbacks/comparators (qsort, event loops), by hand-built vtables (structs of function pointers, how C programs do objects), and since C11 by `_Generic` type-switch macros — at the cost of losing type checking, which is exactly what generics and traits later restored.
---
# Function pointers, `void *`, and generic C

**In one sentence.** Generic code in C means "a pointer to bytes, a size, and a function pointer that
knows the real type" — powerful, error-prone, and the reason later languages grew generics.

## `void *` generics (CS107 "Into the void*")
- `void *` carries an address with no type; to touch the data you need `size`: a generic swap is
  `memcpy` through a temp buffer of `size` bytes; element i of a generic array is `(char *)base + i *
  size` (cast to `char *` for byte arithmetic).
- Library examples: `qsort(base, n, size, cmp)`, `bsearch`, `memcpy`, `memcmp`, `memset`.
- Costs: no type checking (passing `sizeof(int)` for a `double` array compiles), no inlining of the
  comparator (indirect call per comparison — `qsort` is slower than a type-specialized sort),
  clumsy syntax. Callers must be disciplined about `size` and the comparator's argument types
  (`int cmp(const void *a, const void *b)` — cast inside).

## Function pointers
- Declaration `int (*cmp)(const void *, const void *)`; a `typedef` makes it readable. Call as `cmp(a, b)`
  or `(*cmp)(a, b)`. Functions decay to pointers like arrays.
- Uses: **comparators** (`qsort`), **callbacks** (signal handlers, `atexit`, event loops, `pthread_create`
  with a `void *arg` closure substitute), **dispatch tables** (arrays of handlers indexed by opcode —
  interpreters), **plug-in interfaces**.
- Closures are simulated with an extra `void *context` argument — the missing environment
  ([[closures-and-environment-model]]).
- Struct-of-function-pointers = **vtable**: `struct shape_ops { double (*area)(void*); void
  (*destroy)(void*); }` is how the Linux kernel, GTK and SQLite do polymorphism; C++ virtual functions
  and Rust `dyn Trait` compile to the same layout ([[rust-traits-generics-lifetimes]]).

## `_Generic` and macros (Modern C level 2–3)
`#define cbrt(X) _Generic((X), float: cbrtf, long double: cbrtl, default: cbrt)(X)` — a compile-time type
switch giving overload-like behaviour (`<tgmath.h>`). Macros also provide type-generic containers by
token pasting (`DEFINE_VEC(int)`) — code generation without type safety; hygiene issues (double
evaluation, `do { } while (0)`).

## Opaque types
Hide the struct in the .c file and expose `typedef struct stack stack;` with functions — information
hiding and rep independence in C ([[data-abstraction]]); the `void *` version generalizes to any
element type.

## Pitfalls
- Wrong `size` or comparator type (comparing `int` bytes via `strcmp`).
- Pointer arithmetic on `void *` is a GNU extension; cast to `char *`.
- Function pointer to a function of another type is UB when called ([[undefined-behavior]]).

## Related
- [[pointers-and-memory]], [[higher-order-functions]] (the same idea with closures),
  [[type-systems]] (parametric polymorphism), [[rust-traits-generics-lifetimes]],
  [[data-abstraction]].

## Sources
CS107 lectures 8–10 and assignments 3–4; Modern C ch. 16–17; K&R 5.11.

---
title: Undefined behavior in C and C++
type: concept
section: "2.3"
level: 300
tags: [undefined-behavior, ub, signed-overflow, strict-aliasing, uninitialized, null-dereference, data-races, sequence-points, sanitizers, ubsan, asan, compiler-optimization, implementation-defined]
sources: [modern-c-gustedt, csapp-15-213, rust-book]
summary: Undefined behavior is a contract violation the compiler is allowed to assume never happens — so signed overflow, out-of-bounds access, null dereference, use-after-free, uninitialized reads, strict-aliasing violations, and data races don't "usually work", they license the optimizer to delete your checks; detect with sanitizers and warnings, and understand why Rust's safe subset forbids exactly this list.
---
# Undefined behavior

**In one sentence.** UB is not "the program crashes" — it is "the standard imposes no requirements",
and modern compilers exploit that assumption to optimize, so code with UB can pass tests and fail
after a compiler upgrade or `-O2`.

## The catalogue (most common in practice)
| UB | Typical symptom | Why compilers care |
|---|---|---|
| Signed integer overflow | loop never terminates; overflow check deleted | assume `x+1 > x` to simplify induction variables |
| Out-of-bounds array/pointer access | corrupts neighbours, security holes | bounds are not tracked at runtime |
| Null pointer dereference | segfault — or a later `if (p)` check removed | after `*p`, p is assumed non-null |
| Use after free / double free | heap corruption, silent | allocator internals |
| Reading uninitialized memory | "random" values, different per build | value assumed to be anything convenient |
| Strict aliasing violation | writes through one pointer invisible via another | type-based alias analysis |
| Shift by ≥ width / negative; division by zero; INT_MIN / −1 | traps or garbage | hardware differences |
| Modifying an object twice without a sequence point (`i = i++`) | either order | evaluation order freedom |
| Data race (unsynchronized concurrent access) | torn reads, stale values | memory model allows reordering ([[synchronization-primitives]]) |
| Calling a function through a wrong-type pointer; returning no value from non-void | ABI mismatch | |
| Infinite loop without side effects (C++) | loop deleted | forward-progress assumption |

Distinguish **implementation-defined** (documented choice: `char` signedness, `int` size) and
**unspecified** (one of several, not documented: argument evaluation order) from UB.

## Why "it works on my machine" is not evidence
The optimizer reasons from "no UB" backward: `if (x + 1 < x)` is dead code; `if (!p)` after `*p` is
dead code; a bounds check "cannot" fail. Behaviour changes with optimization level, compiler version,
inlining decisions, and target. Famous cases: Linux kernel null-check removal (CVE-2009-1897), GCC
deleting overflow checks in SSL code.

## Defences
- Compile with `-Wall -Wextra -Werror` and `-fsanitize=address,undefined` (ASan/UBSan) in tests; MSan
  for uninitialized reads; TSan for races; valgrind for older setups ([[debugging]]).
- `-fwrapv`/`-fno-strict-aliasing` change the dialect (documented, portable to the compilers that
  support them) but do not fix logic.
- Use `memcpy` for type punning; `unsigned` or checked arithmetic (`__builtin_*_overflow`, C23
  `<stdckdint.h>`) for overflow-prone code ([[integer-representation-and-bits]]).
- Fuzz with sanitizers on ([[fuzzing]]).
- Language-level: Rust's safe subset makes every row above a compile error or a panic; `unsafe` blocks
  reintroduce the obligation and should be small and documented ([[ownership-and-borrowing]]).

## Related
- [[integer-representation-and-bits]], [[pointers-and-memory]], [[memory-safety-and-buffer-overflows]],
  [[ownership-and-borrowing]], [[debugging]], [[compiler-optimizations]].

## Sources
Modern C (integers, effective types, sequence points); CSAPP 2.3, 3.10; CS110L lecture 2 (memory safety); Regehr/Lattner UB essays (not yet ingested).

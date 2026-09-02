---
title: Pointers, arrays, C strings, and the C memory model
type: concept
section: "2.3"
level: 200
tags: [pointers, addresses, dereference, pointer-arithmetic, arrays, array-decay, c-strings, null-terminator, struct-padding, alignment, strict-aliasing, restrict, const, void-pointer]
sources: [csapp-15-213, stanford-cs107, modern-c-gustedt, harvard-cs50]
summary: A pointer is an address plus a static type that determines what one step of arithmetic means; arrays decay to pointers to their first element (so sizeof and strlen differ), C strings end at a NUL byte, structs are laid out in declaration order with alignment padding, and the compiler assumes pointers of different types never alias — the facts behind most C bugs.
---
# Pointers, arrays, and the C memory model

**In one sentence.** `p` holds an address; `*p` reads the object there as type T; `p + 1` moves by
`sizeof(T)` bytes; everything else follows.

## Core rules
- Declaration reads right-to-left: `int *p` (pointer to int), `char **argv`, `int (*f)(int)` (pointer
  to function), `const char *s` (pointer to const char) vs `char *const s` (const pointer).
- **Arrays decay**: in expressions `a` becomes `&a[0]`; `a[i]` ≡ `*(a + i)`; passing an array to a
  function passes a pointer — `sizeof(a)` is the array size only in the declaring scope. Pass lengths
  explicitly.
- **C strings**: `char` arrays terminated by `'\0'`; `strlen` counts bytes before the NUL (O(n), no
  terminator ⇒ read past the buffer); `sizeof "hi"` is 3. `strcpy`/`strcat`/`gets` are unbounded —
  use `strncpy` with care (may not terminate), `snprintf`, or `strlcpy`. Literals are read-only.
- **Pointer arithmetic** is defined only within an object (or one past its end); comparing/subtracting
  pointers into different objects is undefined ([[undefined-behavior]]).
- `void *` is a typeless address: no arithmetic, no dereference; the currency of generic C
  ([[function-pointers-and-generic-c]]). `NULL`/`nullptr` (C23) is the "no object" value — always
  check before dereferencing; dereferencing NULL is UB (usually a segfault).
- **Structs**: fields in declaration order, each aligned to its natural alignment, total size padded
  to the largest alignment (`struct {char c; int i;}` is 8 bytes). Reorder fields largest-first to
  shrink; use `offsetof`; bit-fields for packed flags. Passing structs by value copies them.
- **Effective type / strict aliasing**: accessing an object through a pointer of an incompatible type
  is UB (compilers assume `int*` and `float*` don't alias) — use `memcpy` for type punning
  ([[undefined-behavior]]). `restrict` promises no aliasing for optimization.
- `const` correctness documents which side may write; casting it away is UB if the object is const.
- Multi-level: `int **` for arrays of pointers (argv), out-parameters (`f(&p)` to return a pointer).

## Mental model checklist
Where does it point (stack, heap, static, literal)? Who owns it (who frees, when)? How long is the
buffer (bytes vs elements)? Is it NUL-terminated? Is the pointee `const`? Is it aligned? Could two
pointers alias? ([[memory-layout-stack-heap]], [[dynamic-memory-allocation]])

## Pitfalls (CS107's greatest hits)
- Off-by-one on the terminator (`malloc(strlen(s))` needs `+1`).
- Returning the address of a local (dangling once the frame is popped).
- `sizeof(ptr)` (8) where `sizeof(array)` was intended.
- `char *p; scanf("%s", p);` — uninitialized pointer.
- Comparing strings with `==` (compares addresses) instead of `strcmp`.
- Mixing signed `int` indices with `size_t` sizes (wraparound loops — [[integer-representation-and-bits]]).

## Related
- [[memory-layout-stack-heap]], [[dynamic-memory-allocation]], [[undefined-behavior]],
  [[memory-safety-and-buffer-overflows]], [[ownership-and-borrowing]] (what Rust makes of these rules),
  [[function-pointers-and-generic-c]].

## Sources
CSAPP ch. 3.8–3.10; CS107 lectures 4–8; Modern C levels 1–2 (pointers, memory model); K&R ch. 5–6; CS50 week 4.

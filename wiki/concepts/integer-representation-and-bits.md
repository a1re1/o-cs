---
title: Integer representation — two's complement, overflow, unsigned/signed conversion, bit tricks
type: concept
section: "2.3"
level: 200
tags: [integers, twos-complement, overflow, wraparound, unsigned, signed, integer-promotion, bit-manipulation, shifts, masks, popcount, endianness, size_t, datalab]
sources: [csapp-15-213, stanford-cs107, modern-c-gustedt]
summary: Machine integers are fixed-width residues mod 2^w: two's complement makes the top bit worth −2^(w−1), unsigned arithmetic wraps, signed overflow is undefined in C, mixing signed and unsigned silently converts to unsigned (so -1 > 1u), and shifts/masks/popcount are the everyday bit tools — with the datalab-style tricks and the sanity checks that prevent the classic bugs.
---
# Integer representation and bit manipulation

**In one sentence.** A w-bit integer is a number mod 2^w; two's complement is the same bits
reinterpreted with the top bit negative, which is why addition hardware is shared and why −x = ~x + 1.

## Representations (CSAPP ch. 2)
- Unsigned: value = Σ bᵢ2ⁱ, range [0, 2^w − 1]. Two's complement: value = −b_{w−1}2^{w−1} + Σ bᵢ2ⁱ,
  range [−2^{w−1}, 2^{w−1} − 1]; asymmetric (INT_MIN has no positive counterpart; `-INT_MIN` overflows;
  `abs(INT_MIN)` is UB).
- Same bit patterns: casting between signed and unsigned keeps bits, changes interpretation:
  (unsigned)−1 = 0xFFFFFFFF = UINT_MAX.
- Sign extension when widening signed (copy the top bit); zero extension for unsigned; truncation keeps
  low bits (mod 2^k).
- Endianness: little-endian x86/ARM store the least significant byte first; matters for byte-level I/O
  and network formats (network order is big-endian — `htonl`).

## Arithmetic
- Unsigned add/mul wrap mod 2^w (defined). Signed overflow is **undefined behaviour** in C/C++ — the
  compiler may assume it never happens (`x + 1 > x` folded to true) ([[undefined-behavior]]); Rust
  panics in debug, wraps in release unless you use `wrapping_add`/`checked_add`/`saturating_add`;
  Java/Go wrap; Python has bignums.
- Overflow checks: for unsigned `a + b < a`; for signed use compiler builtins
  (`__builtin_add_overflow`) or C23 `<stdckdint.h>`. Never check `a + b < 0` after the fact.
- Multiplication by constants becomes shifts/adds; division by 2^k: `>>` is arithmetic for signed
  (floor, rounds toward −∞) but `/` rounds toward zero — they differ for negatives; compilers fix with
  a bias `(x + (1<<k) − 1) >> k`.
- **Implicit conversions**: in an expression mixing `int` and `unsigned`, the int converts to unsigned
  — so `-1 < 0u` is false and `for (size_t i = n - 1; i >= 0; i--)` never ends. Use `size_t` for sizes
  and indices *consistently*, or `ptrdiff_t`/`ssize_t` when negatives are possible. Integer promotion:
  `char`/`short` operands become `int` first (`(uint8_t)~x` surprises).

## Bit tricks worth memorizing
`x & (x − 1)` clears the lowest set bit (loop it to count bits; zero iff power of two);
`x & −x` isolates the lowest set bit; `x ^ y ^ y == x`; swap without temp; mask `(1u << k) − 1`;
set/clear/toggle bit k: `|= 1u<<k`, `&= ~(1u<<k)`, `^= 1u<<k`; `popcount`, `clz/ctz`
(`__builtin_popcount`, C23 `<stdbit.h>`); parity via xor-folding; branchless min/max and abs;
`(x >> 31)` as a sign mask (arithmetic shift). Floating-point bit hacks (fast inverse sqrt) rely on
[[floating-point]] layout.

## Pitfalls
- Shifting by ≥ width or a negative amount is UB; left-shifting a negative signed value is UB.
- `1 << 40` overflows `int` — write `1ULL << 40`.
- `char` signedness is implementation-defined; use `unsigned char` for bytes.
- Sizes: `int` is 32-bit on all mainstream 64-bit platforms; `long` is 64 on Linux, 32 on Windows;
  use `<stdint.h>` fixed widths.

## Related
- [[floating-point]], [[undefined-behavior]], [[pointers-and-memory]], [[modular-arithmetic]] (the
  math of wraparound), [[hash-tables]] (masks for power-of-two tables).

## Sources
CSAPP ch. 2.1–2.3 and datalab; CS107 lectures 3, 11; Modern C 5.7 (integers), C23 stdckdint/stdbit.

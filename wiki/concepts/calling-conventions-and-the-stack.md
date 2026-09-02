---
title: x86-64 calling conventions, stack frames, and reading assembly
type: concept
section: "2.3"
level: 300
tags: [x86-64, assembly, calling-convention, system-v-abi, stack-frame, return-address, callee-saved, caller-saved, registers, condition-codes, bomblab, disassembly, abi, alignment]
sources: [csapp-15-213, stanford-cs107]
summary: On x86-64 System V, the first six integer arguments travel in rdi, rsi, rdx, rcx, r8, r9, the return value in rax, `call` pushes the return address and `ret` pops it, rbx/rbp/r12–r15 are callee-saved, the stack must be 16-byte aligned at calls, and locals live at negative offsets from rsp/rbp — enough to read compiler output, debug crashes, and understand why buffer overflows redirect control.
---
# Calling conventions and the runtime stack

**In one sentence.** A function call is a protocol: where arguments go, who saves which registers, how
the return address and locals are laid out — and once you know the protocol you can read any
disassembly and see what a memory bug will overwrite.

## The x86-64 System V convention (Linux/macOS; Windows differs)
- **Arguments**: integers/pointers in `%rdi, %rsi, %rdx, %rcx, %r8, %r9`; floats in `%xmm0–7`;
  extra arguments pushed on the stack (right to left). Return in `%rax` (`%rdx:%rax` for 128-bit,
  `%xmm0` for floats); large structs via a hidden pointer.
- **Caller-saved** (scratch): `rax, rcx, rdx, rsi, rdi, r8–r11` — a callee may clobber them.
  **Callee-saved**: `rbx, rbp, r12–r15` — restored before `ret`.
- `call f` pushes the return address and jumps; `ret` pops into `%rip`. `%rsp` points to the top;
  `%rbp` is an optional frame pointer (omitted at `-O2`, restored with `-fno-omit-frame-pointer` for
  profilers/debuggers).
- **Alignment**: `%rsp` ≡ 0 (mod 16) just before `call`, so on entry it is 8 mod 16.
- **Red zone**: leaf functions may use 128 bytes below `%rsp` without adjusting it.

## A frame, top (low addresses) to bottom
```
[locals / spill slots / outgoing args]  ← %rsp
[saved callee registers]
[saved %rbp]                            ← %rbp (if used)
[return address]                        ← pushed by call
[caller's stack args, if any]
```
A local buffer `char buf[16]` sits *below* the saved registers and return address; writing past its
end walks *up* into them — the mechanism of the stack-smashing attack
([[memory-safety-and-buffer-overflows]]).

## Reading assembly (AT&T syntax, what gcc emits)
- `movq src, dst`; suffixes b/w/l/q = 1/2/4/8 bytes; `%eax` writes zero-extend to `%rax`.
- Addressing `D(B, I, S)` = `Mem[D + B + I·S]` — `movl (%rdi,%rsi,4), %eax` is `a[i]` for `int a[]`.
  `leaq` computes an address without loading (used for arithmetic: `leaq (%rdi,%rdi,2), %rax` = 3x).
- Control flow: `cmp`/`test` set condition codes (CF, ZF, SF, OF); `j{e,ne,l,ge,b,a}` — signed
  (`l/g`) vs unsigned (`b/a`) comparisons reveal the source types; `cmov` for branchless selects;
  `jmp *table(,%rax,8)` is a `switch` jump table; loops become `do-while` shapes.
- Arrays/structs: constant offsets are field offsets; `imul` by `sizeof` for 2-D indexing.
- Tools: `objdump -d`, `gdb` (`disas`, `x/8gx $rsp`, `info registers`), Compiler Explorer.
  Bomblab is the exercise: infer the C from the assembly.

## Why it matters
- Debugging crashes and core dumps (which frame, which register held the bad pointer).
- Performance: argument passing is free, but spills, stack traffic, and unpredictable branches are
  visible ([[compiler-optimizations]], [[caches-and-memory-hierarchy]]).
- Interop/FFI: matching the ABI is what makes C-callable libraries and `extern "C"` work
  ([[linking-and-loading]]).
- Security: return-oriented programming chains existing `ret`-ending gadgets; defences (stack
  canaries, NX, ASLR, shadow stacks, CET) all reference this layout.

## Related
- [[memory-layout-stack-heap]], [[memory-safety-and-buffer-overflows]], [[pointers-and-memory]],
  [[linking-and-loading]], [[integer-representation-and-bits]], [[isa-and-assembly]].

## Sources
CSAPP ch. 3.4–3.7, 3.10; CS107 lectures 12–15; System V AMD64 ABI.

---
title: Instruction set architecture — RISC-V, x86, ARM; the ISA as the hardware/software contract
type: concept
section: "4.1"
level: 200
tags: [isa, instruction-set, risc-v, x86, arm, risc, cisc, load-store, registers, addressing-modes, instruction-encoding, immediates, branches, stored-program, von-neumann, harvard, endianness, microcode, assembler, linker]
sources: [patterson-hennessy-cod, nand2tetris, architecture-seminal-papers, csapp-15-213]
summary: The ISA is the contract between compilers and hardware — registers, memory model, instruction formats and semantics — and RISC (load/store, fixed-width encodings, many registers, simple instructions that pipeline well: RISC-V, ARM, MIPS) versus CISC (variable-length, memory operands, microcoded complex ops: x86) is a story about what compilers actually emit; RISC-V's base ISA fits on a page (R/I/S/B/U/J formats, 32 registers, lw/sw, add/sub/and/or/slt, beq/bne/blt, jal/jalr, lui/auipc) plus extensions (M, A, F/D, C, V), and translating a program means compiler → assembler → linker → loader.
---
# Instruction set architecture

**In one sentence.** Everything above the ISA is software's problem, everything below is
hardware's; the ISA's job is to be easy to compile to and easy to pipeline (Patterson & Ditzel).

## The stored-program model (von Neumann 1945)
Instructions are data in memory; a program counter fetches, decodes, executes, repeats. Registers
are the fast, few, named storage; memory is large, slow, byte-addressed (little-endian on x86,
RISC-V, ARM). Harvard variants split instruction/data memories (Nand2Tetris's Hack; caches are
Harvard at L1, unified below). The fetch–execute bottleneck is what caches, pipelines and
parallelism attack ([[caches-and-memory-hierarchy]], [[pipelining-and-hazards]]).

## RISC-V RV32I/RV64I in a page (COD ch. 2)
- 32 registers x0–x31 (x0 = 0; ABI names: ra, sp, gp, tp, t0–6, s0–11/fp, a0–7), PC.
- Formats: **R** `add rd, rs1, rs2`; **I** `addi rd, rs1, imm12`, loads `lw rd, off(rs1)`,
  `jalr`; **S** stores `sw rs2, off(rs1)`; **B** branches `beq/bne/blt/bge(u) rs1, rs2, off13`;
  **U** `lui`, `auipc` (20-bit upper immediates); **J** `jal rd, off21`. All 32-bit, opcode in
  the low 7 bits, register fields in fixed positions (fast decode — a design principle).
- Arithmetic/logical: add, sub, and, or, xor, sll/srl/sra, slt/sltu; no flags register —
  comparisons produce values or branch directly. Multiply/divide in the **M** extension; atomics
  (lr/sc, amo*) in **A**; floats in **F/D**; compressed 16-bit encodings in **C**; vectors in **V**.
- Loads/stores are the only memory instructions (**load/store architecture**); addressing mode
  = base + 12-bit displacement (build others with `lui`/`auipc`/`add`).
- Procedures: `jal ra, f` … `jalr x0, 0(ra)`; args in a0–a7, return in a0–a1; callee-saved s*,
  caller-saved t*/a*; stack grows down; frame pointer optional
  ([[calling-conventions-and-the-stack]]).
- Pseudo-instructions (`li`, `mv`, `j`, `ret`, `nop`, `bgt`) are assembler sugar.

## x86-64 and ARM in contrast
x86: variable-length (1–15 bytes), two-operand destructive ops, memory operands in most
instructions (`add rax, [rbx+8*rcx+16]`), condition flags, ~1000+ instructions, decoded into
RISC-like micro-ops by the front end — CISC outside, RISC inside; the ISA persists for
compatibility. ARM (AArch64): fixed 32-bit, load/store, 31 registers, condition flags with
conditional select rather than predicated everything; SVE vectors. RISC-V: open, modular, no
licensing — the "Linux of ISAs" (Hennessy–Patterson).

## From source to running program (COD 2.12)
Compiler emits assembly → **assembler** produces an object file (machine code, symbol table,
relocation entries; two passes to resolve forward labels — Nand2Tetris project 6) → **linker**
merges objects and libraries, resolves symbols, patches relocations ([[linking-and-loading]]) →
**loader** maps the executable into memory, sets up stack/args, jumps to `_start`
([[processes-and-threads]]). Dynamic linking defers library resolution to load/run time.

## Design principles (COD)
Simplicity favors regularity; smaller is faster (few registers, short immediates); make the
common case fast (immediates, base+offset); good design demands good compromises (fixed-width
encodings vs immediate size).

## Pitfalls
- Reading the ISA as "what the CPU does": modern cores reorder, speculate, fuse and split
  instructions; the ISA is the *observable* semantics only ([[pipelining-and-hazards]]).
- Signed vs unsigned comparisons/branches and immediates' sign extension.
- Alignment and endianness when reinterpreting memory ([[integer-representation-and-bits]]).

## Related
- [[calling-conventions-and-the-stack]], [[pipelining-and-hazards]], [[digital-logic-and-the-alu]],
  [[linking-and-loading]], [[caches-and-memory-hierarchy]], [[integer-representation-and-bits]],
  [[floating-point]].

## Sources
COD ch. 2; Nand2Tetris projects 4–6; Patterson & Ditzel 1980; CSAPP ch. 3.

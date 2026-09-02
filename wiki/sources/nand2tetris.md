---
title: The Elements of Computing Systems / Nand to Tetris (Nisan & Schocken)
type: source
section: "4.1"
level: 200
tags: [nand2tetris, boolean-logic, gates, alu, memory, flip-flops, hack-computer, machine-language, assembler, virtual-machine, stack-machine, compiler, jack-language, operating-system, first-principles]
sources: []
authors: [Noam Nisan, Shimon Schocken]
year: 2021
institution: Hebrew University / IDC Herzliya
url: https://www.nand2tetris.org/
license: open-course
format: html
summary: Twelve projects that build a working computer from NAND gates up — Part I hardware (Boolean logic gates in HDL, Boolean arithmetic and the ALU, memory from flip-flops to RAM, the Hack machine language, the CPU and computer architecture, an assembler) and Part II software (a stack-based VM translator in two parts, the Jack high-level language, a two-part compiler for it — parsing and code generation — and a minimal operating system) — the fastest way to see every layer of abstraction as something you made.
---
# Nand to Tetris

## What it is
**Part I: Hardware** — Project 1 Boolean logic (Nand → Not, And, Or, Xor, Mux, DMux, 16-bit and
multi-way variants in a simple HDL with a hardware simulator); 2 Boolean arithmetic (half/full
adders, 16-bit adder/incrementer, the Hack ALU computing 18 functions from 6 control bits — an
elegant design where the output flags feed conditional jumps); 3 memory (DFF as primitive → Bit →
Register → RAM8..RAM16K, program counter; sequential logic and the clock); 4 machine language
(Hack: A-instructions `@value` and C-instructions `dest=comp;jump`, memory-mapped screen and
keyboard; write Mult and Fill in assembly); 5 computer architecture (Memory, CPU, Computer chips
wired from the earlier parts — a von Neumann machine with separate instruction ROM, i.e.
Harvard); 6 assembler (two-pass, symbols, labels, variables). **Part II: Software** — 7–8 VM I/II
(stack arithmetic, memory segments — local/argument/this/that/constant/static/pointer/temp —
then program control: branching, function call/return with the calling convention implemented as
stack frames); 9 high-level language (write a game in Jack, an object-based Java-like language);
10–11 compiler I/II (tokenizer, recursive-descent parser producing XML, then symbol tables and
VM code generation for expressions, statements, arrays, objects, methods); 12 operating system
(Math, String, Array, Output, Screen, Keyboard, Memory with a heap allocator, Sys — in Jack).

## Key ideas → pages
- Gates → ALU → registers → CPU: [[digital-logic-and-the-alu]], [[isa-and-assembly]].
- Assembler, VM translator, compiler, OS as the software stack of abstractions —
  [[compilers-overview]] (§4.3), [[calling-conventions-and-the-stack]] (function call/return in
  Project 8 is the same protocol as x86-64's).
- A two-tier compilation (Jack → VM → Hack) foreshadows JVM/CLR and LLVM IR.

## What it adds
The lab that makes [[patterson-hennessy-cod]] concrete; every abstraction layer in §4 is built by
hand once, which is the best inoculation against magic.

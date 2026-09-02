---
title: Digital logic — gates, combinational and sequential circuits, the ALU, registers, memory, and the clock
type: concept
section: "4.1"
level: 200
tags: [digital-logic, gates, nand, boolean-algebra, combinational-logic, multiplexer, decoder, adder, alu, sequential-logic, flip-flop, latch, register, clock, finite-state-machine, ram, hdl, verilog, timing, setup-hold, critical-path]
sources: [nand2tetris, patterson-hennessy-cod]
summary: NAND is functionally complete, so every gate, then multiplexers/decoders/adders and a full ALU are combinational circuits (outputs a pure function of inputs, propagation delay sets the clock); a clocked D flip-flop adds state, giving registers, counters, RAM (addressed register arrays via decoders and muxes), and finite-state machines, and the clock period must exceed the critical path plus setup time — which is why pipelining shortens stages and why the CPU is "just" a big FSM around an ALU and a register file.
---
# Digital logic and the ALU

**In one sentence.** Combinational logic computes, a flip-flop remembers, the clock sequences —
and a CPU is a datapath of the first two driven by a controller made of all three.

## Combinational logic (Nand2Tetris 1–2, COD App. A)
- Boolean algebra: AND/OR/NOT, De Morgan, sum-of-products; any truth table is a circuit
  ([[propositional-logic]]). **NAND** alone builds everything (`Not(a) = Nand(a,a)`).
- Building blocks: Mux (select), DMux, Decoder (n → 2ⁿ one-hot), encoder, comparator, shifter;
  bus-wide versions (And16, Mux16), multi-way (Mux8Way16).
- Arithmetic: half adder (Xor, And), full adder, ripple-carry adder (delay O(n)), carry-lookahead
  (O(log n)); two's complement means subtraction = add the complement plus 1
  ([[integer-representation-and-bits]]); multipliers (array, Booth, Wallace tree) and dividers;
  floating-point units ([[floating-point]]).
- **The Hack ALU**: 6 control bits (zx, nx, zy, ny, f, no) select among 18 functions of x, y (0,
  1, −1, x, y, !x, x+1, x−1, x+y, x−y, x&y, x|y, …) and emit zr/ng flags — the ALU as a
  programmable function of a few muxes. Real ALUs add shifts, comparisons, flags.
- Delay: each gate has propagation delay; the **critical path** through combinational logic
  bounds the clock; glitches before settling are ignored by clocking.

## Sequential logic (Nand2Tetris 3)
- SR latch (cross-coupled NORs) → gated D latch → edge-triggered **D flip-flop** (master–slave):
  Q takes D at the clock edge and holds it. Setup and hold times must be respected.
- 1-bit register = DFF + Mux(load); 16-bit Register; **RAM**: a register array with a decoder to
  select and a mux to read (RAM8 → RAM64 → … RAM16K, recursively); program counter (inc, load,
  reset). Real SRAM uses 6 transistors per bit; DRAM one transistor + capacitor with refresh
  ([[caches-and-memory-hierarchy]]).
- **Finite-state machines**: state register + next-state and output logic (Moore vs Mealy);
  control units, protocol handlers, and the multi-cycle CPU controller are FSMs
  ([[finite-automata-and-regular-languages]]).
- Timing: clock period T ≥ t_clk→q + t_logic(critical) + t_setup; frequency is set by the
  slowest stage → pipeline registers split long paths ([[pipelining-and-hazards]]). Metastability
  when inputs change near edges; synchronizers for asynchronous inputs.

## From logic to a computer (Nand2Tetris 5)
Datapath: instruction register/ROM, register file, ALU, data memory, PC, and muxes; control
decodes instruction bits into mux selects, register loads and jump conditions — a single-cycle
machine executes one instruction per clock; multi-cycle and pipelined designs reuse the same
parts ([[isa-and-assembly]]).

## Tools and practice
HDLs (Verilog/SystemVerilog, VHDL, Chisel) describe circuits; simulate, then synthesize to
FPGAs or ASIC standard cells; timing analysis reports the critical path; the Hack HDL and
simulator are the pedagogical version.

## Pitfalls
- Combinational loops (feedback without a register); missing default cases in HDL → latches.
- Treating HDL as software: statements are concurrent hardware, not sequential steps.
- Ignoring setup/hold and clock domain crossings.

## Related
- [[isa-and-assembly]], [[pipelining-and-hazards]], [[integer-representation-and-bits]], [[floating-point]],
  [[propositional-logic]], [[finite-automata-and-regular-languages]], [[caches-and-memory-hierarchy]].

## Sources
Nand2Tetris projects 1–5; COD appendix A and ch. 3–4; Harris & Harris ch. 1–5.

---
title: Microcontrollers and embedded programming — memory-mapped peripherals, GPIO/timers/ADC, interrupts and ISR design, buses (UART/SPI/I²C), RTOS vs bare metal, low power, debugging, and FPGA basics
type: concept
section: "4.9"
level: 300
tags: [microcontrollers, mcu, arm-cortex-m, risc-v, avr, esp32, memory-mapped-io, peripherals, gpio, timers, pwm, adc, dac, interrupts, nvic, isr, volatile, interrupt-latency, uart, spi, i2c, can, dma, watchdog, bootloader, firmware, rtos, freertos, zephyr, bare-metal, superloop, low-power, sleep-modes, datasheets, jtag, swd, logic-analyzer, hardware-abstraction-layer, fixed-point, fpga, verilog, hdl, iot, ota-updates]
sources: [embedded-systems-texts-and-courses, ostep]
summary: A microcontroller is a CPU (ARM Cortex-M, RISC-V, AVR, Xtensa) with flash, a little SRAM and peripherals on one chip, programmed at the register level — peripherals are memory-mapped registers (read the datasheet: base address, bit fields, read-modify-write, `volatile`), digital I/O through GPIO, timers for periodic events and PWM, ADC/DAC for analog, UART/SPI/I²C/CAN buses for other chips, DMA for bulk moves — and its software is structured around interrupts: an ISR is a concurrent thread that must be short, must not block, and must share data with the main loop through volatile flags, ring buffers or atomics, with latency dominated by the longest interrupts-disabled region; programs are either a superloop with interrupts (bare metal) or an RTOS (FreeRTOS, Zephyr) with priority-scheduled tasks, semaphores and queues once concurrency and timing demands grow; power is managed with sleep modes and event-driven wakeups, robustness with watchdogs and brown-out detection, deployment with bootloaders and signed OTA updates, and debugging with SWD/JTAG, logic analyzers and printf over UART — while FPGAs (Verilog/VHDL synthesized to LUTs and flip-flops) cover the cases where software timing is not deterministic enough.
---
# Microcontrollers and embedded programming

**In one sentence.** No OS, no MMU, kilobytes of RAM, and the datasheet is the API: you
write to the bits that make the world move, and the interrupt is your only concurrency.

## The hardware (Lee & Seshia ch. 8–10; Valvano)
**MCU** = core + flash (code, 32 KB–2 MB) + SRAM (8–512 KB) + peripherals + clock tree; ARM
Cortex-M0/M4/M7 (Thumb-2, NVIC, SysTick, optional FPU/DSP), RISC-V (ESP32-C, CH32), AVR
(Arduino), Xtensa (ESP32 with Wi-Fi/BLE). Boards: dev kits, Arduino, STM32 Nucleo, Raspberry
Pi Pico (RP2040 with PIO state machines). Compare: MPU/SoC with MMU running Linux (Raspberry
Pi) vs MCU; DSPs; FPGAs. **Memory-mapped peripherals**: each peripheral block has registers at
fixed addresses (`*(volatile uint32_t*)0x40020000`, or vendor headers/CMSIS/HAL); set/clear
via read-modify-write (or dedicated set/clear registers to avoid races); **`volatile`** so the
compiler re-reads ([[undefined-behavior]], [[compiler-optimizations]]); memory barriers on
Cortex-M7 with write buffers. Peripherals: **GPIO** (mode, pull-ups, speed, alternate function),
**timers** (prescaler/period, capture/compare, **PWM** for motors/LEDs, input capture for
encoders), **ADC** (resolution, sampling time, oversampling, Nyquist — sample rate vs
bandwidth), DAC, **UART** (async serial, baud, framing — the debug console), **SPI** (fast,
full-duplex, chip selects), **I²C** (two wires, addresses, clock stretching, slow), **CAN**
(automotive, arbitration), USB, **DMA** (peripheral↔memory without the CPU; circular buffers
for ADC/UART streams), RTC, watchdog, crypto engines.

## Interrupts (Lee & Seshia 10.2; Valvano)
Peripheral event → NVIC → context save → **ISR** → return. Design rules: keep ISRs short
(record the event, defer work); never block or call non-reentrant code (`printf`, `malloc`);
share data with the main loop via `volatile` flags, single-producer/single-consumer **ring
buffers**, or atomics; clear the interrupt flag; prioritized and nested interrupts (NVIC
priority grouping); **interrupt latency** = hardware entry + longest critical section (keep
`__disable_irq()` regions tiny). "Sequential software in a concurrent world": an ISR can run
between any two instructions — the same race conditions as threads, with fewer tools
([[synchronization-primitives]], [[processes-and-threads]]). Timing via SysTick or a hardware
timer, not busy loops; measure with a GPIO toggle and an oscilloscope.

## Software structure
- **Bare metal superloop**: init; `while(1) { poll flags; run state machines; sleep; }` with
  ISRs feeding it — deterministic, simple, fine for most products; cooperative schedulers and
  timer wheels; event queues. **State machines** are the natural design unit
  ([[cyber-physical-systems-and-models-of-computation]]).
- **RTOS** (FreeRTOS, Zephyr, ThreadX, RTEMS, NuttX, QNX/VxWorks commercially): preemptive
  priority scheduling ([[real-time-scheduling]]), tasks with their own stacks, semaphores/
  mutexes (with priority inheritance), queues, software timers, tickless idle; memory
  protection with an MPU; Zephyr adds a device-tree-driven driver model, networking and
  Bluetooth. Choose an RTOS when multiple independent timing requirements, blocking I/O, or
  networking stacks appear.
- Layering (White): hardware abstraction layer → drivers → middleware → application; keep
  board-specific code behind interfaces for testing on a host (unit tests with mocks, HIL rigs).
- Language and toolchain: C (MISRA in safety domains), C++ (no exceptions/RTTI, static
  allocation), Rust (embedded-hal, `no_std`, RTIC — ownership solves ISR data sharing —
  [[ownership-and-borrowing]]), MicroPython/Arduino for prototyping; cross compilers (arm-none-
  eabi-gcc), linker scripts (flash/RAM regions, vector table, `.data` copy, `.bss` zero),
  startup code, `-Os`, no dynamic allocation (or pools), **fixed-point** math on cores without
  FPUs, lookup tables ([[numerical-computing-and-floating-point]]).

## Power, robustness, deployment
**Low power**: run fast then sleep; sleep modes (sleep/stop/standby with wake sources); clock
gating; event-driven design; battery budget in μA-hours; radio duty cycling (BLE, LoRa,
Zigbee/Thread for IoT). **Robustness**: watchdog timer (kick only when all tasks are healthy),
brown-out reset, ECC/CRC on flash, defensive state machines, EMI. **Bootloaders and OTA**:
dual-bank images, signed and versioned firmware, rollback on failed boot, secure boot with
hardware root of trust ([[security-principles]], [[cryptography-basics]]). **IoT stacks**:
MQTT/CoAP over Wi-Fi/cellular/LoRaWAN, TLS on small devices (mbedTLS), device provisioning.

## Debugging and measurement
SWD/JTAG probes (ST-Link, J-Link, CMSIS-DAP) with gdb/OpenOCD or vendor IDEs: breakpoints,
watchpoints, live variables, trace (ITM/ETM); UART printf (with care for timing); logic
analyzers and oscilloscopes for buses and timing; `-fstack-usage`, map files, and stack
painting for memory; hard-fault handlers that dump registers; simulators (Renode, QEMU). Read
the errata sheet ([[debugging]]).

## FPGA basics (Lee & Seshia 8.4)
Programmable logic: LUTs, flip-flops, block RAM, DSP slices, routed by a bitstream; described in
Verilog/VHDL (or SpinalHDL/Chisel/Amaranth), simulated, synthesized, placed and routed with
timing closure; HLS from C; soft cores (RISC-V) and SoC FPGAs (Zynq); used for deterministic
timing, high-rate signal processing, protocol bridging, accelerators
([[digital-logic-and-the-alu]]).

## Pitfalls
- Forgetting `volatile`/barriers; read-modify-write races on shared registers.
- Long ISRs; `printf`/`malloc` in ISRs; unbounded interrupt-disabled sections.
- Blocking delays instead of timers; busy-waiting on a battery.
- Stack overflows with no MPU (silent corruption); heap fragmentation.
- No watchdog, no brown-out detection, unsigned OTA, secrets in flash.

## Related
- [[real-time-scheduling]], [[cyber-physical-systems-and-models-of-computation]],
  [[io-and-device-drivers]], [[isa-and-assembly]], [[digital-logic-and-the-alu]],
  [[synchronization-primitives]], [[linking-and-loading]], [[undefined-behavior]],
  [[ownership-and-borrowing]], [[security-principles]].

## Sources
Lee & Seshia ch. 8–11; Valvano EE319K/EE445L; White, Making Embedded Systems (2nd ed.); ARM Cortex-M documentation; FreeRTOS and Zephyr docs; Embedded Rust book.

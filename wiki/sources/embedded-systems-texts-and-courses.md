---
title: Embedded systems — Lee & Seshia Introduction to Embedded Systems: A Cyber-Physical Systems Approach (free), Berkeley EECS149, Valvano's UT Austin EE319K/EE445L, MIT 6.08, White's Making Embedded Systems, Liu's Real-Time Systems, and Liu & Layland (1973) / Lee "Cyber-Physical Systems: Design Challenges" (2008)
type: source
section: "4.9"
level: 300
tags: [embedded-systems, lee-seshia, cyber-physical-systems, eecs149, valvano, ee319k, ee445l, 6-08, making-embedded-systems, elecia-white, real-time-systems, jane-liu, liu-layland, rate-monotonic, cps-design-challenges]
sources: []
authors: [Edward Lee, Sanjit Seshia, Jonathan Valvano, Elecia White, Jane W. S. Liu, C. L. Liu, James Layland]
year: 2017
institution: UC Berkeley / UT Austin / MIT
url: https://ptolemy.berkeley.edu/books/leeseshia/
license: mixed (Lee & Seshia free CC; Valvano course materials open)
format: pdf
summary: Lee & Seshia's book (2nd ed., free, the EECS149 text) treats embedded systems as cyber-physical systems whose correctness includes timing — modeling dynamics (continuous-time, discrete, hybrid systems, state machines, composition, concurrent models of computation — synchronous-reactive, dataflow, timed), design (sensors and actuators, embedded processors, memory architectures, input/output and interrupts, multitasking and scheduling — RM/EDF, priority inversion), and analysis (invariants and temporal logic, equivalence and refinement, reachability and model checking, quantitative analysis — WCET, security); Valvano's EE319K/EE445L teach bare-metal ARM Cortex-M programming (registers, GPIO, timers, ADC, interrupts, UART/SPI/I²C, RTOS design) with labs; MIT 6.08 builds IoT devices with ESP32 and web backends; White's Making Embedded Systems is the practitioner's guide (architecture diagrams, datasheets, debugging, power, product lifecycle); Liu's Real-Time Systems is the scheduling-theory reference; Liu & Layland proved rate-monotonic's utilization bound and EDF's optimality; and Lee's 2008 paper argues that abstractions that discard time make CPS design unsound.
---
# Embedded systems texts and courses

## What they are
- **Lee & Seshia**: I modeling dynamic behaviors — continuous dynamics, discrete dynamics
  (finite-state machines, extended/nondeterministic), hybrid systems (timed automata,
  modal models), composition of state machines (synchronous vs asynchronous, hierarchy),
  concurrent models of computation (structure of models, synchronous-reactive, dataflow —
  SDF/DDF/Kahn networks, timed — discrete-event, continuous); II design of embedded
  systems — sensors and actuators (models, common sensors, actuators, noise/bias/quantization),
  embedded processors (microcontrollers, DSPs, GPUs, FPGAs, parallelism), memory architectures
  (types, hierarchy, models — stack, heap, memory protection), input and output (GPIO, buses,
  ADC/DAC, sequential software in a concurrent world — interrupts, the fact that an ISR is a
  concurrent thread), multitasking (imperative programs, threads, processes, mutual exclusion),
  scheduling (basics, rate-monotonic, EDF, scheduling with precedence/mutual exclusion,
  priority inversion and inheritance, multiprocessor); III analysis and verification —
  invariants and temporal logic (LTL), equivalence and refinement (trace containment,
  simulation, bisimulation), reachability analysis and model checking, quantitative analysis
  (execution time — WCET, loop bounds, caches), security and privacy (basic crypto, protocols,
  side channels, sensor security); appendices on sets/functions and complexity/computability.
- **EECS149/249A** (Berkeley): the book plus labs on a robot/microcontroller (interrupts,
  state machines, sensors, PID, RTOS, verification with model checking).
- **Valvano EE319K / EE445L** (UT Austin, open): ARM Cortex-M (TM4C/MSP432) — assembly and C
  at the register level, GPIO, interrupts (NVIC), SysTick and timers, ADC/DAC, UART/SPI/I²C,
  DMA, LCDs, low-power design, real-time OS (thread scheduler, semaphores, priority) built from
  scratch; Valvano's texts *Embedded Systems: Introduction to ARM Cortex-M* and *Real-Time
  Interfacing*.
- **MIT 6.08** (Interconnected Embedded Systems): ESP32 + sensors + HTTP servers + Python
  backends — the IoT end-to-end arc.
- **White, Making Embedded Systems** (2nd ed. 2024): architecture (block diagrams, layering,
  hardware/software interfaces), datasheets, inputs/outputs/timers, task management and
  RTOS choice, communication, updating code (bootloaders), debugging (JTAG, logic analyzers),
  power management, doing more with less (memory, speed), math on small processors, product
  lifecycle and manufacturing.
- **Liu, Real-Time Systems** (2000): hard vs soft real time, reference model (jobs, tasks,
  release times, deadlines), clock-driven, priority-driven (RM, DM, EDF, LST), resource access
  (priority ceiling), multiprocessor and distributed scheduling, aperiodic servers, real-time
  communication.
- **Liu & Layland, "Scheduling Algorithms for Multiprogramming in a Hard-Real-Time
  Environment" (1973)**: fixed-priority rate-monotonic is optimal among fixed-priority
  schemes; sufficient utilization bound n(2^{1/n} − 1) → ln 2 ≈ 0.693; EDF schedules any set
  with utilization ≤ 1. **Lee, "Cyber-Physical Systems: Design Challenges" (2008)**: computing
  abstractions (threads, ISAs, languages) abstract away time; CPS needs timing-deterministic
  abstractions (PRET machines, synchronous languages, time-triggered architecture).

## Key ideas → pages
[[real-time-scheduling]], [[microcontrollers-and-embedded-programming]],
[[cyber-physical-systems-and-models-of-computation]], [[cpu-scheduling]], [[model-checking]].

## What they add
Lee & Seshia give embedded systems a theory (models of computation, timing as semantics);
Valvano and White give the practice; Liu & Layland is the one theorem every RTOS relies on.

---
title: Cyber-physical systems and models of computation — modeling continuous and discrete dynamics, state machines and their composition, synchronous-reactive and dataflow models, hybrid systems, and verifying timed behaviour
type: concept
section: "4.9"
level: 400
tags: [cyber-physical-systems, cps, models-of-computation, continuous-dynamics, differential-equations, discrete-dynamics, finite-state-machines, extended-state-machines, nondeterminism, composition, synchronous-composition, asynchronous-composition, hierarchical-state-machines, statecharts, synchronous-reactive, esterel, lustre, scade, dataflow, synchronous-dataflow, kahn-process-networks, discrete-event, timed-automata, hybrid-systems, hybrid-automata, control-loops, pid, sensors-actuators, sampling, quantization, timing-determinism, pret, logical-execution-time, invariants, temporal-logic, ltl, reachability, model-checking, wcet, simulation, refinement]
sources: [embedded-systems-texts-and-courses]
summary: Lee & Seshia's thesis is that an embedded system's semantics include physical time and continuous dynamics, so design starts from models — ordinary differential equations for the plant, finite (and extended, nondeterministic) state machines for discrete control, and hybrid automata that combine both with guards, resets and invariants — composed under an explicit model of computation: synchronous composition (all machines step together, as in synchronous-reactive languages Esterel/Lustre/SCADE where a program is a set of equations over streams evaluated each tick), asynchronous interleaving, hierarchical state machines (Statecharts), dataflow (synchronous dataflow with static schedules and bounded buffers, Kahn process networks with deterministic streams), and discrete-event/timed models; sensing (sampling, quantization, noise, bias) and actuation close feedback loops (PID) whose stability depends on timing; and the payoff of modeling is analysis — invariants and temporal logic (LTL) specifications, equivalence/refinement (simulation, bisimulation), reachability and model checking, WCET — plus the argument (Lee 2008) that conventional computing abstractions discard time and CPS needs timing-deterministic ones (PRET, logical execution time).
---
# Cyber-physical systems and models of computation

**In one sentence.** When software controls a physical process, "what does the program
compute" is not enough — "when" is part of the answer, so model the whole loop and pick a
semantics in which time and concurrency are explicit.

## Modeling dynamics (Lee & Seshia ch. 2–4)
**Continuous**: the plant as ODEs (ẋ = f(x, u), Newton's laws, motors, thermal); actor
models with signals as functions of time; integrators; feedback control — proportional/
integral/derivative (**PID**) controllers, stability, gain and phase margins
([[matrices-and-linear-maps]], [[floating-point]] for simulation).
**Discrete**: **finite-state machines** — states, inputs, outputs, guards, reactions; Moore
vs Mealy; **extended** state machines with variables (the practical form: a `switch` in an
ISR loop — [[microcontrollers-and-embedded-programming]]); nondeterminism (abstraction of
unknown environment or unmodeled choice) vs determinism; behaviours as traces; FSMs as
[[finite-automata-and-regular-languages]] with outputs. **Hybrid systems**: hybrid automata —
modes with continuous dynamics inside, guards and resets on transitions, mode invariants
(bouncing ball, thermostat, gear shifting, timed automata as the special case with clocks);
Zeno behaviour; simulation with event detection (Simulink, Modelica, Ptolemy II).

## Composition and models of computation (ch. 5–6)
Concurrent components need a semantics for how they interact — the **model of computation**:
- **Synchronous composition**: all machines react simultaneously in lock step; feedback
  requires fixed-point semantics (constructiveness); **synchronous-reactive** languages
  (Esterel — imperative with signals; Lustre/SCADE — dataflow equations over streams; used
  in Airbus flight software) give deterministic concurrency and compile to sequential code.
- **Asynchronous composition**: interleaving semantics (as in threads, [[processes-and-threads]]);
  nondeterminism explodes the state space — the argument in Lee's "The Problem with Threads".
- **Hierarchical FSMs / Statecharts** (Harel): nested states, history, orthogonal regions —
  UML state machines, SCXML.
- **Dataflow**: actors fire when tokens are available; **synchronous dataflow (SDF)** with
  fixed token rates has statically computable schedules and bounded buffers (signal
  processing pipelines, GNU Radio, StreamIt); dynamic dataflow; **Kahn process networks**
  (blocking reads → deterministic streams regardless of scheduling); relation to
  [[streams-and-lazy-evaluation]] and [[mapreduce-and-dataflow]].
- **Discrete-event**: events with time stamps processed in order (VHDL/Verilog simulation,
  network simulators, SystemC); **continuous-time** solvers; **timed** models (timed automata,
  Giotto/LET, time-triggered).
Ptolemy II composes heterogeneous models hierarchically (a director per level).

## Sensing, actuation, timing (ch. 7, 9–10, 12)
Sensors: affine models, bias and noise, **sampling** (Nyquist, aliasing) and **quantization**
(ADC resolution), sensor fusion (Kalman filtering — [[probability-and-statistics-for-cs]]);
actuators: motors, PWM, saturation and slew limits. Timing: a control loop's stability
depends on latency and jitter; end-to-end latency through ISRs, RTOS tasks and buses
([[real-time-scheduling]]); **logical execution time** (Giotto) and time-triggered
architectures (TTA, FlexRay) make timing part of the interface; **PRET** machines make ISAs
timing-predictable; Lee 2008: the abstraction stack (transistors → ISA → language → threads)
was built to abstract *away* time, which is exactly what CPS cannot afford.

## Analysis and verification (ch. 13–16)
Specify with **invariants** and **temporal logic** (LTL: G safe, F done, G(request → F grant),
until); check by simulation, by **reachability analysis** and **model checking** (explicit-state
and symbolic — [[model-checking]], [[program-verification]]); relate models by trace
containment, **simulation** and **bisimulation** (refinement: an implementation whose
behaviours are a subset of the model's); quantitative analysis — **WCET**, memory bounds;
security of CPS (sensor spoofing, side channels — [[security-principles]]). Model-based design:
generate code from verified models (SCADE, Simulink Coder) and test with hardware-in-the-loop.

## Pitfalls
- Designing control logic in threads with ad hoc timing; assuming "fast enough" is
  deterministic.
- Composing components under unstated models of computation (a dataflow actor in an
  interleaving world).
- Simulating with fixed steps across discontinuities (missed guard crossings); Zeno models.
- Verifying the model, then hand-writing the code.

## Related
- [[real-time-scheduling]], [[microcontrollers-and-embedded-programming]],
  [[finite-automata-and-regular-languages]], [[model-checking]], [[program-verification]],
  [[streams-and-lazy-evaluation]], [[processes-and-threads]], [[floating-point]].

## Sources
Lee & Seshia, Introduction to Embedded Systems, 2nd ed., ch. 2–7, 12–16; Lee, "Cyber-Physical Systems: Design Challenges" (2008); Lee, "The Problem with Threads" (2006); Harel, "Statecharts" (1987); Benveniste et al., "The Synchronous Languages 12 Years Later" (2003).

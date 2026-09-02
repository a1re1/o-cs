---
title: Managing complexity — deep modules, strategic programming, and Ousterhout's red flags
type: concept
section: "2.2"
level: 300
tags: [software-design, complexity, deep-modules, shallow-modules, cognitive-load, change-amplification, unknown-unknowns, strategic-programming, tactical-programming, design-it-twice, pull-complexity-downward, red-flags]
sources: [ousterhout-philosophy-of-software-design, sicp]
summary: Complexity is whatever makes software hard to understand or change; it shows up as change amplification, cognitive load and unknown unknowns, is caused by dependencies and obscurity, and accumulates in small increments — so design deep modules (big functionality, small interface), pull complexity downward into implementations, program strategically (invest in design continually), and watch for the red flags.
---
# Managing complexity in software design

**In one sentence.** The job of design is to reduce the complexity the *next* reader/modifier faces;
the main tool is abstraction — modules whose interfaces are far simpler than what they hide.

## Complexity (Ousterhout ch. 2)
- **Symptoms**: change amplification (one change touches many places), cognitive load (how much you
  must know to do a task), unknown unknowns (you can't tell what you need to know).
- **Causes**: **dependencies** (code can't be understood or changed in isolation) and **obscurity**
  (important information is not obvious — bad names, undocumented units, hidden assumptions).
- Complexity is incremental — each shortcut is small; the sum is a mess. Hence "zero tolerance".

## Deep modules (ch. 4–5)
A module = interface + implementation. **Depth** = functionality ÷ interface complexity. Unix file
I/O (open/read/write/lseek/close) hides file systems, buffering, devices; a garbage collector has *no*
interface. **Shallow** modules (a class whose interface is as complex as its implementation, the Java
`FileInputStream`/`BufferedInputStream` layering, one-method wrappers) add cost without hiding
anything — "classitis". Prefer somewhat general-purpose interfaces (fewer, more powerful methods) over
special-purpose ones; each layer should provide a *different* abstraction (pass-through methods and
decorators are red flags).

## Information hiding and leakage (ch. 5, and Parnas)
Hide design decisions (formats, algorithms, data structures) inside modules; **leakage** is when a
decision is reflected in several modules (both modules know the file format). **Temporal
decomposition** — splitting code by the order things happen (read file, modify, write) — leaks
knowledge across modules; decompose by knowledge instead ([[modularity-and-information-hiding]]).

## Practices
- **Pull complexity downward**: the implementer should suffer so callers don't (configuration
  parameters are often pushed-up complexity).
- **Define errors out of existence**: pick semantics that make error cases normal (see
  [[specifications-and-invariants]] for the fail-fast trade-off); mask/aggregate exceptions at low levels.
- **Better together or apart**: combine if they share information, are always used together, or
  simplify the interface; split if general vs special purpose.
- **Strategic programming**: spend 10–20% on design continually (small investments, not big up-front
  design); **design it twice** — sketch two or three interfaces before picking.
- Comments and naming as design tools ([[code-review]]).

## Red flags (memorize)
Shallow module · information leakage · temporal decomposition · overexposure (rarely used features in
the common interface) · pass-through method · repetition · special-general mixture · conjoined methods
(can't understand one without the other) · comment repeats code · implementation documentation
contaminates interface · vague name · hard-to-pick name · hard-to-describe · nonobvious code.

## Related
- [[modularity-and-information-hiding]], [[specifications-and-invariants]], [[code-review]],
  [[data-abstraction]] (SICP's abstraction barriers are deep modules), [[design-patterns-catalog]].

## Sources
Ousterhout ch. 2–9, 21; SICP 2.1.2.

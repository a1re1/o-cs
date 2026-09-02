---
title: Interaction Design and Cognitive Models
type: concept
section: "9.1"
level: 400
tags: [fitts-law, goms, model-human-processor, direct-manipulation, hicks-law]
sources: [hci-texts-courses-and-seminal-papers]
summary: The quantitative side of HCI — Fitts's law for pointing, GOMS and the Model Human Processor for task time, Hick's law for choice, and direct-manipulation design principles.
---

# Interaction Design and Cognitive Models
**In one sentence.** The predictive, quantitative models of HCI — how long a
pointing move or a menu choice takes, and how to lay out controls so the common
case is fast — plus the interaction styles (direct manipulation) built on them.

## Why it matters
Fitts's law and GOMS turn interface design from taste into engineering: you can
*predict* which of two layouts is faster before building either, and explain why
big buttons at screen edges (infinite width) and radial menus win. This is the
"psychology of HCI" that Card, Moran & Newell founded; see
[[human-computer-interaction]].

## How it works
**Fitts's law** — time to acquire a target by rapid aimed movement:

```
MT = a + b · log2( D / W + 1 )
```

- `D` = distance to the target, `W` = target width along the motion axis.
- The log term is the **index of difficulty (ID)**, in bits; `1/b` is throughput.
- Consequences: bigger and nearer targets are faster; **screen edges and corners
  are effectively infinitely wide** (the pointer stops there), so menu bars and the
  four corners are prime real estate; small close buttons far from the cursor are slow.

**Hick's law** — decision time grows with the log of the number of equally likely
choices: `T = a + b · log2(n + 1)`. Fewer, well-grouped options are faster to choose
than a flat list of many.

**The Model Human Processor (MHP)** — Card/Moran/Newell's engineering model of the
human as perceptual, cognitive, and motor processors with characteristic cycle
times (~100 ms each) and memories. It yields back-of-envelope timing predictions.

**GOMS** — **Goals, Operators, Methods, and Selection rules.** Decompose an expert
task into keystroke-level operators with measured durations (the **Keystroke-Level
Model**, KLM) and sum them to predict skilled task time *without user testing*. Best
for high-frequency expert tasks (data entry, call-center flows).

**Direct manipulation** (Shneiderman): continuous representation of objects,
physical actions instead of complex syntax, rapid reversible operations with
immediate visible feedback. Dragging a file to trash beats `rm`; a slider beats
typing a number. The cost is discoverability of non-visible operations and
scalability to bulk actions.

**Shneiderman's Eight Golden Rules** (a design counterpart to Nielsen's heuristics):
consistency, universal usability, informative feedback, dialog closure, error
prevention, easy reversal, user control (internal locus), and reduce short-term
memory load.

## Complexity & trade-offs
- Fitts/GOMS predict **expert, error-free, motor-bound** performance; they say
  nothing about learning, errors, or satisfaction — pair them with
  [[usability-evaluation-and-user-research]].
- Direct manipulation is discoverable but does not scale to repetitive or bulk
  operations, where a command language or macros win. Modern UIs offer both.

## Pitfalls & gotchas
- Applying Fitts across a discontinuity (targets on another monitor) breaks the
  model; the edge-width trick fails on scrolling or infinite canvases.
- GOMS models the *skilled* user; it overstates performance for novices.
- Over-minimizing choices (Hick's law) can bury power features novices never find.

## Worked example
Two toolbars: A places the most-used tool as a 16 px icon in the center; B places it
as a 48 px icon in the top-left corner. Fitts's law predicts B is faster — larger
`W`, and the corner is effectively infinite width because the pointer cannot overshoot
it. A GOMS/KLM model of a 20-click editing session quantifies the saving before you
build either.

## Related
- [[human-computer-interaction]] — the design principles these models quantify.
- [[usability-evaluation-and-user-research]] — empirical methods that complement the models.
- [[entropy-and-information]] — Fitts's index of difficulty is measured in bits.

## Sources
Distilled from [[hci-texts-courses-and-seminal-papers]] (Card, Moran & Newell 1983;
Fitts 1954; Shneiderman *Designing the User Interface*).

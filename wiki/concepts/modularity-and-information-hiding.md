---
title: Modularity and information hiding (Parnas)
type: concept
section: "2.2"
level: 300
tags: [modularity, information-hiding, parnas, decomposition, interfaces, coupling, cohesion, design-decisions, encapsulation, temporal-decomposition]
sources: [ousterhout-philosophy-of-software-design, mit-6-102-software-construction]
summary: Decompose a system so that each module hides one design decision likely to change (Parnas 1972) rather than one step of the processing; measure the result by coupling (low) and cohesion (high), and expect the interfaces — not the flowchart — to be what survives change.
---
# Modularity and information hiding

**In one sentence.** Parnas's criterion: choose modules so that each one hides a design decision
from the others; then changes to that decision stay inside one module.

## The Parnas argument (1972, "On the Criteria To Be Used in Decomposing Systems into Modules")
The KWIC index example: decomposition 1 follows the flowchart (input, circular shift, alphabetize,
output) — every module knows the line storage format, so changing it touches everything.
Decomposition 2 hides decisions: a line-storage module hides the format; a circular-shifter hides
whether shifts are stored or computed; the alphabetizer hides sort timing. Same functionality, but
decomposition 2 localizes each anticipated change, enables independent development, and is more
comprehensible. Corollary: **interfaces should be designed to reveal as little as possible about
inner workings**, and modules should be documented by the *secret* they keep.
(Ousterhout's "temporal decomposition" red flag is decomposition 1 rediscovered.)

## Vocabulary
- **Coupling**: how much modules depend on each other (shared data formats, globals, call ordering);
  aim low. **Cohesion**: how related the contents of a module are; aim high.
- **Encapsulation** = language support for hiding (private fields, opaque types, module systems);
  information hiding is the *design principle*; you can encapsulate without hiding a meaningful secret.
- **Interface vs implementation**: the interface is the module's promise; everything else may change
  ([[specifications-and-invariants]], [[abstract-data-types-and-rep-invariants]]).

## Heuristics for drawing module boundaries
1. List the decisions likely to change (storage format, algorithm, external service, UI toolkit,
   concurrency strategy); give each a home.
2. Put together things that must change together; separate things that change for different reasons
   (single-responsibility).
3. Depend on abstractions at boundaries you expect to swap (dependency inversion); don't abstract
   what won't change.
4. Check for leaks: does any format or assumption appear in two modules?
5. Prefer deep modules; avoid a module per processing step ([[managing-complexity-in-software-design]]).

## Consequences at scale
Conway's law (systems mirror communication structures), microservice boundaries, and package layering
are Parnas's criterion applied to teams and deployables (§7.1, §7.3 — [[software-architecture-styles]]).

## Related
- [[managing-complexity-in-software-design]], [[data-abstraction]], [[abstract-data-types-and-rep-invariants]],
  [[design-patterns-catalog]], [[software-architecture-styles]].

## Sources
Parnas 1972 (as summarized in Ousterhout ch. 5 and 6.102 reading 06); to be read in full in §2.5.

## Parnas's KWIC experiment (added §2.5)
Parnas 1972 decomposed the same KWIC-index program two ways: by processing step (input → circular
shift → alphabetize → output, all sharing table formats) and by *hidden design decision* (line
storage, shifting, alphabetizing, each behind function interfaces). Against five plausible changes
(input format, storage medium, character packing, shift representation, lazy vs eager sorting), the
flowchart decomposition touched every module while the information-hiding one touched one. Hence
the criterion: list the difficult or likely-to-change decisions first and give each its own module;
"it is almost always incorrect to begin the decomposition … on the basis of a flowchart". See
[[parnas-1972-criteria]]; the deep-module idea in [[managing-complexity-in-software-design]] is the
same criterion restated.

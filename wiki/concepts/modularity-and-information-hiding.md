---
title: Modularity and information hiding — Parnas' criteria for decomposing systems (hide design decisions likely to change, not processing steps; the KWIC example), interfaces and abstraction, coupling and cohesion, deep vs shallow modules (Ousterhout), abstract data types and representation independence, separation of concerns and layering, the open–closed principle and dependency inversion, APIs as contracts (Hyrum's law, versioning, deprecation), design documents, and how to judge a decomposition
type: concept
section: "7.1"
level: 300
tags: [modularity, information-hiding, parnas, kwic, design-decisions, secrets, interfaces, abstraction, abstraction-barrier, coupling, cohesion, loose-coupling, high-cohesion, deep-modules, shallow-modules, ousterhout, philosophy-of-software-design, abstract-data-types, representation-independence, encapsulation, separation-of-concerns, layering, single-responsibility, open-closed, dependency-inversion, solid, api-design, contracts, hyrums-law, versioning, semver, backward-compatibility, deprecation, design-docs, decomposition-criteria, change-impact, leaky-abstractions, dry, orthogonality, interface-segregation, law-of-demeter]
sources: [software-engineering-texts-courses-and-seminal-papers, parnas-1972-criteria]
summary: Parnas (1972) asked what criteria to use when dividing a system into modules and showed with the KWIC-index example that the conventional decomposition — one module per processing step in the flowchart — makes every module depend on shared decisions (the data format, the storage layout) so that changing one decision touches everything, whereas decomposing so that each module hides one design decision likely to change (its "secret": how lines are stored, how the alphabetizer works) lets decisions change inside one module with the interface intact — information hiding, the principle behind encapsulation, abstract data types with representation independence, and every good API; the derived vocabulary is coupling (how much modules know about each other — minimize; data over control over content coupling) and cohesion (how much a module's parts belong together — maximize), separation of concerns and layering (each layer depends only downward), Ousterhout's deep vs shallow modules (a deep module has a small interface over a large implementation — the interface is the cost, the functionality the benefit; shallow modules add interface without hiding anything), the "SOLID" heuristics (single responsibility, open–closed, Liskov substitution, interface segregation, dependency inversion) as restatements, DRY and orthogonality, and the warning that all non-trivial abstractions leak; interfaces are contracts that outlive implementations, which Hyrum's law says will be depended upon in every observable detail, so API design is versioning, backward compatibility, and deprecation policy as much as signatures; and the test of a decomposition is the change-impact question — for each likely change, how many modules must be touched, and can the change be made by someone who understands only one of them?
---
# Modularity and information hiding

**In one sentence.** Divide a system so that each module hides one decision that is likely
to change, expose only an interface that doesn't depend on that decision, and you can
change the decision later without a ripple — everything else in software design
(coupling, cohesion, ADTs, deep modules, SOLID, API versioning) is commentary on that
sentence.

## Parnas' criteria: how should I split my program into modules? (Parnas 1971/72 — read; source page [[parnas-1972-criteria]])
The 1972 paper opens by agreeing with the hymns to modular programming and noting that
"nothing is said about the criteria to use in dividing the system into modules". Example:
a **KWIC** (key word in context) index — lines are circularly shifted, the shifts
alphabetized, the result output. **Modularization 1** (conventional): modules = the
processing steps — input, circular shift, alphabetize, output, master control — sharing a
common core storage format and line representation; each module's interface is the shared
data structure. **Modularization 2** (unconventional): modules = **design decisions** — line
storage (hides how characters/lines are stored), input (hides format), circular shifter
(hides how shifts are represented — a table of indices, computed lazily or eagerly),
alphabetizer (hides the sort algorithm and when it runs), output, master control; each
exposes functions (CHAR(l, w, c), SETCHAR, WORDS, …) not data. Both work; under likely
changes — a different storage medium, packing several characters per word, a different
input format, alphabetizing on demand vs once, dropping the shifts and computing them on
the fly — modularization 1 changes several modules, modularization 2 changes one.
"It is almost always incorrect to begin the decomposition of a system on the basis of a
flowchart. We propose instead that one begins with a list of difficult design decisions
or design decisions which are likely to change. Each module is then designed to hide such
a decision from the others." Anticipated objection — efficiency (function calls instead of
direct data access): answered by compile-time inlining/assembly of modules (the paper
sketches what macros/inlining and later compilers deliver — [[compiler-optimizations]]).
The **secret** of a module is the design decision it hides; the interface is what stays
stable. Corollary (Parnas 1979, "designing for ease of extension and contraction"): modules
in a **uses** hierarchy; minimal subsets and extensions.

## The vocabulary (Constantine & Yourdon; McConnell ch. 5; SWE at Google)
**Coupling**: the degree to which modules depend on each other's internals — from best to
worst: data (parameters), stamp (structures), control (flags directing the callee),
common/global (shared data), content (one module reaching into another's internals);
temporal coupling (must be called in order); minimize and make it explicit through
interfaces. **Cohesion**: how strongly a module's elements belong together — functional
(one purpose) at the top, coincidental at the bottom; **single responsibility** ("one reason
to change") is Parnas restated. **Abstraction** (an interface that suppresses detail — the
**abstraction barrier**; clients program to the interface) vs **encapsulation** (enforcing the
barrier with access control); **abstract data types** ([[abstract-data-types-and-rep-invariants]]):
representation independence — a stack's clients don't know it's an array; the **rep
invariant** and **abstraction function** (Liskov & Guttag) as the discipline for implementers
([[design-by-contract]]). **Separation of concerns** (Dijkstra) and **layering** (each layer
uses only the one below — [[internet-architecture-and-layering]], OS layers): change stays
within a layer; the price is layer-crossing costs and **leaky abstractions** (Spolsky: every
non-trivial abstraction leaks — TCP over lossy links, ORMs over SQL, virtual memory over
disks; you must understand one level down when it leaks — [[virtual-memory]]).
**DRY** (every piece of knowledge has one authoritative representation — not "no
duplicated text") and **orthogonality** (independent axes of change) from the Pragmatic
Programmer; the **Law of Demeter** (talk only to immediate collaborators) as a coupling
heuristic; **SOLID** ([[solid-principles]]): single responsibility, **open–closed** (extend behaviour without
modifying existing code — via polymorphism/plugins), Liskov substitution ([[liskov-substitution]]; subtypes must
honour supertype contracts — [[type-systems]]), interface segregation (small client-
specific interfaces), **dependency inversion** (depend on abstractions; inject
implementations — enables test doubles, [[unit-testing]]).

## Deep modules (Ousterhout, *A Philosophy of Software Design*)
A module's **interface** is its cost (what every user must learn and every change must
preserve); its **functionality** is its benefit. **Deep modules** (Unix file I/O: five calls
hiding devices, buffering, permissions, caching; a garbage collector: zero interface) hide
a lot behind a little; **shallow modules** (a class per method, pass-through layers,
"classitis") add interface without hiding complexity. Complexity is anything that makes a
system hard to understand or modify; its symptoms are change amplification, cognitive
load, and unknown unknowns; its causes are dependencies and obscurity; the strategy is
**pull complexity downward** (make the module's implementation harder so its interface can
be simpler), **define errors out of existence**, and design it twice. This is Parnas with
a cost model: more secrets per interface = deeper.

## Interfaces as contracts, Hyrum's law, and API evolution (SWE at Google ch. 1, 15, 21)
An interface outlives its implementation; users will depend on **every observable
behaviour** whether promised or not (**Hyrum's law**: latency, error messages, iteration
order, exceptions thrown) — so the contract should be explicit (docs, types, assertions —
[[design-by-contract]]), tested at the boundary (contract tests, fuzzing for undocumented
behaviour — [[fuzzing]]), and intentionally narrow (every exposed detail is a future
constraint). **Versioning**: semantic versioning (major = breaking), stability tiers
(experimental/stable/deprecated), the **diamond dependency** problem in dependency
management (why "one version" policies and monorepos exist — [[dependency-management-and-packaging]]);
**backward compatibility** by additive change, feature flags, adapters; **deprecation** as a
planned process — advisory then compulsory, with migration tooling and large-scale-change
infrastructure (Google's LSC: automated refactors across the monorepo), because
unmaintained old versions are the real cost of never removing anything
([[technical-debt-and-maintenance]]). API design heuristics (Bloch): easy to use correctly,
hard to use incorrectly; minimal; consistent naming; fail fast; don't leak implementation
types; documentation is part of the API ([[api-design]]).

## Judging a decomposition (the change-impact test); design docs
The **change-impact test**: list the likely changes (new storage backend, new input format,
different algorithm, new platform, scale ×10, a second client); for each, count the modules
touched and ask whether one engineer who knows only that module can make it. Other tests:
can each module be tested in isolation (test doubles at the interfaces)? Can it be built,
deployed, and owned by one team ([[software-architecture-and-system-design]] — services are
modules with a network in between, and Conway's law makes team boundaries module
boundaries)? Does the interface reveal the secret (a `getArrayIndex()` on a stack does)?
**Design documents** (SWE at Google; RFCs): context and goals, non-goals, the proposed design
with alternatives considered and trade-offs, cross-cutting concerns (security, privacy,
scale), and a decision log — reviewed before the code, kept as the record of *why*, and
cheap to write compared with the code they prevent. Rewriting is not refactoring: the
module boundary is what lets you rewrite one part ([[refactoring]], [[design-patterns-catalog]]
for the mechanisms — strategy, adapter, facade — that realize hiding).

## Pitfalls
- Modules by flowchart step (Parnas' modularization 1) — every change ripples.
- Interfaces that expose the representation (getters for every field; "data classes" as
  APIs) or encode the algorithm (callback order, timing).
- Shallow layers and pass-through methods that add interface without hiding.
- Over-hiding: abstractions for changes that never come (speculative generality —
  YAGNI) and premature frameworks.
- Breaking changes without a deprecation path; or never deprecating.
- Believing an abstraction doesn't leak; not knowing one level down.

## Related
- [[software-engineering-fundamentals]], [[technical-debt-and-maintenance]],
  [[abstract-data-types-and-rep-invariants]], [[design-by-contract]], [[design-patterns-catalog]],
  [[refactoring]], [[unit-testing]] (test doubles), [[api-design]],
  [[dependency-management-and-packaging]], [[software-architecture-and-system-design]],
  [[type-systems]], [[internet-architecture-and-layering]], [[virtual-memory]] (leaky
  abstractions), [[compiler-optimizations]] (inlining answers the efficiency objection),
  [[fuzzing]], [[code-review]].

## Sources
Parnas 1971 (CMU-CS-71-101, read) / CACM 1972; Parnas 1979; Ousterhout 2018; Constantine & Yourdon 1979; Liskov & Guttag 2000; Martin 2000 (SOLID); Hunt & Thomas 1999; Bloch 2006 (API design); Spolsky 2002 (leaky abstractions); Winters, Manshreck & Wright 2020 ch. 1, 15, 21–22 (ToC read).

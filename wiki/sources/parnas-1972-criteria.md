---
title: On the Criteria To Be Used in Decomposing Systems into Modules (Parnas, 1972)
type: source
section: "2.5"
level: 300
tags: [information-hiding, modularity, decomposition, design-decisions, kwic, interfaces, changeability, parnas]
sources: []
authors: [David L. Parnas]
year: 1972
institution: Carnegie Mellon
url: https://dl.acm.org/doi/10.1145/361598.361623
license: ACM-open
format: pdf
summary: The paper that defined information hiding — compares two decompositions of a KWIC index system (by processing step vs. by hidden design decision) against five likely changes and shows that modules should hide difficult or likely-to-change design decisions behind interfaces, not correspond to steps in a flowchart; independent development and comprehensibility improve too, and hierarchical structure is a separate concern.
---
# On the Criteria To Be Used in Decomposing Systems into Modules

## What it is
Five pages. A brief status of modular programming (the benefits — shorter development time,
flexibility, comprehensibility — depend on *how* you divide); the KWIC index example (input,
circular shift, alphabetize, output); **Modularization 1** — one module per processing step, all
sharing the core line/word tables; **Modularization 2** — modules for line storage, input, circular
shifter, alphabetizer, output, master control, each with abstract interfaces (functions like
`CHAR(r, w, c)`, `CSCHAR`, `ITH`). Both work; the comparison is on *changes*: input format, storing
lines on disk vs core, packing characters, storing shifts as indices vs copies, alphabetizing lazily
vs eagerly. In the first decomposition most changes touch every module; in the second each is
confined to one. Independent development starts earlier when interfaces are function names and
parameter types rather than table formats. Then "The Criteria": the flowchart criterion vs
**information hiding** — "every module … is characterized by its knowledge of a design decision
which it hides from all others"; efficiency concerns (procedure-call overhead can be handled by a
build-time assembler); hierarchical structure ("uses") is a separate property; conclusion —
begin with a list of difficult design decisions or decisions likely to change, and make each a
module.

## Notable claims
- "It is almost always incorrect to begin the decomposition of a system on the basis of a
  flowchart."
- Modules 2's interfaces are *abstract*; Modules 1's are shared data formats — the difference is
  what an interface exposes, not the number of modules.
- The examples of hidden decisions: data formats, storage location, sequencing of processing, the
  character encoding.

## What it adds
The origin of [[modularity-and-information-hiding]]; the "design for change" argument later
formalized as deep modules ([[managing-complexity-in-software-design]]), ADTs
([[abstract-data-types-and-rep-invariants]]) and Conway-style team boundaries.

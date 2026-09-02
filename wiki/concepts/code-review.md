---
title: Code review, readability, and comments
type: concept
section: "2.2"
level: 200
tags: [code-review, readability, comments, naming, dry, magic-numbers, global-variables, code-smells, style, obviousness, documentation]
sources: [mit-6-102-software-construction, ousterhout-philosophy-of-software-design]
summary: Code review is reading code for bugs, clarity, and changeability — 6.102's checklist (don't repeat yourself, comments where needed, no magic numbers, one purpose per variable, no globals, return rather than print, avoid special-case code) plus Ousterhout's standard: code should be obvious, and comments should say what the code cannot (interface abstraction, why, units, invariants).
---
# Code review and readable code

**In one sentence.** Review for the three measures — safe from bugs, easy to understand, ready for
change — using a checklist so the review is about the code, not the author.

## The 6.102 checklist (reading 03)
- **Don't repeat yourself**: duplicated code = duplicated bugs; extract a function.
- **Comments where needed**: a spec comment on every function/class (what, not how); cite sources of
  copied code/algorithms; no comments that restate the code.
- **Fail fast**: detect errors early (static > dynamic > silent) ([[specifications-and-invariants]]).
- **Avoid magic numbers**: name constants; explain where they come from.
- **One purpose for each variable**: don't reuse a variable for two things; prefer `const`/final.
- **Use good names**: descriptive, consistent, no abbreviations that only you know; methods are verbs,
  values are nouns; `tmp`, `data`, `result2` are red flags.
- **Use whitespace and consistent formatting** (let the formatter do it).
- **Don't use global variables**: they create hidden dependencies and break testing.
- **Methods should return results, not print them**: keep I/O at the edges.
- **Avoid special-case code**: handle the empty/edge case through the general path when possible.

## Ousterhout's additions
- **Code should be obvious**: a reader should understand it quickly without needing to think hard; if a
  reviewer finds something non-obvious, it *is* non-obvious — fix the code, don't argue.
- **Comments describe what the code can't**: interface comments define the abstraction (what a caller
  needs to know and nothing about the implementation); implementation comments explain *why* and
  non-obvious *what* (units, invariants, ranges, ownership). Write the interface comments *first* — if
  the comment is hard to write, the abstraction is wrong. Red flag: a comment that just repeats the code.
- **Names**: precise, consistent; a hard-to-name thing is often a badly-scoped thing.
- **Consistency** (style, naming, patterns) lowers cognitive load; follow existing conventions even if you
  prefer others.

## Running a review
Small diffs; describe the intent in the PR; reviewer reads the spec/tests first, then the code; comment
on *what* and *why*, suggest rather than command; the author fixes root causes, not just the flagged
line; automate style (formatters, linters) so humans review design and correctness
([[managing-complexity-in-software-design]]).

## Related
- [[specifications-and-invariants]], [[unit-testing]], [[managing-complexity-in-software-design]],
  [[modularity-and-information-hiding]], [[debugging]].

## Sources
6.102 reading 03 (Code Review); Ousterhout ch. 12–18.

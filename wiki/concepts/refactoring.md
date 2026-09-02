---
title: Refactoring — code smells and behavior-preserving transformations
type: concept
section: "2.5"
level: 300
tags: [refactoring, code-smells, extract-function, inline, rename, move-function, guard-clauses, replace-conditional-with-polymorphism, parameter-object, feature-envy, duplicated-code, long-function, technical-debt, tests, two-hats]
sources: [fowler-refactoring, ousterhout-philosophy-of-software-design, mit-6-102-software-construction]
summary: Refactoring is changing internal structure without changing observable behavior, in small verified steps under tests; work smell-first (duplicated code, long function, feature envy, data clumps, primitive obsession, shotgun surgery, repeated switches, message chains…), apply the named refactoring that removes the smell (Extract Function, Rename, Move, Replace Temp with Query, Introduce Parameter Object, Guard Clauses, Replace Conditional with Polymorphism…), never mix refactoring with adding features, and refactor when it makes the next change easier.
---
# Refactoring

**In one sentence.** Make the change easy (this may be hard), then make the easy change — Kent Beck.

## Ground rules (Fowler ch. 2)
- Definition: restructure without changing behaviour; each step is tiny and the tests stay green,
  so a mistake is found immediately and reverted cheaply ([[unit-testing]]).
- **Two hats**: adding function or refactoring, never both at once; commit separately.
- When: rule of three (third duplication → refactor), preparatory (before a feature),
  comprehension (while reading), litter-pickup (tidy as you go), planned only when debt is severe.
  When not: code that never needs changing; a rewrite is genuinely cheaper.
- Performance: refactor for clarity first, then profile and optimize the hot spots
  ([[profiling-and-performance]]).
- Tooling: IDE-safe renames/extracts, type checkers and tests as the net.

## Smell → refactoring map (ch. 3 → catalogue)
| Smell | Typical remedy |
|---|---|
| Mysterious name | Rename (variable/function/field); Change Function Declaration |
| Duplicated code | Extract Function; Pull Up Method; Slide Statements |
| Long function | Extract Function (name by intent); Replace Temp with Query; Decompose Conditional |
| Long parameter list | Introduce Parameter Object; Preserve Whole Object; Replace Parameter with Query |
| Global / mutable data | Encapsulate Variable; Separate Query from Modifier; Split Variable |
| Divergent change / Shotgun surgery | Split Phase; Move Function; Extract Class / Inline Class |
| Feature envy | Move Function to the data it uses |
| Data clumps / Primitive obsession | Extract Class; Replace Primitive with Object |
| Repeated switches / type codes | Replace Conditional with Polymorphism; Replace Type Code with Subclasses |
| Loops | Replace Loop with Pipeline ([[fold-and-structural-recursion]]) |
| Nested conditionals | Replace Nested Conditional with Guard Clauses; Consolidate Conditional |
| Message chains / Middle man | Hide Delegate / Remove Middle Man |
| Refused bequest | Replace Subclass/Superclass with Delegate ([[inheritance-vs-composition]]) |
| Comments explaining bad code | refactor until the comment is unnecessary; keep *why* comments |

## Technique
1. Ensure tests cover the area (write characterization tests for legacy code).
2. Take the smallest step (extract, rename); run tests; commit.
3. Use the compiler: change a signature, follow the errors.
4. Keep a **change list**; stop when the intended change is now easy.
5. Prefer strategic to tactical: refactor toward deep modules and clear interfaces
   ([[managing-complexity-in-software-design]]), not just smaller functions.

## Pitfalls
- "Refactoring" without tests (that's just editing).
- Big-bang restructures that block other work; long-lived branches.
- Over-extracting into one-line functions that scatter logic (Ousterhout's shallow-module warning).
- Refactoring the code you happen to be reading rather than the code the next change needs.

## Related
- [[design-patterns-catalog]], [[solid-principles]], [[unit-testing]], [[code-review]],
  [[managing-complexity-in-software-design]], [[inheritance-vs-composition]].

## Sources
Fowler 2nd ed. ch. 1–4, 6–12; Ousterhout ch. 4, 9; 6.102 code review reading.

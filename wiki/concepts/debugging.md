---
title: Debugging — strategies, binary search on the bug, and the scientific method
type: concept
section: "2.1"
level: 100
tags: [debugging, error-types, syntax-errors, runtime-errors, semantic-errors, print-debugging, debugger, breakpoints, bisecting, minimal-reproduction, rubber-duck, scientific-method]
sources: [think-python, harvard-cs50]
summary: Classify the error (syntax, runtime, semantic), reproduce it minimally, form a hypothesis about where behaviour diverges from expectation, and binary-search the program or the history to localize it — with print statements, a debugger, assertions, or git bisect — then fix one thing at a time and keep the test.
---
# Debugging

**In one sentence.** Debugging is experimental science: reproduce, hypothesize, test with the
cheapest experiment, narrow the region, repeat — never change several things at once and hope.

## Kinds of errors (Think Python)
- **Syntax**: won't parse; read the *first* error message and the line before it.
- **Runtime** (exceptions): read the traceback bottom-up for the exception and top-down for your
  frames; the last *your-code* frame is the usual suspect.
- **Semantic**: runs, wrong answer — the hard one; needs a mental model of what the program should do.

## The loop
1. **Reproduce** deterministically; shrink the input to the smallest that still fails (minimal
   reproduction — [[delta-debugging]] automates this).
2. **Localize** by bisection: add prints/assertions at the midpoint of the suspect region — does the
   state look right here? Halve the region each time. Over history: `git bisect`.
3. **Hypothesize** one cause; predict what an experiment would show; run it. Read the code around the
   suspect line slowly ("reading"); "ruminating" beats random edits.
4. **Fix** one thing; re-run the reproduction *and* the test suite; add a regression test.
5. If stuck: explain the problem aloud to someone or a rubber duck; take a break ("retreating"); revert
   to the last known-good state and re-apply changes incrementally.

## Tools
- Print/log with context (variable names and values, not just "here"); Python f-strings `f"{x=}"`.
- Debuggers (pdb, gdb, lldb, IDE): breakpoints, step, inspect frames, watchpoints — cheaper than prints
  for exploring state, worse for loops with thousands of iterations (use conditional breakpoints).
- Assertions and invariants: fail early near the cause instead of late near the symptom
  ([[invariant-principle]]).
- Type checkers, linters, sanitizers (ASan/UBSan for C — [[undefined-behavior]]), `valgrind`.
- Logging levels and structured logs in long-running systems (§7.4 observability).

## Classic causes to check first
Off-by-one, wrong variable, integer vs float division, mutable default/shared state
([[assignment-state-and-environments]]), stale cache/build, wrong environment/config, uninitialized
memory, unchecked return values, character encoding, timezone.

## Pitfalls
- Fixing the symptom (special-casing the failing input) instead of the cause.
- Changing multiple things before re-testing; not re-running the failing case after the "fix".
- Trusting comments/docs over behaviour; trusting the first stack frame.

## Related
- [[design-recipe]], [[invariant-principle]], [[unit-testing]], [[delta-debugging]], [[undefined-behavior]].

## Sources
Think Python "Debugging" sections and appendix; CS50 weeks 1–4 (debug50, valgrind); Agans' 9 rules and Zeller's Debugging Book to be added in §2.6/§7.2.

## Tools ladder and Agans's rules (added §2.6)
Missing Semester's order: printf/logging with levels and colour (structured logs, `journalctl`,
`/var/log`); a **debugger** for state inspection — `pdb`/`ipdb` (`l s n b p r q`), `gdb`/`lldb`
(`break`, `bt`, `x/8gx $rsp`, `watch`); **specialized tracers** when the bug is outside your code —
`strace`/`dtruss` for syscalls, `ltrace`, `tcpdump`/Wireshark for packets; **static analysis** and
linters (`pyflakes`, `mypy`, `shellcheck`, clang-tidy) and sanitizers ([[undefined-behavior]]);
`git bisect` to find the commit that introduced a regression ([[git-data-model]]).
Agans's nine rules: understand the system; **make it fail** (reproduce reliably, then automate);
**quit thinking and look** (instrument before hypothesizing); divide and conquer (binary search
the pipeline/data/history); change one thing at a time; keep an audit trail; check the plug
(assumptions: right binary? right config?); get a fresh view; if you didn't fix it, it ain't fixed
(a bug that "went away" is still there). See [[tlcl-shotts]], [[profiling-and-performance]].

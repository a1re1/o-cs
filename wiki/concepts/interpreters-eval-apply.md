---
title: Interpreters — the eval/apply cycle and the metacircular evaluator
type: concept
section: "2.1"
level: 200
tags: [interpreters, metacircular-evaluator, eval, apply, read-eval-print-loop, environments, special-forms, scheme, calculator, tree-walking-interpreter, homoiconicity]
sources: [sicp, composing-programs]
summary: An interpreter is two mutually recursive procedures — eval (dispatch on expression type: self-evaluating, variable, special form, or application) and apply (primitive or compound procedure: bind parameters in a new frame and eval the body) — plus environments; writing one for Scheme in Scheme (the metacircular evaluator) makes the language's semantics concrete and is the first step toward compilers.
---
# Interpreters: eval and apply

**In one sentence.** `eval(expr, env)` turns syntax into a value by cases; `apply(proc, args)` runs a
procedure by extending its environment and calling `eval` on the body; everything else is bookkeeping.

## The core (SICP 4.1)
```
eval(exp, env):
  if self_evaluating(exp): return exp                 # numbers, strings
  if variable(exp):        return lookup(exp, env)
  if quoted(exp):          return text_of_quotation(exp)
  if assignment/definition(exp): eval value, then set/define in env
  if if_exp(exp):          eval predicate, then one branch     # special forms control evaluation
  if lambda(exp):          return make_procedure(params, body, env)   # closure captures env
  if begin(exp):           eval sequence, return last
  if cond(exp):            eval(cond_to_if(exp), env)          # derived expressions = macros
  if application(exp):     return apply(eval(operator), [eval(a) for a in operands])
apply(proc, args):
  if primitive(proc):      call the underlying implementation
  if compound(proc):       eval_sequence(body, extend_env(params, args, proc.env))
```
The **environment** (frames with parent pointers) is the interpreter's central data structure
([[substitution-and-environment-models]]); a **special form** is any syntax whose operands are not all
evaluated first (`if`, `and`, `define`, `lambda`, `quote`); **derived expressions** desugar to core
forms; the **read–eval–print loop** parses text into a tree (in Lisp, the tree *is* data: homoiconicity),
evals, prints.

## Why build one
- Makes scoping, closures, tail calls, and evaluation order concrete — you decide them.
- Variations are small edits: lazy evaluation (delay operands — SICP 4.2), nondeterministic `amb`
  with backtracking (4.3), a logic-programming query language via unification (4.4), "analyze once,
  execute many" separating syntax analysis from execution (4.1.7) — the first optimization on the way
  to a compiler ([[compiler-pipeline]]).
- CS61A's Scheme project and Composing Programs' calculator are this design in Python.
- Tree-walking interpreters like this are simple and slow; bytecode VMs and JITs follow the same
  eval/apply structure with a different representation ([[bytecode-and-virtual-machines]]).

## Gotchas when writing one
- Evaluation order of operands (left-to-right? unspecified?) leaks into semantics with side effects.
- Deep recursion in the host language for deep recursion in the guest: implement tail calls
  (trampolining) or an explicit stack.
- Errors: distinguish syntax errors (parse), unbound variables, wrong arity, type errors; good messages
  need source positions.
- `define` inside a body vs at top level; internal definitions are scanned out or made letrec.

## Related
- [[substitution-and-environment-models]], [[data-abstraction]] (dispatch on expression type is
  data-directed programming), [[compiler-pipeline]], [[lambda-calculus]], [[parsing]].

## Sources
SICP 4.1–4.4, 5.5; Composing Programs 3.2–3.5 (calculator and Scheme interpreters).

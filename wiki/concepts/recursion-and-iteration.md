---
title: Recursion vs iteration, tail calls, tree recursion, and memoization
type: concept
section: "2.1"
level: 100
tags: [recursion, iteration, tail-recursion, tail-call-optimization, tree-recursion, memoization, structural-recursion, generative-recursion, accumulators, stack-overflow, base-case]
sources: [sicp, htdp, composing-programs, think-python]
summary: A recursive procedure can generate an iterative process (constant space, tail call) or a recursive one (stack grows); tree recursion can be exponential until memoized; structural recursion follows the data definition and terminates automatically while generative recursion needs a termination argument; accumulators convert one to the other.
---
# Recursion and iteration

**In one sentence.** Recursion is a *procedure* shape; whether the resulting *process* needs a growing
stack depends on whether anything remains to be done after the recursive call.

## Linear recursion vs iteration (SICP 1.2.1)
```
fact(n) = n * fact(n-1)              # recursive process: deferred multiplications pile up, O(n) space
fact_iter(product, counter, n)       # iterative process: state in the arguments, O(1) space (with TCO)
```
The second is a **tail call**: nothing to do after the call returns. Scheme guarantees tail-call
optimization, so loops are unnecessary; Python and Java do not (recursion depth ~1000 in CPython), so
convert deep tail recursion to a loop or an explicit stack. Any recursion can be made iterative with an
explicit stack; any loop can be written as tail recursion with accumulators (HtDP Part VI).

## Tree recursion
fib(n) = fib(n−1) + fib(n−2) does Θ(φⁿ) work because subproblems repeat; **memoization** (cache
results in a dictionary) or bottom-up tabulation makes it Θ(n) — the seed of dynamic programming
([[dynamic-programming]]). Tree recursion is the natural shape for trees, partitions (count_partitions
in Composing Programs), subsets, and backtracking; its cost is the number of nodes in the call tree.

## Structural vs generative recursion (HtDP)
- **Structural**: recursion mirrors the data definition (list → first + rest; tree → children). The
  template guarantees a base case and termination; it is [[induction]] on the data.
- **Generative**: the recursive call is on data you *generate* (quicksort's partitions, gcd, binary
  search, graph search). You must argue termination separately with a decreasing measure
  ([[invariant-principle]]) and check for cycles (visited sets).

## Writing a recursive function
1. Base case(s) first — what input needs no recursion? (Missing base case ⇒ infinite recursion /
   stack overflow; wrong base case ⇒ off-by-one.)
2. Assume the recursive call works on smaller input (the "recursive leap of faith").
3. Combine. Then check: is the recursive input strictly smaller?
4. If the natural version passes context downward (index, running total, visited set), add an
   accumulator parameter and a wrapper.

## Costs and pitfalls
- Recursion depth limits; mutual recursion; blowing the C stack in kernels/embedded code.
- Rebuilding lists by appending in non-tail position is O(n²) in some languages; accumulate and reverse.
- Memoization needs immutable/hashable arguments and unbounded caches need eviction.
- Iteration is not "faster" than recursion in general; the process shape is what matters.

## Related
- [[induction]], [[recurrences]] (cost of recursive algorithms), [[dynamic-programming]],
  [[higher-order-functions]], [[design-recipe]].

## Sources
SICP 1.2; HtDP Parts II, V, VI; Composing Programs 1.7; Think Python ch. 5.

---
title: Divide and conquer, recursion trees, and the master theorem
type: concept
section: "3.2"
level: 300
tags: [divide-and-conquer, master-theorem, recursion-tree, mergesort, karatsuba, strassen, closest-pair, counting-inversions, linear-time-selection, median-of-medians, binary-search, reductions, recursion-fairy]
sources: [erickson-algorithms, clrs, dpv-algorithms, roughgarden-algorithms-illuminated]
summary: Split the input into independent smaller instances of the same problem, solve them recursively (trust the Recursion Fairy — the induction hypothesis), and combine; the running time obeys T(n) = a·T(n/b) + f(n), which the recursion tree and the master theorem resolve by comparing f(n) to n^log_b a — the three cases give mergesort n log n, Karatsuba n^1.585, Strassen n^2.81, binary search log n, and linear-time selection via median of medians.
---
# Divide and conquer

**In one sentence.** Reduce the problem to smaller copies of itself, delegate those to "the
Recursion Fairy" (Erickson's name for the induction hypothesis), and spend your effort on split
and merge.

## Reductions and recursion (Erickson ch. 1)
A **reduction** solves X using a black box for Y; correctness never depends on how the box works
(only running time does). Recursion is reduction to smaller instances of the same problem: solve
directly if small, otherwise simplify and delegate; the only requirement is a well-founded
measure that strictly decreases ([[induction]], [[recursion-and-iteration]]). Never "unroll" the
recursion in your head — trust the specification.

## The recurrence: T(n) = a·T(n/b) + f(n)
a subproblems of size n/b, f(n) to split and combine. **Recursion tree**: level i has aⁱ nodes of
size n/bⁱ, depth log_b n, leaves n^{log_b a}. Sum level costs Σ aⁱ f(n/bⁱ):
- **Case 1** f(n) = O(n^{log_b a − ε}): leaves dominate → T = Θ(n^{log_b a}) (Karatsuba: 3T(n/2)+n
  → n^{1.585}; Strassen: 7T(n/2)+n² → n^{2.807}; binary-tree traversal 2T(n/2)+1 → n).
- **Case 2** f(n) = Θ(n^{log_b a} log^k n): every level equal → T = Θ(n^{log_b a} log^{k+1} n)
  (mergesort 2T(n/2)+n → n log n; binary search T(n/2)+1 → log n).
- **Case 3** f(n) = Ω(n^{log_b a + ε}) with regularity a f(n/b) ≤ c f(n): root dominates →
  T = Θ(f(n)) (T(n/2) + n → n; 2T(n/2)+n² → n²).
Unequal splits and additive terms: Akra–Bazzi; T(n) = T(n/5) + T(7n/10) + n → O(n) because
1/5 + 7/10 < 1. General techniques in [[recurrences]] (substitution/guess-and-check, unrolling).

## The canon
| Algorithm | Split / combine | Recurrence → time |
|---|---|---|
| Mergesort | halves / linear merge | 2T(n/2)+n → n log n ([[sorting]]) |
| Quicksort | partition around pivot / nothing | expected n log n with random pivot ([[randomized-algorithms]]) |
| Binary search | one half / O(1) | T(n/2)+1 → log n |
| Counting inversions | halves / count during merge | n log n |
| Closest pair of points | halves by x / strip check with 7 neighbours | n log n |
| Karatsuba multiplication | 3 half-size products (a+b)(c+d) trick | n^{1.585}; Schönhage–Strassen/FFT n log n ([[fft]]) |
| Strassen | 7 block products instead of 8 | n^{2.807} |
| Linear-time selection | median of medians of 5 as pivot | T(n/5)+T(7n/10)+n → O(n); QuickSelect expected O(n) |
| FFT | even/odd coefficients at roots of unity | 2T(n/2)+n → n log n |
| Tower of Hanoi | 2T(n−1)+1 → 2ⁿ | (not all recursion is fast) |
Cache-oblivious algorithms exploit the same recursion to fit every cache level automatically
([[caches-and-memory-hierarchy]]).

## Pitfalls
- Non-independent subproblems (overlap) → exponential; that's [[dynamic-programming]] territory.
- Forgetting the combine cost, or a merge that isn't linear (list concatenation by copying).
- Recursion depth: n-deep recursion on unbalanced splits (quicksort on sorted input without
  randomization) → stack overflow; convert to iteration or bound the depth.
- Master theorem gaps (f between cases, non-polynomial differences): use the recursion tree.

## Related
- [[recurrences]], [[dynamic-programming]], [[sorting]], [[randomized-algorithms]], [[fft]],
  [[induction]], [[asymptotic-notation]].

## Sources
Erickson ch. 1; CLRS ch. 4, 9; DPV ch. 2; Roughgarden part 1.

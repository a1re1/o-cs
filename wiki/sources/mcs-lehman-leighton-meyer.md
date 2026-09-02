---
title: Mathematics for Computer Science (Lehman, Leighton, Meyer)
type: source
section: "1.1"
level: 200
tags: [discrete-math, proofs, induction, graph-theory, number-theory, counting, probability-discrete, asymptotics]
sources: []
authors: [Eric Lehman, F. Thomson Leighton, Albert R. Meyer]
year: 2015
institution: MIT
url: https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf
license: CC-BY-SA
format: pdf
summary: The free MIT 6.042J textbook; ~1000 pages in four parts (Proofs, Structures, Counting, Probability) that teach discrete math as a programmer's toolkit, with the Invariant Principle, DAG scheduling, stable matching, and tail bounds as CS-flavored set pieces.
---
# Mathematics for Computer Science (Lehman, Leighton, Meyer, 2015)

## What it is
The textbook for [[mit-6-042j]] (now 6.1200). Level 200, no prerequisites beyond high-school algebra.
Four parts: **I Proofs** (ch 1–7: propositions, well ordering, logic, sets/relations/functions,
induction, recursive data types, infinite sets), **II Structures** (ch 8–12: number theory, directed
graphs & partial orders, communication networks, simple graphs, planar graphs), **III Counting**
(ch 13–15: sums & asymptotics, cardinality rules, generating functions), **IV Probability**
(ch 16–21: events, conditional probability, random variables, deviation from the mean, random walks,
Markov chains… actually random processes). Every chapter ends with a large bank of problems; many are
drawn from CS (scheduling, RSA, hashing, load balancing).

The book's distinctive move is to treat discrete math as *reasoning about programs and processes*:
induction is introduced alongside state machines, and the [[invariant-principle]] is a named theorem.

## Key ideas
- Proofs are essays, not calculations; "state your game plan" — see [[proof-techniques]].
- Well ordering, ordinary induction and strong induction are the *same reasoning in three formats*;
  choose the one that reads best — see [[induction]].
- Floyd's **Invariant Principle**: a property preserved by every transition and true of the start state
  is true of every reachable state. Termination via a strictly decreasing derived variable in a
  well-ordered set — see [[invariant-principle]].
- Mapping rules (bijection, injection, surjection) as the engine of [[counting-rules]] and of the
  [[pigeonhole-principle]]; "identify the pigeons, the holes and the function".
- Directed graphs: walk relations, DAGs as prerequisite structures, minimum parallel schedule time =
  longest chain, Dilworth-style antichain bound — see [[dags-and-partial-orders]].
- Simple graphs: degree sum, bipartite matching and Hall's condition, coloring, connectivity, trees,
  the Stable Marriage "mating ritual" (Gale–Shapley) — see [[graph-theory-basics]], [[stable-matching]].
- Number theory built around the Euclidean algorithm, Bézout, modular inverses, Euler's theorem, and
  a full derivation of RSA — see [[number-theory-basics]], [[modular-arithmetic]].
- Asymptotics: little-o, big-O via lim sup, Θ, and the warning that asymptotically faster (O(n^2.55)
  matrix multiply) is not the same as better in practice — see [[asymptotic-notation]].
- Probability: the **Four Step Method** (sample space → events → outcome probabilities → event
  probability) that dissolves Monty Hall; conditional probability, independence, random variables,
  linearity of expectation, and tail bounds (Markov, Chebyshev, Chernoff) — see [[four-step-method]],
  [[concentration-inequalities]].

## Chapter map (selected)
| Ch | Topic | Wiki pages |
|---|---|---|
| 1 | What is a proof; good proofs in practice | [[proof-techniques]] |
| 2, 5 | Well ordering; induction; state machines | [[induction]], [[invariant-principle]] |
| 3 | Propositional logic, SAT, predicate formulas | [[propositional-logic]] |
| 4 | Sets, sequences, functions, relations, cardinality | [[sets-relations-functions]] |
| 6 | Recursive definitions & structural induction | [[induction]] |
| 8 | Number theory, RSA | [[number-theory-basics]], [[modular-arithmetic]] |
| 9 | Directed graphs, DAGs, partial orders, scheduling | [[dags-and-partial-orders]] |
| 11–12 | Simple graphs, matching, coloring, trees, planarity | [[graph-theory-basics]], [[stable-matching]] |
| 13 | Sums, approximating sums, asymptotic notation | [[asymptotic-notation]], [[recurrences]] |
| 14 | Counting rules, pigeonhole, inclusion–exclusion | [[counting-rules]], [[pigeonhole-principle]] |
| 15 | Generating functions, linear recurrences | [[recurrences]] |
| 16–19 | Probability spaces, conditional probability, random variables, deviation | [[four-step-method]], [[concentration-inequalities]] |

## Notable claims & quotes
- "A proof is an essay, not a calculation." Avoid "clearly"/"obviously"; go on alert when you see them.
- Any strong-induction proof can be mechanically rewritten as ordinary induction or as a well-ordering
  proof — the choice is about communication, not power.
- On big-O: "being asymptotically faster does not mean that it is a better choice" (the O(n^2.55)
  multiplication is "almost never used in practice").

## What it adds
First source ingested; it seeds most §1.1 concept pages. Its CS framing (invariants, DAG scheduling,
RSA as a number-theory payoff) makes it a better anchor for programmers than a pure-math discrete text.

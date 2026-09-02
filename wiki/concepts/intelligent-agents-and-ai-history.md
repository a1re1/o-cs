---
title: Intelligent agents and the history of AI — Turing's imitation game and objections, the Dartmouth proposal, symbolic AI (GPS, means–ends analysis, expert systems), knowledge representation and logical agents, classical planning (STRIPS, delete relaxation), Pearl's probabilistic turn, AI winters, the statistical and deep-learning eras, and the rational-agent framework with PEAS and environment types
type: concept
section: "6.1"
level: 300
tags: [agents, rational-agent, peas, environment-types, fully-observable, partially-observable, deterministic, stochastic, episodic, sequential, static, dynamic, discrete, continuous, multiagent, agent-architectures, reflex-agent, model-based, goal-based, utility-based, learning-agent, hierarchical-control, turing-test, imitation-game, turing-1950, lovelace-objection, dartmouth-1956, mccarthy, minsky, newell-simon, gps, means-ends-analysis, physical-symbol-system, expert-systems, mycin, knowledge-representation, logical-agents, propositional-logic, first-order-logic, resolution, planning, strips, pddl, delete-relaxation, plan-graph, pearl, ai-winter, statistical-ai, deep-learning-era, symbol-grounding]
sources: [ai-intro-courses-texts-and-seminal-papers]
summary: AI as taught today is organized around rational agents — an agent perceives an environment through sensors and acts to maximize expected performance (PEAS: performance measure, environment, actuators, sensors), and the environment's properties (observable or partial, deterministic or stochastic, episodic or sequential, static or dynamic, discrete or continuous, single or multi-agent, known or unknown) dictate the architecture from reflex to model-based to goal-based to utility-based and learning agents; historically the field began with Turing's 1950 replacement of "can machines think?" by the imitation game (with his rebuttals to the mathematical, consciousness, and Lady Lovelace objections and his proposal to educate a "child machine"), the 1955 Dartmouth proposal that coined "artificial intelligence" and conjectured that every feature of intelligence can be described precisely enough to simulate, the symbolic era (Newell & Simon's Logic Theorist and GPS with means–ends analysis, the physical symbol system hypothesis, Minsky's "Steps", expert systems such as MYCIN and DENDRAL, knowledge representation with logic and frames, STRIPS planning), two AI winters when brittleness and scaling failed to match the promises, Pearl's probabilistic turn (Bayesian networks, causality), the statistical/machine-learning era of the 1990s–2000s, and the deep-learning era from 2012 that ended in large language models — with the recurring lessons that search plus knowledge plus learning each need the others, and that the Lovelace and symbol-grounding debates never went away.
---
# Intelligent agents and the history of AI

**In one sentence.** An agent is anything that maps percept histories to actions, a rational
agent picks the action expected to maximize its performance measure, and AI's history is the
succession of ways to build that mapping — logic, search, knowledge, probability, learning —
each of which turned out to need the others.

## The agent framework (AIMA ch. 1–2; Poole & Mackworth ch. 1–2)
**Agent** = architecture + program; **rational** = acts to maximize expected performance
given the percept sequence and built-in knowledge (not omniscient, not perfect — rationality
is about expected, not actual, outcomes; information gathering and learning are rational).
**PEAS** specification (taxi: performance = safe/fast/legal/profit; environment = roads,
traffic; actuators = steering, brakes; sensors = cameras, GPS). **Environment types** decide
the method: fully vs **partially observable** (need belief states — [[bayesian-networks-and-hmms]]),
deterministic vs **stochastic** ([[markov-decision-processes]]), episodic vs **sequential**,
static vs **dynamic** (real-time — [[real-time-scheduling]]), discrete vs continuous, single
vs **multi-agent** (competitive — [[adversarial-search-and-game-trees]]; cooperative —
[[game-theory]]), known vs unknown (learning). **Architectures**: simple reflex
(condition–action rules; fail under partial observability), **model-based reflex** (internal
state + transition model), **goal-based** (search and planning — [[search-algorithms-ai]]),
**utility-based** (expected utility under uncertainty), **learning agents** (critic, learning
element, performance element, problem generator — [[machine-learning-basics]]); Poole &
Mackworth's **hierarchical control** (layers at different time scales, from reflexes to
deliberation — Brooks' subsumption in [[robotics-and-autonomous-systems]]) and their
"dimensions of complexity" (modularity, planning horizon, representation, computational
limits, learning, uncertainty in sensing/effects, preferences, number of agents, interaction
mode) as a map of the field.

## Turing 1950 and Dartmouth 1955
**Turing**: "Can machines think?" is too vague — replace it with the **imitation game**: an
interrogator communicating by teletype must tell the machine from a human; the game "draws a
fairly sharp line between the physical and the intellectual capacities". He defines the
digital computer as a universal discrete-state machine (any such machine can mimic any
other — [[turing-machines]]), predicts machines with 10⁹ bits of storage would play the game
well by 2000 (memory right, timeline wrong), and rebuts objections: theological,
"heads in the sand", the **mathematical objection** (Gödel/halting — humans err too,
[[computability-and-halting-problem]]), consciousness (solipsism cuts both ways),
"disabilities", **Lady Lovelace's** ("the Analytical Engine has no pretensions to originate
anything" — machines surprise us; learning machines act beyond their programming),
continuity of the nervous system, informality of behaviour, ESP. His constructive proposal —
build a **child machine** and educate it with rewards and punishments — is the learning
program of §6.2–6.6. **Dartmouth** (McCarthy, Minsky, Rochester, Shannon; summer 1956): the
name "artificial intelligence"; the conjecture that "every aspect of learning or any other
feature of intelligence can in principle be so precisely described that a machine can be
made to simulate it"; agenda: automatic computers, programming a computer to use language,
neuron nets, **theory of the size of a calculation** (efficiency criteria — a decade before
[[complexity-classes]]), self-improvement, abstractions, randomness and creativity. Sixty
years later the list reads as the field's table of contents.

## The symbolic era (1956–1980s)
Newell, Shaw & Simon's **Logic Theorist** (1956, proved *Principia* theorems) and **GPS**
(1959): **means–ends analysis** — pick an operator that reduces the difference between the
current state and the goal; recursively make its preconditions true — and the **physical
symbol system hypothesis** (symbol manipulation is necessary and sufficient for intelligence).
Minsky's "Steps Toward Artificial Intelligence" (1961) surveyed search, pattern recognition,
learning, planning, induction. Samuel's checkers (learned evaluation — [[adversarial-search-and-game-trees]]).
McCarthy's Lisp (1958 — [[higher-order-functions]]) and the Advice Taker (knowledge in
logic). **Knowledge representation & logical agents** (AIMA ch. 7–10): propositional and
first-order logic, entailment, model checking (truth tables, DPLL — [[sat-and-smt-solvers]]),
**resolution** (Robinson 1965; complete refutation procedure — [[first-order-logic]]), forward/
backward chaining on Horn clauses (Prolog — [[logic-programming]]), the wumpus world; frames,
semantic networks, description logics and ontologies ([[knowledge-graphs-and-ontologies]]);
the **frame problem** (what doesn't change) and situation calculus. **Expert systems**:
DENDRAL (1965), **MYCIN** (1970s — ~450 rules with certainty factors, matched specialists),
XCON at DEC; knowledge engineering as a bottleneck. **Classical planning** (AIMA ch. 11):
**STRIPS** (Fikes & Nilsson 1971 — states as sets of literals; actions with preconditions,
add and delete lists; Shakey the robot) and PDDL; planning as search with
domain-independent heuristics from the **delete relaxation** (ignore delete lists → relaxed
plan length, h_add/h_max/h_FF), **planning graphs** (Graphplan 1995, mutexes), planning as
SAT (SATPlan), partial-order planning, hierarchical task networks; the connection to
[[search-algorithms-ai]] and [[constraint-satisfaction-problems]].

## Winters, the probabilistic turn, and learning (1970s–2010s)
**AI winters** (1974–80 after the Lighthill report and perceptron limits — Minsky & Papert
1969; 1987–93 after the expert-system/Lisp-machine bust): brittleness, combinatorial
explosion, lack of learning, funding collapse. Responses: **Pearl's** *Heuristics* (1984) put
search on a mathematical footing and *Probabilistic Reasoning* (1988) replaced ad hoc
certainty factors with **Bayesian networks** — probability as the language of uncertainty,
with conditional independence making it tractable ([[bayesian-networks-and-hmms]]); decision
theory and MDPs for acting; Brooks' behaviour-based robotics (1986, "intelligence without
representation"). The **statistical era** (1990s–2000s): learning from data (backprop
revived 1986, SVMs, boosting, graphical models, HMM speech recognition, statistical MT —
[[machine-learning-basics]], [[nlp-fundamentals]]); Deep Blue 1997; the DARPA Grand Challenge
2005 (Stanley — probabilistic robotics). The **deep-learning era** (2012–): AlexNet, then
AlphaGo (2016), transformers (2017), GPT-3 (2020) and LLMs — the "child machine" educated on
the internet ([[deep-learning-basics]], [[transformers-and-attention]], [[large-language-models]]);
AIMA 4e adds chapters on safety and ethics ([[ai-safety-and-alignment]]).

## Perennial debates
Turing test as a criterion (Searle's Chinese room; ELIZA and Loebner-prize gaming; LLMs
passing versions of it in 2024 while the question moved to capability benchmarks);
**symbol grounding**; strong vs weak AI; neat vs scruffy; symbolic vs connectionist (now
neurosymbolic); the Lovelace objection reborn as "stochastic parrots"; and the "bitter
lesson" (Sutton 2019: general methods that leverage computation win over hand-coded
knowledge — search and learning) versus the persistent need for structure (Bayes nets, MCTS,
planning) inside learned systems.

## Related
- [[search-algorithms-ai]], [[constraint-satisfaction-problems]],
  [[adversarial-search-and-game-trees]], [[markov-decision-processes]],
  [[bayesian-networks-and-hmms]], [[turing-machines]], [[computability-and-halting-problem]],
  [[first-order-logic]], [[logic-programming]], [[sat-and-smt-solvers]],
  [[machine-learning-basics]], [[large-language-models]], [[ai-safety-and-alignment]],
  [[robotics-and-autonomous-systems]], [[game-theory]].

## Sources
Turing 1950 (§1–2 read in full, objections from memory); Dartmouth proposal 1955 (read); AIMA 4e ch. 1–2, 7–11; Poole & Mackworth ch. 1–2, 19; Minsky 1961; Newell & Simon 1959/1976 (physical symbol system); Fikes & Nilsson 1971 (STRIPS); Pearl 1988; Sutton 2019 (bitter lesson).

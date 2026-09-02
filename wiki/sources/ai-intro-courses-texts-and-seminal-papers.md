---
title: Introduction to AI — Berkeley CS188, Harvard CS50 AI, MIT 6.034, Stanford CS221; Russell & Norvig's AIMA and Poole & Mackworth's Foundations of Computational Agents (free); Turing 1950, the Dartmouth proposal (1955), Minsky's "Steps" (1961), Newell & Simon's GPS, Hart–Nilsson–Raphael A* (1968), Pearl's Heuristics and Bayesian networks
type: source
section: "6.1"
level: 300
tags: [cs188, cs50-ai, 6-034, cs221, aima, russell-norvig, poole-mackworth, artint, turing-test, imitation-game, dartmouth, mccarthy, minsky, shannon, rochester, newell-simon, gps, a-star, hart-nilsson-raphael, pearl, heuristics, bayesian-networks, pacman]
sources: []
authors: [Stuart Russell, Peter Norvig, David Poole, Alan Mackworth, Alan Turing, John McCarthy, Marvin Minsky, Nathaniel Rochester, Claude Shannon, Allen Newell, Herbert Simon, Peter Hart, Nils Nilsson, Bertram Raphael, Judea Pearl]
year: 1950
institution: UC Berkeley / Stanford / MIT
url: https://artint.info/3e/html/ArtInt3e.html
license: mixed (CS188 materials and Poole & Mackworth free; AIMA commercial)
format: html
summary: Berkeley CS188 is the canonical intro-AI course (Pacman projects; lectures follow AIMA 4e — uninformed search, A* and heuristics, CSPs, game trees with minimax/expectimax and utilities, MDPs, reinforcement learning, Bayes nets with variable elimination and sampling, HMMs and particle filters, decision networks and VPI, machine learning, neural nets); Russell & Norvig's AIMA (1995, 4e 2020) organizes AI around rational agents; Poole & Mackworth (3e 2023, free) organize it as computational agents in seven parts (agents; reasoning and planning with certainty — search, constraints, propositions, deterministic planning; learning and reasoning with uncertainty — supervised learning, neural nets, reasoning with uncertainty, causality; planning and acting with uncertainty — MDPs, RL, multiagent; individuals and relations — knowledge graphs, relational learning; social impact); the seminal papers are Turing's 1950 "Computing Machinery and Intelligence" (replacing "can machines think?" with the imitation game and rebutting nine objections), the 1955 Dartmouth proposal (McCarthy, Minsky, Rochester, Shannon: "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it", with agenda items automatic computers, language, neuron nets, theory of the size of a calculation, self-improvement, abstractions, randomness and creativity), Minsky's "Steps Toward Artificial Intelligence", Newell & Simon's General Problem Solver (means–ends analysis), the A* paper (admissible heuristics, optimality), and Pearl's Heuristics (1984) and Bayesian networks (1988).
---
# Introduction to AI: courses, texts, and seminal papers

## What they are
- **Berkeley CS188** (Abbeel, Klein, Russell, Dragan, Stuart, … — fully open with Pacman
  projects): 1 intro; 2 uninformed search; 3 A* and heuristics; 4–5 CSPs; 6–7 game trees
  (minimax, expectimax, utilities); 8–9 MDPs; 10–11 reinforcement learning; 12–14 Bayes
  nets (representation, independence, variable elimination, sampling); 15–16 HMMs and
  particle filters; 17 decision networks and value of perfect information; 18–20 machine
  learning (naive Bayes, perceptrons, logistic regression, optimization); 21–22 neural
  networks; guest lectures on ethics/policy. Readings map to AIMA 4e chapters 1–6, 12–17,
  19–21.
- **Russell & Norvig, AIMA** (4e 2020): I foundations (agents); II problem solving (search,
  adversarial, CSPs); III knowledge and reasoning (logic, planning); IV uncertain knowledge
  (probability, Bayes nets, temporal models, decisions, MDPs, multiagent); V learning; VI
  communicating/perceiving/acting; VII philosophy, ethics, safety. The rational-agent frame
  ("do the right thing" = maximize expected utility) organizes everything.
- **Poole & Mackworth, AI: Foundations of Computational Agents** (3e 2023, free HTML): Part I
  agents in the world (agents; architectures and hierarchical control); II reasoning and
  planning with certainty (searching for solutions; reasoning with constraints; propositions
  and inference; deterministic planning); III learning and reasoning with uncertainty
  (supervised ML; neural networks and deep learning; reasoning with uncertainty; learning
  with uncertainty; causality); IV planning and acting with uncertainty (planning with
  uncertainty; RL; multiagent systems); V individuals and relations (knowledge graphs and
  ontologies; relational learning); VI social impact; retrospect and prospect; appendix
  mapping to open-source packages. Distinctive for its dimensions-of-complexity framing
  (modularity, planning horizon, representation, computational limits, learning, uncertainty,
  preferences, number of agents, interaction).
- **Harvard CS50 AI** (search, knowledge, uncertainty, optimization, learning, neural nets,
  language — project-based); **MIT 6.034** (Winston: rule-based systems, search, games,
  constraints, learning — recorded); **Stanford CS221** (search, MDPs, games, CSPs, Bayes
  nets, logic; Liang/Sadigh).
- **Seminal**: Turing 1950 ("Can machines think?" replaced by the imitation game; the
  digital computer as a universal discrete-state machine; nine objections — theological,
  heads-in-the-sand, mathematical (Gödel), consciousness, disabilities, Lady Lovelace's
  ("the machine can only do what we tell it"), continuity of the nervous system,
  informality of behaviour, ESP — and the "child machine" learning proposal that anticipates
  ML); Dartmouth 1955 (the term "artificial intelligence"; the conjecture that intelligence
  can be precisely described and simulated; agenda incl. "theory of the size of a
  calculation" — an early complexity theory — and self-improvement); Minsky 1961 (search,
  pattern recognition, learning, planning, induction — the field's first survey); Newell &
  Simon's GPS (1959: means–ends analysis, difference reduction — the physical symbol system
  hypothesis); Hart, Nilsson & Raphael 1968 (A*: f = g + h with admissible h is optimal and
  optimally efficient); Pearl 1984 *Heuristics* (analysis of heuristic search) and 1988
  *Probabilistic Reasoning in Intelligent Systems* (Bayesian networks: conditional
  independence as the organizing principle for uncertainty — the turn from logic to
  probability that defines modern AI).

## Key ideas → pages
[[search-algorithms-ai]], [[constraint-satisfaction-problems]],
[[adversarial-search-and-game-trees]], [[markov-decision-processes]],
[[bayesian-networks-and-hmms]], [[intelligent-agents-and-ai-history]].

## What they add
CS188 for the problem sets (Pacman as a unifying testbed for search, games, MDPs, RL,
tracking), AIMA for breadth and the agent frame, Poole & Mackworth for a free, rigorous,
modern (causality, knowledge graphs, social impact) treatment; Turing and Dartmouth for how
the questions were first posed and how little the framing has changed.

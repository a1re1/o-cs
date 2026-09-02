---
title: Markov chains, stationary distributions, and MCMC
type: concept
section: "1.4"
level: 300
tags: [markov-chains, transition-matrix, stationary-distribution, irreducible, aperiodic, mixing-time, detailed-balance, reversibility, first-step-analysis, random-walks, mcmc, metropolis-hastings, gibbs-sampling, pagerank]
sources: [blitzstein-stat110, mcs-lehman-leighton-meyer, cs109-probability-for-computer-scientists]
summary: A memoryless process on states with a transition matrix; irreducible aperiodic finite chains converge to a unique stationary distribution π = πP from any start; hitting times come from first-step analysis; and MCMC inverts the picture by designing a chain (Metropolis–Hastings, Gibbs) whose stationary distribution is the one you want to sample.
---
# Markov chains and MCMC

**In one sentence.** P(X_{n+1} = j | X_n = i, history) = P_ij: the future depends on the present
only, so long-run behaviour is linear algebra on the transition matrix P.

## Core facts (finite state space)
- Row-stochastic P (rows sum to 1); n-step transitions are Pⁿ; distribution evolves as row vector
  μ_{n+1} = μ_n P.
- **Stationary distribution** π: πP = π (left eigenvector, eigenvalue 1 — [[eigenvalues-and-eigenvectors]]).
  Exists for every finite chain; **unique** if irreducible (every state reaches every other); the chain
  **converges** to π from any start if also aperiodic (gcd of cycle lengths = 1). Convergence rate is
  governed by the second eigenvalue |λ₂| — the **spectral gap** 1 − |λ₂| controls the mixing time.
- π_i = 1/(expected return time to i). Ergodic theorem: time averages → π.
- **Reversible** chains satisfy detailed balance π_i P_ij = π_j P_ji; a π satisfying detailed balance
  is automatically stationary (the trick behind MCMC). Random walk on an undirected graph is reversible
  with π_v ∝ deg(v).
- **First-step analysis** for hitting/absorption: h_i = 1 + Σ_j P_ij h_j (expected steps), solve the
  linear system ([[random-variables-expectation]]). Gambler's ruin: from i of N with fair coin, P(win) =
  i/N, expected duration i(N−i). Symmetric random walk on Z: recurrent in 1-D and 2-D, transient in 3-D.

## Applications
- **PageRank**: random surfer with teleportation probability 1−d; π is the rank; the teleport step
  makes the chain irreducible & aperiodic so power iteration converges ([[pagerank]]).
- Queueing (birth–death chains), reliability, cache behaviour, language n-gram models, hidden Markov
  models (§6.1, §11.3), reinforcement learning's MDPs (§6.6) add actions and rewards.

## MCMC (Blitzstein ch. 12)
Goal: sample from a target π known only up to a constant (a Bayesian posterior). Build a chain with
stationary distribution π:
- **Metropolis–Hastings**: from x propose x′ ~ q(x′|x); accept with probability
  min(1, π(x′)q(x|x′) / (π(x)q(x′|x))); otherwise stay. Detailed balance holds by construction; the
  normalizer cancels.
- **Gibbs sampling**: update one coordinate at a time from its exact conditional (a special case with
  acceptance 1). Needs tractable conditionals — the workhorse for graphical models (§6.7).
- Practice: burn-in, thinning is mostly unnecessary, diagnose mixing with trace plots / R̂ / effective
  sample size; Hamiltonian Monte Carlo (NUTS) for continuous high-dimensional targets.

## Pitfalls
- Periodic chains (bipartite random walks) oscillate and never converge though π exists — add laziness
  (stay with prob 1/2).
- Reducible chains have many stationary distributions; the limit depends on the start.
- MCMC samples are correlated; naive standard errors are too small.

## Related
- [[eigenvalues-and-eigenvectors]], [[pagerank]], [[bayes-theorem-and-inference]], [[common-distributions]].

## Sources
Blitzstein ch. 11–12; MCS ch. 20 (random walks) and 20.x (Markov matrices/PageRank); CS109 "General Inference" (rejection sampling, Gibbs).

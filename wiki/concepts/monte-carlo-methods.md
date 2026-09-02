---
title: Monte Carlo methods — Monte Carlo estimation and its 1/√N error, inverse-transform and rejection sampling, importance sampling (and its variance blow-up in high dimensions), Markov chain Monte Carlo (Metropolis–Hastings, Gibbs sampling, detailed balance and ergodicity), Hamiltonian Monte Carlo and NUTS, convergence diagnostics (trace plots, R̂, effective sample size, autocorrelation), sequential Monte Carlo and particle filters, simulated annealing, and randomized algorithms' use of sampling
type: concept
section: "6.7"
level: 500
tags: [monte-carlo, sampling, monte-carlo-integration, law-of-large-numbers, variance, standard-error, inverse-transform, rejection-sampling, importance-sampling, effective-sample-size, weight-degeneracy, mcmc, markov-chain-monte-carlo, metropolis-hastings, acceptance-ratio, proposal, random-walk, gibbs-sampling, detailed-balance, stationary-distribution, ergodicity, mixing, burn-in, thinning, hamiltonian-monte-carlo, hmc, leapfrog, nuts, no-u-turn, stan, diagnostics, trace-plot, r-hat, gelman-rubin, autocorrelation, sequential-monte-carlo, particle-filter, resampling, simulated-annealing, slice-sampling, quasi-monte-carlo, variance-reduction, control-variates, antithetic, randomized-algorithms, metropolis-1953]
sources: [pgm-and-bayesian-texts-courses-and-seminal-papers]
summary: Monte Carlo estimates an expectation E_p[f] by averaging f over samples from p, with error O(σ/√N) regardless of dimension — the reason it beats quadrature beyond a few dimensions and the reason it is slow to converge; when p can be sampled directly use inverse transform or rejection sampling, when it cannot, importance sampling reweights samples from a proposal q by p/q (unbiased, but the weights' variance explodes when q misses p's mass — effective sample size collapses in high dimensions), and MCMC constructs a Markov chain whose stationary distribution is p: Metropolis–Hastings proposes x′ ~ q(·|x) and accepts with probability min(1, p(x′)q(x|x′)/(p(x)q(x′|x))) (only p up to a constant is needed — the partition function cancels), Gibbs sampling resamples one variable from its full conditional (always accepted; needs only Markov blankets), detailed balance plus ergodicity guarantee convergence but say nothing about how long mixing takes, and Hamiltonian Monte Carlo uses gradients of log p to simulate Hamiltonian dynamics (leapfrog integrator, momentum resampling) for distant proposals with high acceptance, made automatic by NUTS (adaptive trajectory length and step size) in Stan/PyMC; practice is diagnostics — multiple chains, trace plots, R̂ ≈ 1, effective sample size accounting for autocorrelation, divergences in HMC — plus sequential Monte Carlo/particle filters for online state estimation, simulated annealing (MCMC with a cooling temperature) for optimization, and variance reduction (control variates, antithetic, stratified, quasi-Monte Carlo) when samples are expensive; the same sampling toolkit underlies randomized algorithms, Bayesian inference, physics simulation, rendering, and RL's policy gradients.
---
# Monte Carlo methods

**In one sentence.** Replace an integral you can't do with an average over samples you can
draw — directly, by reweighting a wrong distribution (importance sampling), or by running
a Markov chain whose equilibrium is the right one (MCMC) — and spend your effort on
knowing whether the chain has actually equilibrated.

## Monte Carlo estimation (MacKay ch. 29; CS228 sampling)
E_p[f(x)] ≈ (1/N) Σ f(x⁽ⁱ⁾), x⁽ⁱ⁾ ~ p; unbiased, variance Var(f)/N, standard error σ/√N — the
**dimension-independent** √N rate ([[concentration-inequalities]], [[probability-and-statistics-for-cs]]).
Beats deterministic quadrature (error N^{−k/d}) beyond d ≈ 4–6; π by dart-throwing,
option pricing, integrals in Bayesian inference (posterior means, predictive
distributions — [[bayesian-inference]]), rendering (path tracing — [[computer-graphics-rendering]]),
particle physics. **Variance reduction**: control variates (subtract a correlated function
with known mean), antithetic pairs, stratification, **quasi-Monte Carlo** (low-discrepancy
sequences: O((log N)^d/N)), Rao-Blackwellization (integrate analytically what you can).
Generating samples: pseudo-random generators ([[pseudorandomness-and-derandomization]]), **inverse
transform** (x = F⁻¹(u)), Box–Muller, **rejection sampling** (sample from q ≥ p/M, accept with
probability p/(Mq) — acceptance rate 1/M collapses exponentially in dimension), and
**importance sampling**: E_p[f] = E_q[f p/q] ≈ Σ wᵢ f(xᵢ)/Σ wᵢ with wᵢ = p(xᵢ)/q(xᵢ)
(self-normalized when p is unnormalized); variance is finite only if q's tails cover p's;
the **effective sample size** (Σw)²/Σw² diagnoses **weight degeneracy** — in high dimensions
one weight dominates. Likelihood weighting in Bayes nets is IS with the prior as q
([[bayesian-networks-and-hmms]]); off-policy RL uses IS ratios ([[reinforcement-learning-basics]]).

## MCMC: Metropolis–Hastings and Gibbs (Metropolis 1953; Hastings 1970; Geman & Geman 1984)
Build a **Markov chain** ([[markov-chains]]) with transition T whose **stationary distribution**
is p — sufficient: **detailed balance** p(x)T(x → x′) = p(x′)T(x′ → x) — and that is **ergodic**
(irreducible, aperiodic), so the chain converges to p from any start and time averages equal
expectations. **Metropolis–Hastings**: propose x′ ~ q(x′ | x); accept with probability
α = min{1, [p(x′) q(x | x′)] / [p(x) q(x′ | x)]}, else stay. Only the *ratio* p(x′)/p(x) is
needed — unnormalized densities suffice (posteriors ∝ prior × likelihood; MRFs without Z —
[[probabilistic-graphical-models]]). Random-walk Metropolis (symmetric Gaussian proposal):
step size trades acceptance against distance (optimal acceptance ≈ 0.234 in high d); the
chain explores by diffusion, so mixing time scales badly with dimension and with
correlated coordinates. **Gibbs sampling**: cycle through variables, sampling each from its
**full conditional** p(xᵢ | x₋ᵢ) — a MH move with acceptance 1; needs only the Markov blanket,
so it's natural on graphical models (Bayes nets, Ising models, LDA's collapsed Gibbs);
fails when variables are strongly coupled (blocked Gibbs, auxiliary variables, Swendsen–
Wang for Ising). Other samplers: independence MH, slice sampling (no tuning), Metropolis-
adjusted Langevin, reversible-jump (model dimension changes), tempering/parallel tempering
(multimodality — the hardest case for all of MCMC), simulated annealing (p^{1/T} with T ↓ 0:
optimization — [[search-algorithms-ai]]; Geman & Geman for MAP on MRFs). Theory: mixing
times via spectral gap/conductance ([[markov-chains]]); exact sampling by coupling from the
past (Propp–Wilson).

## Hamiltonian Monte Carlo and NUTS (Neal 2011; Hoffman & Gelman 2014)
Augment x with momentum r ~ N(0, M); H(x, r) = −log p(x) + ½ rᵀM⁻¹r; simulate Hamiltonian
dynamics with the **leapfrog** integrator (L steps of size ε, using ∇ log p — autodiff makes
this free, [[deep-learning-basics]]), then MH-accept with the energy error (leapfrog is
volume-preserving and reversible, so the acceptance is min(1, exp(−ΔH)) ≈ 1). Trajectories
travel far along the typical set in O(d^{1/4}) steps vs random walk's O(d): the method that
made Bayesian inference in hundreds–thousands of dimensions routine. Tuning ε, L is hard →
**NUTS**: build the trajectory forward and backward by doubling until it makes a U-turn,
sample a point from it (multinomial/slice), adapt ε during warm-up to a target acceptance
(~0.8) and M from the warm-up variance — the default in **Stan**, PyMC, NumPyro. Limits:
continuous variables only (marginalize discrete ones), one mode per chain, cost per
iteration = gradient of the full log-posterior (minibatch variants — SGLD/SGHMC — are
approximate). **Divergent transitions** flag regions the integrator can't follow (funnels
in hierarchical models — reparameterize).

## Diagnostics and practice (BDA3 ch. 11–12; Stan manual)
MCMC gives correlated samples from a chain that may not have converged; you cannot prove
convergence, only detect its failure. Run ≥ 4 chains from dispersed starts; discard
**warm-up/burn-in**; **trace plots** (fuzzy caterpillars, chains overlapping); **R̂** (Gelman–Rubin:
between-chain/within-chain variance ratio; want < 1.01); **effective sample size** N_eff =
N/(1 + 2Σ autocorrelations) per quantity (want ≥ 100s; bulk and tail ESS); Monte Carlo
standard error = σ/√N_eff; thinning wastes information (keep all samples unless memory-
bound); posterior predictive checks for model fit ([[bayesian-inference]]). Cost model:
wall-clock per effective sample is the metric — a fast poorly-mixing sampler loses to a
slow HMC.

## Sequential Monte Carlo
**Particle filters** for state-space models: propagate N weighted particles through the
transition, reweight by the likelihood, **resample** when ESS drops (bootstrap filter /
sequential importance resampling); particle degeneracy vs impoverishment; Rao-Blackwellized
PFs (FastSLAM); the same machinery filters robots ([[state-estimation-and-kalman-filters]],
[[bayesian-networks-and-hmms]]), tracks in vision, and estimates marginal likelihoods
(SMC samplers over tempered distributions; particle MCMC).

## Randomized algorithms and Monte Carlo elsewhere
"Monte Carlo" algorithms (probably correct, always fast — Miller–Rabin primality,
Karger's min cut, polynomial identity testing) vs "Las Vegas" (always correct, probably
fast — randomized quicksort) — [[randomized-algorithms]], [[pseudorandomness-and-derandomization]];
random sampling for approximate counting (#P problems via MCMC — Jerrum–Sinclair's
permanent, volume estimation: the theoretical triumph of MCMC), streaming sketches,
and property testing. In ML: dropout/SGD noise, MC dropout uncertainty, REINFORCE's
score-function estimator vs the reparameterization trick (pathwise gradients — [[variational-inference]]),
Monte Carlo tree search ([[adversarial-search-and-game-trees]]), and evaluation by
bootstrap resampling ([[hypothesis-testing-and-confidence-intervals]]).

## Pitfalls
- Importance sampling with a proposal narrower than the target (infinite-variance
  weights); trusting a single dominant weight.
- One chain, no R̂, no ESS; declaring convergence from a smooth trace.
- Random-walk Metropolis in 100 dimensions; Gibbs on highly correlated variables.
- Ignoring HMC divergences; running NUTS on a model with discrete latents un-marginalized.
- Thinning to "reduce autocorrelation" instead of running longer; reporting N instead of
  N_eff.
- Multimodal posteriors sampled by one chain that never leaves its mode.

## Related
- [[markov-chains]], [[probability-and-statistics-for-cs]], [[concentration-inequalities]],
  [[bayesian-inference]], [[variational-inference]], [[probabilistic-graphical-models]],
  [[bayesian-networks-and-hmms]], [[randomized-algorithms]], [[pseudorandomness-and-derandomization]],
  [[search-algorithms-ai]] (simulated annealing), [[state-estimation-and-kalman-filters]],
  [[reinforcement-learning-basics]], [[adversarial-search-and-game-trees]],
  [[computer-graphics-rendering]], [[hypothesis-testing-and-confidence-intervals]],
  [[deep-learning-basics]].

## Sources
MacKay ch. 29–30; CS228 sampling notes (read); BDA3 ch. 10–12; Metropolis et al. 1953; Hastings 1970; Geman & Geman 1984; Neal 2011 ("MCMC using Hamiltonian dynamics"); Hoffman & Gelman 2014; Betancourt 2017 (conceptual HMC); Vehtari et al. 2021 (R̂/ESS); Doucet et al. 2001 (SMC); Robert & Casella, *Monte Carlo Statistical Methods*.

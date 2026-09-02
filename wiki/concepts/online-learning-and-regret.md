---
title: Online learning and regret — prediction with expert advice (Halving, Weighted Majority, Hedge/exponential weights and its O(√(T ln N)) regret), the perceptron and Winnow mistake bounds, online convex optimization (online gradient descent, follow-the-regularized-leader, mirror descent, AdaGrad), online-to-batch conversion, the minimax theorem via no-regret dynamics, adversarial bandits, and the connections to boosting, game theory, and stochastic optimization
type: concept
section: "6.8"
level: 500
tags: [online-learning, regret, no-regret, experts, prediction-with-expert-advice, halving-algorithm, weighted-majority, hedge, exponential-weights, multiplicative-weights, mistake-bound, perceptron-mistake-bound, novikoff, winnow, littlestone-dimension, online-convex-optimization, oco, online-gradient-descent, ogd, follow-the-leader, ftl, follow-the-regularized-leader, ftrl, mirror-descent, adagrad, strongly-convex, log-regret, online-to-batch, sgd, minimax-theorem, zero-sum-games, no-regret-dynamics, nash, correlated-equilibrium, adversarial-bandits, exp3, boosting-as-game, adaboost-hedge, calibration, cesa-bianchi-lugosi, shalev-shwartz-oco]
sources: [learning-theory-texts-courses-and-seminal-papers]
summary: Online learning drops the i.i.d. assumption entirely — an adversary reveals examples one at a time, the learner predicts, then sees the loss — and measures performance by regret, the excess cumulative loss over the best fixed competitor in hindsight; the fundamental result is that sublinear regret is achievable against any sequence: with N experts, the Halving algorithm makes ≤ log₂ N mistakes if one expert is perfect, Weighted Majority ≤ 2.4(m + log₂ N) if the best makes m, and the randomized Hedge/exponential-weights algorithm (weight each expert by e^{−η·cumulative loss}, play proportionally) has regret ≤ √(T ln N / 2) — a bound that is tight and requires randomization (deterministic learners suffer linear regret against adaptive adversaries); the perceptron makes at most (R/γ)² mistakes on γ-separable data (Novikoff), Winnow's multiplicative updates make O(k log d) mistakes when only k features matter, and the Littlestone dimension characterizes online learnability the way VC does batch; online convex optimization generalizes everything — online gradient descent has O(√T) regret for convex Lipschitz losses and O(log T) for strongly convex ones, follow-the-regularized-leader and mirror descent (Hedge is FTRL with entropic regularization) adapt the geometry, AdaGrad adapts per coordinate — and online-to-batch conversion turns any low-regret algorithm into a statistical learner (SGD is online gradient descent averaged over a random sample, which is why SGD's excess risk is O(1/√T)); the same machinery proves the minimax theorem (two no-regret players' average strategies converge to a Nash equilibrium of a zero-sum game — and to correlated equilibria in general games), yields boosting (AdaBoost is Hedge played against a weak learner), handles bandit feedback (Exp3), and underlies calibration and sequential prediction.
---
# Online learning and regret

**In one sentence.** Even against an adversary choosing the data, you can do almost as well
as the best fixed strategy in hindsight — exponential weights over experts, gradient
descent over convex losses — and that one guarantee produces SGD's rates, the minimax
theorem, and boosting as corollaries.

## The setting and regret (Cesa-Bianchi & Lugosi ch. 1–2; Shalev-Shwartz OCO survey; UML ch. 21)
Rounds t = 1..T: learner picks x_t (a prediction, a distribution over experts, a point in a
convex set), the adversary reveals loss ℓ_t, learner suffers ℓ_t(x_t). **Regret** R_T = Σ ℓ_t(x_t)
− min_{u} Σ ℓ_t(u) — against the best *fixed* u in hindsight (comparator class); goal R_T =
o(T) ("no-regret": average regret → 0). No distributional assumptions; **oblivious** vs
**adaptive** adversaries; deterministic learners can be forced to err every round (the
adversary sees x_t), so randomization is essential for 0–1 losses — and the guarantee is on
expected regret. Regret is not "being right": it's "not being much worse than the best
simple alternative", which is exactly the guarantee you want for data you can't model.

## Experts: Halving, Weighted Majority, Hedge (Littlestone & Warmuth 1994; Freund & Schapire 1997)
N experts predict; learner combines. **Halving** (realizable — some expert is perfect): predict
with the majority of consistent experts, discard the wrong ones — ≤ log₂ N mistakes.
**Weighted Majority**: halve the weight of each mistaken expert; mistakes ≤ 2.41(m* + log₂ N)
where m* is the best expert's count — a constant-factor guarantee, deterministic.
**Hedge / exponential weights / multiplicative weights**: w_{t+1,i} ∝ w_{t,i} e^{−η ℓ_{t,i}},
play expert i with probability p_{t,i} = w_{t,i}/Σw; regret ≤ ln N/η + ηT/8 → with η = √(8 ln N/T),
**R_T ≤ √(T ln N / 2)** — tight (matching lower bound); doubling trick or η_t = √(ln N/t) when T
is unknown; potential-function proof via log Σ w_t ([[convexity]]: log-sum-exp). The
**multiplicative weights** method is the same algorithm across CS: approximate LP/SDP
solving, Adaboost, the Plotkin–Shmoys–Tardos packing/covering framework, and derandomized
zero-sum game solving (Arora, Hazan & Kale 2012 — [[linear-programming-and-duality]],
[[approximation-algorithms]]). Tracking the best *shifting* expert (fixed-share), sleeping
experts, and prediction with side information (contextual experts) are the extensions.

## Mistake bounds: perceptron, Winnow, Littlestone dimension (Novikoff 1962; Littlestone 1988)
Online binary classification, count mistakes. **Perceptron** (w ← w + y x on a mistake):
if ∃ u with ‖u‖ = 1, y ⟨u, x⟩ ≥ γ and ‖x‖ ≤ R, mistakes ≤ (R/γ)² — dimension-free, margin-
dependent (the online ancestor of the SVM margin bound — [[statistical-learning-theory]]);
kernelized perceptron. **Winnow** (multiplicative updates on weights): for k-sparse target
disjunctions/halfspaces over d features, O(k log d) mistakes — exponentially better than
additive updates when the target is sparse; the additive-vs-multiplicative (ℓ₂ vs ℓ₁/entropy
geometry) distinction is mirror descent's whole story. **Littlestone dimension** Ldim(H): the
depth of the largest full binary "mistake tree" H can realize; the optimal deterministic
mistake bound in the realizable case is exactly Ldim (Standard Optimal Algorithm), and
randomized regret is Θ(√(T Ldim)) — the online analogue of VC (Ldim ≥ VC; thresholds on ℝ
have VC 1 and infinite Ldim, so online is strictly harder). Online learnability ⇔ finite
Ldim ⇔ (surprisingly) differential privacy of learning (Alon et al. 2019).

## Online convex optimization (Zinkevich 2003; Hazan's book; Shalev-Shwartz 2012)
Decision set K convex, losses f_t convex. **Online gradient descent** x_{t+1} = Π_K(x_t − η ∇f_t(x_t)):
regret ≤ D²/(2η) + η G² T/2 → **O(DG√T)** for G-Lipschitz losses on a set of diameter D;
**O((G²/λ) log T)** for λ-strongly convex losses with η_t = 1/(λt); exp-concave losses get log T
via Online Newton Step. **Follow-the-leader** (play the minimizer of past losses) can have
linear regret (oscillation) — fixed by **FTRL**: x_{t+1} = argmin Σ_{s≤t} f_s(x) + R(x)/η;
with R = ½‖x‖² it's lazy OGD, with the negative entropy it's **Hedge** — so experts and OCO are
one algorithm with different regularizers; **mirror descent** (Nemirovski–Yudin) is the
same with Bregman divergences, matching the geometry of K (entropy on the simplex gives
√(ln N) instead of √N). **AdaGrad** (Duchi, Hazan & Singer 2011): per-coordinate step sizes
from accumulated squared gradients — regret adapts to the gradient geometry (sparse
features) and is the origin of RMSProp/Adam ([[neural-network-training]]); optimistic/
adaptive variants exploit predictable sequences (faster rates for games). Lower bound:
Ω(√T) for Lipschitz convex losses — OGD is optimal in the worst case.

## Online-to-batch and stochastic optimization (Cesa-Bianchi, Conconi & Gentile 2004)
Given i.i.d. samples, run any online algorithm and output the average (or a random
iterate) x̄ = (1/T) Σ x_t: E[F(x̄)] − min F ≤ E[R_T]/T — so **SGD is OGD on stochastic
gradients** with excess risk O(1/√T) (O(log T / T) or O(1/T) with strong convexity) — the
statistical-learning rate derived *without* uniform convergence, holding for any convex
loss with one pass over the data ([[gradient-descent]]; UML's "SGD" and "convex learning"
chapters). Implications: single-pass SGD learns as well as ERM up to constants for convex
problems; regularization ≈ implicit through early stopping/averaging; the analysis of
SGD for deep nets borrows the stability view ([[statistical-learning-theory]]).

## Games, boosting, and bandits (Freund & Schapire 1996/1999; Mohri ch. 7–8; Cesa-Bianchi & Lugosi ch. 7)
**Minimax theorem via no-regret**: two players run Hedge against each other in a zero-sum
game; the average mixed strategies are an ε-**Nash equilibrium** after O(ln N/ε²) rounds —
a constructive proof of von Neumann's theorem and of LP duality (Freund & Schapire 1999 —
[[game-theory]], [[linear-programming-and-duality]]); in general-sum games, no-regret
(external regret) dynamics converge to the set of **coarse correlated equilibria**, no-
internal-regret to correlated equilibria — the learning-theoretic foundation of algorithmic
game theory and of self-play in RL/poker solvers (CFR — counterfactual regret minimization).
**Boosting**: AdaBoost is Hedge played by the "booster" over training examples against a
weak learner choosing hypotheses — the weights on examples are exponential weights on
losses; the training error bound e^{−2γ²T} and the margin explanation follow
([[decision-trees-and-ensembles]]). **Bandit feedback**: only the chosen action's loss is seen
— **Exp3** feeds Hedge importance-weighted estimates, regret O(√(TN ln N)) ([[multi-armed-bandits]]);
bandit convex optimization, partial monitoring. **Calibration and sequential prediction**:
no-regret forecasters can be made calibrated (Foster & Vohra), connecting to weather
forecasting, conformal prediction and the "prediction of individual sequences" program;
universal portfolios (Cover) are online learning in finance; online-to-offline
compression and the Lempel–Ziv connection ([[source-coding-and-compression]]).

## Pitfalls
- Deterministic prediction with 0–1 loss against an adaptive adversary (linear regret).
- Regret bounds read as accuracy: low regret against a weak comparator class says little.
- Follow-the-leader without regularization on linear losses (oscillation).
- Fixed η with unknown T (use the doubling trick or time-varying η); OGD without
  projection onto K.
- Online-to-batch on non-i.i.d. data (the conversion needs the sample to be random).

## Related
- [[statistical-learning-theory]], [[multi-armed-bandits]], [[gradient-descent]],
  [[convexity]], [[neural-network-training]] (AdaGrad → Adam),
  [[decision-trees-and-ensembles]] (boosting), [[game-theory]],
  [[linear-programming-and-duality]], [[approximation-algorithms]] (multiplicative weights),
  [[source-coding-and-compression]], [[concentration-inequalities]], [[machine-learning-basics]].

## Sources
Cesa-Bianchi & Lugosi 2006 ch. 1–4, 7; Shalev-Shwartz 2012 (*Online Learning and Online Convex Optimization*); Hazan 2016 (*Introduction to OCO*); UML ch. 14, 21; Mohri et al. ch. 7–8; Littlestone & Warmuth 1994; Freund & Schapire 1997, 1999; Novikoff 1962; Littlestone 1988; Zinkevich 2003; Duchi, Hazan & Singer 2011; Cesa-Bianchi, Conconi & Gentile 2004; Arora, Hazan & Kale 2012; Alon et al. 2019.

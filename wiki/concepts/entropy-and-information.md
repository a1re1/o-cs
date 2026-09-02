---
title: Entropy, mutual information, KL divergence, and cross-entropy
type: concept
section: "1.7"
level: 400
tags: [entropy, information-theory, mutual-information, kl-divergence, cross-entropy, conditional-entropy, chain-rule, jensen, data-processing-inequality, bits, perplexity]
sources: [shannon-1948, mackay-itila, cs109-probability-for-computer-scientists]
summary: H(X) = −Σ p log p is the average number of bits needed to describe X; conditional entropy, mutual information I(X;Y) = H(X) − H(X|Y), and KL divergence D(p‖q) ≥ 0 are the three derived quantities, with cross-entropy = H(p) + D(p‖q) explaining why cross-entropy loss and perplexity measure model quality.
---
# Entropy and information

**In one sentence.** Information is surprise: an outcome of probability p carries log₂(1/p) bits,
and entropy is the expected surprise — the irreducible cost of describing the source.

## Definitions (logs base 2 ⇒ bits; base e ⇒ nats)
- **Entropy** H(X) = −Σ_x p(x) log p(x) = E[log 1/p(X)]. 0 ≤ H ≤ log |X| with equality for uniform.
  Fair coin 1 bit; biased coin p = 0.1 gives 0.47 bits; English letters ≈ 4.1 bits by frequency, ≈ 1–1.5
  bits per letter accounting for context (Shannon's redundancy ≈ 50–75%).
- **Joint / conditional**: H(X, Y) = H(X) + H(Y|X) (chain rule); H(Y|X) ≤ H(Y) (conditioning never
  increases entropy on average).
- **Mutual information** I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X) = D(p(x,y) ‖ p(x)p(y)) ≥ 0;
  0 iff independent. Symmetric. Capacity is max_p(x) I(X;Y) ([[channel-capacity-and-error-correction]]).
- **KL divergence** D(p‖q) = Σ p log (p/q) ≥ 0 (Gibbs' inequality, by Jensen — [[convexity]]);
  = 0 iff p = q; not symmetric, not a metric; infinite if q = 0 where p > 0. Expected extra bits when
  coding p-distributed data with a code designed for q.
- **Cross-entropy** H(p, q) = −Σ p log q = H(p) + D(p‖q). Minimizing cross-entropy over q ⇔ minimizing
  KL ⇔ maximizing likelihood ([[maximum-likelihood-estimation]]). **Perplexity** = 2^{H(p,q)} =
  effective branching factor; a language model with perplexity 20 is "as uncertain as a fair 20-sided
  die" per token.
- **Data-processing inequality**: X → Y → Z (Markov) ⇒ I(X;Z) ≤ I(X;Y). No processing of Y creates
  information about X — a hard limit on features/embeddings.
- Differential entropy for densities (can be negative; Gaussian maximizes it for fixed variance).

## Where it shows up in CS
- Compression limits and code design ([[source-coding-and-compression]]).
- Decision trees split on information gain = I(feature; label); feature selection by MI.
- Loss functions: cross-entropy/log-loss; KL terms in variational inference and RLHF regularizers
  (§6.4, §6.7).
- Password/key strength in bits of entropy; randomness extractors; min-entropy for security (§5.3).
- Kolmogorov complexity: the algorithmic counterpart of entropy ([[kolmogorov-complexity]]).
- Lower bounds: comparison sorting needs log₂(n!) ≈ n log n bits of decisions ([[sorting]]).

## Pitfalls
- Entropy is a property of a *distribution*, not of a string; "the entropy of this file" means under some model.
- KL asymmetry matters: D(p‖q) penalizes q missing p's modes (mean-seeking), D(q‖p) is mode-seeking.
- Mixing bits and nats (factor ln 2).

## Related
- [[source-coding-and-compression]], [[channel-capacity-and-error-correction]], [[log-probabilities]],
  [[maximum-likelihood-estimation]], [[kolmogorov-complexity]].

## Sources
Shannon 1948 Part I §6–7; MacKay ch. 2, 8; CS109 "Information Theory".

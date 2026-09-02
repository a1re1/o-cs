---
title: Differential privacy and privacy in machine learning — why anonymization fails (linkage, reconstruction, membership inference), the (ε, δ)-DP definition and its guarantees, the Laplace and Gaussian mechanisms and sensitivity, composition and privacy budgets, randomized response, local vs central DP, DP-SGD for training models, privacy amplification and accounting (moments accountant/RDP), the privacy–utility trade-off, deployments (US Census, Apple, Google), federated learning and secure aggregation, and attacks on ML models (memorization, extraction, model inversion)
type: concept
section: "6.11"
level: 500
tags: [differential-privacy, privacy, anonymization, de-anonymization, linkage-attack, netflix-prize, reconstruction-attack, membership-inference, epsilon-delta, privacy-loss, neighboring-datasets, sensitivity, laplace-mechanism, gaussian-mechanism, randomized-response, composition, sequential-composition, advanced-composition, privacy-budget, post-processing, group-privacy, local-dp, central-dp, trusted-curator, dp-sgd, gradient-clipping, noise-addition, moments-accountant, renyi-dp, privacy-amplification, subsampling, privacy-utility-tradeoff, census-2020, apple, google-rappor, federated-learning, secure-aggregation, memorization, training-data-extraction, model-inversion, canary, exposure, dwork, abadi, k-anonymity]
sources: [ai-safety-fairness-and-interpretability-texts-courses-and-seminal-papers]
summary: Releasing statistics or models trained on personal data leaks information about individuals — "anonymized" datasets are re-identified by linkage (Netflix Prize, medical records), aggregate queries enable reconstruction of the underlying records (the reason the 2020 US Census adopted DP), and trained models memorize (membership-inference attacks tell whether a record was in the training set; extraction attacks recover verbatim training text from LLMs) — and differential privacy (Dwork et al. 2006) is the definition that survives these: a randomized mechanism M is (ε, δ)-DP if for any two datasets differing in one person and any output set S, P[M(D) ∈ S] ≤ e^ε P[M(D′) ∈ S] + δ, so what an adversary learns about you is almost the same whether or not you participated, regardless of side information; it is achieved by calibrated noise — the Laplace mechanism adds Lap(Δ/ε) to a query with ℓ1-sensitivity Δ, the Gaussian mechanism adds N(0, σ²) scaled to ℓ2-sensitivity for (ε, δ)-DP, randomized response makes surveys locally private — and it composes (sequential: ε's add; advanced composition and Rényi/moments accounting give ~√k for k queries), is immune to post-processing, and extends to groups at k·ε; DP-SGD (Abadi et al. 2016) trains neural networks privately by clipping per-example gradients and adding Gaussian noise, with privacy amplification by subsampling and a moments accountant tracking the total budget (ε ≈ 1–10 typical), at a cost in accuracy and compute that grows for small datasets and large models; local DP (Google's RAPPOR, Apple's telemetry) protects against the collector, central DP (Census, most ML) trusts a curator; federated learning keeps data on devices and, with secure aggregation and DP on the aggregate, limits what the server learns; and the practical questions are the value of ε (privacy loss is not a small number), what to protect (a record, a user, a conversation), and how DP interacts with fairness (noise hurts small groups more) and with the honest limits of "anonymization" claims.
---
# Differential privacy and privacy in machine learning

**In one sentence.** Any useful release of information about a dataset reveals something
about the people in it; differential privacy bounds how much, per person, by the
randomness of the release — and it is the only definition that holds against every side
channel and every future dataset.

## Why anonymization fails (Narayanan & Shmatikov 2008; Dinur & Nissim 2003; Shokri et al. 2017; Carlini et al. 2021)
Removing identifiers doesn't work: **linkage** — the Netflix Prize ratings re-identified
from public IMDb reviews; Massachusetts hospital records linked to a voter roll by zip +
birthdate + sex (Sweeney — 87 % of Americans are unique on those three); k-anonymity/
l-diversity patch specific attacks and fail to others (homogeneity, background
knowledge, composition). **Reconstruction**: enough accurate aggregate statistics determine
the microdata (Dinur–Nissim: answering n queries with error o(√n) allows reconstructing
almost all records) — the U.S. Census Bureau reconstructed 2010 microdata from published
tables, motivating DP for 2020. **ML models leak**: **membership inference** (does a shadow-
model-trained attacker recognize training examples from confidence/loss? — overfitting
makes it easy), **model inversion** (reconstruct a face from a face-recognition model),
**training-data extraction** (prompt an LLM to regurgitate memorized text — Carlini et al.:
PII, code, licenses; larger models memorize more; deduplication reduces it —
[[large-language-models]]), gradient leakage in federated settings. Privacy is not a
property of the data but of the *release mechanism*.

## The definition (Dwork, McSherry, Nissim & Smith 2006; Dwork & Roth 2014)
A randomized mechanism M is **(ε, δ)-differentially private** if for all neighbouring
datasets D, D′ (differing in one individual's record) and all output sets S:
P[M(D) ∈ S] ≤ e^ε · P[M(D′) ∈ S] + δ. ε is the **privacy loss** (0.1–1 strong, ~10 weak; it is
a multiplicative bound on how much any one person shifts the output distribution);
δ ≪ 1/n allows a tiny failure probability (pure DP: δ = 0). Meaning: whatever an adversary
infers, they would infer almost equally with your record replaced — protection against
arbitrary side information, present and future; it does not prevent learning population
facts (smoking causes cancer) — that's the point. Properties: **post-processing** invariance
(any function of a DP output is DP — free), **sequential composition** (k mechanisms with εᵢ
give Σεᵢ), **parallel composition** (disjoint subsets), **group privacy** (k people: kε),
**advanced composition** (≈ ε√(2k ln(1/δ′)) + kε(e^ε − 1) for k adaptive uses), and tighter
accounting via **Rényi DP** / zero-concentrated DP / f-DP ([[entropy-and-information]]
divergences). The **privacy budget** is finite: every query spends some; the curator must
stop or degrade.

## Mechanisms (Dwork & Roth ch. 3; Warner 1965)
**Sensitivity** Δf = max over neighbours ‖f(D) − f(D′)‖ (ℓ1 or ℓ2): counts have Δ = 1, sums
need bounded ranges (clip), means Δ = range/n. **Laplace mechanism**: f(D) + Lap(Δ₁/ε) is
ε-DP — the noise scale is independent of n, so relative error shrinks as 1/(εn).
**Gaussian mechanism**: f(D) + N(0, σ²I) with σ ≥ Δ₂√(2 ln(1.25/δ))/ε is (ε, δ)-DP — better for
high-dimensional vector queries (ℓ2 sensitivity). **Exponential mechanism** for
non-numeric outputs (choose an option with probability ∝ e^{ε·score/2Δ}). **Randomized
response** (Warner 1965): flip a coin; answer truthfully or randomly — ln 3-DP for a fair
coin, unbiased estimates by inverting the noise; the archetype of **local DP** where each
user randomizes before sending (no trusted curator; Google **RAPPOR**, Apple's emoji/
keyboard telemetry) at a much higher noise cost (error ∝ √n rather than constant) vs
**central DP** (a trusted curator adds noise once; Census 2020's TopDown algorithm,
Google/LinkedIn analytics, DP synthetic data). Sparse-vector technique, private
histograms/heavy hitters, private selection, and DP for streaming/continual release.

## DP for machine learning: DP-SGD (Abadi et al. 2016; Ponomareva et al. 2023)
Training is a sequence of gradient queries: **DP-SGD** — per-example gradients **clipped**
to ℓ2 norm C (bounds sensitivity; a hyperparameter that biases training), summed, plus
Gaussian noise N(0, σ²C²I), then the usual step; **privacy amplification by subsampling**
(a random minibatch of rate q reduces per-step loss to ≈ qε) and the **moments accountant**
(Rényi-DP composition across T steps → ε ≈ q√(T ln(1/δ))/σ scale) make a full training run
fit in ε ≈ 1–8. Costs: accuracy drops (worse for small data, many classes, large models —
noise scales with dimension), compute (per-example gradients; ghost clipping and
vectorized tricks), hyperparameters interact with privacy (larger batches help), and
public-data pretraining + private fine-tuning is the practical recipe (DP fine-tuning of
LLMs with LoRA — [[llm-post-training-sft-rlhf-dpo]]); PATE (teacher ensembles on
disjoint data, noisy voting) as an alternative; DP synthetic data. Auditing: **canaries**
and exposure metrics, membership-inference attacks as empirical lower bounds on leakage
(tight auditing shows DP-SGD's bound is nearly achieved by attacks in the worst case).
Libraries: Opacus, TensorFlow Privacy, JAX-Privacy, OpenDP.

## Federated learning and cryptographic complements (McMahan et al. 2017; Bonawitz et al. 2017)
**Federated learning**: data stays on devices; clients compute updates on local data, the
server averages (FedAvg); non-IID data, stragglers, communication limits. It is *not*
private by itself (updates leak — gradient inversion), so add **secure aggregation** (the
server sees only the sum, via masked shares — [[cryptographic-protocols-and-zero-knowledge]]
secure multi-party computation) and **DP on the aggregate** (user-level DP: a user's entire
contribution is the unit) — Google's Gboard next-word models. Cryptographic tools with
different guarantees: **homomorphic encryption** (compute on ciphertexts — expensive
inference-as-a-service), **secure MPC** (joint computation without revealing inputs),
**trusted execution environments**, and the distinction: cryptography protects the
*computation*, DP protects the *output* — you need both when the output is released.

## Deployments, choices, and tensions (Census 2020; Apple/Google; Bagdasaryan et al. 2019)
The **2020 U.S. Census** applied DP to all published tables (ε ≈ 19.6 total across the
redistricting release — a public argument about accuracy for small areas vs
reconstruction risk); Apple (ε per day per user, criticized as high), Google (RAPPOR,
Chrome, COVID mobility reports), Microsoft telemetry, LinkedIn/Uber analytics, Meta's
mobility data. Choices: the **unit of privacy** (record, user, household, conversation),
ε and δ and their communication, budget over time (a data lake that answers queries
forever must ration). **Tensions**: DP noise degrades accuracy most for **small subgroups**,
so private models can be *less fair* (Bagdasaryan et al.) — a fairness–privacy trade-off
([[fairness-in-machine-learning]]); DP does not address consent, purpose limitation, or
inference about groups ([[ai-safety-and-alignment]] sociotechnical view); legal regimes
(GDPR "anonymization", HIPAA safe harbour) predate DP and don't map onto ε. The honest
claim is quantitative: "this release bounds per-person influence by e^ε", not "this data
is anonymous".

## Pitfalls
- Calling k-anonymized or aggregated data "anonymous" (linkage, reconstruction).
- Reporting ε without δ, the unit of privacy, or the composition over all releases.
- DP-SGD with a huge clipping norm (all noise) or tiny (all bias); tuning
  hyperparameters on private data without accounting.
- Federated learning marketed as privacy without secure aggregation/DP.
- Ignoring that DP noise hits minority groups hardest; ε = 10⁶ "DP" deployments.
- Measuring privacy by "the attack I tried failed" (attacks only lower-bound leakage).

## Related
- [[large-language-models]] (memorization, extraction), [[ai-safety-and-alignment]],
  [[fairness-in-machine-learning]], [[cryptographic-protocols-and-zero-knowledge]] (MPC,
  HE), [[cryptography-basics]], [[entropy-and-information]] (divergences),
  [[concentration-inequalities]] (noise calibration), [[llm-post-training-sft-rlhf-dpo]]
  (DP fine-tuning), [[mlops-and-ml-systems]] (data governance), [[hypothesis-testing-and-confidence-intervals]]
  (statistical inference under noise), [[security-principles]].

## Sources
Dwork, McSherry, Nissim & Smith 2006; Dwork & Roth 2014 (*The Algorithmic Foundations of Differential Privacy*, free); Abadi et al. 2016 (DP-SGD); Mironov 2017 (Rényi DP); Warner 1965; Erlingsson et al. 2014 (RAPPOR); Narayanan & Shmatikov 2008; Dinur & Nissim 2003; Shokri et al. 2017; Carlini et al. 2019 (secret sharer), 2021; Fredrikson et al. 2015; McMahan et al. 2017; Bonawitz et al. 2017; Bagdasaryan et al. 2019; Abowd 2018 (Census); Ponomareva et al. 2023 (DP-fy ML); Nasr et al. 2023 (tight auditing).

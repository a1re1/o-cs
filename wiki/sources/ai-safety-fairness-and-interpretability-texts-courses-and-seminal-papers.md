---
title: AI safety, alignment, ethics, fairness and interpretability — Barocas–Hardt–Narayanan's Fairness and Machine Learning (free), Molnar's Interpretable Machine Learning (free), Christian's The Alignment Problem, Russell's Human Compatible; BlueDot AI Safety Fundamentals, Stanford CS384/CS221 ethics, MIT 6.S898, Berkeley CS294 Responsible AI; Amodei et al. "Concrete Problems in AI Safety", Bostrom and Russell essays, Dwork "Fairness Through Awareness", Hardt equality of opportunity, LIME, SHAP, Anthropic's interpretability series, Christiano RLHF, "Stochastic Parrots", the foundation-models report
type: source
section: "6.11"
level: 400
tags: [barocas, hardt, narayanan, fairmlbook, fairness-and-machine-learning, molnar, interpretable-machine-learning, christian, alignment-problem, russell, human-compatible, bluedot, ai-safety-fundamentals, cs384, cs221-ethics, 6-s898, cs294-responsible-ai, amodei, concrete-problems, bostrom, superintelligence, dwork, fairness-through-awareness, equality-of-opportunity, ribeiro, lime, lundberg, shap, anthropic, interpretability, circuits, superposition, monosemanticity, christiano, rlhf, bender, stochastic-parrots, bommasani, foundation-models-report]
sources: []
authors: [Solon Barocas, Moritz Hardt, Arvind Narayanan, Christoph Molnar, Brian Christian, Stuart Russell, Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, Dan Mané, Nick Bostrom, Cynthia Dwork, Eric Price, Marco Tulio Ribeiro, Scott Lundberg, Su-In Lee, Emily Bender, Timnit Gebru, Rishi Bommasani]
year: 2023
institution: Princeton / Berkeley / Cornell / Anthropic / OpenAI / DeepMind
url: https://fairmlbook.org/
license: mixed (fairmlbook, Molnar, BlueDot free; Christian and Russell commercial)
format: html
summary: Fairness and Machine Learning (Barocas, Hardt & Narayanan; published 2023, free; site read) is the fairness textbook — introduction; when is automated decision making legitimate; classification (formal non-discrimination criteria — independence, separation, sufficiency — their relationships and impossibility); relative notions of fairness; causality (why the classification paradigm falls short); U.S. anti-discrimination law; testing discrimination in practice; a broader view of structural discrimination; and datasets (their role and harms) — with the "21 fairness definitions and their politics" tutorial; Molnar's Interpretable Machine Learning (free) catalogues interpretable models and model-agnostic methods (PDP, ICE, ALE, permutation importance, LIME, Shapley values/SHAP, counterfactual explanations, anchors) and neural-network methods (saliency, feature visualization, concepts); Christian's The Alignment Problem narrates the field (representation, agency, normativity — bias in embeddings, reward hacking, inverse RL, RLHF) and Russell's Human Compatible argues for assistance games with uncertain objectives; the courses run from BlueDot's AI Safety Fundamentals (alignment and governance tracks) to university ethics/responsible-AI modules; and the seminal papers are Amodei et al.'s Concrete Problems in AI Safety (2016; abstract read: five practical accident-risk problems — avoiding side effects and reward hacking from wrong objectives, scalable oversight when the objective is expensive to evaluate, safe exploration and robustness to distributional shift during learning), Bostrom's Superintelligence and Russell's essays on the control problem, Dwork et al.'s Fairness Through Awareness (individual fairness via a task-specific metric), Hardt, Price & Srebro's equality of opportunity (post-processing to equalize true-positive rates; the COMPAS impossibility context), Ribeiro et al.'s LIME (local surrogate explanations) and Lundberg & Lee's SHAP (Shapley-value attributions unifying prior methods), Anthropic's interpretability series (circuits, toy models of superposition, scaling monosemanticity with sparse autoencoders), Christiano et al.'s RL from human preferences (2017), Bender et al.'s Stochastic Parrots (2021) and the Stanford foundation-models report (Bommasani et al. 2021).
---
# AI safety, fairness, and interpretability: sources

## What they are
- **Barocas, Hardt & Narayanan, Fairness and Machine Learning: Limitations and Opportunities**
  (2023, free; contents read): 1 introduction; 2 when is automated decision making
  legitimate? (bureaucratic decision making, normative concern); 3 classification (formal
  non-discrimination criteria in a decision-theoretic setting, their relationships and
  limits); 4 relative notions of fairness (objections to systematic group differences);
  5 causality (the technical repertoire and how it addresses shortcomings of the
  classification paradigm); 6 U.S. anti-discrimination law (what it is and isn't,
  trade-offs, application to ML); 7 testing discrimination in practice; 8 a broader view of
  discrimination (structural, organizational, interpersonal); 9 datasets (their role, harms,
  and the backbone of ML research); plus tutorials (MLSS 2020, NeurIPS 2017, "21 fairness
  definitions and their politics", FAccT 2018) and courses (Berkeley CS294, Cornell INFO
  4270, Princeton COS 597E).
- **Molnar, Interpretable ML** (free): interpretability (importance, taxonomy, evaluation),
  interpretable models (linear/logistic, GLMs/GAMs, trees, rules, RuleFit), model-agnostic
  global (PDP, ALE, interactions, functional decomposition, permutation importance, global
  surrogates, prototypes) and local (ICE, LIME, counterfactuals, scoped rules/anchors,
  Shapley values, SHAP) methods, neural-network interpretation (learned features,
  pixel attribution/saliency, concept detection — TCAV, adversarial examples, influential
  instances).
- **Christian, The Alignment Problem** (2020): Prophecy (representation: word-embedding
  bias, COMPAS), Agency (reinforcement, shaping, curiosity), Normativity (imitation,
  inference — inverse RL, uncertainty — CIRL/assistance games); **Russell, Human Compatible**
  (2019): the standard model (fixed objectives) is the problem; provably beneficial AI via
  machines uncertain about human preferences that defer and learn. **Bostrom,
  Superintelligence** (2014): the control problem, instrumental convergence, orthogonality.
- **Courses**: **BlueDot AI Safety Fundamentals** (alignment track: LLMs, RLHF, scalable
  oversight, interpretability, evals, agent foundations; governance track: compute
  governance, standards, policy); Stanford CS384 (ethics of AI), CS221 ethics modules; MIT
  6.S898 (deep-learning ethics/safety); Berkeley CS294 Responsible AI; **Anthropic/DeepMind/
  OpenAI** research blogs as the live literature.
- **Seminal**: Amodei, Olah, Steinhardt, Christiano, Schulman & Mané 2016 (**Concrete
  Problems**: side effects, reward hacking, scalable oversight, safe exploration,
  distributional shift — "accidents … unintended and harmful behavior that may emerge from
  poor design"); Christiano et al. 2017 (**RLHF**: deep RL from human preferences — Atari and
  MuJoCo from ~1 % of the labels); Bostrom 2012/2014 and Russell 2019 (control problem);
  Dwork, Hardt, Pitassi, Reingold & Zemel 2012 (**fairness through awareness**: Lipschitz
  condition w.r.t. a similarity metric; the group–individual distinction; "fair affirmative
  action"); Hardt, Price & Srebro 2016 (**equality of opportunity**: equalized odds/
  opportunity as post-processing, and its incompatibility with calibration —
  Chouldechova 2017, Kleinberg et al. 2016); Ribeiro, Singh & Guestrin 2016 (**LIME**);
  Lundberg & Lee 2017 (**SHAP**); **Anthropic interpretability**: Olah et al. 2020 (circuits:
  curve detectors, universality), Elhage et al. 2021 (transformer circuits: induction
  heads), Elhage et al. 2022 (**toy models of superposition**), Bricken et al. 2023 (towards
  monosemanticity: sparse autoencoders) and Templeton et al. 2024 (**scaling
  monosemanticity**: features in Claude 3 Sonnet, the Golden Gate feature); Bender, Gebru,
  McMillan-Major & Shmitchell 2021 (**Stochastic Parrots**: scale's environmental and social
  costs, the illusion of understanding); Bommasani et al. 2021 (**foundation models**:
  opportunities and risks — emergence and homogenization); Szegedy et al. 2013 / Goodfellow
  et al. 2014 (adversarial examples); Dwork 2006 / Abadi et al. 2016 (differential privacy
  and DP-SGD); Carlini et al. 2021 (training-data extraction); Perez et al. 2022 (red-teaming
  LMs); Anthropic 2022 (**Constitutional AI**), Bai et al. RLAIF; Hendrycks et al. 2021
  ("unsolved problems in ML safety"); Weidinger et al. 2021 (taxonomy of LM harms).

## Key ideas → pages
[[ai-safety-and-alignment]], [[fairness-in-machine-learning]],
[[interpretability-and-explainability]], [[differential-privacy]];
[[llm-post-training-sft-rlhf-dpo]] (RLHF/CAI mechanics), [[causal-inference]] (fairness's
causal chapter).

## What they add
fairmlbook for the criteria *and* their limits (the book's argument is that the
classification paradigm is not enough — law, causality, and structural discrimination
matter); Molnar for a complete, honest catalogue of explanation methods and their failure
modes; Concrete Problems for the taxonomy the safety field still uses; the Anthropic series
for the empirical program of reading a model's internals; Russell for the reframing of
alignment as uncertainty about objectives rather than better objectives.

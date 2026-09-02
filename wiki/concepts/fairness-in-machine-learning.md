---
title: Fairness in machine learning — where disparities come from (data, labels, features, feedback loops, deployment), protected attributes and the failure of "fairness through unawareness", the three group criteria (independence/demographic parity, separation/equalized odds and equality of opportunity, sufficiency/calibration) and the impossibility of satisfying them together (COMPAS), individual fairness (Dwork's Lipschitz condition), interventions (pre-, in-, post-processing), causal notions (counterfactual fairness, path-specific effects), testing discrimination, U.S. anti-discrimination law (disparate treatment vs impact), datasets and their harms, and the limits of the classification paradigm
type: concept
section: "6.11"
level: 400
tags: [fairness, algorithmic-fairness, discrimination, bias, protected-attributes, proxies, fairness-through-unawareness, demographic-parity, independence, statistical-parity, separation, equalized-odds, equality-of-opportunity, sufficiency, calibration, calibration-within-groups, impossibility-theorem, compas, propublica, chouldechova, kleinberg, base-rates, individual-fairness, lipschitz, fairness-through-awareness, dwork, pre-processing, in-processing, post-processing, threshold-adjustment, constrained-optimization, reweighting, causal-fairness, counterfactual-fairness, path-specific-effects, redlining, feedback-loops, disparate-treatment, disparate-impact, four-fifths-rule, anti-discrimination-law, auditing, testing-discrimination, datasets, benchmark-harms, representation-bias, measurement-bias, intersectionality, embeddings-bias, barocas-hardt-narayanan, 21-definitions]
sources: [ai-safety-fairness-and-interpretability-texts-courses-and-seminal-papers]
summary: Machine-learning systems reproduce and can amplify the disparities in their data — historical discrimination in labels, unrepresentative sampling, features that proxy for protected attributes, measurement error that differs by group, and feedback loops (predictive policing, credit) — so removing the protected attribute ("fairness through unawareness") does nothing when proxies remain, and the field formalized non-discrimination as statistical criteria on a classifier's score R, outcome Y and group A: independence (R ⊥ A — demographic parity: equal acceptance rates), separation (R ⊥ A | Y — equalized odds: equal true- and false-positive rates; equality of opportunity relaxes to equal TPR), and sufficiency (Y ⊥ A | R — calibration within groups: a score means the same thing for everyone), which Barocas–Hardt–Narayanan show are mutually incompatible except in degenerate cases: when base rates differ, a calibrated classifier cannot have equal error rates (Chouldechova, Kleinberg et al. — the ProPublica vs Northpointe COMPAS dispute was exactly this, each side holding a different criterion), so the choice is normative, not technical; individual fairness (Dwork et al.) asks that similar individuals be treated similarly under a task-specific metric — principled but requiring a metric nobody has; interventions act before training (reweighting, repair), during (constrained or adversarial objectives), or after (group-specific thresholds — Hardt et al.'s post-processing achieves equalized odds at some accuracy cost); causal framings (counterfactual fairness, path-specific effects, the causality chapter) separate legitimate from illegitimate pathways and expose that observational criteria can't distinguish them; law (disparate treatment vs disparate impact, the four-fifths rule, business necessity) constrains what may be used and how; discrimination testing (audits, correspondence studies, slice analysis) is how problems are found; and the book's argument is that classification metrics are a narrow lens — legitimacy of the decision, structural discrimination, and the datasets themselves matter more than the parity metric chosen.
---
# Fairness in machine learning

**In one sentence.** A classifier can be fair by acceptance rates, by error rates, or by
what its scores mean — but not all three when base rates differ — so "which fairness"
is a normative choice the data cannot make, and most real unfairness enters before the
classifier through the data, the labels, and the decision's legitimacy.

## Where disparities come from — my model is accurate overall but wrong for one group: what to check (fairmlbook ch. 1, 9; Christian part I)
**Data**: historical decisions encode past discrimination (hiring, lending, policing) and
become labels; **sampling/representation bias** (faces, dialects, geographies missing);
**measurement bias** (arrests as a proxy for crime; healthcare costs as a proxy for need —
Obermeyer et al. 2019: a widely used algorithm underestimated Black patients' needs
because it predicted cost); **label noise** that differs by group; **proxies** (zip code,
name, browsing history) that reconstruct protected attributes, so **fairness through
unawareness** — deleting the attribute — fails and can make auditing harder; **feedback
loops** (predictive policing sends officers where arrests were recorded, generating more —
[[mlops-and-ml-systems]]; recommendation and credit likewise); **aggregation** (one model for
heterogeneous groups); **deployment** context (a screening tool used as a decision tool);
word-embedding and LLM biases learned from text ([[nlp-fundamentals]]; stereotype
benchmarks); **intersectionality** (errors concentrated on subgroups — Buolamwini & Gebru's
Gender Shades: commercial face classifiers failing on darker-skinned women). Datasets
(ch. 9): benchmarks shape research priorities and encode harms (ImageNet person categories,
scraped faces, consent); documentation via datasheets.

## The classification criteria and their impossibility (fairmlbook ch. 3; Hardt et al. 2016; Chouldechova 2017; Kleinberg et al. 2016)
Score/decision R, target Y, sensitive attribute A. Three families:
| Criterion | Condition | Reads as | Fails when |
|---|---|---|---|
| **Independence** (demographic/statistical parity) | R ⊥ A | equal selection rates | ignores Y — can be satisfied by selecting randomly in one group; conflicts with accuracy when base rates differ |
| **Separation** (equalized odds) | R ⊥ A \| Y | equal TPR and FPR across groups; **equality of opportunity** = equal TPR only | requires Y to be a legitimate target; error rates depend on base rates |
| **Sufficiency** (calibration by group) | Y ⊥ A \| R | a score of 0.7 means 70 % for every group | satisfied by many unfair scores; says nothing about error rates |
**Impossibility**: any two of the three hold simultaneously only in degenerate cases
(perfect prediction, or equal base rates P(Y = 1 | A)). The **COMPAS** case: ProPublica showed
Black defendants had a higher false-positive rate (separation violated); Northpointe
showed the scores were calibrated within groups (sufficiency held); both correct — with
different base rates, calibration forces unequal error rates. Consequence: the criterion
must be chosen by the harm one cares about (who bears false positives?), which is a
normative question; also, all three are **observational** — satisfiable by a classifier that
is unfair in ways they cannot see. **Relative notions** (ch. 4): objections to group
differences in treatment/outcome, and when a disparity is a legitimate reflection of
differences vs an injustice to correct.

## Individual fairness (Dwork, Hardt, Pitassi, Reingold & Zemel 2012)
"**Fairness through awareness**": a randomized classifier M is fair if D(M(x), M(y)) ≤ d(x, y)
— similar people (under a task-specific metric d) receive similar distributions over
outcomes (Lipschitz); group fairness follows under conditions on d (the Earthmover
distance between groups); "fair affirmative action" as a constrained version. Principled
but the **metric** is the whole problem (who defines similarity?), it is not observational
(needs d), and it becomes a computational problem of finding the optimal Lipschitz map
(an LP — [[linear-programming-and-duality]]). Related: metric learning from human judgments,
counterfactual (causal) individual fairness.

## Interventions (Hardt et al. 2016; Kamiran & Calders; Zafar et al.; Agarwal et al. 2018)
- **Pre-processing**: reweight/resample training data, repair features toward group
  independence, remove proxies (optimized pre-processing with utility constraints).
- **In-processing**: add a fairness constraint or regularizer to training (constrained
  optimization via Lagrangian/reductions to cost-sensitive classification — Agarwal et al.;
  adversarial debiasing: an adversary tries to predict A from R).
- **Post-processing**: adjust decision thresholds per group on a fixed score — Hardt, Price
  & Srebro derive the equalized-odds/opportunity optimum (group-specific thresholds and
  randomization on the ROC curves' intersection); simple, needs A at decision time, costs
  accuracy and can require deliberately worse decisions for some.
Trade-offs: fairness–accuracy Pareto frontiers; the **cost of fairness** depends on which
criterion; long-term effects (Liu et al. 2018: parity constraints can harm the group they
target over time when outcomes feed back). Practical audit: evaluate every metric per
slice, look at the ROC curves per group, report base rates
([[machine-learning-basics]] evaluation).

## Causality and fairness (fairmlbook ch. 5; Kusner et al. 2017; [[causal-inference]])
Observational criteria conflate paths: a variable may affect Y through a legitimate route
(qualifications) and a discriminatory one (redlining). Causal notions: **counterfactual
fairness** (the decision would be the same had the individual's protected attribute been
different, holding exogenous noise fixed — needs a causal model), **path-specific effects**
(block only the unfair paths), proxy discrimination as intervention on proxies; they make
the normative choice explicit as a graph but require assumptions no data can validate
(the sense in which "race" can be intervened on is itself contested). Causality also
explains why parity constraints act like affirmative-action policies and why data
generated under past policies can't be read as neutral.

## Law, testing, and the broader view (fairmlbook ch. 2, 6–8)
**U.S. anti-discrimination law**: **disparate treatment** (intentional use of a protected
attribute — mostly forbidden, which also forbids some fairness interventions that use A)
vs **disparate impact** (a neutral practice with a disproportionate effect — Griggs; the
EEOC **four-fifths rule** as a screening heuristic — actionable unless "business necessity"
and no less-discriminatory alternative; Title VII, ECOA, FHA; the EU's GDPR/AI Act adding
transparency and risk classes); the law addresses decisions, not models, and its
categories map imperfectly to ML criteria. **Testing discrimination** (ch. 7): audit studies
and **correspondence** experiments (identical résumés with different names), outcome tests
(thresholds by group), regression with controls (and its pitfalls — including colliders),
platform audits with sock-puppet accounts; the practical complexities of access, ground
truth and defining the comparison. **Legitimacy** (ch. 2): before asking whether an automated
decision is fair, ask whether it is legitimate at all — bureaucratic decision-making,
consent, contestability, human review, and the cases where prediction itself is
inappropriate. **Structural discrimination** (ch. 8): organizational and interpersonal
discrimination interact with ML; fairness metrics can launder, not fix, structural
inequality — the book's limitations-and-opportunities thesis. Governance: impact
assessments, model cards, participatory design ([[ai-safety-and-alignment]] for the wider
sociotechnical frame; [[interpretability-and-explainability]] for the right to explanation).

## Pitfalls
- "We removed the protected attribute, so it's fair" (proxies).
- Reporting one parity metric without base rates and error rates by group; claiming a
  system is calibrated *and* has equal error rates (impossible with different base rates).
- Optimizing a fairness metric on a benchmark whose labels encode the discrimination.
- Post-processing thresholds without legal review (disparate treatment); intervening
  on a proxy that is itself a legitimate qualification.
- Slicing only by one attribute (intersectional blind spots); auditing once and never in
  production (drift, feedback).

## Related
- [[causal-inference]], [[machine-learning-basics]], [[nlp-fundamentals]] (embedding bias),
  [[large-language-models]] (LLM bias/toxicity), [[ai-safety-and-alignment]],
  [[interpretability-and-explainability]], [[differential-privacy]],
  [[mlops-and-ml-systems]] (feedback loops, slice monitoring),
  [[linear-programming-and-duality]], [[hypothesis-testing-and-confidence-intervals]]
  (audit statistics), [[bayes-theorem-and-inference]] (base rates).

## Sources
Barocas, Hardt & Narayanan 2023 (contents read; ch. 1–9 from the book); Narayanan 2018 ("21 fairness definitions and their politics"); Dwork et al. 2012; Hardt, Price & Srebro 2016; Chouldechova 2017; Kleinberg, Mullainathan & Raghavan 2016; Angwin et al. 2016 (ProPublica); Kusner et al. 2017; Agarwal et al. 2018; Buolamwini & Gebru 2018; Obermeyer et al. 2019; Liu et al. 2018; Bolukbasi et al. 2016; Gebru et al. 2021 (datasheets).

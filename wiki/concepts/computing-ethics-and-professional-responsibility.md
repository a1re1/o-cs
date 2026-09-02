---
title: Computing ethics and professional responsibility — why engineers' decisions carry ethical weight (scale, opacity, embeddedness), the ethical toolkit (consequentialism, deontology, virtue ethics, contractualism, care — as lenses, not calculators), three senses of responsibility (blameworthiness, liability, taking responsibility) and the many-hands/responsibility-gap problem, professional codes (ACM 2018, SE code, NSPE) and what they actually require, the case literature (Therac-25, Boeing 737 MAX MCAS, Volkswagen defeat devices, Uber ATG, Facebook emotional contagion, Cambridge Analytica, COMPAS, Amazon hiring model), harms of scaled algorithmic systems (O'Neil's opacity/scale/damage, feedback loops), dark patterns and attention design, whistleblowing and dissent inside organizations, the practice of recognizing, reasoning and persuading (the memo), and what to do when asked to build something you believe is wrong
type: concept
section: "7.8"
level: 200
tags: [ethics, computing-ethics, professional-responsibility, professional-ethics, scale, opacity, embeddedness, consequentialism, utilitarianism, deontology, kant, virtue-ethics, contractualism, rawls, care-ethics, moral-lenses, responsibility, blameworthiness, liability, taking-responsibility, many-hands, responsibility-gap, culpable-ignorance, acm-code, software-engineering-code, nspe, public-good, avoid-harm, competence, honesty, therac-25, race-condition, safety-culture, boeing-737-max, mcas, volkswagen, defeat-device, dieselgate, uber-atg, tempe, facebook-emotional-contagion, cambridge-analytica, compas, amazon-hiring, weapons-of-math-destruction, feedback-loops, dark-patterns, deceptive-design, attention-economy, engagement, whistleblowing, dissent, conscientious-objection, refusal, red-teaming, impact-assessment, recognize-reason-persuade, memo, stakeholders, informed-consent, research-ethics, irb, dual-use, weizenbaum, judgment-vs-calculation]
sources: [computing-ethics-texts-courses-and-codes]
summary: Software decisions are ethical decisions because code operates at scale (one default touches millions), opaquely (users and even builders can't see why), and embedded in infrastructure people cannot opt out of — so the ACM Code's first principle, contribute to society and human well-being while avoiding harm, is not aspirational garnish but a description of the job; the ethical theories (consequences, duties and rights, character, fair agreement, care) are best used as lenses that surface different considerations rather than as formulas, and the practically useful distinction (Harvard Embedded EthiCS; Bernstein; Hormio) is between three senses of responsibility — blameworthiness (did you act wrongly, knowingly or through culpable ignorance?), liability (who must pay or fix?), and taking responsibility (who will act to repair or prevent harm, regardless of blame?) — because in large systems the "problem of many hands" and AI "responsibility gaps" mean no one may be blameworthy while everyone must still take responsibility; the case literature is the discipline's memory: Therac-25 (race conditions, reused software trusted without interlocks, dismissed incident reports — a safety-culture failure more than a coding bug), Boeing 737 MAX MCAS (a single-sensor system with authority to move the stabilizer, hidden from pilots for certification reasons), Volkswagen's defeat device (engineers implementing knowing deception, several imprisoned), Uber ATG's Tempe fatality (safety driver reliance, disabled braking), Facebook's emotional-contagion experiment and Cambridge Analytica (consent and data purpose), COMPAS and Amazon's hiring model (fairness, proxies, feedback), and O'Neil's opacity-scale-damage triad for models that punish the already disadvantaged and confirm themselves through feedback loops; day-to-day it shows up as dark patterns and engagement optimization, defaults and permissions, data retention, accessibility, and dual-use tools; the professional's obligations include competence (don't ship what you don't understand — 2.6), honest evaluation of risks (2.5), refusing unauthorized access (2.8), and — when the organization won't listen — escalation, documented dissent, and in extremity whistleblowing, with the CS181 method as the skill to practice: recognize the ethical dimension early, reason about it with the norms of the discipline, and persuade in a clear memo that names the risk, the stakeholders, the options and a recommendation.
---
# Computing ethics and professional responsibility

**In one sentence.** Because code runs at scale, hides its reasons, and becomes
infrastructure, the engineer who writes it holds real power over strangers — the
craft of ethics here is to notice that power in time, reason about it with more than
one lens, distinguish blame from the responsibility to act, and persuade the
organization to do the right thing before the postmortem.

## Why this is part of engineering (ACM Code preamble; O'Neil; Weizenbaum)
Three amplifiers make software choices morally weighty: **scale** — a default, a
threshold, a ranking function applies to millions identically (a 0.1 % error is
thousands of people); **opacity** — users can't inspect the model, the A/B test, or the
data flow, and often the builders can't either ([[interpretability-and-explainability]]);
**embeddedness** — once systems become "integrated into the infrastructure of society"
(ACM 3.7) people cannot opt out (credit scoring, government portals, hiring filters,
content ranking). O'Neil's "weapon of math destruction" triad: **opacity**, **scale**,
**damage** — plus self-reinforcing **feedback loops** (predictive policing sends patrols
where arrests were recorded, producing more records; a credit model that denies loans
produces the defaults it predicted). Weizenbaum (1976), after watching people confide
in ELIZA: computers can *decide* (compute an outcome) but not *choose* (exercise
judgment grounded in values and experience); "since we do not now have any ways of
making computers wise, we ought not now to give computers tasks that demand wisdom" —
an argument that resurfaces in every automation debate ([[ai-safety-and-alignment]]).
The ACM Code's framing: "the public good is always the primary consideration."

## The toolkit: lenses, not calculators (Quinn; CS181)
- **Consequentialism/utilitarianism**: judge by outcomes for all affected — forces you to
  count everyone, including non-users and future people; risks justifying harm to a
  few for aggregate benefit and depends on predictions.
- **Deontology (duties, rights; Kant)**: some acts are wrong regardless of outcome —
  deception, using people merely as means (dark patterns, undisclosed experiments);
  rights (privacy, due process) as side-constraints.
- **Contractualism (Rawls, Scanlon)**: rules that free, equal people could reasonably
  agree to; the "veil of ignorance" test — would you accept this system not knowing
  which user you'd be? (fairness — [[fairness-in-machine-learning]]).
- **Virtue ethics**: what would an honest, courageous, just engineer do; professional
  character and habits (the "grasshopper on your shoulder").
- **Care ethics / stakeholder attention**: relationships and vulnerability; who is
  most exposed and least heard (accessibility, marginalized users).
Use them together: each surfaces considerations the others miss; disagreement between
lenses is the signal that a decision needs deliberation, documentation, and consent
rather than a quick call. Practical framings: **stakeholder analysis** (who is affected,
who decides, who bears risk), **reversibility** (can the harm be undone?), **consent**
(informed, meaningful, revocable — research ethics/IRB norms apply to A/B tests on
emotions: Facebook 2014), **publicity test** (would you defend it on the front page?),
and **precedent** (what does this normalize?).

## Responsibility: blame, liability, taking responsibility (Embedded EthiCS — read; Bernstein; Hormio)
Three senses that come apart: **blameworthiness** (you acted wrongly with knowledge or
**culpable ignorance** — you should have known; negligence vs intent), **liability**
(who must compensate/fix — legal and institutional), **taking responsibility** (who will
act to repair, mitigate, prevent — forward-looking, independent of blame). Cases: an
engineer who follows spec on a system whose harm emerges only at scale may not be
blameworthy yet must still take responsibility once the harm is known (Kodak's Shirley
cards calibrated film to light skin for decades — nobody "decided" it; responsibility
arrived with awareness). **Problem of many hands** (Thompson): in large organizations
responsibility diffuses until no one holds it; **responsibility gaps** in AI systems
(who answers for an autonomous decision?) — the answer is designed accountability:
named owners, review, logging, recourse. **Causal proportion** (Bernstein): degree of
responsibility tracks degree of causal contribution — the engineer who wrote the
defeat device (VW: Liang, Schmidt sentenced) vs the one who approved the deadline;
neither zero. Therac-25's lesson (Leveson & Turner): blaming "a software bug" hides the
system failure — reuse without re-verification, removed hardware interlocks, unreadable
error codes (`MALFUNCTION 54`), incident reports disbelieved, no independent safety
review — safety is a property of the organization ([[chaos-engineering-and-reliability-testing]],
[[site-reliability-engineering]] blameless postmortems make this operational).

## The codes: what they actually require (ACM 2018; SE Code 1999; NSPE)
ACM §1: **1.1** contribute to society and human well-being, acknowledging all people as
stakeholders; **1.2** avoid harm (negative consequences, especially unjust ones; when
harm is unintended, mitigate; when unavoidable, minimize and report — includes
*responsible disclosure*); **1.3** honesty (no deception, no misrepresenting capabilities —
marketing "AI" as more than it is); **1.4** fairness and non-discrimination (also
harassment, accessibility); **1.5** respect creative work (licenses, credit —
[[software-licensing]]); **1.6** privacy (collect minimum, state purposes, retention,
consent — [[technology-law-privacy-and-intellectual-property]]); **1.7** confidentiality.
§2: **2.1** quality; **2.2** competence; **2.3** know the rules (laws, regulations, org
policies) — and challenge unethical ones; **2.4** accept and provide review
([[code-review]]); **2.5** thorough evaluation of systems and their impacts *including
risks* — and if the risk is not communicated or is ignored, "the professional should
report it"; **2.6** work only in areas of competence — decline or learn; **2.7** public
awareness; **2.8** access resources only when authorized or compelled by the public good
(the hacking clause — [[security-principles]]); **2.9** design robustly and usably secure
systems. §3 leadership: **3.1** public good central; **3.2** social responsibility of the
org; **3.3** people, not just productivity; **3.4** policies reflecting the principles;
**3.5** growth of members; **3.6** care when modifying or retiring systems; **3.7** special
care for infrastructure-of-society systems. §4: uphold and promote; treat violations as
inconsistent with membership. The **SE Code**'s ordering of loyalties — public > client/
employer > product > … — is the tie-breaker rule: when the employer's interest conflicts
with public safety, the public wins (NSPE: "hold paramount"). Codes are not laws; they
are the profession's public promise and the vocabulary for internal argument.

## The case file (retell these)
- **Therac-25** (1985–87): six massive radiation overdoses; a race condition on fast
  operator edits and a counter overflow; software reused from a machine that had
  hardware interlocks; the vendor insisted it was impossible — safety culture.
- **Boeing 737 MAX** (2018–19): MCAS moved the stabilizer on a single AoA sensor with
  repeated, growing authority; omitted from manuals to avoid simulator training; 346
  dead; regulatory capture (delegated certification).
- **Volkswagen** (2015): software detected test conditions and switched emissions
  modes; 11 M cars; engineers who built it were prosecuted — "I was told to" failed.
- **Uber ATG, Tempe** (2018): first pedestrian killed by an autonomous test vehicle;
  classification flip-flopping, emergency braking disabled, a distracted safety driver
  and a safety program that relied on her ([[robotics-and-autonomous-systems]]).
- **Facebook emotional contagion** (2014) — 689 000 users' feeds manipulated without
  consent; **Cambridge Analytica** (2018) — data harvested via a quiz app's friends
  permission, repurposed for political targeting: purpose limitation and consent.
- **COMPAS** (ProPublica 2016) and **Amazon's hiring model** (2018): proxies for race and
  gender; the base-rate impossibility of satisfying all fairness criteria
  ([[fairness-in-machine-learning]]); recourse and contestability as design requirements.
- **Knight Capital** (2012): a deployment error and reused feature flag lost $440 M in
  45 minutes — operational ethics ([[continuous-integration-and-delivery]]).
- **Dark patterns** (Brignull): roach motels, confirmshaming, forced continuity, hidden
  costs, privacy zuckering; **engagement optimization** and its externalities (attention,
  misinformation, minors); the FTC/EU now regulate deceptive design
  ([[human-computer-interaction]]).
- **Dual use**: the same tool (face recognition, offensive security tooling, generative
  models) serves protection and oppression — evaluate the deployment, not only the code
  ([[ai-safety-and-alignment]]).

## Practice: recognize, reason, persuade — and dissent. My manager wants me to ship a feature I think is harmful: what should I do? (CS181 — read; Embedded EthiCS)
**Recognize** early: ethics questions arrive disguised as requirements ("just log
everything", "default to opt-in", "ship the model, we'll fix bias later", "the metric
is engagement"); build the habit at design review and in postmortems ("who could this
hurt?"); **red-team** your own product (Embedded EthiCS module): have peers list
objections and concerns before release; impact assessments (privacy, algorithmic,
accessibility) as routine artifacts. **Reason**: apply the lenses, identify stakeholders
and the most vulnerable, weigh reversibility and consent, consult the codes and law,
consider alternatives (the ethical option is often a design option: data minimization,
opt-in, human review, appeal paths, rate limits, sunsetting). **Persuade**: write the
**memo** (CS181's 400 words) — the decision, the risk in concrete terms, who is affected,
options with costs, a recommendation, and what you need; address it to someone who can
act; argue in the organization's own terms (liability, trust, regulation, retention)
alongside the moral ones; propose the smallest change that removes the harm. **Dissent**:
escalate through channels; document (dates, who was told); seek allies; refuse to
personally implement clear wrongs (VW) — conscientious objection has costs but is the
professional's line; **whistleblowing** as the last resort when serious public harm is
being concealed and internal routes are exhausted (legal protections vary: SEC, EU
directive; anonymity, journalists, retaliation risk — Haugen 2021, Wylie 2018); the
Code's 1.2/2.5 make reporting an obligation, not a betrayal. Also: your own conduct —
credit, honesty in estimates and reports ([[software-engineering-fundamentals]]),
respect on teams, mentoring, and the competence duty to keep learning.

## Pitfalls
- "I just build the tool" / "the algorithm decided" — abdication of taking
  responsibility.
- Ethics as a checklist at launch instead of a question at design time.
- Treating one lens (usually a utilitarian metric) as the whole analysis.
- Confusing legal with ethical (both directions).
- Silence: not writing the memo because someone else surely will.

## Related
- [[technology-law-privacy-and-intellectual-property]], [[fairness-in-machine-learning]],
  [[ai-safety-and-alignment]], [[interpretability-and-explainability]],
  [[differential-privacy]], [[security-principles]], [[software-licensing]],
  [[software-engineering-fundamentals]], [[code-review]], [[site-reliability-engineering]],
  [[chaos-engineering-and-reliability-testing]], [[human-computer-interaction]],
  [[robotics-and-autonomous-systems]], [[open-source-practice-and-governance]].

## Sources
ACM Code of Ethics and Professional Conduct 2018 (from memory; fetch blocked); ACM/IEEE-CS Software Engineering Code of Ethics 1999; NSPE Code; Stanford CS181 Spring 2024 (read: syllabus); Harvard Embedded EthiCS (read: module index; "Responsibility in Software Design", "Red Teaming and Responsibility"); Leveson & Turner 1993; Bernstein 2017; Hormio 2018; Thompson 1980 (many hands); Matthias 2004 (responsibility gap); O'Neil 2016; Weizenbaum 1976; Quinn 2022; ProPublica 2016 (COMPAS); Brignull 2010– (dark patterns); NTSB 2019 (Uber Tempe); House Transportation Committee 2020 (737 MAX); Kramer, Guillory & Hancock 2014.

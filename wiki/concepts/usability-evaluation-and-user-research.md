---
title: Usability Evaluation and User Research
type: concept
section: "9.1"
level: 300
tags: [usability, heuristic-evaluation, user-testing, ab-testing, needfinding]
sources: [hci-texts-courses-and-seminal-papers]
summary: The methods for finding out whether an interface works — heuristic evaluation, think-aloud usability testing, needfinding, and controlled A/B experiments.
---

# Usability Evaluation and User Research
**In one sentence.** A toolkit of cheap-to-expensive methods for discovering what
users need and whether a design meets those needs, ranging from expert inspection
to controlled online experiments.

## Why it matters
Opinions about interfaces are cheap and usually wrong; evaluation replaces them
with evidence. The methods differ by cost, when you can run them, and what they
catch — pick the wrong one and you either miss problems or spend a fortune finding
trivial ones. This is applied [[human-computer-interaction]].

## How it works
**Nielsen's 10 usability heuristics** (the checklist for expert inspection):
1. Visibility of system status
2. Match between system and the real world
3. User control and freedom (undo, exits)
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use (accelerators)
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

**Heuristic evaluation.** A handful of evaluators independently judge the interface
against the heuristics, then merge findings. *Discount usability*: 3–5 evaluators
catch the majority of problems at a fraction of a lab study's cost.

**Think-aloud usability testing.** Real users attempt real tasks while narrating
their thoughts; you watch where the mental model breaks. Nielsen's rule of thumb:
**≈5 users surface about 85% of problems**, so run small tests often rather than
one big one. This is formative (find problems), not a benchmark.

**Needfinding / contextual inquiry.** Observe users in their real context *before*
designing, to discover latent needs they cannot articulate. Personas and scenarios
summarize the findings.

**A/B testing (controlled online experiments).** Randomly assign users to variants,
measure a metric, and use statistics to decide. This is *summative* and quantitative
— it tells you which of two finished designs performs better, not *why*. It shares
its statistical core with [[hypothesis-testing-and-confidence-intervals]] and is the same
machinery as scientific [[randomized-controlled-trials]]. Pitfalls: peeking (early
stopping inflates false positives), multiple comparisons, and optimizing a
proxy metric that diverges from real value (Goodhart's law).

## Complexity & trade-offs
| Method | When | Cost | Finds |
|---|---|---|---|
| Heuristic evaluation | any prototype | low | violations of known principles |
| Think-aloud test | mid-fidelity+ | medium | *why* users fail |
| A/B test | shipped variants | high (needs traffic) | *which* variant wins |
| Needfinding | before design | medium | unmet needs |

## Pitfalls & gotchas
- **Leading users** — a question or hint contaminates think-aloud results.
- **A/B without a hypothesis** — mining many metrics guarantees false positives.
- **Formative vs summative confusion** — A/B tells you *that*, not *why*; you still
  need qualitative testing to fix a losing variant.
- **Small samples for quantitative claims** — five users find problems but cannot
  estimate a conversion rate.

## Worked example
A checkout flow drops users at the payment step. Think-aloud testing with five users
shows they can't find where to enter a coupon (heuristic 6, recognition vs recall).
You redesign, then A/B test the new flow against the old on live traffic; conversion
rises 4% with p < 0.01 across enough sessions to be conclusive.

## Related
- [[human-computer-interaction]] — the design principles being evaluated.
- [[interaction-design-and-cognitive-models]] — quantitative predictions to test against.
- [[hypothesis-testing-and-confidence-intervals]] — the statistics under A/B testing.
- [[experiment-design-and-causal-inference]] — randomization and confounds.

## Sources
Distilled from [[hci-texts-courses-and-seminal-papers]] (Nielsen *Usability
Engineering*; Lazar et al. *Research Methods in HCI*).

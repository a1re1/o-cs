---
title: Exploratory Data Analysis
type: concept
section: "10.1"
level: 300
tags: [exploratory-analysis, eda, distributions, outliers, data-quality, tukey]
sources: [data-science-texts-and-courses]
summary: Tukey's practice of summarizing and visualizing data to reveal distributions, relationships, outliers, and data-quality problems before formal modeling.
---

# Exploratory Data Analysis
**In one sentence.** EDA is the first, open-ended phase of analysis — plotting and
summarizing data to understand its distributions, relationships, and defects — before
committing to any model or hypothesis test.

## Why it matters
Modeling data you haven't looked at produces confident nonsense. EDA catches the
skew, the outliers, the missing-value patterns, and the "impossible" values that
would silently break a model, and it generates the hypotheses worth testing. Anscombe's
quartet is the standing proof that summaries without plots mislead; see
[[data-visualization]].

## How it works
**Summarize each variable (univariate).**
- **Distribution shape** — histograms, density plots, box plots; note skew, modality,
  and range.
- **Center and spread** — mean vs median (median resists outliers), standard deviation
  vs IQR.
- **Categoricals** — frequency tables and bar charts.

**Relationships (bivariate / multivariate).**
- **Numeric-numeric** — scatterplots; correlation (Pearson for linear, Spearman for
  monotonic). Correlation is not causation (see [[causal-inference]]).
- **Numeric-categorical** — grouped box/violin plots.
- **Many variables** — correlation heatmaps, pair plots, and
  [[svd-and-pca]] (PCA) to see structure; see [[svd-and-pca]].

**Data quality checks.**
- **Missing data** — how much, and is it missing at random or systematically? The
  pattern dictates whether to drop, impute, or model it.
- **Outliers** — real extreme values vs data-entry errors; investigate, don't reflexively
  delete.
- **Consistency** — units, duplicates, impossible values (age 200, negative counts).

The stance is **iterative and skeptical**: plot, form a question, re-plot, repeatedly —
Tukey's "detective work," distinct from confirmatory analysis.

## Complexity & trade-offs
- EDA is cheap and high-value but **open-ended**; it can rabbit-hole. Time-box it and
  aim it at the decisions the analysis must support.
- Exploring and testing on the *same* data invites false discoveries — see the pitfall
  below.

## Pitfalls & gotchas
- **Mean on skewed data** — a few billionaires make "average wealth" meaningless; use
  the median and show the distribution.
- **Ignoring the distribution** — reporting a mean without its spread or shape hides
  bimodality and outliers.
- **Data dredging / p-hacking** — testing many relationships found during exploration
  on the same data inflates false positives; confirm on held-out data or pre-register.
- **Deleting outliers to make the plot pretty** — you may be discarding the finding.

## Worked example
A dataset of response times has mean 250 ms — seemingly fine. A histogram reveals a
bimodal distribution: most requests at 80 ms and a second cluster at 900 ms (a slow
path). The mean described *neither* population. EDA surfaced a performance bug that a
summary statistic hid; see [[tail-latency-at-scale]].

## Related
- [[data-visualization]] — the plots EDA relies on.
- [[hypothesis-testing-and-confidence-intervals]] — confirmatory analysis after EDA.
- [[causal-inference]] — why correlations found in EDA aren't causes.
- [[data-wrangling-and-tidy-data]] — cleaning that precedes and interleaves with EDA.

## Sources
Distilled from [[data-science-texts-and-courses]] (Data 8/Data 100; Tukey EDA; McKinney).

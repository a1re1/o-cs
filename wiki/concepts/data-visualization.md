---
title: Data Visualization
type: concept
section: "9.4"
level: 300
tags: [data-visualization, tufte, chart-design, data-ink, small-multiples, dashboards]
sources: [data-visualization-texts-courses-and-seminal-papers]
summary: Encoding data into images humans read accurately — Tufte's principles (data-ink, chartjunk, graphical integrity), small multiples, and how to choose a chart that informs rather than misleads.
---

# Data Visualization
**In one sentence.** Data visualization maps data variables to visual properties of a
picture so that a human can perceive patterns, comparisons, and anomalies faster and
more accurately than from the numbers alone.

## Why it matters
Visualization is both an analysis tool (spot outliers and structure that summary
statistics hide) and a communication tool. Done badly it actively misleads — the same
image that reveals a trend can manufacture one. The principles here are the
difference between a chart that informs and chartjunk. It builds on
[[visual-encoding-and-perception]].

## How it works
**Tufte's principles:**
- **Data-ink ratio** — maximize the fraction of ink that encodes data; erase
  non-data ink (heavy gridlines, 3D effects, redundant borders).
- **Chartjunk** — decorative elements that carry no information distract and mislead;
  remove them.
- **Graphical integrity / the lie factor** — the visual magnitude of an effect should
  equal its magnitude in the data. Truncated y-axes, dual axes, and area-encoded
  quantities inflate or shrink effects.
- **Small multiples** — a grid of the same chart across categories or time lets the
  eye compare like with like; often clearer than one overloaded chart.
- **Maximize data density** while keeping it readable; **layering and separation** and
  clear labels over legends.

**Choosing a chart** follows from the *task* and *data type* (Munzner):
- Compare magnitudes across categories → **bar chart** (position/length, most accurate).
- Trend over time → **line chart**.
- Relationship between two quantities → **scatterplot**.
- Distribution → **histogram, box plot, or violin**.
- Part-to-whole → **stacked bar** (pie only for a few slices; area is hard to read).

**Anscombe's quartet / datasaurus** — four datasets with identical mean, variance,
and correlation but wildly different shapes — is the canonical argument for *always
plotting the data*, not trusting summaries alone. See [[exploratory-data-analysis]].

## Complexity & trade-offs
- More data-ink reduction is not always better: some redundancy (a light grid, direct
  labels) aids reading. The goal is *effective*, not *minimal*, ink.
- Interactivity (zoom, filter, tooltips) adds power but also complexity and a
  discoverability cost; static small multiples are often clearer for a report.

## Pitfalls & gotchas
- **Truncated or dual y-axes** exaggerate or fabricate effects — a top integrity
  violation.
- **Encoding quantity by area or color** (pie charts, bubble maps) — perceptually
  inaccurate; prefer position/length. See [[visual-encoding-and-perception]].
- **Rainbow (jet) colormaps** create false boundaries and fail for color-blind
  readers; use perceptually uniform, color-blind-safe scales (viridis).
- **Overplotting** hides density in big scatterplots; use transparency, binning, or
  hexbins.

## Worked example
A report claims sales "doubled." The bar chart's y-axis starts at 90 (not 0), so a
5% rise looks like a doubling — a lie factor far above 1. Fixing the axis to start at
0 shows the real, modest change. Adding small multiples per region reveals one region
drove all the growth, a story the single aggregate bar hid.

## Related
- [[visual-encoding-and-perception]] — why position beats color for quantities.
- [[grammar-of-graphics-and-interactive-visualization]] — how charts are specified and made interactive.
- [[exploratory-data-analysis]] — visualization as the first step of analysis.
- [[human-computer-interaction]] — visualization is perceptual HCI.

## Sources
Distilled from [[data-visualization-texts-courses-and-seminal-papers]] (Tufte;
Munzner; Wilke; Cleveland & McGill 1984).

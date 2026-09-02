---
title: Data Visualization — Texts, Courses, and Seminal Papers
type: source
section: "9.4"
level: 300
tags: [data-visualization, visual-encoding, perception, grammar-of-graphics, d3]
authors: Various
year: 2014
institution: Stanford, UW, UBC
url: https://clauswilke.com/dataviz/
license: mixed
format: texts+courses+papers
sources: []
summary: The data-visualization canon — Tufte, Munzner's Visualization Analysis and Design, Wilke's free text, the Heer/Stanford CS448B course, and the seminal work from Bertin and Cleveland-McGill to D3 and Vega-Lite.
---

# Data Visualization — Texts, Courses, and Seminal Papers (Various)

## What it is
The theory and practice of encoding data into images that human perception can read
accurately and quickly. It is perceptual [[human-computer-interaction]] applied to
data: which visual channel (position, length, color, area) to map each variable onto,
and how to design charts that inform rather than mislead.

## Key ideas
- **Visual encoding & perception** — the effectiveness ranking of visual channels
  (Cleveland-McGill); Bertin's retinal variables. See [[visual-encoding-and-perception]].
- **Design principles** — Tufte's data-ink ratio, chartjunk, small multiples,
  graphical integrity. See [[data-visualization]].
- **Grammar of graphics** — charts as compositions of data + mappings + geometries +
  scales (Wilkinson → ggplot2 → Vega-Lite). See [[grammar-of-graphics-and-interactive-visualization]].
- **Interaction** — Shneiderman's mantra "overview first, zoom and filter, details on
  demand." See [[grammar-of-graphics-and-interactive-visualization]].

## Chapter / lecture map
- **Tufte, *The Visual Display of Quantitative Information*** — data-ink, chartjunk,
  lie factor, small multiples; the aesthetic foundation.
- **Munzner, *Visualization Analysis and Design*** — the systematic framework: what,
  why, how (data/task/idiom abstraction).
- **Wilke, *Fundamentals of Data Visualization* (free)** — practical, principled
  chart choices.
- **Murray, *Interactive Data Visualization for the Web* (free)** — D3 hands-on.
- **Heer, Stanford CS448B / Berkeley CS294-10** — the graduate vis course.

## Notable claims & quotes
- Tufte: "**Above all else show the data.**" and "Graphical excellence is that which
  gives to the viewer the greatest number of ideas in the shortest time with the
  least ink in the smallest space."
- Cleveland & McGill (1984): position along a common scale is decoded most
  accurately; area and color the least — the empirical basis for preferring bar and
  dot plots over pie and bubble charts.

## Seminal papers
- **Bertin, *Semiology of Graphics* (1967)** — the retinal variables (position, size,
  value, texture, color, orientation, shape).
- **Cleveland & McGill (1984)** — experiments ranking graphical perception accuracy.
- **Shneiderman (1996)** — the visual-information-seeking mantra; task taxonomy.
- **Wilkinson, *The Grammar of Graphics* (1999)** → **Wickham, ggplot2** — declarative
  chart construction.
- **Bostock, Ogievetsky & Heer, D3 (2011)** — data-driven documents; the dominant
  web-vis toolkit.
- **Satyanarayan et al., Vega-Lite (2017)** — a high-level grammar for interactive graphics.

## What it adds
Where statistics summarizes data numerically, visualization exposes structure,
outliers, and error that summaries hide (Anscombe's quartet). It links to
[[exploratory-data-analysis]], [[human-computer-interaction]], and
[[frontend-frameworks-and-state-management]] (D3/Vega run in the browser).

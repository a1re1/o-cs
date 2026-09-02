---
title: Visual Encoding and Perception
type: concept
section: "9.4"
level: 300
tags: [visual-encoding, perception, retinal-variables, cleveland-mcgill, preattentive]
sources: [data-visualization-texts-courses-and-seminal-papers]
summary: The perceptual foundation of visualization — Bertin's retinal variables, the Cleveland-McGill accuracy ranking of visual channels, preattentive processing, and color perception.
---

# Visual Encoding and Perception
**In one sentence.** A visualization *encodes* data variables into visual channels
(position, length, angle, area, color, shape), and human perception decodes some
channels far more accurately than others — so channel choice determines whether a
chart is read correctly.

## Why it matters
This is the science under every "which chart?" decision. Cleveland & McGill turned
"pie charts are bad" from opinion into measured fact. Knowing the accuracy ranking
lets you assign your *most important* variable to your *most accurate* channel.

## How it works
**Bertin's retinal variables (1967):** position, size, value (lightness), texture,
color (hue), orientation, shape. Each suits different data:
- **Quantitative** (ordered, magnitudes): position, length, size, value.
- **Ordinal** (ordered categories): position, size, value.
- **Nominal** (unordered categories): hue, shape, texture.

**Cleveland-McGill effectiveness ranking** (most → least accurate for *quantitative*
comparison):
1. Position along a common scale
2. Position on non-aligned scales
3. Length
4. Angle / slope
5. Area
6. Volume, curvature
7. Color saturation / hue

Consequence: bar and dot plots (position/length) beat pie charts (angle/area) and
bubble charts (area) for reading magnitudes. Reserve color hue for *categories*, not
quantities.

**Preattentive processing.** Certain features — a differently colored dot, a longer
bar, a tilted line — "pop out" in under ~250 ms without serial search. Design uses
this to make the key data point instantly findable, and avoids it (too many popping
features) when it would create clutter.

**Color perception.**
- **Hue** is categorical and nominal; **lightness/saturation** read as ordered.
- Use **sequential** scales for ordered data, **diverging** scales for data with a
  meaningful midpoint, **categorical** palettes for nominal data.
- Prefer **perceptually uniform** colormaps (viridis) so equal data steps look equal;
  avoid rainbow/jet (non-uniform, false edges) and ensure **color-blind safety**
  (~8% of men have red-green deficiency) by not relying on hue alone.

**Gestalt principles** (proximity, similarity, connection, enclosure, common fate)
govern what viewers group — connection (a line) binds points more strongly than
proximity, which is why line charts read as series.

## Complexity & trade-offs
- The accuracy ranking is for *precise magnitude reading*; for *gist* or *pattern*,
  a less accurate channel (color heatmap) may communicate the whole faster.
- More channels encode more variables but overload perception; each added encoding
  costs readability.

## Pitfalls & gotchas
- **Encoding quantity by area/hue** — perceptually inaccurate and often misread by a
  factor of 2+.
- **Double-encoding by radius** — doubling a bubble's radius quadruples its area,
  overstating the value.
- **Hue for ordered data** — viewers can't rank hues; use lightness.
- **Relying on color alone** excludes color-blind readers; add shape/label/position.

## Worked example
To show revenue by 12 products, a pie chart forces angle/area comparison — viewers
can't tell the 4th from the 5th largest. A horizontal bar chart sorted by value maps
revenue to length along a common scale (rank #1 accuracy), so the ordering and gaps
are read instantly and accurately.

## Related
- [[data-visualization]] — the design principles built on this perception.
- [[grammar-of-graphics-and-interactive-visualization]] — encodings are the grammar's core.
- [[human-computer-interaction]] — perception and cognition in interfaces.

## Sources
Distilled from [[data-visualization-texts-courses-and-seminal-papers]] (Bertin 1967;
Cleveland & McGill 1984; Munzner; Ware *Information Visualization*).

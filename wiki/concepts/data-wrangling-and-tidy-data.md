---
title: Data Wrangling and Tidy Data
type: concept
section: "10.1"
level: 300
tags: [data-cleaning, tidy-data, pandas, tidyverse, joins, reshaping]
sources: [data-science-texts-and-courses]
summary: The reshape-clean-join work that dominates real analysis — Wickham's tidy-data principles, split-apply-combine, joins, and handling missing and messy values.
---

# Data Wrangling and Tidy Data
**In one sentence.** Data wrangling is the transformation of raw, messy data into a
clean, well-shaped table ready for analysis — the "tidy data" form where each variable
is a column, each observation a row, and each type of unit its own table.

## Why it matters
It is the majority of real analytical work and the part that most often goes wrong.
Tidy data makes every downstream step — plotting, grouping, modeling — uniform, because
tools ([[data-visualization]] grammars, models) expect that shape. Wrong shape or
silent join errors corrupt every conclusion drawn afterward.

## How it works
**Tidy data (Wickham).** Three rules: (1) each variable is a column, (2) each
observation is a row, (3) each observational unit forms a table. Untidy data has
values in column headers (years as columns), multiple variables in one column, or one
observation split across rows.

**Reshaping.** **Pivot longer / melt** turns wide data (columns per year) into long
(a `year` variable + a `value`); **pivot wider / spread** does the reverse. Long form is
usually the tidy, plottable one.

**Split-apply-combine (groupby).** Split rows into groups by a key, apply an
aggregation (sum, mean, count) or transform to each, and combine the results — the core
of pandas `groupby` and dplyr `group_by |> summarise`. It is the single-machine sibling
of [[mapreduce-and-dataflow]].

**Joins.** Combine tables on keys — inner (matches only), left/right (keep one side),
outer (keep all); the same semantics as SQL [[relational-model]] joins. The classic bug
is a **many-to-many** join silently multiplying rows.

**Cleaning.**
- **Missing values** — represented as NaN/NA; decide per variable to drop, impute
  (mean/median/model), or flag; document the choice.
- **Types & parsing** — dates, currencies, and categoricals parsed from strings; a
  single stray non-numeric value coerces a whole numeric column to text.
- **String normalization** — trim, case-fold, deduplicate near-identical categories
  ("USA"/"U.S.A."/"United States").

## Complexity & trade-offs
- Vectorized dataframe operations (pandas/Arrow, dplyr) are far faster than row loops;
  columnar formats ([[columnar-storage-and-data-formats]], Parquet/Arrow) speed I/O and
  analytics.
- In-memory dataframes hit a size wall; beyond it, move to out-of-core or distributed
  engines — see [[mapreduce-and-dataflow]].

## Pitfalls & gotchas
- **Silent join blow-up** — duplicate keys turn a join into a cross product; check row
  counts before and after.
- **Chained indexing / mutation surprises** in pandas produce copies vs views; use
  explicit `.loc` assignment.
- **Imputing before splitting** train/test leaks information; fit imputation on train
  only.
- **Losing rows to inner joins** — an inner join quietly drops unmatched observations,
  biasing the sample.

## Worked example
Sales data has a column per month (`jan`, `feb`, …) — untidy. Pivot longer to a
`month`/`sales` pair, parse `month` to a date, left-join a `region` lookup table
(checking the row count is unchanged), and `groupby(region)` to sum — now the data is
tidy and one line produces a per-region time series plot.

## Related
- [[exploratory-data-analysis]] — wrangling and EDA interleave.
- [[relational-model]] — join semantics come from relational algebra.
- [[mapreduce-and-dataflow]] — split-apply-combine at scale.
- [[columnar-storage-and-data-formats]] — Parquet/Arrow back fast dataframes.
- [[data-visualization]] — tidy data is what chart grammars expect.

## Sources
Distilled from [[data-science-texts-and-courses]] (Wickham tidy data / R4DS; McKinney pandas).

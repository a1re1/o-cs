---
title: Data Science & Analytics — Texts and Courses
type: source
section: "10.1"
level: 300
tags: [data-science, exploratory-analysis, pandas, inference, data-cleaning]
authors: Various
year: 2020
institution: Berkeley, Harvard, MIT
url: https://inferentialthinking.com/
license: free
format: courses+texts
sources: []
summary: The data-science teaching canon — Berkeley Data 8 and Data 100, Harvard CS109, McKinney's Python for Data Analysis and Wickham's R for Data Science — covering EDA, wrangling, inference, and the analysis workflow.
---

# Data Science & Analytics — Texts and Courses (Various)

## What it is
The applied discipline of turning data into understanding: acquiring, cleaning, and
exploring data, then drawing and communicating inferences. It sits between statistics,
programming, and domain knowledge, and is taught project- and notebook-first.

## Key ideas
- **Exploratory data analysis (EDA)** — Tukey's practice of letting the data reveal
  structure before modeling. See [[exploratory-data-analysis]].
- **Data wrangling / tidy data** — the unglamorous majority of the work: reshaping,
  joining, and cleaning. See [[data-wrangling-and-tidy-data]].
- **Inference & simulation** — resampling, the bootstrap, permutation tests,
  confidence intervals. See [[hypothesis-testing-and-confidence-intervals]].
- **The analysis workflow** — reproducible notebooks, from question to communication.

## Chapter / lecture map
- **Berkeley Data 8, *Computational and Inferential Thinking* (free)** — the
  simulation-first intro: tables, EDA, bootstrap, A/B tests, regression.
- **Berkeley Data 100, *Principles and Techniques of Data Science* (free)** — the
  rigorous follow-on: pandas, SQL, regression, gradient descent, PCA.
- **Harvard CS109** — the end-to-end data-science pipeline.
- **McKinney, *Python for Data Analysis* (free)** — pandas by its creator.
- **Wickham & Grolemund, *R for Data Science* (free)** — the tidyverse and tidy data.
- **Spiegelhalter, *The Art of Statistics*** — statistical thinking for a broad audience.

## Notable claims & quotes
- Tukey: "The greatest value of a picture is when it forces us to notice what we never
  expected to see." — the case for EDA.
- "80% of data science is cleaning data" — folklore, but it captures where the effort
  actually goes.

## What it adds
Bridges statistics and software engineering: it operationalizes
[[hypothesis-testing-and-confidence-intervals]] and [[causal-inference]], feeds
[[data-visualization]], and hands off to [[machine-learning-basics]] and
[[mapreduce-and-dataflow]] once the data is clean and understood.

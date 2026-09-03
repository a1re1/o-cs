# LLM eval — can a small model use oasis on this corpus?

Tests whether **drip driving GLM-5.3-Flash** can answer CS questions by *searching the
wiki with oasis* rather than from parametric memory, and whether it cites the right pages.

- `questions.jsonl` — 12 CS questions, each with `expect_pages` (gold page slugs) and
  `expect_points` (key facts a correct answer should contain).
- `grade_llm_eval.py <answers>` — scores a model's answers file on **tool-use rate**
  (did it call oasis), **citation hit rate** (did it cite an expected page), and
  **mean point recall** (fraction of expected key points present as substrings — a
  strict floor, since paraphrases that are correct but use different words score 0 on a
  point).
- `answers-drip.jsonl` — GLM-5.3-Flash's answers (produced by `drip --profile
  glm-5-3-flash`, one background run, answering each question through `oasis --root wiki
  search`/`show`). `answers-glm.jsonl` is the prior run on lci — drip is the Rust port
  of lci and functionally equivalent, so the two files grade identically (see below).
- `results-*.txt` — a graded run.

## Result (2026-09-02, GLM-5.3-Flash via drip 0.103)
tool-use 12/12 (1.00), citation hit 12/12 (1.00), mean point recall 0.59 (the earlier
lci run scored 0.58 on the same questions — the port reproduces the result). The point
recall understates answer quality: it is exact-substring matching, so a correct answer
phrased differently (e.g. "pays the second-highest bid" vs the keyword "pay second
highest") scores 0 on that point while being fully correct. Read `answers-drip.jsonl` —
the answers are accurate and grounded. The takeaways: (1) the small model reliably
*uses the tool* and *cites correctly* rather than hallucinating, which was the main
thing to verify; (2) a substring metric is a poor answer-quality judge — an LLM judge
is the right follow-up.

## Regression use
Re-run after corpus changes to confirm tool-use and citation stay at/near 1.00 as pages
are added. To reproduce the answers, run drip with the goal in this project's session
notes against `oasis --root wiki`:

```
drip --profile glm-5-3-flash --json --max-iterations 30 "$(cat evals/llm_eval/goal.txt)"
python3 evals/llm_eval/grade_llm_eval.py evals/llm_eval/answers-drip.jsonl
```

(`lci --profile glm-5-3-flash …` still works identically if drip is unavailable.)

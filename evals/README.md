# Search-quality eval harness

`evals/run_eval.py` measures how well the `oasis` CLI retrieves the right wiki
page for a set of natural-language queries. Each query row lists the page(s)
that *should* be found; the harness runs `oasis` once per query, scores the
returned ranking, prints an aligned table, and records the run so quality can
be tracked over time.

Everything is python3 stdlib only — no pip installs.

## Files

| path | what it is |
| --- | --- |
| `queries.jsonl` | the real query set (seeded with 3 examples, grown over time) |
| `run_eval.py` | the harness (metric functions are importable for tests) |
| `results/history.jsonl` | one JSON line per run (appended atomically) |
| `results/latest-<mode>.json` | per-query details of the most recent run |

## Query row format (`queries.jsonl`)

JSON Lines: one JSON object per line, no arrays. Blank lines and lines
starting with `#` are ignored.

```json
{"id": "1.1-001", "query": "how does BM25 scoring rank documents against a query", "relevant": ["concepts/bm25.md"], "section": "1.1", "kind": "concept"}
```

| field | required | meaning |
| --- | --- | --- |
| `id` | yes | stable identifier, `<section>-<seq>` (e.g. `1.1-001`); used in reports and `latest-<mode>.json` |
| `query` | yes | natural-language query passed to `oasis search` verbatim |
| `relevant` | yes | list of paths considered correct, **relative to the wiki root** (e.g. `concepts/induction.md`) |
| `section` | yes | curriculum section label (e.g. `1.1`); used for `--section` filtering and the per-section table |
| `kind` | yes | one of `concept`, `howto`, `compare`, `lookup`; descriptive only — it does not affect scoring today |

### Adding queries

1. Append one line per query to `evals/queries.jsonl`.
2. Pick `relevant` paths by checking the file actually exists under the wiki
   root and genuinely answers the query — one precise page beats several
   vague ones. A query is scored per query: it counts as found if **any**
   relevant path appears in the top-k.
3. Keep `id` unique and stable so runs stay comparable across edits.
4. Sanity-check the JSON with:

   ```sh
   python3 -c "import json,sys; [json.loads(l) for l in open('evals/queries.jsonl') if l.strip()]"
   ```

Editing the queries file changes its sha1, which is recorded in each history
entry (`queries_file_sha`), so a run is always traceable to the exact query
set it used.

## Running

From the repo root:

```sh
python3 evals/run_eval.py                                # hybrid mode, wiki/, -k 10, appends history
python3 evals/run_eval.py --mode lexical                 # lexical-only (no dense ONNX model)
python3 evals/run_eval.py --section 1.1                  # only rows whose section contains "1.1"
python3 evals/run_eval.py --verbose                      # also print each miss + its top-3 paths
python3 evals/run_eval.py --no-history                   # dry run: do not append to history
python3 evals/run_eval.py --compare                      # gate against the previous run of this mode
```

Flags:

| flag | default | meaning |
| --- | --- | --- |
| `--root` | `wiki` | wiki root directory passed to `oasis --root` |
| `--queries` | `evals/queries.jsonl` | JSONL query file |
| `-k` | `10` | top-k cutoff requested from oasis; recall is reported at 1/3/5/10 |
| `--mode` | `hybrid` | `hybrid` (dense + lexical) or `lexical` (`--lexical-only`); hybrid needs the ONNX model on first use and is slower |
| `--section` | none | only evaluate rows whose `section` field contains this substring |
| `--verbose` | off | print each miss with its top-3 returned paths |
| `--compare` | off | regression gate against the most recent history entry of the same mode (see below) |
| `--no-history` | off | do not append to `results/history.jsonl` (also skips nothing else) |

Each invocation rebuilds the oasis index, so the harness shells out to oasis
once per query; expect roughly one index build per run.

## Reading the table

```
metric       value
----------------------
recall@1        0.667
recall@3        1.000
...
```

The overall table is the mean over all (selected) queries of:

- **recall@k** — fraction of queries with ≥1 relevant path in the top-k
  results (`k` = 1, 3, 5, 10; `@10` is capped at the `-k` you asked for).
- **mrr** — mean reciprocal rank: `1/rank` of the first relevant hit, 0 if
  none.
- **ndcg@3** — nDCG at rank 3 with binary relevance; oasis returns
  chunk-level hits, so the same path is credited only at its first occurrence.

With `--verbose`, misses are listed below the tables as
`MISS query='...' top3=[...]` — use the top-3 paths to see what beat the
relevant page. For per-query detail (rank found, top paths), read
`evals/results/latest-<mode>.json`.

## History and the regression gate

Without `--no-history`, one line is appended to `evals/results/history.jsonl`:

```json
{"ts": "2026-09-02T00:00:00+00:00", "git_sha": "1a2b3c4", "mode": "lexical",
 "k": 10, "n_queries": 3, "n_pages": 3, "metrics": {"recall@1": 1.0, "...": 0.0},
 "per_section": {"1.1": {"recall@3": 1.0, "mrr": 1.0, "ndcg@3": 1.0}},
 "queries_file_sha": "d41d8cd9..."}
```

`--compare` finds the most recent history entry with the same `mode` and
prints the recall@3 delta:

- no entry for this mode yet → `compare: no previous history entry for this
  mode`, exit 0;
- recall@3 dropped by 0.02 or less → prints the delta, exit 0;
- recall@3 dropped by **more than 0.02** → prints the delta and
  `REGRESSION: ...` on stderr, **exit 1** (so it works as a CI gate).

Typical workflow:

```sh
python3 evals/run_eval.py --mode lexical          # baseline lands in history
python3 evals/run_eval.py --mode lexical --compare  # gate the next change
```

`--compare` itself appends a new history entry first (unless `--no-history`
is also given), so consecutive gated runs compare against the last recorded
run of that mode.

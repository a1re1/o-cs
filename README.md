# o-cs an LLM-maintained computer science wiki, searchable by `oasis`

A corpus of distilled CS knowledge (CS100 â CS500) built by reading the open courses,
textbooks, and seminal papers listed in [`curriculum.md`](curriculum.md) and compiling
them into an interlinked markdown wiki. It exists so that coding agents can run

```sh
oasis --root wiki search "when should I use an LSM tree instead of a B-tree" --json -k 5
```

and get back a ranked set of concept pages, worked examples, and trade-offs with
citations back to the source material.

**Status:** full curriculum §1–§12 ingested — 474 pages (336 concepts, 129 sources, 7 paths, 2 syntheses), 1312 search-eval queries, 0 orphans. See the report for benchmarks.

- **Wiki**: [`wiki/index.md`](wiki/index.md) (catalog) Â· [`wiki/log.md`](wiki/log.md) (timeline)
- **Schema & workflows**: [`CLAUDE.md`](CLAUDE.md)
- **Progress / handoff**: [`PROGRESS.md`](PROGRESS.md)
- **Experiments & findings report**: see the published artifact linked below (source: `reports/experiments.html`)
- **Search evals**: [`evals/`](evals/) Â· **Skills for agents**: [`skills/`](skills/)

## Experiments report

The long-running research log (search-quality benchmarks, oasis tuning experiments,
lci tool-use evals, what worked and what did not) is published here:

**â [o-cs Study Hall â experiments & findings](https://claude.ai/code/artifact/2203cff4-861c-431e-bf89-b0c1f63f6e26)**

Source of truth for the report is [`reports/experiments.html`](reports/experiments.html).

## How the wiki is built

Following Karpathy's "LLM wiki" pattern: raw sources are read once, distilled into
`wiki/concepts`, `wiki/sources`, `wiki/syntheses`, and `wiki/paths` pages with YAML
frontmatter and `[[wikilinks]]`; `scripts/build_index.py` regenerates the index and
log and fails on broken links. Every ingest adds eval queries so search quality is
measured, not assumed.

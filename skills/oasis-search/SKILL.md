---
name: oasis-search
description: Search the o-cs computer-science wiki with the oasis hybrid search engine — how to query it, read the JSON, drill into a hit's full text, and answer CS questions with citations. Use whenever you need specialized CS knowledge (algorithms, systems, theory, ML, security, IR, etc.) from this corpus.
---

# oasis-search — pull CS knowledge from the o-cs wiki

`oasis` is a hybrid **BM25 + dense (bge-small)** search engine over the markdown wiki in
`wiki/`. It fuses a lexical and a semantic ranking with reciprocal rank fusion, so both
exact-term and meaning-based queries work. Use it to answer computer-science questions
with citations instead of relying on memory.

## The three commands

**1. Search** — one query, ranked hits:
```
oasis --root wiki search "<your query>" --json -k 8
```
- `-k N` — number of hits (default 8; 5–10 is usually right).
- `--json` — machine-readable; prefer it so you can read `path` and `chunk_id`.
- `--lexical-only` — BM25 only (faster, ~0.5 s; skips the dense model). Omit for the full
  hybrid ranking (~4 s, better on paraphrases). Default is hybrid.
- `--per-page N` — max hits per document (default 1, so results span distinct pages;
  `--per-page 0` returns every matching chunk of a page).
- `--ignore '<glob>'` — exclude paths, e.g. `--ignore 'log/**'` to skip ingest logs.

**2. Show** — read the full text behind a hit:
```
oasis --root wiki show --path concepts/bm25.md          # whole page
oasis --root wiki show --chunk 227                        # one chunk by id from search --json
```

**3. Index** — smoke-test / stats:
```
oasis --root wiki index
```

## Reading `search --json`
An array of hits, best first. Each hit has:
- `path` — page path under `wiki/` (e.g. `concepts/bm25.md`). **This is your citation.**
- `heading_path` — the section the chunk came from (may be empty for the page head).
- `chunk_id` — pass to `show --chunk` to read that exact passage.
- `snippet` — the matched text; `score` — fused rank score; `chunks_matched` — how many
  chunks of this page matched.

## Workflow: answer a CS question
1. **Search** with the user's question, hybrid, `-k 8`.
2. **Scan** the top `path`s. If a page clearly answers it, `show --path <that page>` to
   read it in full before answering.
3. **Answer** in your own words, and **cite the page path(s)** you used, e.g.
   "(see `concepts/bm25.md`)". Prefer `concept` pages for how-things-work, `source`
   pages for "which textbook/course/paper", `synthesis` pages for comparisons and
   "when to use X vs Y", `path` pages for "what should I study / in what order".
4. If the first query misses, **rephrase**: add the practitioner's exact vocabulary
   (headings are boosted 2×), or try a keyword form and a question form. If lexical
   misses a paraphrase, the hybrid (default) usually catches it.

## Corpus map (where things live)
- `wiki/concepts/<slug>.md` — one page per concept, algorithm, data structure, theorem,
  system. The bulk of the knowledge.
- `wiki/sources/<slug>.md` — one page per course, textbook, or paper (what it is, key
  ideas, chapter map).
- `wiki/syntheses/<slug>.md` — cross-cutting comparisons (e.g. `oasis-search-engine`,
  `classic-essays-of-computing`).
- `wiki/paths/<slug>.md` — learning paths / prerequisite spines (`core-spine`,
  `systems-track`, `ai-ml-track`, `data-track`, …).
- Pages interlink with `[[slug]]` wikilinks; follow them with `show --path`.

## Query tips
- **Keyword queries** ("BM25 term frequency saturation") and **named things**
  ("Raft consensus", "AlphaFold") rank very well lexically.
- **Question / paraphrase queries** ("how do I stop a program using too much memory")
  benefit from hybrid (the default) — keep `--lexical-only` off for those.
- **Comparisons** ("BM25 vs dense retrieval", "SQL vs NoSQL") often land on a synthesis
  or the two concept pages; read both.
- Coverage is the whole CS curriculum §1–§12: math foundations, programming, algorithms,
  systems (arch/OS/networks/DB/distributed), theory, AI/ML, software engineering,
  security, human-centered computing, data & IR, and specialized areas.

## Don't
- Don't answer from memory when the corpus likely has it — search first.
- Don't cite a page you didn't `show`; the snippet may be out of context.
- Don't set `--per-page 0` for normal Q&A (it floods results with chunks of one page).

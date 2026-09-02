# 2026-09-02 — Ingest §12 Learning Paths (prerequisite spines)

**Created 7 path pages** in wiki/paths/, each a prerequisite spine linking existing
concept pages in order:
- core-spine (the backbone everyone takes: programming → discrete math → data structures
  → algorithms → architecture → OS → networks → databases → theory → software construction).
- systems-track, theory-track, ai-ml-track, software-engineering-track,
  human-centered-track, data-track — the six 400/500-level branches, each linking back to
  core-spine and cross-linking sibling tracks.

**Design:** paths link only real slugs (build_index confirms 0 new wanted from paths),
so a "learning path" / "what should I study for X" query lands on an ordered spine of
pages already in the corpus. data-track routes IR learners to [[oasis-search-engine]].

**Status:** build_index ok: 468 pages, 52 logs, 46 wanted, 0 orphans. Curriculum
§1–§12 now fully ingested.

**Next (engineering track):** E3 skills/oasis-search SKILL.md; E4 LLM eval via lci
(glm-5-3-flash only, background); E5 oasis PRs; scripts/lint.py; held-out paraphrase
eval. Plus the deferred report/chart/artifact/PROGRESS/memory bookkeeping for §9–§12.

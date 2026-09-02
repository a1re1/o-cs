#!/usr/bin/env python3
"""Lint the o-cs wiki for corpus-health issues that build_index.py does not gate on.

Reports (does not auto-fix):
  - under-linked pages: fewer than 2 inbound wikilinks (index.md excluded), per CLAUDE.md.
  - broken wikilinks: [[slug]] to a page that does not exist ("wanted"), with counts.
  - missing-page candidates: a slug wiki-linked >= THRESHOLD times but with no page yet.
  - unresolved contradictions: "> **Contradiction:**" blockquotes still present.
  - stale-claim markers: TODO / FIXME / "written from memory" / "as of <year>" flags.
  - thin pages: concept/synthesis pages under MIN_WORDS words (likely stubs).
  - frontmatter hygiene: sources: entries that point at non-existent source pages.

Exit code: 0 if no ERROR-level issues, 1 otherwise. WARN-level issues never fail.
Usage: scripts/lint.py [--strict]   (--strict: treat WARN as ERROR too)
"""
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
DIRS = ["concepts", "sources", "syntheses", "paths"]
WANT_THRESHOLD = 3      # a missing slug linked this many times => should probably exist
MIN_WORDS = 120         # concept/synthesis pages shorter than this look like stubs

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
            else:
                v = v.strip("'\"")
            fm[k.strip()] = v
    return fm

def main():
    strict = "--strict" in sys.argv
    pages = {}
    for d in DIRS:
        for p in sorted((WIKI / d).glob("*.md")):
            pages[p.stem] = {"path": p, "dir": d, "text": p.read_text()}

    inbound = collections.Counter()
    wanted = collections.Counter()
    for slug, pg in pages.items():
        fm = parse_frontmatter(pg["text"]) or {}
        pg["fm"] = fm
        for link in re.findall(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", pg["text"]):
            link = link.strip()
            if link in pages and link != slug:
                inbound[link] += 1
            elif link not in pages:
                wanted[link] += 1
        for src in (fm.get("sources") or []):
            if isinstance(src, str) and src in pages and src != slug:
                inbound[src] += 1

    errors, warns = [], []

    # under-linked pages (< 2 inbound), CLAUDE.md rule
    for slug, pg in pages.items():
        n = inbound[slug]
        if n == 0:
            errors.append(f"ORPHAN         {pg['dir']}/{slug}.md — 0 inbound links")
        elif n < 2:
            warns.append(f"under-linked   {pg['dir']}/{slug}.md — only {n} inbound link (want >=2)")

    # missing-page candidates: linked a lot but no page
    for slug, n in wanted.most_common():
        if n >= WANT_THRESHOLD:
            warns.append(f"wanted x{n}     [[{slug}]] linked {n}x but has no page — consider creating it")

    # unresolved contradictions
    for slug, pg in pages.items():
        for m in re.finditer(r">\s*\*\*Contradiction", pg["text"]):
            warns.append(f"contradiction  {pg['dir']}/{slug}.md — unresolved Contradiction blockquote")

    # stale-claim / placeholder markers
    stale_re = re.compile(r"\b(TODO|FIXME|written from memory|from memory)\b", re.I)
    for slug, pg in pages.items():
        if stale_re.search(pg["text"]):
            hits = sorted(set(m.group(0).lower() for m in stale_re.finditer(pg["text"])))
            warns.append(f"stale-marker   {pg['dir']}/{slug}.md — {', '.join(hits)}")

    # thin pages (concepts/syntheses only; sources/paths are legitimately shorter)
    for slug, pg in pages.items():
        if pg["dir"] in ("concepts", "syntheses"):
            body = re.sub(r"^---\n.*?\n---\n", "", pg["text"], flags=re.S)
            words = len(body.split())
            if words < MIN_WORDS:
                warns.append(f"thin-page      {pg['dir']}/{slug}.md — {words} words (< {MIN_WORDS}, likely a stub)")

    # frontmatter sources: pointing at a non-existent source page
    for slug, pg in pages.items():
        for src in (pg["fm"].get("sources") or []):
            if isinstance(src, str) and src and src not in pages:
                warns.append(f"bad-source-ref {pg['dir']}/{slug}.md — sources: [{src}] has no page")

    for w in warns:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    print(f"\nlint: {len(pages)} pages, {len(errors)} error(s), {len(warns)} warning(s), "
          f"{sum(1 for s in wanted if wanted[s] >= WANT_THRESHOLD)} missing-page candidate(s)")

    fail = len(errors) > 0 or (strict and len(warns) > 0)
    sys.exit(1 if fail else 0)

if __name__ == "__main__":
    main()

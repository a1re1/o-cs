#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["html2text", "pypdf", "requests"]
# ///
"""Fetch a URL (HTML or PDF) and print plain text. Caches raw bytes under raw/.

Usage: scripts/fetch.py URL [--max-chars N] [--grep REGEX]
"""
import hashlib, pathlib, re, sys
import requests, html2text
from pypdf import PdfReader
from io import BytesIO

RAW = pathlib.Path(__file__).resolve().parent.parent / "raw"
RAW.mkdir(exist_ok=True)

def fetch(url: str) -> tuple[bytes, str]:
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    meta = RAW / f"{key}.url"
    for p in RAW.glob(f"{key}.*"):
        if p.suffix != ".url":
            return p.read_bytes(), p.suffix
    r = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0 (o-cs corpus builder)"})
    r.raise_for_status()
    ctype = r.headers.get("content-type", "")
    suffix = ".pdf" if ("pdf" in ctype or url.lower().endswith(".pdf")) else ".html"
    (RAW / f"{key}{suffix}").write_bytes(r.content)
    meta.write_text(url)
    return r.content, suffix

def to_text(data: bytes, suffix: str) -> str:
    if suffix == ".pdf":
        reader = PdfReader(BytesIO(data))
        return "\n\n".join((p.extract_text() or "") for p in reader.pages)
    h = html2text.HTML2Text()
    h.ignore_images = True
    h.ignore_links = True
    h.body_width = 0
    return h.handle(data.decode("utf-8", errors="replace"))

if __name__ == "__main__":
    args = sys.argv[1:]
    url = args[0]
    max_chars = None
    grep = None
    if "--max-chars" in args:
        max_chars = int(args[args.index("--max-chars") + 1])
    if "--grep" in args:
        grep = re.compile(args[args.index("--grep") + 1], re.I)
    data, suffix = fetch(url)
    text = to_text(data, suffix)
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if grep:
        lines = text.splitlines()
        for i, l in enumerate(lines):
            if grep.search(l):
                print(f"{i}: {l[:200]}")
        sys.exit(0)
    if max_chars:
        text = text[:max_chars]
    print(text)

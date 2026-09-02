#!/usr/bin/env python3
"""Print a page range from a cached PDF text that has '— page N —' markers (MIT OCW style) or form-feeds.
Usage: scripts/pdfpages.py raw/file.txt START END"""
import re, sys
text = open(sys.argv[1]).read()
start, end = int(sys.argv[2]), int(sys.argv[3])
parts = re.split(r"— page (\d+|[ivxl]+) — #\d+", text)
# parts: [pre, pageno, body, pageno, body...]
out = []
for i in range(1, len(parts) - 1, 2):
    p = parts[i]
    if p.isdigit() and start <= int(p) <= end:
        out.append(parts[i + 1].strip())
print("\n".join(out))

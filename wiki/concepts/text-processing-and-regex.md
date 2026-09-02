---
title: Data wrangling — regular expressions, sed, awk, and the sort/uniq pipeline
type: concept
section: "2.6"
level: 100
tags: [regex, regular-expressions, grep, sed, awk, sort, uniq, cut, paste, tr, jq, data-wrangling, text-processing, capture-groups, greedy, anchors, character-classes, pcre]
sources: [missing-semester, tlcl-shotts]
summary: Most ad hoc data work is a pipeline — filter lines (grep), transform them (sed s///, awk with fields and patterns), aggregate (sort | uniq -c | sort -rn), reshape (cut, paste, tr, jq for JSON) — powered by regular expressions whose core is literals, ., character classes, anchors ^ $, quantifiers * + ? {n,m} (greedy by default; ? for lazy), alternation |, groups and backreferences; regexes are great for lexing and one-liners and wrong for nested structure.
---
# Text processing and regular expressions

**In one sentence.** `grep | sed | awk | sort | uniq -c | sort -rn | head` answers most "what's in
this log?" questions, and regex is the language all of them speak.

## Regular expressions (the core)
| Syntax | Meaning |
|---|---|
| `.` `\d` `\w` `\s` `[a-z]` `[^0-9]` | any char; digit; word char; whitespace; class; negated class |
| `^` `$` `\b` | start/end of line; word boundary |
| `*` `+` `?` `{n,m}` | 0+, 1+, 0/1, n–m times — **greedy**; add `?` for lazy (`.*?`) |
| `a\|b` `( )` `\1` | alternation; group (capture); backreference |
| `(?:…)` `(?=…)` `(?i)` | non-capturing; lookahead; flags |
Dialects: POSIX basic (`grep`, `sed`: escape `+ ? ( ) {`), extended (`grep -E`, `sed -E`), PCRE
(`grep -P`, most languages). Regexes recognise regular languages ([[finite-automata-and-regular-languages]])
— they cannot match balanced parentheses or nested JSON; use a parser ([[parsing]]). Test at
regex101/regexr; catastrophic backtracking (`(a+)+b`) is a DoS vector — prefer RE2-style engines
for untrusted input.

## The tools
- `grep -rn 'pat' dir`, `-i`, `-v` invert, `-o` only match, `-E`, `-P`; `rg` (ripgrep) for speed and
  gitignore awareness.
- `sed 's/old/new/g'`, `-E` for groups `s/(\w+)@(\w+)/\2 at \1/`, `-n '/start/,/end/p'` ranges,
  `d` delete, `-i` in place (careful).
- `awk -F, '$3 > 100 { sum += $3; n++ } END { print sum/n }'` — fields `$1..$NF`, patterns → actions,
  `BEGIN`/`END`, associative arrays: a real language for columns.
- Aggregate: `sort` (`-n`, `-k2`, `-r`, `-u`), `uniq -c` (adjacent!), `wc -l`, `cut -d: -f1`,
  `paste -sd,`, `tr 'a-z' 'A-Z'`, `tr -s ' '`, `comm`, `join`, `bc`, `datamash`; `jq '.items[] |
  select(.status=="fail") | .id'` for JSON; `column -t` to display; `xargs` to feed results to
  commands; `gnuplot`/`R` for quick plots.
- Binary: `xxd`, `od`, `strings`; `ffmpeg`/`convert` accept stdin/stdout too.

## Worked example (Missing Semester)
```sh
ssh host journalctl | grep sshd | grep "Disconnected from" \
 | sed -E 's/.*Disconnected from (invalid |authenticating )?user (.*) [^ ]+ port [0-9]+( \[preauth\])?$/\2/' \
 | sort | uniq -c | sort -nk1,1 | tail -n10 | awk '{print $2}' | paste -sd,
```
Filter → extract with a capture group → count → rank → reshape. Build it one stage at a time,
checking output after each pipe.

## Pitfalls
- `uniq` without `sort`; greedy `.*` eating too much; unescaped `.`; locale-dependent `sort`
  (`LC_ALL=C` for byte order); `sed -i` differences between GNU and BSD/macOS.
- Parsing structured formats (CSV with quotes, JSON, HTML) with regex — use `csvkit`/`jq`/a parser.

## Related
- [[shell-and-unix-tools]], [[finite-automata-and-regular-languages]], [[parsing]], [[debugging]].

## Sources
Missing Semester lecture 4; TLCL ch. 19–20.

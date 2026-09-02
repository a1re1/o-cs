---
title: String algorithms — substring search (KMP, Boyer–Moore, Rabin–Karp), suffix arrays, and edit distance
type: concept
section: "3.2"
level: 300
tags: [string-algorithms, substring-search, kmp, knuth-morris-pratt, boyer-moore, rabin-karp, rolling-hash, suffix-array, suffix-tree, lcp, z-algorithm, aho-corasick, edit-distance, longest-common-substring, regex-matching, dfa]
sources: [sedgewick-algorithms-4e, clrs, erickson-algorithms]
summary: Substring search beats the naive O(nm) by never re-reading text — KMP builds a failure function/DFA of the pattern for O(n + m) with no backup; Boyer–Moore skips ahead using the bad-character/good-suffix rules for sublinear typical time; Rabin–Karp compares rolling hashes for O(n + m) expected and extends to many patterns; Aho–Corasick matches a dictionary at once; suffix arrays/trees index the text for O(m log n) queries, longest repeated/common substrings and compression; edit distance/alignment is DP; regex matching is NFA simulation or a compiled DFA.
---
# String algorithms

**In one sentence.** Preprocess the pattern (KMP, Boyer–Moore, Rabin–Karp, Aho–Corasick) when the
text changes, preprocess the text (suffix arrays/trees) when the queries change, and reach for DP
when you need approximate matches.

## Substring search (Sedgewick 5.3, CLRS ch. 32)
| Algorithm | Preprocess | Search | Idea |
|---|---|---|---|
| Naive | — | O(nm) worst, ~n typical | try every offset |
| **KMP** | O(m) failure function / O(mR) DFA | O(n), never backs up in the text | on mismatch, the longest proper prefix of the matched part that is also a suffix tells where to resume; streaming-friendly |
| **Boyer–Moore** | O(m + R) | O(n/m) best, sublinear typical, O(nm) worst (O(n) with good-suffix) | scan the pattern right-to-left; bad-character rule skips ahead |
| **Rabin–Karp** | O(m) | O(n + m) expected | rolling hash h = (h − t[i]·R^{m−1})·R + t[i+m] mod Q; verify on hash match (Las Vegas) or trust it (Monte Carlo) — [[randomized-algorithms]]; multiple patterns via a hash set |
| Z-algorithm | O(n + m) | | Z[i] = longest common prefix of s and s[i..]; matches = Z ≥ m on pattern$text |
| **Aho–Corasick** | O(total pattern length) trie + failure links | O(n + #matches) | dictionary matching; grep -F, intrusion detection ([[tries]]) |
Library `find` uses two-way/SIMD variants (memchr, Crochemore–Perrin); grep uses Boyer–Moore
plus a lazy DFA.

## Indexing the text
- **Suffix array**: sorted suffix start positions; build in O(n log n) (prefix doubling) or O(n)
  (SA-IS); search by binary search O(m log n); with the **LCP array** (Kasai, O(n)) gives longest
  repeated substring, number of distinct substrings, longest common substring of two strings,
  and the Burrows–Wheeler transform (bzip2, BWA/Bowtie read aligners — [[source-coding-and-compression]]).
- **Suffix tree** (Ukkonen O(n)): the compressed trie of all suffixes; same queries in O(m);
  heavier in memory. FM-index = BWT + rank structures for compressed full-text search.

## Approximate matching
Edit distance / global alignment (Needleman–Wunsch), local alignment (Smith–Waterman), LCS —
O(nm) [[dynamic-programming]] with Hirschberg's linear-space path reconstruction; banded and
bit-parallel (Myers) variants; used in diff, spell-check, bioinformatics.

## Regular expressions
Thompson's construction: regex → NFA in O(m); simulate the NFA in O(nm) (RE2, grep) or compile to
a DFA (fast, possibly exponential states) — [[finite-automata-and-regular-languages]],
[[text-processing-and-regex]]. Backtracking engines (PCRE) add backreferences at the price of
exponential worst cases.

## Pitfalls
- Unicode: bytes vs code points vs grapheme clusters; case folding; normalization before search.
- Rolling-hash collisions with a small modulus (use 61-bit or double hashing; verify matches).
- KMP's DFA over a large alphabet (memory R·m) — use the failure-function form.

## Related
- [[tries]], [[dynamic-programming]], [[randomized-algorithms]], [[finite-automata-and-regular-languages]],
  [[source-coding-and-compression]], [[sorting]] (suffix sorting, radix), [[text-processing-and-regex]].

## Sources
Sedgewick ch. 5.3–5.5; CLRS ch. 32; Erickson (dynamic programming: edit distance).

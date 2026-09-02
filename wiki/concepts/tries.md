---
title: Tries, ternary search tries, and prefix structures
type: concept
section: "3.1"
level: 200
tags: [tries, prefix-tree, r-way-trie, ternary-search-trie, tst, radix-tree, patricia, autocomplete, longest-prefix-match, string-keys, suffix-trees]
sources: [sedgewick-algorithms-4e, open-data-structures-morin, berkeley-cs61b]
summary: A trie stores string keys as paths from the root, one character per edge, so search costs O(length of key) independent of the number of keys and supports prefix queries (autocomplete, longest prefix match, wildcard) that hash tables and BSTs cannot; R-way tries trade memory for speed, ternary search tries cut space by branching three ways per character, and radix/Patricia tries compress single-child chains — used in routers, dictionaries, and string indexes.
---
# Tries

**In one sentence.** Index strings by their characters instead of comparing whole keys — search
time depends on the key's length, and the structure "knows" prefixes.

## R-way trie (Sedgewick 5.2)
Node = array of R child links (R = alphabet size, e.g. 256) + optional value; the key is the path,
not stored in nodes. `get`: follow one link per character, O(L). `put`: create nodes along the
path. Space: up to R·(number of nodes) links — huge for large alphabets and sparse keys (R = 256,
1M keys ≈ hundreds of MB). Search miss often ends after a few characters (~log_R n typical).
Prefix ops: `keysWithPrefix(p)` (walk to p, collect subtree), `longestPrefixOf(s)` (routing tables,
tokenizers), `keysThatMatch("a.c")` wildcards. Deletion: remove value, prune nodes with no
children/value upward.

## Ternary search trie (TST)
Each node holds one character and three links (less, equal, greater); a search compares the
current character and goes left/right on mismatch, down on match. Space ≈ 3 links per node; time
O(L + ln n) expected; same prefix operations; handles large alphabets (Unicode) gracefully. Java
libraries: none built in; Sedgewick's `TST.java`.

## Compressed variants
- **Radix tree / Patricia trie**: collapse single-child chains into edges labelled with substrings
  — memory-efficient; IP routing (longest-prefix match), Linux kernel radix trees, Redis keys,
  Ethereum's Merkle-Patricia trie.
- **Suffix trie/tree/array**: all suffixes of a text for substring search in O(pattern length)
  after O(n) construction — [[string-algorithms]].
- **Binary tries** on integer keys (ODS ch. 13; x-fast/y-fast tries for O(log log U) predecessor).
- Burst tries, HAT-tries, ART (adaptive radix tree) as cache-conscious in-memory indexes.

## Trie vs hash table vs BST for strings
| | Hash table | Red-black BST | Trie / TST |
|---|---|---|---|
| search hit | O(L) (hash) + compare | O(L·log n) | O(L) / O(L + ln n) |
| prefix / range queries | no / no | range yes, prefix by range | yes, natural |
| memory | compact | ~3 pointers/key | R-way heavy, TST moderate |
| order | none | sorted | sorted |

## Pitfalls
- R-way trie memory blow-up with large R; use TST or radix tree.
- Unicode: index by bytes (UTF-8) or code points consistently.
- Storing the whole key in each node (defeats the purpose).

## Related
- [[hash-tables]], [[balanced-search-trees]], [[string-algorithms]], [[source-coding-and-compression]]
  (Huffman codes are tries), [[finite-automata-and-regular-languages]] (a trie is a DFA for a finite set).

## Sources
Sedgewick 5.2; ODS ch. 13; CS61B week 8.

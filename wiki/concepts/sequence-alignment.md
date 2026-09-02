---
title: Sequence Alignment
type: concept
section: "11.1"
level: 400
tags: [sequence-alignment, needleman-wunsch, smith-waterman, blast, dynamic-programming, edit-distance]
sources: [bioinformatics-texts-and-papers]
summary: Comparing biological sequences by finding the best correspondence under insertions, deletions, and substitutions — global (Needleman-Wunsch) and local (Smith-Waterman) dynamic programming, and the BLAST heuristic for search at scale.
---

# Sequence Alignment
**In one sentence.** Sequence alignment arranges two (or more) biological sequences to
maximize their similarity under a scoring scheme for matches, mismatches, and gaps,
revealing evolutionary and functional relationships.

## Why it matters
Alignment is the workhorse of bioinformatics: it detects homology (shared ancestry),
finds genes, maps sequencing reads to a reference, and underlies BLAST searches run
millions of times a day. It is also the canonical real-world application of
[[dynamic-programming]] and a generalization of **edit distance**.

## How it works
**Scoring.** Assign a score to each aligned column: positive for matches, negative for
mismatches (biology uses substitution matrices like BLOSUM/PAM) and for **gaps**
(insertions/deletions). Total alignment score is the sum.

**Global alignment — Needleman-Wunsch (1970).** Align sequences end to end. Fill a DP
table `F` where `F[i][j]` is the best score aligning the first `i` of one sequence with
the first `j` of the other:

```
F[i][j] = max( F[i-1][j-1] + s(xi, yj),   # match/mismatch
               F[i-1][j]   + gap,         # deletion
               F[i][j-1]   + gap )        # insertion
```

Traceback from `F[m][n]` reconstructs the alignment. O(mn) time and space.

**Local alignment — Smith-Waterman (1981).** Find the best-matching *substring* pair,
not end-to-end. Same recurrence with one change: clamp negative scores to 0
(`max(0, …)`), and start traceback from the highest cell. This finds conserved domains
within otherwise dissimilar sequences.

**Affine gap penalties.** Real indels are contiguous, so a gap of length `k` should cost
`open + k·extend`, not `k·gap`. This needs three DP layers (Gotoh's algorithm) but keeps
O(mn) time.

**BLAST (1990) — search at scale.** Exact DP against a database of billions of bases is
too slow. BLAST is a **seed-and-extend heuristic**: find short exact/near-exact word
matches (seeds), then extend them with local alignment only around promising seeds.
Trades guaranteed optimality for orders-of-magnitude speed, with statistical
significance (E-values) for hits.

## Complexity & trade-offs
- Needleman-Wunsch / Smith-Waterman: O(mn) time and space; space reducible to O(min(m,n))
  with Hirschberg's divide-and-conquer if only the score/one alignment is needed.
- BLAST: near-linear in practice but heuristic — it can miss weak homologies that full
  Smith-Waterman would find. Read mappers (BWA, Bowtie) go further, using the
  Burrows-Wheeler/FM-index for O(read length) lookups against a huge reference.

## Pitfalls & gotchas
- **Wrong scoring matrix / gap penalty** dominates the result; choose a matrix matched
  to the expected divergence (BLOSUM62 for moderate).
- **Global vs local mismatch** — using global alignment on sequences of very different
  lengths forces spurious gaps; use local for domain finding.
- **Alignment is not evolution** — the optimal alignment is a model artifact, not
  ground truth; multiple near-optimal alignments may exist.

## Worked example
Aligning `GATTACA` and `GCATGCU` with match +1, mismatch −1, gap −1: the
Needleman-Wunsch table's bottom-right holds the optimal global score, and traceback
yields an alignment inserting gaps to line up the shared `G…A…C…A` — the same DP that
computes edit distance, with biology's scoring.

## Related
- [[dynamic-programming]] — alignment is its flagship application.
- [[genome-assembly-and-protein-structure]] — read mapping uses alignment.
- [[string-algorithms]] — the FM-index behind fast read mappers.
- [[bayesian-networks-and-hmms]] — profile HMMs generalize alignment probabilistically.

## Sources
Distilled from [[bioinformatics-texts-and-papers]] (Needleman-Wunsch 1970;
Smith-Waterman 1981; Altschul et al. BLAST 1990; Durbin et al.).

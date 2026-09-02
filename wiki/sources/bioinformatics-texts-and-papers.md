---
title: Computational Biology & Bioinformatics — Texts and Papers
type: source
section: "11.1"
level: 400
tags: [bioinformatics, sequence-alignment, genome-assembly, protein-structure, hmms-bio]
authors: Compeau & Pevzner; Durbin et al.
year: 2015
institution: UCSD, MIT
url: https://www.bioinformaticsalgorithms.org/
license: mixed
format: texts+courses+papers
sources: []
summary: The bioinformatics canon — Compeau & Pevzner's Bioinformatics Algorithms, Durbin's Biological Sequence Analysis, MIT 6.047, and the seminal algorithms from Needleman-Wunsch and Smith-Waterman to BLAST, the Burrows-Wheeler aligner, and AlphaFold 2.
---

# Computational Biology & Bioinformatics — Texts and Papers

## What it is
The application of algorithms and statistics to biological data — DNA/RNA/protein
sequences, genomes, and structures. It is one of computing's great algorithm-driven
sciences: dynamic programming, string algorithms, HMMs, and now deep learning applied
to the molecules of life.

## Key ideas
- **Sequence alignment** — comparing sequences via dynamic programming and fast
  heuristics. See [[sequence-alignment]].
- **Genome assembly** — reconstructing a genome from short reads (de Bruijn graphs).
  See [[genome-assembly-and-protein-structure]].
- **Protein structure prediction** — from sequence to 3D fold (AlphaFold). See
  [[genome-assembly-and-protein-structure]].
- **Probabilistic models of sequences** — HMMs for gene finding and profiles. See
  [[bayesian-networks-and-hmms]].

## Chapter / lecture map
- **Compeau & Pevzner, *Bioinformatics Algorithms* / Coursera + Rosalind** —
  problem-driven: alignment, assembly, motif finding, phylogenetics.
- **Durbin, Eddy, Krogh & Mitchison, *Biological Sequence Analysis*** — the
  probabilistic-models classic: pairwise alignment, HMMs, profile HMMs.
- **MIT 6.047/6.878 (Kellis)** — computational biology with genomics.

## Notable claims & quotes
- Sequence alignment is the "hello world" of bioinformatics and a textbook application
  of [[dynamic-programming]] — Needleman-Wunsch predates most of CS's DP literature.
- AlphaFold 2 (2021) is widely regarded as a landmark: deep learning solving a
  50-year-old grand-challenge (the protein-folding problem) to near-experimental accuracy.

## Seminal papers
- **Needleman-Wunsch (1970)** — global alignment by dynamic programming.
- **Smith-Waterman (1981)** — local alignment (best-matching subsequence).
- **Altschul et al., BLAST (1990)** — fast heuristic alignment search; the most-cited
  bioinformatics tool.
- **Burrows-Wheeler transform / BWA (Li & Durbin)** — read mapping via the
  [[string-algorithms]]-style FM-index.
- **Jumper et al., AlphaFold 2 (2021)** — deep-learning protein structure prediction.

## What it adds
Grounds abstract algorithms in a high-impact domain and connects to
[[dynamic-programming]], [[bayesian-networks-and-hmms]], string indexing, and
[[deep-learning-basics]] (AlphaFold). It is also a driver of [[big-data-mining-texts-and-papers]]
(genomic data at scale).

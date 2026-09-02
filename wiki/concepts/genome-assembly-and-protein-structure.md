---
title: Genome Assembly and Protein Structure
type: concept
section: "11.1"
level: 400
tags: [genome-assembly, de-bruijn-graph, protein-folding, alphafold, sequencing]
sources: [bioinformatics-texts-and-papers]
summary: Reconstructing a genome from short sequencing reads via de Bruijn graphs, and predicting a protein's 3D fold from its amino-acid sequence — the AlphaFold breakthrough.
---

# Genome Assembly and Protein Structure
**In one sentence.** Two grand-challenge inverse problems: assemble a whole genome from
millions of short overlapping reads (a graph problem), and predict a protein's
three-dimensional structure from its one-dimensional amino-acid sequence (now a deep
-learning problem solved by AlphaFold).

## Why it matters
Sequencing machines read only short fragments, so *assembly* is required to get a
genome at all; it is a beautiful application of graph theory at massive scale. And a
protein's function follows from its **fold**, so predicting structure from sequence —
the "protein folding problem," open for 50 years — unlocks drug design and biology;
AlphaFold 2 largely solved it in 2021.

## How it works
**Genome assembly via de Bruijn graphs.** Modern short-read assembly:
1. Break every read into overlapping **k-mers** (length-k substrings).
2. Build a **de Bruijn graph**: nodes are (k−1)-mers, and each k-mer is an edge from its
   prefix to its suffix.
3. The genome corresponds to an **Eulerian path** (use every edge once) through the
   graph — which is efficiently findable, unlike the Hamiltonian-path formulation of
   older overlap-layout-consensus methods (NP-hard).

Reality complicates this: sequencing **errors** create false edges/tips (trimmed),
**repeats** longer than k create tangles the graph can't resolve (the fundamental limit,
addressed by longer reads), and both strands must be handled.

**Protein structure prediction — AlphaFold 2 (2021).** Input: an amino-acid sequence.
Key ingredients:
- A **multiple sequence alignment (MSA)** of evolutionarily related proteins — columns
  that co-evolve indicate residues that are physically close (coevolution signal).
- The **Evoformer**, an attention-based network ([[transformers-and-attention]]) that
  reasons jointly over the MSA and a residue-pair representation.
- A **structure module** that outputs 3D atom coordinates directly, trained end to end,
  with a confidence score (pLDDT) per residue.

It reached near-experimental accuracy on most proteins, and its released database
covers hundreds of millions of structures — a step-change for structural biology.

## Complexity & trade-offs
- De Bruijn assembly is near-linear in total read length (vs the NP-hard Hamiltonian
  overlap formulation), which is why it scales to human genomes; the price is
  sensitivity to `k` (small k → tangled repeats, large k → gaps from low coverage).
- AlphaFold trades interpretability and physical first-principles for learned accuracy;
  it needs a good MSA, so it is weaker on orphan proteins with few homologs and on
  effects of single mutations or dynamics.

## Pitfalls & gotchas
- **Repeats** are the core assembly limit — regions longer than the read/k cannot be
  resolved uniquely, producing fragmented or misjoined assemblies; long-read sequencing
  (Nanopore/PacBio) mitigates this.
- **Choosing k** trades repeat resolution against coverage of the graph.
- **AlphaFold confidence** — low-pLDDT regions may be disordered or simply wrong; use
  the per-residue confidence, don't trust the whole model uniformly.

## Worked example
Assembling `...ATGCGTGCA...` from reads: split into 4-mers, build the de Bruijn graph,
and walk an Eulerian path to recover the contig — where a k-mer shared by two genome
locations (a repeat) creates a branch node the path cannot traverse unambiguously,
which is exactly where the assembly breaks into separate contigs.

## Related
- [[sequence-alignment]] — reads are aligned to references and to each other.
- [[graph-representations]] — de Bruijn/Eulerian-path formulation.
- [[transformers-and-attention]] — AlphaFold's Evoformer is attention-based.
- [[deep-learning-basics]] — the learning behind structure prediction.

## Sources
Distilled from [[bioinformatics-texts-and-papers]] (Compeau & Pevzner assembly;
Jumper et al. AlphaFold 2 2021).

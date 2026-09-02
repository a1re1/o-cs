---
title: Classic Essays of Computing (Distilled)
type: synthesis
section: "11.6"
level: 300
tags: [no-silver-bullet, worse-is-better, essential-complexity, research-practice, simplicity]
sources: [computing-history-and-classic-essays]
summary: The recurring wisdom of computing's great essays — Brooks on essential vs accidental complexity, Gabriel's Worse Is Better, Hamming on doing great research, Dijkstra/Hoare on simplicity, and how these tensions still shape practice.
---

# Classic Essays of Computing (Distilled)
**In one sentence.** A handful of essays keep being rediscovered because they name
tensions that never go away — complexity vs simplicity, the right thing vs the shippable
thing, and how to choose problems worth solving.

## Why it matters
These essays are the field's accumulated taste. They explain *why* the engineering
practices in §7 exist and why silver-bullet claims should be met with skepticism. They
are short, quotable, and load-bearing in real technical arguments.

## The essays and their claims
**Brooks, "No Silver Bullet" (1986) — essential vs accidental complexity.** Software
difficulty splits into **accidental** complexity (from our tools, removable) and
**essential** complexity (inherent in the problem, irreducible). Past 10× gains
(high-level languages, time-sharing) removed accidental complexity; no single future
advance will give another 10× because what remains is essential — conceptual design of
complex, changeable, invisible systems. The antidotes are incremental: grow software,
buy don't build, great designers. This is the intellectual immune system against hype
(including, today, overclaimed AI-will-solve-everything). See
[[software-engineering-fundamentals]].

**Gabriel, "Worse Is Better" (1991) — the shippable beats the perfect.** The "MIT/right
thing" approach prizes correctness and completeness; the "New Jersey/worse is better"
approach prizes **simplicity of implementation** even at some cost to correctness and
completeness. Gabriel observed the simpler design spreads faster, gets adopted, and is
improved in place — so "worse" (simpler, incomplete) often wins in the real world. The
enduring debate behind Unix/C's success and countless "good enough" designs.

**Hamming, "You and Your Research" (1986) — doing work that matters.** Work on
**important problems** (most people don't, then wonder why their work doesn't matter);
keep your "door open" to serendipity; tolerate the ambiguity of believing your approach
while doubting enough to correct it; compound small consistent effort. Advice for
choosing problems, not solving them.

**Dijkstra & Hoare — simplicity as a moral stance.** Dijkstra's "Go To… Considered
Harmful" (structured programming) and "The Humble Programmer" argue our limited minds
make **simplicity and discipline** non-negotiable. Hoare's "The Emperor's Old Clothes"
warns that ambition and features breed unreliability, and confesses the **null
reference** as his "billion-dollar mistake" — a design regret that shaped modern
languages' option types.

**Parnas & the modularity thread.** Parnas's information-hiding (1972) is the concrete
technique these essays' "manage complexity" imperative points to; see
[[modularity-and-information-hiding]].

## The recurring tensions
- **Essential vs accidental complexity** — know which you're fighting; tools only remove
  accidental.
- **Right thing vs worse-is-better** — completeness and correctness vs simplicity and
  adoptability; both have their place.
- **Simplicity as discipline** — the through-line from Dijkstra to Hoare to modern
  minimalism.

## Related
- [[software-engineering-fundamentals]] — Brooks's essential complexity in practice.
- [[modularity-and-information-hiding]] — Parnas, the technique behind the philosophy.
- [[technical-debt-and-maintenance]] — accidental complexity accreting over time.
- [[computing-history-and-classic-essays]] — the source collection.

## Sources
Distilled from [[computing-history-and-classic-essays]] (Brooks 1986; Gabriel 1991;
Hamming 1986; Dijkstra 1968/1972; Hoare 1980).

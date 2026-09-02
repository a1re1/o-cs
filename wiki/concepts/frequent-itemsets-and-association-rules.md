---
title: Frequent Itemsets and Association Rules
type: concept
section: "10.2"
level: 400
tags: [frequent-itemsets, association-rules, apriori, fp-growth, market-basket, support-confidence-lift]
sources: [big-data-mining-texts-and-papers]
summary: Market-basket analysis — finding sets of items that co-occur often (frequent itemsets via Apriori/FP-growth) and turning them into if-then association rules scored by support, confidence, and lift.
---

# Frequent Itemsets and Association Rules
**In one sentence.** Given many transactions (baskets of items), find item combinations
that appear together frequently, and derive rules like "{diapers} ⇒ {beer}" scored by
how often and how reliably they hold.

## Why it matters
Market-basket analysis powers "customers who bought X also bought Y," store layout,
cross-selling, and web-usage and bioinformatics pattern mining. Its central algorithmic
idea — the **downward-closure** pruning of Apriori — is a template for searching
exponential candidate spaces efficiently.

## How it works
**Definitions.** For an itemset `I`:
- **Support** = fraction of transactions containing `I` (how common).
- A **rule** `A ⇒ B` has **confidence** = support(A∪B)/support(A) (how reliable) and
  **lift** = confidence/support(B) (how much more than chance; lift > 1 = positive
  association).

**Frequent itemset mining** — find all itemsets with support ≥ a threshold. The search
space is exponential (all subsets of items), so:

**Apriori (Agrawal & Srikant 1994)** exploits the **downward-closure / anti-monotone**
property: *every subset of a frequent itemset is frequent* — equivalently, if an
itemset is infrequent, all its supersets are too. So generate candidate `k`-itemsets
only from frequent `(k−1)`-itemsets, prune any with an infrequent subset, then scan the
data to count them. One data pass per level `k`.

**FP-growth** avoids candidate generation: compress the transactions into a prefix tree
(the **FP-tree**) and mine it recursively; usually much faster than Apriori because it
scans the data only twice and never materializes candidates.

**Rule generation.** From each frequent itemset, form rules and keep those meeting a
minimum confidence (and often minimum lift).

## Complexity & trade-offs
- Apriori does one pass per level and can generate a huge number of candidates when the
  support threshold is low; FP-growth trades that for memory to hold the tree.
- The number of frequent itemsets can explode; mine **closed** or **maximal** itemsets
  (compact representations) to control output size.

## Pitfalls & gotchas
- **Confidence is misleading alone** — a rule can have high confidence just because `B`
  is common; **lift** (or conviction) corrects for `B`'s base rate.
- **Spurious rules from low support** — with millions of items, some co-occur by chance;
  keep support meaningful and correct for multiple comparisons.
- **The diapers-and-beer story** is largely apocryphal — a caution that a striking rule
  is a hypothesis, not a proven cause (see [[causal-inference]]).

## Worked example
10,000 transactions. {diapers} appears in 600 (support 6%), {diapers, beer} in 300.
Rule {diapers} ⇒ {beer}: confidence = 300/600 = 50%. If beer alone has support 20%,
lift = 0.50/0.20 = 2.5 — buyers of diapers are 2.5× as likely to buy beer as a random
basket, a genuinely positive association worth acting on.

## Related
- [[similarity-search-and-lsh]] — the other MMDS pattern-at-scale technique.
- [[recommender-systems]] — "bought together" is item-item co-occurrence.
- [[causal-inference]] — an association rule is not a cause.
- [[mapreduce-and-dataflow]] — counting itemsets distributes across a cluster.

## Sources
Distilled from [[big-data-mining-texts-and-papers]] (MMDS ch. 6; Agrawal & Srikant 1994; FP-growth).

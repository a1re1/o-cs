---
title: Hash tables — hash functions, chaining, open addressing, resizing
type: concept
section: "3.1"
level: 200
tags: [hash-tables, hashing, hash-function, separate-chaining, open-addressing, linear-probing, load-factor, resizing, collisions, tombstones, universal-hashing, tabulation-hashing, robin-hood, swiss-table, hashcode-equals, dictionaries, sets]
sources: [sedgewick-algorithms-4e, open-data-structures-morin, berkeley-cs61b, clrs]
summary: A hash table stores key–value pairs in an array indexed by hash(key) mod M; collisions are resolved by separate chaining (linked lists per slot, average O(1 + α)) or open addressing (linear probing, tombstones for deletion, needs α < 1), the table resizes by doubling to keep the load factor bounded (O(1) amortized), and everything rests on a good hash function — deterministic, consistent with equality, uniform — with universal or randomized hashing to defeat adversarial keys.
---
# Hash tables

**In one sentence.** Turn the key into an array index; handle the inevitable collisions; keep the
array from getting too full — expected O(1) insert/lookup/delete, and the workhorse of practical
programming.

## Hash functions (Sedgewick 3.4)
- Requirements: **deterministic** (equal keys → equal hashes; must be consistent with `equals`/
  `Eq` — [[equality-and-hashing]]), cheap, and **uniform** over [0, M).
- Integers: modular hashing `k mod M` with M prime, or multiplicative hashing `(a·k) >> (w − d)`
  with odd `a` (ODS) — fast, no modulo. Strings: polynomial rolling `h = (R·h + c) mod M` (Java
  R = 31); compound keys combine fields the same way. Floats: hash the bit pattern.
- **Uniform hashing assumption**: analysis assumes keys spread uniformly and independently.
  Adversaries can violate it (hash-flooding DoS) — mitigate with **universal hashing** (pick the
  function at random from a family: `((a·k + b) mod p) mod M`), **tabulation hashing**, or keyed
  SipHash (Python, Rust `HashMap` default).
- Cryptographic hashes are a different tool (collision *resistance*) — [[hash-functions-and-integrity]].

## Collision resolution
| Scheme | Structure | Cost (α = n/M) | Notes |
|---|---|---|---|
| **Separate chaining** | array of linked lists (or small vectors) | search ≈ 1 + α/2 hit, α miss | simple, tolerates α > 1, extra pointers |
| **Linear probing** | one array; on collision try i+1, i+2, … | ≈ ½(1 + 1/(1−α)²) miss (Knuth) | cache-friendly; clustering; keep α ≤ ½; deletion needs re-insertion of the cluster or **tombstones** |
| Quadratic / double hashing | probe i + c₁j + c₂j² / i + j·h₂(k) | fewer clusters | double hashing needs h₂ coprime with M |
| Robin Hood / Swiss tables | probing with displacement bookkeeping / SIMD metadata bytes | very low variance, high α | what modern `HashMap`s (Rust hashbrown, abseil) use |
| Cuckoo hashing | two tables, two hashes, kick-out on collision | O(1) worst-case lookup | inserts may rebuild |

## Resizing
Double M when α exceeds a threshold (chaining ~8 in Java, probing ½), halve when it falls below
⅛ — rehash all keys, O(n) once, **O(1) amortized** per operation ([[amortized-analysis]]). Power-of-
two sizes let `h & (M − 1)` replace mod but expose low bits (mix first). Incremental rehashing for
latency-sensitive systems.

## Operations and costs
Insert/search/delete: expected O(1) under uniform hashing; worst case O(n) (all keys collide).
No ordering: iteration order is arbitrary (and changes on resize — never depend on it); for ordered
queries use [[balanced-search-trees]]. Memory: chaining ≈ n·(key+value+pointer) + M pointers;
probing ≈ M·(key+value).

## Pitfalls
- Overriding `equals` without `hashCode` (or `Eq` without `Hash`): equal keys land in different
  buckets — the classic bug ([[equality-and-hashing]]).
- Mutable keys: mutating a key after insertion silently loses it.
- Bad hash (e.g. `hash = 1`, or using only high bits with power-of-two tables) → O(n).
- Iterating while inserting (rehash mid-iteration); relying on iteration order.
- Floating-point keys and NaN ≠ NaN.

## Related
- [[equality-and-hashing]], [[amortized-analysis]], [[balanced-search-trees]], [[arrays-and-linked-lists]],
  [[probabilistic-analysis-of-algorithms]] (expected costs), [[hash-functions-and-integrity]],
  [[caches-and-memory-hierarchy]] (why probing wins in practice).

## Sources
Sedgewick 3.4; ODS ch. 5; CS61B week 7; CLRS ch. 11.

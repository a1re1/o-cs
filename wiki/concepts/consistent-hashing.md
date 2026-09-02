---
title: Consistent hashing and rendezvous hashing
type: concept
section: "3.3"
level: 400
tags: [consistent-hashing, rendezvous-hashing, hash-ring, virtual-nodes, load-balancing, sharding, distributed-caching, akamai, dynamo, cassandra, jump-hash, bounded-loads]
sources: [cs168-modern-algorithmic-toolbox]
summary: Assigning keys to n servers by hash(key) mod n remaps almost every key when n changes; consistent hashing (Karger et al., the Akamai paper) places both servers and keys on a hash ring and sends each key to the next server clockwise, so adding or removing a server moves only ~1/n of the keys, with virtual nodes to smooth load and replication to the next k servers — the basis of CDNs, Dynamo/Cassandra partitioning, and distributed caches; rendezvous (highest-random-weight) hashing and jump hash are simpler alternatives, and bounded-load variants cap hot spots.
---
# Consistent hashing

**In one sentence.** Hash servers *and* keys into the same circle so that membership changes move
only the keys that must move.

## The problem (CS168 lecture 1)
Distributed cache with n servers: `server = h(key) mod n`. When n → n+1, a (n/(n+1)) fraction of
keys change server — every cache misses at once ("thundering herd"). Requirements: balanced load,
minimal disruption on join/leave, no central directory, agreement among clients with only the
server list ([[hash-tables]] for the single-machine case).

## The ring (Karger, Lehman, Leighton, Levine, Lewin, Panigrahy 1997)
Hash each server id to a point on [0, 2³²); hash each key; assign the key to the first server
clockwise. Adding a server takes over a contiguous arc from one neighbour (expected 1/n of keys);
removing one hands its arc to the next. Lookup: binary search in a sorted array of server points
(O(log n)) — [[balanced-search-trees]]. **Virtual nodes**: give each server ~100 points so arcs
are balanced (load within ~1 ± O(1/√v)) and heterogeneous capacity is easy (more points for
bigger machines). **Replication**: store each key on the next k distinct servers clockwise —
Dynamo's preference list. Properties: balance, monotonicity (keys only move to new servers),
spread and load bounded across differing client views.

## Alternatives
- **Rendezvous / highest-random-weight** (Thaler–Ravishankar): for key k pick argmax_s h(k, s).
  O(n) per lookup but trivially minimal disruption, no virtual nodes, and top-k replication by
  ranking; used in Ceph CRUSH-style placement.
- **Jump consistent hash** (Google): O(log n) arithmetic, no memory, but only supports adding/
  removing the *last* bucket — good for numbered shards.
- **Maglev hashing** (Google load balancers): lookup table with permutations; minimal disruption
  and O(1) lookup.
- **Consistent hashing with bounded loads** (Mirrokni et al.): cap each server at (1+ε)·average;
  overflow to the next server — used in Vimeo/Google to kill hot spots.

## Where it shows up
CDNs (Akamai), Memcached client libraries (Ketama), Dynamo, Cassandra, Riak, Chord DHT (ring +
finger tables for O(log n) routing without knowing all nodes), Kafka partition assignment,
Envoy/Nginx upstream hashing, sharded databases ([[distributed-systems-basics]],
[[replication-and-partitioning]]).

## Pitfalls
- Few points per server → wildly uneven arcs; always use virtual nodes.
- Non-uniform hash (MD5/SHA/xxHash fine; `hashCode` of ints is not).
- Hot keys still overload one server (need bounded loads or key splitting).
- Changing the hash function or virtual-node count is a full remap.

## Related
- [[hash-tables]], [[replication-and-partitioning]], [[distributed-systems-basics]],
  [[streaming-and-sketching]], [[balanced-search-trees]].

## Sources
CS168 lecture 1 and Karger et al. 1997; DeCandia et al. (Dynamo) 2007; Lamping & Veach 2014.

---
title: Distributed systems texts — van Steen & Tanenbaum (free), Lynch's Distributed Algorithms, Cachin/Guerraoui/Rodrigues Reliable and Secure Distributed Programming, Petrov's Database Internals, and the 6.824 paper list
type: source
section: "4.6"
level: 400
tags: [distributed-systems-textbook, van-steen, tanenbaum, lynch, distributed-algorithms, cachin, guerraoui, reliable-distributed-programming, petrov, database-internals, paper-list]
sources: []
authors: [Maarten van Steen, Andrew Tanenbaum, Nancy Lynch, Christian Cachin, Rachid Guerraoui, Luís Rodrigues, Alex Petrov]
year: 2017
institution: various
url: https://www.distributed-systems.net/index.php/books/ds4/
license: mixed (van Steen & Tanenbaum free PDF)
format: pdf
summary: Van Steen & Tanenbaum (4th ed., free) is the broad systems text (architectures, processes, communication/RPC, naming, coordination — clocks, mutual exclusion, election, consistency and replication, fault tolerance — 2PC, reliable multicast, recovery, security); Lynch's Distributed Algorithms is the rigorous treatment of synchronous and asynchronous models, impossibility results (FLP, Byzantine bounds) and proofs; Cachin, Guerraoui & Rodrigues build the abstractions stack — failure detectors, reliable/causal/total-order broadcast, shared memory registers, consensus, Byzantine variants — as modular pseudocode with properties; Petrov's Database Internals covers storage engines (B-trees, LSM) and distributed systems (failure detection, leader election, replication and consistency, anti-entropy, transactions, consensus) for practitioners; and the 6.824 reading list is itself a curated corpus of the field's primary sources.
---
# Distributed systems textbooks

## What they are
- **Van Steen & Tanenbaum**: 1 introduction (goals: resource sharing, transparency,
  openness, scalability; the fallacies of distributed computing); 2 architectures (client–
  server, peer-to-peer, middleware); 3 processes (threads, virtualization, clients/servers,
  code migration); 4 communication (RPC, message-oriented, multicast); 5 naming (flat, structured
  — DNS, attribute-based); 6 coordination (clock synchronization — NTP, Berkeley; logical
  clocks; mutual exclusion; election — bully/ring; location systems; gossip); 7 consistency
  and replication (data-centric models — sequential, causal; client-centric — monotonic
  reads/writes, read-your-writes; replica management; consistency protocols — primary-based,
  quorum); 8 fault tolerance (failure models, process resilience, reliable communication, 2PC/
  3PC, recovery — checkpointing); 9 security.
- **Lynch**: synchronous network algorithms (leader election in rings, BFS, MST, Byzantine
  agreement with n > 3f), asynchronous shared memory (mutual exclusion, consensus impossibility
  with one fault), asynchronous networks (logical time, snapshots, FLP), partially synchronous
  models. The proofs behind every "you can't" in the field.
- **Cachin, Guerraoui & Rodrigues** (2nd ed.): abstractions with modules and properties —
  links (fair-loss, stubborn, perfect), failure detectors (perfect, eventually perfect, leader
  election Ω), reliable/uniform/causal/total-order broadcast, shared memory registers (regular,
  atomic), consensus (flooding, hierarchical, Paxos-style leader-driven), Byzantine versions,
  group membership and view synchrony. Ideal for seeing how Raft's guarantees decompose.
- **Petrov, Database Internals** (2019): part I storage engines (B-tree variants, LSM,
  file formats, transaction processing and recovery); part II distributed systems (failure
  detection, leader election, replication and consistency, anti-entropy and dissemination —
  gossip, Merkle trees; distributed transactions — 2PC, Calvin, Percolator; consensus — Paxos,
  Raft, EPaxos).
- **6.824 paper list**: MapReduce, GFS, VM-FT, Raft, ZooKeeper, CRAQ, Aurora, Frangipani,
  Spanner, FaRM, Spark, Memcached at Facebook, COPS, Certificate Transparency, Bitcoin, Grove.

## Key ideas → pages
[[distributed-systems-basics]], [[time-clocks-and-ordering]], [[consistency-models]],
[[consensus-paxos-raft]], [[replication-and-partitioning]], [[byzantine-fault-tolerance-and-blockchains]].

## What they add
Van Steen for breadth, Cachin for the abstraction stack, Lynch for proofs, Petrov for the
engineer's view; DDIA ([[database-textbooks]]) is the popular synthesis.

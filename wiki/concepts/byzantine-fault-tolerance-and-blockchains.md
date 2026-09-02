---
title: Byzantine fault tolerance and blockchains — the Byzantine generals, PBFT, and Nakamoto consensus
type: concept
section: "4.6"
level: 500
tags: [byzantine-fault-tolerance, byzantine-generals, oral-messages, signed-messages, 3f-plus-1, pbft, castro-liskov, view-change, blockchain, bitcoin, nakamoto-consensus, proof-of-work, longest-chain, probabilistic-finality, sybil-resistance, proof-of-stake, permissioned, permissionless, smart-contracts, certificate-transparency, sundr, fork-consistency]
sources: [mit-6-824, distributed-systems-textbooks, distributed-systems-seminal-papers]
summary: When nodes may lie, not just crash, agreement needs n ≥ 3f+1 (Lamport, Shostak & Pease: with unsigned "oral" messages three generals cannot tolerate one traitor; signatures let any n > f+1 agree but cost more rounds), and PBFT (Castro & Liskov 1999) made it practical for permissioned systems — a primary orders requests, replicas run pre-prepare/prepare/commit with 2f+1 matching messages per phase, clients accept f+1 matching replies, view changes replace a faulty primary, and MACs replace signatures — while Bitcoin (Nakamoto 2008) solved the permissionless case where membership is unknown: proof-of-work makes proposing blocks expensive (Sybil resistance), the longest (heaviest) chain rule gives probabilistic finality that strengthens with confirmations, and the whole thing is a slow, energy-priced total-order broadcast; proof-of-stake and BFT-style chains (Tendermint, HotStuff) bring the two lineages back together, and fork-consistency (SUNDR) and certificate transparency show what an untrusted server can still be forced to reveal.
---
# Byzantine fault tolerance and blockchains

**In one sentence.** Crash tolerance needs a majority; lying tolerance needs two-thirds plus
one and either identities or a price for speaking.

## The Byzantine generals (Lamport, Shostak & Pease 1982)
Loyal generals must agree on attack/retreat despite traitors who send conflicting messages.
With **oral messages** (no authentication) agreement needs **n ≥ 3f+1** and f+1 rounds — the
three-generals-one-traitor case is impossible because a loyal lieutenant cannot tell whether
the commander or the other lieutenant lies. With **signed messages** any number of traitors can
be tolerated among n ≥ f+2. Interactive consistency, the connection to clock synchronization
and to hardware fault tolerance (SIFT). FLP still applies: asynchronous Byzantine consensus
needs randomization or partial synchrony.

## PBFT (Castro & Liskov 1999; 6.824 L21)
Permissioned: **3f+1 replicas** with known identities. Normal case: client → primary
(pre-prepare assigns sequence number) → replicas multicast **prepare**; with 2f+1 prepares a
replica is *prepared* (agreement on order within a view); multicast **commit**; with 2f+1
commits execute and reply; client waits for **f+1 matching replies**. Why 2f+1 quorums: any two
intersect in at least one honest replica. **View change** when the primary is suspected:
new primary collects 2f+1 view-change messages carrying prepared certificates so committed
requests survive. Checkpoints with 2f+1 signatures garbage-collect logs; MACs instead of
public-key signatures made it fast enough for an NFS service. Descendants: Zyzzyva, HotStuff
(linear message complexity, pipelined — used by Diem/Aptos), Tendermint; also used for
replicated firmware/aerospace.

## Nakamoto consensus (Bitcoin 2008; 6.824 L20)
Permissionless: anyone can join, so identities are free (**Sybil attack**) and quorums
meaningless. Bitcoin instead: transactions in blocks; each block references its predecessor's
hash (a hash chain — [[git-data-model]] is the same structure); a block is valid only with a
**proof-of-work** nonce making its hash fall below a target (difficulty retargeted to ~10
min/block); nodes extend the **longest/heaviest** valid chain; miners rewarded with coins. A
transaction is final only probabilistically — an attacker with < 50% hash power falls behind
exponentially with each confirmation (6 blocks ≈ an hour). Properties: total order of
transactions, double-spend prevention, ~7 tx/s, seconds-to-hours latency, energy cost is the
security budget; forks resolve by chain selection; 51% attacks; selfish mining. Peer-to-peer
gossip for blocks and transactions ([[networking-seminal-papers]] — DHT-like overlays);
Merkle trees for transaction commitments and SPV clients.

## Proof-of-stake and hybrids
Replace work with locked capital and slashing (Ethereum's Gasper: Casper FFG + LMD-GHOST);
BFT-style finality gadgets over a chain; committees sampled by verifiable random functions
(Algorand). Smart contracts (Ethereum's EVM — [[bytecode-vms-and-jit]]) make the ledger a
replicated state machine with gas-metered execution ([[consensus-paxos-raft]]). Trade-offs:
finality vs liveness under partitions, validator centralization, MEV.

## Weaker but useful: untrusted servers
**Fork consistency** (SUNDR, 6.824 L19): an untrusted file server cannot be prevented from
showing different clients different histories, but signed version vectors force any lie into a
permanent fork that clients can later detect. **Certificate Transparency**: CAs' certificates
in append-only Merkle logs with signed tree heads and consistency proofs — the same idea for
the web PKI ([[dns-http-and-the-web-stack]], [[cryptography-basics]]).

## Pitfalls
- Using crash-tolerant Raft where participants are mutually distrusting.
- Confusing "decentralized" with "Byzantine tolerant" or with "fast".
- Ignoring synchrony assumptions (PBFT liveness needs eventual delivery; Bitcoin security needs
  block propagation ≪ block interval).
- Treating probabilistic finality as absolute; reorganizations happen.

## Related
- [[consensus-paxos-raft]], [[distributed-systems-basics]], [[cryptography-basics]],
  [[hash-functions-cryptographic]], [[git-data-model]], [[security-principles]].

## Sources
Lamport, Shostak & Pease 1982; Castro & Liskov 1999; Nakamoto 2008; 6.824 L19–21; Lynch ch. 6; Cachin et al. ch. 5.

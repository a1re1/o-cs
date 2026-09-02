---
title: Blockchain and cryptocurrencies — the problem Bitcoin solves (double-spending without a trusted third party), Bitcoin mechanics (coins as chains of signatures, UTXOs, transactions, Merkle-tree blocks, the P2P network, wallets and keys), Nakamoto consensus (proof-of-work, the longest/heaviest chain, difficulty adjustment, mining incentives and halving, why the 51% and honest-majority assumptions matter and where they fail — selfish mining), proof-of-stake and finality (accountability, the availability-finality dilemma), Ethereum and smart contracts (the EVM, gas, Solidity, the world-computer model and its failure modes — reentrancy, The DAO), decentralized finance (stablecoins, AMMs and the constant-product formula, lending, MEV, flash-loan attacks), scaling (payment channels/Lightning, rollups), privacy (mixing, zk-SNARKs/Zcash), and an honest accounting of what blockchains are and aren't good for
type: concept
section: "8.4"
level: 400
tags: [blockchain, cryptocurrency, bitcoin, nakamoto, double-spending, trusted-third-party, utxo, transactions, digital-signatures, merkle-tree, block, proof-of-work, pow, mining, longest-chain, heaviest-chain, difficulty-adjustment, block-reward, halving, incentives, 51-percent-attack, honest-majority, sybil-resistance, selfish-mining, eyal-sirer, nakamoto-consensus, finality, probabilistic-finality, proof-of-stake, pos, staking, slashing, accountability, availability-finality-dilemma, ethereum, buterin, evm, gas, smart-contracts, solidity, world-computer, reentrancy, the-dao, defi, stablecoins, amm, automated-market-maker, constant-product, uniswap, lending, compound, mev, maximal-extractable-value, flash-loans, oracles, scaling, layer-2, payment-channels, lightning-network, rollups, optimistic-rollup, zk-rollup, privacy, mixing, coinjoin, zk-snark, zcash, zerocash, byzantine-fault-tolerance, trilemma]
sources: [privacy-and-blockchain-texts-courses-and-seminal-papers]
summary: Bitcoin (Nakamoto 2008) solves electronic cash without a bank: the double-spending problem — that a digital coin, being copyable, could be spent twice — was previously solved only by a trusted mint checking every transaction, and Nakamoto replaces that trust with a public append-only ledger secured by proof-of-work, where a coin is a chain of digital signatures (each owner signs over the hash of the previous transaction plus the next owner's key), transactions spend unspent outputs (UTXOs), and miners batch transactions into blocks linked by hash into a chain, each block containing a Merkle root of its transactions and a nonce whose hash must fall below a difficulty target (proof-of-work), so that rewriting history means redoing all the work; nodes accept the longest (most-work) chain, and the system is secure as long as honest nodes control a majority of hashing power — which also makes the security economic (attacking costs more than it yields) and probabilistic (a transaction is final only after enough confirmations), with difficulty auto-adjusting to keep ~10-minute blocks and a halving block subsidy giving a fixed supply; the honest-majority assumption is not the whole story — selfish mining (Eyal & Sirer) shows a miner with well under 51% can earn more than its fair share by withholding blocks, and a true 51% enables double-spends and censorship. Proof-of-stake replaces hashing with staked capital and slashing, enabling accountability and faster finality but facing the availability-finality dilemma; Ethereum generalizes the ledger into a world computer — the EVM runs smart contracts (Solidity) whose every operation costs gas paid in ether — which enabled DeFi (stablecoins, automated market makers pricing by the constant-product formula x·y=k, lending protocols, and the MEV and flash-loan attacks that composability makes possible) but also a decade of catastrophic bugs (reentrancy and The DAO, the fundamental hazard of immutable code holding money); the scalability trilemma pushes throughput to layer 2 (Lightning payment channels, optimistic and zk rollups), and privacy — public by default — is added with mixing/CoinJoin and zk-SNARKs (Zerocash/Zcash); the honest verdict is that blockchains buy censorship-resistance and trust-minimization at a large cost in performance, energy (PoW), and complexity, worth it only when removing the trusted third party is the actual requirement.
---
# Blockchain and cryptocurrencies

**In one sentence.** A blockchain is an append-only ledger that a set of mutually
distrusting parties agree on without a central authority, paying for that trust-
minimization with proof-of-work or staked capital, probabilistic finality, low
throughput, and (for Bitcoin) enormous energy — a trade worth making only when removing
the trusted third party is the point.

## The problem: double-spending without a trusted third party (Nakamoto 2008 — abstract, §1–2 read)
Digital money is just data, so a coin can be copied and spent twice; the classical fix is
a **trusted mint** that checks every transaction — but then "the fate of the entire money
system depends on the company running the mint." Nakamoto's goal: "an electronic payment
system based on cryptographic proof instead of trust, allowing any two willing parties to
transact directly with each other without the need for a trusted third party." The
insight is a **public timestamped ledger** everyone agrees on, so double-spends are
visible and the *first* transaction wins. The hard part is agreeing on order without a
coordinator — a **Byzantine agreement** problem ([[byzantine-fault-tolerance-and-blockchains]],
[[consensus-paxos-raft]]) — under **open membership** where identities are free, so
**sybil attacks** (spawn many fake nodes) must be resisted; Nakamoto's answer ties voting
power to a scarce resource (computation) rather than identity.

## Bitcoin mechanics (CS251 L1–3; Princeton book)
A **coin** is "a chain of digital signatures": each owner transfers it by signing a hash of
the previous transaction and the next owner's public key ([[public-key-cryptography]]).
**Transactions** consume **unspent transaction outputs (UTXOs)** and create new ones (inputs
reference prior outputs and carry signatures; outputs specify amounts and locking scripts
— Bitcoin Script, intentionally limited); no account balances, just a UTXO set.
**Blocks** batch transactions; each block header has the previous block's hash (forming
the **chain**), a **Merkle root** committing to all its transactions (so a light client can
verify inclusion with a log-sized proof — [[hash-functions-cryptographic]], SPV), a
timestamp, the difficulty target, and a **nonce**. The **P2P network** floods transactions
and blocks best-effort; **wallets** manage private keys (the real "coins" are the keys —
lose them, lose the money; hardware wallets, seed phrases, HD wallets, multisig). Full
nodes validate every rule; miners assemble blocks.

## Nakamoto consensus: proof-of-work (Nakamoto §3–6; Garay et al. 2015)
To append a block, a miner must find a nonce so that `H(block header) < target` —
**proof-of-work**, a brute-force search over a cryptographic hash (SHA-256 double) with no
shortcut, so producing a block costs real energy; verifying it is one hash. Nodes accept
the **longest (most-work) chain** as truth; to rewrite block k an attacker must redo the
PoW of block k and every block after it *while outpacing* the honest network — infeasible
once enough blocks are stacked on top, which is why a transaction gains **probabilistic
finality** with each **confirmation** (~6 for large Bitcoin payments). **Difficulty adjusts**
every 2016 blocks to hold the average block time near **10 minutes** regardless of total
hashpower. **Incentives**: the miner of a block collects the **block subsidy** (new coins —
**halving** every 210 000 blocks, capping supply at 21 M) plus **transaction fees**; this
both distributes coins and pays for security, aligning miners with honest behavior
because attacking the chain destroys the value of the coins they earn. **Security
assumption**: honest nodes control a **majority of hashpower** ("**51%**"). Where it frays:
a real 51% attacker can **double-spend** (mine a private fork that reverses a confirmed
payment) and **censor**, though not steal others' coins or forge signatures; **selfish
mining** (Eyal & Sirer 2014) shows a miner with well *under* 50% can gain more than its
fair share by strategically **withholding** found blocks and releasing them to orphan
honest work — so "honest majority" is necessary but not sufficient; **mining
centralization** (pools, ASICs, cheap-energy regions) concentrates the very hashpower the
security assumes is diffuse; **eclipse** and network-partition attacks; the energy cost
is the security budget (Bitcoin ≈ a mid-size country's electricity — the central critique
of PoW).

## Proof-of-stake and finality (CS251 L4–6)
**Proof-of-stake** replaces hashpower with **staked capital**: validators lock coins and are
chosen (weighted by stake) to propose/attest blocks; misbehavior is punished by
**slashing** the stake — which gives **accountability** (you can prove who violated the rules
and burn their money, unlike PoW where a failed attack is nearly free) and removes the
energy cost (Ethereum's 2022 "Merge" cut its energy ~99.95 %). Trade-offs: the
**nothing-at-stake** and **long-range** problems (addressed by slashing and weak
subjectivity/checkpoints), stake **centralization** (liquid-staking derivatives), and the
**availability-finality dilemma** — a protocol can guarantee **finality** (never revert)
under partition *or* **availability** (keep producing) but not both (CAP for consensus —
[[distributed-systems-basics]]); Ethereum's Gasper combines a live chain (LMD-GHOST) with
a finality gadget (Casper FFG) that finalizes checkpoints. Classical **BFT** consensus
(PBFT, Tendermint — [[byzantine-fault-tolerance-and-blockchains]]) gives instant finality
with known validators (tolerating < 1/3 Byzantine) and is used by many PoS chains, trading
open membership for speed.

## Ethereum and smart contracts (CS251 L7–8; Buterin 2013; Wood 2014)
Ethereum generalizes the ledger from money to a **world computer**: an account-based state
(balances + contract storage) updated by transactions, where a transaction can deploy or
call a **smart contract** — code that runs on the **EVM** (a stack machine) on *every* node,
deterministically. Because running someone's code on the whole network is a DoS risk,
each operation costs **gas** paid in ether (with a gas limit and a fee market —
EIP-1559's base-fee burn), halting runaway or infinite programs
([[computability-and-halting-problem]] — you pay to postpone the halting problem).
**Solidity** compiles to EVM bytecode; contracts are **immutable once deployed** and **hold
money**, which is the fundamental hazard: a bug is a permanent, exploitable vault.
**Reentrancy** — a contract calls out to an untrusted contract before updating its own
state, which calls back in and drains funds — caused **The DAO** hack (2016, ~$60 M,
leading to the contentious hard fork that split Ethereum/Ethereum Classic); other
classics: integer overflow (pre-0.8), access-control mistakes, oracle manipulation,
delegatecall/proxy bugs (Parity multisig freeze), front-running. Defenses: checks-
effects-interactions, reentrancy guards, audits and formal verification
([[program-verification]]), fuzzing ([[fuzzing]]), bug bounties, upgradeable proxies (which
reintroduce trust). Smart contracts are [[design-by-contract]]'s name colliding with a
different thing — here "contract" means autonomous code, and the assurance bar is far
higher because exploits are irreversible and instantly monetizable.

## DeFi, MEV, scaling, privacy (CS251 L9–17)
**Decentralized finance** composes contracts into financial primitives: **stablecoins**
(fiat-backed like USDC; crypto-collateralized like DAI; algorithmic — Terra/UST's 2022
collapse a case study in reflexive design), **automated market makers** (Uniswap: a pool
holds two assets and prices trades by the **constant-product formula** x·y=k, so price
moves along a curve and liquidity providers earn fees but bear **impermanent loss**),
**lending** (Compound/Aave: over-collateralized loans, algorithmic interest, liquidations).
**MEV** (maximal extractable value): because block proposers order transactions, they (or
searchers bidding for ordering) can extract value by front-running, back-running, and
sandwiching users — a tax on DeFi and a centralizing force (proposer-builder separation
mitigates). **Flash loans**: borrow and repay within one transaction (atomic, so
uncollateralized) — a legitimate tool and a powerful attack primitive (borrow millions,
manipulate a thin oracle/AMM, profit, repay, all atomically). **Oracles** (Chainlink)
bridge off-chain data and are a prime attack surface. **Scaling** (the **trilemma**:
decentralization, security, scalability — pick the trade): base layers do ~10–100 tx/s,
so throughput moves to **layer 2** — **payment/state channels** (Lightning: lock funds in a
channel, transact off-chain instantly, settle on-chain — [[byzantine-fault-tolerance-and-blockchains]]),
and **rollups** (execute transactions off-chain, post compressed data + a proof to L1):
**optimistic rollups** (assume valid, allow fraud proofs during a challenge window) and
**zk-rollups** (post a **validity proof** — a zk-SNARK that the batch was executed correctly —
[[cryptographic-protocols-and-zero-knowledge]]). **Privacy**: chains are pseudonymous but
**public**, so analysis de-anonymizes ([[privacy-enhancing-technologies]]); **mixing/CoinJoin**
break linkage, and **zk-SNARKs** enable shielded transactions (**Zerocash → Zcash**) that
prove a transfer is valid without revealing sender, receiver, or amount.

## What blockchains are and aren't good for
Genuine strengths: **censorship-resistance** and **trust-minimization** — no single party
can freeze funds, rewrite history, or exclude a user; a global, permissionless,
auditable ledger; programmable money and credibly-neutral settlement; self-custody.
Genuine costs: throughput and latency far below centralized systems, energy (PoW) or
capital lockup (PoS), irreversibility (fraud and mistakes are final — the flip side of
no chargebacks), smart-contract risk, key-management burden, MEV, and regulatory/legal
uncertainty ([[technology-law-privacy-and-intellectual-property]] — the Howey test,
securities law). The honest engineering question is whether removing the trusted third
party is a real requirement: for most applications a database with an accountable
operator is faster, cheaper, and reversible; blockchains earn their cost when the
adversary *includes* the operator, or when credible neutrality across mutually
distrusting parties is the product. The underlying ideas — Merkle trees, BFT consensus,
zero-knowledge proofs, incentive design — are valuable well beyond cryptocurrency.

## Pitfalls
- Assuming "honest majority" is the whole security story (selfish mining, pools, MEV).
- Treating confirmations as instant finality; ignoring reorg risk.
- Deploying immutable money-holding code without audits/formal methods (reentrancy).
- "Algorithmic" stablecoins and thin-oracle designs (flash-loan manipulation).
- Reaching for a blockchain when an accountable database would do; conflating
  pseudonymity with privacy.

## Related
- [[byzantine-fault-tolerance-and-blockchains]], [[consensus-paxos-raft]],
  [[distributed-systems-basics]], [[public-key-cryptography]],
  [[hash-functions-cryptographic]], [[cryptographic-protocols-and-zero-knowledge]],
  [[privacy-enhancing-technologies]], [[program-verification]], [[fuzzing]],
  [[design-by-contract]], [[computability-and-halting-problem]],
  [[technology-law-privacy-and-intellectual-property]],
  [[computing-ethics-and-professional-responsibility]].

## Sources
Nakamoto 2008 (read: abstract, §1–2; §3–6, 11 from memory); Buterin 2013 (Ethereum whitepaper); Wood 2014 (Yellow Paper); Eyal & Sirer 2014 (selfish mining); Garay, Kiayias & Leonardos 2015 (Bitcoin backbone); Poon & Dryja 2016 (Lightning); Ben-Sasson et al. 2014 (Zerocash); Buterin & Griffith 2017 (Casper FFG); Daian et al. 2019 (Flash Boys 2.0, MEV); Adams et al. 2020 (Uniswap v2); CS251 syllabus (read); Narayanan et al., *Bitcoin and Cryptocurrency Technologies* (Princeton).

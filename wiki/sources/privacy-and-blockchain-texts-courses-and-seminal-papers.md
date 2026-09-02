---
title: Privacy technologies & blockchains — Dwork & Roth's The Algorithmic Foundations of Differential Privacy (2014, free; ToC read), Near & Abuah's Programming Differential Privacy (free), Stanford CS251 Blockchain Technologies (Boneh; 2025 syllabus read), Princeton's Bitcoin and Cryptocurrency Technologies (free); Dwork et al. differential privacy (2006), Sweeney k-anonymity (2002), Narayanan & Shmatikov Netflix de-anonymization (2008), Chaum mix networks (1981), Dingledine, Mathewson & Syverson's Tor (2004; abstract read), Abadi et al. deep learning with DP (2016), McMahan et al. federated learning (2017); Nakamoto's Bitcoin (2008; abstract and §1–2 read), Buterin's Ethereum whitepaper, Wood's Yellow Paper, Eyal & Sirer selfish mining (2014), the Lightning Network, Ben-Sasson et al. Zerocash (2014)
type: source
section: "8.3"
level: 400
tags: [dwork-roth, algorithmic-foundations-differential-privacy, near-abuah, programming-differential-privacy, cs251, boneh, stanford, princeton-bitcoin, differential-privacy, dwork, sweeney, k-anonymity, narayanan-shmatikov, netflix-deanonymization, chaum, mix-networks, tor, dingledine, onion-routing, abadi, dp-sgd, federated-learning, mcmahan, secure-multiparty-computation, homomorphic-encryption, nakamoto, bitcoin, buterin, ethereum, wood, yellow-paper, eyal-sirer, selfish-mining, lightning-network, zerocash, zcash, zk-snark, proof-of-work, proof-of-stake]
sources: []
authors: [Cynthia Dwork, Aaron Roth, Joseph Near, Chiké Abuah, Dan Boneh, Latanya Sweeney, Arvind Narayanan, Vitaly Shmatikov, David Chaum, Roger Dingledine, Nick Mathewson, Paul Syverson, Brendan McMahan, Satoshi Nakamoto, Vitalik Buterin, Gavin Wood, Ittay Eyal, Emin Gün Sirer]
year: 2014
institution: Microsoft Research / Penn / Stanford / Princeton
url: https://www.cis.upenn.edu/~aaroth/privacybook.html
license: free (Dwork-Roth, Near-Abuah, Princeton book); papers open
format: pdf
summary: The Algorithmic Foundations of Differential Privacy (Dwork & Roth 2014; ToC read) is the definitive monograph — the promise of DP, basic terms and the formal (ε, δ) definition, basic mechanisms and composition (randomized response, the Laplace and exponential mechanisms, composition theorems, the sparse vector technique), releasing linear queries with correlated error (SmallDB, private multiplicative weights), generalizations, boosting, atypical sensitivity (subsample-and-aggregate, propose-test-release, stability), lower bounds and reconstruction attacks, DP and computational complexity, DP and mechanism design, DP and machine learning (private ERM and online learning), and additional models (the local model, pan-privacy, continual observation) — while Near & Abuah's Programming Differential Privacy teaches the same ideas executably in Python; CS251 (Boneh; 2025 syllabus read) covers Bitcoin mechanics (Merkle trees, transactions, UTXO, P2P, wallets), classical consensus and secure state-machine replication (Dolev-Strong, synchrony/asynchrony/partial synchrony, the threshold adversary), Nakamoto consensus and sybil resistance, proof-of-stake with accountability and the availability-finality dilemma, Ethereum/EVM/gas and Solidity, DeFi (stablecoins, lending, AMMs and the constant-product formula, MEV, flash-loan attacks), other L1s, blockchain privacy (mixing, de-anonymization, zk-SNARKs, Zcash, PLONK, polynomial commitments), and scaling (payment/state channels, Lightning, rollups); the privacy seminal papers are Sweeney's k-anonymity and its failure, Narayanan & Shmatikov's linkage de-anonymization of the Netflix Prize data, Dwork et al.'s 2006 definition, Chaum's 1981 mix networks and Tor's onion routing (abstract read: telescoping circuits with perfect forward secrecy, fixed-size cells, SOCKS, hidden services via rendezvous points), Abadi et al.'s DP-SGD, and McMahan et al.'s federated learning; and the blockchain seminal papers are Nakamoto's Bitcoin (abstract and §1–2 read: a coin as a chain of signatures, the double-spending problem solved by a proof-of-work timestamp chain where the longest chain is the honest majority's, "cryptographic proof instead of trust"), Buterin's Ethereum (a Turing-complete world computer), Wood's Yellow Paper, Eyal & Sirer's selfish mining (honest majority is not enough), the Lightning Network, and Zerocash.
---
# Privacy technologies & blockchains: sources

## What they are
- **Dwork & Roth 2014** (read: ToC): 13 chapters — promise; basic terms and (ε, δ)-DP;
  basic techniques and composition (randomized response, Laplace, exponential, composition,
  sparse vector); linear queries (SmallDB, private MW); generalizations; boosting;
  atypical sensitivity (subsample-and-aggregate, propose-test-release, smooth
  sensitivity); lower bounds and reconstruction; DP and complexity; DP and mechanism
  design; DP and ML (private ERM, online); additional models (local, pan-private,
  continual observation); reflections. **Near & Abuah, Programming DP** (free, executable
  Python; UVM CS211) is the practitioner's on-ramp.
- **CS251** (Boneh; read: 2025 syllabus): crypto and cryptocurrencies; Bitcoin mechanics
  and wallets; classical consensus / SMR (Dolev-Strong, network models); Nakamoto
  consensus and sybil resistance; PoS, accountability, availability-finality; Ethereum,
  EVM, gas, Solidity; DeFi (stablecoins, lending — Compound, AMMs — Uniswap constant
  product, MEV, flash loans); other L1s (Solana, Sui, Aptos); privacy (mixing,
  de-anonymization, zk-SNARKs, Zcash, PLONK, polynomial commitments); scaling (Lightning,
  rollups); legal/regulation (Howey test). **Princeton "Bitcoin and Cryptocurrency
  Technologies"** (Narayanan et al.; free textbook + Coursera): intro crypto,
  decentralization, mechanics, mining, anonymity, altcoins, politics.
- **Privacy seminal**: Sweeney 2002 (k-anonymity; and 2000's 87% re-identification);
  Narayanan & Shmatikov 2008 (Netflix Prize de-anonymization by IMDb linkage); Dwork,
  McSherry, Nissim & Smith 2006 (DP definition and Laplace mechanism); Dwork 2006
  (differential privacy, ICALP); Chaum 1981 (mix networks) and 1985 (untraceable
  payments); **Tor** (Dingledine, Mathewson & Syverson 2004; read: abstract) — telescoping
  circuits, PFS, fixed-size cells, directory servers, exit policies, hidden services;
  Abadi et al. 2016 (DP-SGD, the moments accountant); McMahan et al. 2017 (federated
  learning + FedAvg); Yao 1982 (garbled circuits / MPC), Gentry 2009 (FHE).
- **Blockchain seminal**: Nakamoto 2008 (read: abstract, §1–2); Buterin 2013 (Ethereum);
  Wood 2014 (Yellow Paper, EVM); Eyal & Sirer 2014 (selfish mining); Garay, Kiayias &
  Leonardos 2015 (the Bitcoin backbone protocol); Poon & Dryja 2016 (Lightning);
  Ben-Sasson et al. 2014 (Zerocash → Zcash); Lamport et al. 1982 (Byzantine generals —
  [[byzantine-fault-tolerance-and-blockchains]]).

## Key ideas → pages
[[privacy-enhancing-technologies]], [[blockchain-and-cryptocurrencies]]; existing:
[[differential-privacy]], [[byzantine-fault-tolerance-and-blockchains]],
[[public-key-cryptography]], [[cryptographic-protocols-and-zero-knowledge]],
[[hash-functions-cryptographic]], [[technology-law-privacy-and-intellectual-property]].

## What they add
Dwork & Roth is the rigorous foundation (the theorems behind [[differential-privacy]]);
Tor and the mix-network line give anonymity as a distinct goal from confidentiality;
Nakamoto is the four-page paper that started an industry and is best read next to the
consensus theory ([[byzantine-fault-tolerance-and-blockchains]]) that explains what it
did and didn't solve.

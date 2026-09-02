---
title: Privacy-enhancing technologies — the goals beyond confidentiality (data privacy vs communication anonymity vs computing on private data), why de-identification fails (Sweeney's linkage, the Netflix and AOL de-anonymizations, reconstruction and membership-inference attacks), differential privacy as the rigorous answer (pointer to the mechanism), anonymous communication (Chaum mix networks and mixnets, Tor onion routing with telescoping circuits and hidden services, and the limits — traffic analysis, exit nodes, global adversaries), private computation (secure multi-party computation and garbled circuits, homomorphic encryption, private set intersection, private information retrieval, trusted execution), federated learning and its leakage, and how to choose a PET for a threat model
type: concept
section: "8.3"
level: 400
tags: [privacy-enhancing-technologies, pets, privacy, anonymity, confidentiality, de-identification, anonymization, k-anonymity, sweeney, l-diversity, t-closeness, linkage-attack, netflix-prize, aol-search-logs, narayanan-shmatikov, reconstruction-attack, membership-inference, differential-privacy, epsilon, laplace-mechanism, local-dp, randomized-response, anonymous-communication, mix-networks, chaum, mixnet, tor, onion-routing, telescoping-circuit, perfect-forward-secrecy, hidden-services, rendezvous, traffic-analysis, exit-node, global-passive-adversary, dining-cryptographers, secure-multiparty-computation, mpc, garbled-circuits, yao, secret-sharing, homomorphic-encryption, fhe, gentry, private-set-intersection, psi, private-information-retrieval, pir, oblivious-ram, trusted-execution, sgx, federated-learning, mcmahan, fedavg, gradient-leakage, secure-aggregation, dp-sgd, threat-model, metadata]
sources: [privacy-and-blockchain-texts-courses-and-seminal-papers]
summary: Privacy-enhancing technologies pursue three distinct goals that need different tools: keeping individuals' records private while still analyzing data, hiding who is talking to whom (anonymity, a metadata problem confidentiality doesn't touch), and computing on data no party is willing to reveal. The first goal starts by discarding the myth of anonymization — Sweeney showed 87% of Americans are uniquely identified by ZIP + birth date + sex and re-identified the Massachusetts governor's medical record by linking to voter rolls, Narayanan & Shmatikov de-anonymized the Netflix Prize dataset via IMDb, the AOL search-log release outed users, and reconstruction and membership-inference attacks show that even aggregate statistics and trained models leak — so k-anonymity/l-diversity/t-closeness are fragile and the rigorous answer is differential privacy, which bounds how much any one record can change the output (ε) and composes cleanly (the mechanism and its guarantees are in the differential-privacy page). The second goal, anonymity, is served by mix networks (Chaum: batch and re-encrypt messages through mixes so inputs can't be linked to outputs) and by Tor, which builds a telescoping onion circuit through three volunteer relays — each knowing only its neighbors — with perfect forward secrecy and fixed-size cells, and reaches hidden services via rendezvous points, giving low-latency anonymity that is nonetheless defeated by a global passive adversary correlating traffic timing, by malicious exit nodes seeing plaintext, and by application-level leaks. The third goal, private computation, is met by secure multi-party computation (Yao's garbled circuits and secret-sharing let parties jointly compute a function revealing only its output — used for private-set-intersection contact discovery and joint analytics), homomorphic encryption (compute on ciphertext; FHE since Gentry 2009, still costly), private information retrieval and oblivious RAM (query without revealing what you fetched), and trusted execution enclaves (fast but side-channel-leaky); and federated learning keeps raw data on devices and shares only model updates — which still leak (gradient-inversion reconstructs inputs), so it is combined with secure aggregation and DP-SGD. Choosing a PET means naming the adversary and the goal: DP for statistical release, Tor/mixnets for metadata, MPC/HE for joint computation — each with a real cost in utility, latency, or compute.
---
# Privacy-enhancing technologies

**In one sentence.** Privacy is three problems — releasing data about people without
exposing any one of them, hiding who communicates with whom, and computing on inputs no
one will reveal — and each has its own tool (differential privacy, onion routing/mixnets,
secure computation), because confidentiality alone (encrypting content) solves none of
them.

## Three goals, and why anonymization is not one of the tools (Sweeney; Narayanan & Shmatikov 2008)
Confidentiality (encryption — [[cryptography-basics]]) hides *content* from outsiders; PETs
add: **data privacy** (analyze a dataset without exposing individuals), **anonymity**
(hide the *metadata* — who, when, to whom — which encryption leaves in the clear), and
**private computation** (compute a joint result without any party revealing its input).
The foundational lesson is that **de-identification fails**: Sweeney (2000) showed **87 %**
of the US population is uniquely identified by (ZIP, birth date, sex) and re-identified
Governor Weld's "anonymized" hospital record by linking it to public voter rolls (a
**linkage attack**); the **AOL** search-log release (2006) and the **Netflix Prize** dataset
(Narayanan & Shmatikov 2008 — de-anonymized by linking sparse rating vectors to public
IMDb reviews) confirmed it on real releases; **reconstruction attacks** (Dinur–Nissim;
the US Census's motivation for adopting DP) show that answering enough accurate queries
reconstructs the raw data, and **membership-inference** shows a trained model reveals
whether a record was in its training set. So **k-anonymity** (each record
indistinguishable among k on quasi-identifiers), **l-diversity** and **t-closeness** are
brittle patches, not guarantees. The rigorous answer is **differential privacy** — a
formal bound (ε) on how much any single record can change any output, robust to
side information and composing predictably — whose mechanisms (randomized response,
Laplace/Gaussian noise scaled to sensitivity, the exponential mechanism, DP-SGD, the
local vs central models) and guarantees are covered in [[differential-privacy]]. DP is
deployed by the US Census, Apple, Google (RAPPOR), and in ML training.

## Anonymous communication (Chaum 1981; Tor — abstract read)
Even over TLS, an observer sees source and destination IPs, timing, and volume —
**traffic analysis**. **Mix networks** (Chaum 1981): route messages through a sequence of
**mixes**, each of which decrypts one layer, **batches** and **reorders** messages, and
forwards, so an observer can't link a mix's inputs to its outputs; high-latency mixnets
(remailers, and modern designs like Loopix) resist even global adversaries by adding
delay and cover traffic — good for email, bad for browsing. **Tor** (Dingledine,
Mathewson & Syverson 2004): a low-latency **onion-routing** overlay for TCP. A client
builds a **circuit** of (usually three) relays — guard, middle, exit — using a
**telescoping** handshake that negotiates a session key with each hop in turn, giving
**perfect forward secrecy** (a later relay compromise can't decrypt recorded past traffic)
and meaning each relay knows only its **predecessor and successor**, never both ends; data
travels in **fixed-size cells**, each relay peeling one encryption layer (the onion);
**directory servers** publish the relay list; **exit policies** let relays limit what they
forward; **hidden/onion services** let a server be reached without revealing its IP via
**rendezvous points** and introduction points. Limits: a **global passive adversary** who
sees both ends can **correlate** packet timing/volume to link them (Tor explicitly does
not defend against this, trading full anonymity for usability — no mixing/padding);
**malicious exit nodes** see the plaintext to the destination (use HTTPS end-to-end);
**application leaks** (browser fingerprinting, plugins, logins) de-anonymize — hence the
hardened Tor Browser; **de-anonymization** via correlation, congestion attacks, or
compromised guards; **VPNs** are not anonymity (single trusted party). Related: the
**dining cryptographers** protocol (DC-nets, unconditional sender anonymity, poor
scaling), Signal's sealed sender and private contact discovery, mixnets for
cryptocurrency ([[blockchain-and-cryptocurrencies]] privacy).

## Computing on private data (Yao 1982; Gentry 2009; McMahan 2017)
- **Secure multi-party computation (MPC)**: parties jointly compute f(x₁,…,xₙ) learning
  only the output, not each other's inputs. **Yao's garbled circuits** (two-party): one
  party garbles a boolean circuit, the other evaluates it obliviously via oblivious
  transfer; **secret-sharing** MPC (GMW, BGW, SPDZ): split each input into shares,
  compute on shares, reconstruct only the result — secure against honest/dishonest
  majorities with different protocols. Uses: **private set intersection** (find common
  contacts/compromised passwords without revealing the sets — password breach checks,
  contact discovery, ad conversion measurement), joint analytics across institutions
  (hospitals, banks — Boston wage-gap study), threshold signatures/wallets, private
  auctions. Cost: rounds and bandwidth; practical for specific functions, not general
  computation at scale.
- **Homomorphic encryption**: compute directly on ciphertext. Partially HE (RSA/
  ElGamal multiplicative, Paillier additive) enables private aggregation;
  **Fully homomorphic encryption** (Gentry 2009 — bootstrapping) supports arbitrary
  computation on encrypted data (a client encrypts, the server computes blindly,
  the client decrypts) — the "holy grail," now practical for restricted workloads
  (BFV/BGV/CKKS for approximate arithmetic, TFHE for boolean) but orders of magnitude
  slower than plaintext; used for private inference and encrypted database queries.
- **Private information retrieval (PIR)** and **oblivious RAM (ORAM)**: fetch item i from a
  server without revealing i (PIR) or hide the *access pattern* of a program from the
  storage it uses (ORAM — Path ORAM) — important because access patterns leak even under
  encryption ([[access-control-and-isolation]] covert/side channels; enclave
  controlled-channel attacks).
- **Trusted execution environments** (SGX, TrustZone, SEV): compute on data inside a
  hardware-protected enclave the OS can't read, with remote attestation — fast, but the
  trust model includes the CPU vendor and the attacks are side channels
  ([[software-exploitation-and-mitigations]]); often combined with the above.

## Federated learning and PET composition (McMahan et al. 2017)
**Federated learning**: train a shared model without centralizing data — each device
computes an update on its local data and sends only the **update**; the server averages
(**FedAvg**). It reduces raw-data exposure and suits phones/hospitals, but the updates
**leak**: **gradient-inversion** attacks reconstruct training examples from gradients, and
membership inference applies. So FL is layered with **secure aggregation** (MPC so the
server sees only the sum of updates, not any one) and **DP-SGD** (clip and noise updates
for a differential-privacy guarantee — [[differential-privacy]], [[mlops-and-ml-systems]]);
even then, communication cost, non-IID data, and stragglers are open problems
([[distributed-training-and-ml-systems]]). This composition is typical: real deployments
stack PETs (encryption in transit + DP on the release + secure aggregation + enclaves)
because each addresses a different part of the threat model.

## Choosing a PET (start from the adversary)
Name the goal and the adversary, then pick: releasing statistics/training data to
possibly-adversarial recipients → **differential privacy** (accept the utility cost);
hiding communication metadata from network observers → **Tor** (low-latency, not vs global
adversary) or **mixnets** (high-latency, stronger); several parties computing on inputs
they won't share → **MPC** (specific functions) or **FHE** (general, slow); querying without
revealing the query → **PIR/ORAM**; keeping data on user devices → **federated learning +
secure aggregation + DP**. Every PET trades something — accuracy, latency, compute,
or completeness of the guarantee — and "encrypted" is never the same as "private"
([[technology-law-privacy-and-intellectual-property]] GDPR's pseudonymization vs
anonymization; contextual integrity as the norm PETs enforce).

## Pitfalls
- Believing anonymized/aggregated data is safe (linkage, reconstruction, membership
  inference); k-anonymity as a guarantee.
- Treating a VPN as anonymity; using Tor over HTTP (exit node reads plaintext) or while
  logged in.
- Federated learning as private by itself (gradients leak — add secure aggregation + DP).
- FHE/MPC where the cost is unjustified, or enclaves without accounting for side channels.
- Choosing a PET without a stated adversary and goal.

## Related
- [[differential-privacy]], [[cryptography-basics]], [[public-key-cryptography]],
  [[cryptographic-protocols-and-zero-knowledge]], [[hash-functions-cryptographic]],
  [[access-control-and-isolation]], [[software-exploitation-and-mitigations]],
  [[blockchain-and-cryptocurrencies]], [[mlops-and-ml-systems]],
  [[distributed-training-and-ml-systems]], [[technology-law-privacy-and-intellectual-property]],
  [[computing-ethics-and-professional-responsibility]], [[network-security-attacks-and-defenses]].

## Sources
Dwork & Roth 2014 (read: ToC); Near & Abuah 2021; Sweeney 2000/2002 (k-anonymity); Narayanan & Shmatikov 2008 (Netflix); Dinur & Nissim 2003 (reconstruction); Shokri et al. 2017 (membership inference); Chaum 1981 (mixnets), 1988 (dining cryptographers); Dingledine, Mathewson & Syverson 2004 (Tor; read: abstract); Yao 1982/1986; Goldreich, Micali & Wigderson 1987 (GMW); Gentry 2009 (FHE); Stefanov et al. 2013 (Path ORAM); McMahan et al. 2017 (FedAvg); Bonawitz et al. 2017 (secure aggregation); Abadi et al. 2016 (DP-SGD); Zhu et al. 2019 (deep leakage from gradients).

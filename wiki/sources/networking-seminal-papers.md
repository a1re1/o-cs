---
title: Networking seminal papers — Cerf & Kahn (1974), Saltzer/Reed/Clark end-to-end (1984), Clark's design philosophy (1988), Jacobson congestion control (1988), Floyd & Jacobson RED (1993), Chord and Kademlia (2001/02), OpenFlow (2008), DCTCP (2010), BBR (2016), QUIC (2017)
type: source
section: "4.4"
level: 500
tags: [cerf-kahn, tcp-ip-origins, end-to-end-argument, clark-design-philosophy, jacobson, slow-start, congestion-collapse, red, active-queue-management, chord, kademlia, dht, openflow, sdn, dctcp, bbr, quic, history]
sources: []
authors: [Vinton Cerf, Robert Kahn, Jerome Saltzer, David Reed, David Clark, Van Jacobson, Sally Floyd, Ion Stoica, Petar Maymounkov, Nick McKeown, Mohammad Alizadeh, Neal Cardwell, Adam Langley]
year: 1974
institution: various
url: https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf
license: various
format: pdf
summary: Cerf & Kahn proposed gateways and a common internetwork datagram with end-host reliability — the TCP/IP split; Saltzer, Reed & Clark's end-to-end argument says functions that need the application's knowledge (reliability, security, dedup) belong at the endpoints, with lower-level versions justified only as performance enhancements; Clark's design philosophy lists the Internet's goals in priority order (survivability first, accountability last) and explains why datagrams and "fate-sharing" state at hosts followed; Jacobson diagnosed the 1986 congestion collapse and added slow start, RTT variance estimation, and AIMD to BSD TCP under a packet-conservation principle; RED drops packets early and randomly to signal congestion before queues fill; Chord and Kademlia gave O(log n) lookup in peer-to-peer overlays; OpenFlow separated the control plane into software (SDN); DCTCP used ECN marks for datacenter latency; BBR models bottleneck bandwidth and RTT instead of loss; QUIC moved transport into user space over UDP with TLS built in and no head-of-line blocking.
---
# Networking seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Cerf & Kahn, "A Protocol for Packet Network Intercommunication" (1974) | Internetworking via gateways; a common datagram format; hosts responsible for reliability (later split into TCP over IP) | [[internet-architecture-and-layering]] |
| Saltzer, Reed & Clark, "End-to-End Arguments in System Design" (1984) | "The function can completely and correctly be implemented only with the knowledge and help of the application at the endpoints"; low-level reliability, encryption, dedup are at best performance enhancements — the file-transfer example with corrupt copies at each hop | [[internet-architecture-and-layering]], [[file-systems]] (end-to-end checksums) |
| Clark, "The Design Philosophy of the DARPA Internet Protocols" (1988) | Fundamental goal: multiplexed use of existing interconnected networks via packet switching and gateways; second-level goals *in order*: survivability despite loss of networks, multiple types of service, variety of networks, distributed management, cost effectiveness, easy host attachment, accountability — the ordering explains datagrams, fate-sharing state in hosts, and the weaknesses (accounting, QoS) | [[internet-architecture-and-layering]] |
| Jacobson (& Karels), "Congestion Avoidance and Control" (SIGCOMM 1988) | After the Oct 1986 collapse (32 Kbps → 40 bps LBL–Berkeley): packet conservation; **slow start** to reach equilibrium; RTT mean+variance for the retransmit timer (Karn's algorithm); **additive increase / multiplicative decrease** on loss; fast retransmit — the basis of every TCP since | [[tcp-reliability-and-congestion-control]] |
| Floyd & Jacobson, "Random Early Detection Gateways" (1993) | Routers drop/mark probabilistically as average queue length grows, desynchronizing flows and keeping queues short; ancestor of CoDel, PIE, ECN-based AQM | [[tcp-reliability-and-congestion-control]], [[queueing-theory]] |
| Stoica et al., "Chord" (2001); Maymounkov & Mazières, "Kademlia" (2002) | Consistent-hashing rings with finger tables / XOR-metric routing for O(log n) key lookup among churning peers; BitTorrent's DHT, IPFS | [[consistent-hashing]], [[distributed-systems-basics]] |
| McKeown et al., "OpenFlow: Enabling Innovation in Campus Networks" (2008) | Separate the control plane (a controller programs match-action flow tables) from the data plane (switches) — software-defined networking; Google B4, P4 | [[ip-routing-and-forwarding]] |
| Alizadeh et al., "DCTCP" (2010) | Use the fraction of ECN-marked packets to scale the window smoothly; low latency and high throughput in datacenters with shallow buffers | [[tcp-reliability-and-congestion-control]] |
| Cardwell et al., "BBR: Congestion-Based Congestion Control" (2016) | Estimate bottleneck bandwidth and min RTT and pace at their product instead of reacting to loss; avoids bufferbloat; deployed at Google/YouTube | [[tcp-reliability-and-congestion-control]] |
| Langley et al., "The QUIC Transport Protocol" (SIGCOMM 2017); RFC 9000 | Transport over UDP in user space: 0/1-RTT handshakes with TLS 1.3 integrated, independent streams (no head-of-line blocking), connection migration, rapid deployability; HTTP/3 | [[dns-http-and-the-web-stack]] |

## Why read them
Clark and Saltzer et al. give the *why* of the architecture; Jacobson is a masterclass in
diagnosing a live system; BBR and QUIC show the architecture still evolving at the edges the
end-to-end argument predicted.

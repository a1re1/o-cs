---
title: Computer Networking: A Top-Down Approach (Kurose & Ross), Computer Networks: A Systems Approach (Peterson & Davie), TCP/IP Illustrated (Stevens), High Performance Browser Networking (Grigorik), Beej's Guide, and the key RFCs
type: source
section: "4.4"
level: 300
tags: [networking, kurose-ross, peterson-davie, systems-approach, tcp-ip-illustrated, stevens, hpbn, beej, sockets, rfc-791, rfc-793, rfc-9110, rfc-1034, rfc-8446, rfc-7540, rfc-9000, layers, application-layer, transport, network-layer, link-layer]
sources: []
authors: [James Kurose, Keith Ross, Larry Peterson, Bruce Davie, W. Richard Stevens, Ilya Grigorik, Brian Hall]
year: 2021
institution: various
url: https://book.systemsapproach.org/
license: mixed (Systems Approach, HPBN, Beej free)
format: html
summary: Kurose & Ross teach top-down (application protocols HTTP/SMTP/DNS/P2P/video, transport UDP/TCP with reliability and congestion control, network layer data plane — IP, forwarding, routers — and control plane — OSPF, BGP, SDN, link layer and LANs, wireless, security, multimedia); Peterson & Davie's free Systems Approach goes bottom-up (foundation, direct links, internetworking, advanced internetworking, end-to-end protocols, congestion control, end-to-end data, security, applications) with implementation focus; Stevens documents TCP/IP as it actually behaves on the wire; HPBN (free) covers latency, TCP/UDP/TLS tuning, wireless, and HTTP/2 for web performance; Beej's Guide (free) is the sockets API tutorial; and RFCs 791 (IP), 793/9293 (TCP), 9110 (HTTP semantics), 1034/1035 (DNS), 8446 (TLS 1.3), 7540 (HTTP/2), 9000 (QUIC) are the specifications.
---
# Networking textbooks and RFCs

## What they are
**Kurose & Ross** (8th ed.): 1 computer networks and the Internet (network edge/core, packet vs
circuit switching, delay/loss/throughput, protocol layers, security, history); 2 application
layer (principles, HTTP, email, DNS, P2P/BitTorrent, video streaming and CDNs, socket
programming); 3 transport layer (multiplexing, UDP, principles of reliable data transfer —
rdt1.0–3.0 with stop-and-wait, go-back-N, selective repeat — TCP segment structure, RTT
estimation, flow control, connection management, congestion control principles, TCP CUBIC/BBR,
fairness, ECN); 4 network layer data plane (router architecture, IP addressing/CIDR/DHCP/NAT,
IPv6, generalized forwarding/OpenFlow, middleboxes); 5 control plane (link-state OSPF, distance-
vector, BGP, SDN control, ICMP, SNMP); 6 link layer (error detection, multiple access — CSMA/
CD, Ethernet, ARP, switches, VLANs, MPLS, data-center networking); 7 wireless and mobile; 8
security. **Peterson & Davie** (free): the same material bottom-up with a "systems approach"
(implementation, performance metrics, bandwidth-delay product) and chapters on end-to-end data
(presentation formatting, compression) and applications. **Stevens** TCP/IP Illustrated vol. 1:
packet traces of each protocol. **HPBN**: primer on latency and bandwidth, TCP (three-way
handshake, slow start, head-of-line blocking), UDP, TLS (handshake, session resumption, OCSP),
wireless/mobile networks, HTTP/1.x, HTTP/2 (multiplexing, header compression, server push),
browser networking APIs. **Beej**: `getaddrinfo`, `socket`/`bind`/`listen`/`accept`/`connect`,
`send`/`recv`, `select`/`poll`, blocking vs non-blocking, IPv4/IPv6 agnostic code.
**RFCs**: 791 IP, 793 (now 9293) TCP, 768 UDP, 1034/1035 DNS, 9110–9112 HTTP semantics/caching/1.1,
7540 → 9113 HTTP/2, 9000 QUIC, 9114 HTTP/3, 8446 TLS 1.3, 4271 BGP-4, 2328 OSPF.

## Key ideas → pages
[[internet-architecture-and-layering]], [[tcp-reliability-and-congestion-control]],
[[ip-routing-and-forwarding]], [[link-layer-and-lans]], [[dns-http-and-the-web-stack]],
[[sockets-programming]].

## What they add
K&R for concepts, Systems Approach for depth and being free, Stevens for the truth on the wire,
HPBN for what web engineers need, Beej for code, RFCs for the last word.

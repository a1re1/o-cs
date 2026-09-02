---
title: Stanford CS144 Introduction to Computer Networking (with MIT 6.829, Berkeley CS168, Princeton COS461)
type: source
section: "4.4"
level: 300
tags: [cs144, networking-course, tcp-implementation, minnow, labs, byte-stream, reassembler, tcp-receiver, tcp-sender, network-interface, ip-router, 6.829, cos461]
sources: []
institution: Stanford
year: 2024
url: https://cs144.github.io/
license: open-course
format: html
summary: CS144 (labs open) teaches networking by building — its "minnow" labs implement a reliable byte stream, a stream reassembler, a TCP receiver and sender (sequence numbers, acknowledgments, retransmission timers, flow-control windows), a network interface doing ARP, and an IP router with longest-prefix-match forwarding, then run the student TCP against real Internet hosts — around lectures on the Internet's architecture (four-layer model, IP service model, encapsulation, end-to-end principle, packet switching), transport (TCP/UDP/ICMP, reliability, flow and congestion control), network layer (addressing, forwarding, routing, NAT), link layer (Ethernet, switching, error detection), and applications (DNS, HTTP, BitTorrent, video); MIT 6.829, Berkeley CS168 and Princeton COS461 cover the graduate and alternative undergraduate arcs.
---
# Stanford CS144

## What it is
Units: 1 the Internet and IP (a day in the life of an application; the four-layer model; the
IP service model — datagram, unreliable, best-effort, connectionless; the life of a packet;
packet switching principles; layering and encapsulation; byte order; IPv4 addresses and CIDR;
longest prefix match; ARP); 2 transport (TCP service model and the three-way handshake; UDP;
ICMP; the end-to-end principle; error detection — checksums, CRC, MAC; finite state machines;
flow control — stop-and-wait, sliding window; retransmission strategies; TCP header; connection
setup/teardown); 3 packet switching (end-to-end delay, packet delay variation, queueing models,
switching and forwarding architectures, output queued and shared memory switches); 4 congestion
control (basics, AIMD, TCP Tahoe/Reno, fairness, ECN, BBR); 5 applications and NAT (NATs and
their types, HTTP, BitTorrent, DNS, DHCP); 6 routing (flooding, spanning tree, Bellman–Ford
and Dijkstra, distance vector vs link state, RIP/OSPF/BGP, multicast); 7 lower layers (physical
layer basics, coding and modulation, wireless, Ethernet, clocks and framing); 8 security (network
attacks, cryptographic tools, TLS, DDoS). **Labs (minnow, C++)**: 0 networking warmup — an
in-memory reliable byte stream; 1 the reassembler (out-of-order substrings into the stream); 2
the TCP receiver (sequence numbers, ack numbers, window); 3 the TCP sender (segmentation,
retransmission timer, RTO doubling, window probing); 4 measuring the real Internet (ping
statistics); 5 the network interface (ARP, Ethernet framing); 6 the IP router (forwarding table,
longest-prefix match, TTL); 7 putting it together — your TCP talks to a real peer.

## What it adds
The lab sequence is the executable version of [[tcp-reliability-and-congestion-control]] and
[[ip-routing-and-forwarding]]; pairs with [[networking-textbooks]] for the reading.

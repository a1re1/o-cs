---
title: The link layer — framing, error detection, multiple access, Ethernet and switching, ARP, VLANs, and wireless
type: concept
section: "4.4"
level: 300
tags: [link-layer, framing, error-detection, parity, checksum, crc, multiple-access, csma-cd, csma-ca, aloha, ethernet, mac-addresses, switches, learning-bridges, spanning-tree, arp, vlan, wifi, 802.11, hidden-terminal, mpls, datacenter-networks, clos]
sources: [networking-textbooks, stanford-cs144]
summary: The link layer moves frames across one physical network — framing bits into frames, detecting errors with parity/checksums/CRC (and correcting with FEC on noisy links), sharing a medium by channel partitioning, random access (ALOHA, CSMA/CD in classic Ethernet, CSMA/CA with RTS/CTS in Wi-Fi where collisions can't be sensed) or taking turns — with Ethernet's flat 48-bit MAC addresses, self-learning switches that flood unknown destinations and build forwarding tables from source addresses, spanning tree to remove loops, ARP to map IP to MAC on the local network, VLANs for isolation, and datacenter Clos fabrics; the wireless link's high, variable loss is what upper layers misread as congestion.
---
# The link layer and LANs

**In one sentence.** One hop, one physical medium: get frames across it reliably enough and
decide who may transmit when.

## Services and error detection (K&R 6.1–6.2)
Framing (delimiters/bit stuffing or length fields), link access, reliable delivery on lossy
links (Wi-Fi ARQ — a performance enhancement per the end-to-end argument), flow control, error
detection: parity (single bit), Internet checksum (16-bit ones' complement — cheap, weak),
**CRC** (polynomial division mod 2; detects all burst errors ≤ r bits — Ethernet CRC-32); error
correction codes (Hamming, Reed–Solomon, LDPC in 5G/Wi-Fi 6) trade bits for reliability
([[channel-capacity-and-error-correction]]). CS144 lab 5 builds the interface.

## Multiple access (K&R 6.3)
- Channel partitioning: TDMA/FDMA/CDMA (cellular).
- Random access: **ALOHA** (efficiency 18%/37% slotted), **CSMA/CD** — listen before talk, abort
  on collision, binary exponential backoff (classic shared Ethernet; obsolete with switches),
  **CSMA/CA** (802.11: can't detect collisions while transmitting; acks, random backoff, RTS/CTS
  for the **hidden terminal** problem).
- Taking turns: polling, token passing; cable (DOCSIS) hybrids.

## Ethernet and switching (K&R 6.4)
48-bit **MAC addresses** (flat, burned-in, locally unique; broadcast ff:ff:ff:ff:ff:ff), frame:
preamble, dst, src, type, payload (46–1500 B MTU; jumbo 9000), CRC. Speeds 10 Mb → 400 Gb; full
duplex point-to-point links to **switches**: self-learning — record (src MAC, port) on each
frame, forward to the known port, **flood** unknown/broadcast; plug-and-play, isolates
collision domains, store-and-forward or cut-through. Loops → broadcast storms → **spanning tree
protocol** (Perlman) disables redundant links (slow; datacenters use routing/ECMP instead).
**VLANs** (802.1Q tag) partition one switch into isolated broadcast domains; trunk ports.
**ARP**: broadcast "who has IP x?" → unicast reply with MAC; cache with timeouts; gratuitous
ARP; spoofable (security). Hosts reach off-subnet destinations via the gateway's MAC.
**MPLS** adds labels for fast switching/traffic engineering in ISP cores.

## Wireless (K&R ch. 7)
Higher bit error rates, fading, interference, half-duplex, mobility; 802.11 associations, rate
adaptation, power saving; cellular handoff; the link-layer retransmissions mask loss from TCP but
add jitter; mobile IP and QUIC connection migration for changing addresses.

## Datacenter networks (K&R 6.6)
Tens of thousands of hosts in racks; top-of-rack switches → **Clos/fat-tree** fabrics with
many equal-cost paths (ECMP by flow hash), full bisection bandwidth; load balancers; RDMA/RoCE
for low latency; DCTCP and shallow buffers ([[tcp-reliability-and-congestion-control]]);
software-defined control ([[ip-routing-and-forwarding]]).

## Pitfalls
- Broadcast storms from loops when STP is misconfigured; MAC table overflow attacks.
- ARP spoofing on shared LANs (why link-layer trust is dangerous — [[security-principles]]).
- Blaming the application for Wi-Fi jitter; treating wireless loss as congestion.
- MTU mismatches across VLAN/tunnel encapsulations (VXLAN adds 50 bytes).

## Related
- [[internet-architecture-and-layering]], [[ip-routing-and-forwarding]], [[channel-capacity-and-error-correction]],
  [[tcp-reliability-and-congestion-control]], [[security-principles]].

## Sources
K&R ch. 6–7; Peterson & Davie ch. 2; CS144 units 1, 7 and lab 5.

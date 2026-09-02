---
title: The network layer — IP addressing and CIDR, forwarding with longest-prefix match, routing (link-state, distance-vector, BGP), NAT, IPv6, and SDN
type: concept
section: "4.4"
level: 300
tags: [ip, ipv4, ipv6, addressing, cidr, subnets, prefix, forwarding-table, longest-prefix-match, router-architecture, ttl, fragmentation, mtu, icmp, traceroute, routing, link-state, ospf, distance-vector, bellman-ford, rip, bgp, autonomous-systems, policy-routing, nat, dhcp, sdn, openflow, anycast, multicast]
sources: [networking-textbooks, stanford-cs144, networking-seminal-papers]
summary: IP gives every interface a hierarchical address (CIDR prefixes aggregate routes), and a router forwards each datagram by longest-prefix match on its destination in a forwarding table (data plane: line cards, switching fabric, output queues), decrementing TTL and fragmenting or signalling MTU problems via ICMP; the tables are computed by routing protocols (control plane) — link-state (OSPF: flood topology, run Dijkstra) inside a domain, distance-vector (Bellman–Ford, RIP; count-to-infinity) historically, and path-vector BGP between autonomous systems where business policy, not shortest paths, decides — while NAT stretches IPv4, IPv6 fixes addressing with 128-bit addresses, and SDN/OpenFlow move the control plane into software programming match-action tables.
---
# IP routing and forwarding

**In one sentence.** Forwarding is a per-packet table lookup; routing is the distributed
algorithm that builds the table; between networks, politics beats Dijkstra.

## Addressing (K&R 4.3, CS144 unit 1)
IPv4: 32-bit addresses written dotted-decimal; **CIDR** prefixes `a.b.c.d/n` (network part n
bits) replaced classful A/B/C; subnets within an organization; **aggregation** lets one
announced prefix cover many; special ranges (private 10/8, 172.16/12, 192.168/16; loopback
127/8; link-local). **DHCP** assigns addresses, gateway, DNS. **NAT** rewrites private
(addr, port) ↔ public (addr, port) at the edge — conserves IPv4, breaks end-to-end
reachability (inbound connections, P2P need hole punching/STUN/TURN), and is why the Internet
ossified around TCP/UDP. **IPv6**: 128-bit addresses (`2001:db8::1`), no fragmentation in
routers, SLAAC, mandatory in mobile networks; dual-stack and NAT64 transitions.

## Forwarding (data plane)
Router: input ports (link + lookup), switching fabric (memory/bus/crossbar), output ports with
queues (scheduling, AQM — [[tcp-reliability-and-congestion-control]]). **Longest-prefix match**:
the forwarding table maps prefixes → next hop; choose the most specific matching prefix (a trie/
TCAM lookup at line rate — [[tries]]); default route 0.0.0.0/0. Per-packet work: verify
checksum (IPv4), decrement **TTL** (drop at 0 and send ICMP time-exceeded — how `traceroute`
works), fragment if larger than the link **MTU** (IPv6: sender must do path-MTU discovery via
ICMP "packet too big"; blackholes when ICMP is filtered), rewrite link header. ICMP carries
errors and `ping`. Match-action generalization: forwarding on any header fields (OpenFlow).

## Routing (control plane — K&R ch. 5, CS144 unit 6)
- **Link-state** (OSPF, IS-IS): every router floods its link states; each builds the full graph
  and runs Dijkstra ([[shortest-paths]]); fast convergence, O(n log n) per node, needs the whole
  topology; areas for scale.
- **Distance-vector** (RIP, EIGRP): each router sends its distance table to neighbours; Bellman–
  Ford relaxation; simple, but **count-to-infinity** on link failure (split horizon, poisoned
  reverse mitigate); slow convergence.
- **BGP** (path-vector, between **autonomous systems**): advertisements carry the AS path
  (loop detection) and attributes; import/export **policies** implement business relationships
  (customer/provider/peer — the Gao–Rexford model: prefer customer routes, don't transit for
  peers); iBGP inside an AS; route selection by local preference → AS-path length → origin → MED
  → …; route hijacks and leaks (RPKI signs origins); ~1M prefixes in the global table.
  Convergence can take minutes; the Internet is a graph of ~75k ASes with a dense core.
- Intra-domain metrics vs inter-domain policy; hot-potato routing; traffic engineering (MPLS,
  segment routing); anycast (same prefix from many sites — DNS root servers, CDNs); multicast
  (mostly intra-domain).

## SDN (McKeown et al. 2008)
Separate the control plane: a logically centralized controller computes state and installs
**match-action** rules in switches over OpenFlow (or programs pipelines with P4); enables
traffic engineering (Google B4), network virtualization, and rapid innovation without new
distributed protocols; the controller becomes the availability/consistency problem
([[distributed-systems-basics]]).

## Pitfalls
- Overlapping/misaligned subnets and asymmetric routes; MTU mismatches with filtered ICMP.
- Assuming shortest-path routing across the Internet (BGP policy, hot potato).
- NAT traversal assumptions in P2P/VoIP; IPv6 as an afterthought (dual-stack bugs).
- Route flaps and convergence during failures; BGP misconfiguration taking down networks.

## Related
- [[internet-architecture-and-layering]], [[link-layer-and-lans]], [[shortest-paths]], [[tries]],
  [[tcp-reliability-and-congestion-control]], [[distributed-systems-basics]], [[consistent-hashing]] (anycast/CDN).

## Sources
K&R ch. 4–5; Peterson & Davie ch. 3–4; CS144 units 1, 5, 6 and lab 6; McKeown et al. 2008; RFC 791, 4271, 2328.

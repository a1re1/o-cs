---
title: TCP — reliable byte streams, sliding windows, retransmission timers, flow control, and congestion control (slow start, AIMD, CUBIC, BBR)
type: concept
section: "4.4"
level: 400
tags: [tcp, udp, reliable-data-transfer, sequence-numbers, acknowledgments, sliding-window, go-back-n, selective-repeat, sack, retransmission-timeout, rtt-estimation, karn, three-way-handshake, flow-control, receive-window, congestion-control, slow-start, aimd, congestion-avoidance, fast-retransmit, fast-recovery, tahoe, reno, cubic, bbr, dctcp, ecn, red, bufferbloat, head-of-line-blocking, quic]
sources: [networking-textbooks, stanford-cs144, networking-seminal-papers]
summary: TCP turns IP's lossy datagrams into an ordered, reliable byte stream with sequence numbers and cumulative (plus selective) acknowledgments, a sliding window that bounds bytes in flight, a retransmission timer set from smoothed RTT and its variance with exponential backoff, a three-way handshake and four-way close, receiver-advertised flow control — and, since Jacobson's 1988 fixes for congestion collapse, congestion control under a packet-conservation principle: slow start to probe capacity exponentially, additive-increase/multiplicative-decrease in congestion avoidance, fast retransmit/recovery on duplicate acks; CUBIC grows the window as a cubic of time since the last loss, BBR paces at the estimated bottleneck bandwidth × min RTT to avoid bufferbloat, DCTCP scales by ECN mark fraction, and RED/AQM in routers signals early; UDP skips all of it and QUIC reimplements it per stream in user space.
---
# TCP: reliability and congestion control

**In one sentence.** Reliability is sequence numbers plus acknowledgments plus a timer;
congestion control is the sender guessing how many packets the network can hold and adjusting
on every signal — and getting the second wrong once melted the Internet.

## Reliable data transfer (K&R 3.4, CS144 labs 1–3)
- Sender numbers bytes; receiver acks the next expected byte (**cumulative ack**); **SACK**
  reports received ranges. Lost or corrupted (checksum) segments are retransmitted when the
  **RTO** fires or on 3 duplicate acks (**fast retransmit**).
- **Sliding window**: sender keeps ≤ W unacked bytes in flight; go-back-N vs selective repeat
  are the textbook forms; throughput ≤ W / RTT, so W must reach the **bandwidth-delay product**
  (window scaling option for > 64 KB).
- **RTO estimation** (Jacobson): SRTT = (1−α)·SRTT + α·R; RTTVAR similarly; RTO = SRTT +
  4·RTTVAR, doubled on each timeout (exponential backoff); Karn's rule — don't sample RTT from
  retransmitted segments. Delayed acks; Nagle's algorithm (coalesce small writes; `TCP_NODELAY`
  to disable — the interaction with delayed acks causes 40 ms stalls).
- **Connection management**: SYN / SYN-ACK / ACK (initial sequence numbers, options: MSS,
  window scale, SACK, timestamps; SYN cookies against floods); FIN/ACK each way; TIME_WAIT
  (2·MSL) to absorb stragglers — the reason servers run out of ports under churn.
- **Flow control**: receiver advertises free buffer (rwnd); sender sends ≤ min(rwnd, cwnd);
  zero-window probing.
- Byte-stream semantics: no message boundaries (applications frame their own — length prefixes,
  delimiters); **head-of-line blocking** — one lost segment stalls all later data.

## Congestion control (Jacobson 1988; K&R 3.7; CS144 unit 4)
Congestion: packets arriving faster than a router can forward them → queues grow (delay) →
drops (loss) → retransmissions add load → **congestion collapse** (Oct 1986). Principle: a
connection in equilibrium should inject a new packet only when an old one leaves (**packet
conservation**); acks clock the sender ("ack clocking").
- **Slow start**: cwnd starts at ~10 MSS (was 1) and doubles every RTT (exponential) until loss
  or the threshold **ssthresh**.
- **Congestion avoidance (AIMD)**: +1 MSS per RTT (additive increase); on loss, cwnd halved
  (multiplicative decrease) — AIMD converges to fairness among flows sharing a bottleneck (Chiu
  & Jain); throughput ≈ 1.22·MSS / (RTT·√p) for loss rate p (Mathis) — long-RTT flows lose.
- Timeout ⇒ back to slow start (Tahoe); 3 dup acks ⇒ **fast retransmit + fast recovery**, halve
  and continue (Reno); NewReno and SACK handle multiple losses.
- **CUBIC** (Linux default): window grows as a cubic function of time since the last loss —
  plateau near the previous max, then probe; RTT-independent, scales to fat pipes.
- **BBR** (Google 2016): model-based — estimate bottleneck bandwidth (max delivery rate) and
  min RTT, pace sending at their product, periodically probe; ignores random loss, fights
  **bufferbloat** (deep router buffers that loss-based control fills, adding seconds of
  latency). BBRv2/v3 add ECN and fairness fixes.
- **Router side**: tail drop vs **RED**/AQM (probabilistic early drop/mark as the average
  queue grows), **ECN** (mark instead of drop; the receiver echoes; sender halves), **DCTCP**
  (datacenters: reduce cwnd proportionally to the *fraction* of marked packets — low latency at
  high utilization), CoDel/FQ-CoDel (per-flow queues, delay-targeted drops) in home routers and
  Linux.
- Fairness and TCP-friendliness: UDP applications should mimic AIMD rates or use congestion-
  controlled transports; parallel connections and short flows in slow start dominate web
  traffic — why HTTP/2 multiplexing and QUIC matter.

## UDP and QUIC
**UDP**: ports + checksum, nothing else — for DNS, real-time media (own loss handling), and as
the substrate for **QUIC** (RFC 9000): user-space transport with TLS 1.3 handshake integrated
(1-RTT/0-RTT), multiple independent streams (no cross-stream HOL blocking), connection IDs for
migration across networks, pluggable congestion control (CUBIC/BBR) — HTTP/3
([[dns-http-and-the-web-stack]]).

## Measuring and tuning
`ss -ti`, `tcpdump`/Wireshark (retransmissions, window sizes, RTT), `iperf3`; kernel knobs
(`tcp_congestion_control`, buffer autotuning, `tcp_notsent_lowat`); watch for bufferbloat
(latency under load) and for MTU/PMTUD black holes.

## Pitfalls
- Treating loss as the only congestion signal on wireless (BBR/ECN help) or believing "no loss
  = no congestion" (bufferbloat).
- Many parallel TCP connections to "speed up" (unfair, slow-start heavy); disabling Nagle
  everywhere instead of buffering writes.
- Reading TCP as a message protocol (partial reads, coalesced writes) — [[sockets-programming]].
- Choosing UDP "for speed" and then reimplementing TCP badly.

## Related
- [[internet-architecture-and-layering]], [[sockets-programming]], [[dns-http-and-the-web-stack]],
  [[queueing-theory]], [[ip-routing-and-forwarding]], [[probabilistic-analysis-of-algorithms]] (AIMD dynamics).

## Sources
K&R ch. 3; Peterson & Davie ch. 5–6; CS144 units 2, 4 and labs 0–3; Jacobson 1988; Floyd & Jacobson 1993; Cardwell et al. 2016; Alizadeh et al. 2010; RFC 9293, 9000.

---
title: Sockets programming — the Berkeley API, TCP vs UDP servers, blocking vs non-blocking I/O, select/poll/epoll, and framing
type: concept
section: "4.4"
level: 200
tags: [sockets, berkeley-sockets, getaddrinfo, socket, bind, listen, accept, connect, send, recv, tcp-server, udp-server, blocking-io, non-blocking, select, poll, epoll, kqueue, io_uring, event-loop, thread-per-connection, framing, partial-reads, byte-order, sockaddr, so_reuseaddr, nagle, keepalive, c10k]
sources: [networking-textbooks, csapp-15-213]
summary: The sockets API exposes transport endpoints as file descriptors — servers `socket`/`bind`/`listen`/`accept`, clients `connect`, both `send`/`recv` (TCP: a byte stream with partial reads and writes, so applications must frame messages; UDP: `sendto`/`recvfrom` datagrams) — with `getaddrinfo` for protocol-agnostic name resolution and network byte order for headers; concurrency comes from a process or thread per connection, or from non-blocking sockets driven by readiness notification (`select`/`poll` O(n), `epoll`/`kqueue` O(1)) in an event loop (the C10K answer used by nginx, Node, Tokio), or completion-based io_uring; and options (`SO_REUSEADDR`, `TCP_NODELAY`, keepalive, timeouts) handle the practical rough edges.
---
# Sockets programming

**In one sentence.** A socket is a file descriptor for a network endpoint; the API is small, the
subtleties (framing, partial I/O, readiness) are where every network bug lives.

## The API (Beej; CSAPP ch. 11)
```
server: getaddrinfo(NULL, "8080", &hints, &res) → socket() → setsockopt(SO_REUSEADDR) → bind() → listen(backlog) → loop: accept() → recv/send → close
client: getaddrinfo("host", "8080", …) → socket() → connect() → send/recv → close
```
- `getaddrinfo` resolves names and services into `sockaddr` lists for IPv4/IPv6; iterate until
  one works. Addresses/ports in **network byte order** (`htons`, `htonl`).
- TCP (`SOCK_STREAM`): `accept` returns a new fd per connection; **partial reads/writes** —
  `recv` may return fewer bytes than asked, `send` may write fewer; loop until done (`rio_readn`
  in CSAPP). No message boundaries: **frame** with length prefixes, delimiters (`\r\n`), or
  fixed sizes; `recv` returning 0 means the peer closed.
- UDP (`SOCK_DGRAM`): `sendto`/`recvfrom` preserve datagram boundaries; no connection, no
  ordering, may be lost; `connect` on a UDP socket just fixes the peer.
- Unix domain sockets for local IPC; raw sockets for packet crafting (privileged).
- Options: `SO_REUSEADDR` (rebind during TIME_WAIT), `SO_REUSEPORT` (multi-process accept),
  `TCP_NODELAY` (disable Nagle for latency-sensitive small writes), `SO_KEEPALIVE`, `SO_RCVBUF`,
  timeouts (`SO_RCVTIMEO`), `shutdown(SHUT_WR)` to half-close. Signals: `SIGPIPE` on writing to
  a closed peer (ignore it, check `EPIPE`).

## Concurrency models (K&R 2.7; the C10K problem)
| Model | Mechanism | Fits |
|---|---|---|
| Iterative | one client at a time | toys |
| Process per connection | `fork` after `accept` (Apache prefork) | isolation, simple |
| Thread per connection | `pthread_create` / thread pool | moderate scale; blocking code stays simple ([[processes-and-threads]]) |
| **Event-driven** | non-blocking fds + `select`/`poll` (scan all fds, O(n)) or `epoll`/`kqueue`/IOCP (readiness lists, O(1) per event) in an event loop; state machines or callbacks/promises | nginx, Redis, Node.js, Tokio, asyncio — tens of thousands of connections ([[async-and-event-driven-concurrency]]) |
| Completion-based | `io_uring` submission/completion rings; async file and network I/O with few syscalls | highest throughput |
Hybrids: N event-loop threads (one per core) with `SO_REUSEPORT`; blocking work offloaded to
pools. **Edge- vs level-triggered** epoll; read until `EAGAIN` under edge triggering.

## Robustness checklist
Handle `EINTR`; loop on short reads/writes; set timeouts (the network *will* hang); bound
buffers (slowloris); back-pressure when the peer is slow (stop reading/`writev` with limits);
validate lengths from the wire; use TLS via a library, never hand-roll
([[dns-http-and-the-web-stack]]); log with connection ids; test with `nc`, `socat`, `tcpdump`,
`ss`. Higher-level: HTTP libraries, gRPC, ZeroMQ, and language runtimes hide most of this — but
the failure modes (partial frames, TIME_WAIT exhaustion, ephemeral port limits, `ulimit -n`)
still surface.

## Pitfalls
- Assuming one `send` = one `recv`; forgetting framing; ignoring the 0 return.
- Blocking calls inside an event loop; unbounded per-connection buffers.
- Using `gethostbyname`/IPv4-only structs; hard-coding byte order.
- Not handling `accept` failures (`EMFILE`) and `SIGPIPE`.

## Sources and related
- [[tcp-reliability-and-congestion-control]], [[dns-http-and-the-web-stack]], [[processes-and-threads]],
  [[async-and-event-driven-concurrency]], [[limited-direct-execution-and-syscalls]], [[shell-and-unix-tools]].

Beej's Guide; CSAPP ch. 11; K&R 2.7; Kegel "The C10K problem"; Linux `epoll(7)`, `io_uring(7)`.

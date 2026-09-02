---
title: Scalable system design (the system-design-primer canon) — how to approach a design question (requirements, back-of-the-envelope estimates, high-level design, deep dives, scaling), performance vs scalability and latency vs throughput, latency numbers every programmer should know, the building blocks (DNS, CDN, load balancers and reverse proxies, stateless application tier and horizontal scaling, relational databases with replication/federation/sharding/denormalization, NoSQL key-value/document/wide-column/graph and SQL vs NoSQL, caching at every layer with cache-aside/write-through/write-behind/refresh-ahead and invalidation, message and task queues with back pressure, communication choices), availability vs consistency (CAP) and availability math, and worked designs (URL shortener, news feed, web crawler, rate limiter)
type: concept
section: "7.3"
level: 400
tags: [system-design, system-design-interview, system-design-primer, scalability, performance-vs-scalability, latency-vs-throughput, back-of-the-envelope, estimation, latency-numbers, powers-of-two, dns, cdn, push-cdn, pull-cdn, load-balancer, layer-4, layer-7, reverse-proxy, horizontal-scaling, vertical-scaling, stateless-tier, session-store, service-discovery, rdbms, master-slave-replication, master-master, federation, sharding, denormalization, sql-tuning, nosql, key-value-store, document-store, wide-column, graph-database, sql-vs-nosql, caching, cache-aside, write-through, write-behind, refresh-ahead, cache-invalidation, cdn-cache, redis, memcached, message-queue, task-queue, back-pressure, asynchronism, rpc-vs-rest, cap-theorem, availability-patterns, failover, availability-math, nines, consistency-patterns, url-shortener, news-feed, fan-out, web-crawler, rate-limiter, token-bucket, capacity-planning, hot-spots, celebrity-problem]
sources: [software-architecture-texts-courses-and-seminal-papers]
summary: The system-design canon — codified by the open system-design-primer and by interview practice — is a method plus a kit of building blocks: the method is to clarify requirements and constraints (users, read/write ratio, data size, latency and availability targets), estimate with back-of-the-envelope numbers (QPS, storage, bandwidth, using the latency numbers every programmer should know — L1 ~1 ns, RAM ~100 ns, SSD read ~100 µs, disk seek ~10 ms, same-datacentre round trip ~0.5 ms, cross-continent ~150 ms — and powers of two), draw the high-level design, then deep-dive into each component and scale by removing bottlenecks; the kit is DNS, CDNs (push vs pull) for static and cacheable content, layer-4/7 load balancers and reverse proxies in front of a stateless, horizontally scaled application tier (session state moved to a shared store), relational databases scaled first by read replicas (master–slave) and tuning, then federation (split by function), sharding (split by key — with the joins, rebalancing and hot-spot costs consistent hashing mitigates) and denormalization, or NoSQL stores chosen by access pattern (key-value for caches/sessions, document for flexible schemas, wide-column for write-heavy time series, graph for relationships) with the SQL-vs-NoSQL trade-off decided by transactions, joins and schema stability, caching at every layer (client, CDN, web server, database, application: Redis/Memcached) with an explicit policy (cache-aside, write-through, write-behind, refresh-ahead) and the invalidation and thundering-herd problems that come with it, message and task queues that decouple producers from consumers and absorb bursts with back pressure when they overflow, and communication choices (REST vs RPC, sync vs async); availability is quantified in nines and composed (sequential components multiply, redundant ones subtract failure products), CAP forces a choice between consistency and availability under partition, and the worked designs — URL shortener (hash/ID generation, redirects, cache), news feed (fan-out on write vs on read, the celebrity problem), web crawler (frontier, politeness, dedup), rate limiter (token bucket, distributed counters) — are the vocabulary drills in which the same handful of blocks recombine; the deeper theory lives in the distributed-systems and database pages this one points to.
---
# Scalable system design

**In one sentence.** Estimate the load, place a small set of well-understood blocks —
load balancers, stateless servers, replicated and sharded databases, caches, queues,
CDNs — where the numbers say the bottleneck is, and know the trade-off each block
carries (consistency, staleness, complexity), because scaling is the art of moving the
bottleneck to somewhere cheaper.

## How to approach a design question (primer "How to approach"; Harvard CS75 lecture)
1. **Requirements and scope**: who uses it and how (features in/out); read:write ratio;
   users/day, peak vs average; data size and growth; latency, availability, consistency
   needs; constraints (budget, team). 2. **Back-of-the-envelope**: QPS = daily requests /
   86 400 (× 2–3 for peak); storage = objects × size × retention; bandwidth = QPS × size;
   memory for cache = 20 % of daily traffic (80/20 rule). Numbers to carry: L1 1 ns; branch
   mispredict 3 ns; L2 4 ns; mutex 17 ns; RAM 100 ns; compress 1 KB 2 µs; send 1 KB over
   1 Gbps 10 µs; SSD random read 150 µs; read 1 MB from RAM 250 µs; same-DC round trip
   500 µs; read 1 MB from SSD 1 ms; disk seek 10 ms; read 1 MB from disk 20 ms; packet
   CA→NL→CA 150 ms ([[caches-and-memory-hierarchy]], [[tail-latency-at-scale]]).
   A server handles ~10³–10⁴ simple QPS; a single RDBMS ~10³–10⁴ writes/s; 1 M QPS needs
   sharding and caching. 3. **High-level design**: clients → DNS/CDN → LB → app servers →
   cache → DB/queue/blob store. 4. **Design core components** (API — [[api-design]]; data
   model and schema; key algorithms — ID generation, hashing, fan-out). 5. **Scale**:
   find the bottleneck, apply a block, repeat; name the trade-offs.

## Performance vs scalability, latency vs throughput, availability vs consistency
**Performance** problem: slow for one user; **scalability** problem: fast for one, slow
under load — a scalable service's performance is proportional to resources added.
**Latency** (time per operation) vs **throughput** (operations per time): aim for maximal
throughput within acceptable latency; batching raises throughput and latency. **CAP**:
under a network partition choose **consistency** (refuse/timeout — CP: banking, leader
election) or **availability** (serve possibly stale — AP: feeds, carts); without a
partition, latency vs consistency (PACELC) — [[distributed-systems-basics]],
[[consistency-models]]. Consistency patterns: weak (best-effort — VoIP, caches), eventual
(replicas converge — DNS, email, Dynamo), strong (linearizable — file systems, RDBMS
transactions). **Availability patterns**: **fail-over** active–passive (heartbeat; promotes
on loss; risk of split brain and lost writes) vs active–active (both serve; DNS/LB
aware); **replication** (below). **Availability math**: 99.9 % = 8.7 h down/year; 99.99 % =
52 min; components in **sequence** multiply (0.999 × 0.999 = 0.998), in **parallel/redundant**
1 − (1 − 0.999)² = 0.999999 ([[site-reliability-engineering]] SLOs).

## The building blocks
- **DNS**: hierarchical, cached by TTL; managed DNS (Route 53) does weighted/latency/geo
  routing; failures/DDoS at DNS are total ([[dns-http-and-the-web-stack]]).
- **CDN**: edge caches serve static (and some dynamic) content near users, offloading
  origin; **push** (you upload; good for small, rarely changing sets) vs **pull** (edge
  fetches on first miss; simpler, redundant traffic until warm, TTL staleness); cost per
  byte; cache-busting via versioned URLs ([[dns-http-and-the-web-stack]]).
- **Load balancer**: distributes across servers, health-checks, removes failed nodes,
  terminates TLS, can maintain sessions (sticky) — but keep servers **stateless** and put
  sessions in a store; **layer 4** (transport: IP/port, fast, no content awareness) vs
  **layer 7** (application: route by path/header/cookie, slower, flexible); algorithms
  round-robin, least-connections, weighted, hash; LB itself redundant (active–passive,
  anycast); **reverse proxy** (nginx/HAProxy/Envoy) adds caching, compression, security,
  a single public face; **horizontal scaling** (many commodity boxes; needs statelessness,
  service discovery, config management) vs **vertical** (bigger box; simpler; ceiling).
- **Application layer**: separate web tier from application/business tier (scale
  independently); **microservices** and **service discovery** (Consul/etcd/ZooKeeper;
  [[microservices-and-resilience-patterns]]); async workers behind queues.
- **Database — relational**: ACID transactions ([[transactions-and-concurrency-control]]);
  scale by **master–slave replication** (writes to master, reads from replicas; replica lag
  → stale reads; promote on failure) or **master–master** (both accept writes; needs
  conflict resolution or a loose consistency model; ID generation coordination);
  **federation** (split by function: users DB, products DB — fewer joins, more
  application logic); **sharding** (split rows by key — user id hash/range/geo; each
  shard smaller and faster; costs: cross-shard joins, rebalancing when adding shards —
  [[consistent-hashing]] — **hot spots** / the celebrity problem, complex application
  logic); **denormalization** (duplicate to avoid joins; materialized views; write
  amplification, consistency work); **SQL tuning** (benchmark, profile, indexes —
  [[storage-engines-and-indexes]], schema/type tightening, partition hot tables, avoid
  expensive joins, connection pooling — [[query-optimization]]). See
  [[replication-and-partitioning]].
- **Database — NoSQL** (BASE: basically available, soft state, eventual consistency):
  **key-value** (Redis, Memcached, DynamoDB core — O(1) get/put, caches, sessions, rate
  counters); **document** (MongoDB, Couch, DynamoDB — JSON-ish documents, flexible schema,
  per-document atomicity); **wide-column** (Bigtable, HBase, Cassandra — rows × column
  families, sorted keys, write-optimized LSM storage — [[storage-engines-and-indexes]];
  time series, high write throughput); **graph** (Neo4j — nodes/edges, traversal-heavy
  social/recommendation queries). **SQL vs NoSQL**: SQL for structured, relational,
  transactional data with joins and mature tooling and when you need the query
  planner; NoSQL for semi-structured, massive write throughput, flexible schema, simple
  access patterns known in advance (design the table for the query), horizontal scale
  as a first-class feature ([[relational-model]], [[distributed-databases-and-nosql]]).
- **Cache**: layers — client/browser, CDN, web server (reverse proxy), **database cache**
  (buffer pool), **application cache** (Redis/Memcached; in-memory,
  LRU/LFU eviction; cache rows, query results, objects/aggregates; avoid caching raw
  queries with complex invalidation). **Policies**: **cache-aside** (lazy: app checks
  cache, on miss reads DB and writes cache; only requested data cached; miss penalty;
  staleness until TTL/invalidation), **write-through** (write to cache which writes to
  DB synchronously; reads fast and fresh; write latency; cold data cached needlessly),
  **write-behind/back** (write to cache, async flush to DB; fast writes; data loss risk on
  crash), **refresh-ahead** (refresh hot items before expiry; needs good prediction).
  Problems: **invalidation** ("two hard things"), **thundering herd**/cache stampede on
  expiry of a hot key (locks, request coalescing, jittered TTLs, early recompute),
  **hot keys** (replicate/local cache), consistency between cache and DB (delete-on-write,
  versioned values).
- **Asynchronism**: **message queues** (RabbitMQ, SQS, Kafka) hold work so the request
  returns immediately and workers process later (emails, thumbnails, feed fan-out);
  **task queues** (Celery) for scheduled/background jobs; **back pressure**: bounded queues
  that reject (503 + retry-after) when full instead of growing until latency explodes;
  precompute expensive views offline (nightly batch — [[mapreduce-and-dataflow]]).
- **Communication**: HTTP/REST vs **RPC** (gRPC/Thrift — internal, typed, faster; tight
  coupling) — [[api-design]]; TCP vs UDP (reliability vs latency — video, DNS, games);
  WebSockets/SSE for push.
- **Security** basics: TLS, hash+salt passwords, parameterized queries, least privilege,
  input validation — [[web-security]], [[security-principles]].

## Worked designs (primer solutions; interview canon)
**URL shortener** (Pastebin): write path — generate a short key (base-62 of a counter or
Snowflake-style unique id with timestamp+machine+sequence; or hash+truncate with
collision check), store {key → url, expiry}; read path (≫ writes) — 301/302 redirect,
cache hot keys (cache-aside), read replicas; analytics via async queue. **News feed /
timeline**: **fan-out on write** (push: on post, insert into every follower's feed list in
Redis — fast reads, expensive for celebrities with millions of followers) vs **fan-out on
read** (pull: on request, merge recent posts of followees — cheap writes, slow reads);
hybrid: push for normal users, pull for celebrities; ranking service; pagination by
cursor. **Web crawler**: URL frontier with priority and **politeness** (per-host queues,
robots.txt, rate), fetchers, dedup of URLs (Bloom filter — [[randomized-algorithms]]) and content
(simhash), DNS cache, distributed by host hash, checkpointing, freshness recrawl policy
. **Rate limiter**: token bucket / sliding window per key in
Redis (atomic Lua), at the gateway; distributed counters with local approximation;
return 429 + headers. Others: chat (WebSockets, message ids, presence), key-value store
([[replication-and-partitioning]], [[consistent-hashing]], quorums), search
autocomplete (trie + top-k, precomputed), notification system (queues, fan-out,
dedup), typeahead, ticket booking (locks/optimistic concurrency), metrics/logging
pipeline ([[mapreduce-and-dataflow]]), object storage, video streaming (CDN, transcoding
pipeline, adaptive bitrate).

## Pitfalls
- Skipping estimates — designing for 10⁶ QPS when the load is 10; or the reverse.
- Stateful app servers behind a load balancer; sticky sessions as architecture.
- Caching without an invalidation story; unbounded queues; retries without back-off.
- Sharding before replication and caching are exhausted; choosing NoSQL to avoid
  schema design and then needing joins.
- Treating CAP as "pick two" without partitions; ignoring replication lag in reads.

## Related
- [[software-architecture-and-system-design]], [[microservices-and-resilience-patterns]],
  [[api-design]], [[distributed-systems-basics]], [[consistency-models]],
  [[replication-and-partitioning]], [[consistent-hashing]], 
  [[caches-and-memory-hierarchy]], [[storage-engines-and-indexes]], [[query-optimization]],
  [[storage-engines-and-indexes]],  [[mapreduce-and-dataflow]],
  [[mapreduce-and-dataflow]], [[site-reliability-engineering]], [[dns-http-and-the-web-stack]],
  [[dns-http-and-the-web-stack]], [[web-security]].

## Sources
Martin, system-design-primer (read: headings; "How to approach", latency numbers, solutions); Malan, Harvard CS75 "Scalability" lecture; Dean 2009/2012 (numbers every programmer should know; "Designs, lessons and advice"); Kleppmann 2017 ch. 1, 5–6, 11; Abadi 2012 (PACELC); Brewer 2000/2012 (CAP); Beyer et al. 2016 (SRE); Xu 2020 (*System Design Interview*).

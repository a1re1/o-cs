---
title: Distributed file and object storage — GFS/Colossus and HDFS, Ceph and CRUSH, Haystack, S3-style object stores, and the metadata problem
type: concept
section: "4.8"
level: 400
tags: [distributed-file-system, object-storage, gfs, colossus, hdfs, namenode, ceph, rados, crush, placement, haystack, blob-storage, s3, buckets, keys, metadata, chunks, replication, erasure-coding, consistency, read-after-write, multipart-upload, versioning, lifecycle, tiering, cdn, nfs, afs, posix, data-lakes, parquet]
sources: [storage-and-cloud-seminal-papers, datacenter-and-sre-books]
summary: Storage at datacenter scale separates metadata (names, locations, permissions) from data (chunks/objects on many disks) and the design question is where the metadata lives and how consistent the data path must be: GFS/HDFS keep a single in-memory master (simple, a scaling and availability limit — Colossus shards it into Bigtable and HDFS federates NameNodes); Ceph computes placement with CRUSH from a small cluster map so clients and OSDs need no lookup table and rebalancing is deterministic; Haystack shows that for billions of small immutable objects the metadata lookup itself is the bottleneck, so pack objects into large files with an in-memory index; and cloud object stores (S3, GCS, Azure Blob) expose a flat key/value namespace over erasure-coded, multi-AZ storage with simple durable semantics (put/get/list, multipart upload, versioning, lifecycle tiering, now strong read-after-write) that has become the data lake substrate (Parquet, Iceberg) — while POSIX semantics (NFS, AFS, Lustre, GPFS) survive where applications need them, at the cost of coherence and metadata scalability.
---
# Distributed file and object storage

**In one sentence.** Every large storage system is a small metadata problem (where is it?)
wrapped around a large data problem (how do I move and protect it?), and the good designs
keep them apart.

## Lineage
NFS (stateless server, close-to-open consistency), AFS (whole-file caching with callbacks,
volumes), Frangipani/Petal, Lustre/GPFS (parallel file systems for HPC with striping across
object servers) → GFS (2003) → HDFS (2006) → Colossus, Ceph (2006), Haystack (2010), cloud
object stores (S3 2006, Azure Storage 2011 paper, GCS).

## GFS / HDFS (Ghemawat et al. 2003)
Design from workload: component failure is normal (thousands of commodity machines); files are
huge (multi-GB, billions of objects inside them); mutations are appends, reads are sequential;
co-design the API with applications (relaxed consistency, record append). One **master** with
in-memory metadata (namespace, file → chunks, chunk → chunkserver locations learned at
startup), operation log replicated + checkpoints; **chunkservers** store 64 MB chunks as Linux
files with checksums, replicated 3× across racks; clients cache locations, stream data through
a pipeline of replicas, and a **lease** makes one replica primary to order mutations; record
append is atomic at-least-once (duplicates/padding visible to readers); re-replication,
rebalancing, garbage collection by lazy deletion; snapshots via copy-on-write. Limits: master
memory and single-master throughput, small files, latency. **HDFS** copies the design
(NameNode/DataNodes, 128 MB blocks, write-once) and later adds erasure coding, federation and
HA NameNodes. **Colossus**: metadata in Bigtable (itself on Colossus — bootstrapped by a
small GFS-like Chubby-managed layer), Reed–Solomon, flash for hot data, client-driven
replication ([[raid-and-erasure-coding]], [[mapreduce-and-dataflow]]).

## Ceph and CRUSH (Weil et al. 2006)
Object storage daemons (**OSDs**) with **RADOS** replicate and recover among themselves;
placement: object → placement group (hash) → OSDs via **CRUSH**, a deterministic pseudo-random
function over the cluster map and placement rules (failure domains: host/rack/row) — no central
lookup, any client computes locations; map changes propagate and only affected data moves
(cf. [[consistent-hashing]]); monitors run Paxos for the map ([[consensus-paxos-raft]]);
metadata servers with dynamic subtree partitioning for the POSIX layer (CephFS); RBD block
devices and RGW S3 gateway on the same substrate; BlueStore writes directly to raw devices with
checksums and RocksDB metadata ([[storage-engines-and-indexes]]).

## Haystack (Beaver et al. 2010)
Facebook photos on NFS needed ~3 disk reads per photo for directory/inode metadata; with
billions of small files the metadata didn't fit in cache. Solution: **needles** appended to
~100 GB haystack files, an in-memory index (key → offset, size) per store machine, one disk
read per photo; directory maps photos to logical volumes; cache tier for recent uploads; CDN in
front for hot content; deletes as flags, compaction later. Successors: f4 (warm blobs with
erasure coding across datacenters), Tectonic (unified). The lesson generalizes: small objects
need packing and an in-memory index ([[storage-engines-and-indexes]], LSM/log-structured).

## Cloud object storage (S3 and kin)
Flat namespace: bucket + key → object (up to TBs; multipart upload; ETags), simple HTTP API
(put/get/delete/list with prefix; no rename, no append, no partial overwrite); durability by
erasure coding across three+ availability zones (11 nines), availability SLAs (99.9–99.99 %),
strong read-after-write consistency (S3 since 2020; earlier eventual for overwrites), versioning,
lifecycle policies to colder tiers (IA, Glacier: minutes–hours retrieval), object lock,
server-side encryption, pre-signed URLs, event notifications, request-rate scaling per prefix.
Costs: per-GB-month, per-request, egress. Usage: backups, static sites via CDN
([[dns-http-and-the-web-stack]]), **data lakes** — columnar files (Parquet/ORC) + table formats
(Iceberg, Delta, Hudi) + query engines (Trino, Spark, DuckDB) → separation of storage and
compute ([[distributed-databases-and-nosql]]); block storage (EBS/Persistent Disk — replicated
volumes with Physalia-style control planes) and managed file systems (EFS, Lustre) complete
the menu.

## Consistency and semantics
POSIX (byte-range writes, coherence across clients, rename atomicity) is expensive across
machines; most scale-out systems weaken it: write-once/append-only, close-to-open, eventual
listing, immutable objects with versioning. Applications adapt (rename-free commit protocols
for Spark/Iceberg; idempotent puts; manifests). Metadata scalability is the recurring limit:
single master → sharded → computed placement.

## Pitfalls
- Millions of small files on GFS/HDFS-style systems; deep directories on object stores.
- Assuming rename/append/listing are atomic or consistent; treating S3 like a POSIX disk.
- Single-AZ buckets/volumes; no lifecycle rules (cost) or versioning (ransomware).
- Ignoring egress and request costs in architecture.

## Related
- [[raid-and-erasure-coding]], [[file-systems]], [[replication-and-partitioning]],
  [[consistent-hashing]], [[mapreduce-and-dataflow]], [[storage-engines-and-indexes]],
  [[cloud-and-serverless]], [[warehouse-scale-computing]].

## Sources
Ghemawat et al. 2003; Weil et al. 2006; Beaver et al. 2010; Calder et al. "Windows Azure Storage" 2011; Muralidhar et al. "f4" 2014; Pan et al. "Tectonic" 2021; AWS S3 documentation; WSC ch. 2–3.

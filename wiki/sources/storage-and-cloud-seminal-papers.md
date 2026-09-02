---
title: Storage and cloud seminal papers — RAID (1988), GFS (2003) and Colossus, Ceph (2006), Haystack (2010), Amazon S3 and Dynamo, Borg/Omega/Kubernetes (2015–16), Schroeder et al. flash reliability (2016), and "Cloud Programming Simplified" (Berkeley serverless, 2019)
type: source
section: "4.8"
level: 500
tags: [raid, patterson-gibson-katz, gfs, colossus, ceph, crush, weil, haystack, facebook, s3, dynamo, borg, omega, kubernetes, flash-reliability, schroeder, serverless, cloud-programming-simplified, jonas, berkeley-view]
sources: []
authors: [David Patterson, Garth Gibson, Randy Katz, Sanjay Ghemawat, Sage Weil, Doug Beaver, Giuseppe DeCandia, Abhishek Verma, Brendan Burns, Bianca Schroeder, Eric Jonas, Ion Stoica]
year: 1988
institution: various
url: https://www.cs.cmu.edu/~garth/RAIDpaper/Patterson88.pdf
license: various
format: pdf
summary: Patterson, Gibson & Katz argued that arrays of inexpensive disks with redundancy (RAID levels 1–5: mirroring, bit/byte striping with Hamming or single parity, block striping with dedicated or rotated parity) beat single large expensive disks on performance, cost and reliability; GFS built a distributed file system for Google's workload — component failure is the norm, files are huge, mutations are appends, and co-designing the API with applications allows a relaxed consistency model — with a single master and replicated 64 MB chunks (Colossus later sharded the metadata and used Reed–Solomon); Ceph removed the central allocation table with CRUSH, a pseudo-random placement function over a cluster map, and RADOS self-managing object storage; Haystack showed that Facebook's photo store was bound by metadata lookups and packed photos into large append-only files with an in-memory index; S3 and Dynamo defined cloud object and key-value storage with eleven-nines durability via replication/erasure coding across failure domains; Borg, Omega and Kubernetes traced cluster management from monolithic scheduler to shared-state to declarative controllers; Schroeder's field study found flash raw bit errors grow slowly with wear, are not predictive of uncorrectable errors, SLC is no more reliable than MLC in practice, and SSDs are replaced less but have more uncorrectable errors than disks; and the Berkeley serverless view predicted FaaS becomes the default cloud programming model once its storage, communication and cold-start limits are addressed.
---
# Storage and cloud seminal papers

| Paper | Contribution | Page |
|---|---|---|
| Patterson, Gibson & Katz, "A Case for Redundant Arrays of Inexpensive Disks" (1988) | I/O will squander CPU gains unless it scales; five RAID levels with cost/performance/reliability analysis; parity to survive one disk failure; MTTF and repair-time math | [[raid-and-erasure-coding]] |
| Ghemawat, Gobioff & Leung, "The Google File System" (2003); Colossus (talks, 2010s) | Failure is normal; huge append-mostly files; single master with in-memory metadata + chunkservers; relaxed consistency and record append; Colossus: distributed metadata in Bigtable, Reed–Solomon encoding, flash tiering | [[distributed-file-and-object-storage]], [[mapreduce-and-dataflow]] |
| Weil et al., "Ceph: A Scalable, High-Performance Distributed File System" (2006); "CRUSH" (2006) | Decouple data and metadata; **CRUSH** computes placement from the cluster map (no lookup table, failure-domain aware); RADOS OSDs handle replication, recovery, and rebalancing peer-to-peer; dynamic subtree partitioning for metadata | [[distributed-file-and-object-storage]] |
| Beaver et al., "Finding a Needle in Haystack: Facebook's Photo Storage" (2010) | POSIX metadata lookups (several disk reads per photo) were the bottleneck; store photos as needles in large log files with an in-memory index → one disk read per photo; CDN in front; write-once, delete-rarely | [[distributed-file-and-object-storage]] |
| Amazon S3 (2006; "Millions of Tiny Databases", ShardStore, and re:Invent talks); DeCandia et al., Dynamo (2007) | Object storage with buckets/keys, eventual → strong read-after-write consistency (2020), 11 nines durability via erasure coding across AZs, lifecycle tiers; Dynamo's availability-first KV design | [[distributed-file-and-object-storage]], [[distributed-databases-and-nosql]] |
| Verma et al., Borg (2015); Schwarzkopf et al., Omega (2013); Burns et al., "Borg, Omega, and Kubernetes" (2016) | Monolithic → shared-state optimistic scheduling → declarative API with controllers; labels, pods, reconciliation loops | [[cluster-scheduling-and-observability]] |
| Schroeder, Lagisetty & Merchant, "Flash Reliability in Production" (FAST 2016); Schroeder & Gibson disk studies (2007) | Millions of drive-days: RBER grows slowly with PE cycles; UBER is not meaningful; SLC ≈ MLC in the field; SSDs replaced less than HDDs but more uncorrectable errors; age matters more than use; disks: AFR 2–4 %, not the datasheet 0.5 % | [[ssd-and-nvme-storage]], [[raid-and-erasure-coding]] |
| Jonas et al., "Cloud Programming Simplified: A Berkeley View on Serverless Computing" (2019) | Serverless = FaaS + BaaS; autoscaling and pay-per-use; limitations (ephemeral storage, no direct communication, cold starts, hardware access) and predictions | [[cloud-and-serverless]] |

## Why read them
RAID for the reliability arithmetic everyone still uses; GFS/Ceph/Haystack for three
different answers to "where does the metadata live"; Schroeder for the gap between datasheets
and fleets; the Berkeley view for where the cloud's programming model is heading.

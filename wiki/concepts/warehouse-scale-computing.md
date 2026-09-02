---
title: Warehouse-scale computing — the datacenter as one computer, its memory/storage hierarchy, power and cooling (PUE), cost modeling, energy proportionality, and failure as the normal case
type: concept
section: "4.8"
level: 400
tags: [warehouse-scale-computer, wsc, datacenter, barroso, holzle, cluster-architecture, storage-hierarchy, latency-numbers, pue, power-usage-effectiveness, power-distribution, ups, cooling, free-cooling, energy-proportionality, power-capping, tco, capex, opex, cost-per-server, commodity-hardware, failures-are-normal, availability, hardware-accelerators, tpu, rack, cluster-network, clos, disaggregation]
sources: [datacenter-and-sre-books, storage-and-cloud-seminal-papers]
summary: Barroso and Hölzle's warehouse-scale computer is a building of tens of thousands of commodity servers run as a single machine for a few very large internet services, whose design is governed by economics — cost per unit of work drives commodity parts, cheap hardware plus fault-tolerant software beats reliable hardware, and the building (power distribution, UPS, cooling, PUE = total facility power / IT power, now ~1.1 at the best operators) and energy (servers are least efficient at the low utilizations they usually run at, hence energy proportionality and power capping) matter as much as the servers — with a memory/storage hierarchy that spans local DRAM (100 ns), rack and cluster DRAM over the network (10–100 μs), local and remote flash and disk (100 μs–10 ms) so software must be written for the cluster, not the server; failures are continuous at this scale (thousands of disk, DIMM, machine, and network events per year per cluster) and are handled by replication, retries and automated repair rather than avoided, and accelerators (GPUs, TPUs) and disaggregation are the current hardware trend.
---
# Warehouse-scale computing

**In one sentence.** When one program runs on ten thousand machines, the building is the
computer, and its architecture is decided by cost per operation, watts, and the certainty
that something is always broken.

## The WSC (Barroso, Hölzle & Ranganathan ch. 1–2)
Not a hosting datacenter (many small tenants) but a homogeneous fleet running a few very
large applications (search, ads, email, video, ML training/serving) owned by one organization
— so hardware and software are co-designed and economies of scale apply. Software stack:
platform (kernel, libraries), cluster-level (resource management — Borg/Kubernetes
[[cluster-scheduling-and-observability]]; storage — GFS/Colossus/Bigtable/Spanner; RPC,
monitoring), application-level. Workloads: request-level parallelism (many independent
users) and data-level parallelism (MapReduce) — embarrassingly parallel at the top, latency-
critical at the bottom ([[tail-latency-at-scale]]). "Buy vs build": Google builds the whole
stack; the cloud rents it.

## Hardware building blocks (ch. 3)
Cost-efficient servers (low-end/commodity beat high-end per dollar — but not too weak:
Amdahl and per-request latency); racks (~40 servers, top-of-rack switch), clusters (Clos
fabrics — [[link-layer-and-lans]]). **The WSC storage hierarchy** (order-of-magnitude
numbers every engineer should know): L1 ~1 ns, DRAM ~100 ns, rack DRAM over network ~100 μs
(now ~10 μs with RDMA), local flash ~100 μs, datacenter flash ~1 ms, local disk ~10 ms,
datacenter disk ~10s ms; bandwidths fall and capacities rise down the hierarchy. Accelerators
(GPUs, TPUs — [[parallel-architectures-simd-gpu]]) for ML; SmartNICs/DPUs; disaggregated
memory (CXL) and storage (NVMe-oF — [[ssd-and-nvme-storage]]).

## Power, cooling and the building (ch. 4–5)
Utility → transformers → UPS (batteries/flywheels; Google moved batteries onto server
shelves) → PDUs → racks; generators for outages. Cooling: computer-room air handlers, hot/
cold aisle containment, chillers, **free cooling** (outside air, evaporative), liquid cooling
for high-density AI racks. **PUE** = total facility energy / IT equipment energy: industry
average ~1.6, best ~1.1 (Google fleet 1.10); water usage (WUE) and carbon are the next
metrics. **Energy proportionality**: servers draw 40–60 % of peak power at idle, and WSCs run
at 10–50 % utilization, so efficiency at low load is the target (DVFS, idle states, consolidation
— [[cluster-scheduling-and-observability]]); **power provisioning/capping** oversubscribes the
building's power budget safely since not everything peaks together. Energy per operation is
now the design constraint for chips and clusters (hence accelerators — [[performance-equation-and-amdahl]]).

## Cost (ch. 6)
TCO = datacenter capex (amortized over ~10–15 years; ~$10–20 per watt of critical power) +
server capex (3–4 years) + opex (power, staff, repairs, software). A server-year is dominated by
server cost, then power; utilization is the multiplier — an idle fleet is the most expensive
one. Cloud pricing (on-demand, reserved, spot/preemptible — [[cloud-and-serverless]]) exposes
these curves to customers.

## Failures and repairs (ch. 7)
Per cluster per year (Google, Dean's numbers): ~1000 machine failures, thousands of disk
failures, DIMM errors (Schroeder: 8 % of DIMMs see correctable errors yearly; ECC mandatory),
network events, power events, and software/config/human-caused outages dominating actual
unavailability. Hence: **fault-tolerant software** (replication, retries, redundancy across
failure domains — [[replication-and-partitioning]], [[raid-and-erasure-coding]]), automatic
detection and repair queues, degrading gracefully, and treating repair rate rather than
failure rate as the lever. Availability = MTTF/(MTTF+MTTR); the SRE discipline turns this into
SLOs ([[site-reliability-engineering]]).

## Pitfalls
- Designing for the server rather than the cluster (assuming local disk is durable or local
  memory sufficient).
- Ignoring utilization: idle capacity costs the same as busy capacity.
- Treating hardware failure as exceptional (no automation) or as the main cause of outages
  (it isn't — software and operations are).
- Benchmarking PUE alone (a PUE of 1.05 with inefficient servers still wastes energy).

## Related
- [[cluster-scheduling-and-observability]], [[tail-latency-at-scale]], [[site-reliability-engineering]],
  [[cloud-and-serverless]], [[distributed-file-and-object-storage]], [[raid-and-erasure-coding]],
  [[link-layer-and-lans]], [[performance-equation-and-amdahl]].

## Sources
Barroso, Hölzle & Ranganathan, The Datacenter as a Computer, 3rd ed. (2018); Dean "Numbers Everyone Should Know"; Schroeder, Pinheiro & Weber "DRAM Errors in the Wild" 2009; Google Environmental Report (PUE).

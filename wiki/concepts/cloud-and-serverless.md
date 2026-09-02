---
title: Cloud computing and serverless — IaaS/PaaS/FaaS, virtual machines and containers, elasticity and pricing, the serverless programming model and its limits
type: concept
section: "4.8"
level: 400
tags: [cloud-computing, iaas, paas, saas, faas, serverless, aws, gcp, azure, virtual-machines, containers, docker, images, orchestration, kubernetes, autoscaling, elasticity, spot-instances, pricing, multi-tenancy, availability-zones, regions, managed-services, baas, cold-starts, function-as-a-service, lambda, firecracker, infrastructure-as-code, terraform, cloud-programming-simplified, vendor-lock-in, egress]
sources: [datacenter-and-sre-books, storage-and-cloud-seminal-papers]
summary: The cloud rents warehouse-scale computing by the hour (VMs — IaaS), by the deployed application (PaaS), or by the invocation (FaaS/serverless), with elasticity (autoscaling within minutes, spot capacity at a discount), regions and availability zones as failure domains, and a catalog of managed services (object storage, databases, queues, ML) that replace operations with APIs; the enabling technologies are hardware virtualization (KVM/Xen, Nitro/microVMs) for isolation and multi-tenancy and containers (namespaces, cgroups, layered images) for packaging, orchestrated by Kubernetes; serverless (Lambda and kin) takes the abstraction furthest — stateless functions triggered by events, scaled to zero, billed per 100 ms, isolated in Firecracker microVMs — and the Berkeley view (2019) argues it becomes the default once cold starts, ephemeral storage, lack of direct communication, and hardware access are solved; the trade-offs are cost at steady high utilization, egress and lock-in, and the need for infrastructure as code and cost engineering as first-class disciplines.
---
# Cloud computing and serverless

**In one sentence.** The cloud turns the datacenter's economics into an API — and every
layer of abstraction above raw VMs trades control for not having to run it yourself.

## Service models and building blocks
| Layer | You manage | Examples |
|---|---|---|
| IaaS | OS and up | EC2/Compute Engine VMs, block/object storage (EBS, S3 — [[distributed-file-and-object-storage]]), VPC networking |
| Containers as a service | app + container config | EKS/GKE (Kubernetes — [[cluster-scheduling-and-observability]]), ECS, Cloud Run |
| PaaS | code + config | App Engine, Heroku, Elastic Beanstalk |
| FaaS / serverless | functions | Lambda, Cloud Functions, Azure Functions, Cloudflare Workers |
| BaaS / managed services | schemas and calls | DynamoDB, Aurora, BigQuery, SQS/Pub-Sub, Kinesis, SageMaker |
Regions (independent geographies) contain **availability zones** (separate power/network/
building, low latency between) — the failure domains for replication
([[replication-and-partitioning]]). Identity and access (IAM), infrastructure as code
(Terraform, CloudFormation, Pulumi), networking (VPCs, load balancers, CDNs). **Elasticity**:
autoscaling groups on metrics; **spot/preemptible** instances at 60–90 % discounts for
interruptible work; reserved/committed pricing for steady load; pay-as-you-go turns capex into
opex ([[warehouse-scale-computing]] cost model exposed).

## Virtualization and containers (Berkeley "Above the Clouds" 2009; OSTEP)
**VMs**: hardware virtualization (VT-x/AMD-V, EPT — [[os-kernels-and-virtualization]]) for
strong isolation among tenants; hypervisors (Xen originally at AWS, KVM now; Nitro offloads
networking/storage/security to cards so the host runs nearly bare-metal); live migration.
**Containers**: process-level isolation with namespaces (pid, net, mnt, user) and cgroups
(CPU, memory, I/O limits), packaged as layered images (Dockerfile → OCI image; content-
addressed layers — [[git-data-model]]); fast start, dense packing, weaker isolation
(shared kernel) — hence gVisor (user-space kernel), Kata/Firecracker (microVMs per container)
for multi-tenant safety. Orchestration: Kubernetes for scheduling, service discovery, rolling
updates, autoscaling; service meshes (Envoy/Istio) for RPC policy and observability.

## Serverless (Jonas et al. 2019; Brooker on Lambda)
Function-as-a-service: upload code; the platform provisions, scales to zero and to thousands,
isolates each invocation (Firecracker microVMs, snapshot restore), bills per invocation and
100 ms; triggered by HTTP, queues, storage events, schedules. Plus **BaaS** for state (object
storage, serverless databases, queues) — "serverless = FaaS + BaaS". Benefits: no capacity
planning, fine-grained pay-per-use, fast iteration. Limits (the Berkeley view): **cold starts**
(100 ms–seconds; mitigated by snapshots, provisioned concurrency), short lifetimes and small
ephemeral storage, no direct addressing between functions (communication goes through slow
storage — "serverless is a data-shipping architecture"), no accelerators (changing), limited
observability, unpredictable cost at high steady load. Predictions: better ephemeral/durable
storage services, fine-grained coordination, and serverless becoming the default cloud
programming model; workflow orchestration (Step Functions, Durable Functions) and edge
functions (Workers) as the growth areas. Design rules: stateless, idempotent, small, event-
driven, with state in managed services ([[distributed-systems-basics]] for retries/duplicates).

## Economics and strategy
Utilization arbitrage: cloud wins for variable or small loads and for speed; owned hardware
wins at large steady load (the "cloud repatriation" debate); **egress** pricing and
proprietary services create lock-in; multi-cloud costs complexity. FinOps: tagging, budgets,
rightsizing, reserved commitments, spot for batch, shutting things off. Reliability: design
for AZ loss (multi-AZ) and, for the critical few, region loss; the provider's control plane is
itself a dependency ([[site-reliability-engineering]]).

## Pitfalls
- Lift-and-shift VMs paying cloud premiums for none of the elasticity.
- Serverless for long-running or chatty workloads; functions calling functions synchronously.
- Single AZ; no IaC (click-ops drift); secrets in images; open buckets.
- Ignoring egress and per-request costs; unbounded autoscaling during an attack.

## Related
- [[warehouse-scale-computing]], [[cluster-scheduling-and-observability]], [[os-kernels-and-virtualization]],
  [[distributed-file-and-object-storage]], [[site-reliability-engineering]], [[replication-and-partitioning]],
  [[distributed-databases-and-nosql]], [[git-data-model]].

## Sources
Armbrust et al. "Above the Clouds" 2009; Jonas et al. "Cloud Programming Simplified" 2019; Agache et al. "Firecracker" 2020; Burns et al. 2016; AWS Well-Architected Framework; OSTEP virtualization appendix.

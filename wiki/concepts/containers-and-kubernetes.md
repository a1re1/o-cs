---
title: Containers and Kubernetes — what a container is (namespaces, cgroups, union filesystems, OCI images and layers, registries), Docker images and Dockerfiles (layer caching, multi-stage builds, minimal bases), containers vs VMs, the Twelve-Factor App, Kubernetes architecture (control plane: API server, etcd, scheduler, controller manager; nodes: kubelet, kube-proxy, container runtime), the declarative model and reconciliation loops, core objects (Pods, Deployments and ReplicaSets, StatefulSets, DaemonSets, Jobs/CronJobs, Services and Ingress/Gateway, ConfigMaps and Secrets, Volumes and PersistentVolumeClaims, Namespaces, RBAC), probes and self-healing, resource requests/limits and QoS, scheduling (affinity, taints, topology spread), autoscaling (HPA/VPA/cluster), rollouts, Helm/Kustomize and operators, and what Kubernetes costs
type: concept
section: "7.4"
level: 400
tags: [containers, docker, kubernetes, k8s, namespaces, cgroups, union-filesystem, overlayfs, oci, images, layers, layer-caching, registry, dockerfile, multi-stage-build, distroless, containers-vs-vms, twelve-factor, control-plane, api-server, etcd, scheduler, controller-manager, kubelet, kube-proxy, container-runtime, containerd, cri, declarative, desired-state, reconciliation, control-loop, controllers, pods, deployments, replicasets, statefulsets, daemonsets, jobs, cronjobs, services, clusterip, nodeport, loadbalancer, ingress, gateway-api, configmaps, secrets, volumes, persistent-volumes, pvc, storage-classes, namespaces-k8s, rbac, service-accounts, liveness-probe, readiness-probe, startup-probe, self-healing, requests-limits, qos-classes, oom, scheduling, affinity, taints-tolerations, topology-spread, hpa, vpa, cluster-autoscaler, rolling-update, helm, kustomize, operators, crds, service-mesh, borg, complexity-cost]
sources: [devops-cicd-and-sre-texts-courses-and-seminal-papers]
summary: A container is a process (tree) run with Linux kernel isolation — namespaces for what it can see (pid, net, mnt, uts, ipc, user), cgroups for what it can use (CPU, memory, I/O) — on a root filesystem assembled from immutable, content-addressed image layers via a union filesystem, so it starts in milliseconds and ships as one artifact from laptop to production, unlike a VM which virtualizes a whole machine and kernel; Docker made this usable with Dockerfiles (each instruction a cached layer — order for cache hits, multi-stage builds to keep runtime images minimal), registries, and the OCI standards, and the Twelve-Factor App is the discipline that makes services container-friendly (config in the environment, stateless processes, logs to stdout, disposability); Kubernetes (the open-source descendant of Google's Borg) runs containers across a cluster with a declarative model — you submit desired state as objects to the API server (backed by etcd), and controllers run reconciliation loops that drive actual state toward it, which is how self-healing, rollouts and scaling all work — with a control plane (API server, etcd, scheduler, controller manager) and nodes (kubelet, kube-proxy, a CRI runtime such as containerd); the core objects are Pods (one or more co-scheduled containers sharing network and volumes), Deployments (ReplicaSets with rolling updates and rollback) for stateless work, StatefulSets for ordered, stable-identity stateful work, DaemonSets (one per node), Jobs/CronJobs, Services (stable virtual IP and DNS name over a set of Pods; ClusterIP/NodePort/LoadBalancer), Ingress/Gateway for HTTP routing, ConfigMaps and Secrets, Volumes/PersistentVolumeClaims with StorageClasses, Namespaces and RBAC; the kubelet's liveness, readiness and startup probes decide restarts and traffic, resource requests drive scheduling while limits cap usage (QoS classes decide who gets evicted first), the scheduler honours affinity/anti-affinity, taints and tolerations and topology spread, autoscalers scale Pods (HPA on metrics, VPA on right-sizing) and nodes (cluster autoscaler), Helm and Kustomize template and patch manifests, and operators extend the model with custom resources and controllers for databases and other complex systems; the cost is real — a large, fast-moving platform with its own networking, storage and security surface — so the right question is whether the team needs cluster-level scheduling and self-healing at all, or a PaaS/serverless platform that hides it.
---
# Containers and Kubernetes

**In one sentence.** A container is an ordinary Linux process wearing kernel-enforced
blinkers (namespaces) and a budget (cgroups) on top of an immutable layered image; Kubernetes
is a control loop that keeps a cluster's actual state converging on the state you
declared — everything else is objects for saying what you want.

## What a container is (Docker docs; OSTEP virtualization — [[os-kernels-and-virtualization]])
**Namespaces** isolate what a process sees: `pid` (its own process tree), `net` (own
interfaces, routing, ports), `mnt` (own mount table/root), `uts` (hostname), `ipc`, `user`
(uid mapping — rootless containers), `cgroup`, `time`. **cgroups** (v2) limit and account
what it uses: CPU shares/quota, memory (OOM-kill at the limit), I/O, pids. **Root
filesystem** from an **image**: an ordered list of content-addressed, read-only **layers**
(tarballs) unioned by **overlayfs** with a thin writable layer on top — layers are shared
between images and cached by digest; the **OCI** image and runtime specs standardize the
format and `runc`-style execution; `containerd`/CRI-O manage lifecycle. Security
defaults: dropped capabilities, seccomp profile, no-new-privileges, read-only rootfs
where possible; containers share the host kernel — a kernel exploit escapes them, hence
gVisor/Kata/Firecracker micro-VMs for multi-tenant isolation ([[cloud-and-serverless]]).
**Containers vs VMs**: VM = virtual hardware + guest kernel (strong isolation, seconds to
boot, GBs); container = shared kernel (ms to start, MBs, weaker isolation, denser). **Not**
a security boundary by default; a packaging and resource-isolation unit.

## Images, Dockerfiles, registries
`Dockerfile`: `FROM` base → `RUN`/`COPY`/`ADD` (each a layer; **cache** invalidates from the
first changed instruction downward — copy dependency manifests and install before
copying source), `ENV`, `EXPOSE`, `USER` (non-root), `ENTRYPOINT`/`CMD`; **multi-stage
builds** (build in a fat image, `COPY --from=` the binary into a minimal runtime base —
distroless, alpine, scratch) to shrink attack surface and size; `.dockerignore`;
reproducibility via pinned base digests; **registries** (Docker Hub, GHCR, ECR/GCR/ACR)
store layers by digest; tags are mutable — deploy by **digest**; scan images (Trivy,
Grype) and sign (cosign/Sigstore) for supply-chain integrity ([[security-principles]]).
BuildKit for parallel, cached builds; `docker compose` for local multi-container dev.
The **Twelve-Factor App** (Heroku, 2011): one codebase, explicit dependencies, config in
the environment, backing services as attached resources, strict build/release/run
separation, stateless share-nothing processes, port binding, concurrency via processes,
disposability (fast start, graceful stop on SIGTERM), dev/prod parity, logs as event
streams to stdout, admin tasks as one-off processes — the checklist that makes an app
schedulable by anything ([[continuous-integration-and-delivery]] build-once).

## Kubernetes architecture and the reconciliation model (k8s docs "Concepts" — read; Borg)
**Control plane**: **kube-apiserver** (the only thing that talks to **etcd**, the Raft-
replicated key-value store holding all cluster state — [[distributed-systems-basics]];
REST API, authn/authz/admission webhooks, watch streams), **kube-scheduler** (assigns
Pods to nodes: filter feasible nodes, score, bind), **kube-controller-manager** (the
built-in controllers), cloud-controller-manager. **Nodes**: **kubelet** (runs Pods
assigned to it via the CRI runtime, reports status, runs probes), **kube-proxy** (Service
virtual IPs via iptables/IPVS/eBPF), a CNI network plugin (every Pod gets a routable IP;
flat network). **Declarative model**: you `apply` an object's **spec** (desired state); a
**controller** watches objects, compares `status` (observed) with `spec`, and acts to
converge — repeatedly, idempotently, level-triggered (state, not events). Deployment
controller → ReplicaSet controller → kubelet: "3 replicas" becomes three Pods, and stays
three when one dies (**self-healing**). Labels/selectors bind objects loosely
(`app=web`); annotations for metadata; **Namespaces** partition objects; **RBAC** (Roles,
ClusterRoles, bindings to users/ServiceAccounts); owner references and garbage
collection; leases for leader election. Everything is an API object — and the API is
extensible (**CRDs** + custom controllers = **operators**). Borg lineage
([[cluster-scheduling-and-observability]]): bin-packing, priorities/preemption,
resource reclamation.

## Core objects
- **Pod**: one or more containers scheduled together, sharing network namespace
  (localhost) and volumes; ephemeral; init containers (run first), **sidecar** containers
  (proxies, log shippers — service mesh — [[microservices-and-resilience-patterns]]).
- **Deployment** → **ReplicaSet** → Pods: stateless replicas; **rolling update** (`maxSurge`,
  `maxUnavailable`), revision history and `rollout undo`; **StatefulSet**: stable
  ordinal names (`db-0`), stable per-replica storage, ordered start/stop — for databases,
  queues; **DaemonSet**: one Pod per node (agents); **Job**/**CronJob**: run-to-completion.
- **Service**: stable ClusterIP + DNS (`svc.ns.svc.cluster.local`) load-balancing over
  Pods matching a selector (EndpointSlices); **NodePort**, **LoadBalancer** (cloud LB),
  headless (DNS to Pod IPs); **Ingress**/**Gateway API**: L7 HTTP routing, TLS termination
  via a controller (nginx, Envoy, cloud); **NetworkPolicy** for east-west firewalling.
- **ConfigMap** / **Secret** (base64, not encrypted by default — enable envelope encryption,
  or external secret stores) injected as env vars or files; **Volumes**: emptyDir,
  hostPath, projected; **PersistentVolume**/**PersistentVolumeClaim** with **StorageClass**
  dynamic provisioning via CSI drivers; snapshots.
- **Probes** (kubelet): **liveness** (restart if failing — only for deadlock-style
  failures; never depend on downstreams), **readiness** (remove from Service endpoints
  while failing — the one that gates traffic during startup/overload), **startup**
  (slow starters). Graceful termination: SIGTERM → `terminationGracePeriodSeconds` →
  SIGKILL; `preStop` hooks; PodDisruptionBudgets for voluntary disruptions.
- **Resources**: `requests` (scheduler reserves; guaranteed) and `limits` (cgroup cap;
  CPU throttled, memory OOM-killed); **QoS**: Guaranteed (req = lim) > Burstable >
  BestEffort — eviction order under node pressure; LimitRanges and ResourceQuotas per
  namespace.
- **Scheduling**: node selectors, (anti-)affinity (spread replicas across nodes/zones),
  **taints and tolerations** (dedicated/GPU nodes), **topology spread constraints**,
  priority classes and preemption; **HPA** (scale replicas on CPU/memory/custom metrics),
  **VPA** (right-size requests), **cluster autoscaler**/Karpenter (add/remove nodes).
- **Packaging**: **Helm** charts (templated manifests + values; releases), **Kustomize**
  (overlays/patches, built into kubectl), **GitOps** (Argo CD/Flux reconcile the cluster
  to a Git repo — [[infrastructure-as-code-and-devops]]); **operators** (Prometheus,
  Postgres, Kafka operators encode day-2 operations).

## What Kubernetes costs, and alternatives
You operate: a control plane (or pay a managed one — EKS/GKE/AKS), networking (CNI,
ingress, mesh), storage (CSI), identity (RBAC, IRSA/Workload Identity), observability
([[observability-monitoring-and-incident-response]]), upgrades three times a year with
deprecations, YAML sprawl, and a security surface (Pod Security Standards, admission
policies — OPA/Kyverno, image provenance). Good fit: many services, heterogeneous
workloads, multi-cloud/portability, teams that need a shared platform with self-service.
Poor fit: a small team with one app — a PaaS (Heroku/Fly/Render/Cloud Run), serverless
([[cloud-and-serverless]]), or plain VMs + a container runtime costs far less cognitive
load. Kubernetes is a platform for building platforms; most teams want the platform on
top (an internal developer platform), not the substrate.

## Pitfalls
- No resource requests (scheduler flies blind; noisy neighbours) or limits far above
  requests (overcommit → OOM storms); CPU limits causing throttling latency.
- Liveness probes that check dependencies → restart cascades during a downstream outage.
- Running as root; `latest` tags; secrets in ConfigMaps or Git; no NetworkPolicies.
- Single replica Deployments called "highly available"; no PodDisruptionBudget; no
  anti-affinity across zones.
- Treating containers as VMs (ssh-ing in, mutating state) — rebuild and redeploy instead.

## Related
- [[os-kernels-and-virtualization]], [[cluster-scheduling-and-observability]],
  [[cloud-and-serverless]], [[continuous-integration-and-delivery]],
  [[infrastructure-as-code-and-devops]], [[observability-monitoring-and-incident-response]],
  [[microservices-and-resilience-patterns]], [[site-reliability-engineering]],
  [[distributed-systems-basics]], [[security-principles]], [[dns-http-and-the-web-stack]].

## Sources
Kubernetes documentation, Concepts (read: index; Overview, Cluster Architecture, Workloads, Services, Storage, Configuration, Security, Scheduling); Verma et al. 2015 (Borg); Burns et al. 2016 ("Borg, Omega, and Kubernetes", CACM); Docker documentation; OCI specs; Wiggins 2011 (Twelve-Factor); Hightower, Burns & Beda, *Kubernetes: Up and Running* (3e 2022); Arpaci-Dusseau, OSTEP (virtualization chapters).

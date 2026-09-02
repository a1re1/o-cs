---
title: Infrastructure as code and DevOps — the DevOps movement (the Three Ways: flow, feedback, continual learning; "you build it, you run it"; class SRE implements DevOps), the DORA capabilities and Westrum culture, infrastructure as code (declarative vs imperative, Terraform's providers/resources/state/plan/apply/modules, drift, immutable infrastructure, configuration management with Ansible/Puppet/Chef, image baking), GitOps and reconciliation, environments and configuration design (SRE Workbook), secrets management, cloud resource models and cost, policy as code, and platform engineering
type: concept
section: "7.4"
level: 300
tags: [devops, three-ways, flow, feedback, continual-learning, devops-handbook, phoenix-project, you-build-it-you-run-it, sre-vs-devops, dora, capabilities, westrum, generative-culture, blameless, infrastructure-as-code, iac, declarative, imperative, terraform, opentofu, pulumi, cloudformation, cdk, providers, resources, state, state-file, remote-state, state-locking, plan-apply, modules, workspaces, drift, drift-detection, immutable-infrastructure, cattle-not-pets, configuration-management, ansible, puppet, chef, salt, idempotent, image-baking, packer, golden-images, gitops, argo-cd, flux, reconciliation, environments, dev-staging-prod, environment-parity, configuration-design, config-as-code, secrets-management, vault, kms, sops, least-privilege, policy-as-code, opa, sentinel, cloud-cost, finops, platform-engineering, internal-developer-platform, toil]
sources: [devops-cicd-and-sre-texts-courses-and-seminal-papers]
summary: DevOps is the cultural and technical movement that dissolves the wall between development and operations — The DevOps Handbook's Three Ways are flow (small batches, visible work, WIP limits, fewer handoffs), feedback (telemetry everywhere, problems swarmed when found, "andon cord"), and continual learning (blameless postmortems, game days, converting local discoveries into global improvements), Amazon's "you build it, you run it" puts the team on call for its own code, and Google's SRE is one implementation ("class SRE implements DevOps": SLOs, error budgets and toil caps as the concrete mechanisms) — and DORA's research ties the outcomes to specific capabilities (continuous delivery, loosely coupled architecture, empowered teams, lean product practices, monitoring, and a Westrum "generative" culture where information flows and failure leads to inquiry); infrastructure as code applies software practice to infrastructure: declare the desired resources in versioned, reviewed, tested files and let a tool converge reality to them — Terraform/OpenTofu model cloud APIs as providers and resources, record what they created in a state file (kept remote, locked, and treated as sensitive), show a plan (the diff) before apply, and compose modules, while configuration-management tools (Ansible, Puppet, Chef) converge machines idempotently and image bakers (Packer) plus immutable infrastructure ("cattle, not pets": replace, never patch in place) remove drift by construction; GitOps closes the loop by making a Git repository the desired state and a controller (Argo CD, Flux) the reconciler, so every change is a pull request with an audit trail and a rollback is a revert; the discipline extends to environments that mirror production (parity, ephemeral preview environments), configuration design (SRE Workbook: safe defaults, validation, staged rollout of config because config changes cause as many outages as code), secrets kept out of code in a vault or KMS with short-lived credentials and least privilege, policy as code (OPA/Sentinel checks in the pipeline), and cost visibility; the current synthesis is platform engineering — an internal developer platform that packages CI/CD, IaC, observability and guardrails as self-service paved roads so product teams get DevOps outcomes without every team re-learning Kubernetes.
---
# Infrastructure as code and DevOps

**In one sentence.** Treat operations as software — infrastructure declared in
version-controlled code, environments converged by tools rather than hands, changes
shipped through the same reviewed pipeline as application code — and treat the
organization as a system whose flow, feedback loops and learning are what you optimize.

## DevOps: the Three Ways and what SRE adds (Kim et al. 2016; SRE Workbook ch. 1 — ToC read)
Born from the 2009 "10+ deploys per day" talk (Flickr) and the Phoenix Project's
manufacturing analogy (work in progress, bottlenecks — "Brent", unplanned work as the
silent killer). **First Way — flow** (dev → ops → customer): make work visible, limit
WIP, small batches, reduce handoffs, remove constraints, continuous delivery
([[continuous-integration-and-delivery]]). **Second Way — feedback** (right to left): see
problems as they occur (telemetry, [[observability-monitoring-and-incident-response]]),
swarm and fix at the source, push quality closer to the work, optimize for downstream
work centres. **Third Way — continual learning**: institutionalize improvement (20 %
time, kaizen blitzes), blameless postmortems, inject failures on purpose
([[chaos-engineering-and-reliability-testing]]), turn local learning into global.
Anti-patterns: a "DevOps team" as a new silo; renaming ops "DevOps engineers"; tools
without culture. **SRE** (Google): "class SRE implements DevOps" — DevOps names the
values; SRE prescribes mechanisms — SLOs and **error budgets** to negotiate velocity vs
reliability, a **50 % cap on toil**, shared on-call, blameless postmortems, and engineers
who own operations ([[site-reliability-engineering]]). **DORA capabilities** (Accelerate):
technical (version control for everything, deployment automation, CI, trunk-based
development, test automation, test-data management, shift-left security, CD, loosely
coupled architecture, empowered tool choice, monitoring, proactive notification),
process (customer feedback, value-stream visibility, small batches, team
experimentation), lean management (change approval that is lightweight — heavyweight
CABs correlate with *worse* stability, WIP limits, visual management), cultural (Westrum
**generative** culture: high cooperation, messengers trained, risks shared, bridging
encouraged, failure → inquiry, novelty implemented; vs pathological/bureaucratic; job
satisfaction, learning). The result measured by the DORA metrics
([[software-engineering-fundamentals]]).

## Infrastructure as code (Morris; Terraform docs)
Principles: **everything in version control** (network, compute, DNS, IAM, alerts,
dashboards); **declarative** desired state (what, not how) over imperative scripts;
**idempotent** application (running twice changes nothing); **reviewed** like code (PRs,
plan output in the review, [[code-review]]), **tested** (lint, policy, `terraform validate`,
unit tests with mocks, ephemeral integration environments, Terratest), **reproducible**
(a new environment from scratch in minutes — the real test of IaC and of disaster
recovery). **Terraform/OpenTofu**: **providers** wrap cloud/SaaS APIs; **resources** and
data sources in HCL; the **state file** maps config to real resource IDs (store it
**remotely** — S3+DynamoDB lock, GCS, Terraform Cloud — with **locking**; it contains
secrets and is a single point of truth; never hand-edit; `import` existing resources);
`terraform plan` computes the diff (create/update/replace/destroy — read **replace**
carefully: it destroys) and `apply` executes it in dependency order (a DAG —
[[build-systems-and-make]]); **modules** for reuse (versioned, registry); **workspaces** or
directory-per-environment; `for_each`/`count`; lifecycle rules (`prevent_destroy`,
`create_before_destroy`). Alternatives: CloudFormation/Bicep (native), **Pulumi**/**CDK**
(general-purpose languages generating declarative state), Crossplane (Kubernetes-style
reconciliation of cloud resources). **Drift**: reality diverging from code (console
changes, failed applies); detect with periodic `plan`, prevent by removing write access
outside the pipeline. **Configuration management** (Ansible — agentless, push, YAML
playbooks; Puppet/Chef/Salt — agent, pull, converge) for in-place server configuration —
useful for pets, declining as **immutable infrastructure** takes over: bake **images**
(Packer → AMIs/containers) with everything installed, deploy by replacing instances,
never patch running ones ("cattle, not pets"); config at boot via cloud-init/env
([[containers-and-kubernetes]] is the endpoint of this trend). Provisioning vs
configuration vs deployment are separate layers with separate tools.

## GitOps and environments (Argo CD/Flux; Humble & Farley; SRE Workbook ch. 14–15)
**GitOps**: the Git repo *is* the desired state (manifests, Helm values, Terraform); a
**reconciler** in the cluster pulls and applies continuously and reports drift; changes are
PRs (review, audit, rollback = revert), no `kubectl apply` from laptops, no CI credentials
to production (the cluster pulls). Repository layouts: app repo (code) vs config repo
(environments); promotion = PR from staging overlay to prod overlay. **Environments**:
dev → (per-PR **preview environments**, ephemeral) → staging (prod-like, same IaC, smaller)
→ production; **parity** (Twelve-Factor: same OS, versions, backing services) or you ship
"works on staging" bugs; test data management; environment-specific config as a small,
explicit delta. **Configuration design** (Workbook): config changes cause outages as often
as code — so config is code (versioned, reviewed, validated at load, safe defaults,
minimal), rolled out **progressively** (canary config), with the same rollback path;
prefer fewer knobs; distinguish static (build-time) from dynamic (runtime, feature
flags) configuration; beware "configuration in a DSL that became a programming
language" (Jsonnet/CUE address this deliberately).

## Secrets, policy, cost
**Secrets**: never in code, images, or state in plaintext; a **secret manager** (Vault, AWS
Secrets Manager/KMS, GCP Secret Manager, SOPS-encrypted files in Git, Kubernetes
external-secrets); **short-lived credentials** (OIDC federation from CI to cloud, workload
identity, IAM roles — no long-lived keys); rotation; audit; **least privilege** per
pipeline stage and per service ([[security-principles]]). **Policy as code**: OPA/Rego,
Sentinel, Kyverno, Checkov/tfsec — enforce "no public buckets", "tags required",
"encryption on", "no `0.0.0.0/0` ingress" in the pipeline, not in a wiki; guardrails
over gates. **Cost** (FinOps): tagging, budgets and alerts, right-sizing from utilization
data, reserved/spot capacity, autoscaling down, deleting orphans — IaC makes cost
reviewable per PR (Infracost) ([[cloud-and-serverless]] economics). **Disaster recovery**:
backups tested by restore, RPO/RTO targets, multi-region via the same IaC.

## Platform engineering
Every product team re-solving CI, Kubernetes, IaC, secrets, and observability is toil at
organizational scale; a **platform team** builds an **internal developer platform**: paved
roads/golden paths (templates, service scaffolding — Backstage), self-service
environments and pipelines, standard observability and SLO tooling, guardrails as code —
treated as a product with users (Team Topologies: stream-aligned teams consume a
platform from a platform team via a thin interaction). Metrics: time to first deploy for
a new service, lead time, on-call load, toil hours. The failure mode is a mandatory,
bespoke platform that lags the ecosystem — keep the platform thin and the escape hatches
open.

## Pitfalls
- State file in a laptop or in Git; unlocked state; secrets in plaintext state/repos.
- ClickOps drift; `apply` without reading the plan; a `replace` on a database.
- A "DevOps team" silo; CABs approving every change; tools without on-call ownership.
- Staging that doesn't resemble production; config changes without canaries.
- Long-lived cloud keys in CI; over-broad IAM roles; no policy checks.

## Related
- [[continuous-integration-and-delivery]], [[containers-and-kubernetes]],
  [[observability-monitoring-and-incident-response]], [[site-reliability-engineering]],
  [[chaos-engineering-and-reliability-testing]], [[cloud-and-serverless]],
  [[build-systems-and-make]], [[code-review]], [[security-principles]],
  [[software-engineering-fundamentals]], [[technical-debt-and-maintenance]].

## Sources
Kim, Humble, Debois & Willis 2016 (*The DevOps Handbook*); Kim, Behr & Spafford 2013; Forsgren, Humble & Kim 2018; Beyer et al. 2018 (Workbook) ch. 1, 14–15 (ToC read); Beyer et al. 2016 ch. 5, 7 (ToC read); Morris 2020 (*Infrastructure as Code* 2e); Terraform/OpenTofu documentation; Brikman 2022 (*Terraform: Up and Running*); Weaveworks 2017 (GitOps); Wiggins 2011; Skelton & Pais 2019 (*Team Topologies*); Westrum 2004.

---
title: Infrastructure requirements
weight: 2
variants: -flyte +union
---

# Infrastructure requirements

A {{< key product_name >}} self-hosted deployment is built from standard cloud-provider primitives — one or more Kubernetes clusters, VPC(s), object storage, managed identity bindings, TLS-terminating ingress, a container image registry, and a managed PostgreSQL instance for the control plane. Nothing on this page is {{< key product_name >}}-specific infrastructure; it is your cloud account's standard infrastructure wired up to support {{< key product_name >}}'s control plane and data plane.

The default and recommended topology is **separate-cluster** — the control plane and data plane run in different Kubernetes clusters, communicating over the control plane's external ingress. This isolates blast radius (a DP cluster outage doesn't affect CP availability), allows the two planes to evolve independently, and matches how multi-region and multi-environment deployments naturally lay out. **Intra-cluster** — both planes in the same cluster — is supported as a [special case](#intra-cluster-topology) (covered at the end of this page) for footprint-constrained deployments, lab environments, and the [Getting started](./getting-started) walkthrough.

For the installation walkthrough, see [Getting started](./getting-started).

## Sizing model

Self-hosted has two distinct sizing regimes, driven by very different workload signals.

- **Self-hosted runs in single-tenant mode**: one organization per deployment.
- **Control plane is steady-state.** CP footprint scales with **active users** and **concurrent actions in flight** — not with task-pod volume on the data plane side. Once provisioned, CP changes only when those dimensions grow. CP sizing is a one-time exercise revisited annually or when growth dictates.
- **Data plane is peak-driven.** DP footprint tracks the maximum concurrent execution load: actions running, nodes provisioned, pods per node, IPs consumed, NIC and disk throughput. DP sizing must accommodate workload bursts, and the constraints stack — every limit (vCPU quota, pod IP allocation, conntrack table, etcd object count, registry pull rate) bites independently as workload grows.

### Workload signals → size mapping

| Signal | Small | Medium | Large |
| --- | --- | --- | --- |
| Active users | ≤25 | 25–200 | 200+ |
| Concurrent running actions | ≤500 | 500–5,000 | 5,000–30,000+ |
| Peak worker nodes (DP) | ≤25 | 25–250 | 250–3,000+ |
| Peak vCPU consumption (DP) | ≤500 | 500–10,000 | 10,000–90,000 |

### How to read this page

For each resource, the **substrate** description covers what to provision (shared between CP and DP where applicable). Then **Control plane** and **Data plane** sub-blocks describe defaults and scale-up triggers specific to each plane. Where a resource is exclusive to one plane (e.g., the database is CP-only), only that plane's sub-block appears. AWS/GCP tabs show the concrete realization.

## Pre-installation checklist

Provision the following resources in your cloud account before installing the {{< key product_name >}} Helm charts. Each item links to the section on this page that covers requirements in detail, and to the relevant cloud-provider documentation for the creation step itself. The {{< key product_name >}} chart assumes all of these are in place at install time.

The checklist is split between **shared substrate** (resources both planes use or that exist once per cluster), **Control plane** (resources the CP needs), and **Data plane** (resources the DP needs). In separate-cluster topology you complete the per-plane sections for each cluster; in intra-cluster topology the lists collapse onto a single cluster.

### Shared substrate (per cluster)

1. **(GCP only) Enable required project APIs** — see [Project APIs (GCP)](#project-apis-gcp). [Vendor docs: Enabling and disabling services](https://cloud.google.com/service-usage/docs/enable-disable).
2. **VPC and subnets** — see [Networking](#networking). [AWS: Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) · [GCP: Create a VPC network](https://cloud.google.com/vpc/docs/create-modify-vpc-networks).
3. **NAT egress** — single NAT gateway (cost-optimized) or per-AZ (resilient). [AWS: NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) · [GCP: Cloud NAT](https://cloud.google.com/nat/docs/set-up-manage-network-address-translation).
4. **Kubernetes cluster** — managed control plane (EKS / GKE / AKS) plus the system node pool described under [Kubernetes cluster](#kubernetes-cluster). [AWS: Create an EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) · [GCP: Create a GKE cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).
5. **Workload identity foundation** — IRSA OIDC provider (AWS) or Workload Identity Federation (GCP). See [Identity and workload binding](#identity-and-workload-binding). [AWS: Configure IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) · [GCP: GKE Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

### Control plane

6. **Managed PostgreSQL** — instance plus the network plumbing for the CP cluster to reach it privately. See [Database](#database). [AWS: Create an RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) · [GCP: Cloud SQL Private Service Access](https://cloud.google.com/sql/docs/postgres/configure-private-services-access).
7. **CP object storage buckets** — metadata bucket (admin state) and artifacts bucket. See [Object storage → Control plane](#object-storage). [AWS: Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) · [GCP: Create storage buckets](https://cloud.google.com/storage/docs/creating-buckets).
8. **CP service accounts and IAM bindings** — identity bindings for flyteadmin / datacatalog / cacheservice / artifacts. See [Identity → Control plane](#control-plane-2).
9. **Ingress + DNS** — public DNS name for the CP, a TLS certificate, and a DNS zone (`external-dns` writes records into the zone). See [Ingress and DNS](#ingress-and-dns).
10. **OAuth applications in your identity provider** — the Helm-side step, but the IdP work happens here. See [Authentication](./authentication).

### Data plane

11. **DP system node pool capacity** — the DP cluster's system pool hosts the operator (agent), ingress proxy, and executor. Same sizing as the CP system pool. See [Kubernetes cluster → Data plane](#data-plane).
12. **DP object storage buckets** — metadata bucket (per DP cluster) and fast-registration bucket. See [Object storage → Data plane](#object-storage). Vendor docs same as above.
13. **DP service accounts and IAM bindings** — identity bindings for flytepropeller / executor / cluster-resource-sync, plus per-namespace task-pod KSAs, plus the log-pipeline service account (AWS only — the {{< key product_name >}} fluentbit DaemonSet; GCP uses the managed GKE logging agent). See [Identity → Data plane](#data-plane-1).
14. **Container image registry** — private registry for task images (the image builder writes here; nodes pull from here), plus credentials to pull {{< key product_name >}}'s system images. See [Container image registry](#container-image-registry).
15. **Logging backend** — where task pod stdout/stderr is collected and made available to the data plane operator's log-streaming API. AWS writes via the {{< key product_name >}} fluentbit DaemonSet (to S3 by default, or CloudWatch); GCP uses GKE's managed Cloud Logging agent. See [Logging](#logging).

### Shared optional

16. **Secrets store** (optional) — only if you choose to sync from a cloud secrets store rather than supply Kubernetes secrets directly. Used by both planes. See [Secrets](#secrets).

After this list is complete, follow [Getting started](./getting-started) for the in-cluster install steps (Helm charts, Kubernetes secrets, OAuth client wiring in your IdP).

## Project APIs (GCP)

GCP requires explicit API enablement per project before resources backed by those services can be provisioned. The {{< key product_name >}} Terraform modules enable the following APIs in each plane's project:

| API | Used by |
| --- | --- |
| `compute.googleapis.com` | GKE node pools, VPC, Cloud NAT |
| `container.googleapis.com` | GKE control plane |
| `servicenetworking.googleapis.com` | Cloud SQL private service access (CP only) |
| `sqladmin.googleapis.com` | Cloud SQL (CP only) |
| `secretmanager.googleapis.com` | If syncing secrets from Google Secret Manager |
| `iam.googleapis.com` | Service accounts and Workload Identity Federation |
| `artifactregistry.googleapis.com` | Artifact Registry for task images |
| `storage.googleapis.com` | GCS buckets |
| `cloudresourcemanager.googleapis.com` | IAM policy bindings |

Enable via the [`gcloud services enable`](https://cloud.google.com/sdk/gcloud/reference/services/enable) command, the Cloud Console, or your IaC tool of choice.

AWS does not have an equivalent per-account API-enablement step; the relevant services are universally available subject to account-level service quotas.

## Kubernetes cluster

A managed Kubernetes cluster (EKS, GKE, or AKS) for each plane. Separate-cluster topology means two clusters — one hosting the control plane, one hosting the data plane. The CP cluster is sized once and changes rarely; the DP cluster is sized for peak workload.

### Substrate

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

| Component | Setting |
| --- | --- |
| Service | Amazon EKS |
| Kubernetes version | 1.33 |
| Cluster autoscaler | Karpenter for the DP cluster |

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

| Component | Setting |
| --- | --- |
| Service | Google Kubernetes Engine (GKE) |
| Release channel | REGULAR |
| Networking | VPC-native (alias IPs) |
| Max pods per node | 30 (recommended; default 110 — see [Pod density and IP allocation](#pod-density-and-ip-allocation)) |

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Control plane

The CP cluster hosts the control plane services (admin, identity, queue service, executions, ScyllaDB, monitoring stack, ingress). Sized for steady-state.

| Component | Default |
| --- | --- |
| System node pool | 3 nodes, general-purpose on-demand compute, ~4 vCPU / 16 GB minimum per node. **Avoid burstable / `t`-series instance types** — their conntrack-table and CPU-credit limits cause unpredictable failures under sustained CP load |
| Topology | Single regional cluster, multi-AZ |

**Scale up when**:

- **Control plane services run hot** (admin / executions / identity sustained high CPU) → step up to the next-larger instance size in the same family, or move to a compute-optimized variant.
- **More active users or concurrent actions in flight** → scale the admin / identity / executions deployments horizontally. The queue service is single-replica; scale it vertically (raise its CPU / memory limits) rather than adding replicas.

### Data plane

The DP cluster runs the data plane's own system services (the {{< key product_name >}} operator that acts as an agent for the control plane, the ingress proxy, and the executor that schedules task pods) alongside the worker pools that run user tasks. Sized for peak workload; the [scaling constraints](#scaling-constraints) section enumerates the per-cluster ceilings to plan around.

| Component | Default |
| --- | --- |
| System node pool | 3 nodes, general-purpose on-demand compute, ~4 vCPU / 16 GB minimum per node. Hosts the operator (agent), ingress proxy, and executor. **Avoid burstable / `t`-series** instance types — the same conntrack and CPU-credit gotchas apply here as on the CP side |
| Worker pool | **No strict requirements** — worker capacity is intended to be configurable and workload-dependent. Pick instance family, size, disk, and autoscaling bounds for your task profile (general-purpose, compute-optimized, memory-optimized, GPU). By default, task pods can run on the system pool; configure a dedicated worker pool when you need to isolate them from system services, use spot capacity, or attach GPU instance types |
| Spot variant (optional) | Use your standard spot/preemptible nodepool taint convention (e.g., the Karpenter default `karpenter.sh/capacity-type=spot` or your organization's scheme). Workloads scheduled here must tolerate the taint and tolerate interruption |
| GPU pool (optional) | GPU instance class appropriate to your task workload (the GPU family — `g`/`p` on AWS, `n1`/`a2` on GCP — is what affects quota planning, not the specific generation) |

**Scale up when**:

- **Concurrent action volume crosses ~5,000** → raise worker `max_nodes` to 100 or beyond; diversify across multiple instance families to spread vCPU quota pressure (see [vCPU quotas](#vcpu-quotas)).
- **Concurrent action volume approaches the per-cluster ceiling** → review the [etcd ceiling](#etcd-ceiling) and other [scaling constraints](#scaling-constraints) and plan capacity accordingly.
- **GPU is the primary workload** → consider higher-memory GPU instance types; default to on-demand for production GPU pools — spot GPU capacity is unreliable.
- **Spot interruption rate causes failed actions** → configure on-demand fallback in Karpenter; diversify instance types per pool; pin production-critical pools to on-demand.

## Networking

Each cluster needs a VPC with private subnets for nodes, a NAT path for egress, and a Kubernetes pod/service IP allocation. Control plane and data plane have very different IP demand profiles, so the CIDR allocation strategy differs by plane. Separate-cluster deployments typically place CP and DP in different VPCs, optionally peered for private CP↔DP connectivity (otherwise DP→CP traffic flows through the CP's public ingress).

### Allocation strategy

- **Control plane: modest, steady-state.** CP runs a fixed set of services — ~50–200 pods total. A small VPC and pod CIDR is sufficient and easier to fit into an existing IP plan.
- **Data plane: greedy, burst-friendly.** DP pod-IP demand scales with peak workload, and pod-IP exhaustion is the most common scale blocker. Allocate large enough up front to absorb growth without recreating the VPC or cluster. CIDR resizing forces destructive operations on running clusters (nodepool recreation on GKE; VPC CIDR additions on AWS work but resizing existing subnets does not).

The defaults below are sized to support ~40,000 pods / ~9,000 nodes on AWS and the GCP-published per-cluster maxima (≤15,000 nodes, ≤250,000 pods).

### Control plane

CP-side IP demand is small. The CP cluster does not benefit from greedy allocation and can fit comfortably into a smaller VPC.

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

| Component | Setting |
| --- | --- |
| VPC CIDR | `/20` (4,096 IPs) is sufficient; use `/16` if you prefer symmetry with the DP VPC |
| Private subnets | 3× `/22` (one per AZ) — ample for the CP's pod footprint |
| Public subnets | 3× `/28` (one per AZ) — only the ingress endpoints live here |
| NAT gateways | 1 (cost-optimized) or per-AZ (production resilience) |
| VPC interface endpoints | none by default; required for SCP-restricted egress |

These CP defaults are starting points. If your organization has a standard VPC sizing, use it — the CP doesn't need anything larger.

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

| Component | Setting |
| --- | --- |
| VPC subnet (nodes) | `/22` (1,024 IPs) is sufficient for the CP node count |
| Pods secondary range | `/20` (4,096 IPs) — with `max_pods_per_node = 32` supports up to 32 nodes |
| Services secondary range | `/22` (1,024 IPs) |
| Master CIDR | `/28` (GCP requires exactly /28) |
| Cloud NAT | Dynamic Port Allocation enabled |

These CP defaults are starting points. If your organization has a standard VPC sizing, use it — the CP doesn't need anything larger.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Data plane

DP allocation is greedy by design. Pod-IP demand scales with peak workload, and CIDR changes on a running cluster are disruptive. Start with enough headroom to support 3 clusters worth of growth in the same VPC; add CIDR blocks (AWS) or larger secondary ranges (GCP) only if the workload outgrows the provisioned space.

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

Suggested defaults for a production-scale DP cluster:

| Component | Setting |
| --- | --- |
| VPC CIDR | `10.0.0.0/16` |
| Private subnets | 3× `/18` (`10.0.64.0/18`, `10.0.128.0/18`, `10.0.192.0/18`) — ~16,376 IPs per AZ, ~49,128 total |
| Public subnets | 3× `/28` (just the ingress endpoints) |
| NAT gateways | 1 per AZ for production resilience |
| VPC interface endpoints | none by default; add `ecr.api` / `ecr.dkr` / `logs` / `sts` / `s3` for SCP-restricted egress or to bypass NAT for system image pulls |

This sizing supports up to ~40,000 pods and ~9,000 nodes per VPC, with capacity for ~3 clusters running at typical size.

**When to add CIDR blocks**: if you provision more than ~3 DP clusters in one VPC, or a single DP cluster scales past 40,000 concurrent pods, add `10.1.0.0/16`, `10.2.0.0/16`, etc. as additional VPC CIDR blocks and provision new private subnets from them. The AWS VPC CNI does not require contiguous CIDRs.

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

Suggested defaults for a production-scale DP cluster:

| Component | Setting |
| --- | --- |
| VPC subnet (nodes) | `/19` (8,192 IPs) per cluster |
| Pods secondary range | `/19` (8,192 IPs) — with `max_pods_per_node = 32` supports 128 nodes per cluster |
| Services secondary range | `/20` (4,096 IPs) |
| Master CIDR | `/28` (GCP requires exactly /28) |
| Cloud NAT | Dynamic Port Allocation enabled |

The GCP-published per-cluster maxima are 15,000 nodes and 250,000 pods; if you expect a single cluster to scale beyond a few hundred nodes, enlarge the pods secondary range to `/14` (200,000 IPs) up front — changing the pod range on a running nodepool forces nodepool recreation.

GKE assigns each node a CIDR block sized to fit at least `2 × max_pods_per_node` IPs, rounded up to the next power-of-2 block (per [Google's published formula](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)). The [Pod density and IP allocation](#pod-density-and-ip-allocation) section under Scaling constraints has the per-node math and a pool-aware tuning strategy.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Scale up when

- **Cross-AZ availability required for production** → add a NAT gateway per AZ.
- **Pod egress restricted by Service Control Policies (AWS)** → add VPC interface endpoints for `ecr.api`, `ecr.dkr`, `logs`, `sts`, `s3` so workloads don't depend on internet egress.
- **High concurrent egress on Cloud NAT (GCP)** → ensure Dynamic Port Allocation is enabled (32–65,536 ports per VM). The legacy static 1,024-port default exhausts on connection-heavy workloads.

Specific networking-driven constraints — pod IP exhaustion, CoreDNS overload, conntrack saturation — are covered in [Scaling constraints](#scaling-constraints).

## Identity and workload binding

The cluster needs a managed identity mechanism so pods can call cloud APIs (object storage, secrets, registry) without static credentials. Separate-cluster deployments need identity bindings in **both** the CP cluster and the DP cluster, configured independently.

### Substrate

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

**Mechanism**: IAM Roles for Service Accounts (IRSA) on EKS.

The OIDC provider is per-cluster; configure it for each cluster you provision.

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

**Mechanism**: GKE Workload Identity Federation (WIF).

The WIF pool can be shared across clusters in the same project, with separate Kubernetes service-account → Google service-account bindings per cluster.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Control plane

CP service accounts shipped by the {{< key product_name >}} chart that need identity bindings:

- **flyteadmin / datacatalog / cacheservice** — read/write metadata bucket, talk to the database (when using IAM auth)
- **artifacts** — read/write artifacts bucket

Optional supporting services the customer may co-install also need identity bindings — configure these only if you deploy the service:

- **external-secrets** (optional) — read from the cloud secrets store. Skip if you use a different secret-injection mechanism.
- **external-dns** (optional) — manage DNS records for the ingress hostname. Skip if you manage DNS manually or through your own automation.
- **cert-manager** (optional) — issue certificates from a cloud-hosted ACME or PKI provider. Skip if you supply certificates by other means.

### Data plane

DP service accounts shipped by the {{< key product_name >}} chart that need identity bindings:

- **flytepropeller / executor / cluster-resource-sync** — read/write the DP metadata bucket, fetch credentials from the cloud secrets store, authenticate to the CP via OAuth2 client_credentials
- **task pods** (per-namespace KSAs) — read/write the artifacts bucket, fetch user-supplied secrets, pull task images
- **log pipeline** — see [Logging](#logging). On AWS, the {{< key product_name >}} fluentbit DaemonSet needs an IRSA binding to write to the configured destination. On GCP, GKE's managed Cloud Logging agent handles ingestion via the node service account; the DP backend GSA additionally needs `roles/logging.viewer` so the operator can read post-GC task logs back from the Cloud Logging API.

Optional supporting services follow the same pattern as on the CP — external-secrets, external-dns, and cert-manager need identity bindings only if you deploy them on the DP cluster.

#### GCP — Token Creator for signed URLs

On GCP, the DP backend service account additionally needs `roles/iam.serviceAccountTokenCreator` granted to the workload-identity principal of the `union-system` Kubernetes service account in the DP namespace. This lets the dataproxy code path call `signBlob` to mint signed URLs that users use to download task artifacts directly from GCS. The binding is a Workload Identity Federation principal grant rather than a standard service-account-to-service-account impersonation — the chart's docs and Terraform module references show the principal format. Without this binding, signed-URL generation fails and artifact download flows error out.

## Database

The control plane requires a managed PostgreSQL instance for metadata and state storage. The data plane does not connect to the database directly.

### Control plane

| Component | Default |
| --- | --- |
| Service | AWS RDS for PostgreSQL / GCP Cloud SQL for PostgreSQL |
| Version | PostgreSQL 12+ |
| Instance class | `db.t3.medium` (small) / `db.t3.large` (medium) / `db.r6g.xlarge` (large) |
| Storage | 100 GB gp3 to start, with autoscaling enabled |
| Authentication | Database-native (preferred) or IAM auth |
| Backup | Automated backups, 7-day retention minimum |

### Network connectivity

The CP cluster must reach the database instance privately. The plumbing differs by cloud:

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

- Provision RDS inside the CP VPC, in the **same private subnets** the cluster nodes attach to (or in subnets reachable via VPC peering from a separate database VPC).
- Attach a **security group** to the RDS instance that allows inbound TCP on the PostgreSQL port (5432 by default) **only from the CP cluster's node security group**. Do not expose RDS to the internet.
- The CP cluster reaches RDS via its private DNS hostname; resolve this within the VPC.

[Vendor docs: VPC and Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html).

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

- Allocate a **dedicated internal IP range** in the CP VPC for Google-managed services (typically `/22` or larger) and create a **private services access** peering with `servicenetworking.googleapis.com`.
- Provision Cloud SQL with a **private IP only** (no public IP), assigned from the allocated range. The Cloud SQL instance becomes reachable over the VPC peering connection.
- The CP cluster reaches Cloud SQL via the assigned private IP; the Cloud SQL Auth Proxy is not required when private IP is used.

[Vendor docs: Configure private services access](https://cloud.google.com/sql/docs/postgres/configure-private-services-access).

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

**Scale up when**:

- **Connection count approaches `max_connections`** → increase the parameter, or enable connection pooling (pgbouncer) in front of the database.
- **Storage IOPS saturate** → upgrade to provisioned IOPS or move to a larger instance class.
- **Query latency climbs across control plane services** → multiple CP services share the database (flyteadmin, datacatalog, cacheservice, identity, executions, artifacts). Review slow queries to identify the dominant query patterns and tune indexes accordingly. Read replicas can offload read-heavy workloads such as datacatalog.

## Object storage

Buckets for control-plane metadata, task artifact uploads, and fast-registration uploads. Workload identity must permit cluster pods to read/write the buckets.

### Substrate

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

| Bucket | Purpose | Notes |
| --- | --- | --- |
| `<org>-cp-metadata` | CP metadata + admin state | Versioning recommended |
| `<org>-cp-artifacts` | CP artifacts service | Versioning recommended |
| `<cluster>-dp-metadata` | DP metadata (per DP cluster) | |
| `<cluster>-dp-fast-registration` | Fast registration uploads | TTL recommended (delete after 7 days) |

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

| Bucket | Purpose | Notes |
| --- | --- | --- |
| `<org>-cp-metadata` | CP metadata + admin state | |
| `<org>-cp-artifacts` | CP artifacts service | |
| `<cluster>-dp-metadata` | DP metadata (per DP cluster) | |
| `<cluster>-dp-fast-registration` | Fast registration uploads | Lifecycle rule for cleanup |

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Control plane

CP-side buckets host metadata, artifact uploads, and signed-URL targets. Steady-state — bucket size grows with workflow definition count and cached task outputs.

### Data plane

DP-side buckets receive fast-registration uploads and task-output artifacts. Throughput scales with concurrent action count. Apply a TTL or lifecycle rule on fast-registration buckets to keep storage costs bounded.

## Secrets

The {{< key product_name >}} chart consumes **Kubernetes secrets** for OAuth client credentials, database passwords, registry pull credentials, and any user-supplied workflow secrets. How those secrets get into the cluster is your choice — the chart only cares that they exist at the expected names.

Common approaches:

- **Manual `kubectl create secret`** — appropriate for one-time or rarely-rotated values during install (registry pull secret, TLS cert).
- **Sync from a cloud secrets store** — using `external-secrets`, AWS Secrets Manager CSI driver, GCP Secret Manager CSI driver, Vault Agent, or similar. Convenient when secrets are rotated centrally and should propagate to the cluster automatically.
- **Sealed Secrets, SOPS, or another GitOps-friendly mechanism** — secrets committed to git in encrypted form, decrypted in-cluster.
- **Your existing internal secret-distribution tool**.

If you choose to sync from a cloud secrets store, the relevant managed service is AWS Secrets Manager, Google Secret Manager, or Azure Key Vault. Whichever operator you use will need an identity binding scoped to the secret IDs it reads — see [Identity and workload binding → Optional supporting services](#identity-and-workload-binding).

Both planes consume Kubernetes secrets identically. If you sync from a cloud secrets store in both clusters, the operator runs in each cluster with its own identity binding scoped to that cluster's secrets.

### Workflow secrets (`flyte.Secret`)

The `flyte.Secret(...)` API that user code references at task runtime resolves its values from a **configurable backing store**:

- **Default — Kubernetes secrets (in-cluster).** The data plane reads secret values from Kubernetes `Secret` objects in the task namespace. This is the simplest model and the default; it works with any of the population approaches above.
- **AWS Secrets Manager.** Configure the data plane to resolve `flyte.Secret` references directly against AWS Secrets Manager. The worker service account needs `secretsmanager:GetSecretValue` on the relevant secret ARNs.
- **GCP Secret Manager.** Configure the data plane to resolve `flyte.Secret` references directly against Google Secret Manager. The worker service account needs `roles/secretmanager.secretAccessor` on the relevant secrets.

The choice is independent of how the chart's own required secrets (DB password, OAuth credentials, registry credentials) are populated — those always read from Kubernetes `Secret` objects regardless of the workflow-secret backing store.

## Container image registry

A {{< key product_name >}} deployment pulls images from three categories of registries:

1. **{{< key product_name >}} system images** — the control plane and data plane components. Pulled from {{< key product_name >}}'s public registry (`public.ecr.aws/unionai/*` for AWS, mirrored to Google Artifact Registry for GCP tenants). Access requires a registry pull secret you create during install.
2. **Task images built by the {{< key product_name >}} image builder** — when users invoke the `flyte.Image` API, the image builder service writes resulting images into a registry **you provision** in your account. The DP then pulls task pods from this registry. The same registry doubles as the task-image registry for user-built images (see below).
3. **User-supplied task images** — if you build task images outside of `flyte.Image` (your existing CI/CD pipeline pushing to your own registry), the DP pulls from there. This can be the same registry as #2 or a different one.

The image-builder destination and the user-supplied task registry can be the same physical repository. The Terraform selfmanaged modules provision a dedicated Artifact Registry / ECR repo per data plane named `imagebuilder` (or similar) for the image builder's output.

### Substrate

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

- **Service**: Amazon ECR — at least one private repository for task images (the image builder's destination). [Vendor docs: Creating a private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html).
- **Auth**: the worker node IAM role grants `ecr:GetAuthorizationToken`, `ecr:Get*`, `ecr:BatchGet*` on the task-image repository so nodes can pull images. The image builder service additionally needs `ecr:Put*` and `ecr:CompleteLayerUpload` on the same repository so it can push built images.
- **{{< key product_name >}} system images**: pulled from `public.ecr.aws/unionai/*` via the registry pull secret created during install.

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

- **Service**: Google Artifact Registry — at least one Docker repository for task images (the image builder's destination). [Vendor docs: Create a repository](https://cloud.google.com/artifact-registry/docs/repositories/create-repos).
- **Auth**: the worker node service account grants `roles/artifactregistry.reader` for task-image pulls; the image builder service additionally needs `roles/artifactregistry.writer` on the same repository so it can push built images.
- **{{< key product_name >}} system images**: mirrored to a `union-public-images` Artifact Registry repository so GCP tenants avoid cross-cloud pulls. Grant the worker node service account `roles/artifactregistry.reader` on that mirror.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Data plane

The DP is where image-pull pressure shows up: rapid node scale-up means many pods pulling system images simultaneously. See [Image registry pull rate](#image-registry-pull-rate) under Scaling constraints.

## Logging

Task pod stdout/stderr needs to land in a backend the data plane's operator service can read from, so the {{< key product_name >}} console can display logs while a task runs **and** after its pod has been garbage-collected. The {{< key product_name >}} chart targets a different default backend on each cloud, matching what the underlying managed Kubernetes service provides natively:

- **AWS**: a {{< key product_name >}}-managed `fluentbit` DaemonSet runs on every DP worker node and writes container logs to a destination of your choice (DP metadata bucket by default; CloudWatch Logs as an alternative).
- **GCP**: GKE's managed Cloud Logging agent (Google's `fluentbit-gke` in `kube-system`) ships container logs to Cloud Logging automatically. The {{< key product_name >}} chart's optional fluentbit subchart is disabled by default on GCP — running it would duplicate ingestion. The operator reads post-GC task logs directly from the Cloud Logging API.

Either path supports the console's live and post-GC log-viewing flows; the on-cluster moving parts and IAM differ.

### Substrate

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

The {{< key product_name >}} chart installs a `fluentbit` DaemonSet on every DP worker node.

- **Default destination**: the DP metadata S3 bucket. Fluentbit writes log objects under a `persisted-logs/` prefix templated by namespace, pod, and container; lifecycle rules on the bucket control retention. The operator reads from this prefix when the console requests post-GC logs.
- **Alternative**: forward to CloudWatch Logs via the CloudWatch Container Insights add-on. EKS provides a `cloudwatch-observability` add-on that ships with its own IRSA role for the agent. [Vendor docs: CloudWatch Container Insights for EKS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS.html).

If you choose a non-default destination, grant the equivalent permissions to whichever service account the forwarder runs as.

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

GKE clusters created with the default logging configuration (`loggingConfig.componentConfig.enableComponents` includes `WORKLOADS`) ship container stdout/stderr to Cloud Logging via Google's managed `fluentbit-gke` DaemonSet in `kube-system`. No additional in-cluster agent is required. [Vendor docs: GKE logging](https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs).

The {{< key product_name >}} chart's optional fluentbit subchart is disabled by default on GCP — see `values.gcp.yaml`.

The operator queries Cloud Logging directly when streaming post-GC task logs to the console (filtering by `resource.labels.namespace_name`, `pod_name`, and `container_name`), and the v2 task-logs view includes a "GCP Logs" link that opens `console.cloud.google.com/logs/query` filtered to the task pod's labels.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### IAM bindings

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

A dedicated IRSA role grants the `fluentbit` Kubernetes service account the permissions required to write to the destination:

- **S3 destination** (default): `s3:PutObject` and `s3:GetObject` on the DP metadata bucket's `persisted-logs/` prefix.
- **CloudWatch Logs destination**: `logs:CreateLogStream` and `logs:PutLogEvents` on the relevant log group.

The {{< key product_name >}} Terraform selfmanaged modules provision this IRSA binding alongside the rest of the DP service accounts.

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

GKE's managed `fluentbit-gke` agent gets its IAM via the GKE node service account; no per-pod Workload Identity binding is needed for log ingestion.

For the operator to **read** post-GC task logs from Cloud Logging on behalf of the console, the DP backend service account needs `roles/logging.viewer` on the project. This is the same GSA that's bound to the `union-system` Kubernetes service account in the DP namespace via Workload Identity Federation.

The {{< key product_name >}} Terraform selfmanaged modules provision this binding alongside the rest of the DP service accounts.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Ingress and DNS

A TLS-terminating ingress fronting the control plane endpoint, plus DNS records mapping the deployment hostname to that ingress. In separate-cluster topology the CP ingress must be **public** (or at least reachable from the DP cluster) so the DP can authenticate and communicate.

The ingress is a two-layer stack: a cloud load balancer at the edge (L4 by default — passthrough TCP), with `ingress-nginx` inside the cluster doing L7 routing and TLS termination. L7 cloud load balancers (AWS ALB, GCP HTTP(S) LB) are supported alternatives but are not the default pattern; the L4 + `ingress-nginx` combination is what the chart targets out of the box and what mike-apple-gcp runs today (`type: LoadBalancer` service, TCP 80/443, GCP regional Network LB at the edge).

### Substrate

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

- **Edge load balancer**: AWS Network Load Balancer (L4) provisioned via the `type: LoadBalancer` service on `ingress-nginx`
- **L7 termination**: `ingress-nginx` does TLS termination and HTTP/2 routing in-cluster
- **TLS**: cert-manager + ACME (Let's Encrypt) for production CAs, your organization's CA, or self-signed for internal-trust deployments — see [Step 3 of Getting started](./getting-started#step-3-tls-certificates)
- **DNS**: Route 53 hosted zone; record creation handled by your DNS automation of choice

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

- **Edge load balancer**: GCP regional Network Load Balancer (L4, TCP passthrough) provisioned via the `type: LoadBalancer` service on `ingress-nginx`
- **L7 termination**: `ingress-nginx` does TLS termination and HTTP/2 routing in-cluster
- **TLS**: cert-manager + ACME, your organization's CA, or self-signed — see [Step 3 of Getting started](./getting-started#step-3-tls-certificates)
- **DNS**: Cloud DNS for hosted zones inside the GCP project. Cross-cloud strategies (e.g., Route 53 sub-delegating a subdomain to Cloud DNS via NS records) are supported but require coordinating the delegation

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

If you prefer an L7 cloud load balancer (AWS ALB, GCP HTTP(S) LB), you can swap the `ingress-nginx` `type: LoadBalancer` service for an Ingress resource backed by an ALB / GCLB controller. This trades the `ingress-nginx` L7 features (e.g., gRPC-specific routing tuning) for cloud-native L7 capabilities. Validate gRPC-over-HTTP/2 routing with your chosen controller before standardizing on it.

### Control plane

The CP ingress must be reachable from every DP cluster that connects to it. In separate-cluster topology this means a public DNS name with a real CA-signed certificate.

### Data plane

The DP cluster does not require its own public ingress — DP→CP traffic egresses through the DP cluster's NAT to reach the CP's public endpoint. A DP ingress is only needed if you expose user-facing services on the DP (e.g., dataproxy for serving artifact downloads).

## Scaling constraints

Most {{< key product_name >}} scaling pressure is on the data plane. These are the constraints — both infrastructure limits and configurable ceilings — that bind as DP workload grows. Each is independent; you can hit any of them before hitting any of the others.

### Pod density and IP allocation

The most common scale blocker. Each pod consumes a routable IP from the pod CIDR — and how the CIDR is allocated to nodes varies by cloud.

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

The VPC CNI assigns one IP per pod from the **node's subnet**. Completed/terminating pods retain their IPs until garbage-collected, so high-churn workloads compound subnet pressure.

**Default**: a `/20` private subnet (~4,000 IPs) supports a few hundred concurrent pods. Worker counts above ~500 generally need additional CIDR blocks on the VPC.

**Resolution**:
- Add CIDR blocks to the VPC (typically `/16` per block). New private subnets become available immediately.
- Enable VPC CNI **prefix delegation** — allocates `/28` prefixes (16 IPs) per ENI attachment instead of individual IPs.
- Reduce the pod GC timer for completed pods (default 24 h → 1 h) so IPs return to the pool faster.

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

GKE **preallocates** a CIDR block per node sized by `max_pods_per_node`. Per [Google's published formula](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr), the block is the smallest subnet that holds at least `2 × max_pods_per_node` IPs:

| `max_pods_per_node` (range) | Per-node block | IPs reserved |
| --- | --- | --- |
| 8 | /28 | 16 |
| 9–16 | /27 | 32 |
| 17–32 | /26 | 64 |
| 33–64 | /25 | 128 |
| 65–128 | /24 | 256 |
| 129–256 | /23 | 512 |

The Standard-cluster default of 110 falls in the 65–128 band, so every node consumes a `/24` (256 IPs). The cluster-wide node ceiling is `pods_cidr_size / per_node_block`:

| Pod CIDR | `max_pods_per_node` | Node ceiling |
| --- | --- | --- |
| `/19` (8,192 IPs) | 110 (default) | **32 nodes** |
| `/19` (8,192 IPs) | 32 (Google Autopilot value; this module's default) | 128 nodes |
| `/16` (65,536 IPs) | 32 | 1,024 nodes |
| `/14` (262,144 IPs) | 32 | 4,096 nodes |

Setting `max_pods_per_node = 32` yields a 4× headroom improvement over the Standard default while filling the `/26` block (no wasted IPs). The cluster-wide default can't be changed after cluster creation; changing a nodepool's pod range forces nodepool recreation.

#### Pool-aware tuning

`max_pods_per_node` is set per nodepool, not just cluster-wide. Picking the smallest power-of-2 band that comfortably fits each pool's realistic pod count maximizes total node count on a given pods CIDR — different pools have very different pod density profiles, and picking a single cluster-wide value over-allocates for the lightest pool.

| Pool | Realistic pod density | `max_pods_per_node` | Per-node block |
| --- | --- | --- | --- |
| System pool (operator, ingress-nginx, cert-manager, external-dns, external-secrets) | 10–20 fixed | **16** | /27 (32 IPs) |
| Worker pool (general task pods) | 5–20 typical, bursts to 30+ | **32** | /26 (64 IPs) |
| Dedicated monitoring (Prometheus, ClickHouse) | 10–15 stable | **16** | /27 (32 IPs) |
| GPU pool (1–8 GPUs/node, typically 1 pod/node) | 1–4 | **8** | /28 (16 IPs) |

Set the cluster-wide `max_pods_per_node` to match the worker pool (the heaviest user), then override per-nodepool for system / monitoring / GPU pools using GKE's per-nodepool `max-pods-per-node` flag. Combined with a `/14` pods CIDR, this lifts the practical node ceiling beyond what a single cluster-wide value can deliver.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### vCPU quotas

Cloud providers impose per-account, per-region vCPU limits **by instance family**. The most frequently hit limit in production.

**Detection**: node count plateaus at a round number while pending pods grow. Karpenter logs show `VcpuLimitExceeded` (AWS).

**Resolution**:

- Request quota increases proactively (1–5 business days). Pre-position quotas before workload ramps.
- Diversify instance families. AWS quotas are per-family — Standard `m`/`c`/`r`/`t` instances have separate quotas from GPU `g`/`p`. Configure Karpenter NodePools with multiple eligible instance types.
- On GCP, project-wide vCPU quotas behave similarly; raise via the Quotas page.

Quota plateaus repeat as workload scales — every time a new instance family is added or a new region is opened, expect to file a fresh quota request. Make pre-positioning quotas part of the capacity-planning cadence rather than a reactive response.

### Image registry pull rate

System images pulled from public registries (Public ECR) funnel through one or a few NAT gateway IPs. Rapid scale-up exposes this to per-IP rate limits.

**Detection**: `ImagePullBackOff` / `ErrImagePull` during rapid node scale-up, especially affecting system components (operator, propeller) after a rollout.

**Resolution**:

- **Configure ECR pull-through cache** in your private ECR pointing at `public.ecr.aws/unionai/*`. Subsequent pulls hit your private ECR (no rate limit).
- **Add VPC Interface Endpoints** for `ecr.api` and `ecr.dkr`. Endpoints route ECR traffic over the AWS backbone instead of through the NAT gateway.
- For GCP tenants, system images are already mirrored to GAR to avoid cross-cloud rate limits.

### CoreDNS and conntrack

- **Worker count crosses ~1,000 nodes** → CoreDNS overload becomes likely.
  - Spread CoreDNS via pod anti-affinity.
  - Scale CoreDNS replicas (start with 8, grow to 24+ at scale).
  - Move CoreDNS to a dedicated nodepool isolated from worker churn.
  - Deploy **NodeLocal DNS Cache** as a DaemonSet. Note: if a node's nodelocaldns pod dies, all pods on that node lose DNS until restored.

- **Conntrack utilization > 50% on any worker node** → NIC connection-tracking table saturating. Use larger instance types — small and burstable instance families (AWS `t`-series and equivalents) have very limited conntrack tables.

- **GCP Cloud NAT reports `OUT_OF_RESOURCES`** → static port-per-VM allocation exhausted. Confirm Dynamic Port Allocation is enabled (32–65,536 ports per VM).

### Ephemeral disk

Worker nodes commonly attach large persistent disks for task ephemeral storage. Aggregate disk demand can hit regional cloud-provider quotas before vCPU does.

- **AWS regional gp3 quota** (`L-7A658B76`, 50 TiB default). Aggregate EBS demand can hit this ceiling at modest node counts when per-node disks are provisioned generously — e.g., 2 TiB per worker means ~25 nodes consume the full regional quota.
  - Reduce per-node EBS volume size.
  - Request a gp3 quota increase.
  - Where the instance family supports it, prefer NVMe instance store over EBS for task scratch.

### etcd ceiling

Managed Kubernetes' etcd has a hard storage ceiling that {{< key product_name >}} workloads hit before most other limits, because high action churn generates many short-lived Kubernetes objects (pods, events, CRDs).

| Tier | etcd size | etcd objects | Notes |
| --- | --- | --- | --- |
| Healthy | < 4 GB | < 200K | |
| Warning | 4–6 GB | 200K–500K | Investigate object churn and prune what you can |
| Critical | > 6 GB | > 500K | Imminent risk; defer non-essential runs |
| Hard limit (EKS) | ~8 GB | ~1M (perf degrades) | New runs rejected |

**Detection**: monitor `apiserver_storage_size_bytes` and `apiserver_storage_objects:total`. Alert at 6 GB / 500K.

**Resolution at the hard limit**:

- {{< key product_name >}} pauses accepting new runs at the safety threshold (~7 GB) to avoid cluster brickage.
- **EKS Ultra clusters** offer 16 GB etcd at additional cost — doubles the per-cluster ceiling.
- Engage cloud-provider support to investigate object churn and identify what is dominating etcd storage.

### Spot capacity

Spot/preemptible nodes can be reclaimed at any time; spot capacity for GPU instance types is particularly unreliable.

**Resolution**:

- Configure on-demand fallback in Karpenter.
- Diversify instance types per pool to maximize spot availability.
- Pin production-critical pools and GPU workloads to on-demand.

### Queue and executor action limits

V2 execution has a chain of configurable limits. The most common binding constraint is the data plane's executor: each active action holds a Watch connection to the queue service, so the executor caps how many actions can be in flight at once. Above that, the control-plane queue service applies global and per-run caps.

The exact configuration keys, defaults, and override paths live in the chart's `values.yaml` files and may shift between releases. Refer to the published chart sources for the current settings:

- **Data plane executor**: [`charts/dataplane/values.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/dataplane/values.yaml) — search for `executor`.
- **Control plane queue service**: [`charts/controlplane/values.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.yaml) — search for `queue` and related action-limit keys.

**Resolution**:

- Raise the data plane executor's action limit to match expected concurrency. Higher gives more throughput at the cost of more queue-service Watch connections.
- Cap the control plane's scheduled-run ceiling to keep workload bursts predictable. Self-hosted runs single-tenant; any "per-organization" naming in the chart config caps your single org.
- Monitor queue-service health and tune it vertically (CPU/memory limits) if the queue service itself becomes the bottleneck — it is single-replica.

## Intra-cluster topology

Intra-cluster — both planes in the same Kubernetes cluster — is a supported special case. It is the topology the [Getting started](./getting-started) walkthrough uses because it has the simplest substrate footprint (one cluster, one VPC, one set of identity bindings) and the chart ships ready-to-use `values.{aws,gcp}.selfhosted-intracluster.yaml` overlays for it.

### When to use

- **Lab and evaluation environments** where minimizing footprint matters more than isolation.
- **Footprint-constrained production deployments** (regulated air-gapped environments, single-account/single-region constraints) where the operational simplicity of one cluster outweighs the isolation benefits of two.
- **Initial proof-of-concept** before scaling to separate-cluster.

### What changes from separate-cluster

| Aspect | Separate-cluster | Intra-cluster |
| --- | --- | --- |
| Clusters | 2 (CP + DP) | 1 |
| Networking | DP→CP through CP's public ingress | DP→CP over internal `svc.cluster.local` DNS |
| CP ingress | Public, real CA cert recommended | ClusterIP, self-signed acceptable |
| Identity bindings | Two clusters, two OIDC providers (AWS) | One cluster, one OIDC provider |
| Object storage | Separate CP and DP buckets | Same buckets work for both |
| Helm overlay | `values.{aws,gcp}.yaml` (cloud default) | `values.{aws,gcp}.selfhosted-intracluster.yaml` |
| etcd headroom | Two etcds, each scales independently | One etcd serving both planes — DP workload pressure also affects CP responsiveness |

### Scaling considerations specific to intra-cluster

- **Shared etcd**: CP and DP share one Kubernetes control plane's etcd. The data plane drives churn-heavy object creation (action pods, events); the control plane shares whatever headroom is left. The [etcd ceiling](#etcd-ceiling) applies to the combined footprint.
- **Shared node pools**: by default the cluster has one system pool and one worker pool. CP services schedule onto the system pool; task pods onto the worker pool. Make sure the system pool can host the full CP footprint (admin, identity, queue, ScyllaDB, monitoring, ingress) with headroom.
- **Migration path**: when the DP outgrows the cluster's etcd or compute capacity, migrate to separate-cluster topology.

### Reference

The chart's bundled intra-cluster overlays are self-contained and document every override in the file's comment header:

- AWS: [`values.aws.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.aws.selfhosted-intracluster.yaml)
- GCP: [`values.gcp.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.gcp.selfhosted-intracluster.yaml)

## Next

- [Getting started](./getting-started) — end-to-end installation walkthrough (intra-cluster).
- [Authentication](./authentication) — configure OIDC/OAuth2.
- [Operations → Troubleshooting](./operations/troubleshooting) — runtime issues.

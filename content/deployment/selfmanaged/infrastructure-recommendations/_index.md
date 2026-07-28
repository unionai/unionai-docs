---
title: Infrastructure recommendations
weight: 2
variants: -flyte +union
sidebar_expanded: true
---

# Infrastructure recommendations

In a self-managed deployment, {{< key product_name >}} runs the **control plane** and you
run the **data plane** on your own Kubernetes cluster. This page covers the infrastructure
**you** provision for the data plane: a Kubernetes cluster, a VPC, object storage, a
managed identity binding, a container image registry, and egress to the
{{< key product_name >}}-hosted control plane. Nothing here is {{< key product_name >}}-specific
infrastructure — it is your cloud account's standard infrastructure wired up to run
{{< key product_name >}} task workloads.

{{< key product_name >}} is capable of running on any Kubernetes cluster — managed services
such as GKE, AKS, and EKS, as well as self-managed clusters. The recommendations below
ensure the best performance and reliability of your data plane.

> [!NOTE] What {{< key product_name >}} runs vs. what you run
> The **control plane** (admin, identity, queue service, database, control-plane object
> storage) is hosted and operated by {{< key product_name >}} — you do not provision any of it.
> Your responsibility is the **data plane**: the cluster that runs the operator, executor,
> and your task pods. Deployments where you also run the control plane are a separate,
> self-hosted model and are out of scope for this page.

## Sizing model

The data plane is **peak-driven**. Its footprint tracks the maximum concurrent execution
load: actions running, nodes provisioned, pods per node, IPs consumed, NIC and disk
throughput. Size it for workload bursts, not average load — and note that the constraints
stack: every limit (vCPU quota, pod-IP allocation, conntrack table, etcd object count,
registry pull rate) bites independently as workload grows. See
[Scaling constraints](./scaling-constraints) for the per-cluster ceilings to plan around.

### Workload signals → size mapping

Use these signals to pick a starting point. They describe data-plane load only; the
control plane that {{< key product_name >}} operates scales independently.

| Signal | Small | Medium | Large |
| --- | --- | --- | --- |
| Concurrent running actions | ≤500 | 500–5,000 | 5,000–30,000+ |
| Peak worker nodes | ≤25 | 25–250 | 250–3,000+ |
| Peak vCPU consumption | ≤500 | 500–10,000 | 10,000–90,000 |

## Pre-installation checklist

Provision the following in your cloud account before installing the
{{< key product_name >}} data plane Helm chart. Each item links to the section that covers it
in detail; the concrete `aws` / `gcloud` / `az` commands live on the per-cloud
[cloud provider setup](#cloud-provider-setup) pages.

1. **VPC and subnets** — private subnets for worker nodes, sized for peak pod-IP demand.
   See [Networking](#networking).
2. **NAT egress** — outbound path so worker nodes reach public registries **and the
   {{< key product_name >}} control-plane endpoint**. See [Networking](#networking) and
   [Control-plane connectivity](#control-plane-connectivity).
3. **Kubernetes cluster** — managed control plane (EKS / GKE / AKS) plus a system node pool
   and worker pool(s). See [Kubernetes cluster](#kubernetes-cluster).
4. **Workload identity foundation** — IRSA OIDC provider (AWS) or Workload Identity
   Federation (GCP), so the `union-system` service account can call cloud APIs without
   static credentials. See [Identity and workload binding](#identity-and-workload-binding).
5. **Object storage buckets** — metadata bucket and fast-registration bucket. See
   [Object storage](#object-storage).
6. **Container image registry** — a private registry for task images (the image builder
   writes here; nodes pull from here), plus credentials to pull {{< key product_name >}}
   system images. See [Container image registry](#container-image-registry).
7. **Service-account IAM bindings** — bind the `union-system` identity to the buckets and
   registry above. See [Identity and workload binding](#identity-and-workload-binding).
8. **Logging backend** (optional to change) — where task-pod stdout/stderr is collected for
   the console's live and post-GC log views. See [Logging](#logging).

After this list is complete, follow the per-cloud [cloud provider setup](#cloud-provider-setup)
page for the creation commands, then deploy the data plane.

## Kubernetes cluster

A managed Kubernetes cluster (EKS, GKE, or AKS) or a conformant self-managed cluster, sized
for peak workload.

### Kubernetes versions

Run a version that is [actively supported by the Kubernetes community](https://kubernetes.io/releases/)
— typically one of the three most recent minor versions. For example, if the latest is
1.33, run 1.33, 1.32, or 1.31.

### Node pools

Use separate node pools for {{< key product_name >}} system services and for worker (task)
pods. This guards against resource contention between the platform and your workloads. See
[Configuring node pools](../configuration/node-pools) for details.

| Pool | Purpose | Notes |
| --- | --- | --- |
| System pool | Hosts the operator (agent), ingress proxy, and executor | 3 nodes, general-purpose on-demand, ~4 vCPU / 16 GB minimum per node. **Avoid burstable `t`-series types** — their conntrack-table and CPU-credit limits cause unpredictable failures under sustained load. |
| Worker pool | Runs user task pods | **No strict requirements** — pick instance family, size, disk, and autoscaling bounds for your task profile. By default task pods can run on the system pool; add a dedicated worker pool to isolate them, use spot capacity, or attach GPUs. |
| Spot (optional) | Interruptible task capacity | Workloads must tolerate the spot taint and interruption. Configure on-demand fallback for production. |
| GPU (optional) | GPU task pods | The GPU family (`g`/`p` on AWS, `n1`/`a2` on GCP) is what drives quota planning. Default production GPU pools to on-demand — spot GPU capacity is unreliable. |

By default the {{< key product_name >}} data plane requests the following resources for its
system components (excludes user task pods):

|          | CPU (vCPUs) | Memory (GiB) |
|----------|-------------|--------------|
| Requests | 14          | 27.1         |
| Limits   | 17          | 32           |

For GPU access, {{< key product_name >}} injects tolerations and label selectors onto
execution pods. {{< key product_name >}} supports cluster autoscaling and spot/interruptible
instances.

**Scale up when**:

- **Concurrent action volume crosses ~5,000** → raise worker `max_nodes` to 100+ and
  diversify across instance families to spread vCPU-quota pressure (see
  [vCPU quotas](./scaling-constraints#vcpu-quotas)).
- **Concurrent action volume approaches the per-cluster ceiling** → review the
  [etcd ceiling](./scaling-constraints#etcd-ceiling) and other
  [scaling constraints](./scaling-constraints) and plan capacity accordingly.

## Networking

The cluster needs a VPC with private subnets for nodes, a NAT path for egress, and a
Kubernetes pod/service IP allocation. Data-plane pod-IP demand scales with peak workload,
and **pod-IP exhaustion is the single most common scale blocker** — so allocate greedily up
front. CIDR resizing on a running cluster is destructive (nodepool recreation on GKE; on
AWS you can add VPC CIDR blocks but cannot resize existing subnets).

### VPC and subnet sizing

Allocate large enough up front to absorb growth without recreating the VPC or cluster. As a
rule of thumb, plan for **at least one available pod IP per concurrent task**, plus headroom.
Data-plane pod-IP demand is greedy — size the private/pod ranges for peak concurrent pods and
prefer a large range up front, since CIDR changes on a running cluster are disruptive
(nodepool recreation on GKE; on AWS you can add VPC CIDR blocks but not resize existing
subnets).

The concrete CIDR defaults and the per-node IP-allocation model are cloud-specific. See your
cloud's infrastructure page for suggested sizes and the pod-density math:

| Cloud | Networking and capacity guidance |
| --- | --- |
| AWS | [Prepare infrastructure (AWS) → Networking and IP capacity](./aws#networking-and-ip-capacity) |
| GCP | [Prepare infrastructure (GCP) → Networking and IP capacity](./gcp#networking-and-ip-capacity) |
| Azure / OCI / other | Pod IPs come from your VNet/VPC subnets (Azure CNI, Calico, Cilium). Size the node subnet for peak concurrent pods and prefer a large private range up front; if the CNI has a fixed per-node pod cap, the same [pod-density math](./scaling-constraints#pod-density-and-ip-allocation) applies. |

### Public vs. private subnets

Run worker nodes in **private subnets** (no direct internet ingress) — the default for EKS,
GKE, and AKS. Public subnets are only needed for internet-facing load balancers, NAT
gateways, or bastion hosts.

```
VPC (/16)
├── Public subnet  (/24) — NAT gateway, load balancers
└── Private subnet (/18) — worker nodes, pods
```

### NAT gateway requirements

Worker nodes in private subnets need outbound access to pull container images from public
registries (Docker Hub, ECR Public, `ghcr.io`) **and to reach the
{{< key product_name >}}-hosted control plane** (see
[Control-plane connectivity](#control-plane-connectivity)). This requires a NAT gateway (or
equivalent) with an egress path from each AZ.

| Cloud | Service | Notes |
|-------|---------|-------|
| AWS | [NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) | One per AZ for HA. `eksctl --managed` creates these automatically. |
| GCP | [Cloud NAT](https://cloud.google.com/nat/docs/overview) | Attach to the Cloud Router. Enable **Dynamic Port Allocation** — the static 1,024-port default exhausts on connection-heavy workloads. |
| Azure | [NAT Gateway](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview) | Associate with the AKS subnet, or use `outboundType: loadBalancer` (default). |

> [!NOTE] Fully private clusters
> If your cluster has no outbound internet access, configure private endpoints or mirrors
> for all container registries and for the {{< key product_name >}} control-plane endpoint.

## Identity and workload binding

The cluster needs a managed identity mechanism so pods can call cloud APIs (object storage,
image registry, secrets) without static credentials. The {{< key product_name >}} data plane
uses a **single Kubernetes service account, `union-system`**, shared by all platform
components (operator, executor, webhook, proxy, and FluentBit), and the same identity is
assumed by task pods across per-project namespaces.

| Cloud | Mechanism |
| --- | --- |
| AWS | IAM Roles for Service Accounts (IRSA) — per-cluster OIDC provider |
| GCP | GKE Workload Identity Federation (WIF) |
| Azure | Microsoft Entra Workload Identity |

The `union-system` identity needs:

- **Object storage** (S3 / GCS / Azure Blob) — read/write the metadata and fast-registration
  buckets (task inputs/outputs, bundled code).
- **Container registry** (ECR / Artifact Registry / ACR) — pull task images; push images when
  the [image builder](../configuration/image-builder) is enabled.

The concrete IAM policy, role, and service-account annotation for each cloud live on the
per-cloud [cloud provider setup](#cloud-provider-setup) pages. Review the
[common pitfalls](#common-identity-pitfalls) below before you write those bindings.

> [!NOTE] Common service account
> Earlier versions gave each component its own service account. The consolidated
> `union-system` service account simplifies IAM: you bind cloud permissions to a single
> identity.

### Common identity pitfalls

**GCP — `objectAdmin` alone is insufficient.** Several {{< key product_name >}} services use
the stow GCS driver, which calls `storage.buckets.get` on startup to introspect the bucket.
`roles/storage.objectAdmin` covers object read/write but **not** the bucket-metadata
permission. Symptom: pods crash-loop with `Error 403: does not have storage.buckets.get
access`. Fix: also grant `roles/storage.bucketViewer`, or use `roles/storage.admin` (which
includes both).

**GCP — the node service account needs Artifact Registry reader, independent of the pod's
binding.** Kubelet pulls task images using the **node's** identity, not the pod's Workload
Identity binding. If only the pod's GSA has `artifactregistry.reader`, task pods
impersonate the GSA fine at runtime but fail `ErrImagePull` with `403 Forbidden` on the
image-pull token request. Fix: grant the GKE node SA `roles/artifactregistry.reader` on the
repository.

**AWS — same kubelet pattern via the node IAM role.** EKS image pulls use the node's
instance-profile IAM role. Grant the ECR repository policy to the node role (or use ECR
pull-through cache via the node's default ECR auth).

**GCP service-account ID length.** GCP service-account IDs are 6–30 characters. If you
compose names like `<org>-<cluster>-<service>` and the result exceeds 30 chars, the GCP API
rejects creation. Shorten the org or cluster name.

## Object storage

Each data plane uses object-storage buckets for workflow execution data. Workload identity
must permit cluster pods to read/write them.

| Bucket | Purpose | Notes |
| --- | --- | --- |
| Metadata bucket | Workflow execution data — task inputs/outputs, node state | Versioning recommended |
| Fast-registration bucket | Local code artifacts copied into the task container at runtime (`flyte deploy`, `flyte run --copy-style all`) | Apply a TTL / lifecycle rule (e.g. delete after 7 days) to bound cost |

You can use a single bucket for both, but two is recommended so you can apply different
retention policies. Throughput scales with concurrent action count. See
[Data retention](../configuration/data-retention) for lifecycle-policy guidance, and the
per-cloud pages for CORS configuration (required for the
[Code Viewer](../configuration/code-viewer)).

## Container image registry

A {{< key product_name >}} data plane pulls images from three categories of registry:

1. **{{< key product_name >}} system images** — the data-plane components (operator,
   executor, proxy). Pulled from {{< key product_name >}}'s registry; access requires a pull
   secret you create at install time.
2. **Task images built by the image builder** — when users invoke the `flyte.Image` API, the
   [image builder](../configuration/image-builder) writes images into a registry **you
   provision** in your account, and the data plane pulls task pods from it.
3. **User-supplied task images** — images built by your own CI/CD pushing to your registry.
   This can be the same registry as #2 or a different one.

Provide at least one private repository (ECR / Artifact Registry / ACR) for #2 and #3, plus
the pull secret for #1. Image-pull pressure shows up on the data plane during rapid node
scale-up (many pods pulling simultaneously) — see
[Image registry pull rate](./scaling-constraints#image-registry-pull-rate).

## Logging

Task-pod stdout/stderr needs to land in a backend the operator can read, so the console can
display logs **while a task runs and after its pod is garbage-collected**. The default
backend differs by cloud:

- **AWS**: a {{< key product_name >}}-managed FluentBit DaemonSet writes container logs to
  the metadata bucket (default) or CloudWatch Logs.
- **GCP**: GKE's managed Cloud Logging agent ships logs automatically; the operator reads
  post-GC logs from the Cloud Logging API. The FluentBit subchart is disabled by default to
  avoid duplicate ingestion.

See [Persistent logs](../configuration/persistent-logs) for configuration.

## Secrets

The {{< key product_name >}} chart consumes **Kubernetes secrets** for registry pull
credentials, the control-plane OAuth client credential, and user-supplied workflow secrets.
How those secrets get into the cluster is your choice — manual `kubectl create secret`,
`external-secrets` / a cloud secrets-store CSI driver, Sealed Secrets / SOPS, or your own
tooling. The `flyte.Secret(...)` API that user code references at runtime resolves from a
configurable backing store (Kubernetes secrets by default, or a cloud secrets manager). See
[Union secrets](../configuration/union-secrets).

## Control-plane connectivity

Unlike a self-hosted deployment, the data plane authenticates to and communicates with a
**remote, {{< key product_name >}}-hosted control plane** over the internet. Ensure:

- **Egress** from worker nodes (via NAT) can reach the {{< key product_name >}}
  control-plane endpoint (`*.unionai.cloud`) in addition to your container registries.
  Connectivity is **outbound-only** over gRPC-over-TLS (**TCP 443**) and, under the default
  tier, the Cloudflare Tunnel (**TCP 7844**); no inbound firewall rules are required. For the
  full list of outbound destinations and ports, and guidance on allowlisting by IP address,
  see [Egress requirements](../../../security/architecture/network#egress-requirements).
- The operator authenticates to the control plane using an **OAuth2 client-credentials
  ("eager") key**, supplied as a Kubernetes secret. See
  [Authentication](../configuration/authentication).
- If you run **multiple data-plane clusters** under one {{< key product_name >}} control
  plane, each cluster registers independently — see [Multi-cluster](../configuration/multi-cluster).

## Cloud provider setup

Each page below covers the concrete resource-creation commands and the data-plane Helm values
for one provider — the cloud-specific realization of the requirements on this page. Pick yours
after working through the requirements above, then follow [Deploy the data plane](../deploy/_index).

- [AWS](./aws)
- [GCP](./gcp)
- [Azure](./azure)
- [OCI](./oci)
- [Generic Kubernetes](./generic) (on-premise or any S3-compatible environment)
- [CoreWeave](./coreweave)
- [Crusoe](./crusoe)
- [Nebius](./nebius)

## Next

- Pick your [cloud provider](#cloud-provider-setup) and provision its resources.
- [Deploy the data plane](../deploy/_index) — install the operator once your infrastructure is ready.
- [Scaling constraints](./scaling-constraints) — the per-cluster ceilings to plan around as
  data-plane workload grows.

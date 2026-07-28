---
title: Scaling constraints
weight: 9
variants: -flyte +union
---

# Scaling constraints

As data-plane workload grows, a series of independent limits — some infrastructure ceilings,
some configurable — bind one at a time. You can hit any of them before hitting any of the
others, so plan for all of them. This page enumerates the constraints in roughly the order
they tend to bite, with detection signals and resolutions for each.

These are all data-plane concerns. The control plane is operated by
{{< key product_name >}} and scales independently; see
[Infrastructure recommendations](./_index) for the data-plane sizing model.

## Pod density and IP allocation

The most common scale blocker. Each pod consumes a routable IP, and the pool drains fastest
on the data plane during workload bursts. How the pod CIDR is allocated to nodes — and
therefore what runs out first — differs by cloud:

- **AWS (VPC CNI)** assigns one IP per pod from the node's subnet; completed/terminating pods
  hold their IPs until garbage-collected. Relief comes from adding VPC CIDR blocks, enabling
  prefix delegation, and shortening the pod-GC timer.
- **GKE** preallocates a per-node CIDR block sized by `max_pods_per_node`, which caps the
  cluster's node count for a given pod range. Tuning `max_pods_per_node` per nodepool is the
  primary lever.

The concrete per-node math, sizing tables, and tuning strategy live on the cloud-specific
infrastructure pages:
[AWS → Networking and IP capacity](./aws#networking-and-ip-capacity) ·
[GCP → Networking and IP capacity](./gcp#networking-and-ip-capacity).

## vCPU quotas

Cloud providers impose per-account, per-region vCPU limits **by instance family**. The most
frequently hit limit in production.

**Detection**: node count plateaus at a round number while pending pods grow. Karpenter logs
show `VcpuLimitExceeded` (AWS).

**Resolution**:

- Request quota increases proactively (1–5 business days). Pre-position quotas before
  workload ramps.
- Diversify instance families. AWS quotas are per-family — Standard `m`/`c`/`r`/`t`
  instances have separate quotas from GPU `g`/`p`. Configure Karpenter NodePools (or your
  autoscaler) with multiple eligible instance types.
- On GCP, project-wide vCPU quotas behave similarly; raise via the Quotas page.

Quota plateaus repeat as workload scales — every time you add an instance family or open a
new region, expect a fresh quota request. Make pre-positioning quotas part of the
capacity-planning cadence rather than a reactive response.

## Image registry pull rate

System images pulled from public registries funnel through one or a few NAT-gateway IPs.
Rapid scale-up exposes this to per-IP rate limits.

**Detection**: `ImagePullBackOff` / `ErrImagePull` during rapid node scale-up, especially
affecting system components (operator, executor) after a rollout.

**Resolution**:

- **Configure ECR pull-through cache** (AWS) in your private ECR pointing at the public
  source. Subsequent pulls hit your private ECR (no rate limit).
- **Add VPC interface endpoints** for `ecr.api` and `ecr.dkr` so ECR traffic routes over the
  AWS backbone instead of through the NAT gateway.
- Mirror {{< key product_name >}} system images and frequently-used base images into a
  registry inside your own account/region to avoid cross-network pulls.

## CoreDNS and conntrack

- **Worker count crosses ~1,000 nodes** → CoreDNS overload becomes likely.
  - Spread CoreDNS via pod anti-affinity.
  - Scale CoreDNS replicas (start with 8, grow to 24+ at scale).
  - Move CoreDNS to a dedicated nodepool isolated from worker churn.
  - Deploy **NodeLocal DNS Cache** as a DaemonSet. Note: if a node's nodelocaldns pod dies,
    all pods on that node lose DNS until it's restored.

- **Conntrack utilization > 50% on any worker node** → the NIC connection-tracking table is
  saturating. Use larger instance types — small and burstable families (AWS `t`-series and
  equivalents) have very limited conntrack tables.

- **GCP Cloud NAT reports `OUT_OF_RESOURCES`** → static port-per-VM allocation exhausted.
  Confirm Dynamic Port Allocation is enabled (32–65,536 ports per VM).

## Ephemeral disk

Worker nodes commonly attach large persistent disks for task ephemeral storage. Aggregate
disk demand can hit regional cloud-provider quotas before vCPU does.

- **AWS regional gp3 quota** (`L-7A658B76`, 50 TiB default). Aggregate EBS demand can hit
  this ceiling at modest node counts when per-node disks are provisioned generously — e.g.,
  2 TiB per worker means ~25 nodes consume the full regional quota.
  - Reduce per-node EBS volume size.
  - Request a gp3 quota increase.
  - Where the instance family supports it, prefer NVMe instance store over EBS for task
    scratch.

## etcd ceiling

Managed Kubernetes' etcd has a hard storage ceiling that {{< key product_name >}} workloads
can hit before most other limits, because high action churn generates many short-lived
Kubernetes objects (pods, events, CRDs).

| Tier | etcd size | etcd objects | Notes |
| --- | --- | --- | --- |
| Healthy | < 4 GB | < 200K | |
| Warning | 4–6 GB | 200K–500K | Investigate object churn and prune what you can |
| Critical | > 6 GB | > 500K | Imminent risk; defer non-essential runs |
| Hard limit (EKS) | ~8 GB | ~1M (perf degrades) | New runs rejected |

**Detection**: monitor `apiserver_storage_size_bytes` and `apiserver_storage_objects:total`.
Alert at 6 GB / 500K.

**Resolution at the hard limit**:

- {{< key product_name >}} pauses accepting new runs at the safety threshold (~7 GB) to avoid
  cluster brickage.
- **EKS Ultra clusters** offer 16 GB etcd at additional cost — doubles the per-cluster
  ceiling.
- Engage cloud-provider support to investigate object churn and identify what is dominating
  etcd storage.

## Spot capacity

Spot/preemptible nodes can be reclaimed at any time; spot capacity for GPU instance types is
particularly unreliable.

**Resolution**:

- Configure on-demand fallback in your autoscaler (e.g. Karpenter).
- Diversify instance types per pool to maximize spot availability.
- Pin production-critical pools and GPU workloads to on-demand.

## Queue and executor action limits

V2 execution has a chain of configurable limits. The most common binding constraint is the
data plane's **executor**: each active action holds a Watch connection to the control-plane
queue service, so the executor caps how many actions can be in flight at once.

The exact configuration keys, defaults, and override paths live in the chart's `values.yaml`
and may shift between releases. Refer to the published chart sources for current settings:

- **Data plane executor**: [`charts/dataplane/values.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/dataplane/values.yaml)
  — search for `executor`.

**Resolution**:

- Raise the executor's action limit to match expected concurrency. Higher gives more
  throughput at the cost of more queue-service Watch connections.
- Monitor executor health and tune it vertically (CPU/memory limits) if it becomes the
  bottleneck.

## Related

- [Infrastructure recommendations](./_index) — the data-plane sizing model and resource taxonomy.
- [Monitoring](../configuration/monitoring) — dashboards and alerts, including etcd and
  CoreDNS metrics.
- [Node pools](../configuration/node-pools) — configuring system, worker, spot, and GPU pools.

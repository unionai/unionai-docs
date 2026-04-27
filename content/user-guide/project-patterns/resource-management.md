---
title: Resource management and multi-team scaling
weight: 4
variants: -flyte +union
---

# Resource management and multi-team scaling

This guide covers the foundational primitives Union provides for multi-tenancy — projects, domains, quotas, task-level resources, RBAC, and secrets — and the patterns that work best as you scale to multiple teams. It also outlines what's changing in the v2 quota model so you can plan accordingly.

Teams that set these up well early avoid most of the noisy-neighbor, cache-bleed, and resource-starvation problems that surface later.

## Project-domain structure

The combination of **project × domain** is Union's atomic unit of isolation. Each pair gets its own Kubernetes namespace, its own quotas, its own RBAC, and its own secrets.

### One project per team or ML product

Every independent team or ML product should have its own Union project. Projects are isolated from one another by default, though you can reference workflows or tasks across projects to reuse generalizable resources.

The tradeoff worth flagging: cross-project task reuse is possible, but it requires advance coordination and shared coding standards. Don't reach for it casually — the coupling it creates is easy to underestimate.

### Domains are environments, not teams

Domains are orthogonal to projects. They represent distinct environments — typically development, staging, and production — and enable dedicated configurations, permissions, secrets, cached execution history, and resource allocations for each environment.

A production domain in particular ensures a clean slate, so cached executions from development don't produce unexpected behavior in production runs.

## Resource quotas

### Set quotas per project-domain pair

Quotas should be configured for each project-domain pair, not globally. This ensures workflows can't exceed designated limits and prevents any single project or domain from impacting resources available to others.

Configure via `uctl` with a YAML attribute file:

```yaml
domain: development
project: team-alpha
attributes:
  projectQuotaCpu: "500"
  projectQuotaMemory: 2Ti
```

Apply it with:

```bash
uctl update cluster-resource-attribute --attrFile cra.yaml
```

Verify with:

```bash
uctl get cluster-resource-attribute -p <project> -d <domain>
```

### GPU quotas need explicit setup

`projectQuotaGpu` exists in Union BYOC but is not in Flyte OSS. If any team runs GPU workloads, work with Union to set GPU quotas explicitly.

Without GPU quotas, you risk starvation across teams: Propeller won't queue executions, it dispatches them to Kubernetes immediately, and pods then sit pending while the execution shows as "running."

## Task-level resources

### Always declare explicit requests and limits

Pass a `(request, limit)` tuple to `flyte.Resources` for each resource dimension you want to bound:

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    resources=flyte.Resources(cpu=("4", "8"), memory=("16Gi", "32Gi")),
)

@env.task
def my_task():
    ...
```

If you attempt to execute a workflow with unsatisfiable resource requests, the execution fails immediately rather than queueing forever. This fail-fast behavior is a Union-specific improvement over silent Kubernetes pending — but it requires that the node types you request are physically available in the data plane.

### Be explicit about ephemeral storage

The `disk` default is zero, which means a task pod will consume node storage as needed. A pod can be evicted if the node runs short on storage. Any team doing heavy data processing should always set `disk` explicitly:

```python
env = flyte.TaskEnvironment(
    name="my_env",
    resources=flyte.Resources(cpu="4", memory="16Gi", disk="50Gi"),
)
```

## RBAC and secrets

### Scope roles to project-domain pairs

Through Role-Based Access Control, users can be assigned roles — such as contributor or admin — scoped to specific project-domain pairs.

A reasonable default policy:

- **Development domain**: contributor access for everyone on the team
- **Production domain**: restricted to CI/CD service accounts and admins only

### Scope secrets as narrowly as possible

Union supports secrets at the project-domain level, ensuring API keys, tokens, and other sensitive material are only accessible within the workflows that need them. Avoid global-scoped secrets — always scope to the narrowest project-domain that requires access.

## Multi-team scaling patterns

### Establish naming conventions early

Once you have ten or more projects, discoverability degrades quickly. A `<team>-<product>` pattern (for example, `ml-training`, `data-etl`, `inference-serving`) makes quota management, RBAC, and billing attribution substantially easier.

### Put shared utility tasks in a dedicated project

If multiple teams need to share preprocessing tasks or model wrappers, create a `shared-utils` or `platform` project rather than duplicating code. This requires governance around versioning and backward compatibility, but it scales better than copy-paste.

### Use cluster assignment for multi-cluster deployments

The cluster assignment matchable attribute forces matching executions to consistently run on a specific Kubernetes cluster in multi-cluster deployments. Without an explicit assignment, cluster selection is random.

If you have GPU clusters alongside CPU-only clusters, configure execution cluster labels per project-domain so GPU workloads land on the right nodes. Random assignment is fine for homogeneous setups, but a poor default once cluster heterogeneity exists.

### Treat production as a managed service

Each `<project>/production` pair should have its own quota budget and change-management process. Quota changes in production should go through review rather than ad-hoc CLI updates.

## What's changing in v2

The v2 quota system is being modernized substantially.

### Current state

v2 quotas still largely follow the v1 model, but with infrastructure changes underneath. The v2 UI for quota management is not yet available — quota configuration today is done through the v1 UI.

### Architectural changes already underway

- **Decoupled from namespaces.** v2 moves away from the strict "one project equals one namespace" model. Multiple projects can share namespaces, with Union providing its own quota enforcement layer above Kubernetes.
- **Queue-based scheduling.** v2 introduces a queue construct in the control plane that enables priority-based scheduling and more flexible resource management.

### Planned for the first half of 2026

**Enhanced quota model:**

- More granular quotas beyond project-domain level
- Team-level quotas spanning multiple namespaces
- GPU-class-specific quotas (different limits for different GPU types)
- Hierarchical quota structures

**Priority and preemption:**

- Workflows assignable to different priorities
- Higher-priority workloads can preempt lower-priority ones
- Fair-scheduling algorithms in the spirit of Slurm

**Flexible enforcement:**

Union will rely less on Kubernetes ResourceQuotas and more on its own enforcement mechanisms, enabling more dynamic and intelligent resource allocation.

### Migration

The v2 quota system is designed to be backward compatible. Existing v1 quotas will continue to work during the transition. The enhanced capabilities — priority scheduling, hierarchical quotas, GPU-class quotas — are landing in the first half of 2026.

---

## Quick reference

| Decision | Recommendation |
|---|---|
| Team isolation | One project per team or ML product |
| Environments | Use domains (dev / staging / prod) |
| Quota scope | Per project-domain pair, never global |
| GPU workloads | Set `projectQuotaGpu` explicitly via Union |
| Task resources | Always declare `cpu` and `memory` as request/limit tuples |
| Ephemeral storage | Set `disk` explicitly for data-heavy tasks |
| Production access | CI/CD service accounts + admins only |
| Secrets | Scope to narrowest project-domain |
| Multi-cluster | Use cluster assignment, not random routing |
| Naming | `<team>-<product>` once you exceed ~10 projects |

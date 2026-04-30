---
title: Resource management and multi-team scaling
weight: 4
variants: -flyte +union
---

# Resource management and multi-team scaling

This guide covers the foundational primitives Union provides for multi-tenancy — projects, domains, quotas, task-level resources, RBAC, and secrets — and the patterns that work best as you scale to multiple teams.

Teams that set these up well early avoid most of the noisy-neighbor, cache-bleed, and resource-starvation problems that surface later.

## Project-domain structure

The combination of **project × domain** is Union's primary unit of isolation. Each pair gets its own quota budget. RBAC and secrets are flexible: they can be scoped narrowly to a project-domain pair, or broadened across projects, across domains, or organization-wide depending on how you want to share access.

### One project per team or ML product

Every independent team or ML product should have its own Union project. Projects are isolated from one another by default, though you can reference workflows or tasks across projects to reuse generalizable resources.

### Domains are environments, not teams

Domains are orthogonal to projects. They represent distinct environments — typically development, staging, and production — and enable dedicated configurations, permissions, secrets, cached execution history, and resource allocations for each environment.

A production domain in particular ensures a clean slate, so cached executions from development don't produce unexpected behavior in production runs.

A common pattern is to split clusters and networking across domains as well — for example, a dedicated production cluster with stricter network controls, separate from the cluster development and staging share. See [multi-cluster and multi-cloud](../../deployment/byoc/multi-cluster) for how this maps to underlying cloud accounts.

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

### Why quotas matter

Without quotas, projects can starve each other for shared resources. Runs that exceed available capacity are still dispatched to the cluster, and pods sit pending while the execution shows as "running." Quotas turn that silent contention into an explicit, fail-fast signal teams can act on.

## Task-level resources

### Declare resources on the task environment

Set resources on a `flyte.TaskEnvironment` (or override per task) using `flyte.Resources`:

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    resources=flyte.Resources(cpu="4", memory="16Gi", disk="50Gi"),
)

@env.task
def my_task():
    ...
```

If a task's resource request exceeds your project-domain quota, the execution fails immediately rather than queueing forever. That's the behavior you want — but it means teams should know what their quota is before sizing tasks. Coordinate with whoever owns quota configuration so requests stay within budget, or so the budget gets raised intentionally.

### Be explicit about ephemeral storage

By default, `disk` is unset, so no ephemeral-storage request or limit is applied. A task pod can still consume node storage as needed, and it may be evicted if the node comes under storage pressure. Any team doing heavy data processing should always set `disk` explicitly.

## RBAC and secrets

### Roles vs policies

Union splits access control into two concepts:

- **Roles** are named sets of actions (for example, "can register workflows", "can launch executions"). They describe *what* a principal can do.
- **Policies** bind roles to a scope — a specific project-domain pair, a whole domain (across all projects), a whole project (across all domains), or the entire organization. They describe *where* the role applies.

This split means you don't have to define roles per project-domain pair. A single "Contributor" role can be bound by one policy to `team-alpha/development`, and by another policy to *every* `production` domain across the organization. Pick the binding scope that matches the access you actually want to grant.

A reasonable default:

- **Development domains**: bind contributor roles broadly so everyone on the team can register and run workflows.
- **Production domains**: restrict to CI/CD service accounts and admins only.

See [user management](../user-management) for the full walkthrough on creating roles, policies, and assignments.

### Scope secrets as narrowly as possible

Union supports secrets at the project-domain level, ensuring API keys, tokens, and other sensitive material are only accessible within the workflows that need them. Like RBAC, secrets can also be scoped more broadly when shared across projects or domains — but default to the narrowest scope that satisfies the workflows that need access.

## Multi-team scaling patterns

### Establish naming conventions early

Once you have ten or more projects, discoverability degrades quickly. A `<team>-<product>` pattern (for example, `ml-training`, `data-etl`, `inference-serving`) makes quota management, RBAC, and billing attribution substantially easier.

### Put shared utility tasks in a dedicated project

If multiple teams need to share preprocessing tasks or model wrappers, create a `shared-utils` or `platform` project rather than duplicating code. Other teams target these without pulling in the implementation by referencing them through the [remote tasks API](../task-programming/remote-tasks):

```python
import flyte.remote

shared_preprocess = flyte.remote.Task.get(
    "shared-utils.preprocess",
    auto_version="latest",
)
```

This requires governance around versioning and backward compatibility, but it scales better than copy-paste.

### Use cluster assignment for multi-cluster deployments

The cluster assignment matchable attribute pins matching executions to a specific Union cluster in multi-cluster deployments. Without an explicit assignment, cluster selection is random — fine for homogeneous setups, but a poor default once cluster heterogeneity exists (for example, GPU clusters alongside CPU-only clusters).

Set the assignment per project-domain with `uctl`:

```yaml
# cpa.yaml
domain: production
project: team-alpha
clusterPoolName: gpu-pool
```

```bash
uctl update cluster-pool-attributes --attrFile cpa.yaml
```

See [`uctl update cluster-pool-attributes`](../../api-reference/uctl-cli/uctl-update/uctl-update-cluster-pool-attributes) for the full reference.

### Treat production as a managed service

Each `<project>/production` pair should have its own quota budget and change-management process. Quota changes in production should go through review rather than ad-hoc CLI updates.

The [Union Terraform provider](../../deployment/terraform/_index) is a good fit for this: it lets you manage projects, roles, policies, and access assignments declaratively, so production configuration lives in version control and changes go through PR review like any other infrastructure change.

## What's coming next

The next major step in scheduling is the **queue** construct — a control-plane primitive that lets you submit work into named queues with priority levels. Higher-priority work can preempt lower-priority work, and fair-share scheduling decides what runs when capacity is contested. This moves resource arbitration off raw quotas and onto something closer to a Slurm-style scheduler, which scales better for teams running mixed-criticality workloads on shared clusters.

If you're planning ahead for multi-team scaling, the project-domain and quota patterns described above remain the right foundation — queues will sit on top of them rather than replace them.

---

## Quick reference

| Decision | Recommendation |
|---|---|
| Team isolation | One project per team or ML product |
| Environments | Use domains (dev / staging / prod) |
| Quota scope | Per project-domain pair, never global |
| Task resources | Declare `cpu`, `memory`, and `disk` on `flyte.Resources` and stay within your quota |
| Ephemeral storage | Set `disk` explicitly for data-heavy tasks |
| RBAC | Bind roles via policies at the scope you actually need (project-domain, domain, project, or org) |
| Production access | CI/CD service accounts + admins only |
| Secrets | Scope to narrowest project-domain |
| Multi-cluster | Use cluster assignment, not random routing |
| Shared tasks | Put in a dedicated project, target via `flyte.remote.Task` |
| Production config | Manage with the Union Terraform provider |
| Naming | `<team>-<product>` once you exceed ~10 projects |

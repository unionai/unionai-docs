---
title: Resource management and multi-team scaling
weight: 4
variants: -flyte +union
---

# Resource management and multi-team scaling

This guide covers the foundational primitives Union provides for multi-tenancy (projects, domains, quotas, task-level resources, RBAC, and secrets) and the patterns that work best as you scale to multiple teams.

Teams that set these up well early avoid most of the noisy-neighbor, cache-bleed, and resource-starvation problems that surface later.

## Project-domain structure

The combination of **project × domain** is Union's primary unit of isolation. Each pair gets its own quota budget. RBAC and secrets are flexible: they can be scoped narrowly to a project-domain pair, or broadened across projects, across domains, or organization-wide depending on how you want to share access.

### One project per team or ML product

Every independent team or ML product should have its own Union project. Projects are isolated from one another by default, though you can reference workflows or tasks across projects to reuse generalizable resources.

### Domains are environments, not teams

Domains are orthogonal to projects. They represent distinct environments (typically development, staging, and production) and enable dedicated configurations, permissions, secrets, cached execution history, and resource allocations for each environment.

A production domain in particular ensures a clean slate, so cached executions from development don't produce unexpected behavior in production runs.

A common pattern is to split clusters and networking across domains as well: for example, a dedicated production cluster with stricter network controls, separate from the cluster development and staging share. See [multi-cluster and multi-cloud](../../deployment/byoc/multi-cluster) for how this maps to underlying cloud accounts.

## Resource limits

### Set per-task resource limits per project-domain pair

Resource limits are configured through the [settings](../get-started/core-concepts/settings) hierarchy, which resolves through the org → domain → project chain. Set them for a whole domain, or narrow them to a single project-domain pair:

```bash
# Domain-wide, inherited by every project in the domain
flyte edit settings --domain production

# Narrowed to one project-domain pair
flyte edit settings --domain production --project team-alpha
```

The command opens an editor. Uncomment and set the `task_resource` keys you want:

- **`task_resource.max.cpu`**, **`task_resource.max.memory`**, **`task_resource.max.storage`**: hard per-task ceilings. A per-task `flyte.Resources` request above the maximum is **capped to the maximum rather than rejected**. This is how you bound how large any single task in a domain or project can get.
- **`task_resource.min.cpu`**, **`task_resource.min.memory`**, **`task_resource.min.storage`**: the default request applied when a task doesn't specify one.
- **`task_resource.max.gpu`**, **`task_resource.min.gpu`**: the same ceiling and default, applied to GPU.

For scripted or CI setup, apply a YAML file non-interactively instead of opening the editor:

```bash
flyte edit settings --domain production --from-file limits.yaml
```

```yaml
task_resource.max.cpu: "8"
task_resource.max.memory: 32Gi
task_resource.max.gpu: "4"
```

See [Settings](../get-started/core-concepts/settings) for the full key list and how inheritance and overrides work.

### Why limits matter

These are per-task ceilings, not a namespace-wide aggregate: they bound how large any individual task can get, which keeps a single oversized task from claiming a whole node's worth of capacity. Setting a sane `task_resource.max` per domain (tighter in development, looser in production) is a low-effort guardrail against noisy-neighbor contention. Coordinate the ceilings with whoever sizes tasks so requests stay within them.

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

If a task requests more than the `task_resource.max` ceiling set for its project-domain, the request is capped to that ceiling rather than rejected, so the task still runs but with the maximum the scope allows. Teams should know the ceilings before sizing tasks. Coordinate with whoever owns the [settings](../get-started/core-concepts/settings) for the scope so requests stay within the ceiling, or so the ceiling gets raised intentionally.

### Be explicit about ephemeral storage

By default, `disk` is unset, so no ephemeral-storage request or limit is applied. A task pod can still consume node storage as needed, and it may be evicted if the node comes under storage pressure. Any team doing heavy data processing should always set `disk` explicitly.

## RBAC and secrets

### Roles vs policies

Union splits access control into two concepts:

- **Roles** are named sets of actions (for example, "can register workflows", "can launch executions"). They describe *what* a principal can do.
- **Policies** bind roles to a scope: a specific project-domain pair, a whole domain (across all projects), a whole project (across all domains), or the entire organization. They describe *where* the role applies.

This split means you don't have to define roles per project-domain pair. A single "Contributor" role can be bound by one policy to `team-alpha/development`, and by another policy to *every* `production` domain across the organization. Pick the binding scope that matches the access you actually want to grant.

A reasonable default:

- **Development domains**: bind contributor roles broadly so everyone on the team can register and run workflows.
- **Production domains**: restrict to CI/CD service accounts and admins only.

See [user management](../user-management) for the full walkthrough on creating roles, policies, and assignments.

### Scope secrets as narrowly as possible

Union supports secrets at the project-domain level, ensuring API keys, tokens, and other sensitive material are only accessible within the workflows that need them. Like RBAC, secrets can also be scoped more broadly when shared across projects or domains, but default to the narrowest scope that satisfies the workflows that need access.

## Multi-team scaling patterns

### Establish naming conventions early

Once you have ten or more projects, discoverability degrades quickly. A `<team>-<product>` pattern (for example, `ml-training`, `data-etl`, `inference-serving`) makes quota management, RBAC, and billing attribution substantially easier.

### Put shared utility tasks in a dedicated project

If multiple teams need to share preprocessing tasks or model wrappers, create a `shared-utils` or `platform` project rather than duplicating code. Other teams target these without pulling in the implementation by referencing them through the [remote tasks API](../tasks/task-programming/remote-tasks):

```python
import flyte.remote

shared_preprocess = flyte.remote.Task.get(
    "shared-utils.preprocess",
    auto_version="latest",
)
```

This requires governance around versioning and backward compatibility, but it scales better than copy-paste.

### Route work to the right cluster pool in multi-cluster deployments

In a multi-cluster deployment, work reaches a cluster through a [queue](../cluster-workload-management/queues), which routes to a [cluster pool](../cluster-workload-management/cluster-pools). To pin a project or domain's work to a specific pool (for example, a GPU pool), create a queue in that pool and set it as the default queue for the scope:

```bash
flyte edit settings --domain production --project team-alpha
```

Set `run.default_queue` to a queue that lives in the target pool:

```yaml
run.default_queue: gpu-queue
```

An individual task environment can also target a queue directly with the `queue` parameter. See [Managing queues](../cluster-workload-management/queues) for how queues bind to pools and clusters.

### Treat production as a managed service

Each `<project>/production` pair should have its own quota budget and change-management process. Quota changes in production should go through review rather than ad-hoc CLI updates.

The [Union Terraform provider](../../deployment/terraform/_index) is a good fit for this: it lets you manage projects, roles, policies, and access assignments declaratively, so production configuration lives in version control and changes go through PR review like any other infrastructure change.

## Quick reference

| Decision | Recommendation |
|---|---|
| Team isolation | One project per team or ML product |
| Environments | Use domains (dev / staging / prod) |
| Resource limits | Per-task ceilings via settings, scoped per project-domain |
| Task resources | Declare `cpu`, `memory`, and `disk` on `flyte.Resources` and stay within your limits |
| Ephemeral storage | Set `disk` explicitly for data-heavy tasks |
| RBAC | Bind roles via policies at the scope you actually need (project-domain, domain, project, or org) |
| Production access | CI/CD service accounts + admins only |
| Secrets | Scope to narrowest project-domain |
| Multi-cluster | Route via queues to a cluster pool |
| Shared tasks | Put in a dedicated project, target via `flyte.remote.Task` |
| Production config | Manage with the Union Terraform provider |
| Naming | `<team>-<product>` once you exceed ~10 projects |

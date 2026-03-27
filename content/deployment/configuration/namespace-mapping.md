---
title: Namespace mapping
weight: 8
variants: -flyte -serverless -byoc +selfmanaged
---

# Namespace mapping

By default, {{< key product_name >}} maps each project-domain pair to a Kubernetes namespace using the pattern `{project}-{domain}`. For example, the project `flytesnacks` in domain `development` runs workloads in namespace `flytesnacks-development`.

You can customize this mapping by setting the `namespace_mapping.template` value in your Helm configuration.

## Template syntax

The template uses Go template syntax with two variables:

- `{{ project }}` — the project name
- `{{ domain }}` — the domain name (e.g., `development`, `staging`, `production`)

### Examples

| Template | Project | Domain | Resulting namespace |
|----------|---------|--------|---------------------|
| `{{ project }}-{{ domain }}` (default) | `flytesnacks` | `development` | `flytesnacks-development` |
| `{{ domain }}` | `flytesnacks` | `development` | `development` |
| `myorg-{{ project }}-{{ domain }}` | `flytesnacks` | `development` | `myorg-flytesnacks-development` |

> [!WARNING]
> Changing namespace mapping after workflows have run will cause existing data in old namespaces to become inaccessible. Plan your namespace mapping before initial deployment.

## Data plane configuration

Set the `namespace_mapping` value at the top level of your dataplane Helm values. This single value cascades to all services that need it: clusterresourcesync, propeller, operator, and executor.

```yaml
namespace_mapping:
  template: "myorg-{{ '{{' }} project {{ '}}' }}-{{ '{{' }} domain {{ '}}' }}"
```

> [!NOTE]
> The template uses Helm's backtick escaping for Go template delimiters. In your values file, wrap `{{ project }}` and `{{ domain }}` with backtick-escaped `{{` and `}}` delimiters as shown above.

## How it works

Namespace mapping controls several components:

| Component | Role |
|-----------|------|
| **Clusterresourcesync** | Creates Kubernetes namespaces and per-namespace resources (service accounts, resource quotas) based on the mapping |
| **Propeller** | Resolves the target namespace when scheduling workflow pods |
| **Operator** | Resolves the target namespace for operator-managed resources |
| **Executor** | Resolves the target namespace for task execution |
| **Flyteadmin** (control plane) | Determines the target namespace when creating V1 executions |

All components must agree on the mapping. The dataplane chart's top-level `namespace_mapping` value is the canonical source that cascades to clusterresourcesync, propeller, operator, and executor automatically. You should **not** set per-service overrides.

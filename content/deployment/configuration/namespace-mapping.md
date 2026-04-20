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

## Compute plane configuration

Set the `namespace_mapping` value at the top level of your dataplane Helm values. This single value cascades to all services that need it: clusterresourcesync, propeller, operator, and executor.

```yaml
namespace_mapping:
  template: "myorg-{{ '{{' }} project {{ '}}' }}-{{ '{{' }} domain {{ '}}' }}"
```

> [!NOTE]
> The template uses Helm's backtick escaping for Go template delimiters. In your values file, wrap `{{ project }}` and `{{ domain }}` with backtick-escaped `{{` and `}}` delimiters as shown above.

{{< variant selfhosted >}}

## Self-hosted control plane configuration

If you are running a [self-hosted deployment](../selfhosted-deployment/_index) (control plane and data plane in the same cluster), you **must** also configure namespace mapping on the control plane for V1 executions.

> [!IMPORTANT]
> The control plane and data plane namespace mapping templates **must match exactly**. A mismatch causes flyteadmin to assign V1 executions to namespaces that the data plane hasn't created.

Add the following to your control plane Helm values:

```yaml
flyte:
  configmap:
    namespace_config:
      namespace_mapping:
        template: "myorg-{{ '{{' }} project {{ '}}' }}-{{ '{{' }} domain {{ '}}' }}"
```

> [!NOTE]
> `namespace_config` is the flyte-core subchart template key (it renders to `namespace_config.yaml`). `namespace_mapping` is the Go config section flyteadmin reads at runtime. This path uses `toYaml` (not `tpl`), so the Go template delimiters pass through as-is — **no backtick escaping is needed**.

> [!NOTE]
> V2 executions resolve namespaces on the data plane side and do not require control plane namespace mapping configuration.
{{< /variant >}}
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

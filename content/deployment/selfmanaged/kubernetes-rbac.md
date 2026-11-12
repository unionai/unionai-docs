---
title: Kubernetes access controls
description: The Kubernetes RBAC the Helm chart applies, and what each role can reach.
icon: shield-lock
weight: 12
variants: -flyte +union
---

# Kubernetes access controls

Union.ai's data plane runs entirely within your Kubernetes cluster. This page documents the Kubernetes RBAC that the
[`dataplane` Helm chart](https://github.com/unionai/helm-charts/tree/main/charts/dataplane) applies: the service
accounts, the namespace-scoped Roles, and the cluster-wide ClusterRoles, in each mode.

## Service accounts

By default, the Union.ai platform components share one Kubernetes service account, `union-system`: the operator, the
operator proxy, the leaseworker, the pod webhook, and Fluent Bit. The `commonServiceAccount` Helm value configures it.
Prometheus and kube-state-metrics run under their own service accounts, `union-operator-prometheus` and
`union-prometheus-kube-state-metrics`.

You can disable the common service account and configure per-component service accounts instead. When
`commonServiceAccount` is disabled, each component falls back to its own service account (for example,
`operator-system` for the operator, `fluentbit-system` for Fluent Bit). See the
[dataplane Helm chart reference](./helm-chart-reference/dataplane) for the per-component service account values.

## Low-privilege mode vs. standard mode

The data plane supports two RBAC modes:

| Mode | Helm value | RBAC scope | Use case |
|------|------------|-----------|----------|
| **Low-privilege** (chart default) | `low_privilege: true` | Namespace-scoped Roles, with a few ClusterRoles where a component needs them | Restricted environments, shared clusters |
| **Standard** | `low_privilege: false` | ClusterRoles for the platform components | Cluster-wide monitoring and usage collection, multi-namespace deployments |

A data plane installed with Helm runs in low-privilege mode unless you set `low_privilege: false`. A data plane
connected from the Union.ai UI on AWS, GCP, or Azure runs in standard mode, but still runs tasks only in the namespace
you registered: see [What Union.ai installs in your cluster](./whats-installed).

In low-privilege mode:

- The platform components get namespace-scoped Roles in the release namespace instead of ClusterRoles.
- Task pods run in the release namespace.
- Prometheus can't discover nodes or scrape cAdvisor, so task-level CPU and memory charts show no data, and
  kube-state-metrics reports only the release namespace, without node-level metrics. Cost figures are less accurate
  without node metrics.

Choose low-privilege mode when your cluster policies prohibit ClusterRoles (for example, OPA Gatekeeper or Kyverno),
when Union.ai is a tenant on a shared cluster, or when compliance requires minimizing the blast radius to a single
namespace.

### Running in standard mode

To run in standard mode, set `low_privilege: false`. The Prometheus and kube-state-metrics subcharts create no RBAC
of their own by default, and the chart's namespace-scoped Role for them exists only in low-privilege mode. So in
standard mode, also turn on their ClusterRoles, or Prometheus has no permission to scrape anything:

```yaml
low_privilege: false
prometheus:
  rbac:
    create: true
  kube-state-metrics:
    rbac:
      create: true
```

### Multi-namespace mode

By default, task pods run in the release namespace in both modes. To run each project-domain in its own namespace,
set `namespaces.enabled: true` and `clusterresourcesync.enabled: true` in standard mode. Clusterresourcesync then
creates the task namespaces and their resources. See [Namespace mapping](./configuration/namespace-mapping).

## Roles in every mode

These Roles are scoped to the release namespace:

### `union-system-secret`

- Bound to `union-system`
- Secrets: get, list, create, update, delete

### `operator-system`

- Bound to `union-system`
- Secrets and deployments: get, list, watch, create, update
- DaemonSets and StatefulSets: get, list, watch

## Low-privilege mode

In low-privilege mode, the platform components' roles are namespace-scoped Roles in the release namespace:

| Role | Bound to | Grants, in the release namespace |
|------|----------|----------------------------------|
| `operator-system` | `union-system` | In addition to the rules above: full access to FlyteWorkflows; get, list, watch, create, update and delete on resource quotas, pods, ConfigMaps, pod templates, secrets and namespaces; Knative Serving revisions, configurations and services |
| `proxy-system` | `union-system` | Read-only (get, list, watch): events, FlyteWorkflows, pod logs, pods, Ray jobs, resource quotas |
| `union-leaseworker` | `union-system` | Get, list, watch, create, update, delete and patch on all resources in the namespace; events; read pods; manage CRDs |
| `union-webhook-role` | `union-system` | Get, create, update, patch, list and watch on mutating webhook configurations, secrets, pods and replica set finalizers |
| `union-operator-prometheus-rbac` | `union-operator-prometheus`, `union-prometheus-kube-state-metrics` | Read-only access to the scrape targets and to the resources kube-state-metrics reports on |

## Standard mode

In standard mode, the platform components' roles become ClusterRoles, with the same rules applied cluster-wide:

| ClusterRole | Bound to | Grants, cluster-wide |
|-------------|----------|----------------------|
| `operator-system` | `union-system` | Full access to FlyteWorkflows; get, list, watch, create, update and delete on resource quotas, pods, ConfigMaps, pod templates, secrets, namespaces and nodes; the `/metrics` endpoint; Knative Serving revisions, configurations and services |
| `proxy-system` | `union-system` | Read-only (get, list, watch): events, FlyteWorkflows, pod logs, pods, Ray jobs, resource quotas |
| `union-leaseworker` | `union-system` | Get, list, watch, create, update, delete and patch on all resources; events; read pods; manage CRDs |
| `union-webhook-role` | `union-system` | Get, create, update, patch, list and watch on mutating webhook configurations, secrets, pods and replica set finalizers |
| `union-operator-prometheus` | `union-operator-prometheus` | Read-only: nodes (including their `/proxy` and `/metrics` subresources), services, endpoints, endpoint slices, pods, ingresses, ConfigMaps; the `/metrics` endpoint. Created when `prometheus.rbac.create` is `true` |
| `union-kube-state-metrics` | `union-prometheus-kube-state-metrics` | List and watch on the resources kube-state-metrics reports on, across all namespaces. Created when `prometheus.kube-state-metrics.rbac.create` is `true` |

The `operator-system` Role in the release namespace stays as well.

Multi-namespace mode adds:

| ClusterRole | Bound to | Grants, cluster-wide |
|-------------|----------|----------------------|
| `union-clustersync-resource` | `union-clustersync-system` | Full access to namespaces, service accounts, Roles, RoleBindings, ClusterRoleBindings, ConfigMaps, secrets, services, pods, pod templates, resource quotas, limit ranges, persistent volumes and claims |

If you enable propeller (`flytepropeller.enabled: true`, off by default), it adds the `flytepropeller-role`
ClusterRole, bound to `flytepropeller-system`.

## ClusterRoles in every mode

A few components need cluster-scoped access in both modes:

| ClusterRole | Bound to | Grants |
|-------------|----------|--------|
| `union-fluentbit` | `union-system` | Read-only (get, list, watch) on namespaces and pods, to label the logs Fluent Bit ships |
| `flyte-webhook-cleanup-<namespace>` | `flyte-webhook-cleanup` | Get and delete on mutating webhook configurations, deployments and secrets. Used by a pre-upgrade hook that removes the webhook left behind by older chart versions |
| `knative-serving-*`, `net-kourier` | Knative Serving and Kourier | The ClusterRoles Knative Serving needs to run app serving. Created when app serving is on (`apps.enabled`, on by default) |

## Service access

### `operator/operator-proxy`

Service that provides access to both cluster resources and cloud provider APIs, particularly focused on compute resource management.

#### Kubernetes resources

##### Core resources

- Pods: Access via informers to monitor and manage pod lifecycle.
- Nodes: Access to retrieve node information.
- ResourceQuotas: Read access.
- ConfigMaps: Access for configuration management
- Secrets: Access for credentials storage
- Namespaces: Referenced in container/pod identification contexts

##### Custom resources

- FlyteWorkflows: Management of v1alpha1.FlyteWorkflow resources
- Kueue Resources (optional): Access to ResourceFlavor, ClusterQueue, and other queue resources
- Karpenter NodePools (optional): For AWS-based compute resource management

##### Cloud Provider Resources

- Object Storage: Read/write operations to cloud storage buckets

##### Authentication and configuration

- OAuth: Uses app ID for authentication with Union cloud services
- Service Account Roles: Configured via UserRoleKey and UserRole
- Cluster Information: Access to cluster metadata and metrics

### Leaseworker

Takes work from Union.ai's scheduler and runs your tasks as pods in the task namespace. Its role covers the task pods
and the resources they need.

### Pod webhook

A mutating admission webhook that adds Union.ai-specific information to task pods, including secret injection. It runs
as its own deployment, `union-pod-webhook`, with configurable certificate management (Helm-generated, cert-manager,
external, or legacy).

---
title: Kubernetes Access Controls
weight: 4
variants: -flyte +union
---

# Kubernetes Access Controls

## Service account

By default, all data plane components share a single Kubernetes service account: `union-system`. This service account is configured through the `commonServiceAccount` Helm value and is used by the operator, executor, proxy, webhook, and FluentBit.

Users can disable the common service account and configure per-component service accounts instead. When `commonServiceAccount` is disabled, each component falls back to its own service account (for example, `operator-system` for the operator, `fluentbit-system` for FluentBit). Refer to the [dataplane Helm chart reference](../helm-chart-reference/dataplane) for the full set of per-component service account values.

See the [dataplane helm charts](https://github.com/unionai/helm-charts/tree/main/charts/dataplane) for the full set of Roles and ClusterRoles.

## Standard mode vs. low-privilege mode

The data plane supports two RBAC modes:

| Mode | RBAC scope | Use case |
|------|-----------|----------|
| **Standard** (default) | ClusterRoles + namespace Roles | Multi-namespace deployments, full feature set |
| **Low-privilege** (`low_privilege: true`) | Namespace-scoped Roles only | Single-namespace deployments, restricted environments |

In low-privilege mode, the chart automatically:
- Replaces ClusterRoles with namespace-scoped Roles
- Limits resource sync, executor, and monitoring to the release namespace
- Disables features that require cluster-wide access (ClusterResourceSync, OpenCost)

## Namespace-scoped Roles

##### `proxy-system-secret`
- Scoped to `union` namespace
- Permissions on secrets: get, list, create, update, delete

##### `operator-system`
- Scoped to `union` namespace
- Permissions on secrets and deployments: get, list, watch, create, update

##### `union-operator-admission` (for webhook)
- Scoped to `union` namespace
- Permissions on secrets: get, create

## ClusterRoles (standard mode only)

> [!NOTE] Low-privilege mode
> The ClusterRoles below are **not created** in low-privilege mode. Equivalent namespace-scoped Roles are created instead.

### Metrics and Monitoring

##### `release-name-kube-state-metrics`

- **Purpose**: Collects metrics from Kubernetes resources
- **Access Pattern**: Read-only (`list`, `watch`) to numerous resources across multiple API groups
- **Scope**: Comprehensive — covers core resources, workloads, networking, storage, and authentication

##### `prometheus-operator`
- **Access**: Full control (`*`) over Prometheus monitoring resources
- **Key Permissions**:
  - Complete access to monitoring.coreos.com API group resources
  - Full access to statefulsets, configmaps, secrets
  - Pod management (list, delete)
  - Service/endpoint management
  - Read-only for nodes, namespaces, ingresses

##### `union-operator-prometheus`
- **Access**: Read-only access to metrics sources
- **Resources**: nodes, services, endpoints, pods, endpointslices, ingresses
- **Special**: Access to `/metrics` and `/metrics/cadvisor` endpoints

### Resource Management

##### `clustersync-resource`
- **Access**: Full control (`*`) over core and RBAC resources
- **Resources**:
  - Core: configmaps, namespaces, pods, resourcequotas, secrets, services, serviceaccounts, podtemplates
  - RBAC: roles, rolebindings, clusterrolebindings
- **API Groups**: `""` (core) and `rbac.authorization.k8s.io`

##### `proxy-system`
- **Access**: Read-only (`get`, `list`, `watch`)
- **Resources**: events, flyteworkflows, pods/log, pods, rayjobs, resourcequotas

### Workflow Management

##### `operator-system`
- **Access**: Full control over Flyte workflows, CRUD for core resources
- **Resources**:
  - Full access to flyteworkflows
  - Management of pods, configmaps, resourcequotas, podtemplates, nodes
  - Access to `/metrics` endpoint

##### `flytepropeller-webhook-role`
- **Access**: Get, create, update, patch
- **Resources**: mutatingwebhookconfigurations, secrets, pods, replicasets/finalizers

##### `flytepropeller-role`
- **Access**: Varied per resource type
- **Key Permissions**:
  - Read-only for pods
  - Event management
  - CRD management
  - Full control over flyteworkflows including finalizers

## Service Access

### `operator/operator-proxy`
Service that provides access to both cluster resources and cloud provider APIs, particularly focused on compute resource management.

#### Kubernetes Resources

##### Core Resources
- Pods: Access via informers to monitor and manage pod lifecycle.
- Nodes: Access to retrieve node information.
- ResourceQuotas: Read access.
- ConfigMaps: Access for configuration management
- Secrets: Access for credentials storage
- Namespaces: Referenced in container/pod identification contexts

##### Custom Resources
- FlyteWorkflows: Management of v1alpha1.FlyteWorkflow resources
- Kueue Resources (optional): Access to ResourceFlavor, ClusterQueue, and other queue resources
- Karpenter NodePools (optional): For AWS-based compute resource management

##### Cloud Provider Resources
- Object Storage: Read/write operations to cloud storage buckets

##### Authentication and Configuration
- OAuth: Uses app ID for authentication with Union cloud services
- Service Account Roles: Configured via UserRoleKey and UserRole
- Cluster Information: Access to cluster metadata and metrics

### `FlytePropeller/PropellerWebhook`
Kubernetes operator that executes Flyte graphs natively on Kubernetes. The webhook runs as a separate deployment with configurable certificate management (Helm-generated, cert-manager, external, or legacy).

#### Kubernetes Resources
- Manages pod creation for executions
- Secret injection
- MutatingWebhookConfiguration management (standard mode only; disabled in low-privilege mode)

#### Custom Resources
- FlyteWorkflows: Management of v1alpha1.FlyteWorkflow resources

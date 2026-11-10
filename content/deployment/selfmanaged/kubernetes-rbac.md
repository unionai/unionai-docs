---
title: Kubernetes access controls
description: Choose an RBAC scope for the data plane Helm chart, and see the roles each choice creates.
icon: shield-lock
weight: 12
variants: -flyte +union
---

# Kubernetes access controls

The [`dataplane` Helm chart](https://github.com/unionai/helm-charts/tree/main/charts/dataplane) creates
the Kubernetes RBAC resources that Union.ai's data plane components need. There are three Helm values that decide what it creates:

| Value | Default | Decides |
|-------|---------|---------|
| `singleNamespace` | `true` | Whether tasks and apps run in the (Helm) release namespace, or in a namespace per project and domain. |
| `namespaces.enabled`, `namespaces.static` | `enabled.false` , and `static` lists six names | Whether the chart pre-creates the namespaces listed in `namespaces.static` and binds the work-namespace role in each. It applies only when `singleNamespace` is `false`. The scope comes from `singleNamespace` alone. |
| `commonServiceAccount.enabled` | `true` | Whether the Union backend components share one service account or each get their own. Defaults to `true`. |


> [!NOTE] Chart version
> This page describes `dataplane` chart 2026.11.4 or later. Earlier versions name the scope value
> `low_privilege`. See [Upgrade from `low_privilege`](#upgrade-from-low_privilege).

## Choose a scope


| | Single-namespace (`singleNamespace: true`) | Multi-namespace (`singleNamespace: false`) |
|---|---|---|
| Work namespaces where tasks and apps run| The (Helm) release namespace | One namespace per project and domain, created by `clusterresourcesync`, `namespaces.static`, or your own tooling.|
| Grants in the namespaces where work runs | A Role in the release namespace | A RoleBinding in each work namespace, mapped to one shared ClusterRole |
| Cluster-scoped grants | A fixed list of reads, plus Knative's reads when app serving is on | The same, plus cluster-wide `list` and `watch` for components that watch every work namespace |
| What you must provide | Nothing | Something that creates each work namespace and its RoleBinding. Set `clusterresourcesync.enabled: true`, list the namespaces in `namespaces.static`, or use your own tooling. If none of these runs, tasks fail with `Forbidden` |
| Is the work-namespace role bound in the release namespace? | Yes. The release namespace is also the work namespace | No. Work-namespace grants are never bound in the release namespace |

Choose single-namespace mode when:

- The Union.ai stack is a tenant on a shared cluster, or your policies limit it to one namespace.
- A single namespace for all projects and domains is acceptable.

Choose multi-namespace mode when:

- You want each project and domain isolated in its own namespace, with its own quota and cloud identity.
- The work-namespace role, which carries a wildcard, must stay out of the release namespace.

Monitoring, usage collection, and app serving work in both modes.

> Write `singleNamespace` as an unquoted boolean. The chart refuses a quoted string such as `"false"`.

## Single-namespace mode

Single-namespace mode is the default. You don't need to set anything:

```yaml
singleNamespace: true
```

In this mode:

- Union.ai's workloads, tasks and apps included, run in the Helm release namespace. Every grant that can be
  namespaced is a Role in the release namespace. The one exception is `<release-ns>-prometheus-apiserver-discovery`,
  a Role in `default` that Prometheus uses to discover the API server endpoints.
- Cluster-scoped reads are limited to resources that have no namespaced form: nodes, node and API server
  metrics, IngressClass, and Knative's informers.
- Cluster-scoped writes are pinned to named objects. The exceptions are `nodeobserver` and
  `node-bootstrap`, both off by default, which each remove a startup taint from their own node.
- App serving is on by default and adds Knative's cluster-wide reads. 
- Knative's controllers watch every
namespace however their RBAC is written. 

> [!WARNING] The install identity needs cluster permissions.  
> Single-namespace mode limits what Union.ai's components can do. It doesn't make the chart installable
> by an identity confined to one namespace. The chart still creates ClusterRoles, a PriorityClass, and a
> CSIDriver. Subcharts such as ingress-nginx and metrics-server, when enabled, create their own cluster
> RBAC.

## Multi-namespace mode

Set `singleNamespace: false`, and turn on something that creates the work namespaces. The chart ships
[`examples/values.full-privilege.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/dataplane/examples/values.full-privilege.yaml)
with the matching settings. Layer it after your other values files, or set the same values yourself:

```yaml
singleNamespace: false

# Create a namespace per project and domain as projects are registered,
# and bind Union.ai's work-namespace role in each one.
clusterresourcesync:
  enabled: true

prometheus:
  kube-state-metrics:
    # Collect from every namespace, so task pods in work namespaces are included.
    releaseNamespace: false
```

### Create the work-namespace RoleBinding

Union.ai's components reach each work namespace through a RoleBinding named `<release-ns>-work-ns`,
which points at the ClusterRole of the same name. Every work namespace needs this binding. If nothing
creates it, the chart renders without errors but the tasks fail with `Forbidden`.

Use one or more of these ways to create the namespaces and their bindings:

| Option | Set | Covers |
|--------|-----|--------|
| `clusterresourcesync` | `clusterresourcesync.enabled: true` | Each namespace, as its project is registered |
| The chart | `namespaces.enabled: true` and a list in `namespaces.static` | The namespaces you list, at install and upgrade |
| Your own tooling | Nothing in the chart | Whatever your tooling provisions |

To pre-create namespaces with the chart, list the names your namespace mapping produces. The default
mapping is `<project>-<domain>`:

```yaml
singleNamespace: false
namespaces:
  enabled: true
  static:
    - <project>-development
    - <project>-staging
    - <project>-production
  labels:
    union.ai/namespace-type: flyte
```

- A namespace in `namespaces.static` gets only the Namespace and the RoleBinding. `clusterresourcesync`
  also creates the `project-quota` ResourceQuota and the workload identity annotation on the `default`
  service account. Create those yourself for a static namespace.
- Without the `union.ai/namespace-type: flyte` label, the operator doesn't copy the image builder
  configuration into the namespace.
- The chart refuses a `namespaces.static` list that includes the release namespace, and refuses
  `namespaces.enabled: true` with an empty list.
- Namespaces in `namespaces.static` carry `helm.sh/resource-policy: keep`, so `helm uninstall` leaves
  them in place. Argo CD and other GitOps controllers ignore that annotation. Add your controller's own
  retention annotation in `namespaces.annotations`, for example
  `argocd.argoproj.io/sync-options: Prune=false,Delete=false`.

If your own tooling creates the bindings, copy the subjects from a chart render, such as
`helm template ... --set singleNamespace=false --set namespaces.enabled=true`. Don't write them by hand.
The list changes with the components you enable, and any extra subject gets the whole role.

### Confirm the binding

A successful render or sync doesn't show whether the binding exists. After you register a project,
check its namespace:

```bash
kubectl get rolebinding <release-ns>-work-ns -n <work-namespace> \
  -o jsonpath='{.subjects[*].name}'
kubectl auth can-i create pods -n <work-namespace> \
  --as=system:serviceaccount:<release-ns>:<one-of-those-subjects>
```

A missing binding shows up in one of two ways:

- Task pods fail with `Forbidden`.
- Task pods that use private images fail with `ImagePullBackOff`. The pod webhook couldn't copy the pull
  secret into the namespace. The error appears only in
  `kubectl logs -n <release-ns> deploy/union-pod-webhook`.

If `clusterresourcesync` creates the bindings, check its logs for errors applying
`ab_work_ns_binding.yaml`.

### Grant reads for CRD-based task plugins

A task plugin that runs a custom resource, such as a Spark application or a Ray job, watches that
resource in every namespace. Only a ClusterRole can authorize that watch. List the custom resources your
plugins use in `taskPluginClusterReadRules`:

```yaml
taskPluginClusterReadRules:
  - apiGroups: [sparkoperator.k8s.io]
    resources: [sparkapplications]
  - apiGroups: [ray.io]
    resources: [rayjobs, rayclusters]
  - apiGroups: [kubernetes.dask.org]
    resources: [daskjobs]
  - apiGroups: [kubeflow.org]
    resources: [pytorchjobs, tfjobs, mpijobs]
  - apiGroups: [jobset.x-k8s.io]
    resources: [jobsets]
```

The chart grants `list` and `watch` on each entry. Single-namespace mode doesn't need this value.

### Limit what `clusterresourcesync` can write

`clusterresourcesync` creates RoleBindings, and Kubernetes RBAC can't limit a write to a set of
namespaces. The chart pins the role it can bind to `<release-ns>-work-ns`, but not where it can bind it.
A compromised `clusterresourcesync` could bind that role in any namespace, `kube-system` included.

To reduce this:

- Set `commonServiceAccount.enabled: false`, so `clusterresourcesync` runs as its own
  `union-clustersync-system` service account instead of the shared one.
- Add an admission policy, for example with Kyverno or OPA Gatekeeper, that limits that service
  account's Namespace and RoleBinding writes to your project namespace naming convention.
- Or turn `clusterresourcesync` off and create the namespaces and bindings with tooling you trust.

## Service accounts

By default, Union.ai's components share one service account, `union-system`. Prometheus and
kube-state-metrics run as `union-operator-prometheus` and `union-kube-state-metrics`.

To give each component its own service account, set:

```yaml
commonServiceAccount:
  enabled: false
```

This changes which identity holds each grant, not the grants. The rules stay the same, and every component that uses `work-ns` still gets the whole pooled role, so splitting the accounts leaves work-namespace access as it is. The components then run as `operator-system`, `proxy-system`, `leaseworker`, `union-webhook-system`, `union-clustersync-system`,
`dataproxy-system`, `union-imagebuilder`, `flyteconnector`, and, with app serving on, `knative-controller`,
`knative-activator`, `knative-autoscaler`, `knative-webhook`, and `net-kourier`.

> [!WARNING] Bind each new service account to a cloud identity first
> Each new service account needs a workload identity binding before it can reach object storage: an IRSA
> trust subject on AWS, a Workload Identity member on GCP, or a federated credential on Azure. Without
> one, the pods keep running and their storage calls fail.

Fluent Bit keeps the `union-system` service account unless you also set `fluentbit.serviceAccount.name`.

## Roles the chart creates

The chart names each role for the component and where its rules apply:
`<release-ns>-<component>-<slot>`. With the release namespace `union`, the operator's read-only role in
its own namespace is `union-operator-comp-ns-read`.

| Slot | Kind | Applies in | Grants |
|------|------|------------|--------|
| `comp-ns-read`, `comp-ns-write` | Role | The release namespace | One component's access to Union.ai's own Deployments, Secrets, and ConfigMaps |
| `work-ns` | ClusterRole and a RoleBinding per work namespace. A Role in single-namespace mode | Each work namespace | Access to tasks, apps, and image builds. One role, shared by every component that declares rules into it |
| `work-ns-cluster-read` | ClusterRole | Every namespace | `list` and `watch` for components that watch every work namespace. Multi-namespace mode only |
| `cluster-read` | ClusterRole | The cluster | Reads of cluster-scoped resources, such as nodes, and Knative's informers |
| `cluster-write` | ClusterRole | The cluster | Writes to named cluster-scoped objects |

The `work-ns` role holds the combined rules of every component that uses it, including a wildcard on all
resources from the leaseworker and propeller. A component that can create pods in a namespace already
controls that namespace, so the boundary is where the role is bound: only in work namespaces in
multi-namespace mode, and in the release namespace in single-namespace mode.

The chart refuses any rule with a wildcard verb, or with `escalate`, `impersonate`, or `bind`. It refuses
`apiGroups: ["*"]` outside `work-ns`.

### Roles at the default values

With release namespace `union`, app serving on, and the default `commonServiceAccount`:

| Role | Kind | Mode |
|------|------|------|
| `union-operator-comp-ns-read`, `union-operator-comp-ns-write` | Role | Both |
| `union-proxy-comp-ns-read`, `union-leaseworker-comp-ns-read` | Role | Both |
| `union-knative-<component>-comp-ns-read`, `-comp-ns-write` | Role | Both, with app serving on |
| `union-system-secret`, `union-operator-prometheus-rbac` | Role | Both |
| `union-operator-cluster-read` | ClusterRole | Both. Nodes and the API server `/metrics` endpoint |
| `union-prometheus-cluster-read`, `union-kube-state-metrics-cluster-read` | ClusterRole | Both. Node discovery, cAdvisor through the API server proxy, and cluster-scoped metrics |
| `union-knative-<component>-cluster-read`, `union-knative-webhook-cluster-write` | ClusterRole | Both, with app serving on. Every webhook write is pinned to a named object |
| `flyte-webhook-cleanup-union` | ClusterRole and Role | Both. Used by a pre-upgrade hook that deletes webhook objects left by older chart versions, pinned to those objects |
| `union-prometheus-apiserver-discovery` | Role in `default` | Both. Prometheus' discovery of the API server endpoints |
| `union-work-ns` | Role | Single-namespace |
| `union-work-ns` | ClusterRole | Multi-namespace |
| `union-<component>-work-ns-cluster-read` | ClusterRole | Multi-namespace. The operator, proxy, leaseworker, and pod webhook |
| `union-clusterresourcesync-cluster-write` | ClusterRole | Multi-namespace, with `clusterresourcesync` on |
| `union-secret-read` | Role | Multi-namespace. Secret reads in `proxy.secretsNamespace` |
| `union-kube-state-metrics` | Role in single-namespace mode, ClusterRole in multi-namespace mode | Both |

Enabling more components, such as propeller, `nodeobserver`, or `node-bootstrap`, adds roles named the
same way.

### Prometheus and kube-state-metrics

The chart writes Prometheus' and kube-state-metrics' RBAC itself, from the scrape jobs and collectors it
configures. Leave the subcharts' own RBAC off. The chart refuses to render if you set
`prometheus.rbac.create` or `prometheus.kube-state-metrics.rbac.create` to `true`.

To collect more kube-state-metrics data, add a collector to `prometheus.kube-state-metrics.collectors`.
The chart grants the reads that collector needs. See [Monitoring](./configuration/monitoring).

## Audit an install

Audit the rendered roles, not the values. Render the chart with your values files:

```bash
helm template union unionai/dataplane -n <release-ns> -f <your-values>.yaml > rendered.yaml
```

The default multi-namespace render has no work namespaces, so `<release-ns>-work-ns` has no bindings
and an audit that follows bindings reports none of its grants. Add `--set namespaces.enabled=true`, or
audit a live cluster after the first project sync.

Key each permission on service account, namespace, API group, resource, and verb. A grant in a work
namespace doesn't cover the same grant missing in the release namespace. To see everything one identity
can do, list every RoleBinding and ClusterRoleBinding that names it.

## Upgrade from `low_privilege`

Find the row that matches your values on the chart you run now. When you set `singleNamespace`, remove
`low_privilege`, because the render fails when the two keys disagree.

| Your values before 2026.11.4 | Change to |
|------------------------------|-----------|
| Neither key set, or `low_privilege: true` | Nothing. You can rename the key to `singleNamespace: true`. |
| `low_privilege: false` with `namespaces.enabled` unset or `false` | `singleNamespace: true`. This install ran single-namespace. If you keep `low_privilege: false`, it becomes multi-namespace, and every task fails with `Forbidden` until each work namespace has its RoleBinding. |
| `low_privilege: false` with `namespaces.enabled: true` | `singleNamespace: false`, with `namespaces.enabled: true` and your `namespaces.static` list unchanged. Add `clusterresourcesync.enabled: true` or your own tooling for namespaces outside the list. Layer `examples/values.full-privilege.yaml` so kube-state-metrics collects from the work namespaces.  If your own tooling creates work namespaces, create the `<release-ns>-work-ns` RoleBinding in every existing one before you upgrade. Before 2026.11.4, a ClusterRoleBinding gave the leaseworker and propeller access to every namespace.  From 2026.11.4, that RoleBinding is their only grant in a work namespace.

Also:

- Keep every name in `namespaces.static` during this upgrade. The upgrade adds `helm.sh/resource-policy: keep` to each listed namespace, so a name you drop now is deleted with everything in it. Add names freely, and remove them in a later upgrade.
- In multi-namespace mode, list the custom resources of Spark, Ray, Dask, Kubeflow, or JobSet tasks in `taskPluginClusterReadRules`. Before 2026.11.4, a cluster-wide grant covered them.
- Before 2026.11.4, the chart ignored `commonServiceAccount.enabled: false` in single-namespace mode. Now it
  takes effect, so bind each new service account to a cloud identity before you upgrade.
- Propeller and `clusterresourcesync` run as the shared `union-system` account by default. A cloud identity bound to the old propeller or clusterresourcesync account must also trust `union-system`.
- Remove `prometheus.rbac.create` and `prometheus.kube-state-metrics.rbac.create` from your values.
- In templated values, replace `.Values.low_privilege` with `include "singleNamespace" .`.

The chart's [migration guide](https://github.com/unionai/helm-charts/blob/main/charts/MIGRATION.md) has
a values snippet for each case.

## Related pages

- [Namespace mapping](./configuration/namespace-mapping)
- [Monitoring](./configuration/monitoring)
- [Dataplane Helm chart reference](./helm-chart-reference/dataplane)
- [Chart RBAC reference on GitHub](https://github.com/unionai/helm-charts/tree/main/charts/dataplane/docs/rbac)

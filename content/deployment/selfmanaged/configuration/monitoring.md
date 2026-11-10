---
title: Monitoring
description: The Prometheus instance the data plane deploys, the metrics it collects, and the optional cluster monitoring stack.
icon: graph-up
weight: 5
variants: -flyte +union
---

# Monitoring

The Union.ai data plane runs its own [Prometheus](https://prometheus.io/) instance, which collects the metrics that
platform features rely on: cost tracking, task-level resource monitoring, and execution observability. It is
pre-configured and needs no setup.

For operational monitoring of the cluster itself (node health, API server metrics, CoreDNS, and so on), the data plane
chart also includes an optional [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack),
which you turn on separately.

| Concern | What it monitors | Deployed by | On by default |
|---------|------------------|-------------|---------------|
| **Union.ai features** | Task resource usage, cost, GPU utilization, app serving, Union.ai services | The `prometheus` subchart | Yes |
| **Cluster health** | Kubernetes components, nodes, alerting, Grafana dashboards | The `kube-prometheus-stack` subchart, under `monitoring` | No (`monitoring.enabled`) |

## Union.ai features Prometheus

The chart deploys the community [`prometheus` chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus)
as a subchart, with kube-state-metrics, in the release namespace. It needs no Prometheus Operator and no CRDs: the
chart writes the scrape configuration and recording rules into the `union-prometheus` ConfigMap. This instance is a
platform dependency. Don't replace it or change its scrape configuration.

Other data plane components reach it at:

```
http://union-operator-prometheus.<NAMESPACE>.svc/prometheus
```

### Scrape targets

| Job | What it scrapes | Notes |
|-----|-----------------|-------|
| `kube-state-metrics` | Pod and node resource requests, limits, status and capacity | Keeps only the series cost and resource tracking use |
| `union-services` | The Union.ai services' own metrics: operator, operator proxy, data proxy, leaseworker | Services labeled `platform.union.ai/prometheus-group: union-services`, on their `debug` port |
| `kubernetes-apiservers` | API server object counts and request rates | Each API server endpoint behind the `default/kubernetes` Service |
| `kubernetes-cadvisor` | Container CPU and memory usage, from the kubelet through the API server proxy | |
| `serving-envoy` | Envoy request counts and latency for app serving | No targets unless app serving is on (`apps.enabled`, on by default) |
| `gpu-metrics` | DCGM exporter GPU metrics | No targets unless `dcgm-exporter.enabled` |
| `opencost` | Node hourly cost rates | No targets unless `opencost.enabled` (off by default) |
| `flytepropeller` | Propeller execution metrics | No targets unless `flytepropeller.enabled` (off by default) |

### Recording rules

When `cost.enabled` is `true`, the default, the chart loads its cost and GPU recording rules into this Prometheus.

### Metrics sent to the control plane

In zero-trust mode (`zero_trust.enabled`, the default), Prometheus also forwards the metrics it collects to the
control plane, with Prometheus remote write to `https://<CONTROLPLANE_HOST>/metrics/remote_write`. It authenticates
with OAuth2 as the cluster's app, `secrets.admin.clientId`, using the client secret in the `union-secret-auth` secret,
so the chart requires `secrets.admin.enable: true` in this mode. With `zero_trust.enabled: false`, nothing is
forwarded.

### RBAC

The chart writes Prometheus' and kube-state-metrics' RBAC itself, from the scrape jobs and collectors it configures.
Every scrape job, cAdvisor included, works in both [scope modes](../kubernetes-rbac#choose-a-scope). Requires
`dataplane` chart 2026.11.4 or later. With the release namespace `union`:

| Service account | Role | Grants |
|-----------------|------|--------|
| `union-operator-prometheus` | `union-operator-prometheus-rbac` (Role) | `list` and `watch` on endpoints, services, and pods in the release namespace |
| | `union-prometheus-apiserver-discovery` (Role in `default`) | The same, in the `default` namespace, to discover the API server endpoints |
| | `union-prometheus-cluster-read` (ClusterRole) | `list` and `watch` on nodes, `get` on `nodes/proxy` for cAdvisor, and `get` on the `/metrics` endpoint |
| `union-kube-state-metrics` | `union-kube-state-metrics-cluster-read` (ClusterRole) | `list` and `watch` on nodes and namespaces |
| | `union-kube-state-metrics` | `list` and `watch` on pods, deployments, daemonsets, and resource quotas. A Role in the release namespace by default, or a ClusterRole when kube-state-metrics collects from every namespace |

kube-state-metrics collects namespaced resources from the release namespace only
(`prometheus.kube-state-metrics.releaseNamespace: true`). In multi-namespace mode, tasks run in other namespaces, so
set it to `false` to include them. The chart widens the grant to a ClusterRole to match. See
[Multi-namespace mode](../kubernetes-rbac#multi-namespace-mode).

Leave the subcharts' own RBAC off. The chart refuses to render if any of these is set:

- `prometheus.rbac.create: true` or `prometheus.kube-state-metrics.rbac.create: true`
- `prometheus.kube-state-metrics.rbac.extraRules`
- `prometheus.kube-state-metrics.kubeRBACProxy.enabled`, `customResourceState.enabled`, or `autosharding.enabled`
- A templated entry in `prometheus.kube-state-metrics.namespaces`, in single-namespace mode

To collect another resource, add its collector to `prometheus.kube-state-metrics.collectors`. The chart grants the reads
for each collector it knows, and refuses one it has no rule for. If you add a scrape job of your own that discovers
targets outside the release namespace, create a Role for Prometheus in that namespace.

### Configuration

Configure the instance under `prometheus.server`, using the community chart's
[values](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus#configuration). The chart's
defaults:

```yaml
prometheus:
  server:
    retention: "3d"
    persistentVolume:
      enabled: false
    emptyDir:
      sizeLimit: "10Gi"
    resources:
      limits:
        cpu: "3"
        memory: "3500Mi"
      requests:
        cpu: "1"
        memory: "1Gi"
```

> [!NOTE] Retention and storage
> The data lives in an `emptyDir` volume and is lost when the pod is deleted or rescheduled. The 3-day retention is
> enough for Union.ai's features. Increase `retention`, and give the server a persistent volume, only if you query the
> metrics directly.

## Cluster health monitoring

To turn on operational monitoring with the Prometheus Operator, Grafana, and node-exporter:

```yaml
monitoring:
  enabled: true
```

This deploys [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
with these defaults:

- Prometheus with 7-day retention
- Grafana, with the admin password `admin`: set `monitoring.grafana.adminPassword` in production
- Node exporter, kubelet, kube-state-metrics, API server and CoreDNS monitoring. Etcd, scheduler, controller manager
  and kube-proxy monitoring are off.
- Default alerting and recording rules. Alertmanager is off.

### Prometheus Operator CRDs

The stack's Prometheus Operator discovers scrape targets and rules through CRDs (ServiceMonitor, PodMonitor,
PrometheusRule, and others). The chart doesn't install them (`monitoring.crds.enabled: false`), so apply them yourself,
with server-side apply, from the `helm-charts` repository at your chart version:

```shell
git clone --depth 1 --branch dataplane-<CHART_VERSION> https://github.com/unionai/helm-charts.git
kubectl apply --server-side --force-conflicts -f helm-charts/crds/kube-prometheus-stack/
```

> [!NOTE] Server-side apply for large CRDs
> The Prometheus Operator CRDs exceed the 256 KiB limit of the client-side `kubectl.kubernetes.io/last-applied-configuration`
> annotation. `kubectl apply --server-side --force-conflicts` avoids it.

### Union.ai monitoring resources

When the Prometheus Operator CRDs are installed, by this stack or by a Prometheus Operator you already run, the chart
also creates these resources in the release namespace, each labeled `release: <RELEASE>`. The PrometheusRules are
named after the release, for example `union-dataplane-dataplane-rules` for a release named `union`:

| Resource | What it is | Controlled by |
|----------|------------|---------------|
| ServiceMonitor `union-service-monitor` | Scrapes the Union.ai services on their `debug` port | `monitoring.serviceMonitors.enabled` (on) |
| ServiceMonitor `cost` | Scrapes OpenCost, when it runs | `monitoring.serviceMonitors.enabled` and `cost.enabled` (on) |
| PrometheusRule `…-dataplane-rules` | The cost and GPU recording rules | `monitoring.prometheusRules.enabled` and `cost.enabled` (on) |
| PrometheusRule `…-monitoring-rules` | Operational recording rules, plus alerts | `monitoring.prometheusRules.enabled` (on); alerts need `monitoring.alerting.enabled` (off), SLO rules `monitoring.slos.enabled` (off) |

The operational rules cover the health of the Union.ai services and pod scheduling.
`union:dp:pods_unschedulable:sum` counts the task pods that can't be scheduled, per namespace, and the
`UnionDPPodsUnschedulable` alert fires when a namespace has pods stuck Pending for 15 minutes, for example on
insufficient node capacity or a taint the pods don't tolerate. It's the main signal for "why are my task pods
Pending?". It reads `kube_pod_status_unschedulable`, which the stack's kube-state-metrics collects but the Union.ai
features instance drops.

The chart also ships Grafana dashboards as ConfigMaps labeled `grafana_dashboard: "1"`
(`monitoring.dashboards.enabled`, on), which the Grafana sidecar picks up.

### Customizing the monitoring stack

The `monitoring` key accepts all [kube-prometheus-stack values](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack#configuration).
Common overrides:

```yaml
monitoring:
  enabled: true

  # Grafana
  grafana:
    enabled: true
    adminPassword: "my-secure-password"
    ingress:
      enabled: true
      ingressClassName: nginx
      hosts:
        - grafana.example.com

  # Prometheus retention and resources
  prometheus:
    prometheusSpec:
      retention: 30d
      resources:
        requests:
          memory: "2Gi"

  # Alertmanager
  alertmanager:
    enabled: true
    # Configure receivers, routes, etc.
```

The stack's Prometheus supports [remote write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write)
for forwarding metrics to an external time-series database, such as Amazon Managed Prometheus, Grafana Cloud, or Thanos:

```yaml
monitoring:
  prometheus:
    prometheusSpec:
      remoteWrite:
        - url: "https://aps-workspaces.<REGION>.amazonaws.com/workspaces/<WORKSPACE_ID>/api/v1/remote_write"
          sigv4:
            region: <REGION>
```

## Scraping Union.ai services from your own Prometheus

If you already run Prometheus, you can scrape the Union.ai services for operational visibility. This adds to the
built-in instance; it doesn't replace it.

With the Prometheus Operator, you don't need to write anything: the chart's `union-service-monitor` ServiceMonitor
(see [Union.ai monitoring resources](#unionai-monitoring-resources)) selects the services. Make sure your Prometheus
selects ServiceMonitors in the data plane namespace, or with the label `release: <RELEASE>`.

Without it, add a static scrape job:

```yaml
scrape_configs:
  - job_name: union-dataplane-services
    kubernetes_sd_configs:
      - role: endpoints
        namespaces:
          names: [<NAMESPACE>]
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_label_platform_union_ai_prometheus_group]
        regex: union-services
        action: keep
      - source_labels: [__meta_kubernetes_endpoint_port_name]
        regex: debug
        action: keep
```

## Further reading

- [Prometheus documentation](https://prometheus.io/docs/introduction/overview/): configuration, querying, and operation
- [Prometheus remote write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write): forwarding metrics to external storage
- [Prometheus `kubernetes_sd_config`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config): Kubernetes service discovery for scrape targets
- [kube-prometheus-stack chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack): the full monitoring stack with Grafana and alerting

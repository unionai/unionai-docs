---
title: Monitoring
weight: 5
variants: -flyte +union
---

# Monitoring

The {{< key product_name >}} data plane deploys a static [Prometheus](https://prometheus.io/) instance that collects metrics required for platform features like cost tracking, task-level resource monitoring, and execution observability. This Prometheus instance is pre-configured and requires no additional setup.

For operational monitoring of the cluster itself (node health, API server metrics, CoreDNS, etc.), the data plane chart includes an optional [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) instance that can be enabled separately.

## Architecture overview

The data plane supports two independent monitoring concerns:

| Concern | What it monitors | How it's deployed | Configurable |
|---------|-----------------|-------------------|--------------|
| **Union features** | Task execution metrics, cost tracking, GPU utilization, container resources | Prometheus with pre-built scrape config (`prometheus` or `prometheus-simple`) | Retention, resources, scheduling |
| **Cluster health** (optional) | Kubernetes components, node health, alerting, Grafana dashboards | `kube-prometheus-stack` via `monitoring.enabled` | Full kube-prometheus-stack values |

The chart offers two Prometheus deployment options for Union features:

| Option | Helm key | CRDs required | Cluster-wide RBAC | Best for |
|--------|----------|--------------|-------------------|----------|
| **Static Prometheus** (default) | `prometheus` | No | Yes | Standard deployments |
| **Prometheus Simple** | `prometheus-simple` | No | No | Low-privilege / single-namespace deployments |

> [!NOTE] Mutual exclusivity
> `prometheus` and `prometheus-simple` cannot be enabled at the same time. The chart will fail validation if both are enabled.

```
                    ┌─────────────────────────────────────┐
                    │          Data plane cluster         │
                    │                                     │
                    │  ┌──────────────────────┐           │
                    │  │  Prometheus          │           │
                    │  │  (Union features)    │           │
                    │  │  ┌────────────────┐  │           │
                    │  │  │ Scrape targets │  │           │
                    │  │  │ - kube-state   │  │           │
                    │  │  │ - cAdvisor     │  │           │
                    │  │  │ - propeller    │  │           │
                    │  │  │ - opencost     │  │           │
                    │  │  │ - dcgm (GPU)   │  │           │
                    │  │  │ - envoy        │  │           │
                    │  │  └────────────────┘  │           │
                    │  └─────────────────────-┘           │
                    │                                     │
                    │  ┌──────────────────────┐           │
                    │  │  kube-prometheus     │           │
                    │  │  -stack (optional)   │           │
                    │  │  - Prometheus        │           │
                    │  │  - Alertmanager      │           │
                    │  │  - Grafana           │           │
                    │  │  - node-exporter     │           │
                    │  └──────────────────────┘           │
                    └─────────────────────────────────────┘
```

## Union features Prometheus

The static Prometheus instance is always deployed and pre-configured to scrape the metrics that {{< key product_name >}} requires. No Prometheus Operator or CRDs are needed. This instance is a platform dependency and should not be replaced or reconfigured.

### Scrape targets

The following targets are scraped automatically:

| Job | Target | Metrics collected |
|-----|--------|------------------|
| `kube-state-metrics` | Pod/node resource requests, limits, status, capacity | Cost calculations, resource tracking |
| `kubernetes-cadvisor` | Container CPU and memory usage via kubelet | Task-level resource monitoring |
| `flytepropeller` | Execution round info, fast task duration | Execution observability |
| `opencost` | Node hourly cost rates (CPU, RAM, GPU) | Cost tracking |
| `gpu-metrics` | DCGM exporter metrics (when `dcgm-exporter.enabled`) | GPU utilization |
| `serving-envoy` | Envoy upstream request counts and latency (when `serving.enabled`) | Inference serving metrics |

### Configuration

The static Prometheus instance is configured under the `prometheus` key in your data plane values:

```yaml
prometheus:
  image:
    repository: prom/prometheus
    tag: v3.3.1
  # Data retention period
  retention: 3d
  # Route prefix for the web UI and API
  routePrefix: /prometheus/
  resources:
    limits:
      cpu: "3"
      memory: "3500Mi"
    requests:
      cpu: "1"
      memory: "1Gi"
  serviceAccount:
    create: true
    annotations: {}
  priorityClassName: system-cluster-critical
  nodeSelector: {}
  tolerations: []
  affinity: {}
```

> [!NOTE] Retention and storage
> The default 3-day retention is sufficient for {{< key product_name >}} features. Increase `retention` if you query historical feature metrics directly.

### Internal service endpoint

Other data plane components reach Prometheus at:

```
http://union-operator-prometheus.<NAMESPACE>.svc:80/prometheus
```

OpenCost is pre-configured to use this endpoint. You do not need to change it unless you rename the Helm release.

## Prometheus simple (low-privilege mode)

For deployments that cannot use cluster-wide RBAC (e.g., single-namespace or low-privilege mode), enable `prometheus-simple` instead of the default static Prometheus:

```yaml
prometheus:
  enabled: false
prometheus-simple:
  enabled: true
  rbac:
    create: false  # Namespace-scoped Role is created by the dataplane chart
  kube-state-metrics:
    enabled: true
    rbac:
      useClusterRole: false
    releaseNamespace: true
```

This deploys a standalone Prometheus instance with namespace-scoped RBAC. The dataplane chart creates the necessary Role and RoleBinding automatically.

> [!NOTE] Node-level metrics
> In low-privilege mode, kube-state-metrics only watches the release namespace. Pod-level metrics (`kube_pod_*`, `kube_pod_container_*`) are available, but node-level metrics (`kube_node_*`) are not, since nodes are cluster-scoped resources.

### Recording rules

The chart includes pre-built recording rules for cost tracking and execution observability (GPU allocation, execution metadata, workspace metrics). These rules are:

- Embedded in a `PrometheusRule` when using `kube-prometheus-stack`
- Embedded in a ConfigMap when using `prometheus-simple`
- Only enabled when `cost.enabled: true` and the deployment is not in low-privilege mode

## Enabling cluster health monitoring

To enable operational monitoring with Prometheus Operator, Alertmanager, Grafana, and node-exporter:

```yaml
monitoring:
  enabled: true
```

This deploys a full [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) instance with sensible defaults:

- Prometheus with 7-day retention
- Grafana with admin credentials (override `monitoring.grafana.adminPassword` in production)
- Node exporter, kube-state-metrics, kubelet, CoreDNS, API server, etcd, and scheduler monitoring
- Default alerting and recording rules

### Prometheus Operator CRDs

The `kube-prometheus-stack` uses the Prometheus Operator, which discovers scrape targets and alerting rules through Kubernetes CRDs (ServiceMonitor, PodMonitor, PrometheusRule, etc.). If you prefer to use static scrape configs with your own Prometheus instead, see [Scraping Union services from your own Prometheus](#scraping-union-services-from-your-own-prometheus).

To install the CRDs, use the `dataplane-crds` chart:

```yaml
# dataplane-crds values
crds:
  flyte: true
  prometheusOperator: true  # Install Prometheus Operator CRDs
```

Then install or upgrade the CRDs chart before the data plane chart:

```shell
helm upgrade --install union-dataplane-crds unionai/dataplane-crds \
  --namespace union \
  --set crds.prometheusOperator=true
```

> [!NOTE] CRD installation order
> CRDs must be installed before the data plane chart. The `dataplane-crds` chart should be deployed first, and the monitoring stack's own CRD installation is disabled (`monitoring.crds.enabled: false`) to avoid conflicts.

### Customizing the monitoring stack

The monitoring stack accepts all [kube-prometheus-stack values](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack#configuration) under the `monitoring` key. Common overrides:

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

The monitoring stack's Prometheus supports [remote write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) for forwarding metrics to external time-series databases (Amazon Managed Prometheus, Grafana Cloud, Thanos, etc.):

```yaml
monitoring:
  prometheus:
    prometheusSpec:
      remoteWrite:
        - url: "https://aps-workspaces.<REGION>.amazonaws.com/workspaces/<WORKSPACE_ID>/api/v1/remote_write"
          sigv4:
            region: <REGION>
```

For the full set of configurable values, see the [kube-prometheus-stack chart documentation](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack).

## Dashboards and operational alerts

The {{< key product_name >}} charts ship Grafana dashboards (rendered by default via `monitoring.dashboards.enabled`) and a set of alert rules that are **off by default** and enabled with `monitoring.alerting.enabled: true`. Two operational signals are worth calling out because they are easy to miss on resource-usage graphs alone: **project ResourceQuota saturation** and **stuck runs**.

### ResourceQuota utilization

Each {{< key product_name >}} project namespace is created with a `project-quota` `ResourceQuota` that caps `limits.cpu`, `limits.memory`, and `requests.nvidia.com/gpu`. When a namespace reaches its quota, Kubernetes rejects further pod creation with `exceeded quota`, and runs scheduled into that namespace stop starting until capacity frees up. On a shared cluster this can back-pressure execution for other projects.

`kube-state-metrics` already exports the underlying `kube_resourcequota` series (labels `namespace`, `resource`, and `type`, where `type` is `hard` or `used`), so no extra configuration is required. The data plane overview dashboard includes a **ResourceQuota utilization** row showing per-namespace utilization, the most-saturated quotas, and a count of namespaces at or above 90%. Utilization for a single resource is:

```promql
kube_resourcequota{type="used"} / ignoring(type) kube_resourcequota{type="hard"}
```

When alerting is enabled, `UnionDPResourceQuotaNearSaturation` fires when any project quota stays at or above 90% for 10 minutes:

```promql
max by (namespace, resource) (
  kube_resourcequota{type="used"} / ignoring(type) kube_resourcequota{type="hard"}
) >= 0.9
```

> [!NOTE] Raising a saturated quota
> ResourceQuota limits are set per project. If a project legitimately needs more capacity, raise its quota; if a single task is over-requesting, reduce its per-task CPU or memory requests. Quota saturation is a scheduling limit, not a failure — runs resume once usage drops below the cap.

### Stuck-run diagnostics

For deployments on the actions/leasor execution path, the control plane overview dashboard includes a **leasor stuck-run diagnostics** row. The primary signal is `leases_by_state`: run-actions waiting in `unassigned` mean the scheduler has accepted work but no worker has taken it, while a growing `sent` count means work was dispatched but is not completing. The row also surfaces the scheduler's skip reasons (`schedule_skip_total`), dispatch throughput (`dispatch_total`), per-queue run-slot saturation (`queue_active_runs` versus `queue_max_run_concurrency`), and enqueue routing rejects (`enqueue_reject_total`).

When alerting is enabled, two alerts accompany this row:

- `UnionCPLeasorRunsStuck` — run-actions are waiting in `unassigned` while the successful dispatch rate has been zero for 10 minutes.
- `UnionCPLeasorEnqueueRejects` — sustained enqueue rejects, usually a client targeting a queue that is unregistered, draining, or missing a cluster selector.

## Scraping Union services from your own Prometheus

If you already run Prometheus in your cluster, you can scrape {{< key product_name >}} data plane services for operational visibility. All services expose metrics on standard ports.

> [!NOTE] Union features Prometheus
> The built-in static Prometheus handles all metrics required for {{< key product_name >}} platform features. Scraping from your own Prometheus is for additional operational visibility only -- it does not replace the built-in instance.

### Static scrape configs

Add these jobs to your Prometheus configuration:

```yaml
scrape_configs:
  # Data plane service metrics (operator, propeller, etc.)
  - job_name: union-dataplane-services
    kubernetes_sd_configs:
      - role: endpoints
        namespaces:
          names: [union]
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_label_app_kubernetes_io_instance]
        regex: union-dataplane
        action: keep
      - source_labels: [__meta_kubernetes_endpoint_port_name]
        regex: debug
        action: keep
```

### ServiceMonitor (Prometheus Operator)

If you run the Prometheus Operator, create a ServiceMonitor instead:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: union-dataplane-services
  namespace: union
spec:
  selector:
    matchLabels:
      app.kubernetes.io/instance: union-dataplane
  namespaceSelector:
    matchNames:
      - union
  endpoints:
    - port: debug
      path: /metrics
      interval: 30s
```

This requires the Prometheus Operator CRDs. Install them via the `dataplane-crds` chart with `crds.prometheusOperator: true`.

## Further reading

- [Prometheus documentation](https://prometheus.io/docs/introduction/overview/) -- guide to Prometheus configuration, querying, and operation
- [Prometheus remote write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) -- forwarding metrics to external storage
- [Prometheus `kubernetes_sd_config`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config) -- Kubernetes service discovery for scrape targets
- [kube-prometheus-stack chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) -- full monitoring stack with Grafana and alerting
- [OpenCost documentation](https://www.opencost.io/docs/) -- cost allocation and tracking

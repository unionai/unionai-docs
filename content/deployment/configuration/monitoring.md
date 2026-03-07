---
title: Monitoring
weight: 5
variants: -flyte -byoc +selfmanaged
---

# Monitoring

The {{< key product_name >}} data plane deploys a static [Prometheus](https://prometheus.io/) instance that collects metrics required for platform features like cost tracking, task-level resource monitoring, and execution observability. This Prometheus instance is pre-configured and requires no additional setup.

For operational monitoring of the cluster itself (node health, API server metrics, CoreDNS, etc.), the data plane chart includes an optional [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) instance that can be enabled separately.

## Architecture overview

The data plane supports two independent monitoring concerns:

| Concern | What it monitors | How it's deployed | Configurable |
|---------|-----------------|-------------------|--------------|
| **Union features** | Task execution metrics, cost tracking, GPU utilization, container resources | Static Prometheus with pre-built scrape config | Retention, resources, scheduling |
| **Cluster health** (optional) | Kubernetes components, node health, alerting, Grafana dashboards | `kube-prometheus-stack` via `monitoring.enabled` | Full kube-prometheus-stack values |

```
                    ┌─────────────────────────────────────┐
                    │          Data Plane Cluster          │
                    │                                     │
                    │  ┌──────────────────────┐           │
                    │  │  Static Prometheus   │           │
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
                    │  └──────────┬───────────┘           │
                    │             │ remote_write (opt.)   │
                    │             ▼                       │
                    │     External TSDB / Cloud           │
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

The static Prometheus instance is always deployed and pre-configured to scrape the metrics that {{< key product_name >}} requires. No Prometheus Operator or CRDs are needed.

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
    # Add annotations for IRSA or Workload Identity if using remote_write
    # to a cloud-managed service (e.g. Amazon Managed Prometheus)
    annotations: {}
  priorityClassName: system-cluster-critical
  nodeSelector: {}
  tolerations: []
  affinity: {}
```

> [!NOTE] Retention and storage
> The default 3-day retention is sufficient for {{< key product_name >}} features. Increase `retention` if you query historical feature metrics directly. For long-term storage, use [remote write](#exporting-metrics-with-remote-write) to an external time-series database.

### Internal service endpoint

Other data plane components reach Prometheus at:

```
http://union-operator-prometheus.<NAMESPACE>.svc:80/prometheus
```

OpenCost is pre-configured to use this endpoint. You do not need to change it unless you rename the Helm release.

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

The `kube-prometheus-stack` uses the Prometheus Operator, which discovers scrape targets and alerting rules through Kubernetes CRDs (ServiceMonitor, PodMonitor, PrometheusRule, etc.). If you prefer to use static scrape configs instead, see [Integrating with your own Prometheus](#integrating-with-your-own-prometheus).

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

For the full set of configurable values, see the [kube-prometheus-stack chart documentation](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack).

## Integrating with your own Prometheus

If you already run Prometheus in your cluster, you can scrape {{< key product_name >}} services directly without enabling the monitoring stack. All data plane services expose metrics on standard ports.

### Using static scrape configs

Add the following jobs to your Prometheus configuration to collect the same metrics that {{< key product_name >}} features require:

```yaml
scrape_configs:
  # Kube-state-metrics for pod/node resource tracking
  - job_name: union-kube-state-metrics
    static_configs:
      - targets: ['union-dataplane-kube-state-metrics:8080']
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: "kube_pod_container_resource_(limits|requests)|kube_pod_status_phase|kube_node_(labels|status_allocatable|status_condition|status_capacity)|kube_namespace_labels|kube_pod_info|kube_node_info|kube_pod_container_status_restarts_total"
        action: keep

  # Flytepropeller execution metrics
  - job_name: union-flytepropeller
    kubernetes_sd_configs:
      - role: pod
        namespaces:
          names: [union]
        selectors:
          - role: pod
            label: "app.kubernetes.io/name=flytepropeller"
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_container_name]
        regex: flytepropeller
        action: keep

  # OpenCost (when cost tracking is enabled)
  - job_name: union-opencost
    static_configs:
      - targets: ['union-dataplane-opencost:9003']
```

> [!NOTE] Service names
> The target hostnames above assume a Helm release name of `union-dataplane`. Adjust the prefix if your release name differs.

### Using Prometheus Operator ServiceMonitors

If you run the Prometheus Operator, you can create ServiceMonitor resources instead of static configs. First, install the Prometheus Operator CRDs via the `dataplane-crds` chart:

```yaml
# dataplane-crds values
crds:
  prometheusOperator: true
```

Then create ServiceMonitor resources to discover {{< key product_name >}} services. For example, to scrape all data plane services that expose a `debug` port:

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

For the full list of metrics ports and paths, see the [Prometheus operator documentation on ServiceMonitor](https://prometheus-operator.dev/docs/api-reference/api/#monitoring.coreos.com/v1.ServiceMonitor).

## Exporting metrics with remote write

For long-term metric storage or integration with managed monitoring services, configure Prometheus [remote write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) to forward metrics to an external time-series database.

### Overview

Remote write allows the static Prometheus instance to push metrics to external systems while continuing to serve {{< key product_name >}} features locally. Common destinations include:

- [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)
- [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus)
- [Azure Monitor managed service for Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview)
- [Grafana Cloud](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/prometheus/)
- Any [Prometheus remote write compatible](https://prometheus.io/docs/concepts/remote_write_spec/) endpoint (Thanos, Cortex, VictoriaMetrics, etc.)

### Configuration

Remote write is configured by adding a `remote_write` section to the Prometheus ConfigMap. Create a values override file:

```yaml
prometheus:
  # Extend the static config with remote_write
  additionalConfig: |
    remote_write:
      - url: "https://aps-workspaces.<REGION>.amazonaws.com/workspaces/<WORKSPACE_ID>/api/v1/remote_write"
        sigv4:
          region: <REGION>
        queue_config:
          max_samples_per_send: 1000
          max_shards: 200
          capacity: 2500
```

> [!WARNING] Remote write is not yet configurable via Helm values
> The static Prometheus ConfigMap does not currently support `additionalConfig`. To add remote write, create a ConfigMap overlay or patch the rendered ConfigMap after deployment. A future chart release will add first-class support for remote write configuration.

As a workaround, you can patch the ConfigMap directly:

```shell
kubectl get configmap union-operator-prometheus -n union -o yaml > prometheus-config.yaml
# Edit prometheus-config.yaml to add remote_write under the global section
kubectl apply -f prometheus-config.yaml
```

> [!NOTE] Prometheus will reload configuration automatically
> The static Prometheus deployment uses a `configChecksum` annotation that triggers a rollout when the ConfigMap changes via Helm. For manual ConfigMap patches, send a reload signal: `kubectl exec -n union deploy/union-operator-prometheus -- kill -HUP 1`

For detailed remote write configuration options, see the [Prometheus remote write documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write).

### AWS Managed Prometheus example

To write to Amazon Managed Service for Prometheus (AMP), the Prometheus service account needs `aps:RemoteWrite` permissions via IRSA:

```yaml
prometheus:
  serviceAccount:
    annotations:
      eks.amazonaws.com/role-arn: "arn:aws:iam::<ACCOUNT_ID>:role/<PROMETHEUS_AMP_ROLE>"
```

Then patch the ConfigMap to add:

```yaml
remote_write:
  - url: "https://aps-workspaces.<REGION>.amazonaws.com/workspaces/<WORKSPACE_ID>/api/v1/remote_write"
    sigv4:
      region: <REGION>
```

See [Ingesting data with remote write for AMP](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-remote-write.html) for IAM policy details.

## Further reading

- [Prometheus documentation](https://prometheus.io/docs/introduction/overview/) -- comprehensive guide to Prometheus configuration, querying, and operation
- [Prometheus remote write configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) -- all remote write options
- [Prometheus `kubernetes_sd_config`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config) -- Kubernetes service discovery for custom scrape targets
- [kube-prometheus-stack chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) -- full monitoring stack with Grafana and alerting
- [OpenCost documentation](https://www.opencost.io/docs/) -- cost allocation and tracking

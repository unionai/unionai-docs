---
title: Monitoring
weight: 5
variants: -flyte -byoc +selfmanaged
---
# Monitoring

{{< variant selfhosted >}}

> [!NOTE] Self-hosted deployments
> If you are running a [self-hosted deployment](../selfhosted-deployment/monitoring), monitoring is pre-configured with Grafana dashboards and alerting. See the [self-hosted monitoring guide](../selfhosted-deployment/monitoring) for setup details.
> {{< /variant >}}

The {{< key product_name >}} data plane deploys a static [Prometheus](https://prometheus.io/) instance that collects metrics required for platform features like cost tracking, task-level resource monitoring, and execution observability. This Prometheus instance is pre-configured and requires no additional setup.

For operational monitoring of the cluster itself (node health, API server metrics, CoreDNS, etc.), the data plane chart includes an optional [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) instance that can be enabled separately.

## Architecture overview

The data plane supports two independent monitoring concerns:

| Concern                             | What it monitors                                                            | How it's deployed                                    | Configurable                      |
| ----------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------- |
| **Union features**            | Task execution metrics, cost tracking, GPU utilization, container resources | Static Prometheus with pre-built scrape config       | Retention, resources, scheduling  |
| **Cluster health** (optional) | Kubernetes components, node health, alerting, Grafana dashboards            | `kube-prometheus-stack` via `monitoring.enabled` | Full kube-prometheus-stack values |

```
                    ┌─────────────────────────────────────┐
                    │          Data Plane Cluster         │
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

| Job                     | Target                                                               | Metrics collected                    |
| ----------------------- | -------------------------------------------------------------------- | ------------------------------------ |
| `kube-state-metrics`  | Pod/node resource requests, limits, status, capacity                 | Cost calculations, resource tracking |
| `kubernetes-cadvisor` | Container CPU and memory usage via kubelet                           | Task-level resource monitoring       |
| `flytepropeller`      | Execution round info, fast task duration                             | Execution observability              |
| `opencost`            | Node hourly cost rates (CPU, RAM, GPU)                               | Cost tracking                        |
| `gpu-metrics`         | DCGM exporter metrics (when `dcgm-exporter.enabled`)               | GPU utilization                      |
| `serving-envoy`       | Envoy upstream request counts and latency (when `serving.enabled`) | Inference serving metrics            |

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

## Dashboards

When `monitoring.enabled` is `true`, a pre-built Grafana dashboard is included:

- **Dataplane Overview** — operator health, executor status, propeller performance, K8s API health, infrastructure metrics

The dashboard is delivered as a ConfigMap with the `grafana_dashboard: "1"` label, auto-discovered by the Grafana sidecar.

To add custom dashboards, create a ConfigMap with the same label in the data plane namespace:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-custom-dashboard
  labels:
    grafana_dashboard: "1"
data:
  my-dashboard.json: |
    { ... Grafana dashboard JSON ... }
```

## Service Level Objectives (SLOs)

The SLO dashboard row provides at-a-glance visibility into dataplane health using four key indicators.

| SLO                              | What it represents                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Service Availability**   | Are all deployments running their desired replica count? Measures infrastructure health.                            |
| **Execution Success Rate** | Are task executions completing without errors? Combines V1 propeller round success and V2 executor task completion. |
| **Latency**                | Propeller round p99 — the worst-case time to process one workflow reconciliation.                                  |
| **Error Budget**           | How much room is left before the availability target is breached? Derived from execution success rate vs target.    |

To enable SLO recording rules and error budget tracking:

```yaml
monitoring:
  slos:
    enabled: true
    targets:
      availability: 0.999   # 99.9% — adjust to your requirements
      latencyP99: 5          # seconds — adjust to your requirements
```

These are recommended starting points — tune the targets based on your traffic patterns and performance baseline.

## Alerting

{{< key product_name >}} includes two layers of alerting that you can enable independently.

### Operational alerts

Operational alerts detect basic infrastructure failures. Enable them in your data plane values:

```yaml
monitoring:
  alerting:
    enabled: true
```

| Alert           | Severity | Fires when                                        |
| --------------- | -------- | ------------------------------------------------- |
| ServiceDown     | critical | Any deployment has 0 available replicas for 5 min |
| HighRestartRate | warning  | A container restarts more than 5 times in 1 hour  |
| HandlerPanic    | critical | Any service handler panic in the last hour        |

### SLO-based alerts

SLO alerts track error budget consumption and latency against configurable targets. These are provided as recommended starting points — adjust the targets and thresholds to match your operational requirements.

```yaml
monitoring:
  slos:
    enabled: true
    alerting:
      enabled: true
    targets:
      availability: 0.999   # 99.9% — adjust to your requirements
      latencyP99: 5          # seconds — adjust to your requirements
```

| Alert                     | Severity | Fires when                                        |
| ------------------------- | -------- | ------------------------------------------------- |
| HighErrorBudgetBurn       | warning  | Error budget more than 50% consumed               |
| ErrorBudgetExhausted      | critical | Error budget fully consumed                       |
| PropellerLatencySLOBreach | warning  | Propeller p99 latency exceeding target for 10 min |

> [!NOTE]
> The default SLO targets (99.9% availability, 5s p99 latency) are starting points. Every deployment has different traffic patterns and performance characteristics. Review the SLO dashboard panels after enabling to understand your baseline, then tune the targets to values that are meaningful for your environment.

### Configuring notifications

By default, alerts are evaluated but do not send notifications. To receive notifications, configure AlertManager with a receiver:

```yaml
monitoring:
  alertmanager:
    enabled: true
    config:
      route:
        receiver: my-slack
      receivers:
        - name: my-slack
          slack_configs:
            - api_url: "https://hooks.slack.com/services/..."
              channel: "#alerts"
```

If you have Grafana enabled, alerts are also visible under **Alerting → Alert rules** via the Alertmanager datasource.

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

## Independent monitoring resources

{{< key product_name >}} creates ServiceMonitors, PrometheusRules, and Grafana dashboard ConfigMaps independently of the `monitoring.enabled` flag. This means you can use these resources with your own Prometheus and Grafana without deploying the full kube-prometheus-stack.

These flags default to `true`:

```yaml
monitoring:
  # Create ServiceMonitor CRDs for Union services.
  # Your Prometheus Operator discovers these automatically.
  serviceMonitors:
    enabled: true

  # Create PrometheusRule CRDs with recording rules.
  # Enable monitoring.alerting.enabled for alerting rules.
  prometheusRules:
    enabled: true

  # Create dashboard ConfigMaps discovered by Grafana sidecar.
  # Configure label/labelValue to match your Grafana sidecar settings.
  dashboards:
    enabled: true
    label: grafana_dashboard
    labelValue: "1"

  # Opt-in alerting rules (requires AlertManager).
  alerting:
    enabled: false
```

Set any of these to `false` to disable that resource type. These flags work whether `monitoring.enabled` is `true` or `false`.

## Further reading

- [Prometheus documentation](https://prometheus.io/docs/introduction/overview/) -- comprehensive guide to Prometheus configuration, querying, and operation
- [Prometheus remote write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) -- forwarding metrics to external storage
- [Prometheus `kubernetes_sd_config`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config) -- Kubernetes service discovery for scrape targets
- [kube-prometheus-stack chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) -- full monitoring stack with Grafana and alerting
- [OpenCost documentation](https://www.opencost.io/docs/) -- cost allocation and tracking

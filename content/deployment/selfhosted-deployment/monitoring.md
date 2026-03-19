---
title: Monitoring
weight: 8
variants: -flyte -serverless -byoc +selfmanaged
---

# Monitoring

In a self-hosted deployment, monitoring is enabled by default. The controlplane deploys Prometheus, Grafana, and AlertManager. Prometheus scrapes services across both the controlplane and dataplane namespaces.

{{< key product_name >}} also deploys a separate static Prometheus instance in the dataplane for platform features (cost tracking, task-level resource monitoring). This instance is pre-configured and requires no setup. See the [self-managed monitoring configuration](../configuration/monitoring) for details on the static Prometheus.

```
┌──────────────────────────────────────────────────────────┐
│                    Kubernetes Cluster                      │
│                                                            │
│  controlplane namespace              dataplane namespace   │
│  ┌───────────────────┐               ┌──────────────────┐ │
│  │  Prometheus       │──── scrapes ──│  Union Operator   │ │
│  │  (monitoring)     │               │  Executor (V2)    │ │
│  │                   │               │  Propeller (V1)   │ │
│  │  Grafana          │               │  ServiceMonitor   │ │
│  │  AlertManager     │               │  PrometheusRule   │ │
│  │                   │               │  Dashboard CM     │ │
│  │  FlyteAdmin       │               └──────────────────┘ │
│  │  Executions       │                                     │
│  │  Queue            │               ┌──────────────────┐ │
│  │  Cluster          │               │  Static Prometheus│ │
│  │  Authorizer       │               │  (Union features) │ │
│  │  ...              │               │  (pre-configured) │ │
│  └───────────────────┘               └──────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

## Accessing Grafana

Grafana is available at:

```
https://<your-domain>/grafana
```

Authentication is handled by the same ingress auth gate as other controlplane services. No separate Grafana credentials are needed.

## Dashboards

Two dashboards are pre-installed:

### Controlplane Overview

Service health and performance for all controlplane services:

| Row | What it shows |
|-----|---------------|
| Health | Service availability, pod restarts, Connect error rate, handler panics |
| Ingress | Request rate by path, error rate, latency percentiles, active connections |
| Connect / gRPC | Per-service request rate and errors, CacheService gRPC |
| FlyteAdmin | Active executions, event rates, endpoint latency, auth decisions |
| Executions | Execution lifecycle, assignment duration, workqueue operations |
| Queue | Scheduler throughput, queue lengths, dispatcher operations, worker capacity |
| Cluster | Heartbeat rate, cluster health, managed cluster cache |
| CacheService | Cache hit/miss rate, reservation contention |
| Authorizer | Allow/deny rate, authorize latency |
| Data Proxy | Cache rates, image read latency, secret proxy errors |
| Usage | Billable usage reports, message pipeline |
| Infrastructure | CPU, memory, and pod restarts by service |

### Dataplane Overview

Execution engine health and performance:

| Row | What it shows |
|-----|---------------|
| Health | Service availability, active workflows, queue depth, handler panics |
| Union Operator | Work queue operations, heartbeat latency, config sync, billing |
| Executor (V2) | Active actions, capacity, evaluator latency, system failures |
| Propeller (V1) | Round time, success/error rate, workflow updates, event recording |
| gRPC Client | DP→CP request rate, errors, latency |
| Infrastructure | CPU, memory, and pod restarts by service |

### Adding custom dashboards

Create a ConfigMap with the `grafana_dashboard` label in any namespace. The Grafana sidecar discovers it automatically:

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

To use a different label, set `monitoring.dashboards.label` and `monitoring.dashboards.labelValue` in your Helm values.

## Alerting

{{< key product_name >}} includes two layers of alerting that you can enable independently.

### Operational alerts

Operational alerts detect basic infrastructure failures — services that are down, containers that are crashlooping, or code panics. Enable them in your values:

```yaml
monitoring:
  alerting:
    enabled: true
```

| Alert | Severity | Fires when |
|-------|----------|------------|
| ServiceDown | critical | Any deployment has 0 available replicas for 5 min |
| HighRestartRate | warning | A container restarts more than 5 times in 1 hour |
| HandlerPanic | critical | Any service handler panic in the last hour |

These alerts fire on both the controlplane and dataplane.

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

| Alert | Severity | Fires when |
|-------|----------|------------|
| HighErrorBudgetBurn | warning | Error budget more than 50% consumed |
| ErrorBudgetExhausted | critical | Error budget fully consumed |
| LatencySLOBreach | warning | p99 latency exceeding target for 10 min |

> [!NOTE]
> The default SLO targets (99.9% availability, 5s p99 latency) are starting points. Every deployment has different traffic patterns and performance characteristics. Review the SLO dashboard panels after enabling to understand your baseline, then tune the targets to values that are meaningful for your environment.

### Viewing alerts

Alerts are visible in Grafana under **Alerting → Alert rules**. Grafana discovers alerts from AlertManager automatically via the Alertmanager datasource.

### Configuring notifications

By default, alerts are evaluated and visible in Grafana but do not send notifications. To receive notifications when alerts fire:

1. Open Grafana at `https://<your-domain>/grafana`
2. Navigate to **Alerting → Contact points**
3. Click **Add contact point**
4. Select your notification channel (Slack, PagerDuty, email, etc.) and configure it
5. Under **Alerting → Notification policies**, route alerts to your contact point

Alternatively, configure AlertManager receivers directly in your Helm values:

```yaml
monitoring:
  alertmanager:
    config:
      route:
        receiver: my-slack
      receivers:
        - name: my-slack
          slack_configs:
            - api_url: "https://hooks.slack.com/services/..."
              channel: "#alerts"
```

## Independent monitoring resources

ServiceMonitors, PrometheusRules, and dashboard ConfigMaps are created independently of the kube-prometheus-stack. This is useful if you want to use your own Prometheus or Grafana instead of the built-in stack:

```yaml
monitoring:
  serviceMonitors:
    enabled: true       # ServiceMonitor CRDs for Union services
  prometheusRules:
    enabled: true       # Recording rules + alerting rules
  dashboards:
    enabled: true       # Grafana dashboard ConfigMaps
    label: grafana_dashboard
    labelValue: "1"
```

These flags default to `true` and work regardless of whether `monitoring.enabled` is set.

## Remote write

Forward metrics to an external time-series database (Amazon Managed Prometheus, Grafana Cloud, Thanos) by configuring remote write in your controlplane values:

```yaml
monitoring:
  prometheus:
    prometheusSpec:
      remoteWrite:
        - url: "https://aps-workspaces.<REGION>.amazonaws.com/workspaces/<ID>/api/v1/remote_write"
          sigv4:
            region: <REGION>
```

## Using your own Prometheus

If you already run Prometheus, scrape {{< key product_name >}} services directly. All services expose metrics on port 10254 at `/metrics`.

### ServiceMonitor

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: union-services
spec:
  selector:
    matchLabels:
      platform.union.ai/prometheus-group: "union-services"
  namespaceSelector:
    matchNames:
      - controlplane
      - dataplane
  endpoints:
    - port: debug
      path: /metrics
      interval: 30s
```

### Static scrape config

```yaml
scrape_configs:
  - job_name: union-services
    kubernetes_sd_configs:
      - role: endpoints
        namespaces:
          names: [controlplane, dataplane]
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_label_platform_union_ai_prometheus_group]
        regex: union-services
        action: keep
      - source_labels: [__meta_kubernetes_endpoint_port_name]
        regex: debug
        action: keep
```

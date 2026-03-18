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

### Enabling alerts

Enable alerting rules in your data plane values:

```yaml
monitoring:
  alerting:
    enabled: true
```

AlertManager forwards alerts to Grafana's built-in alerting system. Alerts appear in Grafana under **Alerting → Alert rules**.

### Alert rules

| Alert | Severity | Fires when |
|-------|----------|------------|
| ServiceDown | critical | Any deployment has 0 available replicas |
| HighRestartRate | warning | > 5 container restarts in 1 hour |
| HighConnectErrorRate (CP) | warning | Connect RPC error rate > 5% for 10 min |
| IngressHighLatency (CP) | warning | Ingress p99 latency > 5s for 10 min |
| Ingress5xxRate (CP) | warning | Ingress 5xx rate > 1% for 5 min |
| ExecutionsDBErrors (CP) | warning | Postgres errors > 0.1/s for 10 min |
| QueueDispatcherBacklog (CP) | warning | Dispatcher backlog > 100 for 15 min |
| PropellerRoundLatencyHigh (DP) | warning | Propeller round p99 > 5s for 10 min |
| PropellerQueueBacklog (DP) | warning | Propeller queue depth > 100 for 10 min |
| OperatorWorkQueueErrors (DP) | warning | Work queue failure rate > 0.1/s for 10 min |
| PropellerRoundErrors (DP) | warning | Round error rate > 10% for 10 min |
| PropellerWfUpdateFailures (DP) | warning | etcd write failures > 0.1/s for 10 min |
| HandlerPanic (CP + DP) | critical | Any handler panic in the last hour |

### Configuring notifications

To receive alert notifications (Slack, PagerDuty, email, etc.):

1. Open Grafana at `https://<your-domain>/grafana`
2. Navigate to **Alerting → Contact points**
3. Click **Add contact point**
4. Select your notification channel and configure it
5. Under **Alerting → Notification policies**, route alerts to your contact point

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

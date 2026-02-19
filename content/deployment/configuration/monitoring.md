---
title: Monitoring
weight: 5
variants: -flyte -serverless -byoc +selfmanaged
---

# Monitoring

The {{< key product_name >}} data plane ships with two separate [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) instances, each with a distinct responsibility:

| Instance | Helm key | Purpose | User-configurable |
|---|---|---|---|
| Union features | `prometheus` | Powers Task Level Monitoring (TLM), cost tracking, and app metrics. | No — managed automatically. |
| Monitoring | `monitoring` | General cluster and service observability. | Yes — this page covers configuration. |

The two instances are isolated through Prometheus Operator CRD label selectors using the `platform.union.ai/prometheus-group` label. The Union features instance only scrapes CRDs labeled `union-features`, while the monitoring instance scrapes everything *except* `union-features`.

{{< note >}}
The Union features Prometheus is required for platform functionality and cannot be disabled. It is fully self-contained and requires no user configuration.
{{< /note >}}

## Default configuration

The monitoring stack is enabled by default (`monitoring.enabled: true`) and deploys:

- **Prometheus** — scrapes Kubernetes component metrics and Union service health metrics (7-day retention)
- **Grafana** — pre-configured with kube-prometheus-stack dashboards
- **kube-state-metrics** — Kubernetes object state metrics
- **node-exporter** — host-level metrics
- **ServiceMonitors** for API server, kubelet, CoreDNS, etcd, kube-proxy, and kube-scheduler

The default Grafana credentials are `admin` / `admin`. Override them in production:

```yaml
monitoring:
  grafana:
    adminPassword: "<your-password>"
```

To access Grafana, port-forward to the service:

```bash
kubectl port-forward svc/union-monitoring-grafana -n <namespace> 3000:80
```

Then open `http://localhost:3000` in your browser.

## Forwarding metrics to an external destination

If you already operate a central monitoring platform (Grafana Cloud, Thanos, Mimir, VictoriaMetrics, or any Prometheus-compatible remote write endpoint), configure the monitoring Prometheus to forward metrics using `remoteWrite`.

### Grafana Cloud

```yaml
monitoring:
  prometheus:
    prometheusSpec:
      remoteWrite:
        - url: "https://prometheus-prod-01-prod-us-east-0.grafana.net/api/prom/push"
          basicAuth:
            username:
              name: grafana-cloud-credentials
              key: username
            password:
              name: grafana-cloud-credentials
              key: password
```

Create the secret beforehand:

```bash
kubectl create secret generic grafana-cloud-credentials \
  -n <namespace> \
  --from-literal=username="<grafana-cloud-user-id>" \
  --from-literal=password="<grafana-cloud-api-key>"
```

### Generic remote write endpoint

```yaml
monitoring:
  prometheus:
    prometheusSpec:
      remoteWrite:
        - url: "https://your-prometheus-endpoint/api/v1/write"
          # Optional: add authentication headers
          # headers:
          #   Authorization: "Bearer <token>"
```

### Agent mode (write-only)

If you only need to forward metrics and do not need local querying, enable Prometheus agent mode. This reduces resource usage by disabling the local TSDB:

```yaml
monitoring:
  prometheus:
    agentMode: true
    prometheusSpec:
      remoteWrite:
        - url: "https://your-prometheus-endpoint/api/v1/write"
```

{{< note >}}
When agent mode is enabled, the local Prometheus instance cannot serve PromQL queries. Grafana and any dashboards that query the local instance will not function.
{{< /note >}}

## Using your own Prometheus

If you already run a Prometheus instance (or Prometheus Operator) in the cluster and prefer not to deploy a second monitoring stack, disable the built-in one:

```yaml
monitoring:
  enabled: false
```

To scrape Union service metrics from your own Prometheus, create a ServiceMonitor targeting the debug endpoints exposed by Union services. These services carry the label `platform.union.ai/prometheus-group: "union-services"`:

| Service | Port | Port name |
|---|---|---|
| Operator | 10254 | debug |
| Propeller | 10254 | debug |
| Proxy | 10254 | debug |
| Executor | 10254 | debug |
| Cluster resource sync | 10254 | debug |

Example ServiceMonitor:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: union-services
  namespace: <namespace>
spec:
  selector:
    matchLabels:
      platform.union.ai/prometheus-group: "union-services"
  namespaceSelector:
    matchNames:
      - "<namespace>"
  endpoints:
    - port: debug
      interval: 1m
      path: /metrics
      honorLabels: true
```

Replace `<namespace>` with the namespace where the data plane is installed (default: `union`).

### Excluding Union-internal metrics

The data plane deploys an internal `union-features` Prometheus instance that powers Task Level Monitoring and cost tracking. If your Prometheus Operator uses a broad or empty `serviceMonitorSelector`, it may inadvertently scrape the internal ServiceMonitors and PodMonitors.

To prevent this, configure your Prometheus operator with a `NotIn` selector that excludes the `union-features` group:

```yaml
# In your Prometheus CR or kube-prometheus-stack values
prometheus:
  prometheusSpec:
    serviceMonitorSelector:
      matchExpressions:
        - key: platform.union.ai/prometheus-group
          operator: NotIn
          values: ["union-features"]
    podMonitorSelector:
      matchExpressions:
        - key: platform.union.ai/prometheus-group
          operator: NotIn
          values: ["union-features"]
```

The `NotIn` operator matches resources where the label is **absent** or has any value other than `union-features`. This safely includes your own ServiceMonitors, the Union `union-services` monitors, and any other monitors in the cluster, while excluding the internal Union features stack.

{{< note >}}
If you are running both the data plane and control plane in the same cluster, this selector also covers control plane ServiceMonitors, since they carry the `union-services` label (not `union-features`).
{{< /note >}}

## Alertmanager

Alertmanager is disabled by default. To enable it and route alerts to a receiver:

```yaml
monitoring:
  alertmanager:
    enabled: true
    alertmanagerSpec:
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
    config:
      global:
        resolve_timeout: 5m
      route:
        receiver: "default"
        group_by: ["alertname", "namespace"]
      receivers:
        - name: "default"
          # Configure your receiver (Slack, PagerDuty, email, webhook, etc.)
          # See: https://prometheus.io/docs/alerting/latest/configuration/
```

## Disabling monitoring

To remove the monitoring stack entirely:

```yaml
monitoring:
  enabled: false
```

Union platform features (Task Level Monitoring, cost tracking, app metrics) are unaffected because they are powered by the separate Union features Prometheus instance.

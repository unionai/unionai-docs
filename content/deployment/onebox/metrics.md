---
title: Task metrics
description: Show task CPU and memory usage in the Metrics tab by pointing onebox at a Prometheus that scrapes cAdvisor and kube-state-metrics.
icon: graph-up
weight: 8
variants: -flyte +union
---

# Task metrics

The Metrics tab shows each task's CPU and memory usage against what it requested. Onebox reads these series from a Prometheus you run, installed separately; onebox doesn't depend on it to start.

## What Prometheus needs

| Series | Source |
|---|---|
| `container_cpu_usage_seconds_total`, `container_memory_working_set_bytes` | cAdvisor, scraped from each node through the API server |
| `kube_pod_container_resource_requests`, `kube_pod_container_resource_limits`, `kube_pod_status_phase` | kube-state-metrics |
| `DCGM_FI_*` (GPU charts only) | NVIDIA dcgm-exporter |

The `prometheus-community/prometheus` chart scrapes cAdvisor and its bundled kube-state-metrics with its default configuration.

## Install Prometheus

```yaml
# prometheus-values.yaml
alertmanager:
  enabled: false
prometheus-pushgateway:
  enabled: false
prometheus-node-exporter:
  enabled: false
kube-state-metrics:
  enabled: true
server:
  retention: 3d
```

```shell
helm install prometheus prometheus --repo https://prometheus-community.github.io/helm-charts \
  --version 25.30.2 -n monitoring --create-namespace -f prometheus-values.yaml
```

The chart creates a ClusterRole for scraping nodes. To reuse a Prometheus you already run, check that it has the series above, with their `namespace` and `pod` labels.

## Point onebox at it

```yaml
metrics:
  prometheusURL: http://prometheus-server.monitoring.svc
```

Run `helm upgrade`. If your Prometheus serves under a path prefix, include it, for example `http://prometheus.monitoring.svc/prometheus`.

## Gotchas

| Symptom | Cause and fix |
|---|---|
| The Metrics tab says the action ran too briefly | Metrics need at least two scrapes of the task's pod. With a one-minute scrape interval, tasks shorter than about two minutes have no CPU chart. |
| Memory charts render but CPU charts are empty | CPU usage is a rate over two cAdvisor samples. Wait for a second scrape, or lower the scrape interval. |
| Requested and limit lines are missing | kube-state-metrics isn't scraped, or doesn't watch onebox's namespace. |

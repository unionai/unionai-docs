---
title: "Kubernetes RBAC: Data plane"
weight: 17
variants: -flyte +union
---

# Kubernetes RBAC: Data plane

## Union core services (data plane)

| Role Name | Purpose | Kind | API Groups | Scope | Resources | Verbs |
| --- | --- | --- | --- | --- | --- | --- |
| `clustersync-resource` | Synchronizes K8s resources across namespaces: creates per-workspace namespaces, RBAC bindings, service accounts, and resource quotas | ClusterRole | ""(core) `rbac.authorization.k8s.io` | Cluster-wide | `configmaps namespaces pods resourcequotas roles rolebindings secrets services serviceaccounts clusterrolebindings` | *(all) |
| `union-executor` | Node Executor: creates/manages task pods, handles FlyteWorkflow and TaskAction CRDs, manages all plugin resource types (Spark, Ray, etc.) | ClusterRole | ""(core) *(all) `apiextensions.k8s.io flyte.lyft.com` | Cluster-wide | `pods (RO) events *(all plugin objects) customresourcedefinitions flyteworkflows/* taskactions/*` | `get list watch create update delete patch` |
| `proxy-system` | Read-only monitoring: streams workflow events, pod logs, and resource utilization data back to control plane via tunnel | ClusterRole | "*" | Cluster-wide | `events flyteworkflows pods/log pods rayjobs resourcequotas` | `get list watch` |
| `operator-system` | Union Operator: manages FlyteWorkflow lifecycle, cluster-level configuration, health monitoring, node management | ClusterRole | `flyte.lyft.com` *(all) | Cluster-wide | `flyteworkflows flyteworkflows/finalizers resourcequotas pods configmaps podtemplates secrets namespaces nodes` | `get list watch create update delete patch post deletecollection` |
| `flytepropeller-role` | FlytePropeller workflow engine: creates task pods, manages FlyteWorkflow CRDs, handles all plugin resource types, enforces resource limits | ClusterRole | ""(core) *(all) `apiextensions.k8s.io flyte.lyft.com` | Cluster-wide | `pods (RO) events *(all plugin objects) customresourcedefinitions flyteworkflows/* limitranges` | `get list watch create update delete patch` |
| `flytepropeller-webhook-role` | Admission webhook: intercepts pod creation to inject secrets from the secrets backend into task containers | ClusterRole | "*" | Cluster-wide | `mutatingwebhookconfigurations secrets pods replicasets/finalizers` | `get create update patch` |
| `proxy-system-secret` | Manages proxy service secrets within the union namespace for tunnel authentication and configuration | Role | "*" | union namespace | `secrets` | `get list create update delete` |
| `operator-system` (ns) | Operator manages its own secrets and deployments within the union namespace | Role | "*" | union namespace | `secrets deployments` | `get list watch create update` |
| `union-operator-admission` | Webhook admission controller reads/creates TLS secrets for webhook serving certificates | Role | ""(core) | union namespace | `secrets` | `get create` |

## Observability and monitoring

| Role Name | Purpose | Kind | API Groups | Scope | Resources | Verbs |
| --- | --- | --- | --- | --- | --- | --- |
| `release-name-fluentbit` | Fluent Bit log collector: reads pod metadata to tag and route container logs to CloudWatch/Cloud Logging | ClusterRole | ""(core) | Cluster-wide | `namespaces pods` | `get list watch` |
| `opencost` | OpenCost: read-only access to all cluster resources for cost attribution and resource usage tracking | ClusterRole | ""(core) `extensions apps batch autoscaling storage.k8s.io` | Cluster-wide | `configmaps deployments nodes pods services resourcequotas replicationcontrollers limitranges PVCs PVs namespaces endpoints daemonsets replicasets statefulsets jobs storageclasses` | `get list watch` |
| `release-name-kube-state-metrics` | KSM: exports K8s object metrics for Prometheus monitoring dashboards | ClusterRole | ""(core) `extensions apps batch autoscaling policy networking.k8s.io certificates.k8s.io discovery.k8s.io storage.k8s.io admissionregistration.k8s.io` | Cluster-wide | `certificatesigningrequests configmaps cronjobs daemonsets deployments endpoints HPAs ingresses jobs leases limitranges namespaces networkpolicies nodes PVCs PVs pods replicasets replicationcontrollers resourcequotas secrets services statefulsets storageclasses validatingwebhookconfigurations volumeattachments endpointslices` | `list watch` |
| `release-name-grafana-clusterrole` | Grafana: reads `configmaps`/`secrets` for dashboard definitions and data source configuration | ClusterRole | ""(core) | Cluster-wide | `configmaps secrets` | `get watch list` |
| `union-operator-prometheus` | Prometheus: scrapes metrics from all cluster services and nodes for monitoring | ClusterRole | ""(core) `discovery.k8s.io networking.k8s.io` | Cluster-wide | `nodes nodes/metrics services endpoints pods endpointslices ingresses`; `nonResourceURLs`: `/metrics /metrics/cadvisor` | `get list watch` |
| `prometheus-operator` | Prometheus Operator: manages the full Prometheus monitoring stack lifecycle, CRDs, and configurations | ClusterRole | `monitoring.coreos.com apps extensions` (core) `networking.k8s.io policy admissionregistration.k8s.io storage.k8s.io` | Cluster-wide | `alertmanagers prometheuses thanosrulers servicemonitors podmonitors prometheusrules probes scrapeconfigs prometheusagents statefulsets daemonsets deployments configmaps secrets pods services endpoints namespaces ingresses PDBs webhookconfigs storageclasses` | *(all) |
| `release-name-dcgm-exporter` | DCGM Exporter: reads node/pod metadata for GPU metrics labeling (optional, for GPU workloads) | ClusterRole | ""(core) | Cluster-wide | `nodes pods` | `get list watch` |

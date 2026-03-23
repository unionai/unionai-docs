---
title: Appendix
weight: 15
variants: -flyte +byoc +selfmanaged
---

# Appendix

## A: Data residency summary

| Data | Stored In | Accessed Via | Transits Control Plane? |
| --- | --- | --- | --- |
| Task definitions (spec metadata) | Control plane DB | ConnectRPC | Yes — metadata only |
| Run metadata (phase, timestamps) | Control plane DB | ConnectRPC | Yes |
| Action metadata (phase, attempts) | Control plane DB | ConnectRPC | Yes |
| Task inputs/outputs | Customer object store | Presigned URL | No — direct client ↔ object store |
| Code bundles | Customer object store | Presigned URL | No — direct client ↔ object store |
| Reports (HTML) | Customer object store | Presigned URL | No — direct client ↔ object store |
| Container images | Customer container registry | Pulled by K8s | No — stays in customer infra |
| Task logs | Customer log aggregator | Streamed via tunnel | Relayed in-memory (not stored) |
| Secrets | Customer secrets backend | Injected at runtime | Relayed during create (not stored) |
| Observability metrics | Customer ClickHouse | Proxied via DataProxy | Relayed in-memory (not stored) |
| User identity / RBAC | Control plane DB | ConnectRPC | Yes |
| Cluster state | Control plane DB | Internal | Yes |

## B: Presigned URL data types

| Data Type | Access Method | Direction |
| --- | --- | --- |
| Task inputs/outputs | Presign via ObjectStore service | Download (GET) |
| Code bundles (TGZ) | CreateDownloadLinkV2 | Download (GET) |
| Reports (HTML) | CreateDownloadLinkV2 | Download (GET) |
| Fast registration uploads | CreateUploadLocation | Upload (PUT) |

## C: Kubernetes RBAC - control plane

**All roles are ClusterRole**

| Role Name | Purpose | API Groups | Resources | Verbs |
| --- | --- | --- | --- | --- |
| `flyteadmin` | Full control over K8s resources for workflow orchestration, namespace provisioning, RBAC setup for workspaces | ""(core) `flyte.lyft.com rbac.authorization.k8s.io` | `configmaps flyteworkflows namespaces pods resourcequotas roles rolebindings secrets services serviceaccounts spark-role limitranges` | *(all) |
| `scyllacluster-edit` | Aggregated admin/edit role for ScyllaDB cluster management (control plane database) | `scylla.scylladb.com` | `scyllaclusters scylladbmonitorings scylladbdatacenters scylladbclusters scylladbmanagerclusterregistrations scylladbmanagertasks` | `create patch update delete deletecollection` |
| `scylladb:controller:aggregate-to-operator` | ScyllaDB operator controller - manages ScyllaDB cluster lifecycle for the control plane database | ""(core) `apps policy scylla.scylladb.com networking.k8s.io batch` | `events nodes endpoints persistentvolumeclaims pods services configmaps secrets statefulsets deployments daemonsets jobs poddisruptionbudgets serviceaccounts scyllaclusters scyllaoperatorconfigs nodeconfigs ingresses` | `get list watch create update delete patch` |
| `scylla-operator:webhook` | ScyllaDB webhook server for admission control of ScyllaDB resources | `admissionregistration.k8s.io scylla.scylladb.com` | `validatingwebhookconfigurations mutatingwebhookconfigurations scyllaclusters nodeconfigs scyllaoperatorconfigs scylladbdatacenters scylladbclusters scylladbmanagertasks` | `get list watch create update patch delete` |
| `console-clusterrole` | Read-only access for Union Console UI to display namespaces, workflows, and pod logs | ""(core) `flyte.lyft.com` | `namespaces flyteworkflows pods pods/log` | `get list watch` |
| `authorizer-clusterrole` | Authorizer service reads namespaces for authorization decisions | ""(core) | `namespaces` | `get list watch` |
| `cluster-clusterrole` | Cluster management service monitors cluster state for health and capacity | ""(core) `apps` | `namespaces nodes replicasets deployments` | `get list watch` |
| `dataproxy-clusterrole` | DataProxy service reads secrets for presigned URL generation and data relay configuration | ""(core) | `secrets` | `get list watch` |
| `executions-clusterrole` | Executions service reads workflow state for execution management and status tracking | ""(core) `flyte.lyft.com` | `namespaces configmaps flyteworkflows` | `get list watch` |
| `queue-clusterrole` | Queue service reads namespaces for task queue routing | ""(core) | `namespaces` | `get list watch` |
| `run-scheduler-clusterrole` | Run Scheduler reads namespaces to determine scheduling scope for workflows | ""(core) | `namespaces` | `get list watch` |
| `usage-clusterrole` | Usage tracking service reads namespaces for resource usage aggregation | ""(core) | `namespaces` | `get list watch` |

## D: Kubernetes RBAC - compute plane

### Union core services (compute plane)

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

### Observability and monitoring

| Role Name | Purpose | Kind | API Groups | Scope | Resources | Verbs |
| --- | --- | --- | --- | --- | --- | --- |
| `release-name-fluentbit` | Fluent Bit log collector: reads pod metadata to tag and route container logs to CloudWatch/Cloud Logging | ClusterRole | ""(core) | Cluster-wide | `namespaces pods` | `get list watch` |
| `opencost` | OpenCost: read-only access to all cluster resources for cost attribution and resource usage tracking | ClusterRole | ""(core) `extensions apps batch autoscaling storage.k8s.io` | Cluster-wide | `configmaps deployments nodes pods services resourcequotas replicationcontrollers limitranges PVCs PVs namespaces endpoints daemonsets replicasets statefulsets jobs storageclasses` | `get list watch` |
| `release-name-kube-state-metrics` | KSM: exports K8s object metrics for Prometheus monitoring dashboards | ClusterRole | ""(core) `extensions apps batch autoscaling policy networking.k8s.io certificates.k8s.io discovery.k8s.io storage.k8s.io admissionregistration.k8s.io` | Cluster-wide | `certificatesigningrequests configmaps cronjobs daemonsets deployments endpoints HPAs ingresses jobs leases limitranges namespaces networkpolicies nodes PVCs PVs pods replicasets replicationcontrollers resourcequotas secrets services statefulsets storageclasses validatingwebhookconfigurations volumeattachments endpointslices` | `list watch` |
| `release-name-grafana-clusterrole` | Grafana: reads `configmaps`/`secrets` for dashboard definitions and data source configuration | ClusterRole | ""(core) | Cluster-wide | `configmaps secrets` | `get watch list` |
| `union-operator-prometheus` | Prometheus: scrapes metrics from all cluster services and nodes for monitoring | ClusterRole | ""(core) `discovery.k8s.io networking.k8s.io` | Cluster-wide | `nodes nodes/metrics services endpoints pods endpointslices ingresses`; `nonResourceURLs`: `/metrics /metrics/cadvisor` | `get list watch` |
| `prometheus-operator` | Prometheus Operator: manages the full Prometheus monitoring stack lifecycle, CRDs, and configurations | ClusterRole | `monitoring.coreos.com apps extensions` (core) `networking.k8s.io policy admissionregistration.k8s.io storage.k8s.io` | Cluster-wide | `alertmanagers prometheuses thanosrulers servicemonitors podmonitors prometheusrules probes scrapeconfigs prometheusagents statefulsets daemonsets deployments configmaps secrets pods services endpoints namespaces ingresses PDBs webhookconfigs storageclasses` | *(all) |
| `release-name-dcgm-exporter` | DCGM Exporter: reads node/pod metadata for GPU metrics labeling (optional, for GPU workloads) | ClusterRole | ""(core) | Cluster-wide | `nodes pods` | `get list watch` |

## E: AWS IAM roles

| Plane | Service Account | Purpose | K8s Namespace | IAM Role ARN Pattern | Bound To | S3 Access |
| --- | --- | --- | --- | --- | --- | --- |
| Control Plane | `flyteadmin` | Orchestration metadata management, namespace provisioning, presigned URL generation for code upload/download | union | `arn:aws:iam::<account-id>:role/adminflyterole` | FlyteAdmin (workflow admin service) | Generates presigned URLs for customer S3 buckets (does not directly read/write data) |
| Compute Plane | `clustersync-system` | Synchronizes K8s namespaces, RBAC roles, service accounts, resource quotas, and config across the cluster | union | `adminflyterole` (compute plane admin) | ClusterResourceSync controller | No direct S3 access |
| Compute Plane | `executor` | Receives task assignments via tunnel, creates task pods, manages pod lifecycle, reports status back to control plane | union | `adminflyterole` (compute plane admin) | Node Executor (TaskAction controller) | R/W to metadata bucket and fast-registration bucket for staging task inputs/outputs |
| Compute Plane | `proxy-system` | Monitors events, Flyte workflows, pod logs; streams data back to control plane via tunnel | union | `adminflyterole` (compute plane admin) | Proxy Service | Read-only access to metadata bucket for proxying presigned URL requests |
| Compute Plane | `operator-system` | Cluster operations, health monitoring, config management, image builder orchestration, tunnel management | union | `adminflyterole` (compute plane admin) | Union Operator | R/W to metadata bucket for operator state and config |
| Compute Plane | `flytepropeller-system` | K8s operator managing FlyteWorkflow CRDs, pod creation, workflow lifecycle execution | union | `adminflyterole` (compute plane admin) | FlytePropeller (workflow engine) | R/W to metadata bucket for workflow data (inputs, outputs, offloaded data) |
| Compute Plane | `flytepropeller-webhook-system` | Mutating admission webhook that injects secrets into task pods at creation time | union | `adminflyterole` (compute plane admin) | FlytePropeller Webhook | No direct S3 access (handles secrets injection only) |
| Compute Plane | `clusterresource-template` (per-namespace) | Executes user workflow tasks; reads inputs, writes outputs to S3 | Per-workspace namespace | `userflyterole` (compute plane user) | Task Pods (user workloads) | R/W to metadata bucket for task inputs/outputs, code bundles, artifacts |

## F: Deployment concerns for Union-managed Bring Your Own Cloud (BYOC) deployments

This appendix applies only to BYOC deployments where Union.ai manages the customer's compute plane Kubernetes cluster. It does not apply to Self-Managed deployments.

### BYOC vs. Self-Managed comparison

| Aspect | Self-Managed | BYOC |
| --- | --- | --- |
| Compute plane operator | Customer | Union.ai |
| K8s cluster management | Customer | Union.ai (via PrivateLink/PSC) |
| K8s API exposure | Customer-controlled | Private only (never public Internet) |
| Union.ai infrastructure access | None (tunnel only) | K8s cluster management only |
| Data/secrets/logs access | None | None |
| Upgrade responsibility | Customer | Union.ai |
| Monitoring responsibility | Customer | Union.ai + customer |

### BYOC deployment: summary of differences

The following is a consolidated list of how BYOC deployments differ from Self-Managed deployments, organized by Security Brief section. In a Self-Managed deployment, Union.ai has zero access to the customer's compute plane and the customer manages all infrastructure independently. The callouts below describe what changes in BYOC.

| Section | BYOC difference |
| --- | --- |
| Network Architecture | Union.ai maintains a private management connection to the customer's K8s cluster via PrivateLink/PSC for cluster management operations. The K8s API endpoint is never exposed to the public Internet. |
| Human Access | Union.ai personnel have authenticated K8s cluster management access (upgrades, provisioning, monitoring). They cannot access object stores, secrets, registries, or log aggregators. JIT access controls are being implemented. |
| Secrets Management | BYOC deployments default to a cloud-native secrets backend (AWS Secrets Manager, GCP Secret Manager, or Azure Key Vault). |
| Availability | Union.ai is responsible for compute plane cluster availability (K8s version, node pools, autoscaler, monitoring). Customer retains responsibility for underlying cloud account availability. |
| Third-Party Dependencies | Union.ai assumes operational responsibility for cluster-level dependencies and their risk mitigation. |

### Private cluster management

Union strongly recommends against exposing Kubernetes clusters to the public Internet.
To manage customer EKS/GKE clusters without public endpoint exposure, Union leverages cloud-native private connectivity technologies:

| Cloud Provider | Technology | Purpose |
| --- | --- | --- |
| AWS | AWS PrivateLink | Private, secure connection to EKS management nodes without Internet exposure |
| GCP | GCP Private Service Connect | Private, secure connection to GKE management nodes without Internet exposure |
| Azure | Azure Private Link | Private, secure connection to AKS management nodes without Internet exposure |

This approach ensures that the Kubernetes management plane is never exposed to the public Internet, preventing unauthorized access, data breaches, and DDoS attacks while satisfying ISO 27001 A.5.15 (access control), CIS v8 4.4 (restrict administrative access), and CIS v8 12.11 (segment administration interfaces) requirements.

## Contact and resources

Trust Center: trust.union.ai

Website: union.ai

Documentation: docs.union.ai

SOC 2 Type II Report: Available upon request

Security Inquiries: Contact your Union.ai account representative or visit trust.union.ai

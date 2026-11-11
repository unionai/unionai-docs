---
title: Dataplane chart
description: Helm values for the chart that onboards a Kubernetes cluster as a Union data plane.
icon: list-columns
variants: -flyte +union
chart_version: 2026.11.2
weight: 1
---

Deploys the Union dataplane components to onboard a kubernetes cluster to the Union Cloud.

## Chart info

| | |
|---|---|
| **Chart version** | 2026.11.2 |
| **App version** | 2026.11.2 |
| **Kubernetes version** | `>= 1.28.0-0` |

## Dependencies

| Repository | Name | Version |
|------------|------|---------|
| https://fluent.github.io/helm-charts | fluentbit(fluent-bit) | 0.48.9 |
| https://kubernetes-sigs.github.io/metrics-server/ | metrics-server(metrics-server) | 3.12.2 |
| https://kubernetes.github.io/ingress-nginx | ingress-nginx | 4.12.3 |
| https://nvidia.github.io/dcgm-exporter/helm-charts | dcgm-exporter | 4.7.1 |
| https://opencost.github.io/opencost-helm-chart | opencost | 1.42.0 |
| https://prometheus-community.github.io/helm-charts | monitoring(kube-prometheus-stack) | 80.8.0 |
| https://prometheus-community.github.io/helm-charts | prometheus(prometheus) | 25.30.2 |
| https://unionai.github.io/helm-charts | knative-operator(knative-operator) | 2026.6.0 |

## Values

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| additionalPodAnnotations | object | Define additional pod annotations for all of the Union pods. | `{}` |
| additionalPodEnvVars | object | Define additional pod environment variables for all of the Union pods. | `{}` |
| additionalPodLabels | object | Define additional pod labels for all of the Union pods. | `{}` |
| additionalPodSpec | object | Define additional PodSpec values for all of the Union pods. | `{}` |
| additionalServiceAccountAnnotations | object | Define additional serviceAccountAnnotations to be added to all system-created service accounts | `{}` |
| apps | object | Union app serving (Knative Serving). Supersedes the deprecated `serving.enabled`; when both are set this one wins. Left unset (null) so the deprecated flag can still take effect — the effective default is `true`.  Does NOT gate the Envoy gateway, which serves the static dataplane routes zero trust depends on, nor the `knative-operator` subchart, which has its own `knative-operator.enabled` condition evaluated by Helm at parse time — turn that off too on the non-zero-trust path. | `{"enabled":null}` |
| clusterName | string | Cluster identifier (shared with Union). | `"{{ .Values.global.CLUSTER_NAME }}"` |
| clusterresourcesync | object | clusterresourcesync contains the configuration information for the syncresources service. | `(see values.yaml)` |
| clusterresourcesync.additionalTemplates | list | Additional cluster resource templates to create per project namespace. Use this instead of overriding `templates` to avoid accidentally removing the default namespace, service account, and resource quota templates. Each entry has a `key` (filename stem) and `value` (Kubernetes manifest). syncresources renders each `value` once per project namespace ({{ namespace }} is substituted), so this is the non-low_privilege / multi-namespace injection point for a per-namespace read-only model volume. Example — a gcsfuse (GKE Cloud Storage FUSE) PV + RO PVC per namespace (provisioning tooling substitutes the real bucket name). The PV is cluster-scoped, so name it per-namespace to avoid collisions:    - key: d_model_volume_pv     value: |       apiVersion: v1       kind: PersistentVolume       metadata:         name: flyte-metadata-{{ namespace }}       spec:         accessModes: ["ReadOnlyMany"]         capacity: { storage: 1Gi }         storageClassName: ""         persistentVolumeReclaimPolicy: Retain         mountOptions: ["implicit-dirs", "file-cache:max-size-mb:-1"]         claimRef: { namespace: {{ namespace }}, name: flyte-metadata-ro }         csi:           driver: gcsfuse.csi.storage.gke.io           volumeHandle: YOUR_MODEL_BUCKET           readOnly: true   - key: e_model_volume_pvc     value: |       apiVersion: v1       kind: PersistentVolumeClaim       metadata:         name: flyte-metadata-ro         namespace: {{ namespace }}       spec:         accessModes: ["ReadOnlyMany"]         storageClassName: ""         volumeName: flyte-metadata-{{ namespace }}         resources: { requests: { storage: 1Gi } }  The mounting pod also needs the annotation `gke-gcsfuse/volumes: "true"`. | `[]` |
| clusterresourcesync.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| clusterresourcesync.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| clusterresourcesync.affinity | object | affinity configurations for the syncresources pods | `{}` |
| clusterresourcesync.clusterRoleRules | list | ClusterRole rules granted to the syncresources ServiceAccount. Override or extend this list to grant access to additional resources (for example, custom resources or extra core resources) that the cluster resource manager should be able to sync into project namespaces. | `(see values.yaml)` |
| clusterresourcesync.config | object | Syncresources service configuration | `(see values.yaml)` |
| clusterresourcesync.config.clusterResourcesPrivate | object | Additional configuration for the cluster resources service | `{"app":{"isServerless":false}}` |
| clusterresourcesync.config.clusterResourcesPrivate.app | object | Configuration of app serving services. | `{"isServerless":false}` |
| clusterresourcesync.config.cluster_resources.clusterName | string | The name of the cluster.  This should always be the same as the cluster name in the config. | `"{{ include \"getClusterName\" . }}"` |
| clusterresourcesync.config.cluster_resources.refreshInterval | string | How frequently to sync the cluster resources | `"5m"` |
| clusterresourcesync.config.cluster_resources.standaloneDeployment | bool | Start the cluster resource manager in standalone mode. | `true` |
| clusterresourcesync.config.cluster_resources.templatePath | string | The path to the project the templates used to configure project resource quotas. | `"/etc/flyte/clusterresource/templates"` |
| clusterresourcesync.config.union | object | Connection information for the sync resources service to connect to the Union control plane. | `(see values.yaml)` |
| clusterresourcesync.config.union.connection.host | string | Host to connect to | `"{{ include \"dataplane.cp.endpoint\" . }}"` |
| clusterresourcesync.config.union.connection.insecureSkipVerify | bool | InsecureSkipVerify controls whether a client verifies the server's certificate chain and host name. Caution: shouldn't be used for production use cases | `false` |
| clusterresourcesync.enabled | bool | Enable or disable the syncresources service. Required in multi-namespace mode (namespaces.enabled=true and low_privilege=false) to provision the per-domain namespaces + RBAC that task pods land in; its namespace_mapping.yaml is driven by the top-level namespace_mapping. Its configmap is gated off under singleNamespace, where task pods run in the release namespace and no per-domain namespaces are needed. | `false` |
| clusterresourcesync.nodeName | string | nodeName constraints for the syncresources pods | `""` |
| clusterresourcesync.nodeSelector | object | nodeSelector constraints for the syncresources pods | `{}` |
| clusterresourcesync.podAnnotations | object | Additional pod annotations for the syncresources service | `{}` |
| clusterresourcesync.podEnv | object | Additional pod environment variables for the syncresources service | `{}` |
| clusterresourcesync.podLabels | object | Additional pod labels for the syncresources service | `{}` |
| clusterresourcesync.resources | object | Kubernetes resource configuration for the syncresources service | `{"limits":{"cpu":"1","memory":"500Mi"},"requests":{"cpu":"100m","memory":"100Mi"}}` |
| clusterresourcesync.serviceAccount | object | Override service account values for the syncresources service | `{"annotations":{},"name":""}` |
| clusterresourcesync.serviceAccount.annotations | object | Additional annotations for the syncresources service account | `{}` |
| clusterresourcesync.serviceAccount.name | string | Override the service account name for the syncresources service | `""` |
| clusterresourcesync.templates | list | The templates that are used to create and/or update kubernetes resources for Union projects. | `(see values.yaml)` |
| clusterresourcesync.templates[0] | object | Template for namespaces resources | `(see values.yaml)` |
| clusterresourcesync.templates[1] | object | Patch default service account | `(see values.yaml)` |
| clusterresourcesync.tolerations | list | tolerations for the syncresources pods | `[]` |
| clusterresourcesync.topologySpreadConstraints | object | topologySpreadConstraints for the syncresources pods | `{}` |
| commonServiceAccount | object | When enabled, creates a single shared ServiceAccount for all components (operator, leaseworker, proxy, webhook, fluentbit) instead of individual ones. Automatically enabled when singleNamespace mode is active. | `{"annotations":{},"enabled":true,"imagePullSecrets":[],"name":"union-system"}` |
| config | object | Global configuration settings for all Union services. | `(see values.yaml)` |
| config.admin | object | Admin Client configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/subworkflow/launchplan#AdminConfig) | `(see values.yaml)` |
| config.catalog | object | Catalog Client configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/catalog#Config) Additional advanced Catalog configuration [here](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/pluginmachinery/catalog#Config) | `(see values.yaml)` |
| config.catalog_cache | object | Optional catalog cache configuration, rendered as catalog_cache.yaml for propeller. | `{}` |
| config.configOverrides | object | Override any configuration settings. | `(see values.yaml)` |
| config.configOverrides.connection.rootTenantURLPattern | string | replaces this leaf before template rendering). | `"{{ include \"dataplane.cp.endpoint\" . }}"` |
| config.copilot | object | Copilot configuration | `(see values.yaml)` |
| config.copilot.plugins.k8s.co-pilot | object | Structure documented [here](https://pkg.go.dev/github.com/lyft/flyteplugins@v0.5.28/go/tasks/pluginmachinery/flytek8s/config#FlyteCoPilotConfig) | `(see values.yaml)` |
| config.core | object | Core propeller configuration | `(see values.yaml)` |
| config.core.propeller | object | follows the structure specified [here](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/config). | `(see values.yaml)` |
| config.core.webhook.embeddedSecretManagerConfig.clusterName | string | not overwrite each other's credential (FAB-241). | `"{{ include \"getClusterName\" . }}"` |
| config.core.webhook.embeddedSecretManagerConfig.fileMountInitContainer | object | public.ecr.aws. | `(see values.yaml)` |
| config.core.webhook.images | object | flytepropellerwebhook.imageMirrorPaths) and enables it when there are any. | `(see values.yaml)` |
| config.core.webhook.selinuxTaskPods | object | auto-detection would fail closed here and mutate nothing. | `{"enabled":false,"nodeOSImageSubstrings":[],"type":"spc_t"}` |
| config.domain | object | Domains configuration for Union projects. This enables the specified number of domains across all projects in Union. | `(see values.yaml)` |
| config.enabled_plugins.tasks | object | Tasks specific configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#GetConfig) | `(see values.yaml)` |
| config.enabled_plugins.tasks.task-plugins | object | Plugins configuration, [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#TaskPluginConfig) | `(see values.yaml)` |
| config.enabled_plugins.tasks.task-plugins.enabled-plugins | list | [Enabled Plugins](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/config#Config). Enable sagemaker*, athena if you install the backend plugins | `["container","sidecar","k8s-array","echo","fast-task","connector-service","artifact-trigger"]` |
| config.k8s | object | Kubernetes specific Flyte configuration | `(see values.yaml)` |
| config.k8s.plugins.k8s | object | Configuration section for all K8s specific plugins [Configuration structure](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/pluginmachinery/flytek8s/config) @schema type: object properties:   default-labels:     type: array     description: Labels added to every task pod. Set by values.azure.yaml or Fleet.   interruptible-tolerations:     type: array     description: Tolerations added to interruptible task pods. Set by values.azure.yaml or Fleet.   interruptible-node-selector-requirement:     type: object     description: Node selector requirement for interruptible task pods. Set by the cloud overlay or Fleet.     properties:       key: {type: string}       operator: {type: string}       values: {type: array}   non-interruptible-node-selector-requirement:     type: object     description: Node selector requirement for non-interruptible task pods. Set by the cloud overlay or Fleet.     properties:       key: {type: string}       operator: {type: string}       values: {type: array}   gpu-device-node-label:     type: string     description: Node label that names the GPU accelerator. Set by values.gcp.yaml, values.azure.yaml or Fleet.   gpu-partition-size-node-label:     type: string     description: Node label that names the GPU partition size. Set by values.gcp.yaml, values.azure.yaml or Fleet. @schema | `(see values.yaml)` |
| config.operator | object | Configuration for the Union operator service | `(see values.yaml)` |
| config.operator.apiKey | object | Eager API key bootstrap. When enabled, the operator mints the EAGER_API_KEY on the control plane and writes it to the task-pod secret store so eager/actions (v2) tasks can call back to the control plane. Enabled by default: under v2 every deployment runs eager/actions workloads. Requires the proxy secret manager (proxy.secretManager.enabled, on by default) and a control plane that can mint EAGER_API_KEY — either by registering an OAuth client on its IdP, or, for IdPs the CP can't self-register against, via the controlplane chart's identity.apiKeyOverrides seed. | `{"enabled":true}` |
| config.operator.apps | object | Enable app serving | `{"enabled":"{{ if include \"apps.enabled\" . }}true{{ else }}false{{ end }}"}` |
| config.operator.billing | object | Billing model: None, Legacy, Shadow, or ResourceUsage. Independent of tunnels. Defaults to ResourceUsage on install and preserves the installed model on upgrade. Set None explicitly for deployments with billing disabled, including self-hosted control planes. | `{"model":"{{ include \"operator.billing.defaultModel\" . }}"}` |
| config.operator.clusterData | object | Dataplane cluster configuration. | `(see values.yaml)` |
| config.operator.clusterData.appId | string | The client id used to authenticate to the control plane.  This will be provided by Union. | `"{{ tpl .Values.secrets.admin.clientId . }}"` |
| config.operator.clusterData.bucketName | string | The bucket name for object storage. | `"{{ tpl .Values.storage.bucketName . }}"` |
| config.operator.clusterData.bucketRegion | string | The bucket region for object storage. | `"{{ tpl .Values.storage.region . }}"` |
| config.operator.clusterData.cloudHostName | string | The hose name for control plane access. This will be provided by Union. | `"{{ include \"dataplane.cp.host\" . }}"` |
| config.operator.clusterData.cloudProvider | string | Cloud provider the cluster runs on (aws, gcp, azure, oci, or metal). Selects the GPU accelerator node label used for usage attribution and tags billable usage. Defaults to the top-level `provider`. When empty, if the operator isn't running in low privilege mode then the operator falls back to detecting it from node labels. | `"{{ tpl (.Values.provider \| default \"\" \| toString) . }}"` |
| config.operator.clusterData.gcpProjectId | string | For GCP only, the project id for object storage. | `"{{ tpl .Values.storage.gcp.projectId . }}"` |
| config.operator.clusterData.metadataBucketPrefix | string | The prefix for constructing object storage URLs. | `"{{ include \"storage.metadata-prefix\" . }}"` |
| config.operator.clusterHealth | object | Cluster-health snapshot reporting. The snapshot push itself is on by default in the operator; these values tune what it collects. | `{"nodeCapacity":{"clusterWidePods":false,"enabled":false}}` |
| config.operator.clusterHealth.nodeCapacity | object | Report the cluster's real capacity, derived from Node objects, instead of the namespace ResourceQuota ceilings the heartbeat sends. Renders a read-only ClusterRole granting get/list/watch on nodes, and on pods when clusterWidePods is set.  Independent of low_privilege and of disableClusterPermissions: the grant is read-only, so a low-privilege cluster can report capacity without taking on the broad operator ClusterRole. Nodes are cluster-scoped and have no namespaced equivalent, so a cluster that leaves this off reports no capacity rather than partial capacity.  Requires an operator image at 2026.10.2 or later. The operator decodes its config strictly, so an older image rejects clusterHealth.nodeCapacity as an unknown key and exits on startup. The operator image tag defaults to the chart appVersion; when that is older, set image.union.tag before enabling this. | `{"clusterWidePods":false,"enabled":false}` |
| config.operator.clusterHealth.nodeCapacity.clusterWidePods | bool | Read pods cluster-wide for per-pool usage, and add pods to the node-capacity ClusterRole. Required for usage on a low-privilege install, which is always namespace-limited. Without it the operator reports capacity only (node allocatable and counts) and omits usage and accelerators. Ignored when the operator is not namespace-limited. | `false` |
| config.operator.clusterId | object | Set the cluster information for the operator service | `{"name":"{{ include \"getClusterName\" . }}","organization":"{{ tpl .Values.orgName . }}"}` |
| config.operator.clusterId.name | string | and rotate/overwrite one credential (FAB-241 / ENG26-933). | `"{{ include \"getClusterName\" . }}"` |
| config.operator.clusterId.organization | string | The organization name for the cluster.  This should match your organization name that you were provided. | `"{{ tpl .Values.orgName . }}"` |
| config.operator.collectUsages | object | Configuration for the usage reporting service. | `{"enabled":true}` |
| config.operator.collectUsages.enabled | bool | Enable usage collection in the operator service. | `true` |
| config.operator.computeResourceManager | object | Compute resource manager configuration. | `{}` |
| config.operator.dependenciesHeartbeat | object | Heartbeat check configuration. | `(see values.yaml)` |
| config.operator.dependenciesHeartbeat.leaseworker | object | Define the leaseworker health check endpoint. Dropped when the leaseworker is disabled. | `{"endpoint":"{{ include \"leaseworker.health.url\" . }}"}` |
| config.operator.dependenciesHeartbeat.prometheus | object | Define the prometheus health check endpoint. | `{"endpoint":"{{ include \"prometheus.health.url\" . }}"}` |
| config.operator.dependenciesHeartbeat.propeller | object | Define the propeller health check endpoint. | `{"endpoint":"{{ include \"propeller.health.url\" . }}"}` |
| config.operator.dependenciesHeartbeat.proxy | object | Define the operator proxy health check endpoint. | `{"endpoint":"{{ include \"proxy.health.url\" . }}"}` |
| config.operator.disableClusterPermissions | bool | Disable cluster-wide permissions. Auto-set when low_privilege is true. | `false` |
| config.operator.limitNamespace | string | Restrict operator to a single namespace. Auto-set in singleNamespace mode. | `""` |
| config.operator.org | object | Organization namespace template override. | `{}` |
| config.operator.secretsWatcher | object | Configuration for the secrets watcher, which triggers rolling restarts when secrets change. | `{"dryRun":true,"enabled":false}` |
| config.operator.secretsWatcher.dryRun | bool | Log changes but do not update deployments. | `true` |
| config.operator.secretsWatcher.enabled | bool | Enable the secrets watcher. | `false` |
| config.operator.syncClusterConfig | object | Sync the configuration from the control plane. This will overwrite any configuration values set as part of the deploy. | `{"enabled":false}` |
| config.proxy | object | Configuration for the operator proxy service. | `(see values.yaml)` |
| config.proxy.smConfig | object | Secret manager configuration @schema type: object properties:   awsConfig:     type: object     description: AWS Secrets Manager backend. Set by values.aws.yaml or Fleet when type is AWS.     properties:       account: {type: string}       region: {type: string}   azureConfig:     type: object     description: Azure Key Vault backend. Set by values.azure.yaml or Fleet when type is Azure.     properties:       vaultURI: {type: string}   gcpConfig:     type: object     description: GCP Secret Manager backend. Set by values.gcp.yaml or Fleet when type is GCP.     properties:       project: {type: string} @schema | `(see values.yaml)` |
| config.proxy.smConfig.enabled | string | Enable or disable secret manager support for the Union dataplane. | `"{{ .Values.proxy.secretManager.enabled }}"` |
| config.proxy.smConfig.k8sConfig | object | Kubernetes specific secret manager configuration. | `{"namespace":"{{ include \"proxy.secretsNamespace\" . }}"}` |
| config.proxy.smConfig.type | string | The type of secret manager to use. | `"{{ .Values.proxy.secretManager.type }}"` |
| config.proxy.smConfig.webhookHostTemplate | string | Template for the union-pod-webhook headless service host used for secret cache invalidation. %s is replaced with the operator pod namespace. | `"union-pod-webhook-headless.%s.svc"` |
| config.qubole | object | Optional Qubole plugin configuration. | `{}` |
| config.resource_manager | object | Resource manager configuration | `{"propeller":{"resourcemanager":{"type":"noop"}}}` |
| config.resource_manager.propeller | object | resource manager configuration | `{"resourcemanager":{"type":"noop"}}` |
| config.sharedService | object | Section that configures shared union services | `{"features":{"gatewayV2":true},"port":8081}` |
| config.task_logs | object | Section that configures how the Task logs are displayed on the UI. This has to be changed based on your actual logging provider. Refer to [structure](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/logs#LogConfig) to understand how to configure various logging engines | `(see values.yaml)` |
| config.task_logs.plugins.logs.cloudwatch-enabled | bool | One option is to enable cloudwatch logging for EKS, update the region and log group accordingly | `false` |
| config.task_resource_defaults | object | Task default resources configuration Refer to the full [structure](https://pkg.go.dev/github.com/lyft/flyteadmin@v0.3.37/pkg/runtime/interfaces#TaskResourceConfiguration). | `(see values.yaml)` |
| config.task_resource_defaults.task_resources | object | Task default resources parameters | `{"defaults":{"cpu":"100m","memory":"500Mi"},"limits":{"cpu":4096,"gpu":256,"memory":"2Ti"}}` |
| config.union.connection | object | Connection information to the union control plane. | `(see values.yaml)` |
| config.union.connection.host | string | Host to connect to | `"{{ include \"dataplane.cp.endpoint\" . }}"` |
| config.union.connection.http2KeepAlive | object | HTTP/2 keepalive for the Connect transport. Pings an idle control-plane connection so it stays warm (below a load balancer's idle timeout) and closes it if a ping goes unanswered, forcing a reconnect. Unlike unaryRPCTimeout this also protects the leaseworker's server-streaming StreamLeases receive path; 0 (default) disables it and lets a half-open connection go undetected. | `{"pingTimeout":"10s","readIdleTimeout":"30s"}` |
| config.union.connection.insecureSkipVerify | bool | InsecureSkipVerify controls whether a client verifies the server's certificate chain and host name. Caution: shouldn't be used for production use cases | `false` |
| config.union.connection.unaryRPCTimeout | string | Per-unary RPC client-side deadline for control-plane Connect clients. 0 disables it, letting a half-open connection (e.g. an idle-dropped load-balancer flow on a separate-cluster dataplane) hang the leaseworker's claim/heartbeat RPC indefinitely. | `"30s"` |
| controlplaneNamespace | string | Namespace of the control plane (for selfhosted-intracluster mode). When set and secretsWatcher is enabled, RBAC roles are created in this namespace for cross-namespace access. | `""` |
| cost.enabled | bool | Enable or disable the cost service resources.  This does not include the opencost or other compatible monitoring services. | `true` |
| cost.serviceMonitor.matchLabels | object | Match labels for the ServiceMonitor. | `{"app.kubernetes.io/name":"opencost"}` |
| cost.serviceMonitor.name | string | The name of the ServiceMonitor. | `"cost"` |
| databricks | object | Databricks integration configuration | `{"enabled":false,"plugin_config":{}}` |
| dataproxy | object | union-dataproxy backend. Rendered when `zero_trust.enabled: true`; the templates gate on that flag directly. | `(see values.yaml)` |
| dataproxy.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| dataproxy.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| dataproxy.affinity | object | affinity configurations for the dataproxy pods | `{}` |
| dataproxy.nodeName | string | nodeName constraint for the dataproxy pods | `""` |
| dataproxy.nodeSelector | object | nodeSelector constraints for the dataproxy pods | `{}` |
| dataproxy.taskMetrics | object | the server-side Go template placeholders. | `(see values.yaml)` |
| dataproxy.tolerations | list | tolerations for the dataproxy pods | `[]` |
| dataproxy.topologySpreadConstraints | object | topologySpreadConstraints for the dataproxy pods | `{}` |
| dcgm-exporter | object | Dcgm exporter configuration | `(see values.yaml)` |
| dcgm-exporter.enabled | bool | Enable or disable the dcgm exporter | `false` |
| dcgm-exporter.namespace | string | Namespace where dcgm-exporter is deployed. Used by Prometheus scrape config. Override if dcgm-exporter runs outside kube-system (e.g. gpu-operator namespace). | `"kube-system"` |
| dcgm-exporter.serviceMonitor | object | It's common practice to taint and label  to not run dcgm exporter on all nodes, so we can use node selectors and    tolerations to ensure it only runs on GPU nodes. affinity: {} nodeSelector: {} tolerations: [] | `{"enabled":false}` |
| extraObjects | list |  | `[]` |
| fluentbit | object | Configuration for fluentbit used for the persistent logging feature. FluentBit runs as a DaemonSet and ships container logs to the persisted-logs/ path in the configured object store. The fluentbit-system service account must have write access to the storage bucket.  Grant access using cloud-native identity federation:   AWS (IRSA):     annotations:       eks.amazonaws.com/role-arn: "arn:aws:iam::`<ACCOUNT_ID>`:role/`<ROLE_NAME>`"   Azure (Workload Identity):     annotations:       azure.workload.identity/client-id: "`<CLIENT_ID>`"   GCP (Workload Identity):     annotations:       iam.gke.io/gcp-service-account: "`<GSA_NAME>`@`<PROJECT_ID>`.iam.gserviceaccount.com"  See https://www.union.ai/docs/v1/selfmanaged/deployment/configuration/persistent-logs/ | `(see values.yaml)` |
| fluentbit.tailDBPath | string | Path to Fluent Bit's tail input state database. | `"/var/log/flb_kube.db"` |
| flyteagent | object | Flyteagent configuration | `{"enabled":false,"plugin_config":{}}` |
| flyteconnector.additionalContainers | list | Appends additional containers to the deployment spec. May include template values. | `[]` |
| flyteconnector.additionalEnvs | list | Appends additional envs to the deployment spec. May include template values | `[]` |
| flyteconnector.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| flyteconnector.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| flyteconnector.affinity | object | affinity for flyteconnector deployment | `{}` |
| flyteconnector.autoscaling.maxReplicas | int |  | `5` |
| flyteconnector.autoscaling.minReplicas | int |  | `2` |
| flyteconnector.autoscaling.targetCPUUtilizationPercentage | int |  | `80` |
| flyteconnector.autoscaling.targetMemoryUtilizationPercentage | int |  | `80` |
| flyteconnector.configPath | string | Default glob string for searching configuration files | `"/etc/flyteconnector/config/*.yaml"` |
| flyteconnector.enabled | bool |  | `true` |
| flyteconnector.extraArgs | object | Appends extra command line arguments to the main command | `{}` |
| flyteconnector.image.pullPolicy | string | Docker image pull policy | `"IfNotPresent"` |
| flyteconnector.image.repository | string | Docker image for flyteconnector deployment | `(see values.yaml)` |
| flyteconnector.image.tag | string |  | `"py3.13-v2.12.1"` |
| flyteconnector.nodeSelector | object | nodeSelector for flyteconnector deployment | `{}` |
| flyteconnector.podAnnotations | object | Annotations for flyteconnector pods | `{}` |
| flyteconnector.ports.containerPort | int |  | `8000` |
| flyteconnector.ports.name | string |  | `"grpc"` |
| flyteconnector.priorityClassName | string | Sets priorityClassName for datacatalog pod(s). | `""` |
| flyteconnector.prometheusPort.containerPort | int |  | `9090` |
| flyteconnector.prometheusPort.name | string |  | `"metric"` |
| flyteconnector.replicaCount | int | Replicas count for flyteconnector deployment | `2` |
| flyteconnector.resources | object | Default resources requests and limits for flyteconnector deployment | `(see values.yaml)` |
| flyteconnector.service | object | Service settings for flyteconnector | `{"clusterIP":"None","type":"ClusterIP"}` |
| flyteconnector.serviceAccount | object | Configuration for service accounts for flyteconnector | `{"annotations":{},"create":true,"imagePullSecrets":[]}` |
| flyteconnector.serviceAccount.annotations | object | Annotations for ServiceAccount attached to flyteconnector pods | `{}` |
| flyteconnector.serviceAccount.create | bool | Should a service account be created for flyteconnector | `true` |
| flyteconnector.serviceAccount.imagePullSecrets | list | ImagePullSecrets to automatically assign to the service account | `[]` |
| flyteconnector.tolerations | list | tolerations for flyteconnector deployment | `[]` |
| flytepropeller | object | Flytepropeller configuration | `(see values.yaml)` |
| flytepropeller.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| flytepropeller.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| flytepropeller.affinity | object | affinity for Flytepropeller deployment | `{}` |
| flytepropeller.configPath | string | Default regex string for searching configuration files | `"/etc/flyte/config/*.yaml"` |
| flytepropeller.extraArgs | object | extra arguments to pass to propeller. | `{}` |
| flytepropeller.nodeName | string | nodeName constraints for Flytepropeller deployment | `""` |
| flytepropeller.nodeSelector | object | nodeSelector for Flytepropeller deployment | `{}` |
| flytepropeller.podAnnotations | object | Annotations for Flytepropeller pods | `{}` |
| flytepropeller.podLabels | object | Labels for the Flytepropeller pods | `{}` |
| flytepropeller.priorityClass | object | Whether the chart creates the (cluster-scoped) PriorityClass named above. Only rendered when flytepropeller.enabled. Skipped under low_privilege (namespace-only installs can't create cluster resources). Set create: false to bring your own class, or in multi-dataplane-per-cluster setups. value is used only when create: true. | `{"create":true,"value":1000000}` |
| flytepropeller.priorityClassName | string | PriorityClass the flytepropeller pod runs under. Defaults to the chart-managed class below. Set to your own existing class to bring your own, or "" for none. Do NOT use a reserved system class (e.g. system-cluster-critical): GKE's gcp-critical-pods ResourceQuota restricts those to kube-system. The pod still references this class under low_privilege when it is externally managed (priorityClass.create: false) — referencing needs no cluster RBAC; only creation does. | `"union-flytepropeller"` |
| flytepropeller.replicaCount | int | Replicas count for Flytepropeller deployment | `1` |
| flytepropeller.resources | object | Default resources requests and limits for Flytepropeller deployment | `{"limits":{"cpu":"3","memory":"3Gi"},"requests":{"cpu":"1","memory":"1Gi"}}` |
| flytepropeller.securityContext | object | Security context for the Flytepropeller container. | `{}` |
| flytepropeller.serviceAccount | object | Configuration for service accounts for FlytePropeller | `{"annotations":{},"imagePullSecrets":[]}` |
| flytepropeller.serviceAccount.annotations | object | Annotations for ServiceAccount attached to FlytePropeller pods | `{}` |
| flytepropeller.serviceAccount.imagePullSecrets | list | ImapgePullSecrets to automatically assign to the service account | `[]` |
| flytepropeller.tolerations | list | tolerations for Flytepropeller deployment | `[]` |
| flytepropeller.topologySpreadConstraints | object | topologySpreadConstraints for Flytepropeller deployment | `{}` |
| flytepropellerwebhook | object | Configuration for the Flytepropeller webhook | `(see values.yaml)` |
| flytepropellerwebhook.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| flytepropellerwebhook.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| flytepropellerwebhook.affinity | object | affinity for webhook deployment | `{}` |
| flytepropellerwebhook.certificate | object | Configuration for webhook certificates | `(see values.yaml)` |
| flytepropellerwebhook.certificate.certManager | object | cert-manager configuration (only used when provider is "certManager") | `{"issuerRef":{}}` |
| flytepropellerwebhook.certificate.certManager.issuerRef | object | Issuer reference for cert-manager. If not set, a self-signed issuer will be created. | `{}` |
| flytepropellerwebhook.certificate.duration | string | Duration of the certificate (only used with certManager provider) | `"8760h"` |
| flytepropellerwebhook.certificate.external | object | External certificate configuration (only used when provider is "external") | `{"caCert":"","tlsCrt":"","tlsKey":""}` |
| flytepropellerwebhook.certificate.external.caCert | string | Base64-encoded CA certificate (PEM format) | `""` |
| flytepropellerwebhook.certificate.external.tlsCrt | string | Base64-encoded TLS certificate (PEM format) | `""` |
| flytepropellerwebhook.certificate.external.tlsKey | string | Base64-encoded TLS private key (PEM format) | `""` |
| flytepropellerwebhook.certificate.provider | string | `flytepropeller webhook init-certs` to populate an empty secret, then the webhook uses those certs. | `"helm"` |
| flytepropellerwebhook.certificate.renewBefore | string | Renew before duration (only used with certManager provider) | `"720h"` |
| flytepropellerwebhook.enabled | bool | enable or disable secrets webhook | `true` |
| flytepropellerwebhook.imageMirrorPaths | object | us-docker.pkg.dev: [union-public-images/unionai]. | `(see values.yaml)` |
| flytepropellerwebhook.legacyWebhookCleanup | object | Cleanup job to remove the legacy flyte-pod-webhook MutatingWebhookConfiguration left behind when upgrading from versions that used the old webhook name. | `(see values.yaml)` |
| flytepropellerwebhook.legacyWebhookCleanup.enabled | bool | Enable the pre-upgrade hook that deletes the stale flyte-pod-webhook resource. THIS IS MOSTLY NEEDED FOR UPGRADES FROM PRE 2026.24.7 VERSIONS.  IT DOESN'T ACT ON NEW INSTALLS. | `true` |
| flytepropellerwebhook.legacyWebhookCleanup.imagePullSecrets | list | ImagePullSecrets for the cleanup job (use if kubectl image is in a private registry) | `[]` |
| flytepropellerwebhook.managedConfig | bool | Enable Helm-managed MutatingWebhookConfiguration (if false, the webhook will create its own) | `true` |
| flytepropellerwebhook.nodeName | string | nodeName constraints for webhook deployment | `""` |
| flytepropellerwebhook.nodeSelector | object | nodeSelector for webhook deployment | `{}` |
| flytepropellerwebhook.podAnnotations | object | Annotations for webhook pods | `{}` |
| flytepropellerwebhook.podEnv | object | Additional webhook container environment variables | `{}` |
| flytepropellerwebhook.podLabels | object | Labels for webhook pods | `{}` |
| flytepropellerwebhook.priorityClassName | string | Sets priorityClassName for webhook pod | `""` |
| flytepropellerwebhook.replicaCount | int | Replicas | `1` |
| flytepropellerwebhook.securityContext | object | Sets securityContext for webhook pod(s). | `(see values.yaml)` |
| flytepropellerwebhook.service | object | Service settings for the webhook | `(see values.yaml)` |
| flytepropellerwebhook.service.port | int | HTTPS port for the webhook service | `443` |
| flytepropellerwebhook.service.targetPort | int | Target port for the webhook service (container port) | `9443` |
| flytepropellerwebhook.serviceAccount | object | Configuration for service accounts for the webhook | `{"imagePullSecrets":[]}` |
| flytepropellerwebhook.serviceAccount.imagePullSecrets | list | ImagePullSecrets to automatically assign to the service account | `[]` |
| flytepropellerwebhook.tolerations | list | tolerations for webhook deployment | `[]` |
| flytepropellerwebhook.topologySpreadConstraints | object | topologySpreadConstraints for webhook deployment | `{}` |
| flytepropellerwebhook.webhook | object | Configuration for the webhook MutatingWebhookConfiguration and certificates | `(see values.yaml)` |
| flytepropellerwebhook.webhook.configurationName | string | Name of the MutatingWebhookConfiguration resource | `"union-pod-webhook-{{ tpl .Values.orgName . }}"` |
| flytepropellerwebhook.webhook.failurePolicy | string | Failure policy for the webhook (Fail or Ignore) | `"Fail"` |
| flytepropellerwebhook.webhook.reinvocationPolicy | string | Reinvocation policy for the webhook | `"Never"` |
| flytepropellerwebhook.webhook.timeoutSeconds | int | Timeout in seconds for the webhook | `30` |
| flytepropellerwebhook.webhook.webhooks | object | Webhook configurations to create | `(see values.yaml)` |
| flytepropellerwebhook.webhook.webhooks.managedImage | object | Managed image webhook configuration (requires Union operator support) | `(see values.yaml)` |
| flytepropellerwebhook.webhook.webhooks.managedImage.name | string | Name of the webhook | `"managed-image-webhook.union.ai"` |
| flytepropellerwebhook.webhook.webhooks.managedImage.namespaceSelector | e.g. admissionsenforcer | can manage it without SSA field ownership conflicts. | `{}` |
| flytepropellerwebhook.webhook.webhooks.managedImage.objectSelector | object | Object selector for the webhook (matchExpressions) | `(see values.yaml)` |
| flytepropellerwebhook.webhook.webhooks.managedImage.path | string | Path for the webhook | `"/mutate--v1-pod/managed-image"` |
| flytepropellerwebhook.webhook.webhooks.secrets | object | Secrets injection webhook configuration | `(see values.yaml)` |
| flytepropellerwebhook.webhook.webhooks.secrets.name | string | Name of the webhook | `"union-pod-webhook.flyte.org"` |
| flytepropellerwebhook.webhook.webhooks.secrets.namespaceSelector | e.g. admissionsenforcer | can manage it without SSA field ownership conflicts. | `{}` |
| flytepropellerwebhook.webhook.webhooks.secrets.objectSelector | object | Object selector for the webhook | `{"matchLabels":{"inject-flyte-secrets":"true","organization":"{{ tpl .Values.orgName . }}"}}` |
| flytepropellerwebhook.webhook.webhooks.secrets.path | string | Path for the webhook | `"/mutate--v1-pod/secrets"` |
| flytepropellerwebhook.webhook.webhooks.selinuxTaskPods | object | webhooks fail closed. | `(see values.yaml)` |
| flytepropellerwebhook.webhook.webhooks.selinuxTaskPods.enabled | bool | configmap core.webhook.selinuxTaskPods.enabled above. | `false` |
| flytepropellerwebhook.webhook.webhooks.selinuxTaskPods.name | string | Name of the webhook | `"union-pod-webhook-selinux.flyte.org"` |
| flytepropellerwebhook.webhook.webhooks.selinuxTaskPods.namespaceSelector | object | Namespace selector for the webhook | `{}` |
| flytepropellerwebhook.webhook.webhooks.selinuxTaskPods.objectSelector | object | cluster enabling this wants a plugin new enough to set it. | `{"matchLabels":{"organization":"{{ tpl .Values.orgName . }}","volumes.union.ai/channel":"true"}}` |
| flytepropellerwebhook.webhook.webhooks.selinuxTaskPods.path | string | Path for the webhook | `"/mutate--v1-pod/selinux-task-pods"` |
| fullnameOverride | string | Override the chart fullname. | `""` |
| gateway | object | Vendored Knative Serving + Kourier + Envoy gateway. Rendered when `zero_trust.enabled: true`; the templates gate on that flag directly. | `(see values.yaml)` |
| gateway.auth | object | Union auth integration for the kourier gateway. The gateway Envoy calls the control plane to authenticate app requests (/me) and authorize them. All three URLs default off the control-plane host (global.CONTROLPLANE_HOST) when left empty, so apps get SSO out of the box — an app subdomain of the CP host shares its auth cookies. Override only to point app auth at a different tenant URL. | `(see values.yaml)` |
| gateway.auth.caFile | string | Optional PEM CA-bundle path (mounted into the gateway container) used to verify the control-plane certificate. Preferred over insecureSkipVerify. Mount the bundle via gateway.components.envoy volumes/volumeMounts and point this at the mounted path. | `""` |
| gateway.auth.insecureSkipVerify | string | Skip verification of the control-plane TLS certificate when the gateway Envoy auth plugin dials it. The gateway reaches the same control plane as the operator; self-hosted control planes serve a self-signed intracluster cert there, so the plugin must trust its CA (caFile) or skip verification — otherwise it panics at init with x509: unknown authority. Null (default) inherits config.union.connection.insecureSkipVerify (the operator's posture); set true/false to override explicitly. | `nil` |
| gateway.auth.organization | string | Org override for auth. Empty -> orgName (global.ORG_NAME). | `""` |
| gateway.auth.tenantAuthSignInURL | string | App sign-in redirect target. Empty -> https://`<CONTROLPLANE_HOST>`/login | `""` |
| gateway.auth.tenantAuthURL | string | App auth (identity) endpoint. Empty -> https://`<CONTROLPLANE_HOST>`/me | `""` |
| gateway.auth.tenantControlPlaneURL | string | Tenant control-plane base URL. Empty -> https://`<CONTROLPLANE_HOST>` | `""` |
| gateway.enabled | bool | Deliver app serving via this chart's vendored Knative Serving + Kourier + Envoy gateway (raw manifests under templates/gateway/*) instead of the knative-operator subchart. Default delivery. When true and app serving is on (`apps.enabled`), the vendored control plane renders and `knative-operator` must be disabled. Zero trust requires this (it layers dataproxy routes on the Envoy gateway). Set false to fall back to the legacy knative-operator path. | `true` |
| gateway.publicLoadBalancer | object | Public internet-facing LoadBalancer for app serving. Separate-cluster dataplanes (not co-located with the control plane) have no shared CP ingress LB to borrow, so they expose the gateway Envoy directly: DNS `*.apps.<dp>.<domain>` -> this LB -> Envoy, with TLS terminated at Envoy (8444) using the letsencrypt wildcard cert. Off by default; enable and annotate it (external-dns hostname, internet-facing scheme) for separate-cluster dataplanes. Intracluster apps route through the shared CP ingress-nginx instead (`ingress.serving.class`), so this stays off there. | `{"annotations":{},"enabled":false,"tlsSecretName":"dataplane-apps-letsencrypt-tls"}` |
| gateway.publicLoadBalancer.annotations | object | Annotations for the LoadBalancer Service — cloud LB scheme (internet-facing) + external-dns hostname. Set these for separate-cluster dataplanes; e.g. on AWS:   service.beta.kubernetes.io/aws-load-balancer-scheme: internet-facing   service.beta.kubernetes.io/aws-load-balancer-type: external   external-dns.alpha.kubernetes.io/hostname: "*.apps.`<CLUSTER_NAME>`.`<CONTROLPLANE_HOST>`" | `{}` |
| gateway.publicLoadBalancer.tlsSecretName | string | Secret holding the apps wildcard TLS cert (tls.crt/tls.key) that Envoy's apps_https:8443 listener terminates. Required (non-empty) when publicLoadBalancer.enabled — the chart fails to render otherwise, as TLS termination at the load balancer is not yet supported. The dataplane does not create this secret — supply it however you issue certs (cert-manager Certificate, a corporate CA, ACM sync, …). The default matches the name our terraform renders via the letsencrypt DNS-01 issuer; override for a BYO cert. | `"dataplane-apps-letsencrypt-tls"` |
| global.AUTH_CLIENT_ID | string |  | `""` |
| global.CLUSTER_NAME | string |  | `""` |
| global.CONTROLPLANE_HOST | string |  | `""` |
| global.FAST_REGISTRATION_BUCKET | string |  | `""` |
| global.METADATA_BUCKET | string |  | `""` |
| global.OIDC_S2S_SCOPE | string |  | `""` |
| global.ORG_NAME | string |  | `""` |
| global.UNION_CONTROL_PLANE_HOST | string |  | `""` |
| global.imageMirrors | object |  | `{}` |
| host | string | global.CONTROLPLANE_HOST > host > global.UNION_CONTROL_PLANE_HOST. | `""` |
| image.envoy | object | Union envoy build for the zero-trust gateway. | `(see values.yaml)` |
| image.flytecopilot | object | flytecopilot repository and tag. | `(see values.yaml)` |
| image.kubeStateMetrics | object | Kubestatemetrics repository and tag. | `(see values.yaml)` |
| image.kubectl | object | Kubectl image configuration for Helm hook cleanup jobs. Registry host is spelled out: an unqualified repository resolves against the implicit docker.io default, which clusters with an allowed-registry policy reject with ErrImagePull. alpine/k8s (rather than bitnami/kubectl) because upstream pruned every version tag from bitnami/kubectl, leaving only `latest` — nothing pinnable. Matches flytepropellerwebhook.legacyWebhookCleanup. | `(see values.yaml)` |
| image.kubectl.imagePullSecrets | list | Optional imagePullSecrets for dataplane Helm hook cleanup jobs. | `[]` |
| image.kubectl.pullPolicy | string | Optional imagePullPolicy for dataplane Helm hook cleanup jobs. Omit when empty. | `""` |
| image.kubectl.repository | string | Kubectl image repository used by dataplane Helm hook cleanup jobs. | `"{{ include \"dataplane.mirror\" (dict \"root\" . \"upstream\" \"docker.io\") }}/alpine/k8s"` |
| image.kubectl.tag | string | Kubectl image tag used by dataplane Helm hook cleanup jobs. | `"1.32.3"` |
| image.union | object | Image repository for the operator and union services | `(see values.yaml)` |
| imageBuilder.authenticationType | string | "basic" uses basic docker username/password auth to authenticate to the registry. | `"noop"` |
| imageBuilder.basicAuth | object | Used by the operator proxy to authenticate when checking image existence. | `{"passwordPlainText":"","passwordSecretName":"DEPOT_TOKEN","username":"x-token"}` |
| imageBuilder.basicAuth.passwordPlainText | string | Plain text password or token (use passwordSecretName for production). | `""` |
| imageBuilder.basicAuth.passwordSecretName | string | Secret name for password lookup via secret manager (recommended for production). | `"DEPOT_TOKEN"` |
| imageBuilder.basicAuth.username | string | Username for registry authentication. For Depot use "x-token". | `"x-token"` |
| imageBuilder.buildkit.additionalVolumeMounts | list | Additional volume mounts to add to the buildkit container | `[]` |
| imageBuilder.buildkit.additionalVolumes | list | Additional volumes to add to the pod | `[]` |
| imageBuilder.buildkit.arm.enabled | bool | Replicas, autoscaling, resources, security, and storage settings are shared. | `false` |
| imageBuilder.buildkit.arm.nodeSelector | object | Additional ARM node selectors, overriding shared selectors. Architecture is pinned to arm64. | `{}` |
| imageBuilder.buildkit.arm.tolerations | list | Additional ARM tolerations, appended to shared tolerations and the ARM architecture toleration. | `[]` |
| imageBuilder.buildkit.autoscaling | object | buildkit HPA configuration | `{"enabled":false,"maxReplicas":2,"minReplicas":1,"targetCPUUtilizationPercentage":60}` |
| imageBuilder.buildkit.autoscaling.targetCPUUtilizationPercentage | int | We can adjust this as needed. | `60` |
| imageBuilder.buildkit.deploymentStrategy | string | deployment strategy for buildkit deployment | `"Recreate"` |
| imageBuilder.buildkit.enabled | bool | Enable buildkit service within this release. | `true` |
| imageBuilder.buildkit.extraConfig | string | insecure = true | `""` |
| imageBuilder.buildkit.fullnameOverride | string | The name to use for the buildkit deployment, service, configmap, etc. | `""` |
| imageBuilder.buildkit.image.pullPolicy | string | Pull policy | `"IfNotPresent"` |
| imageBuilder.buildkit.image.repository | string | Image name | `"{{ include \"dataplane.mirror\" (dict \"root\" . \"upstream\" \"docker.io\") }}/moby/buildkit"` |
| imageBuilder.buildkit.image.tag | e.g. "buildx-stable-1" becomes "buildx-stable-1-rootless" | unless the tag already contains "rootless". | `"buildx-stable-1"` |
| imageBuilder.buildkit.log | object | Enable debug logging | `{"debug":false,"format":"text"}` |
| imageBuilder.buildkit.nodeSelector | object | Node selector | `{}` |
| imageBuilder.buildkit.nydus | object | Run Union's BuildKit image, which bundles nydus-image, instead of buildkit.image. imageBuilder.enableImageOptimization turns this on by itself; set it alone to roll the builder image out first. | `(see values.yaml)` |
| imageBuilder.buildkit.nydus.image.tag | string | Defaults to the chart appVersion. "-rootless" is appended in rootless mode, as for buildkit.image. | `""` |
| imageBuilder.buildkit.oci | object | Buildkitd service configuration | `{"maxParallelism":0}` |
| imageBuilder.buildkit.oci.maxParallelism | int | maxParalelism limits the number of concurrent builds, default is 0 (unbounded) | `0` |
| imageBuilder.buildkit.openShift | object | OpenShift-specific configuration for buildkit. | `(see values.yaml)` |
| imageBuilder.buildkit.pdb.minAvailable | int | Minimum available pods | `1` |
| imageBuilder.buildkit.podAnnotations | object | Pod annotations | `{}` |
| imageBuilder.buildkit.podEnv | list | Appends additional environment variables to the buildkit container's spec. | `[]` |
| imageBuilder.buildkit.replicaCount | int | Replicas count for Buildkit deployment | `1` |
| imageBuilder.buildkit.resources | object | Resource definitions | `{"requests":{"cpu":"200m","ephemeral-storage":"50Gi","memory":"4Gi"}}` |
| imageBuilder.buildkit.rootless | bool | kernel >= 5.11 with unprivileged user namespace support. | `false` |
| imageBuilder.buildkit.securityContext | object | Overrides the buildkit container securityContext. Leave empty to use the chart defaults for privileged or rootless mode. | `{}` |
| imageBuilder.buildkit.service.annotations | object | Service annotations | `{}` |
| imageBuilder.buildkit.service.loadbalancerIp | string | Static ip address for load balancer | `""` |
| imageBuilder.buildkit.service.port | int | Service port | `1234` |
| imageBuilder.buildkit.service.type | string | Service type | `"ClusterIP"` |
| imageBuilder.buildkit.serviceAccount | object | Service account configuration for buildkit | `(see values.yaml)` |
| imageBuilder.buildkit.serviceAccount.forceDedicated | bool | Force buildkit to use this dedicated service account even when commonServiceAccount or single-namespace mode would normally use union-system. | `false` |
| imageBuilder.buildkit.tolerations | list | Tolerations | `[]` |
| imageBuilder.buildkitUri | string | E.g. "tcp://buildkitd.buildkit.svc.cluster.local:1234" | `""` |
| imageBuilder.buildkitUriArm | string | Mutually exclusive with imageBuilder.buildkit.arm.enabled. | `""` |
| imageBuilder.defaultRepository | string | Set explicitly to override auto-detection (e.g. for Depot, GHCR, or custom registries). | `""` |
| imageBuilder.enableImageOptimization | bool | Build every image in Nydus format, for lazy pulls. Applies to EVERY image the dataplane builds, not only some: they become Nydus-only, so they run only on nodes with the snapshotter. Requires nodeBootstrap.enabled, and every node a task pod can land on must be covered by nodeBootstrap.nodeSelector. Images pulled anywhere else (CI, a laptop, a cluster without nodeBootstrap) will not run. Switches the in-chart BuildKit (and its ARM builder) to imageBuilder.buildkit.nydus.image; an external buildkitUri / buildkitUriArm must already bundle nydus-image. | `false` |
| imageBuilder.enabled | bool |  | `true` |
| imageBuilder.registryName | string | Short name used to construct the default registry URL when defaultRepository is empty. | `"union-dataplane"` |
| imageBuilder.targetConfigMapName | string | Should not change unless coordinated with Union technical support. | `"build-image-config"` |
| imagePrewarm | object | one of those mirrors. See templates/image-prewarm/job.yaml. | `(see values.yaml)` |
| imagePrewarm.activeDeadlineSeconds | int | deadline itself doesn't fail the hook. | `900` |
| imagePrewarm.awsCli | object | ImagePullBackOff. | `{"repository":"public.ecr.aws/aws-cli/aws-cli","tag":"2.36.49"}` |
| imagePrewarm.crane | object | crane with a busybox shell (the :debug variant), pinned by digest. | `(see values.yaml)` |
| imagePrewarm.failOnError | bool | failures are logged as warnings and the hook succeeds. | `true` |
| imagePrewarm.serviceAccount.annotations | object | azure.workload.identity/client-id (AcrPull). | `{}` |
| ingress-nginx.controller.admissionWebhooks.enabled | bool |  | `false` |
| ingress-nginx.controller.allowSnippetAnnotations | bool |  | `true` |
| ingress-nginx.controller.config.annotations-risk-level | string |  | `"Critical"` |
| ingress-nginx.controller.config.grpc-connect-timeout | string |  | `"1200"` |
| ingress-nginx.controller.config.grpc-read-timeout | string |  | `"604800"` |
| ingress-nginx.controller.config.grpc-send-timeout | string |  | `"604800"` |
| ingress-nginx.controller.ingressClassResource.controllerValue | string |  | `"union.ai/dataplane"` |
| ingress-nginx.controller.ingressClassResource.default | bool |  | `false` |
| ingress-nginx.controller.ingressClassResource.enabled | bool |  | `true` |
| ingress-nginx.controller.ingressClassResource.name | string |  | `"dataplane"` |
| ingress-nginx.controller.service.ports.http | int |  | `80` |
| ingress-nginx.controller.service.ports.https | int |  | `443` |
| ingress-nginx.controller.service.type | string |  | `"ClusterIP"` |
| ingress-nginx.enabled | bool |  | `false` |
| ingress-nginx.fullnameOverride | string |  | `"dataplane-nginx"` |
| ingress.dataproxy | object | Dataproxy specific ingress configuration. | `{"annotations":{},"class":"dataplane","hostOverride":"","tls":{}}` |
| ingress.dataproxy.annotations | object | Annotations to apply to the ingress resource. | `{}` |
| ingress.dataproxy.class | string | Ingress class name | `"dataplane"` |
| ingress.dataproxy.hostOverride | string | Ingress host | `""` |
| ingress.dataproxy.tls | object | Ingress TLS configuration | `{}` |
| ingress.enabled | bool |  | `false` |
| ingress.host | string |  | `""` |
| ingress.serving | object | Serving specific ingress configuration. | `(see values.yaml)` |
| ingress.serving.annotations | object | Annotations to apply to the ingress resource. | `{}` |
| ingress.serving.class | string | Ingress class name | `"dataplane"` |
| ingress.serving.enabled | bool | Emit the app-serving nginx Ingress (fronts the gateway via ingressClass). Default true: intracluster routes apps through the shared control-plane nginx. Set false on separate-cluster dataplanes, which have no shared nginx and instead expose the gateway Envoy via gateway.publicLoadBalancer — disable it there so the `<dp>-apps` Ingress isn't left dangling with no controller. | `true` |
| ingress.serving.hostOverride | Optional | Host override for serving ingress rule. Defaults to *.apps.<dataplane.cp.host>. | `"*.apps.{{ include \"dataplane.cp.host\" . }}"` |
| ingress.serving.tls | object | Ingress TLS configuration | `{}` |
| knative-operator.enabled | bool |  | `false` |
| knative-operator.namespaceOverride | string |  | `"{{ .Release.Namespace }}"` |
| knative-operator.skipNamespaceCreation | bool |  | `true` |
| leaseworker.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| leaseworker.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| leaseworker.affinity | object | affinity for leaseworker deployment | `{}` |
| leaseworker.capacity | int |  | `100000` |
| leaseworker.config.cluster | string |  | `"{{ tpl .Values.clusterName . }}"` |
| leaseworker.config.organization | string |  | `"{{ tpl .Values.orgName . }}"` |
| leaseworker.config.unionAuth.injectSecret | bool |  | `true` |
| leaseworker.config.unionAuth.secretName | string |  | `"EAGER_API_KEY"` |
| leaseworker.config.workerName | string |  | `"{{ tpl .Values.orgName . }}-{{ tpl .Values.clusterName . }}-worker1"` |
| leaseworker.dispatcherCount | int |  | `512` |
| leaseworker.enabled | bool |  | `true` |
| leaseworker.fasttask.additional-worker-args[0] | string |  | `"--last-ack-grace-period-seconds"` |
| leaseworker.fasttask.additional-worker-args[1] | string |  | `"120"` |
| leaseworker.fasttask.callback-uri | string |  | `"http://union-operator-leaseworker.{{.Release.Namespace}}.svc.cluster.local:15605"` |
| leaseworker.fasttask.grace-period-status-not-found | string |  | `"2m"` |
| leaseworker.nodeName | string | nodeName constraints for leaseworker deployment | `""` |
| leaseworker.nodeSelector | object | nodeSelector for leaseworker deployment | `{}` |
| leaseworker.plugins.ioutils.remoteFileOutputPaths.deckFilename | string |  | `"report.html"` |
| leaseworker.plugins.k8s.disable-inject-owner-references | bool |  | `true` |
| leaseworker.plugins.k8s.inject-finalizer | bool |  | `true` |
| leaseworker.podAnnotations | object |  | `{}` |
| leaseworker.podEnv | list | Appends additional environment variables to the leaseworker container's spec. | `[]` |
| leaseworker.podLabels."app.kubernetes.io/instance" | string |  | `"{{ .Release.Name }}"` |
| leaseworker.podLabels."app.kubernetes.io/name" | string |  | `"leaseworker"` |
| leaseworker.podLabels.app | string |  | `"leaseworker"` |
| leaseworker.podSecurityContext.fsGroup | int |  | `1337` |
| leaseworker.priorityClass | object | Whether the chart creates the (cluster-scoped) PriorityClass named by priorityClassName above. Skipped under low_privilege (namespace-only installs can't create cluster resources) — pair with a class you create out-of-band. Set create: false to bring your own class, or in multi-dataplane-per-cluster setups (the PriorityClass would otherwise be created once per dataplane). value is used only when create: true. | `{"create":true,"value":1000000}` |
| leaseworker.priorityClassName | string | PriorityClass the leaseworker pod runs under. The leaseworker is a Recreate singleton; a priority class keeps leases flowing when a replacement pod would otherwise sit Pending behind node scale-up. Defaults to the chart-managed class below. To bring your own existing class, set this to its name and priorityClass.create: false. Set to "" to run without one. Do NOT use a reserved system class (e.g. system-cluster-critical): GKE's gcp-critical-pods ResourceQuota restricts those to kube-system. The pod still references this class under low_privilege when it is externally managed (priorityClass.create: false) — referencing needs no cluster RBAC; only creation does (see priorityClass.create). | `"union-leaseworker"` |
| leaseworker.raw_config | object |  | `{}` |
| leaseworker.refreshInterval | string |  | `"10s"` |
| leaseworker.resources.limits.cpu | int |  | `8` |
| leaseworker.resources.limits.memory | string |  | `"16Gi"` |
| leaseworker.resources.requests.cpu | string |  | `"300m"` |
| leaseworker.resources.requests.memory | string |  | `"512Mi"` |
| leaseworker.selector.matchLabels.app | string |  | `"leaseworker"` |
| leaseworker.serviceAccount.annotations | object |  | `{}` |
| leaseworker.sharedService.metrics.scope | string |  | `"leaseworker:"` |
| leaseworker.sharedService.security.allowCors | bool |  | `true` |
| leaseworker.sharedService.security.allowLocalhostAccess | bool |  | `true` |
| leaseworker.sharedService.security.allowedHeaders[0] | string |  | `"Content-Type"` |
| leaseworker.sharedService.security.allowedOrigins[0] | string |  | `"*"` |
| leaseworker.sharedService.security.secure | bool |  | `false` |
| leaseworker.sharedService.security.useAuth | bool |  | `false` |
| leaseworker.task_logs | object | Task log link templates surfaced by the UI for task pods (rendered into the leaseworker ConfigMap as task_logs.yaml). The deprecated executor.task_logs key, if set by an overlay, takes precedence — see templates/leaseworker/configmap.yaml. | `(see values.yaml)` |
| leaseworker.task_logs.plugins.logs.cloudwatch-enabled | bool | One option is to enable cloudwatch logging for EKS, update the region and log group accordingly | `false` |
| leaseworker.terminationGracePeriodSeconds | int |  | `75` |
| leaseworker.tolerations | list | tolerations for leaseworker deployment | `[]` |
| leaseworker.topologySpreadConstraints | object | topologySpreadConstraints for leaseworker deployment | `{}` |
| logging | object | Central logging configuration. All services (propeller, operator, leaseworker, clusterresourcesync, nodeobserver, flyteconnector) pull their log level from here. Go services use level 1–6 (1=least verbose, 6=most verbose; 4=INFO). Python services (FlyteConnector) use stdlib scale: pythonLevel (10=DEBUG, 20=INFO, 30=WARNING). Log format options: json, text, gcp | `{"formatter":{"type":"json"},"level":4,"pythonLevel":20,"show-source":true}` |
| low_privilege | bool | Scopes the deployment, permissions and actions created into a single namespace and avoids any deployments that would  require additional permissions on the cluster. This limits the functionality though.  Known tradeoffs when low_privilege is enabled: - Task-Level Monitoring (TLM) metrics are unavailable: cadvisor scraping requires   cluster-scoped node discovery, and kube-state-metrics is limited to the release   namespace (no cross-namespace pod resource metrics for task execution pods).   Console CPU/memory charts for task executions will show "no data." - Node-level metrics (kube_node_*, node_*) are not collected by the namespace-scoped   kube-state-metrics instance. - Cost calculation accuracy is reduced without node-level resource and pricing metrics. - There are likely additional features that require cluster-scoped permissions and   will not function in low_privilege mode. This list will be expanded as they are   identified. | `true` |
| metrics-server.enabled | bool |  | `false` |
| monitoring.alerting.enabled | bool |  | `false` |
| monitoring.alertmanager.enabled | bool |  | `false` |
| monitoring.coreDns.enabled | bool |  | `true` |
| monitoring.crds.enabled | bool |  | `false` |
| monitoring.dashboards.enabled | bool |  | `true` |
| monitoring.dashboards.label | string |  | `"grafana_dashboard"` |
| monitoring.dashboards.labelValue | string |  | `"1"` |
| monitoring.defaultRules.create | bool |  | `true` |
| monitoring.defaultRules.rules.etcd | bool |  | `false` |
| monitoring.defaultRules.rules.kubeControllerManager | bool |  | `false` |
| monitoring.defaultRules.rules.kubeProxy | bool |  | `false` |
| monitoring.defaultRules.rules.kubeSchedulerAlerting | bool |  | `false` |
| monitoring.defaultRules.rules.kubeSchedulerRecording | bool |  | `false` |
| monitoring.enabled | bool |  | `false` |
| monitoring.fullnameOverride | string |  | `"monitoring"` |
| monitoring.grafana.adminPassword | string |  | `"admin"` |
| monitoring.grafana.enabled | bool |  | `true` |
| monitoring.grafana.fullNameOverride | string |  | `"monitoring-grafana"` |
| monitoring.kube-state-metrics.env | list |  | `[]` |
| monitoring.kube-state-metrics.fullnameOverride | string |  | `"monitoring-kube-state-metrics"` |
| monitoring.kube-state-metrics.nameOverride | string |  | `"monitoring-kube-state-metrics"` |
| monitoring.kubeApiServer.enabled | bool |  | `true` |
| monitoring.kubeControllerManager.enabled | bool |  | `false` |
| monitoring.kubeEtcd.enabled | bool |  | `false` |
| monitoring.kubeProxy.enabled | bool |  | `false` |
| monitoring.kubeScheduler.enabled | bool |  | `false` |
| monitoring.kubeStateMetrics.enabled | bool |  | `true` |
| monitoring.kubelet.enabled | bool |  | `true` |
| monitoring.nameOverride | string |  | `"monitoring"` |
| monitoring.nodeExporter.enabled | bool |  | `true` |
| monitoring.prometheus.agentMode | bool |  | `false` |
| monitoring.prometheus.enabled | bool |  | `true` |
| monitoring.prometheus.prometheusSpec.maximumStartupDurationSeconds | int |  | `600` |
| monitoring.prometheus.prometheusSpec.podMonitorSelectorNilUsesHelmValues | bool |  | `false` |
| monitoring.prometheus.prometheusSpec.resources.limits.cpu | string |  | `"2"` |
| monitoring.prometheus.prometheusSpec.resources.limits.memory | string |  | `"4Gi"` |
| monitoring.prometheus.prometheusSpec.resources.requests.cpu | string |  | `"500m"` |
| monitoring.prometheus.prometheusSpec.resources.requests.memory | string |  | `"1Gi"` |
| monitoring.prometheus.prometheusSpec.retention | string |  | `"7d"` |
| monitoring.prometheus.prometheusSpec.ruleSelectorNilUsesHelmValues | bool |  | `false` |
| monitoring.prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues | bool |  | `false` |
| monitoring.prometheus.service.port | int |  | `80` |
| monitoring.prometheusOperator.enabled | bool |  | `true` |
| monitoring.prometheusRules.enabled | bool |  | `true` |
| monitoring.serviceMonitors.enabled | bool |  | `true` |
| monitoring.slos.alerting.enabled | bool |  | `false` |
| monitoring.slos.enabled | bool |  | `false` |
| monitoring.slos.targets.availability | float |  | `0.999` |
| monitoring.slos.targets.latencyP99 | int |  | `5` |
| nameOverride | string | Override the chart name. | `""` |
| namespace_mapping | object | Namespace mapping template for mapping Union runs to Kubernetes namespaces. This is the canonical source of truth (see the selfmanaged namespace-mapping docs). All dataplane services (propeller, clusterresourcesync, operator, leaseworker) inherit this value via the "dataplane.namespaceTemplate" helper, which pins to the release namespace under singleNamespace. | `{}` |
| namespaces.enabled | bool |  | `false` |
| nodeBootstrap | object | Node bootstrap: installs the Nydus snapshotter on each node so pods lazily pull images the image builder exported in Nydus format (see imageBuilder.enableImageOptimization). Privileged, hostPID, writes to the host's /etc and /home/kubernetes and starts systemd units. Supports aws, gcp and azure node images with systemd and a writable /etc (EKS AL2023, GKE COS, AKS Ubuntu); not Bottlerocket. | `(see values.yaml)` |
| nodeBootstrap.cloudProvider | string | aws, gcp or azure. Empty uses the top-level `provider`. | `""` |
| nodeBootstrap.enabled | bool | Enable the node-bootstrap DaemonSet. | `false` |
| nodeBootstrap.fluentBit | object | Sidecar that streams the snapshotter's journal to the pod log. | `(see values.yaml)` |
| nodeBootstrap.image.tag | string | Defaults to the chart appVersion. | `""` |
| nodeBootstrap.nodeSelector | object | Restrict to the nodes that run task pods; empty means every node. | `{}` |
| nodeBootstrap.priorityClassQuota | object | A ResourceQuota scoped to that priority class. GKE rejects system-*-critical pods outside kube-system without one; elsewhere the quota never binds. Turn off if the namespace already has one. | `{"create":true,"pods":"5000"}` |
| nodeBootstrap.startupTaintKey | string | Startup taint union-node-readiness removes once the snapshotter runs. Add it to the worker nodepools as a startup taint so nothing schedules onto a node that cannot pull Nydus images yet. Empty: no taint handling, and the ServiceAccount gets no API access. | `"startup-taint.cluster-autoscaler.kubernetes.io/unionai-node-not-ready"` |
| nodeBootstrap.tolerations | list | Must tolerate the startup taint above and any worker taints. | `[{"operator":"Exists"}]` |
| nodeobserver.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| nodeobserver.additionalVolumes | list | Appends additional volumes to the daemonset spec. May include template values. | `[]` |
| nodeobserver.affinity | object | affinity configurations for the pods associated with nodeobserver services | `{}` |
| nodeobserver.config.criticalDaemonSets | list |  | `[]` |
| nodeobserver.enabled | bool | Enable or disable nodeobserver | `false` |
| nodeobserver.nodeName | string | nodeName constraints for the pods associated with nodeobserver services | `""` |
| nodeobserver.nodeSelector | object | nodeSelector constraints for the pods associated with nodeobserver services | `{}` |
| nodeobserver.podAnnotations | object | Additional pod annotations for the nodeobserver services | `{}` |
| nodeobserver.podEnv | list | Additional pod environment variables for the nodeobserver services | `[{"name":"KUBE_NODE_NAME","valueFrom":{"fieldRef":{"fieldPath":"spec.nodeName"}}}]` |
| nodeobserver.podLabels | object | Additional pod labels for the nodeobserver services | `{}` |
| nodeobserver.podSecurityContext | object |  | `{}` |
| nodeobserver.resources | object | Kubernetes resource configuration for the nodeobserver service | `{"limits":{"cpu":"1","memory":"500Mi"},"requests":{"cpu":"100m","memory":"100Mi"}}` |
| nodeobserver.securityContext.capabilities.add[0] | string |  | `"SYS_ADMIN"` |
| nodeobserver.securityContext.privileged | bool |  | `true` |
| nodeobserver.securityContext.runAsNonRoot | bool |  | `false` |
| nodeobserver.securityContext.runAsUser | int |  | `0` |
| nodeobserver.serviceAccount.annotations | object |  | `{}` |
| nodeobserver.serviceAccount.name | string |  | `""` |
| nodeobserver.tolerations | list | tolerations for the pods associated with nodeobserver services | `[{"effect":"NoSchedule","operator":"Exists"}]` |
| nodeobserver.topologySpreadConstraints | object | topologySpreadConstraints for the pods associated with nodeobserver services | `{}` |
| objectStore | object | Union Object Store configuration | `{"service":{"grpcPort":8089,"httpPort":8080}}` |
| opencost.enabled | bool | Enable or disable the opencost installation. | `false` |
| opencost.opencost.exporter.resources.limits.cpu | string |  | `"1000m"` |
| opencost.opencost.exporter.resources.limits.memory | string |  | `"4Gi"` |
| opencost.opencost.exporter.resources.requests.cpu | string |  | `"500m"` |
| opencost.opencost.exporter.resources.requests.memory | string |  | `"1Gi"` |
| opencost.opencost.metrics.serviceMonitor.enabled | bool |  | `false` |
| opencost.opencost.prometheus.external.enabled | bool |  | `true` |
| opencost.opencost.prometheus.external.url | string |  | `"http://union-operator-prometheus.{{.Release.Namespace}}.svc:80/prometheus"` |
| opencost.opencost.prometheus.internal.enabled | bool |  | `false` |
| opencost.opencost.ui.enabled | bool |  | `false` |
| operator.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| operator.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| operator.affinity | object | affinity configurations for the operator pods | `{}` |
| operator.autoscaling.enabled | bool |  | `false` |
| operator.connectorConfigMountPath | string | Directory the operator mounts the `connector-config` ConfigMap at; the cluster health snapshot reads the connector apps' endpoints from it. The operator's own default is this same path, so the operator config names it only when it differs. | `"/etc/union/connector-config"` |
| operator.enableTunnelService | bool | Enable the Cloudflare tunnel service for secure data-plane ↔ control-plane communication. Canonical toggle — read by both the operator config (config.yaml) and the operator-proxy tunnel container. Enabled by default (used by everyone except self-hosted / intra-cluster deployments, which set this to false). | `true` |
| operator.imagePullSecrets | list |  | `[]` |
| operator.nodeName | string | nodeName constraints for the operator pods | `""` |
| operator.nodeSelector | object | nodeSelector constraints for the operator pods | `{}` |
| operator.podAnnotations | object |  | `{}` |
| operator.podDisruptionBudget.enabled | bool |  | `false` |
| operator.podDisruptionBudget.minAvailable | int |  | `1` |
| operator.podEnv | object |  | `{}` |
| operator.podLabels | object |  | `{}` |
| operator.podSecurityContext | object |  | `{}` |
| operator.priorityClassName | string |  | `""` |
| operator.replicas | int |  | `1` |
| operator.resources.limits.cpu | string |  | `"2"` |
| operator.resources.limits.memory | string |  | `"3Gi"` |
| operator.resources.requests.cpu | string |  | `"150m"` |
| operator.resources.requests.memory | string |  | `"384Mi"` |
| operator.secretName | string |  | `"union-secret-auth"` |
| operator.securityContext | object |  | `{}` |
| operator.serviceAccount.annotations | object |  | `{}` |
| operator.serviceAccount.create | bool |  | `true` |
| operator.serviceAccount.name | string |  | `"operator-system"` |
| operator.tolerations | list | tolerations for the operator pods | `[]` |
| operator.topologySpreadConstraints | object | topologySpreadConstraints for the operator pods | `{}` |
| orgName | string | Organization name (provided by Union). | `"{{ .Values.global.ORG_NAME }}"` |
| prometheus | object | Prometheus configuration (CRD-free) Configures a standalone Prometheus deployment using the community prometheus chart. It does NOT install the Prometheus Operator or any CRDs (ServiceMonitor, PrometheusRule, etc.). Recording rules are delivered via a ConfigMap instead of PrometheusRule CRDs. Scrape targets are configured via static scrape configs instead of ServiceMonitor CRDs. NOTE: If you also enable dcgm-exporter, set dcgm-exporter.serviceMonitor.enabled=false to avoid creating ServiceMonitor CRDs. | `(see values.yaml)` |
| proxy | object | Union operator proxy configuration | `(see values.yaml)` |
| proxy.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| proxy.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| proxy.affinity | object | affinity configurations for the proxy pods | `{}` |
| proxy.nodeName | string | nodeName constraint for the proxy pods | `""` |
| proxy.nodeSelector | object | nodeSelector constraints for the proxy pods | `{}` |
| proxy.secretManager.namespace | string | Set the namespace for union managed secrets created through the native Kubernetes secret manager. If the namespace is not set, the release namespace will be used. | `""` |
| proxy.tolerations | list | tolerations for the proxy pods | `[]` |
| proxy.topologySpreadConstraints | object | topologySpreadConstraints for the proxy pods | `{}` |
| resourcequota | object | Create global resource quotas for the cluster. | `{"create":false}` |
| scheduling | object | Global kubernetes scheduling constraints that will be applied to the pods.  Application specific constraints will always take precedence. | `{"affinity":{},"nodeName":"","nodeSelector":{},"tolerations":[],"topologySpreadConstraints":{}}` |
| scheduling.affinity | object | See https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node | `{}` |
| scheduling.nodeSelector | object | See https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node | `{}` |
| scheduling.tolerations | list | See https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration | `[]` |
| scheduling.topologySpreadConstraints | object | See https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints | `{}` |
| secrets | object | Connection secrets for the Union control plane services. | `(see values.yaml)` |
| secrets.admin.clientId | string | reference this single source via `{{ tpl .Values.secrets.admin.clientId . }}`. | `"{{ .Values.global.AUTH_CLIENT_ID }}"` |
| secrets.admin.clientSecret | string | The client secret used to authenticate to the control plane.  This will be provided by Union. | `""` |
| secrets.admin.create | bool | Create the secret resource containing the client id and secret.  If set to false the user is responsible for creating the secret before the installation. | `true` |
| secrets.admin.enable | bool | Enable or disable the admin secret.  This is used to authenticate to the control plane. | `true` |
| serviceAccount | object | Service account settings for task pods in single-namespace mode. | `{"imagePullSecrets":[]}` |
| serviceAccount.imagePullSecrets | list | Image pull secrets to assign to the task pod service account. | `[]` |
| serving | object | Configure app serving and knative. | `(see values.yaml)` |
| serving.auth | object | Union authentication and authorization configuration. | `{"enabled":true}` |
| serving.auth.enabled | bool | Disabling is common if not leveraging Union Cloud SSO. | `true` |
| serving.enabled | string | DEPRECATED: use `apps.enabled`. Honored only when `apps.enabled` is unset. Left unset (null) so an explicit value is distinguishable from the default. Installs Knative Serving — knative-operator must be running in the cluster for the non-zero-trust path to work. | `nil` |
| serving.extraConfig | object | Additional configuration for Knative serving | `(see values.yaml)` |
| serving.knativeServingHook | object | Controls legacy Helm hook annotations on the KnativeServing CR. | `{"enabled":true}` |
| serving.metrics | bool | Enables scraping of metrics from the serving component | `true` |
| serving.openShift | object | OpenShift-specific configuration for Knative Serving components. | `(see values.yaml)` |
| serving.replicas | int | The number of replicas to create for all components for high availability. | `2` |
| serving.resources | object | Resources for serving components | `(see values.yaml)` |
| sparkoperator.enabled | bool |  | `false` |
| sparkoperator.plugin_config | object |  | `{}` |
| storage | object | Object storage configuration used by all Union services. | `(see values.yaml)` |
| storage.accessKey | string | The access key used for object storage. | `""` |
| storage.authType | string | The authentication type.  Currently supports "accesskey" and "iam". | `"accesskey"` |
| storage.bucketName | string | The bucket name used for object storage. | `"{{ .Values.global.METADATA_BUCKET }}"` |
| storage.cache | object | Cache configuration for objects retrieved from object storage. | `{"maxSizeMBs":0,"targetGCPercent":70}` |
| storage.credentialsSecretRef | object | Reference to a Kubernetes Secret containing storage credentials. When set, the chart reads two flat keys from the secret AT RENDER TIME (helm lookup) and inlines them into the rendered storage configuration; the raw accessKey/secretKey values are not read. The secret must therefore exist BEFORE the release is installed or upgraded, and rotating it requires a new render (helm upgrade) to take effect.  Create the secret with flat keys:   kubectl create secret generic storage-credentials -n `<namespace>` \     --from-literal=access_key_id=`<key>` \     --from-literal=secret_key=`<secret>`  Then set credentialsSecretRef.name to the secret name. Key names are configurable via accessKeyIdKey and secretKeyKey if your secret uses different field names. | `{"accessKeyIdKey":"access_key_id","name":"","namespace":"","secretKeyKey":"secret_key"}` |
| storage.credentialsSecretRef.accessKeyIdKey | string | Key in the secret that holds the access key ID. | `"access_key_id"` |
| storage.credentialsSecretRef.name | string | Name of the Kubernetes Secret. Leave empty to disable (credentials go in ConfigMaps). | `""` |
| storage.credentialsSecretRef.namespace | string | Namespace the secret lives in. Empty means the release namespace. Set this when the release namespace is not known before install (e.g. the platform names it at deploy time) so the secret can be created in a fixed, pre-agreed namespace ahead of the first render. | `""` |
| storage.credentialsSecretRef.secretKeyKey | string | Key in the secret that holds the secret key. | `"secret_key"` |
| storage.custom | object | Define custom configurations for the object storage.  Only used if the provider is set to "custom". | `{}` |
| storage.disableSSL | bool | Disable SSL for object storage.  This should only used for local/sandbox installations. | `false` |
| storage.enableMultiContainer | bool | overlays run multi-container). | `true` |
| storage.endpoint | string | Define or override the endpoint used for the object storage service. | `""` |
| storage.fastRegistrationBucketName | string | The bucket name used for fast registration uploads. | `"{{ .Values.global.FAST_REGISTRATION_BUCKET }}"` |
| storage.fastRegistrationURL | string | Override the URL for signed fast registration uploads.  This is only used for local/sandbox installations. | `""` |
| storage.gcp | object | Define GCP specific configuration for object storage. | `{"projectId":""}` |
| storage.injectPodEnvVars | bool | Injects the object storage access information into the pod environment variables.  Needed for providers that only support access and secret key based authentication. | `true` |
| storage.limits | object | Internal service limits for object storage access. | `{"maxDownloadMBs":1024}` |
| storage.metadataPrefix | string | Example for Azure: "abfs://my-container@mystorageaccount.dfs.core.windows.net" | `""` |
| storage.provider | string | The storage provider to use.  Currently supports "compat", "aws", "oci", and "custom". | `"compat"` |
| storage.region | string | The bucket region used for object storage. | `"us-east-1"` |
| storage.s3ForcePathStyle | bool | Use path style instead of domain style urls to access the object storage service. | `true` |
| storage.secretKey | string | The secret key used for object storage. | `""` |
| taskPodTemplate.affinity | object | affinity applied to all task pods (e.g. a preferred Spot nodeAffinity). | `{}` |
| taskPodTemplate.nodeSelector | object | nodeSelector applied to all task pods (via the task-template PodTemplate). | `{}` |
| taskPodTemplate.tolerations | list | tolerations applied to all task pods (e.g. a Spot taint toleration). | `[]` |
| taskPodTemplate.workingDir | string |  | `""` |
| telemetry.enabled | bool | Set to false to opt out. Injects DO_NOT_TRACK=1 (https://donottrack.sh) into every task pod, the same switch flyte-sdk, the Flyte backend and the console honour. | `true` |
| tunnelService | object | Tunnel-service ingress config consumed by the union-operator's tunnel sidecar. The dataplane ingress is gated by `zero_trust.enabled` (templates evaluate that flag directly); only the origin URL override is configurable here. | `{"apps":{"enableGlobalIngress":true,"originURL":""},"dataplane":{"originURL":""}}` |
| updateStatus | object | Self-reported CP-client-construction data the operator ships in every UpdateStatus call (UpdateStatusRequest.connection_config). The controlplane prefers this over the legacy admin-set DataplaneIngressURL when present. | `(see values.yaml)` |
| updateStatus.connectionConfig.apps | object | DP-declared app serving. The dataplane reports where it serves apps (domain) and the TLS posture (insecure); the control plane builds an app's public_url as {scheme}://{subdomain}.{domain}. The dataplane owns the apps domain and its Ingress/DNS/TLS. connection_config v2 (apps.domain). | `{"domain":"","insecure":false}` |
| updateStatus.connectionConfig.apps.domain | string | Bare apps domain (no scheme, no subdomain) the dataplane serves apps under, with the dataplane name baked in so the URL routes to the DP running the app. Empty (default) disables self-reporting; the control plane then falls back to its global executions.apps.publicURLPattern (single-dataplane only).  Recommended convention: a subdomain of the control-plane host so apps inherit control-plane SSO — "apps.`<CLUSTER_NAME>`.`<CONTROLPLANE_HOST>`", e.g. "apps.dp-1.union.example.com". SSO cookies set at the control-plane host propagate to its subdomains, and the per-dataplane label routes each app URL to the dataplane running it (required to run apps on more than one dataplane). A domain not under the control-plane host works but forgoes SSO-by-default — you then own its DNS/TLS and cookie setup. | `""` |
| updateStatus.connectionConfig.apps.insecure | bool | Serve app URLs over http:// instead of https:// when true. Default https. | `false` |
| updateStatus.connectionConfig.enabled | bool | Opt in to self-reporting. Off by default: the connection_config ConfigMap, operator `connectionConfigPath`, volume, and mount only render when this is true, keeping the chart compatible with operator images that predate connection_config support. Enable only when the deployed operator image understands `connectionConfigPath`. | `false` |
| updateStatus.connectionConfig.host | string | DP-reachable hostname the CP should dial back. e.g. "dp-1.internal.`<full_domain>`". Bare hostname only — no scheme, no port. Chart helper derives the gRPC endpoint as `dns:///<host>`. Empty falls back to `Values.ingress.host` (the dataplane's own ingress hostname), so most installs don't need to set this explicitly — the chart already knows where the DP is reachable. | `""` |
| updateStatus.connectionConfig.insecure | bool | CP dials this DP with plain HTTP/2 (no TLS) when true. Default false. | `false` |
| updateStatus.connectionConfig.insecureSkipVerify | bool | CP skips cert validation on the TLS handshake (self-signed CP cert envs). | `false` |
| userRoleAnnotationKey | string | This is the annotation key that is added to service accounts. | `"eks.amazonaws.com/role-arn"` |
| userRoleAnnotationValue | string | This is the value of the annotation key that is added to service accounts. | `"arn:aws:iam::ACCOUNT_ID:role/flyte_project_role"` |
| uvolMountBroker | object | nodeobserver contains the configuration information for the node observer service. | `(see values.yaml)` |
| uvolMountBroker.block | object | Block mode: Volumes whose content is one ext4 image that the broker loop-attaches and mounts for the pod (small-file workloads get in-kernel metadata instead of a FUSE round trip per file operation). Attaching makes the node kernel parse filesystem bytes the tenant controls, so it is an explicit, permanent opt-in for TRUSTED workloads. | `{"allow":null,"freezeMax":"60s"}` |
| uvolMountBroker.block.allow | string | Pods allowed to use block-mode Volumes. A pod is allowed when ANY rule matches; a rule matches when EVERY field it sets matches the pod: `namespace`, `serviceAccount`, or both (kubelet supplies them, so a task cannot forge them). A serviceAccount-only rule matches that name in every namespace. Fields are glob patterns: `*` matches anything and `team-*` a prefix, so `[{namespace: "*"}]` is the blanket opt-in for every pod on the cluster. A rule that sets neither field is rejected at broker start. Unset (the default): `[{namespace: "*"}]` when `low_privilege` is false, and disabled when it is true. Any list you set is used as given, and `[]` disables block mode. Attaching makes the node kernel parse filesystem bytes the task controls, so on a cluster running untrusted workloads set an explicit list. Example: `[{namespace: builders}, {namespace: ci, serviceAccount: buildkit}]` | `nil` |
| uvolMountBroker.block.freezeMax | string | Thaw a block mount the client froze (around a Volume commit) after this long, so a client that dies mid-commit cannot wedge the image's writers. | `"60s"` |
| uvolMountBroker.driverName | string | CSI driver name. Task pods reference this exact string, so changing it requires the same change on the client side — leave it alone unless you know you need to. | `"volumes.union.ai"` |
| uvolMountBroker.enabled | bool | Enable the uvol mount broker DaemonSet: a CSI node driver that premounts FUSE channels and hands the fds to unprivileged in-pod clients, so task pods mount versioned Volumes with no CAP_SYS_ADMIN, no /dev/fuse and no hostPath. On by default: Agent Sessions workspaces and any task using Volumes mount through it, and a dataplane without it leaves those pods in FailedMount ("driver name volumes.union.ai not found"). The DaemonSet itself is privileged (host root, CAP_SYS_ADMIN, /dev/fuse) — set false to leave it off a cluster that will not use Volumes. | `true` |
| uvolMountBroker.kubeletDir | string | kubelet's root directory, bind-mounted so the broker can premount inside kubelet-owned publish targets. Distributions that relocate it (k3s, some managed AMIs) must set this to match, or registration fails. | `"/var/lib/kubelet"` |
| uvolMountBroker.maxUnavailable | string | Rolling update budget. The broker is on the task open() path, so a large value trades mount availability for upgrade speed. | `"25%"` |
| uvolMountBroker.metricsScope | string | Top-level metrics scope for every series the broker emits (uvol_broker:* — verb failures, journal write failures, CSI outcomes, active channels). | `"uvol_broker"` |
| uvolMountBroker.nodeCache | object | Node-shared chunk cache for Union Volumes, served by the broker. A task pod that asks (`allow_volumes(shared_node_cache=True)`) gets a per-namespace subtree of `hostPath` bind-mounted by the broker — no hostPath and no privilege in the task pod; pods of one namespace on a node share one cache, other namespaces never see it. On by default, so a pod that asks gets it on every node; set `enabled: false` to refuse (the pod then fails NodePublish with FailedPrecondition rather than mounting anything privileged). Put `hostPath` on the node's fastest local disk (on EKS AMIs with instance store, under /mnt/k8s-disks/0) and budget it: each client evicts against its own limit. | `{"enabled":true,"hostPath":"/var/lib/uvol/node-cache"}` |
| uvolMountBroker.nodeSelector | object | Must cover every node a volume-using task pod can land on: task pods carry no matching nodeSelector of their own, so any node without the broker fails NodePublish with "driver volumes.union.ai not found". Empty = all nodes, which is the safe default. | `{}` |
| uvolMountBroker.podAnnotations | object | Additional pod annotations. | `{}` |
| uvolMountBroker.podEnv | list | Additional pod environment variables. | `[]` |
| uvolMountBroker.priorityClass | object | Whether the chart creates the PriorityClass (the name above, or a derived release-scoped default when empty). Set create: false to bring your own, which then requires priorityClassName. value applies only when create: true. | `{"create":true,"value":1000000}` |
| uvolMountBroker.priorityClassName | string | PriorityClass for the broker DaemonSet: schedules ahead of task pods so a node's broker isn't evicted out from under pods that need it to mount Volumes. Empty (with priorityClass.create) derives a release-scoped default; set an explicit name to override. Empty with create: false is rejected — the broker must have a deliberate class. Do NOT use a reserved system class (e.g. system-node-critical): GKE restricts those to kube-system, so the pods are rejected at creation. | `""` |
| uvolMountBroker.profilerPort | int | flytestdlib profutils port: /metrics, /healthcheck, pprof, and the /readyz endpoint the readinessProbe uses. | `10254` |
| uvolMountBroker.resources | object | The cpu request is what the broker is guaranteed under contention, not a cap: there is deliberately no cpu limit — CFS throttling would inject worse tail latency than fair-share contention — so on an idle node the broker bursts past the request. What the request costs is node schedulability: the broker is a DaemonSet at system-node-critical, so every milli it requests leaves allocatable, and a request a task pod cannot fit around preempts that task pod rather than queueing it. Task pods sized to a node's full allocatable CPU are common, which makes the DaemonSet footprint the binding constraint, so the default is small; raise it per cluster where volume traffic warrants it. Measured at 60us of broker CPU per open with 8 volumes active, so 30m guarantees ~500 opens/s and 500m carries roughly 8,300. Memory is O(channels) at ~15 KiB each (~15 MiB at the 1024-channel node cap); the limit is a leak backstop, not an operating bound. | `{"limits":{"memory":"256Mi"},"requests":{"cpu":"30m","memory":"32Mi"}}` |
| uvolMountBroker.socketDir | string | Host directory for the per-volume unix sockets task pods connect to. | `"/run/uvol"` |
| uvolMountBroker.stateDir | string | Host directory for the broker's state journal, which is what lets kernel mounts and pod-held fds survive a broker restart. | `"/var/lib/uvol/state"` |
| uvolMountBroker.tolerations | list | Tolerate everything, for the same reason: a tainted node that still runs task pods needs the broker. | `[{"operator":"Exists"}]` |
| zero_trust | object | Zero-trust dataplane mode (the default). Installs the Kourier+Envoy gateway (replaces the knative-operator path), the dataproxy backend, and the tunnel-service dataplane ingress. `knative-operator.enabled` must stay false (its default) because Helm evaluates that subchart condition at parse time and can't derive it from this flag. Set false for deployments with self-hosted control planes. | `{"enabled":true}` |

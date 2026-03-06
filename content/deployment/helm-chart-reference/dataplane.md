---
title: Dataplane chart
variants: -flyte -byoc +selfmanaged
chart_version: 2026.3.3
weight: 1
---

Deploys the Union dataplane components to onboard a kubernetes cluster to the Union Cloud.

## Chart info

| | |
|---|---|
| **Chart version** | 2026.3.3 |
| **App version** | 2026.3.2 |
| **Kubernetes version** | `>= 1.28.0-0` |

## Dependencies

| Repository | Name | Version |
|------------|------|---------|
| https://fluent.github.io/helm-charts | fluentbit(fluent-bit) | 0.48.9 |
| https://kubernetes-sigs.github.io/metrics-server/ | metrics-server(metrics-server) | 3.12.2 |
| https://kubernetes.github.io/ingress-nginx | ingress-nginx | 4.12.3 |
| https://nvidia.github.io/dcgm-exporter/helm-charts | dcgm-exporter | 4.7.1 |
| https://opencost.github.io/opencost-helm-chart | opencost | 1.42.0 |
| https://prometheus-community.github.io/helm-charts | prometheus(kube-prometheus-stack) | 72.9.1 |
| https://unionai.github.io/helm-charts | knative-operator(knative-operator) | 2025.5.0 |

## Values

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| additionalPodAnnotations | object | Define additional pod annotations for all of the Union pods. | `{}` |
| additionalPodEnvVars | object | Define additional pod environment variables for all of the Union pods. | `{}` |
| additionalPodLabels | object | Define additional pod labels for all of the Union pods. | `{}` |
| additionalPodSpec | object | Define additional PodSpec values for all of the Union pods. | `{}` |
| clusterName | string | Cluster name should be shared with Union for proper functionality. | `"{{ .Values.global.CLUSTER_NAME }}"` |
| clusterresourcesync | object | clusterresourcesync contains the configuration information for the syncresources service. | `(see values.yaml)` |
| clusterresourcesync.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| clusterresourcesync.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| clusterresourcesync.affinity | object | affinity configurations for the syncresources pods | `{}` |
| clusterresourcesync.config | object | Syncresources service configuration | `(see values.yaml)` |
| clusterresourcesync.config.clusterResourcesPrivate | object | Additional configuration for the cluster resources service | `{"app":{"isServerless":false}}` |
| clusterresourcesync.config.clusterResourcesPrivate.app | object | Configuration of app serving services. | `{"isServerless":false}` |
| clusterresourcesync.config.cluster_resources.clusterName | string | The name of the cluster.  This should always be the same as the cluster name in the config. | `"{{ include \"getClusterName\" . }}"` |
| clusterresourcesync.config.cluster_resources.refreshInterval | string | How frequently to sync the cluster resources | `"5m"` |
| clusterresourcesync.config.cluster_resources.standaloneDeployment | bool | Start the cluster resource manager in standalone mode. | `true` |
| clusterresourcesync.config.cluster_resources.templatePath | string | The path to the project the templates used to configure project resource quotas. | `"/etc/flyte/clusterresource/templates"` |
| clusterresourcesync.config.union | object | Connection information for the sync resources service to connect to the Union control plane. | `(see values.yaml)` |
| clusterresourcesync.config.union.connection.host | string | Host to connect to | `"dns:///{{ tpl .Values.host . }}"` |
| clusterresourcesync.enabled | bool | Enable or disable the syncresources service | `true` |
| clusterresourcesync.nodeName | string | nodeName constraints for the syncresources pods | `""` |
| clusterresourcesync.nodeSelector | object | nodeSelector constraints for the syncresources pods | `{}` |
| clusterresourcesync.podAnnotations | object | Additional pod annotations for the syncresources service | `{}` |
| clusterresourcesync.podEnv | object | Additional pod environment variables for the syncresources service | `{}` |
| clusterresourcesync.resources | object | Kubernetes resource configuration for the syncresources service | `{"limits":{"cpu":"1","memory":"500Mi"},"requests":{"cpu":"500m","memory":"100Mi"}}` |
| clusterresourcesync.serviceAccount | object | Override service account values for the syncresources service | `{"annotations":{},"name":""}` |
| clusterresourcesync.serviceAccount.annotations | object | Additional annotations for the syncresources service account | `{}` |
| clusterresourcesync.serviceAccount.name | string | Override the service account name for the syncresources service | `""` |
| clusterresourcesync.templates | list | The templates that are used to create and/or update kubernetes resources for Union projects. | `(see values.yaml)` |
| clusterresourcesync.templates[0] | object | Template for namespaces resources | `(see values.yaml)` |
| clusterresourcesync.templates[1] | object | Patch default service account | `(see values.yaml)` |
| clusterresourcesync.tolerations | list | tolerations for the syncresources pods | `[]` |
| clusterresourcesync.topologySpreadConstraints | object | topologySpreadConstraints for the syncresources pods | `{}` |
| config | object | Global configuration settings for all Union services. | `(see values.yaml)` |
| config.admin | object | Admin Client configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/subworkflow/launchplan#AdminConfig) | `(see values.yaml)` |
| config.catalog | object | Catalog Client configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/catalog#Config) Additional advanced Catalog configuration [here](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/pluginmachinery/catalog#Config) | `(see values.yaml)` |
| config.configOverrides | object | Override any configuration settings. | `{"cache":{"identity":{"enabled":false}}}` |
| config.copilot | object | Copilot configuration | `(see values.yaml)` |
| config.copilot.plugins.k8s.co-pilot | object | Structure documented [here](https://pkg.go.dev/github.com/lyft/flyteplugins@v0.5.28/go/tasks/pluginmachinery/flytek8s/config#FlyteCoPilotConfig) | `(see values.yaml)` |
| config.core | object | Core propeller configuration | `(see values.yaml)` |
| config.core.propeller | object | follows the structure specified [here](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/config). | `(see values.yaml)` |
| config.domain | object | Domains configuration for Union projects. This enables the specified number of domains across all projects in Union. | `(see values.yaml)` |
| config.enabled_plugins.tasks | object | Tasks specific configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#GetConfig) | `(see values.yaml)` |
| config.enabled_plugins.tasks.task-plugins | object | Plugins configuration, [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#TaskPluginConfig) | `(see values.yaml)` |
| config.enabled_plugins.tasks.task-plugins.enabled-plugins | list | [Enabled Plugins](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/config#Config). Enable sagemaker*, athena if you install the backend plugins | `["container","sidecar","k8s-array","echo","fast-task","connector-service"]` |
| config.k8s | object | Kubernetes specific Flyte configuration | `{"plugins":{"k8s":{"default-cpus":"100m","default-env-vars":[],"default-memory":"100Mi"}}}` |
| config.k8s.plugins.k8s | object | Configuration section for all K8s specific plugins [Configuration structure](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/pluginmachinery/flytek8s/config) | `{"default-cpus":"100m","default-env-vars":[],"default-memory":"100Mi"}` |
| config.logger | object | Logging configuration | `{"level":4,"show-source":true}` |
| config.operator | object | Configuration for the Union operator service | `(see values.yaml)` |
| config.operator.apps | object | Enable app serving | `{"enabled":"{{ .Values.serving.enabled }}"}` |
| config.operator.billableUsageCollector | object | Configuration for billable usage collector. | `{"enabled":true}` |
| config.operator.billableUsageCollector.enabled | bool | Enable billable usage collection in the operator service. | `true` |
| config.operator.clusterData | object | Dataplane cluster configuration. | `(see values.yaml)` |
| config.operator.clusterData.appId | string | The client id used to authenticate to the control plane.  This will be provided by Union. | `"{{ tpl .Values.secrets.admin.clientId . }}"` |
| config.operator.clusterData.bucketName | string | The bucket name for object storage. | `"{{ tpl .Values.storage.bucketName . }}"` |
| config.operator.clusterData.bucketRegion | string | The bucket region for object storage. | `"{{ tpl .Values.storage.region . }}"` |
| config.operator.clusterData.cloudHostName | string | The hose name for control plane access. This will be provided by Union. | `"{{ tpl .Values.host . }}"` |
| config.operator.clusterData.gcpProjectId | string | For GCP only, the project id for object storage. | `"{{ tpl .Values.storage.gcp.projectId . }}"` |
| config.operator.clusterData.metadataBucketPrefix | string | The prefix for constructing object storage URLs. | `"{{ include \"storage.metadata-prefix\" . }}"` |
| config.operator.clusterId | object | Set the cluster information for the operator service | `{"organization":"{{ tpl .Values.orgName . }}"}` |
| config.operator.clusterId.organization | string | The organization name for the cluster.  This should match your organization name that you were provided. | `"{{ tpl .Values.orgName . }}"` |
| config.operator.collectBillableResourceUsage | object | Configuration for billable resource usage collection. | `{"enabled":false}` |
| config.operator.collectBillableResourceUsage.enabled | bool | Enable billable resource usage collection in the operator service. | `false` |
| config.operator.collectUsages | object | Configuration for the usage reporting service. | `{"enabled":true}` |
| config.operator.collectUsages.enabled | bool | Enable usage collection in the operator service. | `true` |
| config.operator.dependenciesHeartbeat | object | Heartbeat check configuration. | `(see values.yaml)` |
| config.operator.dependenciesHeartbeat.prometheus | object | Define the prometheus health check endpoint. | `{"endpoint":"{{ include \"prometheus.health.url\" . }}"}` |
| config.operator.dependenciesHeartbeat.propeller | object | Define the propeller health check endpoint. | `{"endpoint":"{{ include \"propeller.health.url\" . }}"}` |
| config.operator.dependenciesHeartbeat.proxy | object | Define the operator proxy health check endpoint. | `{"endpoint":"{{ include \"proxy.health.url\" . }}"}` |
| config.operator.enableTunnelService | bool | Enable the cloudflare tunnel service for secure communication with the control plane. | `true` |
| config.operator.enabled | bool | Enables the operator service | `true` |
| config.operator.syncClusterConfig | object | Sync the configuration from the control plane. This will overwrite any configuration values set as part of the deploy. | `{"enabled":false}` |
| config.proxy | object | Configuration for the operator proxy service. | `(see values.yaml)` |
| config.proxy.smConfig | object | Secret manager configuration | `(see values.yaml)` |
| config.proxy.smConfig.enabled | string | Enable or disable secret manager support for the Union dataplane. | `"{{ .Values.proxy.secretManager.enabled }}"` |
| config.proxy.smConfig.k8sConfig | object | Kubernetes specific secret manager configuration. | `{"namespace":"{{ include \"proxy.secretsNamespace\" . }}"}` |
| config.proxy.smConfig.type | string | The type of secret manager to use. | `"{{ .Values.proxy.secretManager.type }}"` |
| config.resource_manager | object | Resource manager configuration | `{"propeller":{"resourcemanager":{"type":"noop"}}}` |
| config.resource_manager.propeller | object | resource manager configuration | `{"resourcemanager":{"type":"noop"}}` |
| config.sharedService | object | Section that configures shared union services | `{"features":{"gatewayV2":true},"port":8081}` |
| config.task_logs | object | Section that configures how the Task logs are displayed on the UI. This has to be changed based on your actual logging provider. Refer to [structure](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/logs#LogConfig) to understand how to configure various logging engines | `(see values.yaml)` |
| config.task_logs.plugins.logs.cloudwatch-enabled | bool | One option is to enable cloudwatch logging for EKS, update the region and log group accordingly | `false` |
| config.task_resource_defaults | object | Task default resources configuration Refer to the full [structure](https://pkg.go.dev/github.com/lyft/flyteadmin@v0.3.37/pkg/runtime/interfaces#TaskResourceConfiguration). | `(see values.yaml)` |
| config.task_resource_defaults.task_resources | object | Task default resources parameters | `{"defaults":{"cpu":"100m","memory":"500Mi"},"limits":{"cpu":4096,"gpu":256,"memory":"2Ti"}}` |
| config.union.connection | object | Connection information to the union control plane. | `{"host":"dns:///{{ tpl .Values.host . }}"}` |
| config.union.connection.host | string | Host to connect to | `"dns:///{{ tpl .Values.host . }}"` |
| cost.enabled | bool | Enable or disable the cost service resources.  This does not include the opencost or other compatible monitoring services. | `true` |
| cost.serviceMonitor.matchLabels | object | Match labels for the ServiceMonitor. | `{"app.kubernetes.io/name":"opencost"}` |
| cost.serviceMonitor.name | string | The name of the ServiceMonitor. | `"cost"` |
| databricks | object | Databricks integration configuration | `{"enabled":false,"plugin_config":{}}` |
| dcgm-exporter | object | Dcgm exporter configuration | `(see values.yaml)` |
| dcgm-exporter.enabled | bool | Enable or disable the dcgm exporter | `false` |
| dcgm-exporter.serviceMonitor | object | It's common practice to taint and label  to not run dcgm exporter on all nodes, so we can use node selectors and    tolerations to ensure it only runs on GPU nodes. affinity: {} nodeSelector: {} tolerations: [] | `{"honorLabels":true}` |
| executor.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| executor.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| executor.config.cluster | string |  | `"{{ tpl .Values.clusterName . }}"` |
| executor.config.evaluatorCount | int |  | `64` |
| executor.config.maxActions | int |  | `2000` |
| executor.config.organization | string |  | `"{{ tpl .Values.orgName . }}"` |
| executor.config.unionAuth.injectSecret | bool |  | `true` |
| executor.config.unionAuth.secretName | string |  | `"EAGER_API_KEY"` |
| executor.config.workerName | string |  | `"worker1"` |
| executor.enabled | bool |  | `true` |
| executor.idl2Executor | bool |  | `false` |
| executor.plugins.fasttask | object | Configuration section for all K8s specific plugins [Configuration structure](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/pluginmachinery/flytek8s/config) | `(see values.yaml)` |
| executor.plugins.ioutils.remoteFileOutputPaths.deckFilename | string |  | `"report.html"` |
| executor.plugins.k8s.disable-inject-owner-references | bool |  | `true` |
| executor.podEnv | list | Appends additional environment variables to the executor container's spec. | `[]` |
| executor.podLabels.app | string |  | `"executor"` |
| executor.propeller.node-config.disable-input-file-writes | bool |  | `true` |
| executor.raw_config | object |  | `{}` |
| executor.resources.limits.cpu | int |  | `4` |
| executor.resources.limits.memory | string |  | `"8Gi"` |
| executor.resources.requests.cpu | int |  | `1` |
| executor.resources.requests.memory | string |  | `"1Gi"` |
| executor.selector.matchLabels.app | string |  | `"executor"` |
| executor.serviceAccount.annotations | object |  | `{}` |
| executor.sharedService.metrics.scope | string |  | `"executor:"` |
| executor.sharedService.security.allowCors | bool |  | `true` |
| executor.sharedService.security.allowLocalhostAccess | bool |  | `true` |
| executor.sharedService.security.allowedHeaders[0] | string |  | `"Content-Type"` |
| executor.sharedService.security.allowedOrigins[0] | string |  | `"*"` |
| executor.sharedService.security.secure | bool |  | `false` |
| executor.sharedService.security.useAuth | bool |  | `false` |
| executor.task_logs.plugins.logs.cloudwatch-enabled | bool | One option is to enable cloudwatch logging for EKS, update the region and log group accordingly | `false` |
| executor.task_logs.plugins.logs.dynamic-log-links[0].vscode.displayName | string |  | `"VS Code Debugger"` |
| executor.task_logs.plugins.logs.dynamic-log-links[0].vscode.linkType | string |  | `"ide"` |
| executor.task_logs.plugins.logs.dynamic-log-links[0].vscode.templateUris[0] | string |  | `(see values.yaml)` |
| executor.task_logs.plugins.logs.dynamic-log-links[1].wandb-execution-id.displayName | string |  | `"Weights & Biases"` |
| executor.task_logs.plugins.logs.dynamic-log-links[1].wandb-execution-id.linkType | string |  | `"dashboard"` |
| executor.task_logs.plugins.logs.dynamic-log-links[1].wandb-execution-id.templateUris[0] | string |  | `(see values.yaml)` |
| executor.task_logs.plugins.logs.dynamic-log-links[2].wandb-custom-id.displayName | string |  | `"Weights & Biases"` |
| executor.task_logs.plugins.logs.dynamic-log-links[2].wandb-custom-id.linkType | string |  | `"dashboard"` |
| executor.task_logs.plugins.logs.dynamic-log-links[2].wandb-custom-id.templateUris[0] | string |  | `(see values.yaml)` |
| executor.task_logs.plugins.logs.dynamic-log-links[3].comet-ml-execution-id.displayName | string |  | `"Comet"` |
| executor.task_logs.plugins.logs.dynamic-log-links[3].comet-ml-execution-id.linkType | string |  | `"dashboard"` |
| executor.task_logs.plugins.logs.dynamic-log-links[3].comet-ml-execution-id.templateUris | string |  | `(see values.yaml)` |
| executor.task_logs.plugins.logs.dynamic-log-links[4].comet-ml-custom-id.displayName | string |  | `"Comet"` |
| executor.task_logs.plugins.logs.dynamic-log-links[4].comet-ml-custom-id.linkType | string |  | `"dashboard"` |
| executor.task_logs.plugins.logs.dynamic-log-links[4].comet-ml-custom-id.templateUris | string |  | `(see values.yaml)` |
| executor.task_logs.plugins.logs.dynamic-log-links[5].neptune-scale-run.displayName | string |  | `"Neptune Run"` |
| executor.task_logs.plugins.logs.dynamic-log-links[5].neptune-scale-run.linkType | string |  | `"dashboard"` |
| executor.task_logs.plugins.logs.dynamic-log-links[5].neptune-scale-run.templateUris[0] | string |  | `"https://scale.neptune.ai/{{`{{ .taskConfig.project }}`}}/-/run/?customId={{`{{ .podName }}`}}"` |
| executor.task_logs.plugins.logs.dynamic-log-links[6].neptune-scale-custom-id.displayName | string |  | `"Neptune Run"` |
| executor.task_logs.plugins.logs.dynamic-log-links[6].neptune-scale-custom-id.linkType | string |  | `"dashboard"` |
| executor.task_logs.plugins.logs.dynamic-log-links[6].neptune-scale-custom-id.templateUris[0] | string |  | `(see values.yaml)` |
| executor.task_logs.plugins.logs.kubernetes-enabled | bool |  | `true` |
| extraObjects | list |  | `[]` |
| fluentbit | object | Configuration for fluentbit used for the persistent logging feature. FluentBit runs as a DaemonSet and ships container logs to the persisted-logs/ path in the configured object store. The fluentbit-system service account must have write access to the storage bucket.  Grant access using cloud-native identity federation:   AWS (IRSA):     annotations:       eks.amazonaws.com/role-arn: "arn:aws:iam::`<ACCOUNT_ID>`:role/`<ROLE_NAME>`"   Azure (Workload Identity):     annotations:       azure.workload.identity/client-id: "`<CLIENT_ID>`"   GCP (Workload Identity):     annotations:       iam.gke.io/gcp-service-account: "`<GSA_NAME>`@`<PROJECT_ID>`.iam.gserviceaccount.com"  See the [persistent logs documentation](/deployment/configuration/persistent-logs/) | `(see values.yaml)` |
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
| flyteconnector.enabled | bool |  | `false` |
| flyteconnector.extraArgs | object | Appends extra command line arguments to the main command | `{}` |
| flyteconnector.image.pullPolicy | string | Docker image pull policy | `"IfNotPresent"` |
| flyteconnector.image.repository | string | Docker image for flyteconnector deployment | `"ghcr.io/flyteorg/flyte-connectors"` |
| flyteconnector.image.tag | string |  | `"py3.13-2.0.0b50.dev3-g695bb1db3.d20260122"` |
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
| flytepropeller.replicaCount | int | Replicas count for Flytepropeller deployment | `1` |
| flytepropeller.resources | object | Default resources requests and limits for Flytepropeller deployment | `{"limits":{"cpu":"3","memory":"3Gi"},"requests":{"cpu":"1","memory":"1Gi"}}` |
| flytepropeller.serviceAccount | object | Configuration for service accounts for FlytePropeller | `{"annotations":{},"imagePullSecrets":[]}` |
| flytepropeller.serviceAccount.annotations | object | Annotations for ServiceAccount attached to FlytePropeller pods | `{}` |
| flytepropeller.serviceAccount.imagePullSecrets | list | ImapgePullSecrets to automatically assign to the service account | `[]` |
| flytepropeller.tolerations | list | tolerations for Flytepropeller deployment | `[]` |
| flytepropeller.topologySpreadConstraints | object | topologySpreadConstraints for Flytepropeller deployment | `{}` |
| flytepropellerwebhook | object | Configuration for the Flytepropeller webhook | `(see values.yaml)` |
| flytepropellerwebhook.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| flytepropellerwebhook.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| flytepropellerwebhook.affinity | object | affinity for webhook deployment | `{}` |
| flytepropellerwebhook.enabled | bool | enable or disable secrets webhook | `true` |
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
| fullnameOverride | string | Override the chart fullname. | `""` |
| global.CLIENT_ID | string |  | `""` |
| global.CLUSTER_NAME | string |  | `""` |
| global.FAST_REGISTRATION_BUCKET | string |  | `""` |
| global.METADATA_BUCKET | string |  | `""` |
| global.ORG_NAME | string |  | `""` |
| global.UNION_CONTROL_PLANE_HOST | string |  | `""` |
| host | string | Set the control plane host for your Union dataplane installation.  This will be provided by Union. | `"{{ .Values.global.UNION_CONTROL_PLANE_HOST }}"` |
| image.flytecopilot | object | flytecopilot repository and tag. | `{"pullPolicy":"IfNotPresent","repository":"cr.flyte.org/flyteorg/flytecopilot","tag":"v1.14.1"}` |
| image.kubeStateMetrics | object | Kubestatemetrics repository and tag. | `(see values.yaml)` |
| image.union | object | Image repository for the operator and union services | `{"pullPolicy":"IfNotPresent","repository":"public.ecr.aws/p0i0a9q8/unionoperator","tag":""}` |
| imageBuilder.authenticationType | string | "azure" uses az acr login to authenticate to the default registry. Requires Azure Workload Identity to be enabled. | `"noop"` |
| imageBuilder.buildkit.additionalVolumeMounts | list | Additional volume mounts to add to the buildkit container | `[]` |
| imageBuilder.buildkit.additionalVolumes | list | Additional volumes to add to the pod | `[]` |
| imageBuilder.buildkit.autoscaling | object | buildkit HPA configuration | `{"enabled":false,"maxReplicas":2,"minReplicas":1,"targetCPUUtilizationPercentage":60}` |
| imageBuilder.buildkit.autoscaling.targetCPUUtilizationPercentage | int | We can adjust this as needed. | `60` |
| imageBuilder.buildkit.deploymentStrategy | string | deployment strategy for buildkit deployment | `"Recreate"` |
| imageBuilder.buildkit.enabled | bool | Enable buildkit service within this release. | `true` |
| imageBuilder.buildkit.fullnameOverride | string | The name to use for the buildkit deployment, service, configmap, etc. | `""` |
| imageBuilder.buildkit.image.pullPolicy | string | Pull policy | `"IfNotPresent"` |
| imageBuilder.buildkit.image.repository | string | Image name | `"docker.io/moby/buildkit"` |
| imageBuilder.buildkit.image.tag | e.g. "buildx-stable-1" becomes "buildx-stable-1-rootless" | unless the tag already contains "rootless". | `"buildx-stable-1"` |
| imageBuilder.buildkit.log | object | Enable debug logging | `{"debug":false,"format":"text"}` |
| imageBuilder.buildkit.nodeSelector | object | Node selector | `{}` |
| imageBuilder.buildkit.oci | object | Buildkitd service configuration | `{"maxParallelism":0}` |
| imageBuilder.buildkit.oci.maxParallelism | int | maxParalelism limits the number of concurrent builds, default is 0 (unbounded) | `0` |
| imageBuilder.buildkit.pdb.minAvailable | int | Minimum available pods | `1` |
| imageBuilder.buildkit.podAnnotations | object | Pod annotations | `{}` |
| imageBuilder.buildkit.podEnv | list | Appends additional environment variables to the buildkit container's spec. | `[]` |
| imageBuilder.buildkit.replicaCount | int | Replicas count for Buildkit deployment | `1` |
| imageBuilder.buildkit.resources | object | Resource definitions | `{"requests":{"cpu":1,"ephemeral-storage":"20Gi","memory":"1Gi"}}` |
| imageBuilder.buildkit.rootless | bool | kernel >= 5.11 with unprivileged user namespace support. | `true` |
| imageBuilder.buildkit.service.annotations | object | Service annotations | `{}` |
| imageBuilder.buildkit.service.loadbalancerIp | string | Static ip address for load balancer | `""` |
| imageBuilder.buildkit.service.port | int | Service port | `1234` |
| imageBuilder.buildkit.service.type | string | Service type | `"ClusterIP"` |
| imageBuilder.buildkit.serviceAccount | object | Service account configuration for buildkit | `{"annotations":{},"create":true,"imagePullSecret":"","name":"union-imagebuilder"}` |
| imageBuilder.buildkit.tolerations | list | Tolerations | `[]` |
| imageBuilder.buildkitUri | string | E.g. "tcp://buildkitd.buildkit.svc.cluster.local:1234" | `""` |
| imageBuilder.defaultRepository | string | Note, the build-image task will fail unless "registry" is specified or a default repository is provided. | `""` |
| imageBuilder.enabled | bool |  | `true` |
| imageBuilder.targetConfigMapName | string | Should not change unless coordinated with Union technical support. | `"build-image-config"` |
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
| ingress-nginx.enabled | bool |  | `false` |
| ingress.dataproxy | object | Dataproxy specific ingress configuration. | `{"annotations":{},"class":"","hostOverride":"","tls":{}}` |
| ingress.dataproxy.annotations | object | Annotations to apply to the ingress resource. | `{}` |
| ingress.dataproxy.class | string | Ingress class name | `""` |
| ingress.dataproxy.hostOverride | string | Ingress host | `""` |
| ingress.dataproxy.tls | object | Ingress TLS configuration | `{}` |
| ingress.enabled | bool |  | `false` |
| ingress.host | string |  | `""` |
| ingress.serving | object | Serving specific ingress configuration. | `{"annotations":{},"class":"","hostOverride":"","tls":{}}` |
| ingress.serving.annotations | object | Annotations to apply to the ingress resource. | `{}` |
| ingress.serving.class | string | Ingress class name | `""` |
| ingress.serving.hostOverride | Optional | Host override for serving ingress rule. Defaults to *.apps.{{ .Values.host }}. | `""` |
| ingress.serving.tls | object | Ingress TLS configuration | `{}` |
| knative-operator.crds.install | bool |  | `true` |
| knative-operator.enabled | bool |  | `false` |
| low_privilege | bool | Scopes the deployment, permissions and actions created into a single namespace | `false` |
| metrics-server.enabled | bool |  | `false` |
| monitoring.enabled | bool |  | `true` |
| nameOverride | string | Override the chart name. | `""` |
| namespace_mapping | object | Namespace mapping template for mapping Union runs to Kubernetes namespaces. This is the canonical source of truth. All dataplane services (propeller, clusterresourcesync, operator, executor) will inherit this value unless explicitly overridden in their service-specific config sections (config.namespace_config, config.operator.org, executor.raw_config). | `{}` |
| namespaces.enabled | bool |  | `true` |
| nodeobserver | object | nodeobserver contains the configuration information for the node observer service. | `(see values.yaml)` |
| nodeobserver.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| nodeobserver.additionalVolumes | list | Appends additional volumes to the daemonset spec. May include template values. | `[]` |
| nodeobserver.affinity | object | affinity configurations for the pods associated with nodeobserver services | `{}` |
| nodeobserver.enabled | bool | Enable or disable nodeobserver | `false` |
| nodeobserver.nodeName | string | nodeName constraints for the pods associated with nodeobserver services | `""` |
| nodeobserver.nodeSelector | object | nodeSelector constraints for the pods associated with nodeobserver services | `{}` |
| nodeobserver.podAnnotations | object | Additional pod annotations for the nodeobserver services | `{}` |
| nodeobserver.podEnv | list | Additional pod environment variables for the nodeobserver services | `(see values.yaml)` |
| nodeobserver.resources | object | Kubernetes resource configuration for the nodeobserver service | `{"limits":{"cpu":"1","memory":"500Mi"},"requests":{"cpu":"500m","memory":"100Mi"}}` |
| nodeobserver.tolerations | list | tolerations for the pods associated with nodeobserver services | `[{"effect":"NoSchedule","operator":"Exists"}]` |
| nodeobserver.topologySpreadConstraints | object | topologySpreadConstraints for the pods associated with nodeobserver services | `{}` |
| objectStore | object | Union Object Store configuration | `{"service":{"grpcPort":8089,"httpPort":8080}}` |
| opencost.enabled | bool | Enable or disable the opencost installation. | `true` |
| opencost.fullnameOverride | string |  | `"opencost"` |
| opencost.opencost.exporter.resources.limits.cpu | string |  | `"1000m"` |
| opencost.opencost.exporter.resources.limits.memory | string |  | `"4Gi"` |
| opencost.opencost.exporter.resources.requests.cpu | string |  | `"500m"` |
| opencost.opencost.exporter.resources.requests.memory | string |  | `"1Gi"` |
| opencost.opencost.prometheus.external.enabled | bool |  | `true` |
| opencost.opencost.prometheus.external.url | string |  | `"http://union-operator-prometheus.{{.Release.Namespace}}.svc:80/prometheus"` |
| opencost.opencost.prometheus.internal.enabled | bool |  | `false` |
| opencost.opencost.ui.enabled | bool |  | `false` |
| operator.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| operator.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| operator.affinity | object | affinity configurations for the operator pods | `{}` |
| operator.autoscaling.enabled | bool |  | `false` |
| operator.enableTunnelService | bool |  | `true` |
| operator.imagePullSecrets | list |  | `[]` |
| operator.nodeName | string | nodeName constraints for the operator pods | `""` |
| operator.nodeSelector | object | nodeSelector constraints for the operator pods | `{}` |
| operator.podAnnotations | object |  | `{}` |
| operator.podEnv | object |  | `{}` |
| operator.podLabels | object |  | `{}` |
| operator.podSecurityContext | object |  | `{}` |
| operator.priorityClassName | string |  | `""` |
| operator.replicas | int |  | `1` |
| operator.resources.limits.cpu | string |  | `"2"` |
| operator.resources.limits.memory | string |  | `"3Gi"` |
| operator.resources.requests.cpu | string |  | `"1"` |
| operator.resources.requests.memory | string |  | `"1Gi"` |
| operator.secretName | string |  | `"union-secret-auth"` |
| operator.securityContext | object |  | `{}` |
| operator.serviceAccount.annotations | object |  | `{}` |
| operator.serviceAccount.create | bool |  | `true` |
| operator.serviceAccount.name | string |  | `"operator-system"` |
| operator.tolerations | list | tolerations for the operator pods | `[]` |
| operator.topologySpreadConstraints | object | topologySpreadConstraints for the operator pods | `{}` |
| orgName | string | Organization name should be provided by Union. | `"{{ .Values.global.ORG_NAME }}"` |
| prometheus | object | Prometheus configuration This section configures kube-prometheus-stack for monitoring the Union dataplane. By default, most Kubernetes component monitoring is disabled to reduce resource usage. Enable specific components as needed for your observability requirements. | `(see values.yaml)` |
| prometheus.defaultRules | object | -------------------------------------------------------------------------- Configure which Prometheus alerting and recording rules to enable. These rules provide pre-built alerts for common Kubernetes issues. See: https://github.com/prometheus-operator/kube-prometheus/tree/main/manifests | `(see values.yaml)` |
| prometheus.defaultRules.rules | object | Disable specific rules by name disabled:   KubeAPIDown: true   KubeAPITerminatedRequests: true | `(see values.yaml)` |
| prometheus.defaultRules.rules.kubeApiserverAvailability | bool | API Server availability alerts (e.g., KubeAPIDown, KubeAPITerminatedRequests) | `false` |
| prometheus.defaultRules.rules.kubeApiserverBurnrate | bool | API Server burn rate alerts for SLO monitoring | `false` |
| prometheus.defaultRules.rules.kubeApiserverHistogram | bool | API Server latency histogram recording rules | `false` |
| prometheus.defaultRules.rules.kubeApiserverSlos | bool | API Server SLO (Service Level Objective) rules | `false` |
| prometheus.defaultRules.rules.kubeControllerManager | bool | Uncomment to enable: SLO-based alerting for API server performance kubeApiserverSlos: true | `false` |
| prometheus.grafana | object | -------------------------------------------------------------------------- Grafana provides visualization dashboards for Prometheus metrics. Enable this section to deploy Grafana with pre-built Kubernetes dashboards. | `(see values.yaml)` |
| prometheus.grafana.additionalDataSources | list | Additional data sources (e.g., Loki for logs) | `[]` |
| prometheus.grafana.admin | object | Use existing secret for admin credentials (recommended for production) | `{"existingSecret":"","passwordKey":"admin-password","userKey":"admin-user"}` |
| prometheus.grafana.adminUser | string | Default admin credentials (change in production!) | `"admin"` |
| prometheus.grafana.dashboardsConfigMaps | object | Custom dashboards can be configured with additional ConfigMaps Format: `<configmap-name>`: `<folder-name>` | `{}` |
| prometheus.grafana.ingress | object | Ingress configuration for external Grafana access | `{"enabled":false}` |
| prometheus.kubeApiServer | object | -------------------------------------------------------------------------- Enable kubeApiServer to collect metrics from the Kubernetes API server. This provides insights into API request latencies, error rates, and throughput. Note: Requires appropriate RBAC permissions and network access to the API server. | `{"enabled":false}` |
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
| secrets | object | Connection secrets for the Union control plane services. | `{"admin":{"clientId":"dataplane-operator","clientSecret":"","create":true,"enable":true}}` |
| secrets.admin.clientId | string | The client id used to authenticate to the control plane.  This will be provided by Union. | `"dataplane-operator"` |
| secrets.admin.clientSecret | string | The client secret used to authenticate to the control plane.  This will be provided by Union. | `""` |
| secrets.admin.create | bool | Create the secret resource containing the client id and secret.  If set to false the user is responsible for creating the secret before the installation. | `true` |
| secrets.admin.enable | bool | Enable or disable the admin secret.  This is used to authenticate to the control plane. | `true` |
| serving | object | Configure app serving and knative. | `(see values.yaml)` |
| serving.auth | object | Union authentication and authorization configuration. | `{"enabled":true}` |
| serving.auth.enabled | bool | Disabling is common if not leveraging Union Cloud SSO. | `true` |
| serving.enabled | bool | Enables the serving components. Installs Knative Serving. Knative-Operator must be running in the cluster for this to work. Enables app serving in operator. | `false` |
| serving.extraConfig | object | Additional configuration for Knative serving | `{}` |
| serving.metrics | bool | Enables scraping of metrics from the serving component | `true` |
| serving.replicas | int | The number of replicas to create for all components for high availability. | `2` |
| serving.resources | object | Resources for serving components | `(see values.yaml)` |
| sparkoperator.enabled | bool |  | `false` |
| sparkoperator.plugin_config | object |  | `{}` |
| storage | object | Object storage configuration used by all Union services. | `(see values.yaml)` |
| storage.accessKey | string | The access key used for object storage. | `""` |
| storage.authType | string | The authentication type.  Currently supports "accesskey" and "iam". | `"accesskey"` |
| storage.bucketName | string | The bucket name used for object storage. | `"{{ .Values.global.METADATA_BUCKET }}"` |
| storage.cache | object | Cache configuration for objects retrieved from object storage. | `{"maxSizeMBs":0,"targetGCPercent":70}` |
| storage.custom | object | Define custom configurations for the object storage.  Only used if the provider is set to "custom". | `{}` |
| storage.disableSSL | bool | Disable SSL for object storage.  This should only used for local/sandbox installations. | `false` |
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
| userRoleAnnotationKey | string | This is the annotation key that is added to service accounts.  Used with GCP and AWS. | `"eks.amazonaws.com/role-arn"` |
| userRoleAnnotationValue | string | This is the value of the annotation key that is added to service accounts. Used with GCP and AWS. | `"arn:aws:iam::ACCOUNT_ID:role/flyte_project_role"` |

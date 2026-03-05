---
title: Dataplane chart
variants: -flyte -byoc +selfmanaged
chart_version: 2026.2.10
weight: 1
---

Deploys the Union dataplane components to onboard a kubernetes cluster to the Union Cloud.

## Chart info

| | |
|---|---|
| **Chart version** | 2026.2.10 |
| **App version** | 2026.2.12 |
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
| config.k8s | object | Kubernetes specific Flyte configuration | `(see values.yaml)` |
| config.k8s.plugins.k8s | object | Configuration section for all K8s specific plugins [Configuration structure](https://pkg.go.dev/github.com/lyft/flyteplugins/go/tasks/pluginmachinery/flytek8s/config) | `(see values.yaml)` |
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
| config.operator.dependenciesHeartbeat.executor | object | Define the propeller health check endpoint. | `{"endpoint":"{{ include \"executor.health.url\" . }}"}` |
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
| executor | object | Executor service configuration for running fast tasks and eager workflows. | `(see values.yaml)` |
| executor.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| executor.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| executor.config | object | Core executor configuration. | `(see values.yaml)` |
| executor.config.cluster | string | Cluster name for the executor. Should match .Values.clusterName. | `"{{ tpl .Values.clusterName . }}"` |
| executor.config.evaluatorCount | int | Number of evaluator goroutines for processing workflow nodes. | `64` |
| executor.config.maxActions | int | Maximum number of concurrent actions the executor can handle. | `2000` |
| executor.config.organization | string | Organization name for the executor. Should match .Values.orgName. | `"{{ tpl .Values.orgName . }}"` |
| executor.config.unionAuth | object | Authentication configuration for eager workflows. | `{"injectSecret":true,"secretName":"EAGER_API_KEY"}` |
| executor.config.unionAuth.injectSecret | bool | Inject an API key secret into eager workflow pods. | `true` |
| executor.config.unionAuth.secretName | string | Name of the environment variable containing the API key secret. | `"EAGER_API_KEY"` |
| executor.config.workerName | string | Name of this executor worker instance. | `"worker1"` |
| executor.enabled | bool | Enable or disable the executor service. | `true` |
| executor.idl2Executor | bool | Use IDL v2 executor protocol. | `true` |
| executor.plugins | object | Plugin configuration for the executor. | `(see values.yaml)` |
| executor.plugins.fasttask | object | Fast task plugin configuration. Enables in-process task execution for reduced overhead. | `(see values.yaml)` |
| executor.plugins.ioutils | object | IO utilities configuration. | `{"remoteFileOutputPaths":{"deckFilename":"report.html"}}` |
| executor.plugins.ioutils.remoteFileOutputPaths.deckFilename | string | Filename for Flyte Deck HTML reports. | `"report.html"` |
| executor.plugins.k8s | object | Kubernetes plugin configuration for the executor. | `{"disable-inject-owner-references":true}` |
| executor.plugins.k8s.disable-inject-owner-references | bool | Disable injecting owner references on task pods (executor manages lifecycle independently). | `true` |
| executor.podEnv | list | Appends additional environment variables to the executor container's spec. | `[]` |
| executor.podLabels | object | Labels to apply to executor pods. | `(see values.yaml)` |
| executor.propeller | object | Propeller node configuration overrides for the executor. | `{"node-config":{"disable-input-file-writes":true}}` |
| executor.propeller.node-config.disable-input-file-writes | bool | Disable writing input files to disk (uses remote storage instead). | `true` |
| executor.raw_config | object | Raw configuration to merge into the executor config. Allows arbitrary overrides. | `{}` |
| executor.resources | object | Resource requests and limits for the executor deployment. | `{"limits":{"cpu":4,"memory":"8Gi"},"requests":{"cpu":1,"memory":"1Gi"}}` |
| executor.selector | object | Label selector for the executor deployment. | `{"matchLabels":{"app":"executor"}}` |
| executor.serviceAccount | object | Service account configuration for the executor. | `{"annotations":{}}` |
| executor.serviceAccount.annotations | object | Annotations to add to the executor service account. | `{}` |
| executor.sharedService | object | Shared service configuration for the executor gRPC/HTTP server. | `(see values.yaml)` |
| executor.sharedService.metrics | object | Metrics configuration for the executor. | `{"scope":"executor:"}` |
| executor.sharedService.metrics.scope | string | Prometheus metrics prefix scope. | `"executor:"` |
| executor.sharedService.security | object | Security configuration for the executor API. | `(see values.yaml)` |
| executor.sharedService.security.allowCors | bool | Enable CORS support. | `true` |
| executor.sharedService.security.allowLocalhostAccess | bool | Allow localhost access without authentication. | `true` |
| executor.sharedService.security.secure | bool | Enable TLS for the executor API. | `false` |
| executor.sharedService.security.useAuth | bool | Require authentication for the executor API. | `false` |
| executor.task_logs | object | Task log configuration for the executor. | `{"plugins":{"logs":{"cloudwatch-enabled":false,"kubernetes-enabled":false}}}` |
| executor.task_logs.plugins.logs.cloudwatch-enabled | bool | One option is to enable cloudwatch logging for EKS, update the region and log group accordingly | `false` |
| executor.task_logs.plugins.logs.kubernetes-enabled | bool | Enable Kubernetes-native log fetching. | `false` |
| extraObjects | list | Extra Kubernetes objects to deploy with the helm chart. Each entry is a raw Kubernetes manifest. | `[]` |
| fluentbit | object | Configuration for fluentbit used for the persistent logging feature. FluentBit runs as a DaemonSet and ships container logs to the persisted-logs/ path in the configured object store. The fluentbit-system service account must have write access to the storage bucket. Grant access using cloud-native identity federation:   AWS (IRSA):     annotations:       eks.amazonaws.com/role-arn: "arn:aws:iam::`<ACCOUNT_ID>`:role/`<ROLE_NAME>`"   Azure (Workload Identity):     annotations:       azure.workload.identity/client-id: "`<CLIENT_ID>`"   GCP (Workload Identity):     annotations:       iam.gke.io/gcp-service-account: "`<GSA_NAME>`@`<PROJECT_ID>`.iam.gserviceaccount.com" See https://www.union.ai/docs/v1/selfmanaged/deployment/configuration/persistent-logs/ | `(see values.yaml)` |
| flyteagent | object | Flyteagent configuration | `{"enabled":false,"plugin_config":{}}` |
| flyteconnector | object | Flyte connector deployment configuration. Connectors provide external service integrations (e.g., Databricks, SageMaker, Snowflake) for Flyte tasks. | `(see values.yaml)` |
| flyteconnector.additionalContainers | list | Appends additional containers to the deployment spec. May include template values. | `[]` |
| flyteconnector.additionalEnvs | list | Appends additional envs to the deployment spec. May include template values | `[]` |
| flyteconnector.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| flyteconnector.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| flyteconnector.affinity | object | affinity for flyteconnector deployment | `{}` |
| flyteconnector.autoscaling | object | Horizontal pod autoscaler configuration for flyteconnector. | `(see values.yaml)` |
| flyteconnector.autoscaling.maxReplicas | int | Maximum number of flyteconnector replicas. | `5` |
| flyteconnector.autoscaling.minReplicas | int | Minimum number of flyteconnector replicas. | `2` |
| flyteconnector.autoscaling.targetCPUUtilizationPercentage | int | Target CPU utilization percentage for scaling. | `80` |
| flyteconnector.autoscaling.targetMemoryUtilizationPercentage | int | Target memory utilization percentage for scaling. | `80` |
| flyteconnector.configPath | string | Default glob string for searching configuration files | `"/etc/flyteconnector/config/*.yaml"` |
| flyteconnector.enabled | bool | Enable or disable the flyteconnector deployment. | `false` |
| flyteconnector.extraArgs | object | Appends extra command line arguments to the main command | `{}` |
| flyteconnector.image | object | Container image configuration for flyteconnector. | `(see values.yaml)` |
| flyteconnector.image.pullPolicy | string | Docker image pull policy. | `"IfNotPresent"` |
| flyteconnector.image.repository | string | Docker image for flyteconnector deployment. | `"ghcr.io/flyteorg/flyte-connectors"` |
| flyteconnector.image.tag | string | Docker image tag for flyteconnector. | `"py3.13-2.0.0b50.dev3-g695bb1db3.d20260122"` |
| flyteconnector.nodeSelector | object | nodeSelector for flyteconnector deployment | `{}` |
| flyteconnector.podAnnotations | object | Annotations for flyteconnector pods | `{}` |
| flyteconnector.ports | object | gRPC port configuration for flyteconnector. | `{"containerPort":8000,"name":"grpc"}` |
| flyteconnector.ports.containerPort | int | Container port for the gRPC service. | `8000` |
| flyteconnector.ports.name | string | Port name. | `"grpc"` |
| flyteconnector.priorityClassName | string | Sets priorityClassName for datacatalog pod(s). | `""` |
| flyteconnector.prometheusPort | object | Prometheus metrics port configuration. | `{"containerPort":9090,"name":"metric"}` |
| flyteconnector.prometheusPort.containerPort | int | Container port for Prometheus metrics. | `9090` |
| flyteconnector.prometheusPort.name | string | Port name. | `"metric"` |
| flyteconnector.replicaCount | int | Replicas count for flyteconnector deployment. | `2` |
| flyteconnector.resources | object | Default resources requests and limits for flyteconnector deployment | `(see values.yaml)` |
| flyteconnector.service | object | Service settings for flyteconnector | `{"clusterIP":"None","type":"ClusterIP"}` |
| flyteconnector.serviceAccount | object | Configuration for service accounts for flyteconnector | `{"annotations":{},"create":true,"imagePullSecrets":[]}` |
| flyteconnector.serviceAccount.annotations | object | Annotations for ServiceAccount attached to flyteconnector pods | `{}` |
| flyteconnector.serviceAccount.create | bool | Should a service account be created for flyteconnector | `true` |
| flyteconnector.serviceAccount.imagePullSecrets | list | ImagePullSecrets to automatically assign to the service account | `[]` |
| flyteconnector.tolerations | list | tolerations for flyteconnector deployment | `[]` |
| flytepropeller | object | Flytepropeller configuration. Propeller is the workflow execution engine that processes registered workflows by evaluating node dependencies and launching task pods. | `(see values.yaml)` |
| flytepropeller.additionalContainers | object | Additional sidecar containers to add to the propeller pod. | `{}` |
| flytepropeller.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| flytepropeller.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| flytepropeller.affinity | object | affinity for Flytepropeller deployment. | `{}` |
| flytepropeller.cacheSizeMbs | int | Maximum size in MiB for the in-memory blob cache. 0 disables caching. | `0` |
| flytepropeller.configPath | string | Default regex string for searching configuration files. | `"/etc/flyte/config/*.yaml"` |
| flytepropeller.enabled | bool | Enable or disable the Flytepropeller deployment. | `true` |
| flytepropeller.extraArgs | object | Extra arguments to pass to propeller. | `{}` |
| flytepropeller.nodeName | string | nodeName constraints for Flytepropeller deployment. | `""` |
| flytepropeller.nodeSelector | object | nodeSelector for Flytepropeller deployment. | `{}` |
| flytepropeller.podAnnotations | object | Annotations for Flytepropeller pods. | `{}` |
| flytepropeller.podEnv | object | Additional environment variables for propeller pods. | `{}` |
| flytepropeller.podLabels | object | Labels for the Flytepropeller pods. | `{}` |
| flytepropeller.priorityClassName | string | PriorityClassName for Flytepropeller pods. Set to "system-cluster-critical" to ensure propeller is scheduled even under resource pressure. | `"system-cluster-critical"` |
| flytepropeller.replicaCount | int | Replicas count for Flytepropeller deployment. | `1` |
| flytepropeller.resources | object | Default resources requests and limits for Flytepropeller deployment. | `{"limits":{"cpu":"3","memory":"3Gi"},"requests":{"cpu":"1","memory":"1Gi"}}` |
| flytepropeller.secretName | string | Name of the Kubernetes secret containing authentication credentials. | `"union-secret-auth"` |
| flytepropeller.service | object | Service configuration for propeller. | `(see values.yaml)` |
| flytepropeller.service.additionalPorts | list | Additional ports to expose on the propeller service. | `[{"name":"fasttask","port":15605,"protocol":"TCP","targetPort":15605}]` |
| flytepropeller.service.enabled | bool | Enable the propeller Kubernetes service. | `true` |
| flytepropeller.serviceAccount | object | Configuration for service accounts for FlytePropeller. | `{"annotations":{},"imagePullSecrets":[]}` |
| flytepropeller.serviceAccount.annotations | object | Annotations for ServiceAccount attached to FlytePropeller pods. | `{}` |
| flytepropeller.serviceAccount.imagePullSecrets | list | ImagePullSecrets to automatically assign to the service account. | `[]` |
| flytepropeller.terminationMessagePolicy | string | Override the termination message policy for propeller pods. | `""` |
| flytepropeller.tolerations | list | tolerations for Flytepropeller deployment. | `[]` |
| flytepropeller.topologySpreadConstraints | object | topologySpreadConstraints for Flytepropeller deployment. | `{}` |
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
| flytepropellerwebhook.webhook.webhooks.managedImage.objectSelector | object | Object selector for the webhook (matchExpressions) | `(see values.yaml)` |
| flytepropellerwebhook.webhook.webhooks.managedImage.path | string | Path for the webhook | `"/mutate--v1-pod/managed-image"` |
| flytepropellerwebhook.webhook.webhooks.secrets | object | Secrets injection webhook configuration | `(see values.yaml)` |
| flytepropellerwebhook.webhook.webhooks.secrets.name | string | Name of the webhook | `"flyte-pod-webhook.flyte.org"` |
| flytepropellerwebhook.webhook.webhooks.secrets.objectSelector | object | Object selector for the webhook | `{"matchLabels":{"inject-flyte-secrets":"true","organization":"{{ tpl .Values.orgName . }}"}}` |
| flytepropellerwebhook.webhook.webhooks.secrets.path | string | Path for the webhook | `"/mutate--v1-pod/secrets"` |
| fullnameOverride | string | Override the chart fullname. | `""` |
| global.CLIENT_ID | string | Client ID for dataplane authentication. Provided by Union team. | `""` |
| global.CLUSTER_NAME | string | Unique cluster identifier. Format: Lowercase alphanumeric with hyphens. Example: "prod-us-east-1". Must be unique within your organization. | `""` |
| global.FAST_REGISTRATION_BUCKET | string | S3 bucket for code uploads. Example: "my-union-fast-registration-bucket". Can be same as metadata bucket or separate. | `""` |
| global.METADATA_BUCKET | string | S3 bucket for workflow metadata. Example: "my-union-metadata-bucket". Bucket must exist before deployment. | `""` |
| global.ORG_NAME | string | Organization name. Format: RFC 1123 compliant (lowercase alphanumeric and hyphens). Example: "acme-corp". Provided by Union team. | `""` |
| global.UNION_CONTROL_PLANE_HOST | string | Union control plane hostname. Format: "hostname" (no protocol prefix for standard BYOC). Example: "mycompany.unionai.cloud". Provided by Union team for BYOC deployments. | `""` |
| host | string | Set the control plane host for your Union dataplane installation.  This will be provided by Union. | `"{{ .Values.global.UNION_CONTROL_PLANE_HOST }}"` |
| image | object | Container image configuration for Union services. | `(see values.yaml)` |
| image.flytecopilot | object | Flytecopilot sidecar image configuration. Copilot handles data I/O for task pods. | `{"pullPolicy":"IfNotPresent","repository":"cr.flyte.org/flyteorg/flytecopilot","tag":"v1.14.1"}` |
| image.flytecopilot.pullPolicy | string | Image pull policy. | `"IfNotPresent"` |
| image.flytecopilot.repository | string | Image repository. | `"cr.flyte.org/flyteorg/flytecopilot"` |
| image.flytecopilot.tag | string | Image tag. | `"v1.14.1"` |
| image.kubeStateMetrics | object | Kube-state-metrics image configuration. | `(see values.yaml)` |
| image.kubeStateMetrics.pullPolicy | string | Image pull policy. | `"IfNotPresent"` |
| image.kubeStateMetrics.repository | string | Image repository. | `"registry.k8s.io/kube-state-metrics/kube-state-metrics"` |
| image.kubeStateMetrics.tag | string | Image tag. | `"v2.11.0"` |
| image.union | object | Image repository for the operator and union services. | `{"pullPolicy":"IfNotPresent","repository":"public.ecr.aws/p0i0a9q8/unionoperator","tag":""}` |
| image.union.pullPolicy | string | Image pull policy. | `"IfNotPresent"` |
| image.union.repository | string | Image repository. | `"public.ecr.aws/p0i0a9q8/unionoperator"` |
| image.union.tag | string | Image tag. Defaults to the chart appVersion if empty. | `""` |
| imageBuilder | object | Image builder configuration for building container images from Flyte ImageSpec. | `(see values.yaml)` |
| imageBuilder.authenticationType | string | How build-image task and operator proxy will attempt to authenticate to the container registry. Supported values: "noop" (no auth), "google" (docker-credential-gcr), "aws" (docker-credential-ecr-login), "azure" (az acr login, requires Azure Workload Identity). | `"noop"` |
| imageBuilder.buildkit | object | BuildKit daemon configuration for container image builds. | `(see values.yaml)` |
| imageBuilder.buildkit.additionalVolumeMounts | list | Additional volume mounts to add to the buildkit container. | `[]` |
| imageBuilder.buildkit.additionalVolumes | list | Additional volumes to add to the buildkit pod. | `[]` |
| imageBuilder.buildkit.autoscaling | object | Buildkit HPA configuration. | `{"enabled":false,"maxReplicas":2,"minReplicas":1,"targetCPUUtilizationPercentage":60}` |
| imageBuilder.buildkit.autoscaling.enabled | bool | Enable HPA for buildkit. | `false` |
| imageBuilder.buildkit.autoscaling.maxReplicas | int | Maximum number of buildkit replicas. | `2` |
| imageBuilder.buildkit.autoscaling.minReplicas | int | Minimum number of buildkit replicas. | `1` |
| imageBuilder.buildkit.autoscaling.targetCPUUtilizationPercentage | int | Target CPU utilization for scaling. Set lower than usual to promote faster scale out and reduce queue times for build requests. | `60` |
| imageBuilder.buildkit.deploymentStrategy | string | Deployment strategy for buildkit deployment. | `"Recreate"` |
| imageBuilder.buildkit.enabled | bool | Enable buildkit service within this release. | `true` |
| imageBuilder.buildkit.fullnameOverride | string | The name to use for the buildkit deployment, service, configmap, etc. | `""` |
| imageBuilder.buildkit.image | object | Buildkit container image configuration. | `{"pullPolicy":"IfNotPresent","repository":"moby/buildkit","tag":"buildx-stable-1"}` |
| imageBuilder.buildkit.image.pullPolicy | string | Image pull policy. | `"IfNotPresent"` |
| imageBuilder.buildkit.image.repository | string | Image repository. | `"moby/buildkit"` |
| imageBuilder.buildkit.image.tag | string | Image tag. When rootless mode is enabled, "-rootless" is appended automatically (e.g. "buildx-stable-1" becomes "buildx-stable-1-rootless") unless the tag already contains "rootless". | `"buildx-stable-1"` |
| imageBuilder.buildkit.log | object | Logging configuration for buildkit. | `{"debug":false,"format":"text"}` |
| imageBuilder.buildkit.log.debug | bool | Enable debug logging. | `false` |
| imageBuilder.buildkit.log.format | string | Log format ("text" or "json"). | `"text"` |
| imageBuilder.buildkit.nodeSelector | object | Node selector for buildkit pods. | `{}` |
| imageBuilder.buildkit.oci | object | OCI worker configuration for buildkit. | `{"maxParallelism":0}` |
| imageBuilder.buildkit.oci.maxParallelism | int | Maximum number of concurrent builds. 0 means unbounded. | `0` |
| imageBuilder.buildkit.pdb | object | Pod disruption budget for buildkit. | `{"minAvailable":1}` |
| imageBuilder.buildkit.pdb.minAvailable | int | Minimum available pods. | `1` |
| imageBuilder.buildkit.podAnnotations | object | Annotations for buildkit pods. | `{}` |
| imageBuilder.buildkit.podEnv | list | Appends additional environment variables to the buildkit container's spec. | `[]` |
| imageBuilder.buildkit.replicaCount | int | Replicas count for Buildkit deployment. | `1` |
| imageBuilder.buildkit.resources | object | Resource requests and limits for the buildkit container. | `{"requests":{"cpu":1,"ephemeral-storage":"20Gi","memory":"1Gi"}}` |
| imageBuilder.buildkit.rootless | bool | Run buildkit in rootless mode (non-privileged). Uses the moby/buildkit rootless image variant which bundles RootlessKit to set up user namespaces. Requires kernel >= 5.11 with unprivileged user namespace support. | `true` |
| imageBuilder.buildkit.service | object | Service configuration for buildkit. | `{"annotations":{},"loadbalancerIp":"","port":1234,"type":"ClusterIP"}` |
| imageBuilder.buildkit.service.annotations | object | Service annotations. | `{}` |
| imageBuilder.buildkit.service.loadbalancerIp | string | Static IP address for load balancer (only used with LoadBalancer type). | `""` |
| imageBuilder.buildkit.service.port | int | Service port. | `1234` |
| imageBuilder.buildkit.service.type | string | Service type. | `"ClusterIP"` |
| imageBuilder.buildkit.tolerations | list | Tolerations for buildkit pods. | `[]` |
| imageBuilder.buildkitUri | string | The URI of the buildkitd service. Used for externally managed buildkitd services. Leaving empty and setting imageBuilder.buildkit.enabled to true will create a buildkitd service. E.g. "tcp://buildkitd.buildkit.svc.cluster.local:1234" | `""` |
| imageBuilder.defaultRepository | string | The default repository to publish images to when "registry" is not specified with imagespec. The build-image task will fail unless "registry" is specified or a default repository is provided. | `""` |
| imageBuilder.enabled | bool | Enable or disable the image builder feature. | `true` |
| imageBuilder.targetConfigMapName | string | The config map build-image container task attempts to reference. Should not change unless coordinated with Union technical support. | `"build-image-config"` |
| ingress | object | Ingress configuration for exposing dataplane services externally. Enable this when not using Cloudflare tunnels for service access. | `(see values.yaml)` |
| ingress-nginx | object | Ingress-nginx subchart configuration. Disabled by default; enable if you need an ingress controller for dataplane services instead of Cloudflare tunnels. | `(see values.yaml)` |
| ingress-nginx.enabled | bool | Enable or disable the ingress-nginx controller subchart. | `false` |
| ingress.dataproxy | object | Dataproxy specific ingress configuration. | `{"annotations":{},"class":"","hostOverride":"","tls":{}}` |
| ingress.dataproxy.annotations | object | Annotations to apply to the ingress resource. | `{}` |
| ingress.dataproxy.class | string | Ingress class name. | `""` |
| ingress.dataproxy.hostOverride | string | Override the ingress host. Can reference Kubernetes service DNS, e.g. dataproxy-service.{{ .Release.Namespace }}.svc.cluster.local | `""` |
| ingress.dataproxy.tls | object | Ingress TLS configuration. | `{}` |
| ingress.enabled | bool | Enable or disable ingress resources. | `false` |
| ingress.host | string | Default host for ingress rules. Omitted if empty. | `""` |
| ingress.serving | object | Serving specific ingress configuration. | `{"annotations":{},"class":"","hostOverride":"","tls":{}}` |
| ingress.serving.annotations | object | Annotations to apply to the ingress resource. | `{}` |
| ingress.serving.class | string | Ingress class name. | `""` |
| ingress.serving.hostOverride | string | (Optional) Host override for serving ingress rule. Defaults to *.apps.{{ .Values.host }}. | `""` |
| ingress.serving.tls | object | Ingress TLS configuration. | `{}` |
| knative-operator | object | Knative operator subchart. Required for app serving. | `{"crds":{"install":true},"enabled":false}` |
| knative-operator.crds | object | Install Knative CRDs. | `{"install":true}` |
| knative-operator.enabled | bool | Enable or disable the Knative operator. Must be enabled when serving.enabled is true. | `false` |
| low_privilege | bool | Scopes the deployment, permissions and actions created into a single namespace and avoids any deployments that would  require additional permissions on the cluster. This limits the functionality though. | `false` |
| metrics-server | object | Enable or disable the metrics-server subchart. Only needed if your cluster does not already have a metrics server. | `{"enabled":false}` |
| monitoring | object | Global monitoring toggle. When disabled, skips creation of ServiceMonitor and related monitoring resources. | `{"enabled":true}` |
| monitoring.enabled | bool | Enable or disable monitoring resource creation. | `true` |
| nameOverride | string | Override the chart name. | `""` |
| namespace_mapping | object | Custom namespace mapping for mapping Union runs to Kubernetes namespaces. | `{}` |
| namespaces | object | Namespace management configuration. | `{"enabled":true}` |
| namespaces.enabled | bool | Automatically create the release namespace if it does not exist. | `true` |
| nodeobserver | object | Node observer DaemonSet configuration. Monitors node health and critical DaemonSet availability to detect infrastructure issues affecting workflow execution. | `(see values.yaml)` |
| nodeobserver.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| nodeobserver.additionalVolumes | list | Appends additional volumes to the daemonset spec. May include template values. | `[]` |
| nodeobserver.affinity | object | affinity configurations for the pods associated with nodeobserver services | `{}` |
| nodeobserver.config | object | Nodeobserver configuration. | `{"criticalDaemonSets":[]}` |
| nodeobserver.config.criticalDaemonSets | list | List of critical DaemonSets to monitor. Nodeobserver will report nodes as unhealthy if these DaemonSets are not running. | `[]` |
| nodeobserver.enabled | bool | Enable or disable nodeobserver. | `false` |
| nodeobserver.nodeName | string | nodeName constraints for the pods associated with nodeobserver services | `""` |
| nodeobserver.nodeSelector | object | nodeSelector constraints for the pods associated with nodeobserver services | `{}` |
| nodeobserver.podAnnotations | object | Additional pod annotations for the nodeobserver services | `{}` |
| nodeobserver.podEnv | list | Additional pod environment variables for the nodeobserver services | `(see values.yaml)` |
| nodeobserver.podSecurityContext | object | Pod-level security context for the nodeobserver. | `{}` |
| nodeobserver.resources | object | Kubernetes resource configuration for the nodeobserver service | `{"limits":{"cpu":"1","memory":"500Mi"},"requests":{"cpu":"500m","memory":"100Mi"}}` |
| nodeobserver.securityContext | object | Container-level security context for the nodeobserver. Requires privileged access for node-level inspection. | `{"capabilities":{"add":["SYS_ADMIN"]},"privileged":true,"runAsNonRoot":false,"runAsUser":0}` |
| nodeobserver.serviceAccount | object | Service account configuration for the nodeobserver. | `{"annotations":{},"name":""}` |
| nodeobserver.serviceAccount.annotations | object | Annotations for the nodeobserver service account. | `{}` |
| nodeobserver.serviceAccount.name | string | Override the service account name for the nodeobserver. | `""` |
| nodeobserver.tolerations | list | tolerations for the pods associated with nodeobserver services | `[{"effect":"NoSchedule","operator":"Exists"}]` |
| nodeobserver.topologySpreadConstraints | object | topologySpreadConstraints for the pods associated with nodeobserver services | `{}` |
| objectStore | object | Union Object Store service configuration. Provides an internal API for accessing object storage. | `{"service":{"grpcPort":8089,"httpPort":8080}}` |
| objectStore.service | object | Service port configuration. | `{"grpcPort":8089,"httpPort":8080}` |
| objectStore.service.grpcPort | int | gRPC port for the object store service. | `8089` |
| objectStore.service.httpPort | int | HTTP port for the object store service. | `8080` |
| opencost | object | OpenCost subchart configuration for cost allocation and monitoring. | `(see values.yaml)` |
| opencost.enabled | bool | Enable or disable the opencost installation. | `true` |
| opencost.opencost | object | OpenCost application configuration. | `(see values.yaml)` |
| operator | object | Union operator deployment configuration. The operator manages cluster lifecycle, usage reporting, heartbeat checks, and tunnel connectivity to the Union control plane. | `(see values.yaml)` |
| operator.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| operator.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| operator.affinity | object | affinity configurations for the operator pods. | `{}` |
| operator.autoscaling | object | Horizontal pod autoscaler configuration for the operator. | `{"enabled":false}` |
| operator.autoscaling.enabled | bool | Enable HPA for the operator deployment. | `false` |
| operator.enableTunnelService | bool | Enable the Cloudflare tunnel service for secure control plane connectivity. | `true` |
| operator.imagePullSecrets | list | Image pull secrets for the operator deployment. | `[]` |
| operator.nodeName | string | nodeName constraints for the operator pods. | `""` |
| operator.nodeSelector | object | nodeSelector constraints for the operator pods. | `{}` |
| operator.podAnnotations | object | Annotations for operator pods. | `{}` |
| operator.podEnv | object | Additional environment variables for operator pods. | `{}` |
| operator.podLabels | object | Labels for operator pods. | `{}` |
| operator.podSecurityContext | object | Pod-level security context for the operator. | `{}` |
| operator.priorityClassName | string | PriorityClassName for operator pods. | `""` |
| operator.replicas | int | Number of operator replicas. | `1` |
| operator.resources | object | Resource requests and limits for the operator deployment. | `{"limits":{"cpu":"2","memory":"3Gi"},"requests":{"cpu":"1","memory":"1Gi"}}` |
| operator.secretName | string | Name of the Kubernetes secret containing authentication credentials. | `"union-secret-auth"` |
| operator.securityContext | object | Container-level security context for the operator. | `{}` |
| operator.serviceAccount | object | Service account configuration for the operator. | `{"annotations":{},"create":true,"name":"operator-system"}` |
| operator.serviceAccount.annotations | object | Annotations for the operator service account (e.g., for cloud IAM role binding). | `{}` |
| operator.serviceAccount.create | bool | Create a dedicated service account for the operator. | `true` |
| operator.serviceAccount.name | string | Name of the operator service account. | `"operator-system"` |
| operator.tolerations | list | tolerations for the operator pods. | `[]` |
| operator.topologySpreadConstraints | object | topologySpreadConstraints for the operator pods. | `{}` |
| orgName | string | Organization name should be provided by Union. | `"{{ .Values.global.ORG_NAME }}"` |
| prometheus | object | Prometheus configuration (kube-prometheus-stack subchart). This section configures kube-prometheus-stack for monitoring the Union dataplane. By default, most Kubernetes component monitoring is disabled to reduce resource usage. Enable specific components as needed for your observability requirements. | `(see values.yaml)` |
| prometheus.additionalPrometheusRulesMap | object | Additional Prometheus recording or alerting rules. | `{}` |
| prometheus.alertmanager | object | Alertmanager configuration. | `{"enabled":false}` |
| prometheus.alertmanager.enabled | bool | Enable or disable the Alertmanager deployment. | `false` |
| prometheus.crds | object | Prometheus Operator CRD configuration. | `{"enabled":true}` |
| prometheus.crds.enabled | bool | Install Prometheus Operator CRDs. | `true` |
| prometheus.defaultRules | object | Default Prometheus alerting and recording rules. | `(see values.yaml)` |
| prometheus.defaultRules.create | bool | Create default alerting and recording rules. | `false` |
| prometheus.defaultRules.rules | object | Disable specific rules by name disabled:   KubeAPIDown: true   KubeAPITerminatedRequests: true | `(see values.yaml)` |
| prometheus.defaultRules.rules.kubeApiserverAvailability | bool | API Server availability alerts (e.g., KubeAPIDown, KubeAPITerminatedRequests) | `false` |
| prometheus.defaultRules.rules.kubeApiserverBurnrate | bool | API Server burn rate alerts for SLO monitoring | `false` |
| prometheus.defaultRules.rules.kubeApiserverHistogram | bool | API Server latency histogram recording rules | `false` |
| prometheus.defaultRules.rules.kubeApiserverSlos | bool | API Server SLO (Service Level Objective) rules | `false` |
| prometheus.defaultRules.rules.kubeControllerManager | bool | Uncomment to enable: SLO-based alerting for API server performance kubeApiserverSlos: true | `false` |
| prometheus.enabled | bool | Enable or disable the kube-prometheus-stack deployment. | `true` |
| prometheus.grafana | object | Grafana configuration for visualization dashboards. | `(see values.yaml)` |
| prometheus.grafana.additionalDataSources | list | Additional data sources (e.g., Loki for logs) | `[]` |
| prometheus.grafana.admin | object | Use existing secret for admin credentials (recommended for production) | `{"existingSecret":"","passwordKey":"admin-password","userKey":"admin-user"}` |
| prometheus.grafana.adminPassword | string | Default admin password (change in production!). | `"union-dataplane"` |
| prometheus.grafana.adminUser | string | Default admin username (change in production!). | `"admin"` |
| prometheus.grafana.dashboardsConfigMaps | object | Custom dashboards can be configured with additional ConfigMaps Format: `<configmap-name>`: `<folder-name>` | `{}` |
| prometheus.grafana.enabled | bool | Enable or disable the Grafana deployment. | `false` |
| prometheus.grafana.ingress | object | Ingress configuration for external Grafana access | `{"enabled":false}` |
| prometheus.ingress | object | Prometheus ingress configuration for external access to the Prometheus UI. | `{"annotations":{},"enabled":false,"hosts":[]}` |
| prometheus.ingress.annotations | object | Annotations for the Prometheus ingress resource. | `{}` |
| prometheus.ingress.enabled | bool | Enable or disable ingress for Prometheus. | `false` |
| prometheus.ingress.hosts | list | Hosts for the Prometheus ingress resource. | `[]` |
| prometheus.kube-state-metrics | object | Kube-state-metrics subchart configuration. Provides Kubernetes object metrics to Prometheus. | `(see values.yaml)` |
| prometheus.kubeApiServer | object | -------------------------------------------------------------------------- Enable kubeApiServer to collect metrics from the Kubernetes API server. This provides insights into API request latencies, error rates, and throughput. Note: Requires appropriate RBAC permissions and network access to the API server. | `{"enabled":false}` |
| prometheus.nodeExporter | object | Node exporter configuration for collecting host-level metrics. | `{"enabled":false}` |
| prometheus.nodeExporter.enabled | bool | Enable or disable the node exporter DaemonSet. | `false` |
| prometheus.prometheus | object | Prometheus server configuration. | `(see values.yaml)` |
| prometheus.prometheus-node-exporter | object | Prometheus node-exporter subchart configuration. | `{"namespaceOverride":"kube-system"}` |
| prometheus.prometheus.enabled | bool | Enable the Prometheus server. | `true` |
| prometheus.prometheus.prometheusSpec | object | Prometheus server spec configuration. | `(see values.yaml)` |
| prometheus.prometheus.prometheusSpec.maximumStartupDurationSeconds | int | Maximum time in seconds for Prometheus startup before it is considered failed. | `900` |
| prometheus.prometheus.prometheusSpec.resources | object | Resource requests and limits for the Prometheus server. | `{"limits":{"cpu":"3","memory":"3500Mi"},"requests":{"cpu":"1","memory":"1Gi"}}` |
| prometheus.prometheus.prometheusSpec.retention | string | How long to retain metrics data. | `"3d"` |
| prometheus.prometheus.prometheusSpec.routePrefix | string | URL path prefix for the Prometheus web UI. | `"/prometheus/"` |
| prometheus.prometheusOperator | object | Prometheus Operator configuration. | `{"fullnameOverride":"prometheus-operator"}` |
| proxy | object | Union operator proxy configuration. The proxy serves as the dataplane's API gateway, handling data uploads/downloads, secret management, and image building requests. | `(see values.yaml)` |
| proxy.additionalVolumeMounts | list | Appends additional volume mounts to the main container's spec. May include template values. | `[]` |
| proxy.additionalVolumes | list | Appends additional volumes to the deployment spec. May include template values. | `[]` |
| proxy.affinity | object | affinity configurations for the proxy pods. | `{}` |
| proxy.autoscaling | object | Horizontal pod autoscaler configuration for the proxy. | `{"enabled":false,"maxReplicas":10,"minReplicas":1,"targetCPUUtilizationPercentage":80}` |
| proxy.autoscaling.enabled | bool | Enable HPA for the proxy deployment. | `false` |
| proxy.autoscaling.maxReplicas | int | Maximum number of proxy replicas. | `10` |
| proxy.autoscaling.minReplicas | int | Minimum number of proxy replicas. | `1` |
| proxy.autoscaling.targetCPUUtilizationPercentage | int | Target CPU utilization percentage for scaling. | `80` |
| proxy.enableTunnelService | bool | Enable the Cloudflare tunnel service for secure control plane connectivity. | `true` |
| proxy.imagePullSecrets | list | Image pull secrets for the proxy deployment. | `[]` |
| proxy.nodeName | string | nodeName constraint for the proxy pods. | `""` |
| proxy.nodeSelector | object | nodeSelector constraints for the proxy pods. | `{}` |
| proxy.podAnnotations | object | Annotations for proxy pods. | `{}` |
| proxy.podEnv | object | Additional environment variables for proxy pods. | `{}` |
| proxy.podLabels | object | Labels for proxy pods. | `{}` |
| proxy.podSecurityContext | object | Pod-level security context for the proxy. | `{}` |
| proxy.priorityClassName | string | PriorityClassName for proxy pods. | `""` |
| proxy.replicas | int | Number of proxy replicas. | `1` |
| proxy.resources | object | Resource requests and limits for the proxy container. | `{"limits":{"cpu":"3","memory":"3Gi"},"requests":{"cpu":"500m","memory":"500Mi"}}` |
| proxy.secretManager | object | Secret manager configuration for the proxy. Manages user-defined secrets for workflows. | `{"enabled":true,"namespace":"","type":"K8s"}` |
| proxy.secretManager.enabled | bool | Enable secret manager support for storing and injecting workflow secrets. | `true` |
| proxy.secretManager.namespace | string | Set the namespace for union managed secrets created through the native Kubernetes secret manager. If the namespace is not set, the release namespace will be used. | `""` |
| proxy.secretManager.type | string | The type of secret manager to use. Supported: "K8s" (native Kubernetes secrets). | `"K8s"` |
| proxy.secretName | string | Name of the Kubernetes secret containing authentication credentials. | `"union-secret-auth"` |
| proxy.securityContext | object | Container-level security context for the proxy. | `{}` |
| proxy.serviceAccount | object | Service account configuration for the proxy. | `{"annotations":{},"create":true,"name":"proxy-system"}` |
| proxy.serviceAccount.annotations | object | Annotations for the proxy service account (e.g., for cloud IAM role binding). | `{}` |
| proxy.serviceAccount.create | bool | Create a dedicated service account for the proxy. | `true` |
| proxy.serviceAccount.name | string | Name of the proxy service account. | `"proxy-system"` |
| proxy.tolerations | list | tolerations for the proxy pods. | `[]` |
| proxy.topologySpreadConstraints | object | topologySpreadConstraints for the proxy pods. | `{}` |
| proxy.tunnel_resources | object | Resource requests and limits for the Cloudflare tunnel sidecar container. | `{"limits":{"cpu":"3","memory":"3Gi"},"requests":{"cpu":"500m","memory":"500Mi"}}` |
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
| sparkoperator | object | Spark operator integration configuration. | `{"enabled":false,"plugin_config":{}}` |
| sparkoperator.enabled | bool | Enable or disable the Spark operator integration. | `false` |
| sparkoperator.plugin_config | object | Plugin configuration for the Spark operator. | `{}` |
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

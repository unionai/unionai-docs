---
title: Plugin setup
weight: 6
variants: -flyte -serverless +byoc +selfmanaged
---

# Plugin setup

{{< key product_name >}} supports various distributed computing plugins that extend the platform's capabilities for running specialized workloads. This guide covers how to install and configure the Dask and Ray plugins in your cluster.

## Dask

[Dask](https://www.dask.org/) is a flexible parallel computing library for analytics. The Dask plugin enables you to run distributed Dask workloads in your {{< key product_name >}} cluster.

For detailed information on using Dask in your workflows, see the [Dask plugin documentation]({{< relref "/integrations/native-backend-plugins/k8s-dask-plugin" >}}).

### Installing the Dask Operator

First, install the Dask Kubernetes operator using Helm:

```bash
helm repo add dask https://helm.dask.org
helm repo update
helm upgrade --install dask-kubernetes-operator dask/dask-kubernetes-operator \
  --create-namespace \
  --namespace dask-operator \
  --version 2024.4.1 \
  --timeout 600s
```

### Configuring Dask for AWS

Add the following configuration to your Helm values file:

```yaml
enabled_plugins:
  tasks:
    task-plugins:
      enabled-plugins:
        - agent-service
        - container
        - dask
        - echo
        - k8s-array
        - sidecar
      default-for-task-types:
        dask: dask

task_logs:
  plugins:
    dask:
      logs:
        cloudwatch-enabled: false
        kubernetes-enabled: false
        templates:
          - displayName: "Cloudwatch Logs"
            scheme: TaskExecution
            templateUris:
              - 'https://{{ ternary .Values.storage.s3.region "us-east-2" (eq .Values.storage.type "s3") }}.console.aws.amazon.com/cloudwatch/home?region={{ ternary .Values.storage.s3.region "us-east-2" (eq .Values.storage.type "s3") }}#logsV2:log-groups/log-group/$252Funion$252Fcluster-{{.Values.clusterName}}$252Ftask/log-events/kube.namespace-{{`{{.namespace}}`}}.pod-{{`{{.podName}}`}}.cont-job-runner'
          - displayName: Dask Dashboard
            linkType: dashboard
            scheme: TaskExecution
            templateUris:
              - "/dataplane/dask/v1/generated_name/task/{{`{{.executionProject}}`}}/{{`{{.executionDomain}}`}}/{{`{{.executionName}}`}}/{{`{{.nodeID}}`}}/{{`{{.taskRetryAttempt}}`}}/{{.Values.clusterName}}/{{`{{.namespace}}`}}/{{`{{.taskProject}}`}}/{{`{{.taskDomain}}`}}/{{`{{.taskID}}`}}/{{`{{.taskVersion}}`}}/{{`{{.generatedName}}`}}/status"
          - displayName: Dask Runner logs
            scheme: TaskExecution
            templateUris:
              - "/console/projects/{{`{{.executionProject}}`}}/domains/{{`{{.executionDomain}}`}}/executions/{{`{{.executionName}}`}}/nodeId/{{`{{.nodeID}}`}}/taskId/{{`{{.taskID}}`}}/attempt/{{`{{.taskRetryAttempt}}`}}/view/logs?duration=all&fromExecutionNav=true"
```

### Configuring Dask for GCP

Add the following configuration to your Helm values file:

```yaml
enabled_plugins:
  tasks:
    task-plugins:
      enabled-plugins:
        - agent-service
        - container
        - dask
        - echo
        - k8s-array
        - sidecar
      default-for-task-types:
        dask: dask

task_logs:
  plugins:
    dask:
      logs:
        cloudwatch-enabled: false
        kubernetes-enabled: false
        templates:
          - displayName: "Stackdriver Logs"
            scheme: TaskExecution
            templateUris:
              - "https://console.cloud.google.com/logs/query;query=resource.labels.namespace_name%3D%22{{`{{.namespace}}`}}%22%0Aresource.labels.pod_name%3D%22{{`{{.podName}}`}}%22%0Aresource.labels.container_name%3D%22job-runner%22?project={{.Values.storage.gcs.projectId}}&angularJsUrl=%2Flogs%2Fviewer%3Fproject%3D{{.Values.storage.gcs.projectId}}"
          - displayName: Dask Dashboard
            linkType: dashboard
            scheme: TaskExecution
            templateUris:
              - "/dataplane/dask/v1/generated_name/task/{{`{{.executionProject}}`}}/{{`{{.executionDomain}}`}}/{{`{{.executionName}}`}}/{{`{{.nodeID}}`}}/{{`{{.taskRetryAttempt}}`}}/{{.Values.clusterName}}/{{`{{.namespace}}`}}/{{`{{.taskProject}}`}}/{{`{{.taskDomain}}`}}/{{`{{.taskID}}`}}/{{`{{.taskVersion}}`}}/{{`{{.generatedName}}`}}/status"
          - displayName: Dask Runner logs
            scheme: TaskExecution
            templateUris:
              - "/console/projects/{{`{{.executionProject}}`}}/domains/{{`{{.executionDomain}}`}}/executions/{{`{{.executionName}}`}}/nodeId/{{`{{.nodeID}}`}}/taskId/{{`{{.taskID}}`}}/attempt/{{`{{.taskRetryAttempt}}`}}/view/logs?duration=all&fromExecutionNav=true"
```

## Ray

[Ray](https://www.ray.io/) is a unified framework for scaling AI and Python applications. The Ray plugin enables you to run distributed Ray workloads in your {{< key product_name >}} cluster.

For detailed information on using Ray in your workflows, see the [Ray plugin documentation]({{< relref "/integrations/native-backend-plugins/ray-plugin" >}}).

### Installing the Ray Operator

First, install the KubeRay operator:

```bash
kubectl create -k "https://github.com/ray-project/kuberay/ray-operator/config/crd?ref=v1.1.0"
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update
helm upgrade --install kuberay-operator kuberay/kuberay-operator \
  --create-namespace \
  --namespace kuberay-operator \
  --version 1.4.0 \
  --set resources.limits.memory=1Gi \
  --skip-crds
```

### Configuring Ray for AWS

Add the following configuration to your Helm values file:

```yaml
enabled_plugins:
  tasks:
    task-plugins:
      enabled-plugins:
        - agent-service
        - container
        - echo
        - k8s-array
        - ray
        - sidecar
      default-for-task-types:
        ray: ray

task_logs:
  plugins:
    ray:
      logs:
        templates:
          - displayName: "Ray Dashboard"
            linkType: dashboard
            scheme: TaskExecution
            templateUris:
              - "/dataplane/ray/v1/generated_name/task/{{`{{.executionProject}}`}}/{{`{{.executionDomain}}`}}/{{`{{.executionName}}`}}/{{`{{.nodeID}}`}}/{{`{{.taskRetryAttempt}}`}}/{{.Values.clusterName}}/{{`{{.namespace}}`}}/{{`{{.taskProject}}`}}/{{`{{.taskDomain}}`}}/{{`{{.taskID}}`}}/{{`{{.taskVersion}}`}}/{{`{{.generatedName}}`}}/"
          - displayName: "Cloudwatch Logs (Ray All)"
            scheme: TaskExecution
            templateUris:
              - 'https://{{ternary .Values.storage.s3.region "us-east-2" (eq .Values.storage.type "s3")}}.console.aws.amazon.com/cloudwatch/home?region={{ternary .Values.storage.s3.region "us-east-2" (eq .Values.storage.type "s3")}}#logsV2:log-groups/log-group/$252Funion$252Fcluster-{{.Values.clusterName}}$252Ftask$3FlogStreamNameFilter$3Dkube.namespace-{{`{{.namespace}}`}}.pod-{{`{{.executionName}}`}}-{{`{{.nodeID}}`}}-{{`{{.taskRetryAttempt}}`}}'
          - displayName: Ray Head logs
            scheme: TaskExecution
            templateUris:
              - "/console/projects/{{`{{.executionProject}}`}}/domains/{{`{{.executionDomain}}`}}/executions/{{`{{.executionName}}`}}/nodeId/{{`{{.nodeID}}`}}/taskId/{{`{{.taskID}}`}}/attempt/{{`{{.taskRetryAttempt}}`}}/view/logs?duration=all&fromExecutionNav=true"
```

### Configuring Ray for GCP

Add the following configuration to your Helm values file:

```yaml
enabled_plugins:
  tasks:
    task-plugins:
      enabled-plugins:
        - agent-service
        - container
        - echo
        - k8s-array
        - ray
        - sidecar
      default-for-task-types:
        ray: ray

task_logs:
  plugins:
    ray:
      logs:
        templates:
          - displayName: "Ray Dashboard"
            linkType: dashboard
            scheme: TaskExecution
            templateUris:
              - "/dataplane/ray/v1/generated_name/task/{{`{{.executionProject}}`}}/{{`{{.executionDomain}}`}}/{{`{{.executionName}}`}}/{{`{{.nodeID}}`}}/{{`{{.taskRetryAttempt}}`}}/{{.Values.clusterName}}/{{`{{.namespace}}`}}/{{`{{.taskProject}}`}}/{{`{{.taskDomain}}`}}/{{`{{.taskID}}`}}/{{`{{.taskVersion}}`}}/{{`{{.generatedName}}`}}/"
          - displayName: "Stacktrace Logs (Ray All)"
            scheme: TaskExecution
            templateUris:
              - "https://console.cloud.google.com/logs/query;query=resource.labels.namespace_name%3D%22{{`{{.namespace}}`}}%22%0Aresource.labels.pod_name%3D%7E%22{{`{{.executionName}}`}}-{{`{{.nodeID}}`}}-{{`{{.taskRetryAttempt}}`}}%22?project={{.Values.storage.gcs.projectId}}&angularJsUrl=%2Flogs%2Fviewer%3Fproject%3D{{.Values.storage.gcs.projectId}}"
          - displayName: Ray Head logs
            scheme: TaskExecution
            templateUris:
              - "/console/projects/{{`{{.executionProject}}`}}/domains/{{`{{.executionDomain}}`}}/executions/{{`{{.executionName}}`}}/nodeId/{{`{{.nodeID}}`}}/taskId/{{`{{.taskID}}`}}/attempt/{{`{{.taskRetryAttempt}}`}}/view/logs?duration=all&fromExecutionNav=true"
```

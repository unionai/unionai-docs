---
title: Data plane setup on Azure
weight: 5
variants: -flyte -serverless -byoc +selfmanaged
---

# Data plane setup on Azure

{{< key product_name >}}’s modular architecture allows for great flexibility and control. The customer can decide how many clusters to have, their shape, and who has access to what. All communication is encrypted.  The Union architecture is described on the [Architecture](../../architecture) page.

## Assumptions
* You have a {{< key product_name >}} organization and you know the Control Plane URL for your Organization.
* You have a cluster name provided by or coordinated with Union
* You have a Kubernetes cluster, running one of the most recent three minor K8s versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured an storage bucket(s)
* You have configured your AKS cluster as indicated in the [Cluster Recommendations](./cluster-recommendations.md/#aks) section.


## Prerequisites
* Install [Helm 3](https://helm.sh/docs/intro/install/)
* Install [union](../api-reference/union-cli) and [uctl](../api-reference/uctl-cli).


## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:
```shell
helm repo add unionai https://unionai.github.io/helm-charts/
helm repo update
```

2. Use the `uctl create admin-oauth-app` command to generate a new client and client secret for communicating with your Union control plane:
```shell
uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
uctl create admin-oauth-app
```
* The output will emit the ID, name, and a secret that will be used by the union services to communicate with your control plane.
```shell
 --------------- ---------------- ------------------------------------------------------------------
| CLIENT ID     | CLIENT NAME    | SECRET                                                           |
 --------------- ---------------- ------------------------------------------------------------------
| xxxxxxxxxxxxx | xxxxxxxxxxxxxx | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx |
 --------------- ---------------- ------------------------------------------------------------------
1 rows
```
* Save the secret that is displayed. Union does not store the credentials and it cannot be retrieved later.

3. Create a values file that include, at a minimum, the following fields:

```yaml
host: <UNION_ORG_HOST> # FQDN of the Union control plane, without https://
clusterName: <UNION_CLUSTER_NAME> # Provided by or coordinated with Union
orgName: <ORG_NAME> # Union organization name
additionalPodLabels:
  azure.workload.identity/use: "true"
secrets:
  admin:
    create: true
    clientId: <UNION_CLIENT_ID> # Generated in the previous step
    clientSecret: <UNION_CLIENT_SECRET> # Generated in the previous step
azure:
  tenantId: <YOUR_AZURE_TENANT_ID>
  subscriptionId: <AZURE_SUBSCRIPTION_ID>
  resourceGroupName: <AZURE_RESOURCE_GROUP>
storage:
  provider: "custom"
  custom:
    container: <STORAGE_CONTAINER> # storage_container_name
    connection: {}
    type: stow
    stow:
      kind: azure
      config:
        account: <STORAGE_ACCOUNT_NAME> # storage_account_name
        key: <STORAGE_ACCOUNT_KEY>

# Configure Union workers with managed identity client ID
userRoleAnnotationKey: "azure.workload.identity/client-id"
userRoleAnnotationValue: <WORKERS_CLIENT_ID> #see the Cluster Recommendations section

additionalServiceAccountAnnotations:
  azure.workload.identity/client-id: <SERVICES_CLIENT_ID> # see the Cluster Recommendations section

config:
  k8s:
    plugins:
      k8s:
        default-env-vars:
          - AZURE_STORAGE_ACCOUNT_NAME: <STORAGE_ACCOUNT_NAME> # storage_account_name
        default-labels:
          - azure.workload.identity/use: "true"
        interruptible-tolerations:
        - key: kubernetes.azure.com/scalesetpriority
          value: spot
          operator: Equal
          effect: NoSchedule
        interruptible-node-selector-requirement:
          key: kubernetes.azure.com/scalesetpriority
          operator: In
          values:
            - spot
        non-interruptible-node-selector-requirement:
          key: kubernetes.azure.com/scalesetpriority
          operator: DoesNotExist

  # Azure relies on Workload Identity for authentication.
  # We have to explicitly map domain to namespaces to have a discrete set of
  # Union workspaces (E.g. development, staging, production) to support reliable
  # federated token retrieval.
  namespace_config:
    namespace_mapping:
      template: "{{ domain }}"

  task_logs:
    plugins:
      logs:
        templates:
          - displayName: Task Logs
            scheme: TaskExecution
            templateUris:
              - "/console/projects/{{`{{.executionProject}}`}}/domains/{{`{{.executionDomain}}`}}/executions/{{`{{.executionName}}`}}/nodeId/{{`{{.nodeID}}`}}/taskId/{{`{{.taskID}}`}}/attempt/{{`{{.taskRetryAttempt}}`}}/view/logs?duration=all&fromExecutionNav=true"
        azure-log-templates:
          - displayName: "Azure Logs"
            templateUris:
              - "https://portal.azure.com#@{{.Values.azure.tenantId}}/blade/Microsoft_OperationsManagementSuite_Workspace/Logs.ReactView/resourceId/%2Fsubscriptions%2F{{.Values.azure.subscriptionId}}%2FresourceGroups%2F{{.Values.azure.resourceGroupName}}/source/LogsBlade.AnalyticsShareLinkToQuery/q/"
      k8s-array:
        logs:
          config:
            templates:
              - displayName: Task Logs
                scheme: TaskExecution
                templateUris:
                  - "/console/projects/{{`{{.executionProject}}`}}/domains/{{`{{.executionDomain}}`}}/executions/{{`{{.executionName}}`}}/nodeId/{{`{{.nodeID}}`}}/taskId/{{`{{.taskID}}`}}/attempt/{{`{{.taskRetryAttempt}}`}}/view/logs?duration=all&fromExecutionNav=true"
            azure-log-templates:
              - displayName: "Azure Logs"
                templateUris:
                  - "https://portal.azure.com#@{{.Values.azure.tenantId}}/blade/Microsoft_OperationsManagementSuite_Workspace/Logs.ReactView/resourceId/%%2Fsubscriptions%%2F{{.Values.azure.subscriptionId}}%%2FresourceGroups%%2F{{.Values.azure.resourceGroupName}}/source/LogsBlade.AnalyticsShareLinkToQuery/q/"
      fasttask:
        logs:
          dynamic-log-links:
            - vscode:
                displayName: VSCode
                templateUris:
                  - "/dataplane/pod/v1/generated_name/task/{{`{{.executionProject}}`}}/{{`{{.executionDomain}}`}}/{{`{{.executionName}}`}}/{{`{{.nodeID}}`}}/{{`{{.taskRetryAttempt}}`}}/{{`{{.taskProject}}`}}/{{`{{.taskDomain}}`}}/{{`{{.taskID}}`}}/{{`{{.taskVersion}}`}}/"
          templates:
            - displayName: Task Logs
              scheme: TaskExecution
              templateUris:
                - "/console/projects/{{`{{.executionProject}}`}}/domains/{{`{{.executionDomain}}`}}/executions/{{`{{.executionName}}`}}/nodeId/{{`{{.nodeID}}`}}/taskId/{{`{{.taskID}}`}}/attempt/{{`{{.taskRetryAttempt}}`}}/view/logs?duration=all&fromExecutionNav=true"
          azure-log-templates:
            - displayName: "Azure Logs"
              templateUris:
                - "https://portal.azure.com#@{{.Values.azure.tenantId}}/blade/Microsoft_OperationsManagementSuite_Workspace/Logs.ReactView/resourceId/%2Fsubscriptions%2F{{.Values.azure.subscriptionId}}%2FresourceGroups%2F{{.Values.azure.resourceGroupName}}/source/LogsBlade.AnalyticsShareLinkToQuery/q/"

  operator:
    clusterData:
      metadataBucketPrefix: "abfs://{{.Values.storage.custom.container}}@{{.Values.storage.custom.stow.config.account}}.dfs.core.windows.net"

  proxy:
    smConfig:
      enabled: true
      type: Azure
    persistedLogs:
      sourceType: "AzureLogAnalytics"
      azureLogAnalytics:
        logAnalyticsWorkspaceResourceIdTemplate: "/subscriptions/{{.Values.azure.subscriptionId}}/resourceGroups/{{.Values.azure.resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/union-{{.Values.orgName}}"
```

4. Optionally configure the resource `limits` and `requests` for the different services.  By default these will be set minimally, will vary depending on usage, and follow the Kubernetes `ResourceRequirements` specification.
    * `clusterresourcesync.resources`
    * `flytepropeller.resources`
    * `flytepropellerwebhook.resources`
    * `operator.resources`
    * `proxy.resources`

5. Install the {{< key product_name >}} operator and CRDs:
```shell
helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds
helm upgrade --install unionai-dataplane unionai/dataplane \
    --create-namespace \
    --namespace union \
    --values <YOUR_VALUES_FILE>
```

6. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

```shell
uctl get cluster
 ----------- ------- --------------- -----------
| NAME      | ORG   | STATE         | HEALTH    |
 ----------- ------- --------------- -----------
| <cluster> | <org> | STATE_ENABLED | HEALTHY   |
 ----------- ------- --------------- -----------
1 rows
```
7. You can then register and run some example workflows through your cluster to ensure that it is working correctly.

```shell
uctl register examples --project=union-health-monitoring --domain=development
uctl validate snacks --project=union-health-monitoring --domain=development
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
| NAME                 | LAUNCH PLAN NAME                  | VERSION  | STARTED AT                     | ELAPSED TIME | RESULT    | ERROR MESSAGE |
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
| alskkhcd6wx5m6cqjlwm | basics.hello_world.hello_world_wf | v0.3.341 | 2025-05-09T18:30:02.968183352Z | 4.452440953s | SUCCEEDED |               |
 ---------------------- ----------------------------------- ---------- -------------------------------- -------------- ----------- ---------------
1 rows
```
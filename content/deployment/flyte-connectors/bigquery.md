---
title: BigQuery connector
weight: 9
variants: +flyte -serverless -byoc -selfmanaged
---
# Google BigQuery connector

This guide provides an overview of setting up BigQuery connector in your Flyte deployment.
Please note that the BigQuery connector requires Flyte deployment in the GCP cloud; it is not compatible with demo/AWS/Azure.

## Set up the GCP Flyte cluster

- Ensure you have a functional Flyte cluster running in [GCP](https://docs.flyte.org/en/latest/deployment/gcp/index.html#deployment-gcp).
- Create a service account for BigQuery. For more details, refer to: <https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries>
- Verify that you have the correct kubeconfig and have selected the appropriate Kubernetes context
- Confirm that you have the correct Flytectl configuration at `~/.flyte/config.yaml`

## Specify connector configuration

### flyte-binary

Add the following to your values file:
```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - container
      - sidecar
      - k8s-array
      - connector-service
    default-for-task-types:
      - container: container
      - container_array: k8s-array
      - bigquery_query_job_task: connector-service
```
### flyte-core

Create a file named `values-override.yaml` and add the following configuration to it:

```yaml
configmap:
  enabled_plugins:
    # -- Tasks specific configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#GetConfig)
    tasks:
      # -- Plugins configuration, [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#TaskPluginConfig)
      task-plugins:
        # -- [Enabled Plugins](https://pkg.go.dev/github.com/flyteorg/flyteplugins/go/tasks/config#Config). Enable sagemaker*, athena if you install the backend
        enabled-plugins:
          - container
          - sidecar
          - connector-service
        default-for-task-types:
          container: container
          sidecar: sidecar
          bigquery_query_job_task: connector-service
```
Ensure that flytepropeller has the correct service account for BigQuery.

## Upgrade the Helm release


```bash
helm upgrade <RELEASE_NAME> flyteorg/<HELM_CHART> -n <YOUR_NAMESPACE> --values values-override.yaml

```

Replace ``<RELEASE_NAME>`` with the name of your release (e.g., ``flyte-backend``),
``<YOUR_NAMESPACE>`` with the name of your namespace (e.g., ``flyte``) and `<HELM_CHART>` with `flyte-binary`, `flyte-core ` or `flyte-sandbox`.


Wait for the upgrade to complete. You can check the status of the deployment pods by running the following command:

```bash
kubectl get pods -n flyte
```

Once all the components are up and running, go to the examples section to learn more about how to use Flyte connectors.


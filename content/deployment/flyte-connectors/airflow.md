---
title: Airflow connector
weight: 8
variants: +flyte -serverless -byoc -selfmanaged
---

# Airflow connector

This guide provides an overview of how to set up the Airflow connector in your Flyte deployment.
Please note that you don't need an Airflow cluster to run the Airflow tasks, since Flytekit will automatically compile Airflow tasks to Flyte tasks and execute them on the Flyte cluster.

## Specify connector configuration

### Flyte binary

Add the following to your values file:

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - container
      - sidecar
      - connector-service
    default-for-task-types:
      - container: container
      - airflow: connector-service
```

### flyte-core

Create a file named values-override.yaml and add the following configuration to it:

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
          - k8s-array
          - connector-service
        default-for-task-types:
          container: container
          sidecar: sidecar
          container_array: k8s-array
          airflow: connector-service
```

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

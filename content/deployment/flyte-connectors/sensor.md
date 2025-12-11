---
title: Sensor connector
weight: 16
variants: +flyte -serverless -byoc -selfmanaged
---
# Sensor connector

The [sensor connector](https://docs.flyte.org/en/latest/flytesnacks/examples/sensor/index.html) enables users to continuously check for a file or a condition to be met periodically.
When the condition is met, the sensor will complete.

This guide provides an overview of how to set up the sensor connector in your Flyte deployment.

## Spin up a cluster

### flyte-binary

    You can spin up a demo cluster using the following command:

    ```bash
    flytectl demo start
    ```

    Or install Flyte using the [flyte-binary helm chart](https://docs.flyte.org/en/latest/deployment/deployment/cloud_simple.html).

### flyte-core

    If you've installed Flyte using the [`flyte-core` helm chart](https://github.com/flyteorg/flyte/tree/master/charts/flyte-core), please ensure:

    - You have the correct kubeconfig and have selected the correct Kubernetes context.
    - Confirm that you have the correct Flytectl configuration at `~/.flyte/config.yaml`.

> [!NOTE]
> Add the Flyte chart repo to Helm if you're installing via the Helm charts:
>
> ```bash
> helm repo add flyteorg https://flyteorg.github.io/flyte
> ```

## Specify connector configuration

Enable the sensor connector by adding the following config to the relevant YAML file(s):

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
          - sensor: connector-service
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
              - k8s-array
              - connector-service
            default-for-task-types:
              container: container
              sidecar: sidecar
              container_array: k8s-array
              sensor: connector-service
    ```

## Upgrade the deployment

### Demo cluster

        ```bash
        kubectl rollout restart deployment flyte-sandbox -n flyte
        ```

### flyte-binary

        ```bash
        helm upgrade <RELEASE_NAME> flyteorg/flyte-binary -n <YOUR_NAMESPACE> --values <YOUR_YAML_FILE>
        ```

        Replace `<RELEASE_NAME>` with the name of your release (e.g., `flyte-backend`),
        `<YOUR_NAMESPACE>` with the name of your namespace (e.g., `flyte`),
        and `<YOUR_YAML_FILE>` with the name of your YAML file.

### flyte-core

    ```bash
    helm upgrade <RELEASE_NAME> flyte/flyte-core -n <YOUR_NAMESPACE> --values values-override.yaml
    ```

    Replace `<RELEASE_NAME>` with the name of your release (e.g., `flyte`)
    and `<YOUR_NAMESPACE>` with the name of your namespace (e.g., `flyte`).

Wait for the upgrade to complete.

You can check the status of the deployment pods by running the following command:

```bash
kubectl get pods -n flyte
```
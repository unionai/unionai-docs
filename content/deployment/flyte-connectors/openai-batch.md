---
title: OpenAI Batch connector
weight: 14
variants: +flyte -serverless -byoc -selfmanaged
---

# OpenAI Batch Connector

This guide provides an overview of how to set up the OpenAI Batch connector in your Flyte deployment.

## Specify connector configuration

### flyte-binary

    Edit the relevant YAML file to specify the connector.

    ```bash
    kubectl edit configmap flyte-sandbox-config -n flyte
    ```

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
          - openai-batch: connector-service
    ```

### flyte-core
    Create a file named `values-override.yaml` and add the following configuration to it:

    ```yaml
    configmap:
      enabled_plugins:
        tasks:
          task-plugins:
            enabled-plugins:
              - container
              - sidecar
              - k8s-array
              - connector-service
            default-for-task-types:
              container: container
              sidecar: sidecar
              container_array: k8s-array
              openai-batch: connector-service
    ```

## Add the OpenAI API token

1. Install `flyteconnector` pod using Helm:

    ```bash
    helm repo add flyteorg https://flyteorg.github.io/flyte
    helm install flyteconnector flyteorg/flyteconnector --namespace flyte
    ```

2. Set Your OpenAI API Token as a Secret (Base64 Encoded):

    ```bash
    SECRET_VALUE=$(echo -n "<OPENAI_API_TOKEN>" | base64) && \
    kubectl patch secret flyteconnector -n flyte --patch "{\"data\":{\"flyte_openai_api_key\":\"$SECRET_VALUE\"}}"
    ```

3. Restart the deployment:

    ```bash
    kubectl rollout restart deployment flyteconnector -n flyte
    ```

## Upgrade the Flyte Helm release

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

You can refer to the [documentation](https://docs.flyte.org/en/latest/flytesnacks/examples/openai_batch_connector/index.html)
to run the connector on your Flyte cluster.

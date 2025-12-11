---
title: Snowflake connector
weight: 18
variants: +flyte -serverless -byoc -selfmanaged
---
# Snowflake connector

This guide provides an overview of how to set up the Snowflake connector in your Flyte deployment.

1. Set up the key pair authentication in Snowflake. For more details, see the [Snowflake key-pair authentication and key-pair rotation guide](https://docs.snowflake.com/en/user-guide/key-pair-auth).
2. Create a secret with the group `"private-key"` and the key `"snowflake"`.
   This is hardcoded in the flytekit SDK, since we can't know the group and key name in advance.
   This is for permission to upload and download data with structured dataset in the Python task pod.

```bash
   kubectl create secret generic private-key --from-file=snowflake=<YOUR PRIVATE KEY FILE> --namespace=flytesnacks-development
 ```

3. Create a secret in the flyteconnector's pod, this is for executing Snowflake queries in the connector pod.

```bash
ENCODED_VALUE=$(cat <YOUR PRIVATE KEY FILE> | base64) && kubectl patch secret flyteconnector -n flyte --patch "{\"data\":{\"snowflake_private_key\":\"$ENCODED_VALUE\"}}"
```
## Specify connector configuration

### Flyte binary
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
      - snowflake: connector-service
```

### flyte-core

Create a file named values-override.yaml and add the following configuration:

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
          snowflake: connector-service

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

---
title: Snowflake plugin
weight: 7
variants: +flyte -serverless -byoc -selfmanaged
---

# Snowflake Plugin

This guide provides an overview of how to set up Snowflake in your Flyte deployment.

## Specify plugin configuration

### flyte-binary

Edit the relevant YAML file to specify the plugin.

```yaml

          tasks:
            task-plugins:
              enabled-plugins:
                - container
                - sidecar
                - k8s-array
                - snowflake
              default-for-task-types:
                - container: container
                - container_array: k8s-array
                - snowflake: snowflake
```
### flyte-core

Create a file named ``values-override.yaml`` and add the following config to it:

```yaml
        configmap:
          enabled_plugins:
            # -- Tasks specific configuration [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#GetConfig)
            tasks:
              # -- Plugins configuration, [structure](https://pkg.go.dev/github.com/flyteorg/flytepropeller/pkg/controller/nodes/task/config#TaskPluginConfig)
              task-plugins:
                # -- [Enabled Plugins](https://pkg.go.dev/github.com/flyteorg/flyteplugins/go/tasks/config#Config). Enable sagemaker*, athena if you install the backend
                # plugins
                enabled-plugins:
                  - container
                  - sidecar
                  - k8s-array
                  - snowflake
                default-for-task-types:
                  container: container
                  sidecar: sidecar
                  container_array: k8s-array
                  snowflake: snowflake
```

## Obtain and add the Snowflake JWT token

Create a Snowflake account, and follow the [Snowflake docs](https://docs.snowflake.com/en/developer-guide/sql-api/authenticating#using-key-pair-authentication)
to generate a JWT token.
Then, add the Snowflake JWT token to FlytePropeller.

### flyte-binary

Create a secret as follows (or add to it if it already exists from other plugins):

```bash
          cat <<EOF | kubectl apply -f -
          apiVersion: v1
          kind: Secret
          metadata:
            name: flyte-binary-external-services
            namespace: flyte
          type: Opaque
          stringData:
            FLYTE_SNOWFLAKE_CLIENT_TOKEN: <JWT_TOKEN>
          EOF
  ```
Replace ``<JWT_TOKEN>`` with your JWT token.

Reference the newly created secret in ``.Values.configuration.inlineSecretRef`` in your YAML file as follows:

```yaml
configuration:
  inlineSecretRef: flyte-binary-external-services
```

### flyte-core

Add the JWT token as a secret to ``flyte-secret-auth``.

```bash
kubectl edit secret -n flyte flyte-secret-auth
```
```yaml
      apiVersion: v1
      data:
        FLYTE_SNOWFLAKE_CLIENT_TOKEN: <JWT_TOKEN>
        client_secret: Zm9vYmFy
      kind: Secret
      ...
```
Replace ``<JWT_TOKEN>`` with your JWT token.

### Upgrade the deployment

```bash
helm upgrade <RELEASE_NAME> flyteorg/<HELM_CHART> -n <YOUR_NAMESPACE> --values <YOUR_YAML_FILE>
```
Replace ``<RELEASE_NAME>`` with the name of your release (e.g., ``flyte-backend``), ``<YOUR_NAMESPACE>`` with the name of your namespace (e.g., ``flyte``), `<HELM_CHART>` with either `flyte-binary` or `flyte-core` and ``<YOUR_YAML_FILE>`` with the name of your YAML file.


  For Snowflake plugin on the Flyte cluster, please refer to `Snowflake Plugin Example <https://docs.flyte.org/en/latest/flytesnacks/examples/snowflake_plugin/snowflake.html>`_

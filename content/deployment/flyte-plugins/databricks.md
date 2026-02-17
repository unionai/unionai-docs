---
title: Databricks plugin
weight: 6
variants: +flyte -serverless -byoc -selfmanaged
---

# Databricks Plugin

This guide provides an overview of how to set up Databricks in your Flyte deployment.

## Databricks workspace

To set up your Databricks account, follow these steps:

1. Create a [Databricks account](https://www.databricks.com/).
2. Ensure that you have a Databricks workspace up and running.
3. Generate a [personal access token](https://docs.databricks.com/dev-tools/auth.html#databricks-personal-ACCESS_TOKEN-authentication) to be used in the Flyte configuration. You can find the personal access token in the user settings within the workspace.
4. When testing the Databricks plugin on the demo cluster, create an S3 bucket because the local demo cluster utilizes MinIO. Follow the [AWS instructions](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html) to generate access and secret keys, which can be used to access your preferred S3 bucket.
5. Create an [instance profile](https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html) for the Spark cluster. This profile enables the Spark job to access your data in the S3 bucket.
Please follow all four steps specified in the documentation.

Upload the following entrypoint.py file to either
[DBFS](https://docs.databricks.com/archive/legacy/data-tab.html)
(the final path can be ``dbfs:///FileStore/tables/entrypoint.py``) or S3.
This file will be executed by the Spark driver node, overriding the default command in the
[dbx](https://docs.databricks.com/dev-tools/dbx.html) job.

```python

  import os
  import sys
  from typing import List

  import click
  import pandas
  from flytekit.bin.entrypoint import fast_execute_task_cmd as _fast_execute_task_cmd
  from flytekit.bin.entrypoint import execute_task_cmd as _execute_task_cmd
  from flytekit.exceptions.user import FlyteUserException
  from flytekit.tools.fast_registration import download_distribution


  def fast_execute_task_cmd(additional_distribution: str, dest_dir: str, task_execute_cmd: List[str]):
      if additional_distribution is not None:
          if not dest_dir:
              dest_dir = os.getcwd()
          download_distribution(additional_distribution, dest_dir)

      # Insert the call to fast before the unbounded resolver args
      cmd = []
      for arg in task_execute_cmd:
          if arg == "--resolver":
              cmd.extend(["--dynamic-addl-distro", additional_distribution, "--dynamic-dest-dir", dest_dir])
          cmd.append(arg)

      click_ctx = click.Context(click.Command("dummy"))
      parser = _execute_task_cmd.make_parser(click_ctx)
      args, _, _ = parser.parse_args(cmd[1:])
      _execute_task_cmd.callback(test=False, **args)


  def main():

      args = sys.argv

      click_ctx = click.Context(click.Command("dummy"))
      if args[1] == "pyflyte-fast-execute":
          parser = _fast_execute_task_cmd.make_parser(click_ctx)
          args, _, _ = parser.parse_args(args[2:])
          fast_execute_task_cmd(**args)
      elif args[1] == "pyflyte-execute":
          parser = _execute_task_cmd.make_parser(click_ctx)
          args, _, _ = parser.parse_args(args[2:])
          _execute_task_cmd.callback(test=False, dynamic_addl_distro=None, dynamic_dest_dir=None, **args)
      else:
          raise FlyteUserException(f"Unrecognized command: {args[1:]}")


  if __name__ == '__main__':
      main()
```

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
                - databricks
              default-for-task-types:
                - container: container
                - container_array: k8s-array
                - spark: databricks

          inline:
            plugins:
              databricks:
                entrypointFile: dbfs:///FileStore/tables/entrypoint.py
                databricksInstance: <DATABRICKS_ACCOUNT>.cloud.databricks.com
```

Substitute ``<DATABRICKS_ACCOUNT>`` with the name of your Databricks account.

### flyte-core

Create a file named ``values-override.yaml`` and add the following config to it:

```yaml
      configmap:
        enabled_plugins:
          tasks:
            task-plugins:
              enabled-plugins:
                - container
                - sidecar
                - k8s-array
                - databricks
              default-for-task-types:
                container: container
                sidecar: sidecar
                container_array: k8s-array
                spark: databricks
      databricks:
        enabled: True
        plugin_config:
          plugins:
            databricks:
              entrypointFile: dbfs:///FileStore/tables/entrypoint.py
              databricksInstance: <DATABRICKS_ACCOUNT>.cloud.databricks.com
```
Substitute ``<DATABRICKS_ACCOUNT>`` with the name of your Databricks account.

## Add the Databricks access token

Add the Databricks access token to FlytePropeller:

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
            FLYTE_DATABRICKS_API_TOKEN: <ACCESS_TOKEN>
          EOF
```
Reference the newly created secret in  ``.Values.configuration.inlineSecretRef`` in your YAML file as follows:

```yaml
          configuration:
            inlineSecretRef: flyte-binary-external-services
```
Replace ``<ACCESS_TOKEN>`` with your access token.

### flyte-core

Add the access token as a secret to ``flyte-secret-auth``.

```bash
kubectl edit secret -n flyte flyte-secret-auth
```

```yaml
      apiVersion: v1
      data:
        FLYTE_DATABRICKS_API_TOKEN: <ACCESS_TOKEN>
        client_secret: Zm9vYmFy
      kind: Secret
      ...
```
Replace ``<ACCESS_TOKEN>`` with your access token.

## Upgrade the deployment


```bash
helm upgrade <RELEASE_NAME> flyteorg/<HELM_CHART> -n <YOUR_NAMESPACE> --values <YOUR_YAML_FILE>
```
Replace ``<RELEASE_NAME>`` with the name of your release (e.g., ``flyte-backend``), ``<YOUR_NAMESPACE>`` with the name of your namespace (e.g., ``flyte``), `<HELM_CHART>` with either `flyte-binary` or `flyte-core` and ``<YOUR_YAML_FILE>`` with the name of your YAML file.

> Make sure you enable [custom containers](https://docs.databricks.com/administration-guide/clusters/container-services.html) on your Databricks cluster before you trigger the workflow.
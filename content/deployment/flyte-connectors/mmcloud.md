---
title: MMCloud connector
weight: 13
variants: +flyte -serverless -byoc -selfmanaged
---

# MMCloud Connector

MemVerge Memory Machine Cloud (MMCloud) empowers users to continuously optimize cloud resources during runtime,
safely execute stateful tasks on spot instances, and monitor resource usage in real time.
These capabilities make it an excellent fit for long-running batch workloads.

This guide provides an overview of how to set up MMCloud in your Flyte deployment.

## Set up MMCloud

To run a Flyte workflow with Memory Machine Cloud, you will need to deploy Memory Machine Cloud.
Check out the [MMCloud User Guide](https://docs.memverge.com/mmce/current/userguide/olh/index.html) to get started!

By the end of this step, you should have deployed an MMCloud OpCenter.

## Spin up a cluster

### flyte-binary

    You can spin up a demo cluster using the following command:

    ```bash
    flytectl demo start
    ```

    Or install Flyte using the [flyte-binary helm chart](deployment-deployment-cloud-simple).

### flyte-core

    If you've installed Flyte using the
    [flyte-core helm chart](https://github.com/flyteorg/flyte/tree/master/charts/flyte-core), please ensure:

    - You have the correct kubeconfig and have selected the correct Kubernetes context.
    - You have configured the correct flytectl settings in `~/.flyte/config.yaml`.

Note:
    Add the Flyte chart repo to Helm if you're installing via the Helm charts.

    ```bash
    helm repo add flyteorg https://flyteorg.github.io/flyte
    ```

## Specify connector configuration

Enable the MMCloud connector by adding the following config to the relevant YAML file(s):

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - connector-service
    default-for-task-types:
      - mmcloud_task: connector-service
```

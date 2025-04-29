---
title: Memory Machine Cloud connector
weight: 1
variants: +flyte -serverless -byoc -byok
sidebar_expanded: false
---

# Memory Machine Cloud connector

[MemVerge](https://memverge.com/) [Memory Machine Cloud](https://www.mmcloud.io/) (MMCloud)—available on AWS, GCP, and AliCloud—empowers users to continuously optimize cloud resources during runtime, safely execute stateful tasks on spot instances, and monitor resource usage in real time. These capabilities make it an excellent fit for long-running batch workloads. Flyte can be integrated with MMCloud, allowing you to execute Flyte tasks using MMCloud.

## Installation

To install the connector, run the following command:

```shell
$ pip install flytekitplugins-mmcloud
```

To get started with Memory Machine Cloud, see the [Memory Machine Cloud user guide](https://docs.memverge.com/mmce/current/userguide/olh/index.html).

## Example usage

For a usage example, see [Memory Machine Cloud connector example usage](./mmcloud-connector-example-usage).

## Local testing

To test the MMCloud connector locally,
create a class for the connector task
that inherits from [AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
This mixin can handle asynchronous tasks
and allows flytekit to mimic FlytePropeller's behavior in calling the connector.

<!-- TODO add back when page correctly relocated
For more information,
see "[Testing connectors locally](https://docs.flyte.org/en/latest/flyte_connectors/testing_connectors_in_a_local_python_environment.html)".
-->

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

## Flyte deployment configuration

> [!NOTE]
> If you are using a managed deployment of Flyte,
> you will need to contact your deployment administrator to configure connectors in your deployment.

To enable the Memory Machine Cloud connector in your Flyte deployment, see the [MMCloud connector setup guide](../../../deployment/flyte-connectors/mmcloud).

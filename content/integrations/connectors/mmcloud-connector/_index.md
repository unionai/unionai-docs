---
title: Memory Machine Cloud connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Memory Machine Cloud connector

[MemVerge](https://memverge.com/) [Memory Machine Cloud](https://www.mmcloud.io/) (MMCloud)—available on AWS, GCP, and AliCloud—empowers users to continuously optimize cloud resources during runtime, safely execute stateful tasks on spot instances, and monitor resource usage in real time. These capabilities make it an excellent fit for long-running batch workloads. {{< key product_name >}} can be integrated with MMCloud, allowing you to execute {{< key product_name >}} tasks using MMCloud.

## Installation

To install the connector, run the following command:

```shell
$ pip install flytekitplugins-mmcloud
```

To get started with Memory Machine Cloud, see the [Memory Machine Cloud user guide](https://docs.memverge.com/MMCloud/latest/User%20Guide/about).

## Example usage

{{< variant flyte >}}
{{< markdown >}}

For an example query, see [Memory Machine Cloud connector connector example usage](./mmcloud-connector-example-usage)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

For an example query, see [Memory Machine Cloud connector connector example usage](./mmcloud-connector-example-usage-union)

{{< /markdown >}}
{{< /variant >}}

## Local testing

To test the MMCloud connector locally, create a class for the connector task that inherits from
[AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
This mixin can handle asynchronous tasks and allows the SDK to mimic the system's behavior in calling the connector.

For more information, see [Testing connectors locally](../#testing-your-connector-locally).

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

{{< variant flyte >}}
{{< markdown >}}

## Flyte deployment configuration

To enable the Memory Machine Cloud connector in your Flyte deployment, see the [MMCloud connector setup guide](../../../deployment/flyte-connectors/mmcloud).

{{< /markdown >}}
{{< /variant >}}

---
title: MemVerge Memory Machine Cloud (MMC) connector
weight: 6
variants: +flyte -serverless +byoc +byok
sidebar_expanded: false
---

# MemVerge Memory Machine Cloud (MMC) connector

[MemVerge](https://memverge.com/) [Memory Machine Cloud](https://www.mmcloud.io/) (MMCloud)—available on AWS, GCP, and AliCloud—empowers users to continuously optimize cloud resources during runtime, safely execute stateful tasks on spot instances, and monitor resource usage in real time. These capabilities make it an excellent fit for long-running batch workloads. {{< key product_name >}} can be integrated with MMCloud, allowing you to execute {{< key product_name >}} tasks using MMCloud.

## Installation

To install the MMCloud connector, run the following command:


```
pip install flytekitplugins-mmcloud
```

To get started with Memory Machine Cloud, see the [Memory Machine Cloud user guide](https://docs.memverge.com).

## Example usage

For a usage example, see [Memory Machine Cloud connector example](./mmcloud-connector-example).

## Local testing

To test the MMCloud connector locally, create a class for the connector task that inherits from [`AsyncConnectorExecutorMixin`](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354). This mixin allows flytekit to mimic FlytePropeller's behavior in calling the connector.

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when

{{< variant byoc >}}
{{< markdown >}}

## {{< key product_name >}} cluster deployment

After you have finished testing the connector locally, contact the {{< key product_name >}} team to enable it in your cluster.

{{< /markdown >}}
{{< /variant >}}

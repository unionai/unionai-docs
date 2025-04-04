---
title: MemVerge Memory Machine Cloud (MMC) agent
weight: 6
variants: +flyte -serverless +byoc +byok
sidebar_expanded: true
---

# MemVerge Memory Machine Cloud (MMC) agent

[MemVerge](https://memverge.com/) [Memory Machine Cloud](https://www.mmcloud.io/) (MMCloud)—available on AWS, GCP, and AliCloud—empowers users to continuously optimize cloud resources during runtime, safely execute stateful tasks on spot instances, and monitor resource usage in real time. These capabilities make it an excellent fit for long-running batch workloads. {{< key product_name >}} can be integrated with MMCloud, allowing you to execute {{< key product_name >}} tasks using MMCloud.

## Installation

To install the MMCloud agent, run the following command:


```
pip install flytekitplugins-mmcloud
```

To get started with Memory Machine Cloud, see the [Memory Machine Cloud user guide](https://docs.memverge.com).

## Example usage

For a usage example, see [Memory Machine Cloud agent example](./mmcloud-agent-example).

## Local testing

To test the MMCloud agent locally, create a class for the agent task that inherits from [`AsyncAgentExecutorMixin`](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_agent.py#L278-382). This mixin allows flytekit to mimic FlytePropeller's behavior in calling the agent.

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when

{{< variant byoc >}}
{{< markdown >}}

## {{< key product_name >}} cluster deployment

After you have finished testing the agent locally, contact the {{< key product_name >}} team to enable it in your cluster.

{{< /markdown >}}
{{< /variant >}}

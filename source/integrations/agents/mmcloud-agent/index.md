# MemVerge Memory Machine Cloud (MMC) agent

[MemVerge](https://memverge.com/) [Memory Machine Cloud](https://www.mmcloud.io/) (MMCloud)—available on AWS, GCP, and AliCloud—empowers users to continuously optimize cloud resources during runtime, safely execute stateful tasks on spot instances, and monitor resource usage in real time. These capabilities make it an excellent fit for long-running batch workloads. Flyte can be integrated with MMCloud, allowing you to execute Flyte tasks using MMCloud.

## Installation

To install the MMCloud agent, run the following command:


```
pip install flytekitplugins-mmcloud
```

To get started with Memory Machine Cloud, see the [Memory Machine Cloud user guide](https://docs.memverge.com/mmce/current/userguide/olh/index.html).

## Example usage

For a usage example, see [Memory Machine Cloud agent example](mmcloud-agent-example).

## Local testing

To test the MMCloud agent locally, create a class for the agent task that inherits from [`AsyncAgentExecutorMixin`](https://github.com/flyteorg/flytekit/blob/master/flytekit/extend/backend/base_agent.py#L259). This mixin allows flytekit to mimic FlytePropeller's behavior in calling the agent.

:::{note}

In some cases, you will need to store credentials in your local environment when testing locally.

:::

{@@ if byoc @@}
## Union cluster deployment

After you have finished testing the agent locally, contact the Union team to enable it in your cluster.
{@@ endif @@}
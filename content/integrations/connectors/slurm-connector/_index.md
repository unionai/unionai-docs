---
title: Slurm connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Slurm connector

## Installation

To install the Slurm connector, run the following command:

```shell
$ pip install flytekitplugins-slurm
```

## Example usage

{{< variant flyte >}}
{{< markdown >}}

For an example query, see [Slurm connector example usage](./slurm-connector-example-usage)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

For an example query, see [Slurm connector example usage](./slurm-connector-example-usage-union)

{{< /markdown >}}
{{< /variant >}}

## Local testing

To test the Slurm connector locally, create a class for the connector task that inherits from
[AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
This mixin can handle asynchronous tasks and allows the SDK to mimic the system's behavior in calling the connector.

For more information, see [Testing connectors locally](../#testing-your-connector-locally).

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

{{< variant flyte >}}
{{< markdown >}}

## Flyte deployment configuration

To enable the Slurm connector in your Flyte deployment, see the [Slurm connector deployment guide](../../../deployment/flyte-connectors/slurm).

{{< /markdown >}}
{{< /variant >}}

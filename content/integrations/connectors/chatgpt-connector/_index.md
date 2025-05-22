---
title: ChatGPT connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: false
---

# ChatGPT connector

## Installation

To install the ChatGPT connector, run the following command:

```shell
$ pip install flytekitplugins-openai
```

## Example usage

{{< variant flyte >}}
{{< markdown >}}

For an example query, see [ChatGPT connector example usage](./chatgpt-connector-example-usage)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

For an example query, see [ChatGPT connector example usage](./chatgpt-connector-example-usage-union)

{{< /markdown >}}
{{< /variant >}}

## Local testing

To test the ChatGPT connector locally, create a class for the connector task that inherits from
[SyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L304).
This mixin can handle synchronous tasks and allows the SDK to mimic the system's behavior in calling the connector.

For more information, see [Testing connectors locally](../#testing-your-connector-locally).

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

{{< variant flyte >}}
{{< markdown >}}

## Flyte deployment configuration

To enable the ChatGPT connector in your Flyte deployment, see the [ChatGPT connector deployment guide](../../../deployment/flyte-connectors/chatgpt).

{{< /markdown >}}
{{< /variant >}}

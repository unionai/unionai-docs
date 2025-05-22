---
title: Snowflake connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Snowflake connector

{{< key product_name >}} can be seamlessly integrated with the [Snowflake](https://www.snowflake.com) service,
providing you with a straightforward means to query data in Snowflake.

## Installation

To use the Snowflake connector, run the following command:

```shell
$ pip install flytekitplugins-snowflake
```

## Example usage

{{< variant flyte >}}
{{< markdown >}}

For an example query, see [Snowflake connector example usage](./snowflake-connector-example-usage)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

For an example query, see [Snowflake connector example usage](./snowflake-connector-example-usage-union)

{{< /markdown >}}
{{< /variant >}}


## Local testing

To test the Snowflake connector locally, create a class for the connector task that inherits from
[AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
This mixin can handle asynchronous tasks and allows the SDK to mimic the system's behavior in calling the connector.

For more information, see [Testing connectors locally](../#testing-your-connector-locally).

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

{{< variant flyte >}}
{{< markdown >}}

## Flyte deployment configuration

To enable the Snowflake connector in your Flyte deployment, see the [Snowflake connector setup guide](../../../deployment/flyte-connectors/snowflake).

{{< /markdown >}}
{{< /variant >}}

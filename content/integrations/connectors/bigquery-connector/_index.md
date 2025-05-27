---
title: BigQuery connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: false
---

# BigQuery connector

## Installation

To install the BigQuery connector, run the following command:

This connector is purely a spec. Since SQL is completely portable, there is no need to build a Docker container.

## Example usage

{{< variant flyte >}}
{{< markdown >}}

For an example query, see [BigQuery connector example usage](./bigquery-connector-example-usage)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

For an example query, see [BigQuery connector example usage](./bigquery-connector-example-usage-union)

{{< /markdown >}}
{{< /variant >}}

## Local testing

To test the BigQuery connector locally, create a class for the connector task that inherits from
[AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
This mixin can handle asynchronous tasks and allows the SDK to mimic the system's behavior in calling the connector.

For more information, see [Testing connectors locally](../#testing-your-connector-locally).

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

{{< variant flyte >}}
{{< markdown >}}

## Flyte deployment configuration

To enable the BigQuery connector in your Flyte deployment, see the [BigQuery connector deployment guide](../../../deployment/flyte-connectors/bigquery)

{{< /markdown >}}
{{< /variant >}}


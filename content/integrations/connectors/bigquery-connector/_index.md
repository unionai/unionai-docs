---
title: BigQuery connector
weight: 1
variants: +flyte -serverless -byoc -byok
sidebar_expanded: false
---

# BigQuery connector

## Installation

To install the BigQuery connector, run the following command:

This connector is purely a spec. Since SQL is completely portable, there is no need to build a Docker container.

## Example usage

For an example query, see [BigQuery connector example usage](./bigquery-connector-example-usage)

## Local testing

To test the BigQuery connector locally,
create a class for the connector task
that inherits from [AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
This mixin can handle asynchronous tasks
and allows flytekit to mimic FlytePropeller's behavior in calling the connector.

<!-- TODO: add back when section is correctly relocated
For more information,
see "[Testing connectors locally](https://docs.flyte.org/en/latest/flyte_connectors/testing_connectors_in_a_local_python_environment.html)".
-->

> [!NOTE]
>
> In some cases, you will need to store credentials in your local environment when testing locally.
>

## Flyte deployment configuration

> [!NOTE]
> If you are using a managed deployment of Flyte,
> you will need to contact your deployment administrator to configure connectors in your deployment.

To enable the BigQuery connector in your Flyte deployment, see the [BigQuery connector deployment guide](../../../deployment/flyte-connectors/bigquery)


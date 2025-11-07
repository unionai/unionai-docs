---
title: BigQuery connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: true
---

# BigQuery connector

The BigQuery connector allows you to submit and manage SQL queries against Google BigQuery from within Flyte.


## Installation

To install the BigQuery connector, run the following command:

This connector is purely a spec. Since SQL is completely portable, there is no need to build a Docker container.

## Example usage

For an example query, see [BigQuery connector example usage](./bigquery-connector-example-usage)

## Local testing

To test the BigQuery connector locally, create a class for the connector task that inherits from
[AsyncConnectorExecutorMixin](https://github.com/flyteorg/flyte-sdk/blob/1d49299294cd5e15385fe8c48089b3454b7a4cd1/src/flyte/connectors/_connector.py#L206).
This mixin simulates how the Flyte system executes asynchronous connector tasks, making it easier to validate your connector implementation before deploying it.


> [!NOTE]
> When testing locally, you may need to store and provide Google Cloud credentials in your environment.
> Ensure you’ve authenticated with Google Cloud (gcloud auth application-default login) or set the appropriate service account environment variables.

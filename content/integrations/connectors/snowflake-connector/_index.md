---
title: Snowflake connector
weight: 1
variants: +flyte -serverless -byoc -byok
sidebar_expanded: false
---

# Snowflake connector

Flyte can be seamlessly integrated with the [Snowflake](https://www.snowflake.com) service,
providing you with a straightforward means to query data in Snowflake.

## Installation

To use the Snowflake connector, run the following command:

```shell
$ pip install flytekitplugins-snowflake
```

## Example usage

For a usage example, see [Snowflake connector example usage](./snowflake-connector-example-usage).

## Local testing

To test the Snowflake connector locally, create a class for the connector task that inherits from [AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354). This mixin can handle asynchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the connector.

<!-- TODO add back when page correctly relocated
For more information,
see "[Testing connectors locally](https://docs.flyte.org/en/latest/flyte_connectors/testing_connectors_in_a_local_python_environment.html)".
-->

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

## Flyte deployment configuration

> [!NOTE]
> If you are using a managed deployment of Flyte,
> you will need to contact your deployment administrator to configure connectors in your deployment.

To enable the Snowflake connector in your Flyte deployment, see the [Snowflake connector setup guide](../../../deployment/flyte-connectors/snowflake).

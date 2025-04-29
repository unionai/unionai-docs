---
title: OpenAI Batch Connector
weight: 1
variants: +flyte -serverless -byoc -byok
sidebar_expanded: false
---

# OpenAI Batch Connector

The Batch API connector allows you to submit requests for asynchronous batch processing on OpenAI.
You can provide either a JSONL file or a JSON iterator, and the connector handles the upload to OpenAI,
creation of the batch, and downloading of the output and error files.

## Installation

To use the OpenAI Batch connector, run the following command:

```shell
$ pip install flytekitplugins-openai
```

## Example usage

For a usage example, see [OpenAI Batch connector example usage](./openai-batch-connector-example-usage).

## Local testing

To test an connector locally, create a class for the connector task that inherits from
[SyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L304)
or [AsyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354).
These mixins can handle synchronous and synchronous tasks, respectively,
and allow flytekit to mimic FlytePropeller's behavior in calling the connector.

<!-- TODO add back when page correctly relocated
For more information,
see "[Testing connectors locally](https://docs.flyte.org/en/latest/flyte_connectors/testing_connectors_in_a_local_python_environment.html)".
-->

## Flyte deployment configuration

> [!NOTE]
> If you are using a managed deployment of Flyte, you will need to contact your deployment administrator to configure connectors in your deployment.

To enable the OpenAI Batch connector in your Flyte deployment, refer to the
[OpenAI Batch connector setup guide](../../../deployment/flyte-connectors/openai-batch)

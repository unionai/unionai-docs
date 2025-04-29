---
title: OpenAI connectors
weight: 8
variants: +flyte -serverless +byoc +byok
sidebar_expanded: false
---

# OpenAI connectors

There are two OpenAI connectors:
* [**Batch connector**](./batch-connector-example): The Batch API connector allows you to submit requests for asynchronous batch processing on OpenAI.
* [**ChatGPT connector**](./chatgpt-connector-example) The ChatGPT connector allows you to submit prompts to ChatGPT and receive responses synchronously.

## Installation

To use the OpenAI batch or ChatGPT connector, run the following command:

```
pip install flytekitplugins-openai
```

## Example usage

### Batch connector

For a batch connector usage example, see [OpenAI Batch connector example usage](./batch-connector-example).

### ChatGPT connector

For a ChatGPT usage example, see [ChatGPT connector example](./chatgpt-connector-example).

## Local testing

### Batch connector

To test the batch connector locally, create a class for the connector task that inherits from [`AsyncConnectorExecutorMixin`](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354). This mixin can handle asynchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the connector.

### ChatGPT connector

To test the ChatGPT connector locally, create a class for the connector task that inherits from [SyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L304). This mixin can handle synchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the connector.

## {{< key product_name >}} cluster deployment

After you have finished testing the batch or ChatGPT connector locally, contact the {{< key product_name >}} team to enable it in your cluster.

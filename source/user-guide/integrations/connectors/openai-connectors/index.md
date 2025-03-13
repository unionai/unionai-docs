# OpenAI connectors

There are two OpenAI connectors:
* [**Batch connector**](./batch-connector-example.md): The Batch API connector allows you to submit requests for asynchronous batch processing on OpenAI.
* [**ChatGPT connector**](./chatgpt-connector-example.md) The ChatGPT connector allows you to submit prompts to ChatGPT and receive responses synchronously.

## Installation

To use the OpenAI batch or ChatGPT connector, run the following command:

```
pip install flytekitplugins-openai
```

## Example usage

### Batch connector

For a batch connector usage example, see [OpenAI Batch connector example usage](./batch-connector-example.md).

### ChatGPT connector

For a ChatGPT usage example, see [ChatGPT connector example](./chatgpt-connector-example.md).

## Local testing

### Batch connector

To test the batch connector locally, create a class for the connector task that inherits from [`AsyncConnectorExecutorMixin`](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_connector.py#L278-382). This mixin can handle asynchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the connector.

### ChatGPT connector

To test the ChatGPT connector locally, create a class for the connector task that inherits from [SyncConnectorExecutorMixin](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_connector.py#L232-275). This mixin can handle synchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the connector.

## Union cluster deployment

After you have finished testing the batch or ChatGPT connector locally, contact the Union team to enable it in your cluster.

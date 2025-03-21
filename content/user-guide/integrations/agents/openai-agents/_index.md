---
title: OpenAI agents
weight: 8
variants: +flyte -serverless +byoc +byok
---

# OpenAI agents

There are two OpenAI agents:
* [**Batch agent**](./batch-agent-example.md): The Batch API agent allows you to submit requests for asynchronous batch processing on OpenAI.
* [**ChatGPT agent**](./chatgpt-agent-example.md) The ChatGPT agent allows you to submit prompts to ChatGPT and receive responses synchronously.

## Installation

To use the OpenAI batch or ChatGPT agent, run the following command:

```
pip install flytekitplugins-openai
```

## Example usage

### Batch agent

For a batch agent usage example, see [OpenAI Batch agent example usage](./batch-agent-example.md).

### ChatGPT agent

For a ChatGPT usage example, see [ChatGPT agent example](./chatgpt-agent-example.md).

## Local testing

### Batch agent

To test the batch agent locally, create a class for the agent task that inherits from [`AsyncAgentExecutorMixin`](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_agent.py#L278-382). This mixin can handle asynchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the agent.

### ChatGPT agent

To test the ChatGPT agent locally, create a class for the agent task that inherits from [SyncAgentExecutorMixin](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_agent.py#L232-275). This mixin can handle synchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the agent.

## {{< key product_name >}} cluster deployment

After you have finished testing the batch or ChatGPT agent locally, contact the {{< key product_name >}} team to enable it in your cluster.

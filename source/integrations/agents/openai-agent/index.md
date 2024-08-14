# OpenAI batch agent

The Batch API agent allows you to submit requests for asynchronous batch processing on OpenAI.
You can provide either a JSONL file or a JSON iterator, and the agent handles the upload to OpenAI,
creation of the batch, and downloading of the output and error files.

## Installation

To use the OpenAI Batch agent, run the following command:

```
pip install flytekitplugins-openai
```

## Example usage

For a usage example, see [OpenAI Batch agent example usage](openai-batch-agent-example).

## Local testing

To test an agent locally, create a class for the agent task that inherits from [`AsyncAgentExecutorMixin`](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_agent.py#L278-382). This mixin can handle asynchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the agent.

## Union cluster deployment

After you have finished testing the agent locally, contact the Union team to enable it in your cluster.
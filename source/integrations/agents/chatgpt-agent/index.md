# OpenAI ChatGPT agent

## Installation

To install the ChatGPT agent, run the following command:

```{code-block} shell
$ pip install flytekitplugins-openai
```

## Example usage

For a usage example, see [ChatGPT agent example](./chatgpt-agent-example).

## Local testing

To test the ChatGPT agent locally, create a class for the agent task that inherits from [SyncAgentExecutorMixin](https://github.com/flyteorg/flytekit/blob/03d23011fcf955838669bd5058c8ced17c6de3ee/flytekit/extend/backend/base_agent.py#L232-275). This mixin can handle synchronous tasks and allows flytekit to mimic FlytePropeller's behavior in calling the agent.

{@@ if byoc @@}
## Union cluster deployment

After you have finished testing the agent locally, contact the Union team to enable it in your cluster.
{@@ endif @@}
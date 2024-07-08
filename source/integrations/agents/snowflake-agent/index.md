# Snowflake agent

Union can be seamlessly integrated with the [Snowflake](https://www.snowflake.com) service,
allowing you to easily query data in Snowflake.

## Installation

To use the Snowflake agent, run the following command:

```
pip install flytekitplugins-snowflake
```

## Example usage

For a usage example, see [Snowflake agent example](./snowflake-agent-example).

## Local testing

To test the MMCloud agent locally, create a class for the agent task that inherits from [`AsyncAgentExecutorMixin`](https://github.com/flyteorg/flytekit/blob/master/flytekit/extend/backend/base_agent.py#L259). This mixin allows flytekit to mimic FlytePropeller's behavior in calling the agent.

:::{note}

In some cases, you will need to store credentials in your local environment when testing locally.

:::

{@@ if byoc @@}
## Union cluster deployment

After you have finished testing the agent locally, contact the Union team to enable it in your cluster.
{@@ endif @@}
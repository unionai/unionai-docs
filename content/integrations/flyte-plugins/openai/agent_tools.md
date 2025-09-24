---
title: Agent tools
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Agent tools

In this example, we will use the `openai-agents` library to create a simple agent that can use tools to perform tasks.
This example is based on the [basic tools example](https://github.com/openai/openai-agents-python/blob/main/examples/basic/tools.py) example from the `openai-agents-python` repo.

First, create an OpenAI API key, which you can get from the [OpenAI website](https://platform.openai.com/account/api-keys).
Then, create a secret on your Flyte cluster with:

```
flyte create secret OPENAI_API_KEY --value <your-api-key>
```

Then, we'll use `uv script` to specify our dependencies.

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/openai/openai/agents_tools.py" fragment=uv-script lang=python >}}

Next, we'll import the libraries and create a `TaskEnvironment`, which we need to run the example:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/openai/openai/agents_tools.py" fragment=imports-task-env lang=python >}}

## Define the tools

We'll define a tool that can get weather information for a
given city. In this case, we'll use a toy function that returns a hard-coded `Weather` object.

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/openai/openai/agents_tools.py" fragment=tools lang=python >}}

In this code snippet, the `@function_tool` decorator is imported from `flyteplugins.openai.agents`, which is a drop-in replacement for the `@function_tool` decorator from `openai-agents` library.

## Define the agent

Then, we'll define the agent, which calls the tool:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/openai/openai/agents_tools.py" fragment=agent lang=python >}}

## Run the agent

Finally, we'll run the agent. Create `config.yaml` file, which the `flyte.init_from_config()` function will use to connect to
the Flyte cluster:

```bash
flyte create config \
--output ~/.flyte/config.yaml \
--endpoint demo.hosted.unionai.cloud/ \
--project flytesnacks \
--domain development \
--builder remote
```

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/openai/openai/agents_tools.py" fragment=main lang=python >}}

## Conclusion

In this example, we've seen how to use the `openai-agents` library to create a simple agent that can use tools to perform tasks.

The full code is available [here](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/openai/openai).

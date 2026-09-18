---
title: OpenAI
version: 2.5.8
variants: +flyte +union
layout: py_api
---

# OpenAI

> [!WARNING] Deprecated
> `flyteplugins-openai` has been removed from the Flyte SDK and no longer publishes new
> releases. This page is a frozen snapshot of version 2.5.8, kept for users still on an older
> release.
>
> Use [`flyteplugins-agents-openai`](../agents/openai/_index) instead. Its `tool` decorator
> replaces `function_tool`, and `run_agent` drives the OpenAI Agents SDK loop from inside a Flyte
> task, so model turns replay on resume. See [Agent frameworks](../../../integrations/agents/_index)
> for the full set of adapters and [OpenAI](../../../integrations/agents/openai) for the migration
> target.

## Directory

### Methods

| Method | Description |
|-|-|
| [`function_tool()`](#function_tool) | Flyte-compatible replacement for @agents. |


## Methods

#### function_tool()

```python
def function_tool(
    func: typing.Union[flyte._task.AsyncFunctionTaskTemplate, typing.Callable, NoneType],
    kwargs,
) -> flyteplugins.openai.agents._function_tools.FunctionTool | agents.tool.FunctionTool
```
Flyte-compatible replacement for @agents.function_tool

**kwargs are forwarded to the underlying @agents.function_tool decorator.
For @flyte.trace functions, this just forwards all the arguments to the
agents.function_tool decorator:
https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.function_tool

For @TaskEnvironment.task functions, this will create a flyte-compatible
FunctionTool dataclass that can run tools as flyte tasks.


| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Union[flyte._task.AsyncFunctionTaskTemplate, typing.Callable, NoneType]` | |
| `kwargs` | `**kwargs` | |


---
title: flyteplugins.openai.agents
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyteplugins.openai.agents

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


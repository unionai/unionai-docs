---
title: flytekitplugins.openai.chatgpt.agent
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.openai.chatgpt.agent

## Directory

### Classes

| Class | Description |
|-|-|
| [`ChatGPTAgent`](.././flytekitplugins.openai.chatgpt.agent#flytekitpluginsopenaichatgptagentchatgptagent) | This is the base class for all sync agents. |

### Variables

| Property | Type | Description |
|-|-|-|
| `OPENAI_API_KEY` | `str` |  |
| `TIMEOUT_SECONDS` | `int` |  |

## flytekitplugins.openai.chatgpt.agent.ChatGPTAgent

This is the base class for all sync agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents.
Propeller sends a request to agent service, and gets a response in the same call.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def ChatGPTAgent()
```
### Methods

| Method | Description |
|-|-|
| [`do()`](#do) | This is the method that the agent will run. |


#### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekit.extend.backend.base_agent.Resource
```
This is the method that the agent will run.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `task_category` |  | {{< multiline >}}task category that the agent supports
{{< /multiline >}} |


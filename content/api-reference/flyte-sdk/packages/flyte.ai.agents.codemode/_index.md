---
title: flyte.ai.agents.codemode
version: 2.3.3
variants: +flyte +union
layout: py_api
---

# flyte.ai.agents.codemode

CodeModeAgent — LLM + Monty sandbox orchestration with automatic retry.

The agent auto-generates its system prompt from the tool registry so that
adding a new tool is the only step required. Tools can be flyte tasks,
``@flyte.trace`` functions, or plain Python callables.

Skills (additional context injected into the system prompt) can be literal
strings or ``pathlib.Path`` objects pointing to local files.
## Directory

### Classes

| Class | Description |
|-|-|
| [`CodeModeAgent`](../flyte.ai.agents.codemode/codemodeagent) | Generates code via an LLM, executes it in a Monty sandbox, and. |

### Methods

| Method | Description |
|-|-|
| [`generate_code()`](#generate_code) | Call the LLM to generate analysis code and extract it. |


### Variables

| Property | Type | Description |
|-|-|-|
| `codemode_progress_cb` | `ContextVar` |  |

## Methods

#### generate_code()

```python
def generate_code(
    call_llm: Callable[..., Any],
    model: str,
    system: str,
    messages: list[dict[str, str]],
) -> str
```
Call the LLM to generate analysis code and extract it.


| Parameter | Type | Description |
|-|-|-|
| `call_llm` | `Callable[..., Any]` | |
| `model` | `str` | |
| `system` | `str` | |
| `messages` | `list[dict[str, str]]` | |


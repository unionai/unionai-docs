---
title: Agent
version: 2.3.8
variants: +flyte +union
layout: py_api
---

# Agent

**Package:** `flyte.ai.agents.protocol`

Minimal protocol that any agent must satisfy to work with
:class:`AgentChatAppEnvironment`.


```python
protocol Agent()
```
## Methods

| Method | Description |
|-|-|
| [`run()`](#run) | Process *message* (with prior *history*) and return an :class:`AgentResult`. |
| [`tool_descriptions()`](#tool_descriptions) | Return JSON-friendly metadata for every registered tool. |


### run()

```python
def run(
    message: str,
    history: list[dict[str, str]],
) -> AgentResult
```
Process *message* (with prior *history*) and return an :class:`AgentResult`.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `history` | `list[dict[str, str]]` | |

### tool_descriptions()

```python
def tool_descriptions()
```
Return JSON-friendly metadata for every registered tool.

Each dict should contain at least ``name``, ``signature``, and
``description`` keys.



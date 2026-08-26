---
title: AgentProtocol
version: 2.6.9
variants: +flyte +union
layout: py_api
---

# AgentProtocol

**Package:** `flyte.ai.agents.protocol`

Minimal protocol that any agent must satisfy to work with
`flyte.ai.chat.AgentChatAppEnvironment`.


```python
protocol AgentProtocol()
```
## Methods

| Method | Description |
|-|-|
| [`run()`](#run) | Process *message* (with prior *memory*) and return a `flyte.ai.agents.AgentResult`. |
| [`tool_descriptions()`](#tool_descriptions) | Return JSON-friendly metadata for every registered tool. |


### run()

```python
def run(
    message: str,
    memory: list[dict[str, Any]] | 'MemoryStore' | None = None,
) -> AgentResult
```
Process *message* (with prior *memory*) and return a `flyte.ai.agents.AgentResult`.

`memory` may be a `list[dict]` of prior messages (e.g. a chat
`history`) or a `flyte.ai.agents.MemoryStore` for durable, cross-run state.

Synchronous entry point. In async contexts, use `run.aio(...)`.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `memory` | `list[dict[str, Any]] \| 'MemoryStore' \| None` | |

### tool_descriptions()

```python
def tool_descriptions()
```
Return JSON-friendly metadata for every registered tool.

Each dict should contain at least `name`, `signature`, and
`description` keys.



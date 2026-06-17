---
title: AgentEvent
version: 2.5.1
variants: +flyte +union
layout: py_api
---

# AgentEvent

**Package:** `flyte.ai.agents.agent`

Lightweight event emitted by the agent loop.

The agent stays decoupled from any specific UI: subscribe via
:data:`agent_progress_cb` to forward these to logs, NDJSON streams, websockets,
Flyte reports, etc.


## Parameters

```python
class AgentEvent(
    type: EventType,
    data: dict[str, Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` | `EventType` | |
| `data` | `dict[str, Any]` | |


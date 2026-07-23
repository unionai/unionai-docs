---
title: AgentEvent
version: 2.5.12
variants: +flyte +union
layout: py_api
---

# AgentEvent

**Package:** `flyte.ai.agents`

Lightweight event emitted by the agent loop.

The agent stays decoupled from any specific UI: subscribe via
:data:`agent_progress_cb` to forward these to logs, NDJSON streams, websockets,
Flyte reports, etc.

``agent`` and ``run_id`` are stamped automatically on every event so that
consumers receiving events from multiple runs in one process (concurrent
agents, sub-agents used as tools, parallel runs of the same agent) can
attribute each event to the run that produced it.


## Parameters

```python
class AgentEvent(
    type: EventType,
    data: dict[str, Any],
    agent: str,
    run_id: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` | `EventType` | |
| `data` | `dict[str, Any]` | |
| `agent` | `str` | |
| `run_id` | `str` | |


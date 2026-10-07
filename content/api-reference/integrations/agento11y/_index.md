---
title: Grafana Agent Observability
description: "Grafana Agent Observability for Flyte agents."
icon: book
version: 2.11.1.dev2+g6d3d72b81
variants: +flyte +union
layout: py_api
---

# Grafana Agent Observability



Grafana Agent Observability for Flyte agents.

One call wires an agent built with the Flyte agents plugin into Grafana's Agent
Observability: generations, tool calls, and cost land in Grafana, nested inside the Flyte
task span, and grouped by Flyte run.

    import flyte
    from flyteplugins.agento11y import init
    from flyteplugins.agents.openai import run_agent

    # Module scope, not inside a task.
    init(service_name="my-agent")

    env = flyte.TaskEnvironment(name="agent_env")

    @env.task
    async def agent(question: str) -> str:
        return await run_agent(question, tools=[...], model="gpt-4.1")

Nothing else changes in the agent code. The adapter offers its framework's run payload to an
instrumentor on the way past, which is how a handler reaches a call the adapter owns rather
than you.

Supported frameworks: langchain, langgraph, openai, claude, google, pydantic-ai. crewai and
mistral have Flyte adapters but no agento11y integration yet, so their runs are still traced
but their generations are not captured.
## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteIdentityBinding`](./flyteidentitybinding) | Binds Flyte's run, task, and version onto agento11y's context for each task. |
| [`GrafanaAgentObservability`](./grafanaagentobservability) | A link to this run's conversation in Grafana Agent Observability. |

### Methods

| Method | Description |
|-|-|
| [`get_client()`](#get_client) | The client `init` built, for recording generations by hand. |
| [`init()`](#init) | Send Flyte agent runs to Grafana Agent Observability. |
| [`instrumented_frameworks()`](#instrumented_frameworks) | Frameworks that got an instrumentor, that is, whose integration package is installed. |
| [`shutdown()`](#shutdown) | Unbind, unregister, and flush a client we created. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SUPPORTED_FRAMEWORKS` | `tuple` |  |

## Methods

#### get_client()

```python
def get_client()
```
The client `init` built, for recording generations by hand.


#### init()

```python
def init(
    service_name: str | None = None,
    endpoint: str | None = None,
    client: Client | None = None,
    client_options: typing.Mapping[str, typing.Any] | None = None,
    bind_conversation: bool = True,
    bind_agent_name: bool = True,
    trace: bool = True,
    **otel_kwargs: typing.Any,
) -> Client
```
Send Flyte agent runs to Grafana Agent Observability.

Call this at module scope, not inside a task. Task spans open before the task body runs,
so initializing from within the body means that task's span, and the identity binding
that rides on it, have already been missed.

Three things get wired up. An agento11y client, sharing the tracer from
`flyteplugins-otel` so generation spans nest inside the Flyte task span rather than
floating off as their own traces. A binding that hands Flyte's run, task, and version to
agento11y as conversation id, agent name, and agent version. And an instrumentor for each
agent framework whose integration package is installed, which is what lets the agents
plugin attach handlers to calls it owns.



| Parameter | Type | Description |
|-|-|-|
| `service_name` | `str \| None` | Value for service.name on the OpenTelemetry side. |
| `endpoint` | `str \| None` | agento11y generation export endpoint. Falls back to the AGENTO11Y_ env vars, which is how the Grafana docs configure it. |
| `client` | `Client \| None` | Use a client you built yourself. Its tracer and exporters are left alone, and it is not shut down by `shutdown`. |
| `client_options` | `typing.Mapping[str, typing.Any] \| None` | Extra `ClientConfig` fields, for anything this signature does not surface: auth mode and token, protocol, content capture, a custom `generation_exporter`. Ignored when `client` is supplied. |
| `bind_conversation` | `bool` | Bind the Flyte run name as agento11y's conversation id. Turn this off if conversations in your product span more than one run. |
| `bind_agent_name` | `bool` | Bind the Flyte task name as agento11y's agent name. Turn this off for a task that drives more than one agent, so each keeps its framework-given name instead of all of them reporting as the task. |
| `trace` | `bool` | Also initialize `flyteplugins-otel`, so Flyte tasks and trace steps become spans and generations nest inside them. Turn it off if you initialize it yourself, or if you only want generations. |
| `**otel_kwargs` | `typing.Any` | |

**Returns:** The agento11y client, for creating generations directly.

#### instrumented_frameworks()

```python
def instrumented_frameworks()
```
Frameworks that got an instrumentor, that is, whose integration package is installed.


#### shutdown()

```python
def shutdown()
```
Unbind, unregister, and flush a client we created.



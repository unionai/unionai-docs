---
title: Agents
weight: 4
variants: +flyte +union
---

# Agents

An agent is a program that decides what to do next by calling a model in a loop. On Flyte, each step of that loop is a task, which is what makes the agent durable: every model call, tool call, and intermediate result is recorded, so a run that fails partway through can be inspected and resumed rather than restarted.

This matters more for agents than for batch jobs. An agent's control flow is decided at runtime by the model, so you cannot know in advance which path a run took. Recording each step is what makes the run explainable afterward.

```python
@env.task
def step(state: State) -> State:
    ...  # one model call plus its tool calls
```

Nothing here is a separate agent framework. An agent is tasks for the reasoning steps, an app when it needs to be reachable over HTTP, and a sandbox when it executes code the model wrote.

{{< grid >}}

{{< link-card target="build-agent" icon="robot" title="Build an agent" >}}
Implement ReAct, Plan-and-Execute, and other agent patterns with full observability.
{{< /link-card >}}

{{< link-card target="build-mcp" icon="code" title="Build an MCP" >}}
Serve Model Context Protocol servers for AI assistants to interact with, hosted on {{< key product_name >}}.
{{< /link-card >}}

{{< link-card target="sandboxing" icon="box" title="Sandboxing" >}}
Safely execute LLM-generated code with workflow sandboxes or ephemeral containers.
{{< /link-card >}}

{{< /grid >}}

## Related

{{< grid >}}

{{< link-card target="../../integrations/agents" icon="plugin" title="Agent frameworks" >}}
Run agents from OpenAI, Claude, LangGraph, CrewAI, and more as durable Flyte tasks.
{{< /link-card >}}

{{< link-card target="../tasks" icon="gear" title="Tasks" >}}
The unit each reasoning step is built from.
{{< /link-card >}}

{{< /grid >}}

---
title: Agent frameworks
variants: +flyte +union
weight: 1
---

# Agent frameworks

API reference for the `flyteplugins-agents-*` adapters, one package per agent framework on a shared core.

Every adapter exports the same two things, so the reference below is mostly a matter of which framework's types show up in the signatures:

- `tool` stacks on `@env.task` to expose a task as a tool the framework recognizes.
- `run_agent` drives the framework's own agent loop from inside a Flyte task.

For usage, patterns, and per-framework examples, see the [Agent frameworks](../../../integrations/agents/_index) guide.

| Package | API reference | Guide |
| --- | --- | --- |
| `flyteplugins-agents-core` | [Core](./core/_index) | [How it works](../../../integrations/agents/how-it-works) |
| `flyteplugins-agents-openai` | [OpenAI Agents SDK](./openai/_index) | [OpenAI](../../../integrations/agents/openai) |
| `flyteplugins-agents-claude` | [Claude Agent SDK](./claude/_index) | [Claude](../../../integrations/agents/claude-agent-sdk) |
| `flyteplugins-agents-google` | [Google ADK](./google/_index) | [Google ADK](../../../integrations/agents/google-adk) |
| `flyteplugins-agents-mistral` | [Mistral](./mistral/_index) | [Mistral](../../../integrations/agents/mistral) |
| `flyteplugins-agents-langchain` | [LangChain](./langchain/_index) | [LangChain](../../../integrations/agents/langchain) |
| `flyteplugins-agents-langgraph` | [LangGraph](./langgraph/_index) | [LangGraph](../../../integrations/agents/langgraph) |
| `flyteplugins-agents-deepagents` | [Deep Agents](./deepagents/_index) | [Deep Agents](../../../integrations/agents/deepagents) |
| `flyteplugins-agents-crewai` | [CrewAI](./crewai/_index) | [CrewAI](../../../integrations/agents/crewai) |
| `flyteplugins-agents-pydantic-ai` | [Pydantic AI](./pydantic-ai/_index) | [Pydantic AI](../../../integrations/agents/pydantic-ai) |
| `flyteplugins-agents-hermes` | [Hermes](./hermes/_index) | [Hermes](../../../integrations/agents/hermes) |

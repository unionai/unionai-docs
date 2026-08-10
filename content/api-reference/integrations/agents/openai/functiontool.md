---
title: FunctionTool
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# FunctionTool

**Package:** `flyteplugins.agents.openai`

An OpenAI Agents ``FunctionTool`` backed by a Flyte task.

Behaves exactly like ``agents.FunctionTool`` from the SDK's perspective, but
when the agent invokes it the call is dispatched to the underlying Flyte task
— so it runs as a durable child action (its own container/resources, with
retries and caching) rather than inline in the agent's process.


## Parameters

```python
class FunctionTool(
    name: str,
    description: str,
    params_json_schema: dict[str, Any],
    on_invoke_tool: Callable[[ToolContext[Any], str], Awaitable[Any]],
    strict_json_schema: bool,
    is_enabled: bool | Callable[[RunContextWrapper[Any], AgentBase], MaybeAwaitable[bool]],
    tool_input_guardrails: list[ToolInputGuardrail[Any]] | None,
    tool_output_guardrails: list[ToolOutputGuardrail[Any]] | None,
    needs_approval: bool | Callable[[RunContextWrapper[Any], dict[str, Any], str], Awaitable[bool]],
    timeout_seconds: float | None,
    timeout_behavior: ToolTimeoutBehavior,
    timeout_error_function: ToolErrorFunction | None,
    defer_loading: bool,
    task: TaskTemplate | None,
    native_interface: NativeInterface | None,
    report: bool,
    custom_data_extractor: FunctionToolCustomDataExtractor | None,
    allowed_callers: list[ToolCaller] | None,
    output_json_schema: dict[str, Any] | None,
    _output_type_adapter: TypeAdapter[Any] | None,
    _failure_error_function: ToolErrorFunction | None,
    _use_default_failure_error_function: bool,
    _is_agent_tool: bool,
    _agent_tool_default_identity: tuple[str, str] | None,
    _is_codex_tool: bool,
    _agent_instance: Any,
    _tool_namespace: str | None,
    _tool_namespace_description: str | None,
    _mcp_title: str | None,
    _tool_origin: ToolOrigin | None,
    _emit_tool_origin: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `description` | `str` | |
| `params_json_schema` | `dict[str, Any]` | |
| `on_invoke_tool` | `Callable[[ToolContext[Any], str], Awaitable[Any]]` | |
| `strict_json_schema` | `bool` | |
| `is_enabled` | `bool \| Callable[[RunContextWrapper[Any], AgentBase], MaybeAwaitable[bool]]` | |
| `tool_input_guardrails` | `list[ToolInputGuardrail[Any]] \| None` | |
| `tool_output_guardrails` | `list[ToolOutputGuardrail[Any]] \| None` | |
| `needs_approval` | `bool \| Callable[[RunContextWrapper[Any], dict[str, Any], str], Awaitable[bool]]` | |
| `timeout_seconds` | `float \| None` | |
| `timeout_behavior` | `ToolTimeoutBehavior` | |
| `timeout_error_function` | `ToolErrorFunction \| None` | |
| `defer_loading` | `bool` | |
| `task` | `TaskTemplate \| None` | |
| `native_interface` | `NativeInterface \| None` | |
| `report` | `bool` | |
| `custom_data_extractor` | `FunctionToolCustomDataExtractor \| None` | |
| `allowed_callers` | `list[ToolCaller] \| None` | |
| `output_json_schema` | `dict[str, Any] \| None` | |
| `_output_type_adapter` | `TypeAdapter[Any] \| None` | |
| `_failure_error_function` | `ToolErrorFunction \| None` | |
| `_use_default_failure_error_function` | `bool` | |
| `_is_agent_tool` | `bool` | |
| `_agent_tool_default_identity` | `tuple[str, str] \| None` | |
| `_is_codex_tool` | `bool` | |
| `_agent_instance` | `Any` | |
| `_tool_namespace` | `str \| None` | |
| `_tool_namespace_description` | `str \| None` | |
| `_mcp_title` | `str \| None` | |
| `_tool_origin` | `ToolOrigin \| None` | |
| `_emit_tool_origin` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `qualified_name` | `str` | Return the public qualified name used to identify this function tool. |

## Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | Run the wrapped task directly (a durable child action in a task context). |


### execute()

```python
def execute(
    args: *args,
    kwargs: **kwargs,
) -> typing.Any
```
Run the wrapped task directly (a durable child action in a task context).


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |


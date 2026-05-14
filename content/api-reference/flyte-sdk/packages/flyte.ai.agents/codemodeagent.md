---
title: CodeModeAgent
version: 2.3.1
variants: +flyte +union
layout: py_api
---

# CodeModeAgent

**Package:** `flyte.ai.agents`

Generates code via an LLM, executes it in a Monty sandbox, and
optionally retries on failure.

Parameters
----------
tools:
    The callables available inside the sandbox. Accepts either a
    ``dict[str, Callable]`` mapping or a sequence containing any mix of:

    - plain Python functions
    - ``@flyte.trace`` helpers
    - ``@env.task`` :class:`~flyte.TaskTemplate` instances (durable)
    - :class:`~flyte.remote._task.LazyEntity` references to remote tasks

    Sequence entries are keyed by ``TaskTemplate.func.__name__`` for tasks
    (and ``__name__`` for plain callables). Pass a dict to expose a tool
    under a different name to the LLM (e.g.
    ``tools={"fetch_data": durable_fetch_with_retries}``). The sandbox
    receives the original objects, so ``@env.task`` entries execute
    durably on the cluster; the prompt introspects ``TaskTemplate.func``
    to surface the underlying signature and docstring.
model:
    Model identifier passed to *call_llm*.
max_retries:
    How many *additional* attempts after the first failure.
skills:
    Extra context injected into the system prompt. Each entry is
    either a literal string or a ``pathlib.Path`` to a local file
    whose contents will be read.
call_llm:
    Async callback ``(model, system, messages) -&gt; str``. Defaults to
    a *litellm*-based implementation.
system_prompt_prefix:
    Optional text prepended to the auto-generated system prompt,
    allowing callers to set the agent persona or additional
    instructions.


## Parameters

```python
class CodeModeAgent(
    tools: Sequence[Callable] | dict[str, Callable],
    model: str,
    max_retries: int,
    skills: Sequence[str | pathlib.Path],
    call_llm: Callable[..., Any],
    system_prompt_prefix: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `tools` | `Sequence[Callable] \| dict[str, Callable]` | |
| `model` | `str` | |
| `max_retries` | `int` | |
| `skills` | `Sequence[str \| pathlib.Path]` | |
| `call_llm` | `Callable[..., Any]` | |
| `system_prompt_prefix` | `str \| None` | |

## Methods

| Method | Description |
|-|-|
| [`run()`](#run) | Generate code, execute in sandbox, retry on failure. |
| [`tool_descriptions()`](#tool_descriptions) | Return JSON-friendly metadata for every registered tool. |
| [`uses_flyte_tools()`](#uses_flyte_tools) | True when the tool registry contains Flyte tasks or remote lazy tasks. |


### run()

```python
def run(
    message: str,
    history: list[dict[str, str]],
) -> AgentResult
```
Generate code, execute in sandbox, retry on failure.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `history` | `list[dict[str, str]]` | |

### tool_descriptions()

```python
def tool_descriptions()
```
Return JSON-friendly metadata for every registered tool.


### uses_flyte_tools()

```python
def uses_flyte_tools()
```
True when the tool registry contains Flyte tasks or remote lazy tasks.



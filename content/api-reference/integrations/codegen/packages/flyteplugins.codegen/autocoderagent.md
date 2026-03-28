---
title: AutoCoderAgent
version: 2.0.12.dev22+g879ad6de4
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# AutoCoderAgent

**Package:** `flyteplugins.codegen`

Agent for single-file Python code generation with automatic testing and iteration.

Generates a single Python script, builds a sandbox image with the required
dependencies, runs pytest-based tests, and iterates until tests pass.

Uses Sandbox internally for isolated code execution.



## Parameters

```python
class AutoCoderAgent(
    model: str,
    name: str,
    system_prompt: typing.Optional[str],
    api_key: typing.Optional[str],
    api_base: typing.Optional[str],
    litellm_params: typing.Optional[dict],
    base_packages: typing.Optional[list[str]],
    resources: typing.Optional[flyte._resources.Resources],
    image_config: typing.Optional[flyte.sandbox._code_sandbox.ImageConfig],
    max_iterations: int,
    max_sample_rows: int,
    skip_tests: bool,
    sandbox_retries: int,
    timeout: typing.Optional[int],
    env_vars: typing.Optional[dict[str, str]],
    secrets: typing.Optional[list],
    cache: str,
    backend: typing.Literal['litellm', 'claude'],
    agent_max_turns: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `str` | LLM model to use (required). Must support structured outputs. For backend="litellm" (default): e.g. "gpt-4.1", "claude-sonnet-4-20250514". For backend="claude": a Claude model ("sonnet", "opus", "haiku"). |
| `name` | `str` | Name for the agent (used in image naming and logging). |
| `system_prompt` | `typing.Optional[str]` | Optional system prompt to use for LLM. If not provided, a default prompt with structured output requirements is used. |
| `api_key` | `typing.Optional[str]` | Optional environment variable name for LLM API key. |
| `api_base` | `typing.Optional[str]` | Optional base URL for LLM API. |
| `litellm_params` | `typing.Optional[dict]` | Optional dict of additional parameters to pass to LiteLLM calls. |
| `base_packages` | `typing.Optional[list[str]]` | Optional list of base packages to install in the sandbox. |
| `resources` | `typing.Optional[flyte._resources.Resources]` | Optional resources for sandbox execution (default: cpu=1, 1Gi). |
| `image_config` | `typing.Optional[flyte.sandbox._code_sandbox.ImageConfig]` | Optional image configuration for sandbox execution. |
| `max_iterations` | `int` | Maximum number of generate-test-fix iterations. Defaults to 10. |
| `max_sample_rows` | `int` | Optional maximum number of rows to use for sample data. Defaults to 100. |
| `skip_tests` | `bool` | Optional flag to skip testing. Defaults to False. |
| `sandbox_retries` | `int` | Number of Flyte task-level retries for each sandbox execution. Defaults to 0. |
| `timeout` | `typing.Optional[int]` | Timeout in seconds for sandboxes. Defaults to None. |
| `env_vars` | `typing.Optional[dict[str, str]]` | Environment variables to pass to sandboxes. |
| `secrets` | `typing.Optional[list]` | flyte.Secret objects to make available to sandboxes. |
| `cache` | `str` | CacheRequest for sandboxes: "auto", "override", or "disable". Defaults to "auto". |
| `backend` | `typing.Literal['litellm', 'claude']` | Execution backend: "litellm" (default) or "claude". |
| `agent_max_turns` | `int` | Maximum agent turns when backend="claude". Defaults to 50. |

## Methods

| Method | Description |
|-|-|
| [`generate()`](#generate) | Generate and evaluate code in an isolated sandbox. |


### generate()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <AutoCoderAgent instance>.generate.aio()`.
```python
def generate(
    prompt: str,
    schema: typing.Optional[str],
    constraints: typing.Optional[list[str]],
    samples: typing.Optional[dict[str, pandas.core.frame.DataFrame | flyte.io._file.File]],
    inputs: typing.Optional[dict[str, type]],
    outputs: typing.Optional[dict[str, type]],
) -> flyteplugins.codegen.core.types.CodeGenEvalResult
```
Generate and evaluate code in an isolated sandbox.

Each call is independent with its own sandbox, packages and execution environment.



| Parameter | Type | Description |
|-|-|-|
| `prompt` | `str` | The prompt to generate code from. |
| `schema` | `typing.Optional[str]` | Optional free-form context about data formats, structures or schemas. Included verbatim in the LLM prompt. Use for input formats, output schemas, database schemas or any structural context the LLM needs to generate code. |
| `constraints` | `typing.Optional[list[str]]` | Optional list of constraints or requirements. |
| `samples` | `typing.Optional[dict[str, pandas.core.frame.DataFrame \| flyte.io._file.File]]` | Optional dict of sample data. Each value is sampled and included in the LLM prompt for context, and converted to a File input for the sandbox. Values are used as defaults at runtime — override them when calling `result.run()` or `result.as_task()`. Supported types: File, pd.DataFrame. |
| `inputs` | `typing.Optional[dict[str, type]]` | Optional dict declaring non-sample CLI argument types (e.g., `{"threshold": float, "mode": str}`). Sample entries are automatically added as File inputs — don't redeclare them here. Supported types: str, int, float, bool, File. |
| `outputs` | `typing.Optional[dict[str, type]]` | Optional dict defining output types (e.g., `{"result": str, "report": File}`). Supported types: str, int, float, bool, datetime, timedelta, File. |

**Returns:** CodeGenEvalResult with solution and execution details.


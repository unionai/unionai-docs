---
title: AutoCoderAgent
version: 2.0.9
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# AutoCoderAgent

**Package:** `flyteplugins.codegen`

Agent for single-file Python code generation with automatic testing and iteration.

    Generates a single Python script, builds a sandbox image with the required
    dependencies, runs pytest-based tests, and iterates until tests pass.

    Uses Sandbox internally for isolated code execution.

    Args:
        name: Name for the agent (used in image naming and logging).
        model: LLM model to use (required). Must support structured outputs.
            For backend="litellm" (default): e.g. "gpt-4.1", "claude-sonnet-4-20250514".
            For backend="claude": a Claude model ("sonnet", "opus", "haiku").
        system_prompt: Optional system prompt to use for LLM. If not provided,
            a default prompt with structured output requirements is used.
        api_key: Optional environment variable name for LLM API key.
        api_base: Optional base URL for LLM API.
        litellm_params: Optional dict of additional parameters to pass to LiteLLM calls.
        base_packages: Optional list of base packages to install in the sandbox.
        resources: Optional resources for sandbox execution (default: cpu=1, 1Gi).
        image_config: Optional image configuration for sandbox execution.
        max_iterations: Maximum number of generate-test-fix iterations. Defaults to 10.
        max_sample_rows: Optional maximum number of rows to use for sample data. Defaults to 100.
        skip_tests: Optional flag to skip testing. Defaults to False.
        sandbox_retries: Number of Flyte task-level retries for each sandbox execution. Defaults to 0.
        timeout: Timeout in seconds for sandboxes. Defaults to None.
        env_vars: Environment variables to pass to sandboxes.
        secrets: flyte.Secret objects to make available to sandboxes.
        cache: CacheRequest for sandboxes: "auto", "override", or "disable". Defaults to "auto".
        backend: Execution backend: "litellm" (default) or "claude".
        agent_max_turns: Maximum agent turns when backend="claude". Defaults to 50.

    Example::

        from flyte.sandbox import sandbox_environment
        from flyteplugins.codegen import AutoCoderAgent

        agent = AutoCoderAgent(
            model="gpt-4.1",
            base_packages=["pandas"],
            resources=flyte.Resources(cpu=1, memory="1Gi"),
        )

        env = flyte.TaskEnvironment(
            name="my-env",
            depends_on=[sandbox_environment],
        )

        @env.task
        async def my_task(data_file: File) -&gt; float:
            result = await agent.generate.aio(
                prompt="Process CSV data",
                samples={"csv": data_file},
                outputs={"total": float},
            )
            return await result.run.aio()
    


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
| `model` | `str` | |
| `name` | `str` | |
| `system_prompt` | `typing.Optional[str]` | |
| `api_key` | `typing.Optional[str]` | |
| `api_base` | `typing.Optional[str]` | |
| `litellm_params` | `typing.Optional[dict]` | |
| `base_packages` | `typing.Optional[list[str]]` | |
| `resources` | `typing.Optional[flyte._resources.Resources]` | |
| `image_config` | `typing.Optional[flyte.sandbox._code_sandbox.ImageConfig]` | |
| `max_iterations` | `int` | |
| `max_sample_rows` | `int` | |
| `skip_tests` | `bool` | |
| `sandbox_retries` | `int` | |
| `timeout` | `typing.Optional[int]` | |
| `env_vars` | `typing.Optional[dict[str, str]]` | |
| `secrets` | `typing.Optional[list]` | |
| `cache` | `str` | |
| `backend` | `typing.Literal['litellm', 'claude']` | |
| `agent_max_turns` | `int` | |

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


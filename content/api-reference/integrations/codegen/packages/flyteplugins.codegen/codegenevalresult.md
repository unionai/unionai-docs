---
title: CodeGenEvalResult
version: 2.1.0
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# CodeGenEvalResult

**Package:** `flyteplugins.codegen`

Result from code generation and evaluation.


## Parameters

```python
class CodeGenEvalResult(
    plan: typing.Optional[flyteplugins.codegen.core.types.CodePlan],
    solution: flyteplugins.codegen.core.types.CodeSolution,
    tests: typing.Optional[str],
    success: bool,
    output: str,
    exit_code: int,
    error: typing.Optional[str],
    attempts: int,
    conversation_history: list[dict[str, str]],
    detected_packages: list[str],
    detected_system_packages: list[str],
    image: typing.Optional[str],
    total_input_tokens: int,
    total_output_tokens: int,
    declared_inputs: typing.Optional[dict[str, type]],
    declared_outputs: typing.Optional[dict[str, type]],
    data_context: typing.Optional[str],
    original_samples: typing.Optional[dict[str, flyte.io._file.File]],
    generated_schemas: typing.Optional[dict[str, str]],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `plan` | `typing.Optional[flyteplugins.codegen.core.types.CodePlan]` | |
| `solution` | `flyteplugins.codegen.core.types.CodeSolution` | |
| `tests` | `typing.Optional[str]` | |
| `success` | `bool` | |
| `output` | `str` | |
| `exit_code` | `int` | |
| `error` | `typing.Optional[str]` | |
| `attempts` | `int` | |
| `conversation_history` | `list[dict[str, str]]` | |
| `detected_packages` | `list[str]` | Language packages detected by LLM from imports |
| `detected_system_packages` | `list[str]` | System packages detected by LLM |
| `image` | `typing.Optional[str]` | The Flyte Image built with all dependencies |
| `total_input_tokens` | `int` | Total input tokens used across all LLM calls |
| `total_output_tokens` | `int` | Total output tokens used across all LLM calls |
| `declared_inputs` | `typing.Optional[dict[str, type]]` | Input types (user-provided or inferred from samples) |
| `declared_outputs` | `typing.Optional[dict[str, type]]` | Output types declared by user |
| `data_context` | `typing.Optional[str]` | Extracted data context (schema, stats, patterns, samples) used for code generation |
| `original_samples` | `typing.Optional[dict[str, flyte.io._file.File]]` | Sample data converted to Files (defaults for run()/as_task()) |
| `generated_schemas` | `typing.Optional[dict[str, str]]` | Auto-generated Pandera schemas (as Python code strings) for validating data inputs |

## Methods

| Method | Description |
|-|-|
| [`as_task()`](#as_task) | Create a sandbox that runs the generated code in an isolated sandbox. |
| [`run()`](#run) | Run generated code in an isolated sandbox (one-off execution). |


### as_task()

```python
def as_task(
    name: str,
    resources: typing.Optional[flyte._resources.Resources],
    retries: int,
    timeout: typing.Optional[int],
    env_vars: typing.Optional[dict[str, str]],
    secrets: typing.Optional[list],
    cache: str,
)
```
Create a sandbox that runs the generated code in an isolated sandbox.

The generated code will write outputs to /var/outputs/{output_name} files.
Returns a callable wrapper that automatically provides the script file.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name for the sandbox |
| `resources` | `typing.Optional[flyte._resources.Resources]` | Optional resources for the task |
| `retries` | `int` | Number of retries for the task. Defaults to 0. |
| `timeout` | `typing.Optional[int]` | Timeout in seconds. Defaults to None. |
| `env_vars` | `typing.Optional[dict[str, str]]` | Environment variables to pass to the sandbox. |
| `secrets` | `typing.Optional[list]` | flyte.Secret objects to make available. |
| `cache` | `str` | CacheRequest: "auto", "override", or "disable". Defaults to "auto". |

**Returns:** Callable task wrapper with the default inputs baked in. Call with your other declared inputs.

### run()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <CodeGenEvalResult instance>.run.aio()`.
```python
def run(
    name: str,
    resources: typing.Optional[flyte._resources.Resources],
    retries: int,
    timeout: typing.Optional[int],
    env_vars: typing.Optional[dict[str, str]],
    secrets: typing.Optional[list],
    cache: str,
    overrides,
) -> typing.Any
```
Run generated code in an isolated sandbox (one-off execution).

If samples were provided during generate(), they are used as defaults.
Override any input by passing it as a keyword argument. If no samples
exist, all declared inputs must be provided via `**overrides`.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name for the sandbox |
| `resources` | `typing.Optional[flyte._resources.Resources]` | Optional resources for the task |
| `retries` | `int` | Number of retries for the task. Defaults to 0. |
| `timeout` | `typing.Optional[int]` | Timeout in seconds. Defaults to None. |
| `env_vars` | `typing.Optional[dict[str, str]]` | Environment variables to pass to the sandbox. |
| `secrets` | `typing.Optional[list]` | flyte.Secret objects to make available. |
| `cache` | `str` | CacheRequest: "auto", "override", or "disable". Defaults to "auto". |
| `overrides` |  | |

**Returns:** Tuple of typed outputs.


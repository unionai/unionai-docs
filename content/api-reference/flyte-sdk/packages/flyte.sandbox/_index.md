---
title: flyte.sandbox
version: 2.2.0
variants: +flyte +union
layout: py_api
---

# flyte.sandbox

Sandbox utilities for running isolated code inside Flyte tasks.

Warning: Experimental feature: alpha — APIs may change without notice.

`flyte.sandbox` provides two distinct sandboxing approaches:

---

**1. Orchestration sandbox** — powered by Monty
    Runs pure Python *orchestration logic* (control flow, routing, aggregation)
    with zero overhead. The Monty runtime enforces strong restrictions:
    no imports, no IO, no network access, microsecond startup.  Used via
    `@env.sandbox.orchestrator` or `flyte.sandbox.orchestrator_from_str()`.

    Sandboxed orchestrators are:

    - **Side-effect free**: No filesystem, network, or OS access
    - **Microsecond startup**: No container spin-up — runs in the same process
    - **Multiplexable**: Many orchestrators run safely on the same Python process

    Example:

        env = flyte.TaskEnvironment(name="my-env")

        @env.sandbox.orchestrator
        def route(x: int, y: int) -> int:
            return add(x, y)   # calls a worker task

        pipeline = flyte.sandbox.orchestrator_from_str(
            "add(x, y) * 2",
            inputs={"x": int, "y": int},
            output=int,
            tasks=[add],
        )

---

**2. Code sandbox** — arbitrary code in an isolated container
    Runs arbitrary Python scripts or shell commands inside an ephemeral Docker
    container. The image is built on demand from declared `packages` and
    `system_packages`, executed once, then discarded. Used via `flyte.sandbox.create()`.

    Three execution modes are supported:

    - Code mode — provide Python source that runs with automatic input/output wiring.
    - Verbatim mode — run a script that manages its own I/O via /var/inputs and /var/outputs.
    - Command mode — execute an arbitrary command or entrypoint.

    Network access is allowed by default. Pass `block_network=True` to block all
    outbound access — locally via Docker `network_mode=none`, on-cluster via a
    `NetworkPolicy`.

    Examples
    --------

    Code mode
    ~~~~~~~~~

    Provide Python code that uses inputs as variables and assigns
    outputs as Python values.

        _stats_code = """
        import numpy as np
        nums = np.array([float(v) for v in values.split(",")])
        mean = float(np.mean(nums))
        std  = float(np.std(nums))

        window_end = dt + delta
        """

        stats_sandbox = flyte.sandbox.create(
            name="numpy-stats",
            code=_stats_code,
            inputs={
                "values": str,
                "dt": datetime.datetime,
                "delta": datetime.timedelta,
            },
            outputs={
                "mean": float,
                "std": float,
                "window_end": datetime.datetime,
            },
            packages=["numpy"],
        )

        mean, std, window_end = await stats_sandbox.run.aio(
            values="1,2,3,4,5",
            dt=datetime.datetime(2024, 1, 1),
            delta=datetime.timedelta(days=1),
        )


    Verbatim mode
    ~~~~~~~~~~~~~

    Run a script that explicitly reads inputs from /var/inputs and
    writes outputs to /var/outputs.

        _etl_script = """        import json, pathlib

        payload = json.loads(
            pathlib.Path("/var/inputs/payload").read_text()
        )
        total = sum(payload["values"])

        pathlib.Path("/var/outputs/total").write_text(str(total))
        """

        etl_sandbox = flyte.sandbox.create(
            name="etl-script",
            code=_etl_script,
            inputs={"payload": File},
            outputs={"total": int},
            auto_io=False,
        )


    Command mode
    ~~~~~~~~~~~~

    Execute an arbitrary command inside the sandbox environment.

        sandbox = flyte.sandbox.create(
            name="test-runner",
            command=["/bin/bash", "-c", "pytest /var/inputs/tests.py -q"],
            inputs={"tests.py": File},
            outputs={"exit_code": str},
        )

    Notes
    -----

    • Inputs are materialized under /var/inputs.
    • Outputs must be written to /var/outputs.
    • In code mode, inputs are available as Python variables and
    scalar outputs are captured automatically.
    • Additional Python dependencies can be specified via the
    `packages` argument.
## Directory

### Classes

| Class | Description |
|-|-|
| [`CodeTaskTemplate`](../flyte.sandbox/codetasktemplate) | A sandboxed task created from a code string rather than a decorated function. |
| [`ImageConfig`](../flyte.sandbox/imageconfig) | Configuration for Docker image building at runtime. |
| [`SandboxedConfig`](../flyte.sandbox/sandboxedconfig) | Configuration for a sandboxed task executed via Monty. |
| [`SandboxedTaskTemplate`](../flyte.sandbox/sandboxedtasktemplate) | A task template that executes the function body in a Monty sandbox. |

### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a stateless Python code sandbox. |
| [`orchestrate_local()`](#orchestrate_local) | One-shot local execution of a code string in the Monty sandbox. |
| [`orchestrator_from_str()`](#orchestrator_from_str) | Create a reusable sandboxed task from a code string. |


### Variables

| Property | Type | Description |
|-|-|-|
| `ORCHESTRATOR_SYNTAX_PROMPT` | `str` |  |
| `sandbox_environment` | `TaskEnvironment` |  |

## Methods

#### create()

```python
def create(
    name: typing.Optional[str],
    code: typing.Optional[str],
    inputs: typing.Optional[dict[str, type]],
    outputs: typing.Optional[dict[str, type]],
    command: typing.Optional[list[str]],
    arguments: typing.Optional[list[str]],
    packages: typing.Optional[list[str]],
    system_packages: typing.Optional[list[str]],
    additional_commands: typing.Optional[list[str]],
    resources: typing.Optional[flyte._resources.Resources],
    image_config: typing.Optional[flyte.sandbox._code_sandbox.ImageConfig],
    image_name: typing.Optional[str],
    image: typing.Optional[str],
    auto_io: bool,
    retries: int,
    timeout: typing.Optional[int],
    env_vars: typing.Optional[dict[str, str]],
    secrets: typing.Optional[list],
    cache: str,
    block_network: bool,
) -> flyte.sandbox._code_sandbox._Sandbox
```
Create a stateless Python code sandbox.

The sandbox is **stateless** — each invocation runs in a fresh, ephemeral
container. No filesystem state, environment variables or side effects
carry over between runs.

Three modes, mutually exclusive:

- **Auto-IO mode** (`code` provided, `auto_io=True`, default): write
  just the business logic. Flyte auto-generates an argparse preamble so
  declared inputs are available as local variables, and writes declared
  scalar outputs to `/var/outputs/` automatically. No boilerplate needed.
- **Verbatim mode** (`code` provided, `auto_io=False`): run an
  arbitrary Python script as-is. CLI args for declared inputs are still
  forwarded, but the script handles all I/O itself (reading from
  `/var/inputs/`, writing to `/var/outputs/&lt;name&gt;` manually).
- **Command mode** (`command` provided): run any shell command directly,
  e.g. a compiled binary or a shell pipeline.

Call `.run()` on the returned sandbox to build the image and execute.

Example — auto-IO mode (default, no boilerplate)::

    sandbox = flyte.sandbox.create(
        name="double",
        code="result = x * 2",
        inputs={"x": int},
        outputs={"result": int},
    )
    result = await sandbox.run.aio(x=21)  # returns 42

Example — verbatim mode (complete Python script, full control)::

    sandbox = flyte.sandbox.create(
        name="etl",
        code="""
            import json, pathlib
            data = json.loads(pathlib.Path("/var/inputs/payload").read_text())
            pathlib.Path("/var/outputs/total").write_text(str(sum(data["values"])))
        """,
        inputs={"payload": File},
        outputs={"total": int},
        auto_io=False,
    )

Example — command mode::

    sandbox = flyte.sandbox.create(
        name="test-runner",
        command=["/bin/bash", "-c", pytest_cmd],
        arguments=["_", "/var/inputs/solution.py", "/var/inputs/tests.py"],
        inputs={"solution.py": File, "tests.py": File},
        outputs={"exit_code": str},
    )



| Parameter | Type | Description |
|-|-|-|
| `name` | `typing.Optional[str]` | Sandbox name. Derives task and image names. |
| `code` | `typing.Optional[str]` | Python source to run (auto-IO or verbatim mode). Mutually exclusive with `command`. |
| `inputs` | `typing.Optional[dict[str, type]]` | Input type declarations. Supported types: - Primitive: `int`, `float`, `str`, `bool` - Date/time: `datetime.datetime`, `datetime.timedelta` - IO handles: `flyte.io.File`, `flyte.io.Dir`   (bind-mounted at `/var/inputs/&lt;name&gt;`; available as a path   string in auto-IO mode) |
| `outputs` | `typing.Optional[dict[str, type]]` | Output type declarations. Supported types: - Primitive: `int`, `float`, `str`, `bool` - Date/time: `datetime.datetime` (ISO-8601), `datetime.timedelta` - IO handles: `flyte.io.File`, `flyte.io.Dir`   (user code must write the file or directory to `/var/outputs/&lt;name&gt;`) |
| `command` | `typing.Optional[list[str]]` | Entrypoint command (command mode). Mutually exclusive with `code`. |
| `arguments` | `typing.Optional[list[str]]` | Arguments forwarded to `command` (command mode only). |
| `packages` | `typing.Optional[list[str]]` | Python packages to install via pip. |
| `system_packages` | `typing.Optional[list[str]]` | System packages to install via apt. |
| `additional_commands` | `typing.Optional[list[str]]` | Extra Dockerfile `RUN` commands. |
| `resources` | `typing.Optional[flyte._resources.Resources]` | CPU / memory resources for the container. |
| `image_config` | `typing.Optional[flyte.sandbox._code_sandbox.ImageConfig]` | Registry and Python version settings. |
| `image_name` | `typing.Optional[str]` | Explicit image name, overrides the auto-generated one. |
| `image` | `typing.Optional[str]` | Pre-built image URI. Skips the build step if provided. |
| `auto_io` | `bool` | When `True` (default), Flyte wraps `code` with an auto-generated argparse preamble and output-writing epilogue so declared inputs are available as local variables and scalar outputs are collected automatically — no boilerplate needed. When `False`, `code` is run verbatim and must handle all I/O itself. |
| `retries` | `int` | Number of task retries on failure. |
| `timeout` | `typing.Optional[int]` | Task timeout in seconds. |
| `env_vars` | `typing.Optional[dict[str, str]]` | Environment variables available inside the container. |
| `secrets` | `typing.Optional[list]` | Flyte `flyte.Secret` objects to mount. |
| `cache` | `str` | Cache behaviour — `"auto"`, `"override"`, or `"disable"`. |
| `block_network` | `bool` | When `True`, blocks all outbound network access — locally via Docker ``network_mode=none``, on-cluster via a NetworkPolicy. Defaults to `False`. |

**Returns:** Configured sandbox ready to `.run()`.

#### orchestrate_local()

```python
def orchestrate_local(
    source: str,
    inputs: Dict[str, Any],
    tasks: Optional[List[Any]],
    timeout_ms: int,
) -> Any
```
One-shot local execution of a code string in the Monty sandbox.

Warning: Experimental feature: alpha — APIs may change without notice.

    Sends the code + inputs to Monty and returns the result directly,
    without creating a `TaskTemplate` or going through the controller.

    The **last expression** in *source* becomes the return value::

        result = await sandbox.orchestrate_local(
            "add(x, y) * 2",
            inputs={"x": 1, "y": 2},
            tasks=[add],
        )
        # → 6

    Parameters
    ----------
    source:
        Python code string to execute in the sandbox.
    inputs:
        Mapping of input names to their values.
    tasks:
        List of external functions (tasks, durable ops) available inside the
        sandbox. Each item's `__name__` is used as the key.
    timeout_ms:
        Sandbox execution timeout in milliseconds.


| Parameter | Type | Description |
|-|-|-|
| `source` | `str` | |
| `inputs` | `Dict[str, Any]` | |
| `tasks` | `Optional[List[Any]]` | |
| `timeout_ms` | `int` | |

#### orchestrator_from_str()

```python
def orchestrator_from_str(
    source: str,
    inputs: Dict[str, type],
    output: type,
    tasks: Optional[List[Any]],
    name: str,
    timeout_ms: int,
    cache: CacheRequest,
    retries: int,
    image: Optional[Any],
) -> CodeTaskTemplate
```
Create a reusable sandboxed task from a code string.

Warning: Experimental feature: alpha — APIs may change without notice.

    The returned `CodeTaskTemplate` can be passed to `flyte.run()`
    just like a decorated task.

    The **last expression** in *source* becomes the return value::

        pipeline = sandbox.orchestrator_from_str(
            "add(x, y) * 2",
            inputs={"x": int, "y": int},
            output=int,
            tasks=[add],
        )
        result = flyte.run(pipeline, x=1, y=2)  # → 6

    Parameters
    ----------
    source:
        Python code string to execute in the sandbox.
    inputs:
        Mapping of input names to their types.
    output:
        The return type (default `NoneType`).
    tasks:
        List of external functions (tasks, durable ops) available inside the
        sandbox. Each item's `__name__` is used as the key.
    name:
        Task name (default `"sandboxed-code"`).
    timeout_ms:
        Sandbox execution timeout in milliseconds.
    cache:
        Cache policy for the task.
    retries:
        Number of retries on failure.
    image:
        Docker image to use. If not provided, a default Debian image with
        `pydantic-monty` is created automatically.


| Parameter | Type | Description |
|-|-|-|
| `source` | `str` | |
| `inputs` | `Dict[str, type]` | |
| `output` | `type` | |
| `tasks` | `Optional[List[Any]]` | |
| `name` | `str` | |
| `timeout_ms` | `int` | |
| `cache` | `CacheRequest` | |
| `retries` | `int` | |
| `image` | `Optional[Any]` | |


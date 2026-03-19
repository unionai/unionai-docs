---
title: Code sandboxing
weight: 4
variants: +flyte +byoc +selfmanaged
sidebar_expanded: false
llm_readable_bundle: true
---

# Code sandboxing

`flyte.sandbox.create()` runs arbitrary Python code or shell commands inside an ephemeral, stateless Docker container.
The container is built on demand from declared dependencies, executed once, and discarded.
Each invocation starts from a clean slate — no filesystem state, environment variables, or side effects carry over between runs.

## Execution modes

`flyte.sandbox.create()` supports three mutually exclusive execution modes.

### Auto-IO mode

The default mode. Write only the business logic — Flyte generates the I/O boilerplate automatically.

How it works:

1. Flyte generates an `argparse` preamble that parses declared inputs from CLI arguments.
2. Declared inputs become local variables in scope.
3. After your code runs, Flyte writes declared scalar outputs to `/var/outputs/` automatically.

```python{hl_lines=[2, 4, 6, 11]}
import flyte
import flyte.sandbox

sandbox = flyte.sandbox.create(
    name="double",
    code="result = x * 2",
    inputs={"x": int},
    outputs={"result": int},
)

result = await sandbox.run.aio(x=21)  # returns 42
```

No imports, no argument parsing, no file writing. The variable `x` is available directly, and the variable `result` is captured automatically because it matches a declared output name.

A more involved example with third-party packages:

```python{hl_lines=["4-9", 12, 20, 24]}
import datetime

_stats_code = """\
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
    outputs={"mean": float, "std": float, "window_end": datetime.datetime},
    packages=["numpy"],
)

mean, std, window_end = await stats_sandbox.run.aio(
    values="1,2,3,4,5",
    dt=datetime.datetime(2024, 1, 1),
    delta=datetime.timedelta(days=1),
)
```

When there are multiple outputs, `.run()` returns them as a tuple in declaration order.

### Verbatim mode

Set `auto_io=False` to run a complete Python script with full control over I/O.
Flyte runs the script exactly as written — no injected preamble, no automatic output collection.

Your script must:

- Read inputs from `/var/inputs/<name>` (files are bind-mounted at these paths)
- Write outputs to `/var/outputs/<name>`

```python{hl_lines=["4-9", 12, 17]}
from flyte.io import File

_etl_script = """\
import json, pathlib

payload = json.loads(pathlib.Path("/var/inputs/payload").read_text())
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

total = await etl_sandbox.run.aio(payload=payload_file)
```

Use verbatim mode when you need precise control over how inputs are read and outputs are written, or when your script has its own argument parsing.

### Command mode

Run any shell command, binary, or pipeline. Provide `command` instead of `code`.

```python{hl_lines=[5]}
from flyte.io import File

linecount_sandbox = flyte.sandbox.create(
    name="line-counter",
    command=[
        "/bin/bash",
        "-c",
        "grep -c . /var/inputs/data_file > /var/outputs/line_count || echo 0 > /var/outputs/line_count",
    ],
    inputs={"data_file": File},
    outputs={"line_count": str},
)

count = await linecount_sandbox.run.aio(data_file=data_file)
```

Command mode is useful for running test suites, compiled binaries, shell pipelines, or any non-Python workload.

Use `arguments` to pass positional arguments to the command.
File inputs are bind-mounted at `/var/inputs/<name>` and can be referenced in the arguments list:

```python{hl_lines=[4, 5]}
sandbox = flyte.sandbox.create(
    name="test-runner",
    command=["/bin/bash", "-c", pytest_cmd],
    arguments=["/var/inputs/solution.py", "/var/inputs/tests.py"],
    inputs={"solution.py": File, "tests.py": File},
    outputs={"exit_code": str},
)
```

## Executing a sandbox

Call `.run()` on the sandbox object to build the image and execute.

**Async execution**

```python
result = await sandbox.run.aio(x=21)
```

**Sync execution**

```python
result = sandbox.run(x=21)
```

Both forms build the container image (if not already built), start the container, execute the code or command, collect outputs, and discard the container.

`flyte.sandbox.create()` defines the sandbox configuration and can be called at module level or inside a task. The actual container execution happens when you call `.run()`, which must run inside a Flyte task (either locally or remotely on the cluster).

### Error handling

If the sandbox code fails (non-zero exit code, Python exception, or timeout), `.run()` raises an exception with the error details.
If `retries` is set, Flyte automatically retries the execution before surfacing the error.

If the image build fails due to an invalid package, an `InvalidPackageError` is raised with the package name and the underlying error message.

## Supported types

Inputs and outputs must use one of the following types:

| Category         | Types                                     |
| ---------------- | ----------------------------------------- |
| **Primitive**    | `int`, `float`, `str`, `bool`             |
| **Date/time**    | `datetime.datetime`, `datetime.timedelta` |
| **File handles** | `flyte.io.File`                           |

### How types are handled

**In auto-IO mode:**

- **Primitive and date/time inputs** are injected as local variables with the correct Python type. Flyte generates an `argparse` preamble behind the scenes — your code just uses the variable names directly.
- **`File` inputs** are bind-mounted into the container. The input variable contains the file path as a string (e.g., `"/var/inputs/payload"`), so you can read it with `pathlib.Path(payload).read_text()`.
- **Primitive and date/time outputs** are written to `/var/outputs/<name>` automatically. Just assign the value to a variable matching the declared output name.
- **`File` outputs** are the exception — your code must write the file to `/var/outputs/<name>` manually.

**In verbatim mode:**

- All inputs (including primitives) are available at `/var/inputs/<name>`. Your script reads them directly from the filesystem.
- All outputs must be written to `/var/outputs/<name>` by your script.

**In command mode:**

- `File` inputs are bind-mounted at `/var/inputs/<name>`.
- All outputs must be written to `/var/outputs/<name>` by your command.

## Configuring the container image

### Python packages

Install PyPI packages with `packages`:

```python{hl_lines=[6]}
sandbox = flyte.sandbox.create(
    name="data-analysis",
    code="...",
    inputs={"data": str},
    outputs={"result": str},
    packages=["numpy", "pandas>=2.0", "scikit-learn"],
)
```

### System packages

Install system-level (apt) packages with `system_packages`:

```python{hl_lines=[7]}
sandbox = flyte.sandbox.create(
    name="image-processor",
    code="...",
    inputs={"image": File},
    outputs={"result": File},
    packages=["Pillow"],
    system_packages=["libgl1-mesa-glx", "libglib2.0-0"],
)
```

> [!NOTE]
> `gcc`, `g++`, and `make` are included automatically in every sandbox image.

### Additional Dockerfile commands

For advanced image customization, use `additional_commands` to inject arbitrary `RUN` commands into the Dockerfile:

```python{hl_lines=[6]}
sandbox = flyte.sandbox.create(
    name="custom-env",
    code="...",
    inputs={"x": int},
    outputs={"y": int},
    additional_commands=["curl -sSL https://example.com/setup.sh | bash"],
)
```

### Pre-built images

Skip the image build entirely by providing a pre-built image URI:

```python{hl_lines=[6]}
sandbox = flyte.sandbox.create(
    name="prebuilt",
    code="result = x + 1",
    inputs={"x": int},
    outputs={"result": int},
    image="ghcr.io/my-org/my-sandbox-image:latest",
)
```

### Image configuration

Control the registry and Python version with `ImageConfig`:

```python{hl_lines=["8-12"]}
from flyte.sandbox import ImageConfig

sandbox = flyte.sandbox.create(
    name="custom-registry",
    code="...",
    inputs={"x": int},
    outputs={"y": int},
    image_config=ImageConfig(
        registry="ghcr.io/my-org",
        registry_secret="ghcr-credentials",
        python_version=(3, 12),
    ),
)
```

## Runtime configuration

### Resources

Set CPU and memory limits for the container:

```python{hl_lines=[6]}
sandbox = flyte.sandbox.create(
    name="heavy-compute",
    code="...",
    inputs={"data": str},
    outputs={"result": str},
    resources=flyte.Resources(cpu=4, memory="8Gi"),
)
```

The default is 1 CPU and 1Gi memory.

### Retries

Automatically retry failed executions:

```python{hl_lines=[6]}
sandbox = flyte.sandbox.create(
    name="flaky-task",
    code="...",
    inputs={"x": int},
    outputs={"y": int},
    retries=3,
)
```

### Timeout

Set a maximum execution time in seconds:

```python{hl_lines=[6]}
sandbox = flyte.sandbox.create(
    name="bounded-task",
    code="...",
    inputs={"x": int},
    outputs={"y": int},
    timeout=300,  # 5 minutes
)
```

### Environment variables

Inject environment variables into the container:

```python{hl_lines=[6]}
sandbox = flyte.sandbox.create(
    name="configured-task",
    code="...",
    inputs={"x": int},
    outputs={"y": int},
    env_vars={"LOG_LEVEL": "DEBUG", "FEATURE_FLAG": "true"},
)
```

### Secrets

Mount Flyte secrets into the container:

```python{hl_lines=[6]}
sandbox = flyte.sandbox.create(
    name="authenticated-task",
    code="...",
    inputs={"query": str},
    outputs={"result": str},
    secrets=[flyte.Secret(key="api-key", as_env_var="API_KEY")],
)
```

### Caching

Control output caching behavior:

```python{hl_lines=["6-8"]}
sandbox = flyte.sandbox.create(
    name="cached-task",
    code="...",
    inputs={"x": int},
    outputs={"y": int},
    cache="auto",      # default — Flyte decides based on inputs
    # cache="override"  # force re-execution and update cache
    # cache="disable"   # no caching
)
```

## Deploying a sandbox as a task

Use `.as_task()` to convert a sandbox into a deployable `ContainerTask`.
The returned task has the generated script pre-filled as a default input, so retriggers from the UI only require user-declared inputs.

This pattern is useful when you want to define a sandbox dynamically (for example, with LLM-generated code) and then deploy it as a standalone task that others can trigger from the UI.

```python{hl_lines=[4, 11, "33-38"]}
import flyte
import flyte.sandbox
from flyte.io import File
from flyte.sandbox import sandbox_environment

# sandbox_environment provides the base runtime image for code sandboxes.
# Include it in depends_on so Flyte builds the sandbox runtime before your task runs.
env = flyte.TaskEnvironment(
    name="sandbox-demo",
    image=flyte.Image.from_debian_base(name="sandbox-demo"),
    depends_on=[sandbox_environment],
)


@env.task
async def deploy_sandbox_task() -> str:
    # Initialize the Flyte client for in-cluster operations (image building, deployment)
    flyte.init_in_cluster()

    sandbox = flyte.sandbox.create(
        name="deployable-sandbox",
        # In auto-IO mode, File inputs become path strings — read with pathlib
        code="""\
import json, pathlib
data = json.loads(pathlib.Path(payload).read_text())
total = sum(data["values"])
""",
        inputs={"payload": File},
        outputs={"total": int},
        resources=flyte.Resources(cpu=1, memory="512Mi"),
    )

    # Build the image and get a ContainerTask with the script pre-filled
    task = await sandbox.as_task.aio()

    # Create a TaskEnvironment from the task and deploy it
    deploy_env = flyte.TaskEnvironment.from_task("deployable-sandbox", task)
    versions = flyte.deploy(deploy_env)

    return versions[0].summary_repr()
```

## End-to-end example

The following example defines sandboxes in all three modes, creates helper tasks, and runs everything in a single pipeline:

{{< code file="/unionai-examples/v2/user-guide/sandboxing/code_sandbox.py" lang=python highlight="5 7 14 17-18 25 46 64">}}

## API reference

### `flyte.sandbox.create()`

| Parameter             | Type              | Description                                                |
| --------------------- | ----------------- | ---------------------------------------------------------- |
| `name`                | `str`             | Sandbox name. Derives task and image names.                |
| `code`                | `str`             | Python source to run. Mutually exclusive with `command`.   |
| `inputs`              | `dict[str, type]` | Input type declarations.                                   |
| `outputs`             | `dict[str, type]` | Output type declarations.                                  |
| `command`             | `list[str]`       | Shell command to run. Mutually exclusive with `code`.      |
| `arguments`           | `list[str]`       | Arguments forwarded to `command`.                          |
| `packages`            | `list[str]`       | Python packages to install via pip.                        |
| `system_packages`     | `list[str]`       | System packages to install via apt.                        |
| `additional_commands` | `list[str]`       | Extra Dockerfile `RUN` commands.                           |
| `resources`           | `flyte.Resources` | CPU and memory limits. Default: 1 CPU, 1Gi memory.         |
| `image_config`        | `ImageConfig`     | Registry and Python version settings.                      |
| `image_name`          | `str`             | Explicit image name (overrides auto-generated).            |
| `image`               | `str`             | Pre-built image URI (skips build).                         |
| `auto_io`             | `bool`            | Auto-generate I/O wiring. Default: `True`.                 |
| `retries`             | `int`             | Number of retries on failure. Default: `0`.                |
| `timeout`             | `int`             | Timeout in seconds.                                        |
| `env_vars`            | `dict[str, str]`  | Environment variables for the container.                   |
| `secrets`             | `list[Secret]`    | Flyte secrets to mount.                                    |
| `cache`               | `str`             | `"auto"`, `"override"`, or `"disable"`. Default: `"auto"`. |

### Sandbox methods

| Method                            | Description                                                       |
| --------------------------------- | ----------------------------------------------------------------- |
| `sandbox.run(**kwargs)`           | Build the image and execute synchronously. Returns typed outputs. |
| `await sandbox.run.aio(**kwargs)` | Async version of `run()`.                                         |
| `sandbox.as_task()`               | Build the image and return a deployable `ContainerTask`.          |
| `await sandbox.as_task.aio()`     | Async version of `as_task()`.                                     |

Both `run()` and `as_task()` accept an optional `image` parameter to provide a pre-built image URI, skipping the build step.

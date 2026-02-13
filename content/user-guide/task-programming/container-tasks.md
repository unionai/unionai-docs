---
title: Raw Container Tasks
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

Container tasks are one of Flyte's superpowers. They allow you to execute tasks using any container image without requiring the Flyte SDK to be installed in that container. This means you can run code written in any language, execute shell scripts, or even use pre-built containers pulled directly from the internet while still maintaining Flyte's data orchestration capabilities.

## What are Container Tasks?

A container task is a special type of Flyte task that executes arbitrary container images. Unlike standard `@task` decorated functions that require the Flyte SDK, container tasks can run:

- Code written in any programming language (Rust, Go, Java, R, etc.)
- Legacy containers with unsupported Python versions
- Pre-built bioinformatics or scientific computing containers
- Shell scripts and command-line tools
- Dynamically generated code in sandboxed environments

## How Data Flows In and Out

The magic of container tasks lies in Flyte's **copilot sidecar system**. When you execute a container task, Flyte:

1. Launches your specified container alongside a copilot sidecar container
2. Uses shared Kubernetes pod volumes to pass data between containers
3. Reads inputs from `input_data_dir` and writes outputs to `output_data_dir`
4. Automatically handles serialization and deserialization of typed data

This means you can construct workflows where some tasks are container tasks while others are Python functions, and data will flow seamlessly between them.

## Basic Usage

Here's a simple example that runs a shell command in an Alpine container:

```python
import flyte
from flyte.extras import ContainerTask

greeting_task = ContainerTask(
    name="echo_and_return_greeting",
    image=flyte.Image.from_base("alpine:3.18"),
    input_data_dir="/var/inputs",
    output_data_dir="/var/outputs",
    inputs={"name": str},
    outputs={"greeting": str},
    command=[
        "/bin/sh",
        "-c",
        "echo 'Hello, my name is {{.inputs.name}}.' | tee -a /var/outputs/greeting"
    ],
)
```

### Template Syntax for Inputs

Container tasks support template-style references to inputs using the syntax `{{.inputs.<input_name>}}`. This gets replaced with the actual input value at runtime:

```python
command=["/bin/sh", "-c", "echo 'Processing {{.inputs.user_id}}' > /var/outputs/result"]
```

### Using Container Tasks in Workflows

Container tasks integrate seamlessly with Python tasks:

```python
container_env = flyte.TaskEnvironment.from_task("container_env", greeting_task)
env = flyte.TaskEnvironment(name="hello_world", depends_on=[container_env])

@env.task
async def say_hello(name: str = "flyte") -> str:
    print("Hello container task")
    return await greeting_task(name=name)
```

## Advanced: Passing Files and Directories

Container tasks can accept `File` and `Dir` inputs. For these types, use path-based syntax (not template syntax) in your commands:

```python
from flyte.io import File
import pathlib

code_runner = ContainerTask(
    name="python_code_runner",
    image="ghcr.io/astral-sh/uv:debian-slim",
    input_data_dir="/var/inputs",
    output_data_dir="/var/outputs",
    inputs={"script.py": File, "a": int, "b": int},
    outputs={"result": int},
    command=[
        "/bin/sh",
        "-c",
        "uv run /var/inputs/script.py {{.inputs.a}} {{.inputs.b}} > /var/outputs/result"
    ],
)

@env.task
async def execute_script() -> int:
    path = pathlib.Path(__file__).parent / "my_script.py"
    script_file = await File.from_local(path)
    return await code_runner(**{"script.py": script_file, "a": 10, "b": 20})
```

Note that when passing files, the input key can include the filename (e.g., `"script.py"`), and you reference it in the command as `/var/inputs/script.py`.

## Use Case: Agentic Sandbox Execution

Container tasks are perfect for running AI-generated code in isolated environments. You can generate a data analysis script dynamically and execute it safely:

```python
import flyte
from flyte.extras import ContainerTask
from flyte.io import File
import pathlib

env = flyte.TaskEnvironment(name="agentic_sandbox")

@env.task
async def run_generated_code(script_content: str, param_a: int, param_b: int) -> int:
    # Define a container task that runs arbitrary Python code
    sandbox = ContainerTask(
        name="code_sandbox",
        image="ghcr.io/astral-sh/uv:debian-slim",
        input_data_dir="/var/inputs",
        output_data_dir="/var/outputs",
        inputs={"script": File, "a": int, "b": int},
        outputs={"result": int},
        command=[
            "/bin/sh",
            "-c",
            "uv run --script /var/inputs/script {{.inputs.a}} {{.inputs.b}} > /var/outputs/result"
        ],
    )

    # Save the generated script to a temporary file
    temp_path = pathlib.Path("/tmp/generated_script.py")
    temp_path.write_text(script_content)

    # Execute it in the sandbox
    script_file = await File.from_local(temp_path)
    return await sandbox(script=script_file, a=param_a, b=param_b)
```

This pattern allows you to:
- Generate code using LLMs or other AI systems
- Execute it in a controlled, isolated environment
- Capture results and integrate them back into your workflow
- Maintain full observability and reproducibility

## Use Case: Legacy and Specialized Containers

Many scientific and bioinformatics tools are distributed as pre-built containers. Container tasks let you integrate them directly:

```python
# Run a bioinformatics tool
blast_task = ContainerTask(
    name="run_blast",
    image="ncbi/blast:latest",
    input_data_dir="/data",
    output_data_dir="/results",
    inputs={"query": File, "database": str},
    outputs={"alignments": File},
    command=[
        "blastn",
        "-query", "/data/query",
        "-db", "{{.inputs.database}}",
        "-out", "/results/alignments",
        "-outfmt", "6"
    ],
)

# Run legacy code with an old Python version
legacy_task = ContainerTask(
    name="legacy_python",
    image="python:2.7",  # Unsupported Python version
    input_data_dir="/app/inputs",
    output_data_dir="/app/outputs",
    inputs={"data_file": File},
    outputs={"processed": File},
    command=[
        "python",
        "/legacy_app/process.py",
        "/app/inputs/data_file",
        "/app/outputs/processed"
    ],
)
```

## Use Case: Multi-Language Workflows

Build workflows that span multiple languages:

```python
# Rust task for high-performance computation
rust_task = ContainerTask(
    name="rust_compute",
    image="rust:1.75",
    inputs={"n": int},
    outputs={"result": int},
    input_data_dir="/inputs",
    output_data_dir="/outputs",
    command=["./compute_binary", "{{.inputs.n}}"],
)

# Python task for orchestration
@env.task
async def multi_lang_workflow(iterations: int) -> dict:
    # Call Rust task for heavy computation
    computed = await rust_task(n=iterations)

    # Process results in Python
    processed = await python_analysis_task(computed)

    return {"rust_result": computed, "analysis": processed}
```

## Configuration Options

### ContainerTask Parameters

- **name**: Unique identifier for the task
- **image**: Container image to use (string or `Image` object)
- **command**: Command to execute in the container (list of strings)
- **inputs**: Dictionary mapping input names to types
- **outputs**: Dictionary mapping output names to types
- **input_data_dir**: Directory where Flyte writes input data (default: `/var/inputs`)
- **output_data_dir**: Directory where Flyte reads output data (default: `/var/outputs`)
- **arguments**: Additional command arguments (list of strings)
- **metadata_format**: Format for metadata serialization (`"JSON"`, `"YAML"`, or `"PROTO"`)
- **local_logs**: Whether to print container logs during local execution (default: `True`)

### Supported Input/Output Types

Container tasks support all standard Flyte types:

- Primitives: `str`, `int`, `float`, `bool`
- Temporal: `datetime.datetime`, `datetime.timedelta`
- File system: `File`, `Dir`
- Complex types: dataclasses, Pydantic models (serialized as JSON/YAML/PROTO)

## Best Practices

1. **Use specific image tags**: Prefer `alpine:3.18` over `alpine:latest` for reproducibility
2. **Keep containers focused**: Each container task should do one thing well
3. **Handle errors gracefully**: Ensure your container commands exit with appropriate status codes
4. **Test locally first**: Container tasks can run locally with Docker, making debugging easier
5. **Consider image size**: Smaller images lead to faster task startup times
6. **Document input/output contracts**: Clearly specify what data flows in and out

## Local Execution

Container tasks require Docker to be installed and running on your local machine. When you run them locally, Flyte will:

1. Pull the specified image (if not already available)
2. Mount local directories for inputs and outputs
3. Stream container logs to your console
4. Extract outputs after container completion

This makes it easy to develop and test container tasks before deploying to a remote cluster.

## When to Use Container Tasks

Choose container tasks when you need to:

- Run code in languages other than Python
- Execute pre-built tools or legacy applications
- Isolate potentially unsafe code (AI-generated scripts)
- Use specific runtime environments or dependencies
- Integrate external tools without Python wrappers
- Execute shell scripts or command-line utilities

For Python code that can use the Flyte SDK, standard `@task` decorated functions are usually simpler and more efficient.

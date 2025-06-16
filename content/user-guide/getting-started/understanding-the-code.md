---
title: Understanding the code
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Understanding the code

This is a simple "Hello, world!" example consisting of flat directory:

```shell
├── LICENSE
├── README.md
├── hello_world.py
├── pyproject.toml
└── uv.lock
```

## Python code

The `hello_world.py` file illustrates the essential components of a {{< key product_name >}} workflow:

{{< variant flyte >}}
{{< markdown >}}

```python
# Hello World

import flytekit as fl
import os

image_spec = fl.ImageSpec(
    # The name of the image. This image will be used by the `say_hello`` task.
    name="say-hello-image",

    # Lock file with dependencies to be installed in the image.
    requirements="uv.lock",

    # Image registry to to which this image will be pushed.
    # Set the Environment variable FLYTE_IMAGE_REGISTRY to the URL of your registry.
    # The image will be built on your local machine, so enure that your Docker is running.
    # Ensure that pushed image is accessible to your Flyte cluster, so that it can pull the image
    # when it spins up the task container.
    registry=os.environ['FLYTE_IMAGE_REGISTRY']
)


@fl.task(container_image=image_spec)
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@fl.workflow
def hello_world_wf(name: str = "world") -> str:
    greeting = say_hello(name=name)
    return greeting
```

{{< /markdown >}}
{{< /variant >}}

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

```python
# Hello World

import union

image_spec = union.ImageSpec(
    # The name of the image. This image will be used byt he say_hello task
    name="say-hello-image",

    # Lock file with dependencies to install in image
    requirements="uv.lock",

    # Build the image using Union's built-in cloud builder (not locally on your machine)
    builder="union",
)


@union.task(container_image=image_spec)
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@union.workflow
def hello_world_wf(name: str = "world") -> str:
    greeting = say_hello(name=name)
    return greeting
```

{{< /markdown >}}
{{< /variant >}}

### ImageSpec

The `ImageSpec` object is used to define the container image that will run the tasks in the workflow.

Here we have the simplest possible `ImageSpec` object, which specifies:

* The `name` of the image.
  * This name will be used to identify the image in the container registry.

* The `requirements` parameter.
  * We specify that the requirements should be read from the `uv.lock` file.

{{< variant flyte >}}
{{< markdown >}}

* The `registry` to which the image will be pushed.
  * Here we use the environment variable `FLYTE_IMAGE_REGISTRY` to hold the URL of the registry.
  * You must ensure that this environment variable is correctly set before you register the workflow.
  * You must also ensure that when the image is pushed to the registry, it will be accesible to your Flyte cluster, so that it can pull the image when it spins up the task container.

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

* The `builder` to use to build the image.
  * We specify `union` to indicate that the image is built using {{< key product_name >}}'s cloud image builder.

{{< /markdown >}}
{{< /variant >}}

See [ImageSpec](../development-cycle/image-spec) for more information.

### Tasks

The `@{{< key kit_as >}}.task` decorator indicates a Python function that defines a [**task**](../core-concepts/tasks).
A task tasks some input and produces an output.
When deployed to {{< key product_name >}} cluster, each task runs in its own Kubernetes pod.
For a full list of task parameters, see [Task parameters](../core-concepts/tasks/task-parameters).

### Workflow

The `@{{< key kit_as >}}.workflow` decorator indicates a function that defines a [workflow](../core-concepts/workflows).
This function contains references to the tasks defined elsewhere in the code.

A workflow appears to be a Python function but is actually a [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) that only supports a subset of Python syntax and semantics.

When deployed to {{< key product_name >}}, the workflow function is compiled to construct the directed acyclic graph (DAG) of tasks, defining the order of execution of task pods and the data flow dependencies between them.

> [!NOTE] `@{{< key kit_as >}}.task` and `@{{< key kit_as >}}.workflow` syntax
> * The `@{{< key kit_as >}}.task` and `@{{< key kit_as >}}.workflow` decorators will only work on functions at the top-level
>   scope of the module.
> * You can invoke tasks and workflows as regular Python functions and even import and use them in
>   other Python modules or scripts.
> * Task and workflow function signatures must be type-annotated with Python type hints.
> * Task and workflow functions must be invoked with keyword arguments.

## pyproject.toml

The `pyproject.toml` is the standard project configuration used by `uv`.
It specifies the project dependencies and the Python version to use.
The default `pyproject.toml` file created by `{{< key cli >}} init` from the `{{< key product >}}-simple` template looks like this

```toml
[project]
name = "{{< key product >}}-simple"
version = "0.1.0"
description = "A simple {{< key product_name >}} project"
readme = "README.md"
requires-python = ">=3.9,<3.13"
dependencies = ["{{< key kit >}}"]
```

(You can update the `name` and `description` to match the actual name of your project, `my-project`, if you like).

The most important part of the file is the list of dependencies, in this case consisting of only one package, `{{< key kit >}}`.
See [uv > Configuration > Configuration files](https://docs.astral.sh/uv/configuration/files/) for details.

## uv.lock

The `uv.lock` file is generated from `pyproject.toml` by `uv sync` command.
It contains the exact versions of the dependencies required by the project.

The `uv.lock` included in the `init` template may not reflect the latest version of the dependencies, so you should update it by doing a fresh `uv sync`.

See [uv > Concepts > Projects > Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) for details.

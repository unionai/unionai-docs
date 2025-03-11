---
title: Understanding the code
weight: 4
variants: "+flyte +serverless +byoc +byok"
---

# Understanding the code

This is a simple "Hello, world!" example consisting of flat directory:

```shell
.
├── LICENSE
├── README.md
├── hello_world.py
├── pyproject.toml
└── uv.lock
```

## Python code

The `hello_world.py` file illustrates the essential components of a {@= Product =@} workflow:

{{< if-variant "serverless byoc byok" >}}

```python
"""Hello World"""

import union

image_spec = union.ImageSpec(

    # Build the image using Union's built-in cloud builder (not locally on your machine)
    builder="union",

    # The name of the image. This image will be used byt he say_hello task
    name="say-hello-image",

    # Lock file with dependencies to install in image
    requirements="uv.lock",

)

@union.task(container_image=image_spec)
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@union.workflow
def hello_world_wf(name: str = "world") -> str:
    greeting = say_hello(name=name)
    return greeting
```

{{< /if-variant >}}
{{< if-variant flyte >}}

```python
"""Hello World"""

import flytekit as fl

image_spec = fl.ImageSpec(

    # The name of the image. This image will be used byt he say_hello task
    name="say-hello-image",

    # Lock file with dependencies to install in image
    requirements="uv.lock",
)

@fl.task(container_image=image_spec)
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@fl.workflow
def hello_world_wf(name: str = "world") -> str:
    greeting = say_hello(name=name)
    return greeting
```

{{< /if-variant >}}


### ImageSpec

The `ImageSpec` object is used to define the container image that will run the tasks in the workflow.

Here we have the simplest possible `ImageSpec` object, which specifies:

{{< if-variant "serverless byoc byok" >}}

* The `builder` to use to build the image. We specify `union` to indicate that the image is built using Union's cloud image builder.

{{< /if-variant >}}

* The `name` of the image. This name will be used to identify the image in the container registry.

* The `requirements` parameter. We specify that the requirements should be read from the `uv.lock` file.

See [ImageSpec](../development-cycle/image-spec.md) for more information.


### Tasks

The `{@= task =@}` decorator indicates a Python function that defines a [**task**](../core-concepts/tasks/index.md).
A task tasks some input and produces an output.
When deployed to Union cluster, each task runs in its own Kubernetes pod.
For a full list of task parameters, see [Task parameters](../core-concepts/tasks/task-parameters.md).


### Workflow

The `{@= workflow =@}` decorator indicates a function that defines a [workflow](../core-concepts/workflows/index.md).
This function contains references to the tasks defined elsewhere in the code.

A workflow appears to be a Python function but is actually a [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) that only supports a subset of Python syntax and semantics.

When deployed to Union, the workflow function is compiled to construct the directed acyclic graph (DAG) of tasks, defining the order of execution of task pods and the data flow dependencies between them.

{{< note "`{@= task =@}` and `{@= workflow =@}` syntax" >}}
* The `{@= task =@}` and `{@= workflow =@}` decorators will only work on functions at the top-level scope of the module.
* You can invoke tasks and workflows as regular Python functions and even import and use them in other Python modules or scripts.
* Task and workflow function signatures must be type-annotated with Python type hints.
* Task and workflow functions must be invoked with keyword arguments.
{{< /note >}}


## pyproject.toml

The `pyproject.toml` is the standard project configuration used by `uv`.
In particular, it specifies the project dependencies and the Python version to use.
The default `pyproject.toml` file created by `{@= cli =@} init` from the `{@= product =@}-simple` template looks like this

```toml
[project]
name = "{@= product =@}-simple"
version = "0.1.0"
description = "A simple {@= Product =@} project"
readme = "README.md"
requires-python = ">=3.9,<3.13"
dependencies = ["{@= kit =@}"]
```

(You can update the `name` and `description` to match the actual name of your project, `my-project`, if you like).

The most important part of the file is the list of dependencies, in this case consisting of only one package, `{@= kit =@}`.
See [uv > Configuration > Configuration files](https://docs.astral.sh/uv/configuration/files/) for details.

## uv.lock

The `uv.lock` file is generated from `pyproject.toml` by `uv sync` command.
It contains the exact versions of the dependencies required by the project.
See [uv > Concepts > Projects > Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) for details.

---
title: Local dependencies
weight: 6
variants: +flyte +serverless +byoc +byok
---

# Local dependencies

During the development cycle you will want to be able to run your workflows both locally on your machine and remotely on Union.
To enable this, you need to ensure that the required dependencies are installed in both places.
Here we will explain how to install your dependencies locally.
For information on how to make your dependencies available on Union, see [Remote dependencies with ImageSpec](./remote-dependencies-with-image-spec.md).

## Define your dependencies in your `pyproject.toml`

We recommend using the [`uv` tool](https://docs.astral.sh/uv/) for project and dependency management.

When using the best way declare your dependencies is to list them under `dependencies` in your `pyproject.toml` file, like this:

```toml
[project]
name = "union-simple"
version = "0.1.0"
description = "A simple Union project"
readme = "README.md"
requires-python = ">=3.9,<3.13"
dependencies = ["union"]
```

## Create a Python virtual environment

Ensure that your Python virtual environment is properly set up with the required dependencies.

Using `uv`, you can install the dependencies with the command:

```shell
$ uv sync
```

You can then activate the virtual environment with:

```shell
source .venv/bin/activate
```

> [!NOTE] `activate` vs `uv run`
> When running the `union` CLI within your local project you must run it in the virtual environment _associated with_ that project.
>
> To run union within your project's virtual environment using `uv`, you can prefix it use the `uv run` command. For example:
>
> `uv run union ...`
>
> Alternatively, you can activate the virtual environment with `source .venv/bin/activate` and then run the `union` command directly.
> In our examples we assume that you are doing the latter.

Having installed your dependencies in your local environment, you can now [run your workflows locally using `union run`](./running-your-code.md).

The next step is to ensure that the same dependencies are also [available in the remote environment on Union](./remote-dependencies-with-image-spec.md).

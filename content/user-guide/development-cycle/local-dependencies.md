---
title: Local dependencies
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Local dependencies

During the development cycle you will want to be able to run your workflows both locally on your machine and remotely on {{< key product_name >}}.
To enable this, you need to ensure that the required dependencies are installed in both places.
Here we will explain how to install your dependencies locally.
For information on how to make your dependencies available on {{< key product_name >}}, see [ImageSpec](./image-spec).

## Define your dependencies in your `pyproject.toml`

We recommend using the [`uv` tool](https://docs.astral.sh/uv/) for project and dependency management.

When using the best way declare your dependencies is to list them under `dependencies` in your `pyproject.toml` file, like this:

```toml
[project]
name = "union-simple"
version = "0.1.0"
description = "A simple {{< key product_name >}} project"
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
$ source .venv/bin/activate
```

> [!NOTE] `activate` vs `uv run`
> When running the {{< key cli_name >}} CLI within your local project you must run it in the virtual environment _associated with_ that project.
>
> To run `{{< key cli >}}` within your project's virtual environment using `uv`, you can prefix it use the `uv run` command. For example:
>
> `uv run {{< key cli >}} ...`
>
> Alternatively, you can activate the virtual environment with `source .venv/bin/activate` and then run the `{{< key cli >}}` command directly.
> In our examples we assume that you are doing the latter.

Having installed your dependencies in your local environment, you can now [run your workflows locally using `{{< key cli >}} run`](./running-your-code).

The next step is to ensure that the same dependencies are also [available in the remote environment on {{< key product_name >}}](./image-spec).

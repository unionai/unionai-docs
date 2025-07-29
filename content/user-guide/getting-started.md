---
title: Getting started
weight: 20
variants: +flyte +serverless +byoc +selfmanaged
---

# Getting started

This section gives you a quick introduction to writing and running workflows on Union and Flyte 2.

## Installing Flyte 2

### Install uv

First, [install the `uv` package manager](https://docs.astral.sh/uv/getting-started/installation/).

> [!NOTE]
> You will need to use the [`uv` package manager](https://docs.astral.sh/uv/) to run the examples in this guide.
> In particular, we leverage `uv`'s ability to [embed dependencies directly in scripts](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).

### Ensure that you have Python 3.10 or later installed

Install Python 3.13 or later on your machine and pin it as the default Python version for `uv`:

```shell
uv python install 3.13
uv python pin 3.13 --global
```

### Create and activate a Python virtual environment

In your working directory, create a Python virtual environment and activate it:

```shell
uv venv
source .venv/bin/activate
```

### Install the `flyte` package

Install the latest flyte package in the virtual environment (we are currently in beta, so you have to enable prerelease installation):

```shell
uv pip install --no-cache --prerelease=allow --upgrade flyte
```

## Configuration setup

### Create a config.yaml

Next, create a `config.yaml` file that points to your Union/Flyte instance using the [`flyte create config`](../api-reference/flyte-cli#flyte-create-config) command.

```shell
flyte create config \
    --endpoint <your-instance-endpoint> \
    --builder <image-builder> \
    --domain <default-domain> \
    --project <default-project>
```

For example, this command:

```shell
flyte create config \
    --endpoint my-instance.example.com \
    --builder remote \
    --domain development \
    --project my-project
```

will create this `config.yaml` file:

{{< code file="/external/migrate-to-unionai-examples-flyte2/config.yaml" lang="yaml" >}}

See [Setting up a configuration file](./configuration#setting-up-a-configuration-file) for details.

## Hello world example

We'll start with a "Hello world" example.
Create a file called `hello.py` with the following content:

{{< code file="/external/migrate-to-unionai-examples-flyte2/hello.py" lang="python" >}}

## Understanding the code

In the code above we do the following:

* Import the `flyte` package.
* Define a `TaskEnvironment` to group the configuration used by tasks.
* Define two tasks using the `@env.task` decorator.
    * Tasks are regular Python functions, and each runs in its own container.
    * When deployed to your Union/Flyte instance, each task will run in its own separate container.
    * Both tasks use the same `env` (the same `TaskEnvironment`) so, while each runs in its own container, those containers will be configured identically.

> [!NOTE]
> In this guide we adopt a few conventions to make each example script as self-contained as possible
> and therefore easy to run:
>
> * Each script has a main guard that programmatically deploys and runs the tasks defined in the same file.
>   All you have to do is execute the script itself.
> * Each script has a comment at the top that specifies the dependencies required to run it.
>   These dependencies are automatically installed locally when you run the script using `uv run`.
>   This is [a feature of `uv`](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies),
>   and one reason that we recommend using it.

## Running the code

Make sure that your `config.yaml` file is in the same directory as your `hello.py` script.

Now, run the script with:

```shell
uv run --prerelease allow hello.py
```

**This executes the script locally, but in doing so, it actually deploys the tasks defined in the script to your Union/Flyte instance and runs those there.**

The main guard section in the script performs a `flyte.init_from_config` to set up the connection with your Union/Flyte instance and a `flyte.run` to send your task code to that instance and execute it there.

## Viewing the results

In your terminal, you should see output like this:

```shell
cg9s54pksbjsdxlz2gmc
https://my-instance.example.com/v2/runs/project/my-project/domain/development/cg9s54pksbjsdxlz2gmc
Run 'a0' completed successfully.
```

Click the link to go to your Union instance and see the run in the UI:

![V2 UI](../_static/images/user-guide/v2ui.png)

## Understanding the UI

<!-- TODO: Add explanation of the UI elements and their functionality -->

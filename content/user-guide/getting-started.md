---
title: Getting started
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Getting started

This section gives you a quick introduction to writing and running workflows on Union and Flyte.

## Configuration setup

### Install uv

First, [install the `uv` package manager](https://docs.astral.sh/uv/getting-started/installation/).

> [!NOTE]
> We strongly recommend using the [`uv` package manager](https://docs.astral.sh/uv/).
> In this guide we use it to enable [embedding of dependencies directly in scripts](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).
> You can also use its `uvx` sub-command to it [run the `flyte` CLI instantly](https://docs.astral.sh/uv/concepts/tools/) without installing it in a virtual environment.

### Create a config.yaml

Next, create a `config.yaml` file that points to your Union/Flyte instance using the [`flyte create config`](../api-reference/flyte-cli#flyte-create-config) command.

```shell
uvx --prerelease allow flyte create config \
    --endpoint <your-instance-endpoint> \
    --builder <image-builder> \
    --domain <default-domain> \
    --project <default-project>
```

> [!NOTE]
> Here we use the [`flyte` CLI](../api-reference/flyte-cli) via [`uvx`](https://docs.astral.sh/uv/concepts/tools/)
> to quickly install the `flyte` package and invoke the `flyte` CLI in one step.
> You can also [install the `flyte` package in a virtual environment]() and use the `flyte` CLI directly, but using `uvx` is more convenient for quick examples.
>
> In further examples, we show only the `flyte` command itself and assume that you have either installed
> the `flyte` package in your Python environment or are using `uvx` to run it.

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


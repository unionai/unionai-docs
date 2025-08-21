---
title: Getting started
weight: 20
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Getting started

This section gives you a quick introduction to writing and running workflows on Union and Flyte 2.

## Prerequisites

### Install uv

First, [install the `uv` package manager](https://docs.astral.sh/uv/getting-started/installation/).

> [!NOTE]
> You will need to use the [`uv` package manager](https://docs.astral.sh/uv/) to run the examples in this guide.
> In particular, we leverage `uv`'s ability to [embed dependencies directly in scripts](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).

### Ensure that you have Python 3.13 or later installed

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

## Install the `flyte` package

Install the latest flyte package in the virtual environment (we are currently in beta, so you have to enable prerelease installation):

```shell
uv pip install --no-cache --prerelease=allow --upgrade flyte
```

## Create a config.yaml

{{< variant flyte >}}
{{< markdown >}}

Next, create a `config.yaml` file that points to your Flyte instance.
Use the [`flyte create config`](../../api-reference/flyte-cli#flyte-create-config) command, making the following changes:

- Replace `my-org.my-company.com` with the actual URL of your Flyte backend instance.
  You can simply copy the domain part of the URL from your browser when logged into your backend instance.
- Replace `my-project` with an actual project.
  The project you specify must already exist on your Flyte backend instance.

```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --builder local \
    --domain development \
    --project my-project
```

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

Next, create a `config.yaml` file that points to your Union instance.
Use the [`flyte create config`](../../api-reference/flyte-cli#flyte-create-config) command, making the following changes:

- Replace `my-org.my-company.com` with the actual URL of your Union backend instance.
  You can simply copy the domain part of the URL from your browser when logged into your backend instance.
- Replace `my-project` with an actual project.
  The project you specify must already exist on your Union backend instance.

```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --builder remote \
    --domain development \
    --project my-project
```

{{< /markdown >}}
{{< /variant >}}

This will create a `config.yaml` file in your current working directory.
See [Setting up a configuration file](./local-setup#setting-up-a-configuration-file) for details.

## Hello world example

Create a file called `hello.py` with the following content:

{{< code file="/external/migrate/user-guide/getting-started/hello.py" lang="python" >}}

## Understanding the code

In the code above we do the following:

- Import the `flyte` package.
- Define a `TaskEnvironment` to group the configuration used by tasks.
- Define two tasks using the `@env.task` decorator.
  - Tasks are regular Python functions, but each runs in its own container.
  - When deployed to your Union/Flyte instance, each task execution will run in its own separate container.
  - Both tasks use the same `env` (the same `TaskEnvironment`) so, while each runs in its own container, those containers will be configured identically.

## Running the code

Make sure that your `config.yaml` file is in the same directory as your `hello.py` script.

Now, run the script with:

```shell
uv run --prerelease allow hello.py
```

The main guard section in the script performs a `flyte.init_from_config` to set up the connection with your Union/Flyte instance and a `flyte.run` to send your task code to that instance and execute it there.

> [!NOTE]
> The example scripts in this guide have a main guard that programmatically deploys and runs the tasks defined in the same file.
> All you have to do is execute the script itself.
> You can also deploy tasks using the `flyte` CLI instead. We will cover this in a later section.

## Viewing the results

In your terminal, you should see output like this:

```shell
cg9s54pksbjsdxlz2gmc
https://my-instance.example.com/v2/runs/project/my-project/domain/development/cg9s54pksbjsdxlz2gmc
Run 'a0' completed successfully.
```

Click the link to go to your Union instance and see the run in the UI:

![V2 UI](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/user-guide/v2ui.png)

<!-- TODO: Add explanation of the UI elements and their functionality
## Understanding the UI
-->

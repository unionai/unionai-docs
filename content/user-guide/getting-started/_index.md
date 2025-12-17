---
title: Getting started
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Getting started

This section gives you a quick introduction to writing and running workflows on Union and Flyte 2.

## Prerequisites

You will need the following:
- An active Python virtual environment with Python 3.10 or later.
- The URL of you Union/Flyte instance.
- An existing project set up on your Union/Flyte instance where you have permission to run workflows.

## Install the `flyte` package

Install the latest `flyte` package in the virtual environment (we are currently in beta, so you will have to enable prerelease installation). For example:

```shell
pip install --no-cache --prerelease=allow --upgrade flyte
```

Check that installation succeeded (and that you have activated your virtual environment):

```shell
flyte --version
```

## Create a config.yaml

{{< variant flyte >}}
{{< markdown >}}

Next, create a configuration file that points to your Flyte instance.
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

### Ensure local Docker is working

> [!NOTE]
> We are using the `--builder local` option here to specify that we want to [build images](../task-configuration/container-images) locally.
> If you were using a Union instance, you would typically use `--builder remote` instead to use Union's remote image builder.
> With Flyte OSS instances, `local` is the only option available.

To enable local image building, ensure that
- You have Docker installed and running on your machine
- You have permission to read from the public GitHub `ghcr.io` registry.
- You have successfully logged into the `ghcr.io` registry using Docker:

```shell
docker login ghcr.io
```

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

Next, create a configuration file that points to your Union instance.
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

By default, this will create a `./.flyte/config.yaml` file in your current working directory.
See [Setting up a configuration file](./local-setup#setting-up-a-configuration-file) for details.

{{< note >}}
Run `flyte get config` to see the current configuration file being used by the `flyte` CLI.
{{< /note >}}

## Hello world example

Create a file called `hello.py` with the following content:

{{< code file="/external/unionai-examples/v2/user-guide/getting-started/hello.py" lang="python" >}}

## Understanding the code

In the code above we do the following:

- Import the `flyte` package.
- Define a `TaskEnvironment` to group the configuration used by tasks.
- Define two tasks using the `@env.task` decorator.
  - Tasks are regular Python functions, but each runs in its own container.
  - When deployed to your Union/Flyte instance, each task execution will run in its own separate container.
  - Both tasks use the same `env` (the same `TaskEnvironment`) so, while each runs in its own container, those containers will be configured identically.

## Running the code

Assuming that your current directory looks like this:

```
.
├── hello.py
└── .flyte
    └── config.yaml
```

and your virtual environment is activated, you can run the script with:

```shell
flyte run hello.py main
```

This will package up the code and send it to your Flyte/Union instance for execution.

## Viewing the results

In your terminal, you should see output like this:

```shell
cg9s54pksbjsdxlz2gmc
https://my-instance.example.com/v2/runs/project/my-project/domain/development/cg9s54pksbjsdxlz2gmc
Run 'a0' completed successfully.
```

Click the link to go to your Flyte/Union instance and see the run in the UI:

![V2 UI](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/user-guide/v2ui.png)

<!-- TODO: Add explanation of the UI elements and their functionality
## Understanding the UI
-->

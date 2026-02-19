---
title: Quickstart
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Quickstart

Let's get you up and running with your first workflow.

## What you'll need

- Python 3.10+ in a virtual environment
- Access to a {{< key product_name >}} instance (you'll need the URL of your instance)

## Install the SDK

Install the `flyte` package:

```shell
pip install flyte
```

Verify it worked:

```shell
flyte --version
```

## Configure your connection

{{< variant flyte >}}
{{< markdown >}}

Create a config file pointing to your Flyte instance. Replace the placeholder value with your actual endpoint:

```shell
flyte create config \
    --endpoint <my-org.my-company.com> \
    --domain development \
    --project flytesnacks \
    --builder local
```

We will use the `flytesnacks` project and the `development` domain.
These exist by default on any newly installed Flyte instance.

### Set up local Docker

Since Flyte OSS uses local image building, you'll need Docker running and logged into the GitHub registry:

```shell
docker login ghcr.io
```

> [!NOTE]
> The `--builder local` option means images are [built locally](./task-configuration/container-images). Union instances can use `--builder remote` instead.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

Create a config file pointing to your Union instance. Replace the placeholder value with your actual endpoint:

```shell
flyte create config \
    --endpoint <my-org.my-company.com> \
    --domain development \
    --project flytesnacks \
    --builder remote
```

We will use the `flytesnacks` project and the `development` domain.
These exist by default on any newly installed Union.ai instance.

{{< /markdown >}}
{{< /variant >}}

This creates `./.flyte/config.yaml` in your current directory. See [Setting up a configuration file](./local-setup#configuration-file) for more options.

{{< note >}}
Run `flyte get config` to check which configuration is currently active.
{{< /note >}}

## Write your first workflow

Create `hello.py`:

{{< code file="/external/unionai-examples/v2/user-guide/getting-started/hello.py" lang="python" >}}

Here's what's happening:

- **`TaskEnvironment`** specifies configuration for your tasks (container image, resources, etc.)
- **`@env.task`** turns Python functions into tasks that run remotely
- Both tasks share the same `env`, so they'll have identical configurations

## Run it

With your config file in place:

```
.
├── hello.py
└── .flyte
    └── config.yaml
```

Run the workflow:

```shell
flyte run hello.py main
```

This packages your code and sends it to your Union/Flyte instance for execution.

## See the results

You'll see output like:

```shell
cg9s54pksbjsdxlz2gmc
https://my-instance.example.com/v2/runs/project/my-project/domain/development/cg9s54pksbjsdxlz2gmc
Run 'a0' completed successfully.
```

Click the link to view your run in the UI:

![V2 UI](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/user-guide/v2ui.png)

## Next steps

Now that you've run your first workflow:

- [**Core concepts**](./core-concepts/_index): Understand the core concepts of Flyte programming

---
title: Running your code
weight: 8
variants: +flyte +serverless +byoc +byok
---

# Running your code

## Set up your development environment

If you have not already done so, follow the [Getting started](../getting-started/_index.md) section to sign in to {{< key product_name >}}, and set up your local environment.

## CLI commands for running your code

The {{< key cli_name >}} CLI provides a set of commands that allow you to deploy and run your code at different stages of the development cycle:

<!-- TODO: Link to the union commands below to the reference section -->

1. `{{< key cli >}} run`: For deploying and running a single script immediately in your local Python environment.
2. `{{< key cli >}} run --remote`: For deploying and running a single script immediately in the cloud on {{< key product_name >}}.
3. `{{< key cli >}} register`: For deploying multiple scripts to {{< key product_name >}} and running them from the Web interface.
{{< variant byoc byok serverless >}}
{{< markdown >}}
4. `{{< key cli >}} package` and `uctl register`: For deploying workflows to production and for scripting within a CI/CD pipeline.

> [!NOTE]
> In some cases, you may want to test your code in a local cluster before deploying it to {{< key product_name >}}.
> This step corresponds to using the commands 2, 3, or 4, but targeting your local cluster instead of {{< key product_name >}}.
> For more details, see [Running in a local cluster](./running-in-a-local-cluster.md).

{{< /markdown >}}
{{< /variant >}}

## Running a script in local Python with `{{< key cli >}} run`

During the development cycle you will want to run a specific workflow or task in your local Python environment to test it.
To quickly try out the code locally use `{{< key cli >}} run`:

```shell
$ {{< key cli >}} run workflows/example.py wf --name 'Albert'
```

Here you are invoking `{{< key cli >}} run` and passing the name of the Python file and the name of the workflow within that file that you want to run.
In addition, you are passing the named parameter `name` and its value.

This command is useful for quickly testing a workflow locally to check for basic errors.
For more details see [{{< key cli >}} run details](./details-of-union-run.md).

## Running a script on {{< key product_name >}} with `{{< key cli >}} run --remote`

To quickly run a workflow on {{< key product_name >}}, use `{{< key cli >}} run --remote`:

```shell
$ {{< key cli >}} run --remote --project basic-example --domain development workflows/example.py wf --name 'Albert'
```

Here we are invoking `{{< key cli >}} run --remote` and passing:
* The project, `basic-example`
* The domain, `development`
* The Python file, `workflows/example.py`
* The workflow within that file that you want to run, `wf`
* The named parameter `name`, and its value

This command will:
* Build the container image defined in your `ImageSpec`.

{{< variant flyte >}}
{{< markdown >}}

* Push the image to the container registry specified in that `ImageSpec`. Don't forget make the image accessible to {{< key product_name >}}. For example, if you are using GitHub Container Registry, you will need to make the image public.

{{< /markdown >}}
{{< /variant >}}

* Package up your code and deploy it to the specified project and domain in {{< key product_name >}}.
* Run the workflow on {{< key product_name >}}.

This command is useful for quickly deploying and running a specific workflow on {{< key product_name >}}.
For more details see [{{< key cli >}} run details](./details-of-union-run.md).

## Deploying your code to {{< key product_name >}} with `{{< key cli >}} register`

```shell
$ {{< key cli >}} register workflows --project basic-example --domain development
```

Here we are registering all the code in the `workflows` directory to the project `basic-example` in the domain `development`.

This command will:
* Build the container image defined in your `ImageSpec`.
* Package up your code and deploy it to the specified project and domain in {{< key product_name >}}.
  The package will contain the code in the Python package located in the `workflows` directory.
  Note that the presence of the `__init__.py` file in this directory is necessary in order to make it a Python package.

The command will not run the workflow. You can run it from the Web interface.

This command is useful for deploying your full set of workflows to {{< key product_name >}} for testing.

{{< variant byoc byok serverless >}}

## Deploying your code to production with `{{< key cli >}} package` and `uctl register`

The combination of `{{< key cli >}} package` and `uctl register` is the standard way of deploying your code to production.
This method is often used in scripts to [build and deploy workflows in a CI/CD pipeline](./ci-cd-deployment.md).

First, package your workflows:

```shell
$ {{< key cli >}} --pkgs workflows package
```

This will create a tar file called `flyte-package.tgz` of the Python package located in the `workflows` directory.
Note that the presence of the `__init__.py` file in this directory is necessary in order to make it a Python package.

Once the code is packaged you register it using the `uctl` CLI:

```shell
$ uctl register files --project basic-example --domain development \
       --archive flyte-package.tgz --version 1.0
```

See [Uctl CLI](../../api-reference/uctl-cli/_index.md) for more details.
{{< /variant >}}

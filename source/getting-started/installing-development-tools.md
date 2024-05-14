# Installing development tools

## Gather your credentials

After your administrator has onboarded you to **Union.ai**, you should have the following at hand:

* Your **Union.ai** credentials.
* The credentials to access the AWS or GCP account hosting your **Union.ai** instance.
* The URL of your Union instance. We will refer to this as `<union-host-url>` below.

## Install Python and Docker

Next, make sure that you have the following installed on your local machine:

* [Python](https://www.python.org/):
Versions 3.8.x - 3.11.x are supported.
Version 3.11.x is used in this guide and is recommended.
* [Conda](https://docs.conda.io/projects/conda/en/stable/):
In this guide, we use the `conda` tool (installed via [Miniconda](https://docs.conda.io/en/latest/miniconda.html)) to manage Python versions and virtual environments.
You can also use other tools such as [`pyenv`](https://github.com/pyenv/pyenv) and [`venv`](https://docs.python.org/3/library/venv.html).
Using some type of Python virtual environment manager is highly recommended.
* [Docker](https://docs.docker.com/get-docker/):
Any [OCI-compatible](https://opencontainers.org/) container engine like [Podman](https://podman.io/), [LXD](https://linuxcontainers.org/lxd/introduction/), or [Containerd](https://containerd.io/) should also work.
Ensure that the associated client daemon is running.

## Install the Union.ai CLI `uctl`

::::{tab-set}

:::{tab-item} macOS
To use [Homebrew](https://brew.sh/), do this:

```{code-block} shell
$ brew tap unionai/homebrew-tap
$ brew install uctl
```

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and do this:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::

:::{tab-item} Linux
To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and do this:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::

:::{tab-item} Windows
To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and do this:

```{code-block} shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

To download manually, see the [UCTL releases](https://github.com/unionai/uctl/releases).
:::
::::

:::{note}
`uctl`is an enhanced version of `flytectl`, [the Flyte command-line tool](https://docs.flyte.org/en/latest/flytectl/docs_index.html).
It adds Union-specific functionality, letting you manage not only Flyte entities (projects, domains, workflows, tasks, and launch plans) but also Union-specific entities like users, roles, and Union configurations.
:::

## Set up an image registry

When you deploy a workflow to Union (or to a local demo cluster), each task in the workflow runs inside a container.
Part of the workflow definition is the specification of the container image that each task will run in (this is done using the `ImageSpec` object in the Python code, as we will see later).
When you deploy (we say "register") your workflow to Union, the container images defined in your code are built on your local machine and pushed to a container registry, from which they are later pulled by Union when the workflow is executed.
For this reason, you will need access to an image registry.

In this example, we assume you will be using the GitHub Container Registry (GHCR) that comes as part of your GitHub account.
For more information, see [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

:::{admonition} Specifying your registry in the `ImageSpec`
Later in the process, you will need to specify the name of your registry (in this case, the name of your GitHub organization) in the `ImageSpec` object in your Python code.
We will call out the need to do this at that time.
:::

## Authenticate to the registry

You will need to set up your local Docker client to authenticate with GHCR in order for `pyflyte` to be able to push the image built according to the `ImageSpec` to GHCR.

Follow the directions in [Working with the Container registry > Authenticating to the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry.md#authenticating-to-the-container-registry).

:::{admonition} Making your image publicly accessible
In addition to making sure your registry is accessible from your local machine, you will need to ensure that the specific image, once pushed to the registry, is itself publicly accessible.

However, this step can ony be done once the image *has been* pushed, which comes later in the process.
We will call out the need to make the image publicly accessible at that time.
:::

## Set up a Python virtual environment

Create a Python virtual environment for our `wine-classification` example and switch to it:

```{code-block} shell
[~]:base
$ conda create -n wine-classification python=3.11 -y

[~]:base
$ conda activate wine-classification

[~]:wine-classification
$
```

:::{note}

We use [`conda`](https://docs.conda.io/en/latest/miniconda.html) to manage the Python version and virtual environments.
You are free to use other tools such as [`pyenv`](https://github.com/pyenv) and [`venv`](https://docs.python.org/3/library/venv.html).

:::

## Install the Flytekit SDK used by Union.ai

Finally, install [`flytekit`](https://pypi.org/project/flytekit/), the Flyte Python SDK, within the virtual environment that you just set up:

```{code-block} shell
[~]:wine-classification
$ pip install -U flytekit
```

This installs both the `flytekit` library and the `pyflyte` command-line tool.

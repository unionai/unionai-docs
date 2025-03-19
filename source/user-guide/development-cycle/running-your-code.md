# Running your code

## Set up your development environment

If you have not already done so, follow the [Getting started](../getting-started/index.md) section to sign in to Union.ai, and set up your local environment.

## CLI commands for running your code

The `union` CLI provides a set of commands that allow you to deploy and run your code at different stages of the development cycle:

{@# TODO: Link to the union commands below to the union CLI reference section #@}

1. `union run`: For deploying and running a single script immediately in your local Python environment.
2. `union run --remote`: For deploying and running a single script immediately in the cloud on Union.ai.
3. `union register`: For deploying multiple scripts to Union.ai and running them from the Web interface.
{@@ if byoc @@}
4. `union package` and `uctl register`: For deploying workflows to production and for scripting within a CI/CD pipeline.

```{note}
In some cases, you may want to test your code in a local cluster before deploying it to Union.ai.
This step corresponds to using the commands 2, 3, or 4, but targeting your local cluster instead of Union.ai.
For more details, see [Running in a local cluster](./running-in-a-local-cluster.md).
```
{@@ endif @@}

## Running a script in local Python with `union run`

During the development cycle you will want to run a specific workflow or task in your local Python environment to test it.
To quickly try out the code locally use `union run`:

```{code-block} shell
$ union run workflows/example.py wf --name 'Albert'
```

Here you are invoking `union run` and passing the name of the Python file and the name of the workflow within that file that you want to run.
In addition, you are passing the named parameter `name` and its value.

This command is useful for quickly testing a workflow locally to check for basic errors.
For more details see [union run details](./details-of-union-run.md).

## Running a script on Union.ai with `union run --remote`

To quickly run a workflow on Union.ai, use `union run --remote`:

```{code-block} shell
$ union run --remote --project basic-example --domain development workflows/example.py wf --name 'Albert'
```

Here we are invoking `union run --remote` and passing:
* The project, `basic-example`
* The domain, `development`
* The Python file, `workflows/example.py`
* The workflow within that file that you want to run, `wf`
* The named parameter `name`, and its value

This command will:
* Build the container image defined in your `ImageSpec`.
{@@ if byoc @@}
* Push the image to the container registry specified in that `ImageSpec`.
  * (Don't forget make the image accessible to Union.ai. For example, if you are using GitHub Container Registry, you will need to make the image public.)
{@@ endif @@}
* Package up your code and deploy it to the specified project and domain in Union.ai.
* Run the workflow on Union.ai.

This command is useful for quickly deploying and running a specific workflow on Union.ai.
For more details see [union run details](./details-of-union-run.md).

## Deploying your code to Union.ai with `union register`

```{code-block} shell
$ union register workflows --project basic-example --domain development
```

Here we are registering all the code in the `workflows` directory to the project `basic-example` in the domain `development`.

This command will:
* Build the container image defined in your `ImageSpec`.
* Package up your code and deploy it to the specified project and domain in Union.ai.
  The package will contain the code in the Python package located in the `workflows` directory.
  Note that the presence of the `__init__.py` file in this directory is necessary in order to make it a Python package.

The command will not run the workflow. You can run it from the Web interface.

This command is useful for deploying your full set of workflows to Union.ai for testing.

{@@ if byoc @@}

## Deploying your code to production with `union package` and `uctl register`

The combination of `union package` and `uctl register` is the standard way of deploying your code to production.
This method is often used in scripts to [build and deploy workflows in a CI/CD pipeline](./ci-cd-deployment.md).

First, package your workflows:

```{code-block} shell
$ union --pkgs workflows package
```

This will create a tar file called `flyte-package.tgz` of the Python package located in the `workflows` directory.
Note that the presence of the `__init__.py` file in this directory is necessary in order to make it a Python package.

Once the code is packaged you register it using the `uctl` CLI:

```{code-block} shell
$ uctl register files --project basic-example --domain development \
       --archive flyte-package.tgz --version 1.0
```
See [Uctl CLI](../../api-reference/uctl-cli/index.md) for more details.
{@@ endif @@}

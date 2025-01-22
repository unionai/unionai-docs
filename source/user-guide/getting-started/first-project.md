# First project

In this section we will set up a Union project. A Union project consists of

* A local directory (typically the checkout a Git repository, or a subdirectory of a Git repository) holding your workflow code.

* A project registered on Union to which you deploy this workflow code.

You deploy your code from your local project to the corresponding Union project by "registering" your workflows and tasks
using the `union` CLI.

Union provides a default project (called **{@= default_project =@}**) where all your workflows will be registered unless you specify otherwise.
We will use this default project for the rest of this guide.
To create additional projects, see [Setting up a project](../development-cycle/setting-up-a-project.md).

:::{admonition} Initialize a project from scratch
In this example we will start with an existing Git repository.
Alternatively, you can initialize a fresh project from a template with the `union init` command, which you then check into Git.
See [Setting up a project](../development-cycle/setting-up-a-project.md) for more details.
:::


## Clone the example project

We will use the **Getting started: Machine learning example**, found in the [`https://github.com/unionai/unionai-examples/`](unionai/unionai-examples/) GitHub repository under `user-guide/getting-started`.

Clone the repository to your local machine and `cd` to the project directory:

```{code-block} shell
$ git clone https://github.com/unionai/unionai-examples/
$ cd unionai-examples/user-guide/getting-started
```

Once you have cloned the repository, ensure that your Python virtual environment is properly set up with the required dependencies.

Using `uv`, you can install the dependencies with the command:

```{code-block} shell
$ uv sync
```

You can then activate the virtual environment with:

```{code-block} shell
source .venv/bin/activate
```

:::{admonition} `activate` vs `uv run`
When running the `union` CLI within your local project you must run it in the virtual environment _associated with_ that project.
This differs from our earlier usage of the tool when [we installed `union` globally](./local-setup.md#install-union-cli) in order to [set up its configuration](./local-setup.md#configure-the-union-cli).

To run union within your project's virtual environment using `uv`, you can prefix it use the `uv run` command. For example:

`uv run union ...`

Alternatively, you can activate the virtual environment with `source .venv/bin/activate` and then run the `union` command directly.

In our examples docs we assume that you are doing the latter.
:::


## Take a look at the code

This example illustrates training a simple model using `union`, `scikit-learn`, and `pandas`.

The model training workflow has three steps:

* Getting the `penguins` dataset from `openml.org`.
* Training a `HistGradientBoostingClassifier` model using `scikit-learn`.
* Evaluating the model by creating a confusion matrix, displayed as a `union.Deck`.


## Run the code locally

Because tasks and workflows are defined as regular Python functions, they can be executed in your local Python environment.

You can run the workflow locally with the command [`union run <FILE> <WORKFLOW>`](../../api-reference/union-cli.md#union-cli-commands):

```{code-block} shell
$ union run src/ml_workflow.py main
```

If the code runs successfully, you should see output like this:

```{code-block} shell
Running Execution on local.
0.9767441860465116
```
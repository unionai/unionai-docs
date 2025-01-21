# First project

In this section we will set up a Union project.

A Union project consists of:

* A local directory (usually the checkout a Git repository, or a subdirectory of a Git repository) holding your workflow code.
    * In this section we will use an existing project from our example repository. See below.

* A project registered on Union to which you deploy this workflow code.
    * We will show you how to create a project on Union, below

:::{admonition} Initialize a project from scratch
But you can initialize a fresh project from a template with the `union init` command, which you then check into Git.
See [Setting up a project](../development-cycle/setting-up-a-project.md) for more details.
_In this example we will start with an existing Git repository_
:::

## Get the example project

We will use the **Getting started: Machine learning example**, found in the [`https://github.com/unionai/unionai-examples/`](unionai/unionai-examples/) GitHub repository under `user-guide/getting-started`.

Clone the repository to your local machine and `cd` to the project directory:

```{code-block} shell
$ git clone https://github.com/unionai/unionai-examples/
$ cd unionai-examples/user-guide/getting-started
```

## Take a look at the code

This example illustrates training a simple model using `union`, `scikit-learn`, and `pandas`.

The model training workflow has three steps:

* Getting the `penguins` dataset from `openml.org`.
* Training a `HistGradientBoostingClassifier` model using `scikit-learn`.
* Evaluating the model by creating a confusion matrix, displayed as a `union.Deck`.


## Running locally

Because tasks and workflows are defined as regular Python functions, they can be executed in your local Python environment.

You can run the workflow locally with the command [`union run <FILE> <WORKFLOW>`](../../api-reference/union-cli.md#union-cli-commands):

```{code-block} shell
$ union run src/ml_workflow.py main
```


[DONE TO HERE]()



## Running on Union

Local execution is useful for testing and debugging your workflows.
But to run them at scale, you will need to deploy them (or as we say, "register" them) on to your Union instance.

When task and workflow code is registered on Union:

* The `@union.task` function is loaded into a container defined by the `image_spec` object specified in the `container_image` parameter of the decorator.
* The `@union.workflow` function is compiled into a directed acyclic graph that controls the running of the tasks invoked within it.

{@@ if serverless @@}

On Union Serverless, the system automatically handles building and registering the container images used by your tasks.
No local setup is required.

Go to [Running on Union](./running-on-union.md) for next steps.

{@@ elif byoc @@}

On Union BYOC, you will need to set up the tools and access to build and push the container images used by your tasks.

Go to [Container images](./container-images.md) for next steps.

{@@ endif @@}
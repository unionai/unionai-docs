# Getting started

This section gives you a quick introduction to writing and running Union workflows.

{@@ if serverless @@}

## Sign up for Union Serverless

First, sign up for Union Serverless:

:::{button-link} https://signup.union.ai/
:color: secondary

Create an account
:::

Once you've received confirmation that your sign-up succeeded, navigate to
the UI at [serverless.union.ai](https://serverless.union.ai).

To get started, try selecting the default project, called `{@= default_project =@}`, from the list of projects.
This will take you to `{@= default_project =@}` project dashboard:

![Union UI](/_static/images/quick-start/serverless-dashboard.png)

## Run your first workflow

Run your first workflow on a Union Workspace.

:::{dropdown} {octicon}`play` Start workspace
:open:
:animate: fade-in
:color: light

Select **Workspaces** in the left navigation bar.

Start the default workspace by clicking on the `default` workspace item.

![Start workspace](/_static/gifs/start-workspace.gif)
:::

:::{dropdown} {octicon}`book` Open workspace
:animate: fade-in
:color: light

When the `Status` is `Active` on the `default` workspace, you can click on it
again to open the workspace.

*It will take a few moments to load the VSCode interface.*

![Open workspace](/_static/gifs/open-workspace.gif)
:::

:::{dropdown} {octicon}`check-circle-fill` Complete walkthrough
:animate: fade-in
:color: light

Once the workspace is open, you should see a VSCode interface in your browser.

![Workspace VSCode](/_static/images/quick-start/serverless-workspace-vscode.png)

In the walkthrough, you'll learn how to:

1. 🤖 Train a model
2. 🔀 Parallelize model training
3. 📘 Iterate on a Jupyter Notebook
:::

:::{dropdown} {octicon}`stop` Stop workspace
:animate: fade-in
:color: light

The workspace will terminate after 20 minutes of idle time, but you can also
stop it manually on the Workspaces page.

![Open workspace](/_static/gifs/stop-workspace.gif)
:::


## Next steps

🎉 Congratulations! You've just run your first workflow on Union.

{@@ elif byoc @@}

## Gather your credentials

After your administrator has onboarded you to Union (see [Deployment](../../deployment/index.md)), you should have the following at hand:

* Your Union credentials.
* The URL of your Union instance. We will refer to this as `<union-host-url>` below.

## Log into Union

Navigate to the UI at `<union-host-url>` and log in with your credentials.
Once you have logged in you should see the Union UI.

To get started, try selecting the default project, called `{@= default_project =@}`, from the list of projects.
This will take you to `{@= default_project =@}` project dashboard:

![Union UI](/_static/images/quick-start/byoc-dashboard.png)

{@@ endif @@}

Continue to [First project](./first-project.md).






## Your project on Union

Union provides a default project (called **{@= default_project =@}**) where all your workflows will be registered unless you specify otherwise. We will use this default project for the rest of this guide.

To create additional projects, see [Setting up a project](../development-cycle/setting-up-a-project.md).

## Our example workflow

In this section, we will use a workflow from Union's [`unionai/unionai-examples`](https://github.com/unionai/unionai-examples) GitHub repository that illustrates training a simple model using `flytekit`, `scikit-learn`, and `pandas`.

The model training workflow has three steps:
- Getting the `penguins` dataset from [openml.org](https://www.openml.org/search?type=data&sort=runs&id=42585&status=active)
- Training a `HistGradientBoostingClassifier` model using `scikit-learn`.
- Evaluating the model by creating a confusion matrix, displayed as a Flyte `Deck`.

## Next step

The next step is [Setting up your local environment](./setting-up-your-local-environment.md).







## Create a "Hello, world!" workflow

To create an example workflow file, copy the following into a file called `hello.py`:

```{code-block} python
from flytekit import task, workflow

@task
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@workflow
def hello_world_wf(name: str = 'world') -> str:
    res = say_hello(name=name)
    return res
```

## Tasks and workflows

The "Hello, world!" code contains a task and a workflow, which are Python functions decorated with the `@task` and `@workflow` decorators, respectively.
For more information, see the [tasks](./user-guide/core-concepts/tasks/index.md) and [workflows](./user-guide/core-concepts/workflows/index.md) documentation.

## Run the workflow locally in Python

You can run the workflow in your local Python environment with the [`union run` command](./api-reference/union-cli.md#union-cli-commands):

```{code-block} shell
$ union run hello.py hello_world_wf
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, world!
```

Since the `@workflow` function takes an argument called `name`, you can also pass that in
as a command-line argument like this:

```{code-block} shell
$ union run hello.py hello_world_wf --name Ada
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, Ada!
```

## Run the workflow remotely on Union

To run the workflow remotely on Union, add the [`--remote` flag](./api-reference/union-cli.md#union-cli-commands):

```{code-block} shell
$ union run --remote hello.py hello_world_wf --name "Ada"
```

The output displays a URL that links to the workflow execution in the UI:

{@@ if serverless @@}

```{code-block} shell
[✔] Go to https://serverless.union.ai/org/... to see execution in the UI.
```

{@@ elif byoc @@}

```{code-block} shell
[✔] Go to https://<union-host-url>/org/... to see execution in the UI.
```

{@@ endif @@}

Click the link to see the execution in the UI.



















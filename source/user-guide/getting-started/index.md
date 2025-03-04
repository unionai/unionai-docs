# Getting started

This section gives you a quick introduction to writing and running {@= union_flyte_upper =@} workflows.

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

🎉 Congratulations! You've just run your first workflow on Union.

{@@ elif byoc or byok @@}

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

This dashboard gives you an overview of the workflows and tasks in your project.
Since you are just starting out, it will be empty.
To build and deploy your first workflow, the first step is to [set up your local environment](./local-setup.md).

{@@ elif flyte @@}

:::{admonition} Try Flyte in your browser
You can try Flyte in your browser without any setup simply by [signing up for
**Union Serverless**](https://signup.union.ai/).

[Union Serverless is a fully-hosted version of Flyte](https://docs.union.ai/serverless) with additional features.
:::

## Try Flyte on your local machine

You can also install Flyte's SDK (called `flytekit`) and a local Flyte cluster to run workflows on your local machine.

To get started, follow the instructions on the next page, [Local setup](./local-setup.md).

{@@ endif @@}

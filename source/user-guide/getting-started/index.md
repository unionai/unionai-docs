# Getting started

This section gives you a quick introduction to writing and running Union.ai workflows.

{@@ if serverless @@}

## Sign up for Union.ai Serverless

First, sign up for Union.ai Serverless:

:::{button-link} https://signup.union.ai/
:color: secondary

Create an account
:::

Once you've received confirmation that your sign-up succeeded, navigate to
the UI at [serverless.union.ai](https://serverless.union.ai).

To get started, try selecting the default project, called `{@= default_project =@}`, from the list of projects.
This will take you to `{@= default_project =@}` project dashboard:

![Union.ai UI](/_static/images/quick-start/serverless-dashboard.png)

## Run your first workflow

Run your first workflow on a Union.ai Workspace.

:::{dropdown} {octicon}`play` Start workspace
:open:
:animate: fade-in
:color: light

Select **Workspaces** in the left navigation bar.

Start the default workspace by clicking on the `default` workspace item.

![Start workspace](/_static/images/quick-start/serverless-workspace-start.png)
:::

:::{dropdown} {octicon}`book` Open workspace
:animate: fade-in
:color: light

When the `Status` is `Active` on the `default` workspace, you can click on it
again to open the workspace.

*It will take a few moments to load the VSCode interface.*

![Open workspace](/_static/images/quick-start/serverless-workspace-open.png)
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

![Stop workspace](/_static/images/quick-start/serverless-workspace-stop.png)
:::

🎉 Congratulations! You've just run your first workflow on Union.ai.

{@@ elif byoc @@}

## Gather your credentials

After your administrator has onboarded you to Union.ai (see [Deployment](../../deployment/index.md)), you should have the following at hand:

* Your Union.ai credentials.
* The URL of your Union.ai instance. We will refer to this as `<union-host-url>` below.

## Log into Union.ai

Navigate to the UI at `<union-host-url>` and log in with your credentials.
Once you have logged in you should see the Union.ai UI.

To get started, try selecting the default project, called `{@= default_project =@}`, from the list of projects.
This will take you to `{@= default_project =@}` project dashboard:

![Union.ai UI](/_static/images/quick-start/byoc-dashboard.png)

This dashboard gives you an overview of the workflows and tasks in your project.
Since you are just starting out, it will be empty.
To build and deploy your first workflow, the first step is to [set up your local environment](./local-setup.md).

{@@ endif @@}

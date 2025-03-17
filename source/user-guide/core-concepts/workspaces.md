# Workspaces

Workspaces provide a convenient VSCode development environment for iterating on
your Union.ai tasks, workflows, and apps.

With workspaces, you can:

- 🧑‍💻 Develop and debug your tasks, workflows, or code in general
- ▶️ Run your tasks and workflows in a way that matches your production environment
- 🚀 Deploy your workflows and apps to development, staging, or production environments
- 🗂️ Persist files across workspace restarts to save your work
- 🔑 Specify secrets and resources for your workspace
- 🐳 Specify custom container images
- 💻 Specify custom `on_startup` commands
- ⏱️ Adjust the idle time-to-live (TTL) for your workspace to avoid unneeded expenses
- 🔑 Authenticate with GitHub to clone private repositories

## Creating a workspace

To create a workspace, click on the `Workspace` tab on left navbar and click
on the `New Workspace` button on the top right.

![Create Workspace](/_static/images/user-guide/core-concepts/workspaces/create-new-workspace-1.png)

Provide a name for your workspace, set an **Idle TTL** (time to live), and
click `Create`.

![Create Workspace](/_static/images/user-guide/core-concepts/workspaces/create-new-workspace-2.png)

```{note}
The Idle TTL is the amount of time a workspace will be idle before it is
automatically stopped. Workspaces have a global TTL of 1 day, but you can set
the idle TTL field to a shorter duration to stop the workspace sooner.
```

You should see a new workspace created in the Workspaces view:

![Create Workspace](/_static/images/user-guide/core-concepts/workspaces/create-new-workspace-3.png)


## Running a workspace

To run a workspace, click on the switch on the workspace item:

![Run Workspace](/_static/images/user-guide/core-concepts/workspaces/run-workspace-1.png)

Once the workspace has started, you can click on the `Open in VSCode` button:

![Run Workspace](/_static/images/user-guide/core-concepts/workspaces/run-workspace-2.png)

Once the startup commands have completed, you'll see a browser-based VSCode IDE:

![Run Workspace](/_static/images/user-guide/core-concepts/workspaces/run-workspace-3.png)

To stop a workspace, click on the toggle switch on the workspace item.

## Filesystem Persistence

Any changes to the filesystem that you make in the working directory of your
workspace (the directory you find yourself in when you first open the workspace)
are persisted across workspace restarts.

This allows you to save data, code, models, and other files in your workspace.

```{note}
Storing large datasets, models, and other files in your workspace may slow down
the start and stop times of your workspace. This is because the workspace
instance needs time to download/upload the files from persistent storage.
```

## Editing a workspace

Change the workspace configuration by clicking on the `Edit` button:

![Edit Workspace](/_static/images/user-guide/core-concepts/workspaces/edit-workspace-1.png)

Note that you can change everything except the workspace name.

![Edit Workspace](/_static/images/user-guide/core-concepts/workspaces/edit-workspace-2.png)


## The workspace detail view

Clicking on the workspace item on the list view will reveal the workspace detail view,
which provides all the information about the workspace.

![Workspace Detail](/_static/images/user-guide/core-concepts/workspaces/workspace-detail.png)


## Archiving a workspace

Archive a workspace by clicking on the `Archive` button:

![Archive Workspace](/_static/images/user-guide/core-concepts/workspaces/archive-workspace.png)

Show archived workspaces by clicking on the `Show archived` toggle
on the top right of the workspaces list view. Unarchive a workspace by clicking
on the `Unarchive` button:

![Unarchive Workspace](/_static/images/user-guide/core-concepts/workspaces/unarchive-workspace.png)


## Setting secrets

If you don't have any secrets yet, create them with the `union create secret`
command:

```{code-block} shell
union create secret --project my_project --domain my_domain --name my_secret
```

You'll be prompted to enter a secret value in the terminal:

```
Enter secret value: ...
```

```{note}
You can learn more about secrets management [here](../../development-cycle/managing-secrets.md).
```

Set secrets for your workspace by clicking on the `Secrets` tab in the sidebar.
Provide the `my_secret` key and optionally, the environment variable you want
to assign it to in the workspace.

![Secrets](/_static/images/user-guide/core-concepts/workspaces/setting-secrets.png)


## Setting resources

You can also set the resources for your workspace:

![Resources](/_static/images/user-guide/core-concepts/workspaces/setting-resources.png)

{@@ if serverless @@}

These resources must be compatible with the resource limits available to you
on your Union.ai serverless account. Go the the top-level dashboard to view your
execution settings:

![Execution Settings](/_static/images/user-guide/core-concepts/workspaces/serverless-execution-settings.png)

For the `GPU` field, you can choose from the [available accelerators](../tasks/task-hardware-environment/accelerators.md).

{@@ elif  byoc @@}

These resources must be compatible with the resources available to your BYOC
cluster. Find the details of your BYOC cluster in the top-level dashboard:

![BYOC Compute Resources](/_static/images/user-guide/core-concepts/workspaces/byoc-compute-resources.png)

You can choose [the GPU accelerator](../tasks/task-hardware-environment/accelerators.md) that corresponds to your available instance types.

{@@ endif @@}


## Specifying custom `on_startup` commands

If you need to run any commands like install additional dependencies or `wget`
a file from the web, specify custom `on_startup` commands:

![On Startup](/_static/images/user-guide/core-concepts/workspaces/customize-onstartup.png)

## Specifying custom container images

By default, the workspace will use a Union.ai-provided container image which contains
the following Python libraries:

- `union`
- `flytekit`
- `uv`
- `ipykernel`
- `pandas`
- `pyarrow`
- `scikit-learn`
- `matplotlib`

You can specify a pre-built custom container image by clicking on the `Container`
tab in the sidebar and provide the image name in the workspace creation form.

![Custom Container](/_static/images/user-guide/core-concepts/workspaces/customize-container-image.png)

In many cases, you may want to use the same container image as a task execution
that you want to debug. You can find the container image URI by going to the
task execution details page:

![Task Execution](/_static/images/user-guide/core-concepts/workspaces/customize-container-image-get-uri.png)

{@@ if byoc @@}

You can specify:
- Any public container image URI
- Images built with the Union.ai [image builder service](../development-cycle/image-spec.md)
- Images available in your private container registry (e.g. [AWS ECR](../integrations/enabling-aws-resources/enabling-aws-ecr.md), [GCP Artifact Registry](../integrations/enabling-gcp-resources/enabling-google-artifact-registry.md), or [Azure Container Registry](../integrations/enabling-azure-resources/enabling-azure-container-registry.md))

{@@ endif @@}


## Authenticating with GitHub

If you want to clone a private GitHub repository into your workspace, you can
using the pre-installed `gh` CLI to authenticate your workspace session:

```{code-block} shell
gh auth login
```

You'll be prompted to enter either a GitHub personal access token (PAT) or
authenticate via the browser.

```{note}
You can create and set a `GITHUB_TOKEN` secret to set the access token for your
workspace, but you'll need to authenticate via `gh auth login` in every new
workspace session:

- Create a secret with the `union create secret` command
- Create a workspace or update an existing one with the `GITHUB_TOKEN` secret,
  setting the environment variable to e.g. `GITHUB_TOKEN`
- In the workspace session, run `gh auth login` to authenticate with GitHub and
  use the `$GITHUB_TOKEN` environment variable as the personal access token.
```

## Sorting and filtering workspaces

You can filter workspaces to only the active ones by clicking on the `Active`
toggle on the top left of the workspaces list view.

![Active Workspaces](/_static/images/user-guide/core-concepts/workspaces/active-workspaces.png)

Sort by recently updated by clicking on the `Recently updated` toggle on the
top right of the workspaces list view, and you can also sort by recently
updated by clicking on the `Recently updated` toggle on the top right of the
workspaces list view.

![Filtering and Sorting Workspaces](/_static/images/user-guide/core-concepts/workspaces/filtering-sorting-workspaces.png)

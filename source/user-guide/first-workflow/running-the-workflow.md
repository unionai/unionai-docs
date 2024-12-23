# Running the workflow

## Log in to Union

To run workflows on Union using the `union` CLI, run the following command:

{@@ if serverless @@}

```{code-block} shell
$ union create login --serverless
```
This will create the `~/.union/config.yaml` with the configuration information to connect to Union Serverless.

{@@ elif byoc @@}

```{code-block} shell
$ union create login --host <union-host-url>
```

where `<union-host-url>` is the URL of your Union instance.

This will create the `~/.union/config.yaml` with the configuration information to connect to your Union instance.

{@@ endif @@}

## Run the workflow locally in Python

To quickly check your workflow code, you can run it in your local Python environment with the following command:

```{code-block} shell
$ union run user_guide/first_workflow/ml_workflow/ml_workflow.py main --max_bins 64
```

If the code runs successfully, you should see output like this:

```{code-block} shell
Running Execution on local.
0.9767441860465116
```

## Run the workflow remotely on Union

{@@ if serverless @@}

To run the workflow in the cloud on Union, add the `--remote` option:

```{code-block} shell
$ union run --remote user_guide/first_workflow/ml_workflow/ml_workflow.py main --max_bins 64
```

You should see the following output in your terminal:

```{code-block} shell
👍 Build submitted!
⏳ Waiting for build to finish at: https://serverless.union.ai/org/...
✅ Build completed in 0:01:57!

[✔] Go to https://serverless.union.ai/org/... to see execution in the UI.
```

When you invoke `union run --remote`, the system first launches a Union hosted image builder that creates the container images with the Python dependencies required for the tasks in your workflow.

Next, the workflow code is registered to Union (meaning that it is serialized uploaded to Union),
the images defined in `ImageSpec` blocks are used to initialize the containers for each task, and the workflow is executed.

The first URL in the output above points to the image builder and the second URL points to the workflow execution.

{@@ elif byoc @@}

To run the workflow on Union, you will need to register the workflow, make your container image accessible to Union, and finally, run the workflow from the Union interface.

### Register the workflow on Union

When starting with a new workflow that requires a new container image that has not been previously built, you must first register your workflow code with `union register`. To register the `ml_workflow` example, run the following command:

```{code-block} shell
$ union register guide/first_workflow/ml_workflow
```

This command does the following:

* Builds the images defined by the `ImageSpec` objects in your code and pushes them to the specified container registry.
* Pushes the workflow code to Union.
* Sets up the workflow DAG and its constituent task containers.
* Registers the workflow in the default domain (`development`) of the default project (`flytesnacks`) in Union.

You should see the following output (or similar) in your terminal:

```{code-block} shell
Successfully serialized 5 flyte objects
[✔] Registration ml_workflow.ml_workflow.evaluate_model type TASK successful with version nuHakW_PUV5uk71n-to7bg
[✔] Registration ml_workflow.ml_workflow.train_model type TASK successful with version nuHakW_PUV5uk71n-to7bg
[✔] Registration ml_workflow.ml_workflow.get_dataset type TASK successful with version nuHakW_PUV5uk71n-to7bg
[✔] Registration ml_workflow.ml_workflow.main type WORKFLOW successful with version nuHakW_PUV5uk71n-to7bg
[✔] Registration ml_workflow.ml_workflow.main type LAUNCH_PLAN successful with version nuHakW_PUV5uk71n-to7bg
Successfully registered 5 entities
```

### Make your image accessible to Union

Before you can run the workflow from the Union interface, you must make sure that the image defined in your `ImageSpec` is public.

In the GitHub Container Registry, switch the visibility of your container image to Public. For more information, see [Configuring a package's access control and visibility](https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility.md#about-inheritance-of-access-permissions-and-visibility).

At this point, you can run the workflow from the Union interface.

### Run the workflow from the Union interface

To run the workflow from the Union interface:

1. Navigate to the Union dashboard.
2. In the left sidebar, click **Workflows**.
3. Search for your workflow, then select the workflow from the search results.
4. On the workflow page, click **Launch Workflow**.
5. In the "Create New Execution" dialog, you can change the workflow version, Launch Plan, and inputs (if present). Click "Advanced options" to change the security context, labels, annotations, max parallelism, override the interruptible flag, and overwrite cached inputs.
6. To execute the workflow, click **Launch**. You should see the workflow status change to "Running", then "Succeeded" as the execution progresses.

To view the workflow execution graph, click the **Graph** tab above the running workflow.

{@@ endif @@}

## View the workflow execution on Union

When you view the workflow execution graph, you will see the following:

![Graph](/_static/images/user-guide/first-workflow/running-the-workflow/graph.png)

Above the graph, there is metadata that describes the workflow execution, such as the
duration and the workflow version. Next, click on the `evaluate_model` node to open up a
sidebar that contains additional information about the task:

![Sidebar](/_static/images//user-guide/first-workflow/running-the-workflow/sidebar.png)

Click on the "Flyte Deck" button in the sidebar to open up visualizations generated
by the task:

![Flyte Deck](/_static/images//user-guide/first-workflow/running-the-workflow/flyte-deck.png)

Now that we are familiar with the UI, let's jump into the code and see how to build the
workflow!

## Next step

The next step is to take a look at the [Example code components](example-code-components).

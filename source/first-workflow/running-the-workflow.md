# Running the workflow

## Run the workflow locally in Python

To quickly check your workflow code, you can run it in your local Python environment with the following command:

```{code-block} shell
$ unionai run guides/01_getting_started/ml_workflow/ml_workflow.py main --max_bins 64
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
$ unionai run --remote guides/01_getting_started/ml_workflow/ml_workflow.py main --max_bins 64
```

You should see the following output in your terminal:

```{code-block} shell
👍 Build submitted!
⏳ Waiting for build to finish at: https://serverless.union.ai/org/...
✅ Build completed in 0:01:57!

[✔] Go to https://serverless.union.ai/org/... to see execution in the UI.
```

When you invoke `unionai run --remote`, the system first launches a Union hosted image builder that creates the container images with the Python dependencies required for the tasks in your workflow.

Next, the workflow code is registered to Union (meaning that it is serialized uploaded to Union),
the images defined in `ImageSpec` blocks are used to initialize the containers for each task, and the workflow is executed.

The first URL in the output above points to the image builder and the second URL points to the workflow execution.

{@@ elif byoc @@}

To run the workflow on Union, you will need to register the workflow, make your container image accessible to Union, and finally, run the workflow from the Union interface.

### Register the workflow on Union

When starting with a new workflow that requires a new container image that has not been previously built, you must first register your workflow code with `unionai register`. To register the `ml_workflow` example, run the following command:

```{code-block} shell
$ unionai register guides/01_getting_started/ml_workflow
```

This command does the following:

* Builds the images defined by the `ImageSpec` objects in your code and pushes them to the specified container registry.
* Pushes the workflow code to Union.
* Sets up the workflow DAG and its constituent task containers.
* Registers the workflow in the default domain (`development`) of the default project (`flytesnacks`) in Union.

You should see the following output (or similar) in your terminal:

```{code-block} shell
Running pyflyte register from /Users/me/repos/unionai/unionai-examples with images ImageConfig(default_image=Image(name='default', fqn='cr.flyte.org/flyteorg/flytekit', tag='py3.11-1.12.2', digest=None), images=[Image(name='default', fqn='cr.flyte.org/flyteorg/flytekit', tag='py3.11-1.12.2', digest=None)]) and image destination folder /root on 1 package(s) ('/Users/me/repos/unionai/unionai-examples/guides/01_getting_started/ml_workflow',)
Registering against union.my-company.com
Detected Root /Users/me/repos/unionai/unionai-examples/guides/01_getting_started, using this to create deployable package...
No output path provided, using a temporary directory at /var/folders/vh/5cnb0p254xv44zpn2ntj_0ch0000gn/T/tmp4a9iqzqt instead
Computed version is nuHakW_PUV5uk71n-to7bg
Loading packages ['ml_workflow'] under source root /Users/me/repos/unionai/unionai-examples/guides/01_getting_started
Image flytekit:Jg0osJpciXDDf5amjsBDAw not found. building...
Run command: envd build --path /var/folders/vh/5cnb0p254xv44zpn2ntj_0ch0000gn/T/flyte3i9ry6kc/control_plane_metadata/local_flytekit/03f65b09b7ea32403f5e7673ebae1993  --platform linux/amd64 --tag flytekit:Jg0osJpciXDDf5amjsBDAw
#1 docker-image://cr.flyte.org/flyteorg/flytekit:py3.11-1.12.2
...
#9 DONE 9.0s

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

![Graph](/_static/images/getting-started-graph.jpg)

Above the graph, there is metadata that describes the workflow execution, such as the
duration and the workflow version. Next, click on the `evaluate_model` node to open up a
sidebar that contains additional information about the task:

![Sidebar](/_static/images/getting-started-full-sidebar.jpg)

The `Inputs` and `Outputs` tabs contains links to data coming into the task and the
task's output:

![Input-Output](/_static/images/getting-started-input-output.jpg)

Finally, click on the "Flyte Deck" button in the sidebar to open up visualizations generated
by the task:

![Flyte Deck](/_static/images/getting-started-flyte-deck.jpg)

Now that we are familiar with the UI, let's jump into the code and see how to build the
workflow!

## Next step

The next step is to take a look at the [Example code components](example-code-components).

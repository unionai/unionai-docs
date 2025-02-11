# Running your workflow

## Running locally the code locally

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

## Running remotely on Union

Local execution is useful for testing and debugging your workflows.
But to run them at scale, you will need to deploy them (or as we say, "register" them) on to your Union instance.

When task and workflow code is registered on Union:

* The `@union.task` function is loaded into a container defined by the `ImageSpec` object specified in the `container_image` parameter of the decorator.
* The `@union.workflow` function is compiled into a directed acyclic graph that controls the running of the tasks invoked within it.

## ImageSpec and image building

In this example the `ImageSpec` object is defined like this:

```{code-block} python
image = union.ImageSpec(
    builder = "union",
    name="ml-workflow-image",
    packages=[
        "scikit-learn==1.4.1.post1",
        "pandas==2.2.1",
        "matplotlib==3.8.3",
        "pyarrow==17.0.0",
        "union==0.1.132",
    ]
)
```

Specifying `builder = "union"` tells Union to build the image using its cloud image builder and register it in its own image registry,
from where it will be pulled when the task container is spun up.

Alternatively, if you do not specify `builder = "union"` the `union` CLI will use your local Docker to build the image on your local machine,
register it to the registry that you specify (using the `registry` parameter in the `ImageSpec`).
See [Container images](../development-cycle/container-images.md) for more information.

The main advantages offered by local building are:

* You can specify a custom base image to build from (whereas the cloud builder always uses the default `union` image).
* You can store your image in a private registry.

If these advantages are not important to you, we recommend using the cloud builder, as it is simpler and faster.


## Run the workflow on Union

To run the workflow on Union, add the [`--remote` option](../../api-reference/union-cli.md#union-cli-commands):

```{code-block} shell
$ union run --remote src/ml_workflow.py main
```

The output displays a URL that links to the workflow execution in the UI:

{@@ if serverless @@}

```{code-block} shell
👍 Build submitted!
⏳ Waiting for build to finish at: https://serverless.union.ai/org/...
✅ Build completed in 0:01:57!

[✔] Go to https://serverless.union.ai/org/... to see execution in the UI.
```

{@@ elif byoc @@}

```{code-block} shell
👍 Build submitted!
⏳ Waiting for build to finish at: https://<union-host-url>/org/...
✅ Build completed in 0:01:57!

[✔] Go to https://<union-host-url>/org/... to see execution in the UI.
```

{@@ endif @@}

Click the link to see the execution in the UI.

## Register the workflow without running

Above we used the `union run --remote` to register and immediately run a workflow on Union.

This is useful for quick testing, but for more complex workflows you may want to register the workflow first and then run it from the Union interface.

To do this, you can use the `union register` command to register the workflow code with Union.

The form of the command is:

```{code-block} shell
$ union register <path-to-src>
```

in our case, from within the `getting-started` directory, you would do:

```{code-block} shell
$ union register src
```

This registers all code in the `src` directory to Union but does not immediately run anything.
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


## Run the workflow from the Union interface

To run the workflow, you need to go to the Union interface:

1. Navigate to the Union dashboard.
2. In the left sidebar, click **Workflows**.
3. Search for your workflow, then select the workflow from the search results.
4. On the workflow page, click **Launch Workflow**.
5. In the "Create New Execution" dialog, you can change the workflow version, Launch Plan, and inputs (if present). Click "Advanced options" to change the security context, labels, annotations, max parallelism, override the interruptible flag, and overwrite cached inputs.
6. To execute the workflow, click **Launch**. You should see the workflow status change to "Running", then "Succeeded" as the execution progresses.

To view the workflow execution graph, click the **Graph** tab above the running workflow.


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

Now that we are familiar with the UI, let's jump into the code and see how the
workflow is constructed.

# Running the workflow

## Run the workflow locally in Python

Often it helps to do a quick check by first running your code in your local Python environment first.
You can do that with the following command:

```{code-block} shell
$ unionai run --remote guides/01_getting_started/ml_workflow/ml_workflow.py main --max_bins 64
```

If the code runs successfully, you should see output like this:

```{code-block} shell
Running Execution on local.
0.9767441860465116
```

## Run the workflow remotely on Union

To run workflow in the cloud on Union, just add the `--remote` options:

```{code-block} shell
$ unionai run --remote guides/01_getting_started/ml_workflow/ml_workflow.py main --max_bins 64
```

This will output the following to the console, where the first URL points to the image builder and
the second URL is the workflow execution:

{@# DONE TO HERE #@}

{@@ if serverless @@}

```{code-block} shell
👍 Build submitted!
⏳ Waiting for build to finish at: https://serverless.union.ai/org/...
✅ Build completed in 0:01:57!

[✔] Go to https://serverless.union.ai/org/... to see execution in the console.
```

When we run the workflow, it launches a Union hosted image builder that creates a image
with the Python dependencies required for the workflow.
Afterwards, the machine learning workflow executes with the image built from the previous step.

{@@ elif byoc @@}



{@@ endif @@}

Open the second link to view the execution in Union's user interface and click on the "Graph" tab
to see a visualization of the workflow:

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

## Diving into the code

You can find the full example code on [{fab}`github` Github](https://github.com/unionai/examples/blob/main/guides/01_getting_started/ml_workflow/ml_workflow.py)

### Defining a workflow

The overall [workflow](https://docs.union.ai/core-concepts/workflows/) is a collection
of tasks that manages the data flow between tasks. Our standard workflow is defined using
a `@workflow` decorator the wraps a Python function:


```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 100-103
```

The workflow's `max_bins` parameter is automatically added to the `unionai run` CLI allowing
us to run `--max_bins 64` to configure the parameter.

### Defining a task

Each task is defined with a Python function that is decorated with a `@task` decorator.
For example, the `train_model` task is defined as follows:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 55-64
```

We highlight some of features used to define the task:

1. Python typing is required for all inputs and outputs. Union uses the types for serialization
   and to validate workflows.
2. The `Resources(cpu="3", mem="2Gi")` is **declarative infrastructure** that allocates 3 CPUs
   and `2Gi` of memory for the task.
3. The `container_image=image` sets an image that has all the dependencies required by the task.

The task requires custom dependencies, which we specify with an `ImageSpec`:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 36-38
```

The `requirements.txt` contain the same dependencies we used to configure our local development environment. The Union hosted image builder builds the image based
on the `ImageSpec` specification and uses that image for the machine learning workflow.

The `get_dataset` task uses a cache of the data outputs of the task:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 41-52
```

`get_dataset` returns the training and test data as pandas DataFrames which gets cached by Union.
With caching, future executions of the workflow will use the cached data instead of running
the task again.

### Visualizations

The Flyte Deck feature enables us to show custom visualizations in Union's user interface.
The visualizations is enabled with a single `enable_deck=True`:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/guides/01_getting_started/ml_workflow/ml_workflow.py
:language: python
:lines: 67-96
```

Enabling the deck adds the "Flyte Deck" button in the UI and task's code places the
visualizations into the deck.

## Conclusion

You can learn more about Union-specific capabilities by exploring the
[Core Concepts](../core-concepts/index) section.
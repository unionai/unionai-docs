# Consuming artifacts

## Defining a workflow that consumes an artifact

You can define a workflow that consumes an artifact by defining a query and passing it as an input to the consuming workflow.

The following code defines a query, `data_query`, that searches across all versions of `BasicArtifact` that match the partition values. This query binds parameters to the workflow's `key1` and `time_partition` inputs and returns the most recent version of the artifact.

{@@ if byoc @@}
:::{note}
To use the example code on this page, you will need to add your `registry` to the `pandas_image` ImageSpec block.
:::
{@@ endif @@}

```{literalinclude} ../../../_static/includes/core-concepts/artifacts/query.py
:language: python
:emphasize-lines: 23-26,35
```

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/query.py
:caption: query.py
:language: python
:emphasize-lines: 23-26,35
```

You can also directly reference a particular artifact version in a query using the `get()` method:
```{code-block} python
data = BasicArtifact.get(<organization>/<domain>/BasicArtifact@<artifact-version>)
```

:::{note}
For a full list of Artifact class methods, see the [Flytekit Artifact documentation](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.Artifact.html).
:::

## Launching a workflow that consumes an artifact

To launch a workflow that consumes an artifact as one of its inputs, navigate to the workflow in the UI and click **Launch Workflow**:

![Launch workflow UI with artifact query](/_static/images/artifacts/launch_workflow_artifact_query.png)

In the `query_wf` example, the workflow takes three inputs: `key1`, `dt`, and a `BasicArtifact` artifact query. In order to create the workflow execution, you would enter values for `key1` and `dt` and click **Launch**. The artifacts service will supply the latest version of the `BasicData` artifact that meets the partition query criteria.

You can also override the artifact query from the launch form by clicking **Override**, directly supplying the input that the artifact references (in this case, a blob store URI), and clicking **Launch**:

![Launch workflow UI with artifact query override](/_static/images/artifacts/launch_workflow_artifact_query_override.png)
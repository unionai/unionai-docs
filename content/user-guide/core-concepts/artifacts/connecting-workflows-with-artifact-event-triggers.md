# Connecting workflows with artifact event triggers

In the following example, we define an upstream workflow and a downstream workflow, and define a [trigger](../launch-plans/reactive-workflows.md) in a launch plan to connect the two workflows via an [artifact event](../launch-plans/reactive-workflows.md#artifact-events).

## Imports

{@@ if byoc @@}
:::--note--
To use the example code on this page, you will need to add your `registry` to the `pandas_image` ImageSpec block.
:::
{@@ endif @@}

First we import the required packages:

```--rli-- https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/trigger_on_artifact.py
:caption: trigger_on_artifact.py
:language: python
:lines: 1-7
```


## Upstream artifact and workflow definition

Then we define an upstream artifact and a workflow that emits a new version of `UpstreamArtifact` when executed:

```--rli-- https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/trigger_on_artifact.py
:caption: trigger_on_artifact.py
:language: python
:lines: 13-31
```

## Artifact event definition

Next we define the artifact event that will link the upstream and downstream workflows together:

```--rli-- https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/trigger_on_artifact.py
:caption: trigger_on_artifact.py
:language: python
:lines: 34-36
```

## Downstream workflow definition

Then we define the downstream task and workflow that will be triggered when the upstream artifact is created:

```--rli-- https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/trigger_on_artifact.py
:caption: trigger_on_artifact.py
:language: python
:lines: 34-36
:lines: 39-46
```

## Launch plan with trigger definition

Finally we create a launch plan with a trigger set to an `OnArtifact` object to link the two workflows via the `Upstream` artifact. The trigger will initiate an execution of the downstream `downstream_wf` workflow upon the creation of a new version of the `Upstream` artifact.

```--rli-- https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/trigger_on_artifact.py
:caption: trigger_on_artifact.py
:language: python
:lines: 49-53
```

:::--note--
The `OnArtifact` object must be attached to a launch plan in order for the launch plan to be triggered by the creation of a new version of the artifact.
:::

## Full example code

Here is the full example code file:

```--rli-- https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/trigger_on_artifact.py
:caption: trigger_on_artifact.py
:language: python
```
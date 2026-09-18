---
title: Artifacts
description: Register task outputs and uploads as named, versioned artifacts, trigger runs on new versions, mount them into apps, and trace lineage.
icon: box-seam
weight: 4
variants: -flyte +union
---

# Artifacts

An artifact is a named, versioned reference to an object in storage. Instead of remembering which bucket path holds last week's training set, you register the output under a name, and downstream tasks, triggers, and apps refer to it by that name.

Your data path does not change. Files, directories, and dataframes are offloaded to object storage exactly as before. An artifact adds a name, a version, and a record of where it came from. Registering under the same name again creates a new version, and Union records which run produced each version and which tasks and apps consume it, so you can trace a deployed model back to the dataset it was trained on.

Any `flyte.io.File`, `flyte.io.Dir`, or `flyte.io.DataFrame` can become an artifact. The most common way is to wrap a task's return value:

```python
@env.task(produces_artifacts=True)
async def train() -> File:
    weights = await File.from_local("model.pt")
    return artifacts.new(weights, artifacts.Metadata(name="trained-model"))
```

{{< grid >}}

{{< link-card target="task-outputs" icon="box-seam" title="Task outputs as artifacts" >}}
Wrap a task's return value with `flyte.artifacts.new()` to register it as a named, versioned artifact with metadata and a model or data card.
{{< /link-card >}}

{{< link-card target="publish-artifacts" icon="cloud-upload" title="Publish your own artifacts" >}}
Upload existing datasets and model weights from anywhere with `Artifact.create` or `flyte create artifact`, recording where they came from.
{{< /link-card >}}

{{< link-card target="prefetch-models" icon="download" title="Prefetch Hugging Face models" >}}
Pull model weights from the Hugging Face Hub into your own storage as a model artifact, versioned by commit, with the model card attached.
{{< /link-card >}}

{{< link-card target="artifact-triggers" icon="lightning-charge" title="Trigger on new versions" >}}
Run a task automatically whenever a new version of an artifact lands, using `flyte.OnArtifact`. It fires no matter who published the version.
{{< /link-card >}}

{{< link-card target="artifacts-in-apps" icon="window" title="Use artifacts in apps" >}}
Mount model weights and datasets into serving apps with `flyte.app.ArtifactValue`, resolved and pinned at deploy time.
{{< /link-card >}}

{{< link-card target="lineage" icon="diagram-3" title="Automatic lineage tracking" >}}
Union records who produced each artifact version and which tasks, triggers, and apps depend on it, and shows the graph in the UI.
{{< /link-card >}}

{{< /grid >}}

## Related

{{< grid >}}

{{< link-card target="../tasks" icon="gear" title="Tasks" >}}
The unit of work that produces and consumes artifacts.
{{< /link-card >}}

{{< link-card target="../apps" icon="window" title="Apps" >}}
Long-running services that serve the models and datasets artifacts hold.
{{< /link-card >}}

{{< /grid >}}

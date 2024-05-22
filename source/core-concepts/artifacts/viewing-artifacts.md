# Viewing artifacts

## Artifacts list

[Artifacts](index) can be viewed in the Union console by navigating to the artifacts app in the left sidebar:

![Artifacts navigation](/_static/images/artifacts/artifacts_navigation.png)

![Artifacts overview](/_static/images/artifacts/artifacts_overview.png)

## Artifact view

Selecting a specific artifact from the artifact list will take you to that artifact's **Overview** page:

![Single artifact overview](/_static/images/artifacts/single_artifact_overview.png)

Here you can see relevant metadata about the artifact, including:
* Its version
* Its partitions
* The task or workflow that produced it
* Its creation time
* Its object store URI
* Code for accessing the artifact via [UnionRemote](../../development-cycle/unionremote)

You can also view the artifact's object structure, model card, and lineage graph.

### Artifact lineage graph

Once an artifact is materialized, you can view its lineage in the Union console, including the specific upstream task or workflow execution that created it, and any downstream workflows that consumed it. You can traverse the lineage graph by clicking between artifacts and inspecting any relevant workflow executions in order to understand and reproduce any step in the AI development process.

![Artifact lineage overview](/_static/images/artifacts/artifacts_lineage_overview.png)

To navigate through the lineage graph, you can click from artifact to artifact. Clicking the **timeseries-hashed** box in the image above will switch the scope such that the `timeseries-hashed` artifact is in focus. The lineage service then shows all artifacts that are one degree of separation from `timeseries-hashed`:

![Single artifact lineage detail](/_static/images/artifacts/single_artifact_lineage_detail.png)